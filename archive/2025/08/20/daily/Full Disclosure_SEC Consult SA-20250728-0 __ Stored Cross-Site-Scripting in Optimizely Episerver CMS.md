---
title: SEC Consult SA-20250728-0 :: Stored Cross-Site-Scripting in Optimizely Episerver CMS
url: https://seclists.org/fulldisclosure/2025/Aug/18
source: Full Disclosure
date: 2025-08-20
fetch_date: 2025-10-07T00:50:58.787031
---

# SEC Consult SA-20250728-0 :: Stored Cross-Site-Scripting in Optimizely Episerver CMS

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
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20250728-0 :: Stored Cross-Site-Scripting in Optimizely Episerver CMS

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 7 Aug 2025 08:39:11 +0000

---

```
Confidentiality class: Internal & Partner

SEC Consult Vulnerability Lab Security Advisory < publishing date 20250728-0 >
=======================================================================
              title: Multiple Stored Cross-Site Scripting Vulnerabilities
            product: Optimizely Episerver Content Management System (EPiServer.CMS.Core)
 vulnerable version: Version 11.X: <11.21.4
                     Version 12.X: <12.22.1
      fixed version: Version 11.X: 11.21.4
                     Version 12.X: 12.22.1
         CVE number: CVE-2025-27800, CVE-2025-27801, CVE-2025-27802
             impact: medium
           homepage: https://www.optimizely.com
              found: 2024-04-25
                 by: Kai Zimmermann (Office Frankfurt)
                     Felix Beie (Office Fürth)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Optimizely Content Management System equips marketers and developers with a modern,
fully composable suite of user-friendly tools. Deliver impactful experiences across
any channel, and personalize with AI-driven insights."

Source: https://www.optimizely.com/products/content-management/

Business recommendation:
------------------------
The vendor already provides a security patch (updated packages) which should be
installed immediately.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Stored Cross-Site Scripting in Admin Dashboard (CVE-2025-27800)
The Admin dashboard offered the functionality to add gadgets to the dashboard.
This included the "Notes" gadget. An authenticated attacker with the corresponding
access rights (such as "WebAdmin") that was impersonating the victim could insert
malicious JavaScript code in these notes that would be executed if the victim
visited the dashboard.

2) Stored Cross-Site Scripting in Media Selection Preview (CVE-2025-27801)
ContentReference properties, which could be used in the "Edit" section of the CMS,
offered an upload functionality for documents. These documents could later be used
as displayed content on the page. It was possible to upload SVG files that include
malicious JavaScript code that would be executed if a user visited the direct URL
of the preview image. Attackers needed at least the role "WebEditor" in order to
exploit this issue.

3) Stored Cross-Site Scripting in Edit Preview (CVE-2025-27802)
RTE properties (text fields), which could be used in the "Edit" section of the CMS,
allowed the input of arbitrary text. It was possible to input malicious JavaScript
code in these properties that would be executed if a user visits the previewed
page. Attackers needed at least the role "WebEditor" in order to exploit this issue.

Proof of concept:
-----------------
1) Stored Cross-Site Scripting in Admin Dashboard (CVE-2025-27800)
After adding a newly created note on the dashboard, it could be edited by sending
the following request:

--------------------------------------------------------------------------------
POST /EPiServer/CMS/Notes/Save?preferredNamespace=EPiServer.Cms.Shell.UI.Controllers.Internal&gadgetId=$GADGETID HTTP/2
Host: $SERVER
Cookie: sessionId=[...]; .EPiServerLogin=[...]; .ASPXROLES=[...]; __RequestVerificationToken=[...]
Content-Type: application/x-www-form-urlencoded
Content-Length: 177

content=Test%3cbr%3e%3cimg%20src%3dx%20onerror%3dalert(window.location)%3e&__RequestVerificationToken=[...]
--------------------------------------------------------------------------------

Visiting the dashboard again, as seen in figure 1 below, showed that the
JavaScript code is executed:
[01_admin_dashboard.png]

2) Stored Cross-Site Scripting in Media Selection Preview (CVE-2025-27801)
The following SVG file containing a JavaScript alert could be uploaded as a document
in one of the ContentReference properties:

--------------------------------------------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd";>
<svg xmlns="http://www.w3.org/2000/svg"; version="1.1" width="1" height="1">
    <rect x="1" y="1" width="1" height="1" fill="green" stroke="black" />
    <script type="text/javascript">alert(window.origin);</script>
</svg>
--------------------------------------------------------------------------------

Visiting the preview URL, as seen in figure 2 below, showed that the JavaScript alert
was executed:
[02_svg_upload.png]

3) Stored Cross-Site Scripting in Edit Preview (CVE-2025-27802)
When adding HTML elements directly in the input field, they were encoded by the
frontend. The request, which was sent when editing the text, could be intercepted
and modified so that the encoding was reverted. The following request was then
sent to add a malicious JavaScript element that caused an alert when the element
was rendered:

--------------------------------------------------------------------------------
POST /EPiServer/cms/Stores/contentdata/$ID HTTP/2
Host: $SERVER
Cookie: .EPiServerLogin=[...];
Content-Length: 194
Content-Type: application/json
[...]

{"id":"$ID","properties":{"address":"\"[...]<script>alert(window.location)</script>[...]""},"action":$ACTIONID}
--------------------------------------------------------------------------------

After publishing the changes, the page preview could be visited by clicking on the
respective icon on the top right of the "Edit" section. Before the preview was
shown, the JavaScript alert was executed, as can be seen in figure 3 below:
[03_edit_preview.png]

Vulnerable / tested versions:
-----------------------------
The vendor confirmed that the following plugin versions are affected:
* Version 11.X: EPiServer.CMS.Core (<11.21.4) with EPiServer.CMS.UI (<11.37.5)
* Version 12.X: EPiServer.CMS.Core (<12.22.1) with EPiServer.CMS.UI (<11.37.3)

Vendor contact timeline:
------------------------
2024-05-23: Contacting vendor through securityeng () optimizely com
2024-05-24: Vendor responds to submit our vulnerabilities at Bugcrowd
2024-05-27: Asking vendor if it is possible via email, no suitable category
            at Bugcrowd; no response.
2024-06-04: Asking vendor where to submit the advisory for the CMS;
            Vendor confirms that Bugcrowd should not be used and requested
            advisory unencrypted via email. Submitted advisory.
2024-06-06: Sending requested information to the vendor; Vendor responds they
            got everything they need to check the provided advisory.
2024-06-10: Vendor provides details for all vulnerabiliti...