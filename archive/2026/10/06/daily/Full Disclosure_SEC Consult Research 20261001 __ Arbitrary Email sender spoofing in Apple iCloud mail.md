---
title: SEC Consult Research 20261001 :: Arbitrary Email sender spoofing in Apple iCloud mail
url: https://seclists.org/fulldisclosure/2026/Oct/1
source: Full Disclosure
date: 2026-10-06
fetch_date: 2026-10-07T07:55:42.137389
---

# SEC Consult Research 20261001 :: Arbitrary Email sender spoofing in Apple iCloud mail

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

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# SEC Consult Research 20261001 :: Arbitrary Email sender spoofing in Apple iCloud mail

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 1 Oct 2026 12:08:33 +0000

---

```
SEC Consult Vulnerability Lab Research Announcement < 20261001 >
=======================================================================
              title: Arbitrary Email sender spoofing in Apple iCloud mail
            product: Apple iCloud mail (SMTP submission service)
 vulnerable version: iCloud mail infrastructure (cloud service)
      fixed version: Fixed by Apple (verified by SEC Consult, 2025-12-09)
         CVE number: None assigned
             impact: Sending of emails from arbitrary icloud.com addresses,
                     passing SPF, DKIM and DMARC checks
           homepage: https://www.apple.com/
           reported: 2024-05-21 (issue 1), 2024-12-07 (issue 2)
                 by: Timo Longin (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Summary:
--------
The SEC Consult Vulnerability Lab has published a blog post about two
email spoofing vulnerabilities in Apple's iCloud mail infrastructure.
They allowed an authenticated iCloud user to send emails from arbitrary
icloud.com addresses. The spoofed messages passed SPF, DKIM and DMARC
checks at the receiving side. The research builds on SMTP smuggling.

Blog URL:
---------
Full technical details here:
https://r.sec-consult.com/icloud

Vulnerability overview/description:
-----------------------------------
1) From header smuggling via bare CR characters
iCloud's SMTP submission services handle a From header containing bare
CR characters differently in two internal components. The component
that authenticates the sender ignores the manipulated header, while a
second component, which is likely Postfix-based, replaces standalone CR
characters with CR LF. This pushes the legitimate From header into the
message body and leaves the attacker-controlled From header as the one
seen by the receiver.

2) From header smuggling via dot-stuffing handling ("dot-peeling")
After Apple hardened the From header parsing of the first component, a
second bypass was found. The first component does not honor the
dot-stuffing rules of RFC 5321 section 4.5.2, which allowed the
separation of header and body to be abused in the second component.

Impact:
-------
Both issues allowed sending emails as arbitrary icloud.com addresses.
DKIM signatures are created after the message has been processed by the
second component, therefore SPF, DKIM and DMARC checks all passed on the
receiving side.

Vendor contact timeline:
------------------------
2024-05-21: Initial vulnerability report submitted to Apple: icloud.com SMTP
            services can be abused via CRLF injection in the From: header to
            send spoofed emails (e.g., admin () icloud com) with valid DKIM/DMARC.
            PoC files and script attached; credit line requested for Timo Longin
            / SEC Consult Vulnerability Lab.
2024-06-06: Follow-up requesting a status update and fix timeline; Apple
            responds that the issue is still under investigation and asks that
            details not be disclosed until fixed.
2024-06-27: Follow-up requesting a status update.
2024-06-29: Apple reports no new status update.
2024-08-01: SEC Consult confirms the PoC script no longer works and asks Apple
            to confirm a fix was made.
2024-08-09: Apple reports no new status update, thanks SEC Consult for patience.
2024-09-01: Follow-up requesting a status update.
2024-09-11: Apple reports still investigating, no new updates to share.
2024-10-07: Follow-up checking the issue hasn't been forgotten.
2024-10-08: SEC Consult notes an upcoming SMTP smuggling talk at IT-SECX (Oct
            11) that will not disclose new vulnerability details; asks Apple for
            a fix timeline.
2024-10-17: Apple states changes have been made and asks SEC Consult to confirm
            current behavior.
2024-11-01: SEC Consult confirms the original PoC (CRLF injection in From:
            header) is no longer exploitable; proposes public disclosure at
            BSidesVienna on Nov 23, 2024, plus a blog post in December.
2024-11-04: Apple confirms the report as remediated and asks to review a draft
            of the planned disclosure.
2024-11-07: Draft BSidesVienna slides shared with Apple (attachment failed to
            send).
2024-11-09: Apple reports the attachment wasn't received; asks SEC Consult to
            resend.
2024-11-11: Slides resent; SEC Consult asks Apple for root-cause details
            (proprietary iCloud SMTP vs. third-party software).
2024-11-19: Apple confirms the report qualifies for the Apple Security Bounty
            and awards $15,000.
2024-12-06: SEC Consult discovers a second, related parsing issue enabling
            From-header spoofing via a different method; Apple asks that it be
            filed as a separate report.
2024-12-07: New report opened and tracked as OE196504222209; Apple acknowledges
            receipt.
2024-12-11: SEC Consult reports the deployed fix is insufficient - it merely
            blacklists the POC substring "admin" in the From: header rather than
            fixing the root parsing flaw, leaving most other @icloud.com
            addresses spoofable and potentially breaking mail for legitimate
            users with "admin" somewhere in their address.
2024-12-12: SEC Consult provides a new working PoC spoofing security () icloud com,
            with supporting screenshots, raw message, and script.
2024-12-16: Apple acknowledges the additional information and states it will
            follow up if further details are needed.
2025-01-28: SEC Consult shares further technical analysis, noting Postfix's
            smtpd_sender_login_maps limitations and recommending a Milter-based
            filter (e.g., milterfrom) that checks the From: header against the
            final email data before sending, as a likely root-cause fix.
2025-01-29: Apple acknowledges the analysis, states the issue is still under
            investigation.
2025-03-28: SEC Consult confirms the vulnerability is still exploitable. Apple
            replies (marked confidential) that a fix is planned for a future
            security update and asks that disclosure wait until it ships.
2025-04-04: SEC Consult agrees to hold disclosure and asks for a rough
            timeframe; Apple says more information will be available in the
            coming weeks.
2025-05-22: SEC Consult asks for an update, noting the issue remains
            exploitable.
2025-05-24: Apple reports an update was released in the prior 48 hours and asks
            SEC Consult to reassess whether the issue is remediated.
2025-06-10: Apple follows up again asking SEC Consult to confirm whether the
            update fixed the issue.
2025-06-13: SEC Consult confirms a bypass still exists, working the same way as
          ...