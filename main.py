import PyPDF2 as p2


PDFfile = open('SME Leads.pdf', 'rb')
pdfread = p2.PdfFileReader(PDFfile)

x = pdfread.getPage(1)
print(x.extractText())

