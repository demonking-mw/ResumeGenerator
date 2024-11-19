# ResumeGenerator
A resume customization software that uses the job description to select appropriate items to fill a resume

STAGE1: COMPLETED

The resume builder is functional at this stage. run the following command to generate the resume to Download:
python -m FileGenerator.resume_pdf_builder

To use it: get your own openai api key and put it into a .env under FileGenerator like:
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

Adding items to sections are implemented in file_parse. sample code is commented out, uncomment to use. 

STAGE2:
- Implement frontend to make usage easy:
    - init page where user enters their own openai api key
    - modification page to make editing resume information easy
    - generator page for easy use
    - publish for free use as an app
- Improve backend:
    - write edit and remove function for items
    - write a display function that gives out all useful informations in a neat format
    - write function to edit specific attribute for some item
    - write cross compare function that compares the same attribute across different items

STAGE3+:
- Implement more advanced frontend
    - page for visually comparing attribute for different items
    - page to dynamically change attribute 
    - web version with database
    - publish for paid access 
- Implement more advanced backend:
    - option to sort items by specific order everytime resume is generated
    - a few more templates
        - for different styles of resume
        - allows more section options
    - implement company research
        - cultures of company
        - past hiring examples of company
        - aims to more accurately outline required traits/skills





.\venv\Scripts\Activate.ps1