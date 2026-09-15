---
title: 3BB Attacker Used MeshCentral Backdoor for Root Access, Targeted Subscriber Credentials
url: https://thehackernews.com/2026/09/3bb-attacker-used-meshcentral-backdoor.html
source: The Hacker News
date: 2026-09-14
fetch_date: 2026-09-15T07:03:15.474778
---

# 3BB Attacker Used MeshCentral Backdoor for Root Access, Targeted Subscriber Credentials

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [3BB Attacker Used MeshCentral Backdoor for Root Access, Targeted Subscriber Credentials](https://thehackernews.com/2026/09/3bb-attacker-used-meshcentral-backdoor.html)

**Swati Khandelwal**Sep 14, 2026Network Security / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9khzZCrFkNfQ1fOYHT8A4LJrIsfc52ppe6xZffdUrfRacqTVQ76P0VPDZhqC2UfKM32jdbEiQfaCZDbrV2F0_dssOM8V8nT3ZZYvwhflLdfEhJhdNa0-UntK9XHkFJ4R5RthFMOM2X5kDZxUKW1RnRLmmQ0xLh5foMldMZovB0ZPdafoRf9cEb_w9Hwk/s1700-nu-rw-lo-l85-e365/3bb.jpg)

An attacker was operating inside the network of **3BB**, one of Thailand's largest broadband providers, and maintained remote control of internal machines using a legitimate management tool called MeshCentral, threat intelligence firm Hunt.io said.

The company uncovered the intrusion by examining a server the attacker had left open on the internet, which held the attacker's own tools and a list of machines already under their control.

The researchers captured the exposed server on June 3, 2026, while the operation was still live. The tools on it had been run from a computer inside 3BB's own network, and one recovered file showed the attacker gaining full administrative control, known as root, of an internal server.

To maintain that access, the attacker installed **MeshCentral**, a free tool that IT teams typically use to manage computers remotely. The recovered settings show it was configured as a hidden backdoor, with the agents reporting to a control server that the attacker ran at www.ayuthayatech[.]com, under a device group named **TH-3BB**.

Attackers [increasingly abuse](https://www.labs.greynoise.io/grimoire/2025-12-09-react2shell-meshcentral) this kind of remote-management software because it is trusted and its activity blends in with routine administration.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

A device list recovered from the server named the machines enrolled in the attacker's MeshCentral setup. Several were connected and running with root privileges when the list was made, which the researchers said showed the attacker held active administrative control at that point.

A separate cleanup script was written to erase logs and delete the attacker's other tools while deliberately leaving the MeshCentral agent in place so that the access would survive.

Inside the network, the attacker worked to widen their access. Recovered scripts sprayed passwords against more than 55 internal computers over SSH, probed 3BB's internal sales portal at agent.3bb.co[.]th, and searched compromised machines for stored passwords, database logins, and SSH keys. Other scripts could plant web shells, hidden pages that run an attacker's commands, and add SSH keys as backup ways back in.

Hunt.io said the attacker's main goal was 3BB's subscriber data. Scripts on the server were built to copy out the company's RADIUS databases, the systems that store the login credentials broadband customers use to get online. The evidence shows those databases were targeted, not that any data was taken.

The same server pointed to a second target. It held a valid VPN certificate from 3BB's own systems and active login sessions for services on the Jasmine network, a company 3BB was once part of and still shares infrastructure with. Hunt.io said this suggested the attacker was working against both, though it did not confirm that Jasmine itself had been breached.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhB6fZv9iKdWOjwwJeQZW6bIjcpSBBUQ3mCcXysAWXkuQz4v8Hf_OZ4l2zvghUl4Or_hvkcFuuTvoESEk9LUlkvyONphCMUMB4u-gBZTKd3yT_1veMnxOReTIpM8B5dBwzsZ9uOSnxT5M5fljrc26pZudJjbmVhPE_Ei0tKeBDs0DY_3t47qGQA-GJNJQc/s1700-nu-rw-lo-l85-e365/forti.png)

How the attacker initially gained access to 3BB is not established. The server held a full toolkit aimed at a 3BB FortiGate SSL-VPN gateway, the remote-access box at mail.3bb.co[.]th, including a complete exploit for [CVE-2024-21762](https://thehackernews.com/2024/02/fortinet-warns-of-critical-fortios-ssl.html), a serious 2024 Fortinet flaw that lets an attacker run code on the device without logging in. The targeted gateway was running a firmware version affected by the flaw.

But nothing Hunt.io recovered shows the exploit actually worked, or that it was how the attacker got in. The FortiGate tooling was the most developed part of the kit, yet it points to the attacker's capability and intent, not a confirmed break-in through that device.

The attacker has since closed the exposed directory. Whether they still have access inside 3BB is not known, because the evidence describes the intrusion as it stood in early June, not today.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

The researchers said they notified the affected companies and the relevant national response team about their findings before publishing.

### What Defenders Should Do

The recovered toolkit points to a clear set of steps for organizations running similar edge devices and authentication systems:

* Patch or confirm that FortiGate SSL-VPN appliances are fixed against CVE-2024-21762. [Fortinet's advisory](https://fortiguard.fortinet.com/psirt/FG-IR-24-015) says that if you cannot patch at once, you should turn off SSL-VPN, and that turning off web mode alone is not a valid workaround.
* Check for MeshCentral agents you did not install, and for connections to management servers you do not recognize.
* Rotate credentials that may have been exposed, including SSH keys, database and RADIUS passwords, VPN certificates, and application secrets. Patching does not remove an agent that is already installed or reset a password that has already been copied.
* Hunt for hidden ways back in, such as unexpected SUID files, web shells, changed SSH keys, and newly added remote-management software.
* Preserve logs and evidence before cleaning up, becau...