import os
import shutil
import logging
from typing import List

# Setup logging
logger = logging.getLogger(__name__)

class FileManager:
    """
    Handles local file system operations for resumes and processed data.
    Ensures directory structures exist before operations.
    """
    
    def __init__(self, base_dir: str = "data"):
        self.base_dir = base_dir
        self.resumes_dir = os.path.join(base_dir, "resumes")
        self.processed_dir = os.path.join(base_dir, "processed")
        self._ensure_dirs()

    def _ensure_dirs(self):
        """Creates required data directories if they do not exist."""
        for directory in [self.resumes_dir, self.processed_dir]:
            if not os.path.exists(directory):
                os.makedirs(directory)
                logger.info(f"Created directory: {directory}")

    def save_uploaded_file(self, uploaded_file) -> str:
        """
        Saves a Streamlit UploadedFile object to the local resumes directory.
        
        Args:
            uploaded_file: The file object from st.file_uploader
            
        Returns:
            str: The absolute path to the saved file.
        """
        file_path = os.path.join(self.resumes_dir, uploaded_file.name)
        try:
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            logger.info(f"Successfully saved file to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error saving file {uploaded_file.name}: {e}")
            raise IOError(f"Could not save uploaded file: {e}")

    def clear_resumes(self):
        """Deletes all files in the resumes directory to reset state."""
        for filename in os.listdir(self.resumes_dir):
            file_path = os.path.join(self.resumes_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                logger.error(f"Failed to delete {file_path}. Reason: {e}")

    def list_resumes(self) -> List[str]:
        """Returns a list of paths for all files in the resumes directory."""
        return [os.path.join(self.resumes_dir, f) for f in os.listdir(self.resumes_dir) 
                if os.path.isfile(os.path.join(self.resumes_dir, f))]

# Singleton instance for easy access
file_manager = FileManager()