from . import style_info
from . import styles
#python -m ResumeGenerator.FileGenerator.test
def main():
    resume_style = styles.ALlStyles().resume_style_0
    print(resume_style.subsections["HEADING"].subsections["heading_name_font"].get_paragraph_style())

if __name__ == "__main__":
    main()