#Importing the regular expression library
import re

#Creating a regular expression patterns dictionarywith different patterns
patterns = {
    #email pattern that matches most common email formats such as user12@example.com
    "email_address": r"\b[A-Za-z0-9]+(?:[._%+-]?[A-Za-z0-9]+)*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    #url pattern that matches http and https URLs
    "urls": r"(https?:\/\/[^\s]+)",
    #phone number pattern that matches various formats including numbers in parantheses and with different separators such as hyphens,...
    "phone_numbers": r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})",
    #credit card pattern that matches 16-digit credit card numbers 
    "credit_card_numbers": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
    #currency pattern that matches dollar amounts with optional commas and decimal points
    "currency_amount": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
    #time pattern that matches 12-hour and 24-hour time formats
    "time": r"\b(?:(?:1[0-2]|0?[1-9]):(?:[0-5][0-9])\s?(?:AM|PM)|(?:[01]?[0-9]|2[0-3]):[0-5][0-9])\b",
    #html tag pattern that matches any HTML tags such as <p>,...
    "html_tags": r"<[^>]+>",
    #hashtag pattern that matches hashtags used in social media posts, news articles,...
    "hashtags": r"#\w+"
}
#Creating various functions to extract data based on the regex patterns created above
def extract_data(text: str, regex: str):
    return re.findall(regex, text)

def extract_email_address(text: str):
    return extract_data(text, patterns["email_address"])

def extract_urls(text: str):
    return extract_data(text, patterns["urls"])

def extract_phone_numbers(text: str):
    return extract_data(text, patterns["phone_numbers"])

def extract_credit_card_numbers(text: str):
    return extract_data(text, patterns["credit_card_numbers"])

def extract_currency_amount(text: str):
    return extract_data(text, patterns["currency_amount"])

def extract_time(text: str):
    return extract_data(text, patterns["time"])

def extract_html_tags(text: str):
    return extract_data(text, patterns["html_tags"])

def extract_hashtags(text: str):
    return extract_data(text, patterns["hashtags"])


# Testing our code by running this file directly
if __name__ == "__main__":
  
    
# Testing data with a random mix of valid and invalid examples for each pattern
    test_data = {
    "email_address": [
        "emma.smith@example.com",          
        "bob_2025@testmail.org",           
        "linda+newsletter@mydomain.co.uk",
        "user-xyz@company.info",           
        "ADMIN@EXAMPLE.NET",               
        "double..dot@invalid..com",      
        "no-at-symbol.com",                
        "missingdomain@.com"               
    ],
    "urls": [
        "https://newsite.com",            
        "https://blog.example.org",        
        "ftp://oldserver.net",             
        "http://wrongprotocol.com",        
        "https://invalidtld.abcdefgh",    
        "https://123abc.org/path/to/page",
        "https://subdomain.-site.com"      
    ],
    "phone_numbers": [
        "321-654-0987",                    
        "(456)789-0123",                   
        "+44 (123) 456-7890",             
        "5555555555",                     
        "123-45-6789",                      
        "phone123456",                       
        "(999)-888-7777"                  
    ],
    "credit_card_numbers": [
        "4321-8765-2109-6543",             
        "1111 2222 3333 4444",             
        "1234123412341234",                 
        "1234-5678-9012-345678",           
        "abcd-ijkl-mnop-qrst",             
        "9999 0000 1111 222"               
    ],
    "time": [
        "8:15 AM",                         
        "11:45 PM",                        
        "00:30",                             
        "18:20",                            
        "14:61",                            
        "25:00",                            
        "6:75",                            
        "12:99 PM"                           
    ],
    "html_tags": [
        "<section>",                        
        "</header>",                         
        "<img src='pic.jpg' alt='pic'/>",   
        "<script>console.log('hi')</script>",
        "<123invalid>",                       
        "<input type='text' disabled>",     
        "<!-- comment -->"                   
    ],
    "currency_amount": [
        "$250",                            
        "$19.95",                            
        "$23,456.78",                        
        "250",                               
        "$5000",                            
        "$34,56.78",                        
        "$12.345",                           
        "$1,000,000.00"                      
    ],
    "hashtags": [
        "#PythonRocks",                     
        "#100DaysOfCode",                    
        "#DataScience",                        
        "NoHashTagHere",                      
        "#WebDev",                             
        "#OpenAI",                             
        "#123Invalid!",                        
        "#Another_Tag"                          
    ]
}

 #Using join to combine all test data into a single string for testing   
test_string = " ".join(
test_data["email_address"] +
test_data["urls"] +
test_data["phone_numbers"] +
test_data["credit_card_numbers"] +
test_data["currency_amount"] +
test_data["time"] +
test_data["html_tags"]+
test_data["hashtags"]
)
#Printing the valid extracted results according to each pattern
print("Emails:", extract_email_address(test_string))
print("URLs:", extract_urls(test_string))
print("Phones:", extract_phone_numbers(test_string))
print("Credit Cards:", extract_credit_card_numbers(test_string))
print("Currency:", extract_currency_amount(test_string))
print("Time:", extract_time(test_string))
print("HTML Tags:", extract_html_tags(test_string))
print("Hashtags:", extract_hashtags(test_string))
