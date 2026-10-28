---
title: SEC Consult SA-20261023-0 :: Multiple Cross-Site Scripting Vulnerabilities in VertiGIS WebOrderSystem
url: https://seclists.org/fulldisclosure/2026/Oct/37
source: Full Disclosure
date: 2026-10-27
fetch_date: 2026-10-28T07:49:43.659861
---

# SEC Consult SA-20261023-0 :: Multiple Cross-Site Scripting Vulnerabilities in VertiGIS WebOrderSystem

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

[![Previous](/images/left-icon-16x16.png)](36)
[By Date](date.html#37)
[![Next](/images/right-icon-16x16.png)](38)

[![Previous](/images/left-icon-16x16.png)](48)
[By Thread](index.html#37)
[![Next](/images/right-icon-16x16.png)](38)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20261023-0 :: Multiple Cross-Site Scripting Vulnerabilities in VertiGIS WebOrderSystem

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 23 Oct 2026 06:29:26 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20261023-0 >
=======================================================================
              title: Multiple Cross-Site Scripting Vulnerabilities
            product: VertiGIS WebOrderSystem (KundenManager, AuftragsManager)
 vulnerable version: <=7.0.8.6
      fixed version: unknown
         CVE number: CVE-2026-4950, CVE-2026-4951, CVE-2026-4952
             impact: medium/high
           homepage:https://www.vertigis.com/
              found: 2025-01-14
                 by: Kai Zimmermann (Office Frankfurt)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"VertiGIS creates industry-leading technology that advances spatial visibility
into assets – across industries and across the globe. Our intuitive range of
use-case-based tools can help you solve complex business challenges, leverage
spatial data in new ways and build solutions that make a difference."

Source:https://www.vertigis.com/

Business recommendation:
------------------------
The vendor did not communicate a patch for the identified vulnerabilities in
VertiGIS "WebOrderSystem" and told us that "LM Explorer" will incorporate the
fixes. Version numbers were not provided nor when the fixes were implemented.

A workaround exists for CVE-2026-4952, which should be applied while no
official fix is available. Contact the vendor fur further information
regarding fixes or hardening measures.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Stored Cross-Site Scripting in VertiGIS CustomerAdministration Portal (CVE-2026-4950)
The VertiGIS CustomerAdministration portal (KundenManager) allows privileged
users to manage the employees (users) of defined companies (user groups). An
authenticated attacker with access to the CustomerAdministration portal can
insert malicious JavaScript code in a user's properties while editing the user.
The inserted code will be executed if other privileged users visit either the
user entry directly or the user overview of the specific user group.

2) Reflected Cross-Site Scripting in VertiGIS CustomerAdministration Portal (CVE-2026-4951)
The VertiGIS CustomerAdministration portal (KundenManager) allows privileged
users to search for employees (users) across all defined companies (user groups).
The search parameter "searchValue" can be embedded in the URL, so that if a
privileged user that is currently logged into the CustomerAdministration portal
visits that URL, the search will be performed. An unauthenticated attacker with
knowledge about the URL structure can craft a URL containing malicious
JavaScript code in the "searchValue" parameter. The inserted code will be
executed if the target privileged user visits the crafted URL while already
being logged into the CustomerAdministration portal.

3) Stored Cross-Site Scripting in VertiGIS OrderAdministration Portal (CVE-2026-4952)
The VertiGIS "ASMobile" web interface, which is part of the software package
"GIS Portal", allows authenticated users to define a business reference. An
attacker can insert malicious JavaScript code inside the business reference.
Initially this issue affects the "ASMobile" web interface as what is considered
a "self-xss". However, when placing orders through the web interface, the malicious
business reference will be included in the order details and will later be shown
in the OrderAdministration portal (AuftragsManager). The inserted JavaScript code
will be executed if a high privileged user with access to the OrderAdministration
portal visits the order that contains the attacker's malicious business reference.

Proof of concept:
-----------------
1) Stored Cross-Site Scripting in VertiGIS CustomerAdministration Portal (CVE-2026-4950)
When editing an existing user of a user group through the CustomerAdministration
portal, the following request, including malicious JavaScript code in the
"secondName" parameter, can be sent when saving the changes:

--------------------------------------------------------------------------------
[ PoC removed ]
--------------------------------------------------------------------------------

After saving the changes, the JavaScript code will be executed immediately after
the editing page, as can be seen in figure 1 below:

[01_stored_xss_01.png]

Figure 2 below shows that the JavaScript code will also be executed when a user
visits the user overview of the edited user's user group:

[02_stored_xss_02.png]

2) Reflected Cross-Site Scripting in VertiGIS CustomerAdministration Portal (CVE-2026-4951)
An unauthenticated attacker with knowledge about the CustomerAdministration portal's
URL structure can craft the following URL, which contains malicious JavaScript code
in the "searchValue" parameter:

--------------------------------------------------------------------------------
[ PoC removed ]
--------------------------------------------------------------------------------

When a privileged user, who is currently logged into the CustomerAdministration
portal, visits the crafted URL, the included JavaScript code will be executed, as
can be seen in figure 3 below:

[03_reflected_xss.png]

Potential further impacts may arise from the fact that administrative users can
change other user's (including other administrators) passwords without specifying
the old password. An attacker may be able to craft a URL loading a remote script
that performs a password reset, allowing to either take over specific accounts
or lock out other users entirely from the application.

3) Stored Cross-Site Scripting in VertiGIS OrderAdministration Portal (CVE-2026-4952)
```

A user's business reference can be edited by the user through the "ASMobile" web interface, when being logged in. For demonstration purposes, an image HTML tag can be inserted in the reference, which, when causing an error, executes a JavaScript alert. When adding such a
payload to the business reference and exiting the text field, the JavaScript alert will be executed, as can be seen in figure 4 below: [04\_stored\_xss\_2\_alert.png] Rechecking the business reference
after exiting the alert shows that the malicious image tag was rendered inside the page, as shown in figure 5 below: [05\_stored\_xss\_2\_rendered.png] When placing orders through the web interface, the
user's business reference will also be included. After the order is placed, it will be listed in the administrative OrderAdministration portal and the malicious JavaScript code will be executed in a
high privileged browser of the victi...