# Import the libraries
import paho.mqtt.client as mqtt
import time
import random

# Define the broker address and the topic
broker = "broker.hivemq.com"
topic = "city/temperature"

# Create a client object and connect to the broker
client = mqtt.Client("Temperature_Sensor")
client.connect(broker)

# Loop forever and publish random temperature values every second
while True:
    # Generate a random temperature value between 10 and 40 degrees Celsius
    temperature = random.randint(10, 40)
    # Convert the temperature to a string and publish it to the topic
    client.publish(topic, str(temperature))
    # Print the temperature value to the console
    print(f"Published {temperature} to {topic}")
    # Wait for one second
    time.sleep(1)
