import nltk
import sys

def download_nltk_data():
    """Download required NLTK data."""
    print("Downloading NLTK data...")
    try:
        nltk.download('punkt', quiet=True)
        print("Successfully downloaded NLTK data")
    except Exception as e:
        print(f"Error downloading NLTK data: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    download_nltk_data() 