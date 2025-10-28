---
title: Bytes over DNS Tools
url: https://blog.didierstevens.com/2025/10/27/bytes-over-dns-tools/
source: Didier Stevens
date: 2025-10-27
fetch_date: 2025-10-28T03:06:50.713122
---

# Bytes over DNS Tools

# [Didier Stevens](https://blog.didierstevens.com/)

## Monday 27 October 2025

### Bytes over DNS Tools

Filed under: [Hacking](https://blog.didierstevens.com/category/hacking/),[Networking](https://blog.didierstevens.com/category/networking/) — Didier Stevens @ 9:07

Here are the tools I used to conduct my “[Bytes over DNS](https://isc.sans.edu/diary/Bytes%2Bover%2BDNS/32420/)” tests.

On the server side, I start my dnsresolver.py program with the following custom script:

```
LOGFILENAME = 'bod-dnsresolver-test.log'

def BoDTest(request, reply, dCommand):
    if request.q.qtype == dnslib.QTYPE.A:
        if len(request.q.qname.label[2]) == 1 and int(request.q.qname.label[1].decode(), 16) == ord(request.q.qname.label[2]):
            with open(LOGFILENAME, 'a') as fOut:
                print(f'BYTE_EQUAL {request.q.qname.label[1]} {request.q.qname.label[2]}', file=fOut)
            qname = request.q.qname
            answer = '. 60 IN A 127.0.0.1'
            for rr in dnslib.RR.fromZone(answer):
                a = copy.copy(rr)
                a.rname = qname
                reply.add_answer(a)
            return False, None
        else:
            with open(LOGFILENAME, 'a') as fOut:
                print(f'BYTE_DIFFERENT {request.q.qname.label[1]} {request.q.qname.label[2]}', file=fOut)
    return True, None
```

Start it as follows: dnsresolver.py -s bod-dnsresolver-test.py type=resolve,label=bytes,function=BoDTest

And make sure your DNS glue records (e.g., for mydomain.com) point to your server.

Then you can do a small test: nslookup bytes.3D.=.mydomain.com.

This will return 127.0.0.1 when the request arrives unaltered, and NXDOMAIN when it is altered. The BoDTest function will also log the results in text file bod-dnsresolver-test.log.

Then, on your workstation, you can run the following script to test all bytes values in the DNS request via the API of your OS:

```
#!/usr/bin/env python3

import socket
import sys

DOMAIN = '.mydomain.com.'

def DNSResolveA(char: int):
    hostname_ascii = 'bytes.%02x.%s' % (char, chr(char)) + DOMAIN
    hostname_ascii = hostname_ascii.replace('\\', '\\\\')
    print(hostname_ascii)
    try:
        results = socket.getaddrinfo(hostname_ascii, None, family=socket.AF_INET, type=0, proto=0, flags=socket.AI_CANONNAME)
    except socket.gaierror as e:
        print(f"Resolution failed: {e}")
        return 1
    except UnicodeError as e:
        print(f"Resolution failed: {e}")
        return 1

    if not results:
        print("No results returned by getaddrinfo.")
        return 0

    # Collect canonical name (may be empty) and addresses
    canon_names = set()
    addresses = []
    for res in results:
        family, socktype, proto, canonname, sockaddr = res
        if canonname:
            canon_names.add(canonname)
        # sockaddr is a tuple; for IPv4 it's (addr, port), for IPv6 it's (addr, port, flowinfo, scopeid)
        ip = sockaddr[0]
        addresses.append((family, ip))

    if canon_names:
        print("Canonical name(s):")
        for cn in sorted(canon_names):
            print("  -", cn)
        print()

    # Deduplicate and group by family
    unique_ips = {}
    for fam, ip in addresses:
        fam_name = "IPv4" if fam == socket.AF_INET else ("IPv6" if fam == socket.AF_INET6 else str(fam))
        unique_ips.setdefault(fam_name, set()).add(ip)

    for fam_name in sorted(unique_ips.keys()):
        print(f"{fam_name} addresses ({len(unique_ips[fam_name])}):")
        for ip in sorted(unique_ips[fam_name]):
            print("  -", ip)
    print()

    # Optionally, try reverse DNS for each IP (may be slow / not always available)
    print("Reverse DNS (PTR) lookups:")
    for fam_name, ips in unique_ips.items():
        for ip in sorted(ips):
            try:
                host, aliases, _ = socket.gethostbyaddr(ip)
                print(f"  {ip} -> {host}")
            except Exception as e:
                print(f"  {ip} -> (no PTR)  [{e}]")

    return 0

if __name__ == "__main__":
    for char in range(256):
        DNSResolveA(char)
```

Use this script to perform the tests via the [dnspython](https://pypi.org/project/dnspython/)/dns.resolver Python module:

```
import dns.resolver

resolver = dns.resolver.Resolver()
DOMAIN = b'.mydomain.com.'

#resolver.nameservers = ['127.0.0.1']
#resolver.nameservers = ['1.1.1.1']
resolver.nameservers = ['8.8.8.8']

for i in range(256):
    if i == 0x2E:
        continue
    if i == 0x5C:
        byte = b'\\\\'
    else:
        byte = bytes([i])
    try:
        answer = resolver.resolve(((b'bytes.%02x.%s' + DOMAIN) % (i, byte)).decode('latin'), "A")
        for rdata in answer:
            print(i, rdata.to_text())
    except (dns.name.LabelTooLong, dns.resolver.NXDOMAIN) as e:
        print(i, e)
```

And use this script to perform the tests by crafting your own DNS packets:

```
import socket

DOMAIN = b'mydomain.com.'
DNS = '1.1.1.1'
DNS = '8.8.8.8'

def send_udp_payload(data: bytes, target_ip: str, port: int = 53) -> None:
    """
    Send raw binary data via UDP to a target IP and port (default 53).

    :param data: The binary payload to send (must be bytes).
    :param target_ip: The destination IP address (string).
    :param port: Destination UDP port (default = 53).
    """
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(data, (target_ip, port))
        print(f"Sent {len(data)} bytes to {target_ip}:{port}")
    except Exception as e:
        print(f"Error sending data: {e}")
    finally:
        sock.close()

def DNSEncodeDomain(domain):
    labels = domain.split(b'.')
    if labels[-1] != b'':
        labels.append(b'')
    data = bytearray()
    for label in labels:
        data += bytes([len(label)])
        data += label
    return data

data = bytearray([0x88, 0xea, 0x01, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x05, 0x62, 0x79, 0x74, 0x65, 0x73, 0x02, 0x32, 0x65, 0x01, 0x2e]) + DNSEncodeDomain(DOMAIN) + bytearray([0x00, 0x01, 0x00, 0x01])

for i in range(256):
    data[1] = i
    data[22] = i
    hexvalue = b'%02x' % i
    data[19:21] = hexvalue
    print(data)
    send_udp_payload(data, DNS)
```

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2025/10/27/bytes-over-dns-tools/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2025/10/27/bytes-over-dns-tools/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2025/10/27/bytes-over-dns-tools/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2025/10/27/bytes-over-dns-tools/feed/) [TrackBack URI](https://blog.didierstevens.com/2025/10/27/bytes-over-dns-tools/trackback/)

### Leave a Reply (comments are moderated)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* ## Pages

  + [About](https://blog.didierstevens.com/about/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [Links](https://blog.didierstevens.com/links/)
  + [My Python Templates](https://blog.didierstevens.com/my-python-templates/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Professional](https://blog.didierstevens.com/professional/)
  + [Programs](https://blog.didierstevens.com/programs/)
    - [Ariad](https://blog.didierstevens.com/programs/ariad/)
    - [Authenticode Tools](https://blog.didierstevens.com/programs/authenticode-tools/)
    - [Binary Tools](https://blog.didierstevens.com/programs/binary-tools/)
    - [CASToggle](https://blog.didierstevens.com/programs/castoggle/)
    - [Cobalt Strike Tools](https://blog.didierstevens.com/programs/cobalt-strike-tools/)
    - [Disitool](https://blog.didierstevens.com/programs/disitool/)
    - [EICARgen](https://blog.did...