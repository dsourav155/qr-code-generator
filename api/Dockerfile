# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/scr/app

# Copy the dependencies file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

#Run the Application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"] 