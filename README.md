# Paho MQTT Client Example

## Overview
This is an MQTT client example project that showcases how you can use HiveMQ Cloud with the Eclipse Paho Python Client. The example project covers the basic MQTT functionality: Connecting MQTT clients to your HiveMQ Cloud cluster, subscribing to topics and publishing data (sending and receiving messages using the MQTT protocol).

The Eclipse Paho project provides open source, mainly client side, implementations of MQTT and MQTT-SN in a variety of programming languages.
The Python client used here supports MQTT v3.1, v3.1.1 and v5 on Python 2.7.9+ or 3.5+.
You can find documentation for this client library here: https://www.hivemq.com/blog/mqtt-client-library-paho-python/.

This example repository is easily and clearly structured, so you can start quickly:
This readme file is your starting point. Here we will describe what you have to do step-by-step to get started with this example.
[``simple_example.py``](simple_example.py) is a simple implementation that demonstrates the core functionality of an MQTT Client.
The files [``separate_publisher.py``](separate_publisher.py) and [``separate_subscriber.py``](separate_subscriber.py) are meant to be run independently. 
In comparison to the simple implementation, these two files show the functions of publishing and subscribing separately. 
Follow the instructions in the following paragraphs to get started yourself.


## HiveMQ Cloud
[HiveMQ](https://www.hivemq.com/) is the industry leader for enterprise-ready, beautifully scalable, large-scale IoT deployments with MQTT. We help companies connect things to the Internet. Our MQTT-based messaging platform ensures fast, reliable, and secure movement of data to and from connected IoT devices for companies around the world. HiveMQ Cloud is our fully-managed, cloud-native IoT messaging platform that makes trustworthy and scalable IoT device connectivity simple. You can learn more about HiveMQ Cloud on our [website](https://www.hivemq.com/mqtt-cloud-broker/), [documentation](https://www.hivemq.com/docs/hivemq-cloud/introduction.html)  and our [blog posts](https://www.hivemq.com/tags/cloud/).

## Getting started
[By signing up](https://console.hivemq.cloud) for HiveMQ Cloud you will automatically get access to a HiveMQ Cloud Basic cluster. HiveMQ Cloud Basic is our smallest package that allows you to connect up to 100 MQTT clients for free and test the full MQTT functionality. 

The [HiveMQ Cloud Quick Start Guide](https://www.hivemq.com/docs/hivemq-cloud/introduction.html#guide) gives you step-by-step instructions on how to set up your HiveMQ Cloud account, create clusters, and connect MQTT clients.


### Prerequisites 
After signing up, you have a running HiveMQ Cloud cluster, that you can use in this example.
Now clone this repository into your local IDE.

For using the code examples, you need to install [paho mqtt for python](https://www.eclipse.org/paho/index.php?page=clients/python/index.php).
Use the provided requirements file to get the same version for paho-mqtt, that we have used for this example.
```sh
pip install -r requirements.txt
```

### Broker credentials
To define the HiveMQ Cloud cluster which should be targeted, you need to fill the placeholders in the code with your host name, username and password.
The <b>host name</b> can be found in the <b>Details</b> section of the <b>Overview</b> tab of your cluster.
![cluster overview](/img/hivemq-cloud-cluster-overview.png)

After the cluster is created, add a set of credentials that you can use in this example or future implementations.
Use any secure username and password you desire.
The <b>username</b> and <b>password</b> are the values used as <b>Client Credentials</b> that you just created.
![credentials](/img/hivemq-cloud-credentials.png)


### Code Examples
This example project covers the core functionality of an MQTT client interacting with HiveMQ Cloud.
To securely connect the MQTT client with HiveMQ Cloud you need to enable TLS.
Use your username and password, to authenticate your MQTT client at HiveMQ Cloud.
To connect the client, use the port 8883 that is standard for secure MQTT communication. 
```python
# enable TLS
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("<your_username>", "<your_password>")
# connect to HiveMQ Cloud on port 8883
client.connect("<your_host>", 8883)
```

The code located inside [``simple_example.py``](simple_example.py) connects to the configured HiveMQ Cloud Broker in a simple way. 
This is a ready-set example that can simply be run after inputting your credentials.

The code first subscribes to the topic filter "encyclopedia/#".  
That means the MQTT client receives all messages that are published to this [topic filter](https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices/).
The so-called wildcard ("#") in the topic filter includes all topics that begin with "encyclopedia/".
The ``on_subscribe`` callback acts as a reassurance that the subscription worked.
Then the code publishes a message and prints it to the terminal, when it is received.
It prints the message, because of the ``on_message`` callback, that gets triggered when a message comes in.

```python
# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("encyclopedia/#", qos=1)

# a single publish, this can also be done in loops, etc.
client.publish("encyclopedia/temperature", payload="hot", qos=1)
```

Use [``separate_publisher.py``](separate_publisher.py) and [``separate_subscriber.py``](separate_subscriber.py) as independent scripts to run on two different devices.
They use the same subscribe-publish functionality, but separate them into two different files.
You can, for example, run the subscriber on your desktop pc and the publisher on a DIY thermometer, that would publish the temperature constantly.
The only prerequisite is that both devices have an internet connection, but they do not need to be connected to one another.



## Learn more

If you want to learn more about MQTT, visit the [MQTT Essentials](https://www.hivemq.com/mqtt-essentials/) guide, that explains the core of MQTT concepts, its features and other essential information. To learn more about the Eclipse Paho Python Client, visit their [official website](https://www.eclipse.org/paho/index.php?page=clients/python/index.php). For a lot more and detailed examples look at the [paho.mqtt.python github](https://github.com/eclipse/paho.mqtt.python). You can also find extensive documentation there.

## Contributing

Please see our [contributing guidelines](./CONTRIBUTING.adoc) and [code of conduct](./code-of-conduct.md).

## License

[Apache 2.0](./LICENSE).

