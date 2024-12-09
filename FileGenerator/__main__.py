from . import resume_pdf_builder


if __name__ == "__main__":
    print("start")
    pdf_name = "BobSmithResume1.pdf"
    side_margin = 25
    r = resume_pdf_builder.ResumeBuilder(pdf_name, side_margin, "Accurate")
    r.build()
