from flask import Flask
from flask import render_template, request

import config as cfg
import ibm_boto3
from ibm_botocore.client import Config
import requests
import json
app = Flask(__name__)

def transcription(data):
    cos = ibm_boto3.client("s3",
                        ibm_api_key_id=cfg.COS_API_KEY_ID,
                        ibm_service_instance_id=cfg.COS_RESOURCE_CRN,
	    ibm_auth_endpoint=cfg.COS_AUTH_ENDPOINT,
	    config=Config(signature_version="oauth"),
	    endpoint_url=cfg.COS_ENDPOINT
    )
    headers = {
        'Content-Type': 'audio/flac',
    }
    params = (
        ('word_alternatives_threshold', '0.9'),
        ('keywords', 'colorado,tornado,tornadoes'),
        ('keywords_threshold', '0.5'),
    )
    with open(data, 'wb') as test:
        cos.download_fileobj('buckettestestandard', data, test)
    data = open(data, 'rb').read()
    url = cfg.STTURL + '/v1/recognize'

    
        
    response = requests.post(url, headers=headers, params=params, data=data, auth=('apikey', cfg.STTAPIKEY))
    resp = json.loads(response.text)
    
    return str(resp['results'][0]['alternatives'][0]['transcript'])
        

        
    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    text = transcription(request.form['filename'])
    
    return render_template('index.html', text=text)

if __name__ == "__main__":
    app.run()