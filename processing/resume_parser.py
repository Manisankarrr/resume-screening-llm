import fitz  # PyMuPDF
import logging
import io
from typing import Union

# Configure basic logging for production tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_source: Union[str, bytes, io.BytesIO]) -> str:
    """
    Extracts raw text from a PDF document.
    
    Args:
        pdf_source: Can be a file path (str), raw bytes (from Streamlit), 
                    or a BytesIO object.
                    
    Returns:
        str: The extracted text from all pages of the PDF.
        
    Raises:
        ValueError: If the input type is unsupported.
        RuntimeError: If PyMuPDF fails to read the document.
    """
    extracted_text = []
    doc = None
    
    try:
        # Handle different input types (Disk vs. In-Memory Streamlit uploads)
        if isinstance(pdf_source, str):
            logger.info(f"Opening PDF from path: {pdf_source}")
            doc = fitz.open(pdf_source)
        elif isinstance(pdf_source, (bytes, bytearray)):
            logger.info("Opening PDF from byte stream.")
            doc = fitz.open(stream=pdf_source, filetype="pdf")
        elif isinstance(pdf_source, io.BytesIO):
            logger.info("Opening PDF from BytesIO stream.")
            doc = fitz.open(stream=pdf_source.read(), filetype="pdf")
        else:
            raise ValueError("Unsupported pdf_source type. Must be str, bytes, or BytesIO.")

        # Iterate through pages and extract text
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            if text:
                extracted_text.append(text)
                
        # Join all pages with a newline separator
        final_text = "\n".join(extracted_text).strip()
        
        if not final_text:
            logger.warning("PDF was opened successfully, but no text was found. (Might be an image-based PDF)")
            
        return final_text

    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        raise RuntimeError(f"Failed to process PDF: {str(e)}") from e
        
    finally:
        # Ensure the document is closed to free up memory
        if doc is not None:
            doc.close()