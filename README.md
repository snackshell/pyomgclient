# PyOMGClient
> A PYTHON OMEGLE CLIENT 

# installation

```bash
pip install pyomgclient
```

# usage

```python 

from pyomgclient.omgclient import Client

client = Client()

@client.set_on_open_cb
def on_open ():
  print ("stranger connected")

@client.set_on_disconnect_cb
def on_close ():
  print ("stranger disconnected")
  # to restart
  client.start()

@client.set_on_typing_cb
def on_typing ():
  print ("stranger typing")

@client.set_on_message_cb
def on_message (msg):
  print ("message: "+msg)
  # sends a message 
  # set typ = True for type and send
  client.send_message ("hi", typ = True)
  # or
  client.start_typing()
  time.sleep (1)
  # stop typing must be called otherwise the typing wont turn off
  client.stop_typing()

# always call the start function
# atfer setting callbacks
# otherwise client will connect without
# any callbacks

client.start()

# returns client configuration in json format
print (client.credentials())
```

# Solving Recaptcha

**this project cannot solve captcha so if your client is not getting any updates then go to your browser and open omegle then solve the captcha**

# Example Projects

> [pyomgcli (made by us)](https://github.com/TheXProjects/pyomgcli)

# ⚠️ DISCLAIMER

`this projects was made for educational purposes
do not spam people with this 
and we are not responsible for any illegal purpose done with this project`

  `omegle may ban your ip address so be careful`


**© XProjects**
