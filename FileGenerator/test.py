import os
fn = "Informations/" + "Informations" + "/" + "SKILLS.csv"
abs_file_path = os.path.abspath(fn)
print(abs_file_path)
open(abs_file_path, "r")
