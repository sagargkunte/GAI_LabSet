import pdfplumber

with pdfplumber.open("yourPdf.pdf") as pdf:
    text = ""
    for pdf in pdf.pages:
        text += pdf.extract_text() + "\n"
        

while True:
    q = input("Enter query (type exit) : ").lower()
    if q == "exit":
        break
    found = False
    for line in text.split("\n"):
        if q in line.lower():
            print(line)
            found = True
            
    if not found:
            print("Not found!")
        
    print("-"*30)
