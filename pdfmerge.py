from PyPDF2 import PdfMerger
from os import listdir
from os.path import isfile, join

mypath = b'F:\Unizeugs\Semester 6\GR\Skript'
pdfs  = [f for f in listdir(mypath) if isfile(join(mypath, f))]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
