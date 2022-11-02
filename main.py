from pyngrok import ngrok
import paho.mqtt.client as mqtt
import time
mqttc=mqtt.Client()
mqttc.connect("broker.emqx.io", 8083, 60)                                  # Mqtt broker
ngrok.set_auth_token("**")      # Enter the registered Auth_Token
public_url = ngrok.connect("**")                       # tunnel to host:port instead of localhost

print(public_url)                                                              # Displaying the ngrok_tunnel url 

while True:
    # time.sleep(0.04)
    mqttc.publish("testtopic1",public_url)                                      # Publishing the created URL to "test_mqqt1" Topic 
    mqttc.loop(0.001)
    time.sleep(120) # send mqtt message every 2 minutes
