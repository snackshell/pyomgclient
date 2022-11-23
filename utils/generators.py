import random
from pyomgclient.utils import config
import string
import json

ports = ['30', '42', '48', '35', '37', '14', '17', '5', '11', '18', '26', '31', '20', '19', '38', '8', '16', '13', '1', '29', '47', '41', '39', '34', '44', '10', '45', '40', '3', '33', '46', '23', '43', '15', '9', '7', '6', '24', '22', '2', '32', '25', '28', '21', '12', '4', '27', '36']

def generate_port ():
  return ports[random.randint (1, len(ports))]

def generate_randid ():
  result = random.choices (string.ascii_uppercase, k=8)
  fres = ""
  for i in result:
    fres += i
  return str(random.randint(1,9))+str(fres)

def generate_client_id (port, randid, session, lang = "en"):

  payload = {
    "caps": "recaptcha2,t2",
    "firstevents": 1,
    "spid": "",
    "randid": randid,
    "m": 1,
    "lang": lang
  }

  try:
    res = session.post (config.OM_START_URL.format(str(port))+f"?caps={payload['caps']}&firstevents={payload['firstevents']}&spid=&randid={payload['randid']}&m=1&lang={payload['lang']}", payload)
    return json.loads(res.text)
  except Exception as e:
    return e
