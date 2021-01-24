import PyPDF2 as p2

PDFfile = open('hasnat_osman.pdf', 'rb')
pdfread = p2.PdfFileReader(PDFfile)
x = pdfread.getPage(0)
print(x.extractText())