# QR Code Generator

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
The QR Code Generator is a web application that allows users to generate QR codes for any URL. The application consists of a front-end built with Next.js and a back-end API built with FastAPI. The generated QR codes are stored in an AWS S3 bucket and can be accessed via a public URL.

## Features
- Generate QR codes for any URL.
- Store QR codes in AWS S3 for easy access and sharing.
- Responsive front-end interface built with Next.js.
- Secure API with CORS enabled for local testing.

## Architecture
- **Front-end**: Built with Next.js, React, and Tailwind CSS.
- **Back-end**: Built with FastAPI, using Python.
- **Storage**: AWS S3 for storing QR code images.

## Installation

### Prerequisites
- Node.js and npm
- Python 3.9
- AWS account with S3 access
- Docker

### Front-end Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/dsourav155/qr-code-generator.git
   cd qr-code-generator/front-end-nextjs
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

### Back-end Setup
1. Navigate to the API directory:
   ```bash
   cd qr-code-generator/api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the API server:
   ```bash
   uvicorn main:app --reload
   ```

## Usage
1. Open your browser and navigate to `http://localhost:3000`.
2. Enter a URL in the input field and click "Generate QR Code".
3. The generated QR code will be displayed and stored in your AWS S3 bucket.

## Configuration
- **AWS Credentials**: Store your AWS credentials in the `api/.env` file.
  ```env
  AWS_ACCESS_KEY=your_access_key
  AWS_SECRET_KEY=your_secret_key
  ```

- **S3 Bucket**: Update the `bucket_name` in `api/main.py` with your S3 bucket name.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or support, please contact [work.sourav155@gmail.com](mailto:work.sourav155@gmail.com).
