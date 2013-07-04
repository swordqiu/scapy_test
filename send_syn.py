#!/usr/bin/env python

from scapy.all import IP, TCP, send

def send_syn(dest, src=None, sport=1234, dport=80):
    pkt = IP(dst=dest,src=src)/TCP(sport=sport,dport=dport,flags="S")
    send(pkt)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            send_syn(sys.argv[1], src=sys.argv[2])
        else:
            send_syn(sys.argv[1])
    else:
        print 'Usage: scan_syn <destIP>'
        print '       scan_syn <destIP> <srcIP>'
