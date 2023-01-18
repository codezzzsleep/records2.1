from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

print(pytesseract.image_to_string(Image.open('img.png')))

# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
#
# print(pytesseract.image_to_boxes(Image.open('test.png')))
#
# print(pytesseract.image_to_data(Image.open('test.png')))
#
# print(pytesseract.image_to_osd(Image.open('test.png')))
#
# print(pytesseract.image_to_string('test.png'))
#
# pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
#
# hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')
