# dash.py - listen for Amazon Dash buttons booting and perform a custom
# action when button is pressed.
#
# Copyright (c) 2016 John Graham-Cumming

from scapy.all import Ether, sniff
import time

# Dictionary of buttons identifed by MAC address. The value for each
# button is the parameter passed to the rx() function.

# TODO: fill in MAC addresses of your dash buttons
buttons = {'74:c2:46:xx:xx:xx': 'button1',
           '74:c2:46:xx:xx:xx': 'button3'}

# Used to record the last time an individual dash button was
# pressed. This is done to prevent multiple packets (DHCP followed by
# ARP) being interpreted as multiple button presses.  

lastseen = {}

# The minimum interval between button presses in seconds.

interval = 60

# Called when a dash button is pressed with the appropriate parameter
# from the buttons dictionary.

def rx(param):
    # TODO: perform whatever task you want
    print param

def dispatch(pkt):
      src = pkt[Ether].src
      if src in buttons:
          now = time.time()
          if lastseen[src] == 0 or lastseen[src] < now - interval:
              lastseen[src] = now
              rx(buttons[src])

for mac in buttons:
    lastseen[mac] = 0

f = " or ".join([ "ether src " + mac for mac in buttons])
sniff(prn=dispatch, filter=f, store=0, count=0)
