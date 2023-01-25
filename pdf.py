#This will print each sheet of a multi-page PDF into .PDF file per sheet.
#I used this to separate monthly paystub and annual W2 / 1099 for a Non-profit

from PyPDF2 import PdfFileWriter, PdfFileReader

inputfile = PdfFileReader(open("w2.pdf","rb"))

for i in range(inputfile.numPages):
    output = PdfFileWriter()
    output.addPage(inputfile.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
