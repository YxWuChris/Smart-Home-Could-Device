from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time


loop = True;

def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    myMQTTClient.publish("myTopicPublish", "Chris Recived", 0)
    print("--------------\n\n")
    loop = False;

myMQTTClient = AWSIoTMQTTClient("Chris_Macbook")
myMQTTClient.configureEndpoint("a1g9fizbnjxy2u.iot.us-west-2.amazonaws.com", 443)
myMQTTClient.configureCredentials("/Users/yuxuanwu/Desktop/IoT/Amazon_Root_CA_1.pem", "/Users/yuxuanwu/Desktop/IoT/cf09431bee-private.pem.key", "/Users/yuxuanwu/Desktop/IoT/cf09431bee-certificate.pem.crt")
# For Websocket, we only need to configure
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  #
myMQTTClient.connect()
#myMQTTClient.publish("myTopic", "Chris IoT Test", 0)
myMQTTClient.subscribe("myTopicListen", 1, customCallback)

while loop:
	time.sleep(1)
