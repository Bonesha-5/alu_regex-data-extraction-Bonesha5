import re


def extract_emails(text):
    """Extracts email addresses from the given text."""
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)


def extract_urls(text):
    """Extracts URLs from the given text."""
    return re.findall(r"https?://[^\s]+", text)


def extract_phones(text):
    """Extracts phone numbers from the given text."""
    return re.findall(r"\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}", text)


def extract_currency(text):
    """Extracts currency amounts from the given text."""
    return re.findall(r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?", text)


# Example run
sample = "Contact me at u.kevine@alustudent.com or visit https://www.example.com. Price is $19.99. Call (079) 176-1041."
print("Emails:", extract_emails(sample))
print("URLs:", extract_urls(sample))
print("Phones:", extract_phones(sample))
print("Currency:", extract_currency(sample))
