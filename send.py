from pubnub import Pubnub

pubnub=Pubnub(publish_key='pub-c-519554a2-0a6b-4154-8516-4b7f1b7ad3d5',subscribe_key='sub-c-f29517fc-0332-11e6-861b-02ee2ddab7fe')

def _callback(message):
	print(message)

def _error(message):
	print(message)
while(1):
	pubnub.publish('ch2','Hi from me',callback=_callback,error=_error)

