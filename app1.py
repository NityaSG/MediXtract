from flask import Flask, request, render_template
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'"C:\Program Files\Tesseract-OCR\tesseract.exe"'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        image = Image.open(file.stream)
        ocr_text = pytesseract.image_to_string(image)
        return ocr_text

    return '''
    <!doctype html>
    <title>Upload an Image</title>
    <h1>Upload an image and get OCR text</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
