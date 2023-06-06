from flask import Flask, request, jsonify
import os
import PyPDF2

app = Flask(__name__)

UPLOAD_FOLDER = './pdf_path'
ALLOWED_EXTENSIONS = {'pdf'}

@app.route('/pdf-extract', methods=['POST'])
def pdf_text():

    file = request.files.get('file')
    filename = file.filename

    file.save(os.path.join(UPLOAD_FOLDER, filename))

    file_path = f'{UPLOAD_FOLDER}/{filename}'
    
    with open(file_path, 'rb') as pdf:
        pdf_extraido = PyPDF2.PdfReader(pdf)
        numero_paginas = len(pdf_extraido.pages)

        texto = ''
        for i in range(numero_paginas):
            page = pdf_extraido.pages[i]
            texto += page.extract_text()
    os.remove(file_path)
    resultado = {'result': texto}

    return jsonify(resultado)
    

    
if __name__ == '__main__':
    app.run(debug=True)