from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import qrcode
import boto3
import os
from io import BytesIO
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Loading Environment variable
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add debug endpoint to check environment variables
@app.get("/debug-env/")
async def debug_env():
    return {
        "aws_access_key_exists": bool(os.getenv("AWS_ACCESS_KEY_ID")),
        "aws_secret_key_exists": bool(os.getenv("AWS_SECRET_ACCESS_KEY"))
    }

# Initialize S3 client with debug logging
try:
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )
    logger.info("S3 client initialized successfully")
except Exception as e:
    logger.error(f"S3 client initialization failed: {str(e)}")
    raise

bucket_name = 'qr-code-generator-dsourav155'

# Add test endpoint for S3 bucket access
@app.get("/test-bucket/")
async def test_bucket():
    try:
        response = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=1)
        return {"message": "Bucket access successful", "response": str(response)}
    except Exception as e:
        logger.error(f"Bucket access failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-qr/")
async def generate_qr(url: str):
    logger.info(f"Received request to generate QR code for URL: {url}")
    
    try:
        # Generate QR Code
        logger.info("Generating QR code")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        logger.info("QR code generated successfully")
        
        # Save QR Code to BytesIO
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        logger.info("QR code saved to BytesIO")

        # Generate safe filename
        safe_filename = url.replace('://', '_').replace('/', '_')
        file_name = f"qr_codes/{safe_filename}.png"
        logger.info(f"Generated filename: {file_name}")

        # Upload to S3
        logger.info("Attempting to upload to S3")
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=img_byte_arr,
            ContentType='image/png',
            ACL='public-read'
        )
        logger.info("S3 upload successful")
        
        # Generate the S3 URL
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        logger.info(f"Generated S3 URL: {s3_url}")
        return {"qr_code_url": s3_url}
    
    except Exception as e:
        logger.error(f"Error in generate_qr: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Add health check endpoint
@app.get("/health/")
async def health_check():
    return {"status": "healthy"}