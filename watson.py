#pip install --upgrade "ibm-watson>=4.1.0"  --- Ibm-watsonin asennus

import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Ylermi Assistantin apikey, url ja ID
apikey = "zAJZfCddImpTfg-dREhL--RUPiHidr9z_MMQ1IHivbiK"
url = "https://gateway-lon.watsonplatform.net/assistant/api"
assistant_id = "9455850f-8f26-4ea4-9424-38f25c3f4442"

authenticator = IAMAuthenticator(apikey)
assistant = AssistantV2(
    version="2019-02-28",
    authenticator=authenticator
)
assistant.set_service_url(url)
assistant.set_disable_ssl_verification(True)


#Luodaan sessio ja tallennetaan session_id
session = assistant.create_session(
    assistant_id = assistant_id
    
).get_result()

session = json.dumps(session, indent=2)

#session_id tallennettu sessionID-muuttujaan
sessionID = (json.loads(session)["session_id"])


#puhe = str(input("Talk to Watson\n")) -- Testausta

#Viesti assistantille
response = assistant.message(
    assistant_id=assistant_id,
    session_id=sessionID,
    input={
        'message_type': 'text',
        'text': puhe #Puhe-muuttuja korvataan Google speech to text ohjelman Outputilla
    }
).get_result()



#Vastauksen karsiminen tekstimuotoon
answer = (json.dumps(response, indent=2))
output = (json.loads(answer)["output"])

text = output['generic'][0]['text'] # Text-muuttujassa Watson assistantin vastaus
# print(text) -- Testausta
