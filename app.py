import pdf2image
import pytesseract
import phonenumbers
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def convert_pdf_to_images(pdf_file_path):
    print("Converting PDF to images...")
    return pdf2image.convert_from_path(pdf_file_path)

def ocr_images(images):
    print("Performing OCR on images...")
    extracted_text = ""
    for image in images:
        extracted_text += pytesseract.image_to_string(image)
        print("Extracted text from image: " + extracted_text)
    return extracted_text

def find_and_validate_phone_numbers(text):
    possible_numbers = phonenumbers.PhoneNumberMatcher(text, "US")
    valid_phone_numbers = []

    for number_match in possible_numbers:
        if phonenumbers.is_valid_number(number_match.number):
            valid_phone_numbers.append(phonenumbers.format_number(number_match.number, phonenumbers.PhoneNumberFormat.E164))

    return valid_phone_numbers

@app.post("/api/find_phone_numbers", response_model=List[str])
async def find_phone_numbers(file: UploadFile = File(...)):
    with open("temp.pdf", "wb") as f:
        f.write(await file.read())

    images = convert_pdf_to_images("temp.pdf")
    extracted_text = ocr_images(images)
    valid_phone_numbers = find_and_validate_phone_numbers(extracted_text)

    return valid_phone_numbers
