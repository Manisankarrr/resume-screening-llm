import re
import unicodedata

def clean_text(text: str) -> str:
    """
    Cleans raw text extracted from PDFs to improve LLM and Embedding performance.
    - Normalizes unicode characters.
    - Removes multiple newlines and extra spaces.
    - Strips control characters.
    """
    if not text:
        return ""

    # Normalize unicode (handles ligatures, weird quotes, etc.)
    text = unicodedata.normalize("NFKC", text)

    # Replace multiple newlines with a single newline
    text = re.sub(r'\n+', '\n', text)

    # Replace multiple spaces with a single space
    text = re.sub(r' +', ' ', text)

    # Remove non-printable control characters
    text = "".join(ch for ch in text if unicodedata.category(ch)[0] != "C")


    return text.strip()