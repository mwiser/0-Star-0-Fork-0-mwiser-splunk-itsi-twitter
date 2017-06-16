import sys
import json
import platform
import subprocess
import requests
from splunk.clilib.bundle_paths import make_splunkhome_path

sys.path.append(make_splunkhome_path(['etc', 'apps', 'SA-ITOA', 'lib']))

from ITOA.fix_appserver_import import FixAppserverImports
from ITOA.setup_logging import setup_logging
from itsi.event_management.sdk.eventing import Event
from itsi.event_management.sdk.custom_event_action_base import CustomEventActionBase

class Email(CustomEventActionBase):
    def execute(self):
     
        self.logger.debug('Received settings from splunkd=`%s`',json.dumps(self.settings))
        self.logger.info('Executed action. Processed events count=`%s`.', count)
  
if __name__ == "__main__":
    logger = setup_logging("itsi_event_management.log", "itsi.event_action.tweet")
    logger.info("Starting of Tweet")
    if len(sys.argv) > 1 and sys.argv[1] == '--execute':
        input_params = sys.stdin.read()
        logger.info(input_params)
        payload = json.loads(input_params)
        logger.info(payload)
        event_id = payload['result']['event_id']
        session_key = payload['session_key'] 
        logger.info("Session Key:"+session_key+" event id:"+event_id)
	description=payload['result']['title']
	description = description + " Get Details: http://bb9c6bdd.ngrok.io/en-US/app/itsi/itsi_event_management"
	urlstring = "https://afky8ff8x9.execute-api.us-east-1.amazonaws.com/prod"
	payload = {"tweet": description}
	r = requests.post(urlstring, data=json.dumps(payload))
	event = Event(session_key, logger)
        event.create_comment(event_id, "Tweet has been created")



