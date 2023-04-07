# Import necessary modules and libraries
import pdf2image
import pytesseract
import phonenumbers
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Create a FastAPI instance
app = FastAPI()

# Add middleware to allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define function to convert a PDF file to a list of images
def convert_pdf_to_images(pdf_file_path):
    # Print status message
    print("Converting PDF to images...")
    # Use pdf2image module to convert PDF to list of images
    return pdf2image.convert_from_path(pdf_file_path)

# Define function to perform OCR on a list of images and extract text
def ocr_images(images):
    # Print status message
    print("Performing OCR on images...")
    # Initialize empty string to store extracted text
    extracted_text = ""
    # Loop through images in list and extract text using pytesseract module
    for image in images:
        extracted_text += pytesseract.image_to_string(image)
        # Print extracted text for debugging purposes
        print("Extracted text from image: " + extracted_text)
    # Return the extracted text
    return extracted_text

# Define function to find and validate phone numbers in a string of text
def find_and_validate_phone_numbers(text):
    # Use phonenumbers module to find possible phone numbers in text
    possible_numbers = phonenumbers.PhoneNumberMatcher(text, "US")
    # Initialize empty list to store valid phone numbers
    valid_phone_numbers = []
    # Loop through possible phone number matches and validate them using phonenumbers module
    for number_match in possible_numbers:
        if phonenumbers.is_valid_number(number_match.number):
            # If the phone number is valid, add it to the list of valid phone numbers
            valid_phone_numbers.append(phonenumbers.format_number(number_match.number, phonenumbers.PhoneNumberFormat.E164))
    # Return the list of valid phone numbers
    return valid_phone_numbers

# Define API endpoint to find and return phone numbers in a PDF file uploaded by user
@app.post("/api/find_phone_numbers", response_model=List[str])
async def find_phone_numbers(file: UploadFile = File(...)):
    # Save the uploaded PDF file to disk as "temp.pdf"
    with open("temp.pdf", "wb") as f:
        f.write(await file.read())
    # Convert the PDF file to a list of images using convert_pdf_to_images function
    images = convert_pdf_to_images("temp.pdf")
    # Perform OCR on the images and extract text using ocr_images function
    extracted_text = ocr_images(images)
    # Find and validate phone numbers in the extracted text using find_and_validate_phone_numbers function
    valid_phone_numbers = find_and_validate_phone_numbers(extracted_text)
    # Return the list of valid phone numbers
    return valid_phone_numbers
