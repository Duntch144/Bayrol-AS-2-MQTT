# Bayrol-AS-2-MQTT
Publish websocket Bayrol website data to Local MQTT

This Python script intend to continuously collect websocket data from Bayrol pool access website and publish them on a local brocker. It is valid for Automatic Salt system.
It uses Paho as a bridge to collect data then publish the same data on the local MQTT brocker.

Websocket login can be retreived from the Bayrol website. 
Procedure from @harb70

https://community.home-assistant.io/t/multiscrape-please-help-with-scraping-bayrol-site/617419/13?u=duntch144

1 connect to the web portal

2 clic on “Direct Access”

3 on dev tools, clic network, search for the websocket connexion wss://www.bayrol-poolaccess.de:8083/

4 Clic on Messages and find the 1st one

5 you will find the username to use.

You can test with a MQTT tool like MQTT Explorer

Dev tool screenshot (Red line is the username to copy)








![image](https://github.com/Duntch144/Bayrol-AS-2-MQTT/assets/74782281/184f916d-30b4-4429-a620-171b467516b0)


Bayrol protocol identified codes


![image](https://github.com/Duntch144/Bayrol-AS-2-MQTT/assets/74782281/c633dfd0-7244-4994-8d97-e441c8b91b45)

