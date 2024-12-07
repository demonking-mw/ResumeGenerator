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
    - init page where user enters their own openai api key -Optional
    - modification page to make editing resume information easy -V
    - generator page for easy use -V
    - initial testing of the app and the backend
    - publish for free use as an app
- Improve backend:
    - write edit and remove function for items -V
    - write a display function that gives out all useful informations in a neat format -V
    - write function to edit specific attribute for some item -V

STAGE3+:
- Implement more advanced frontend
    - write cross compare function that compares the same attribute across different items
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


Project Journal 1:
- Date: 2024-12-06.
- Current state: almost completing stage 2 objectives, in the process of testing and getting the basic app ready for usage.

- Progress so far:
The project went mostly well so far. Lots of the envisioned objectives are within reach if not already a reality. The builder works. It is not too pretty, but it gets the basic job done. Probably will rework it in the future. The frontend is what I envisioned but not really what I hoped. PYQT is quite annoying to work with. I would rather use some sort of html.Annoyance aside, it saves a lot of time from trying to fit front end to the back end since they are the same language. Git has been going well. Attempting to use git despite working on the project alone is a really good idea, since it grants experience and make progress very visible. It also gives the satisfaction bonus running git push at the end of a day.
On a more technical side, I have been trying to fix some design mistakes such as using WET coding and some other naming silliness in the past. This is my first project, so it is what it is. Bugs have yet to show themselves fully, and basic tests have gone decently well. 

- Good things
There are quite a few good things so far. Firstly, the decision to approach the project with a simple implementation really keep the project going. The shallower learning curve and the lack of really difficulty subtasks allows the project to go this far without ragequits. In the backend, some design choices are decently made. The idea of a standard section is really a life saver although it did not appear so at the beginning. Using git and allowing myself to see what have changed is also pretty cool, although i did not use the feature too often. Lastly, the decision to use PYQT instead of some crazy frontend stuff allows a funcitonal frontend for testing to be built quickly. It is not too easy to use in terms of the modification tab, but the generation tab is good enough. It will suffice for now because the usage of the application is generation heavy.

- Shitty things
There are too many. Starting with the coding decision itself. Modular and good-looking code is the opposite of this project. I went lazy on too many formatting and data decisions. They seemed to save time, but they are and will cause me exponentially more effort to get right. Firstly, the sections have not one, not two, but THREE types. The more I enjoy having a standard section, the more i regret not making it more powerful to include everything. the extra 50 line of code can probably cut so much effort on file parse and frontend. The frontend itself also got similar problems. Much of the code is super similar and can be reduced by one section builder. The ones written later is better, but much improvement can be made. Moving out toward the file structure itself. I started with a singular file. That is sad. Clearly parse_file and fonts are basically a class for helpers, why are they in the same level as build??? Another bad decision is using reportlab. Latex is much better at making pdf and has similar learning curves. Now I have to try to migrate while dragging the entire sloppy backend with me.

- Lessons
1. Actually plan a little. 
Take a moment to think of the less significant details. File structure, naming convention, data structure, expandability of the backend, combining as many similarities as humanly possible, etc
2. Do not be lazy on structures.
Making 3 sections instead of 1 will surely save a ton of time since the standard section structure need far less work. However, any upgrade in the future will be triple the work. Live example in file_parse, where code must be written almost 3 times to do the same thing to each section.
3. Do stage 1 with future in mind. 
Surely choosing an easy out can be good for starting a project. If that have to be then sure. Something to keep in mind is that stage one is, after all, stage one only. The entire project will likely not be ending at stage one. The worst thing to do in stage one is to make structure and design choices exclusively for stage one. Define each file and its purpose accurately. Split up the program in mini chunks. Make data definition and file structure future proof. These will all make version 2+ much easier.
4. Type hint is too op in the future to miss
Dont just write list for the creepy 5d list a function returns. Do as much typehint as possible, and explain the rest in comment. It will save many WTF moments.

- Future
I will get stage 2 done and done and done soon. I will then decide between two options: to change the file structure and design choices for the convinience of stage 3, or to rewrite the entire project with the previous ideas in mind. Then I will advance into the third stage.

.\venv\Scripts\Activate.ps1