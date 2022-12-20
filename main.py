from flask import Flask

app = Flask(__name__)

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
    return prefix_google + "Hello World lab2 from ANAIS BELLIA"

@app.route('/Logger',methods=['GET'])
def logger():
    page="""
    <script>console.log('aaa')</script>"""
    return "hfgvhjbggh" + page

