import random
import requests
import sys
import string
import threading
import json
import time
from pyomgclient.utils import config
from pyomgclient.utils.generators import *
from pyomgclient import __version__
class Client:
  def __init__ (self, lang = "en", on_start = None, on_error = None, on_disconnect = None, on_message = None, on_typing = None):
    self.lang = lang
    self.port = generate_port()
    self.version = __version__
    self.randid = generate_randid()
    self.session = requests.Session()
    self.clientId = False
    self.typing = False
    self.events = {}
    self.poll = threading.Thread (target=self.events_handler)

  def events_handler (self):
    while True:
      ev = json.loads(requests.post (config.OM_EVENTS_URL.format(str(self.port)), {"id": self.clientId}).text)
      if ev:
        for i in ev:
          if i[0] in self.events:
            func = self.events.get(i[0])
            if i[0] == "gotMessage":
              func(i[1])
            else:
              func()
          
    time.sleep (1)

  def send_message (self, msg, typ = False):
    url = config.OM_SEND_URL.format(str(self.port))
    payload = {
        "id": self.clientId,
        "msg": msg
    }
    if not typ:
      self.session.post (url, payload)
    else:
      self.start_typing ()
      time.sleep (1)
      self.stop_typing ()
      self.session.post (url, payload)

  def start_typing (self):
    url = config.OM_START_TYPING_URL.format(str(self.port))
    payload = {
        "id": self.clientId
    }
    if not self.typing:
      self.session.post(url, payload)
      self.typing = True
    else:
      return False

  def stop_typing (self):
    url = config.OM_STOP_TYPING_URL.format(str(self.port))
    payload = {
        "id": self.clientId
    }
    if self.typing:
      self.session.post (url, payload)
      self.typing = False
    else:
      return False

  def start (self):
    res = generate_client_id(port = self.port, randid = self.randid, session = self.session)
    if res["events"]:
      for i in res["events"]:
        if i[0] == "recaptchaRequired" and "recaptchaRequired" in self.events:
          self.events["recaptchaRequired"](i[1])
          
    else:
      self.clientId = res["clientID"]
      if self.events.get("start"):
        self.events.get("start")()

    if not self.poll.is_alive(): self.poll.start()


  
  def credentials (self):
    creds = {}
    creds["lang"] = self.lang
    creds["version"] = self.version
    creds["port"] = self.port
    creds["clientId"] = self.clientId
    creds["randid"] = self.randid
    return creds

  def set_on_message_cb (self, cb):
    self.events["gotMessage"] = cb

  def set_on_start_cb (self, cb):
    self.events["start"] = cb

  def set_on_typing_cb (self, cb):
    self.events["typing"] = cb

  def set_on_disconnect_cb (self, cb):
    self.events["strangerDisconnected"] = cb

  def set_on_recaptcha_cb (self, cb):
    self.events["recaptchaRequired"] = cb


