**Regular Expression Data Extraction**

Extracts data from text using Python regex. Supports emails, URLs, phone numbers, credit cards, time, HTML tags, hashtags, and currency amounts.

Features

Extracts common patterns from text.
Includes test data for validation.
Easy to modify or extend regex patterns.
Patterns Used:
Email Address: \b[A-Za-z0-9]+(?:[._%+-]?[A-Za-z0-9]+)*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b
URLs: (https?:\/\/[^\s]+)
Phone Numbers: (\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})
Credit Card Numbers: \b(?:\d{4}[-\s]?){3}\d{4}\b
Currency Amounts: \$\d{1,3}(?:,\d{3})*(?:\.\d{2})?
Time: \b(?:(?:1[0-2]|0?[1-9]):(?:[0-5][0-9])\s?(?:AM|PM)|(?:[01]?[0-9]|2[0-3]):[0-5][0-9])\b
HTML Tags: <[^>]+>
Hashtags: #\w+
Usage
git clone https://github.com/Bonesha-5/alu_regex-data-extraction-EKIRABO.git
cd alu_regex-data-extraction-EKIRABO
python regex.py or just run the file normally.
