#!/bin/python3

import PyPDF2

# Print welcome message
print('*' * 50)
print("Welcome to PDFMERGER 1.1 Created by Rajesh Kumar")
print('*' * 50)

# Prompt user to enter PDF filenames
first_pdf = input('Enter the filename of the first PDF: ')
second_pdf = input('Enter the filename of the second PDF: ')
merged_pdf = input('Enter the filename for the merged PDF: ')

# Create a list of PDF filenames to merge
pdf_files = [first_pdf, second_pdf]

# Create a PDF merger object
merger = PyPDF2.PdfFileMerger()

# Loop through each PDF file and append it to the merger object
for filename in pdf_files:
    # Use 'with' statement to ensure proper handling of the file
    # The 'rb' mode is used to open the file in binary mode for reading
    with open(filename, 'rb') as pdf_file:
        # Create a PDF reader object to read the contents of the file
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        # Append the contents of the file to the PDF merger object
        merger.append(pdf_reader)

# Write the merged PDF to a file
# The 'wb' mode is used to open the file in binary mode for writing
with open(merged_pdf, 'wb') as output:
    # Write the contents of the merger object to the output file
    merger.write(output)

# Print success message
print('-' * 50)
print(f'{first_pdf} and {second_pdf} have been merged into {merged_pdf}.')
print('-' * 50)
