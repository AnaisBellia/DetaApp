from flask import Flask, render_template
import requests
import logging
app = Flask(__name__)

'''
@app.route('/', methods=["GET"])
def hello_world():
    prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=UA-250432838-1"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', ' UA-250432838-1');
</script>
 """
    return prefix_google + "Hello World from ANAIS BELLIA"
'''


@app.route('/Logger',methods=['GET'])
def logger():
    page="""
    <script> console.log('message de la console ANAIS BELLIA') </script>"""
    return "voir console" + page

### Prints a log on python
logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)
#log.warning('I print to stderr by default')
print('hello world in python console from Anaïs Bellia')

## textbox
@app.route('/')
def home():
    return render_template('base.html')

@app.route('/',methods=['POST'])
def login():
    text=requests.form['text']
    processedtext=text.upper()
    return processedtext #"""<h1>Welcome</h1> """

@app.route('/google',methods=['GET'])
def get_google_request():
    req = requests.get("https://www.google.com/")
    return req.cookies.get_dict() #"""<h1>Welcome</h1> """

@app.route('/GA',methods=['GET'])
def get_GA_request():
    req = requests.get("https://analytics.google.com/analytics/web/#/report-home/a250432838w344296954p280819955")
    return req.text #"""<h1>Welcome</h1> """


if __name__=='__main__':
    app.run(debug=True)

