#
# Copyright 2021 HiveMQ GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

# create a set of 2 test messages that will be published at the same time
msgs = [{'topic': "paho/test/multiple", 'payload': "test 1"}, ("paho/test/multiple", "test 2", 0, False)]

# use TLS for secure connection with HiveMQ Cloud
sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

# put in your cluster credentials and hostname
auth = {'username': "<username>", 'password': "<password>"}
publish.multiple(msgs, hostname="<hostname>", port=8883, auth=auth,
                 tls=sslSettings, protocol=paho.MQTTv31)
