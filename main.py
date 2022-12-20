from flask import Flask, Response, redirect, Request,render_template
import sys
import logging
import requests
from oauth2client.service_account import ServiceAccountCredentials
#from apiclient.discovery import build
# good
from googleapiclient.discovery import build


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


## cookies
@app.route('/google',methods=['GET'])
def get_google_request():
    req = requests.get("https://www.google.com/")
    return req.cookies.get_dict() #"""<h1>Welcome</h1> """

@app.route('/GA',methods=['GET'])
def get_GA_request():
    req = requests.get("https://analytics.google.com/analytics/web/#/report-home/a250432838w344296954p280819955")
    return req.text #"""<h1>Welcome</h1> """

## jusqu'ici c'est ok


#### GET THE NUMBER OF VISITORS

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'myprojectdeta-18043a20e2d1.json'
VIEW_ID = 'UA-250432838-1' #You can find this in Google Analytics > Admin > Property > View > View Settings (VIEW ID)
#344309589

def initialize_analyticsreporting():
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics


def get_report(analytics):
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:pageviews'}],
          'dimensions': []
        }]
      }
  ).execute()


def get_visitors(response):
  visitors = 0 # in case there are no analytics available yet
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

    for row in report.get('data', {}).get('rows', []):
      dateRangeValues = row.get('metrics', [])

      for i, values in enumerate(dateRangeValues):
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          visitors = value

  return str(visitors)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/visitors')
def visitors():
  analytics = initialize_analyticsreporting()
  response = get_report(analytics)
  visitors = get_visitors(response)

  return render_template('visitors.html', visitors=str(visitors))

##########################

if __name__=='__main__':
    app.run(debug=True)

