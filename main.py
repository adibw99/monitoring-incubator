from pyngrok import ngrok
import paho.mqtt.client as mqtt
import time
mqttc=mqtt.Client()
mqttc.connect("broker.emqx.io", 8083, 60)                                  # Mqtt broker
ngrok.set_auth_token("1g64Fo2JUcdnAFEj5IYVHpFrw9q_4CVPj2tEu1m2qewp3b8E4")      # Enter the registered Auth_Token
public_url = ngrok.connect("192.168.137.139")                       # tunnel to host:port instead of localhost

print(public_url)                                                              # Displaying the ngrok_tunnel url 

while True:
    # time.sleep(0.04)
    mqttc.publish("testtopic1",public_url)                                      # Publishing the created URL to "test_mqqt1" Topic 
    mqttc.loop(0.001)
    time.sleep(120) # send mqtt message every 2 minutes