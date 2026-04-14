from pypdf import PdfReader

def extract_text(pdf_doc): # to extract text from the pdf document
    try:
        
        pdf = PdfReader(pdf_doc)
        
        raw_text = ''
        for index, page in enumerate(pdf.pages): # to extract text from each page of the pdf document
            text = page.extract_text() # to extract text from the page
            if text: # to check if the text is not empty and then concatenate it to the raw_text variable
                raw_text += text    
        return raw_text
    except Exception as e: # to handle any exceptions that may occur during the text extraction process
        return f"An error occurred while extracting text:"