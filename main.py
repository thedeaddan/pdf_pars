import fitz
with fitz.open("/driveone/excel/file.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

text = text.split("\n")

index = text.index("3-2 ис")

message = f"""{text[index+1]} {text[index+2]} {text[index+3]}
{text[index+4]} {text[index+5]} {text[index+6]}
{text[index+7]} {text[index+8]} {text[index+9]}
{text[index+10]} {text[index+11]} {text[index+12]}
"""

print(message)
