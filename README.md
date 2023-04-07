# PDF Phone Number Extractor

This is a Python application that extracts phone numbers from a PDF file uploaded by a user. The application uses OCR (Optical Character Recognition) to extract text from images of each page in the PDF file, and then uses the Phonenumbers library to find and validate phone numbers in the extracted text.

## **Installation**

### **Running with Docker**

To run this application using Docker, you'll need to have Docker installed on your system. You can download Docker from the official website: **[https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)**

Once you have Docker installed, you can build a Docker image of the application using the provided Dockerfile. In a terminal, navigate to the directory containing the Dockerfile and run the following command:

```
docker build -t pdf-phone-number-extractor .
```

This will build a Docker image named **`pdf-phone-number-extractor`** using the Dockerfile. Once the image is built, you can run the application in a Docker container using the following command:

```
docker run -p 8000:8000 pdf-phone-number-extractor
```

This will start the application and bind it to port 8000 on your host machine. You can access the application in your web browser at **[http://localhost:8000/](http://localhost:8000/)**.

### **Running Locally**

To run this application locally, you'll need to have Python 3.6 or higher installed on your system. You can download Python from the official website: **[https://www.python.org/downloads/](https://www.python.org/downloads/)**

Once you have Python installed, you can install the required Python packages using the following command:

```
pip install -r requirements.txt
```

This will install the following packages:

- pdf2image
- pytesseract
- phonenumbers
- fastapi
- uvicorn
- python-multipart

To start the application, run the following command:

```
uvicorn app:app --host 0.0.0.0 --port 8000
```

This will start the application and bind it to port 8000 on your host machine. You can access the application in your web browser at **[http://localhost:8000](http://localhost:8000/)**.

### **Running on Render**

To run this application on Render, you'll need to have a Render account. You can sign up for a free account at https://render.com/signup

Once you have a Render account, you can deploy the application using the following steps:

Fork this repository and clone the forked repository to your local machine.
Create a new Render service for the repository.
In the deployment settings, choose the "Render-managed Dockerfile" option and specify Dockerfile as the path to the Dockerfile.
Wait for the build to complete and the service to start.
Access the application at the URL provided by Render.
That's it! You're now running this application on Render.

## **Usage**

Once the application is running, you can access it in your web browser at **[http://localhost:8000](http://localhost:8000/)**. You'll see a simple web form where you can upload a PDF file.

After uploading a PDF file, the application will extract text from each page in the PDF file using OCR, and then find and validate any phone numbers in the extracted text. The application will return a list of valid phone numbers in E.164 format.