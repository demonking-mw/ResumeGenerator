from ResumeGenerator.FileGenerator.resume_pdf_builder import ResumeBuilder


if __name__ == "__main__":
    print("start")
    pdf_name = "BobSmithResume1.pdf"
    side_margin = 25
    r = ResumeBuilder(pdf_name, side_margin, "Accurate")
    r.build()
