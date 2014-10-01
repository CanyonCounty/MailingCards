from pyPdf import PdfFileWriter, PdfFileReader
import sys

fname = "PB44.pdf"

output = PdfFileWriter()
address = PdfFileReader(file("input\\address\\"+fname, "rb"))
location = PdfFileReader(file("input\\location\\"+fname, "rb"))

print "Location Pages:", location.numPages
print "Address Pages:", address.numPages

if location.numPages > 1 :
  print "Location has more than 1 page, exiting..."
  sys.exit()
  
page = location.getPage(0)
for i in xrange(address.numPages):
  #print ".",
  output.addPage(address.getPage(i))
  output.addPage(page)
#  if i > 4:
#    break
#print ""

# output should be double address
print "Output Pages:", output.getNumPages()

#if output.getNumPages() == (address.numPages *2):
if output.getNumPages() > 0:
  outStream = file("output\\"+fname, "wb")
  output.write(outStream)
  outStream.close()
  print "Generation Complete"