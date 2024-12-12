import pytesseract  # For OCR
from pdf2image import convert_from_path  # To convert PDF pages to images
import re  # For regular expressions
from nltk.tokenize import word_tokenize  # For basic NLP tokenization

def parse_document(file_path):
    try:
        # Converting PDF to image(s) if the input is a PDF
        pages = convert_from_path(file_path)
        
        Extracting text  using OCR
        full_text = ""
        for page in pages:
            text = pytesseract.image_to_string(page)
            full_text += text

        # Tokenizing  and processing  the extracted text
        tokens = word_tokenize(full_text)

        # Extracting  key terms and populating fields
        extracted_data = {}
        extracted_data['case_id'] = extract_text(full_text, "Case ID")
        extracted_data['debtor_name'] = extract_text(full_text, "Debtor Name")
        extracted_data['amount_due'] = extract_text(full_text, "Amount Due")

        if not all(extracted_data.values()):
            raise ValueError("Document parsing failed. Some data fields are missing.")

       
        return extracted_data

    except Exception as e:
        raise RuntimeError(f"Error during document parsing: {e}")

def extract_text(document, field_name):
    
    """
        Searches the document text for a specific field and extracts its value.
        :param document: Text of the document
        :param field_name: The field name to search for
        :return: Extracted value for the field or None if not found
        """
    try:
        # Using regex to find the value after the field name
        pattern = rf"{field_name}:\s*(.+)"
        match = re.search(pattern, document)
        if match:
            return match.group(1).strip()
    except Exception as e:
        print(f"Error extracting field {field_name}: {e}")
    return None

if __name__ == "__main__":
    file_path = "sample_legal_document.pdf"
    try:
        extracted_fields = parse_document(file_path)
        print("Extracted Data:", extracted_fields)
    except Exception as e:
        print(e)
 #need more work