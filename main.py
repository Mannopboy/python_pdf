from pypdf import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# packet = io.BytesIO()
# can = canvas.Canvas(packet, pagesize=letter)
# can.setFillColorRGB(255, 255, 255)
# can.drawString(300, 660, "Nigga")
# can.rotate(45)
# can.save()
#
# packet.seek(0)
#
# new_pdf = PdfReader(packet)
#
# existing_pdf = PdfReader(open("MMR.pdf", "rb"))
# output = PdfWriter()
# page = existing_pdf.pages[0]
# page.merge_page(new_pdf.pages[0])
# output.add_page(page)
# output_stream = open(f"destination.pdf", "wb")
# output.write(output_stream)
# output_stream.close()


data = open('404.txt', 'x')
data.write('He nigga')
print(data)
