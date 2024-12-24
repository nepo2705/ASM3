from flask import Flask, render_template,request
import os
print("Template folder path:", os.path.join(os.getcwd(), 'templates'))
app = Flask(__name__)
template_folder=os.path.join(os.getcwd(), 'templates')
@app.route('/')
def index():
    # Connecting to a template (html file)
    return render_template('index.html')

@app.route('/signup')
def signup():
    
    return render_template('signup.html')

@app.route('/thankyou')
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')
    
    return render_template('thankyou.html', first =first, last = last)

if __name__ == '__main__':
    app.run(debug=True)