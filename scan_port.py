#!/usr/bin/env python

import random
from scapy.all import IP, TCP, send

def send_syn(dest, src=None, sport=1234, dport=80):
    pkt = IP(dst=dest,src=src)/TCP(sport=sport,dport=dport,flags="S")
    send(pkt)

def scan_port(dest):
    for dport in range(1, 65536):
        send_syn(dest, sport=random.randint(21024, 51024), dport=dport)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        scan_port(sys.argv[1])
    else:
        print 'Usage: scan_syn <dest>'
