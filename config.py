import os
import json
coscred = os.environ.get('COS_SERVICES')

cos_cred = json.loads(coscred)
sttcred = os.environ.get('STT_SERVICES')
stt_cred = json.loads(sttcred) 


COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID = cos_cred['apikey']
COS_AUTH_ENDPOINT = "https://iam.cloud.ibm.com/identity/token"
COS_RESOURCE_CRN = cos_cred['resource_instance_id']


STTAPIKEY = stt_cred['apikey']
STTURL = stt_cred['url']