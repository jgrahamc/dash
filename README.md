# dash

Program to monitor Amazon Dash button presses and perform custom action.

<img src="https://raw.githubusercontent.com/jgrahamc/dash/master/dash.jpg" width="640px">

# Amazon Dash

As has been
[blogged](https://medium.com/@edwardbenson/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8#.77z7gdnvg)
elsewhere the [Amazon
Dash](http://www.amazon.com/b/?node=10667898011&lo=digital-text)
button can be used as a WiFi enabled button if it is incorrectly
configured. By partially setting up an Amazon Dash button it's
possible to have it boot and send out small number of broadcast
packets (DHCP and ARP) on start up.

<img src="https://raw.githubusercontent.com/jgrahamc/dash/master/wireshark.png" width="640px">

A computer running on the same WiFi network can sniff these packets
and use them as an indication that the Dash button has been pressed.

I found in practice that the blogged about technique of just listening
for an ARP packet was unreliable. Sometimes the packet would not get
received. The code here listens for all packets sent from the MAC
address of one or more buttons and uses a time window (default 60
seconds) to filter out multiple packets being received.

# TODO

There are two TODOs in the code: one where you fill in the MAC
addresses of the Amazon Dash buttons you want to monitor and another
in the rx() function to implement whatever action you want your
button(s) to perform.

# Caveat

I almost never write Python code.