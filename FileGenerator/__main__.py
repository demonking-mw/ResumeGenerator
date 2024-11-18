
from . import file_parse
from . import resume_pdf_builder

if __name__ == "__main__":
    # print("start")
    # pdf_name = "BobSmithResume1.pdf"
    # side_margin = 25
    # r = resume_pdf_builder.ResumeBuilder(pdf_name, side_margin, "Accurate")
    # r.build()
    f = file_parse.FileAccMod()
    sf = [["PROGRAMMING", 1], ["COOKING", 2]]
    f.mod_by_header_ss(
        sf,
        "Strong",
        "PROJECTS.csv",
        "Cheese",
        "1234",
        ["see, now I can add stuff to the resume", "nah I want more shit"],
    )
