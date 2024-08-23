# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/' , methods=['POST'])
def index():
    mail = request.form.get('email')
    text_area = request.form.get('text')

    with open('comment.txt', 'a') as f:
        f.write(f'''--------------NEW COMMENT-------------
                \n Email: {mail}
                \n Comment: {text_area} \n\n ''')

    return render_template('index.html') 


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_html = request.form.get('button_html')
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_db = request.form.get('button_db')
    return render_template('index.html', 
                           button_python=button_python,
                           button_html = button_html,
                           button_discord = button_discord,
                           button_db = button_db)

            

if __name__ == "__main__":
    app.run(debug=True)
