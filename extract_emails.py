import re

# File paths
input_file = 'sample.txt'
output_file = 'extracted_emails.txt'

# Read from the input file
with open(input_file, 'r') as file:
    text = file.read()

# Extract emails using regular expression
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

# Write found emails to the output file
with open(output_file, 'w') as file:
    for email in emails:
        file.write(email + '\n')

print(f"{len(emails)} email(s) extracted and saved to '{output_file}'")
