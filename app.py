from flask import Flask, render_template, request, redirect, url_for
import os
from chatbot.agents import Chatbot

chatbot = Chatbot()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    query = request.form['query']
    if not query:
        return render_template('index.html', error='Please enter a question.')
    
    response = chatbot.handle_input(query)
    return render_template('index.html', query=query, response=response)

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', upload_error='No file found.')
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', upload_error='No selected file.')
    
    if file and allowed_file(file.filename):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        text = chatbot.handle_file_upload(filepath)
        return render_template('index.html', extracted_text="file upload completed successfully!")
    
    return render_template('index.html', upload_error='Invalid file type.')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'docx'}

if __name__ == '__main__':
    app.run(debug=True)
