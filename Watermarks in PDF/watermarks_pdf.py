from pikepdf import Pdf, Page, Rectangle

old_pdf = Pdf.open("Enter the path of the first Pdf file")
old_pdf_one = Pdf.open("Enter the path of the second Pdf file")

des_page = Page(old_pdf.pages[0])
sources_page = Page(old_pdf_one.pages[0])

des_page.add_overlay(sources_page, Rectangle(0,0,500,500))

old_pdf.save("new_pdf.pdf")