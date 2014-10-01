from pyPdf import PdfFileWriter, PdfFileReader
from pyPdf import *
import sys

fname = "PB44.pdf"

output = PdfFileWriter()

# Let's not forget the pdf properties
# Store the last one
item = output._objects.pop()
# delete the one we don't care about (send to the last one)
output._objects.pop()
# Create a new object for the Properties...
properties = pdf.DictionaryObject()
properties.update ({
  pdf.NameObject("/Title"): pdf.createStringObject(u"Nothing to see here"),
  pdf.NameObject("/Producer"): pdf.createStringObject(u"Python PDF Library - http://pybrary.net/pyPdf/"),
  pdf.NameObject("/Author"): pdf.createStringObject(u"Kenneth Wilcox"),
  pdf.NameObject("/Subject"): pdf.createStringObject(u"Headaches are fun"),
  pdf.NameObject("/Creator"): pdf.createStringObject(u"Ken's gen.py script"),
  pdf.NameObject("/Keywords"): pdf.createStringObject(u"what the hell - does this work")
  })
# Add It
output._addObject(properties)
# Add back the one we deleted first
output._addObject(item)

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

# output should be double address
print "Output Pages:", output.getNumPages()

#if output.getNumPages() == (address.numPages *2):
if output.getNumPages() > 0:
  outStream = file("output\\"+fname, "wb")
  output.write(outStream)
  outStream.close()
  print "Generation Complete"