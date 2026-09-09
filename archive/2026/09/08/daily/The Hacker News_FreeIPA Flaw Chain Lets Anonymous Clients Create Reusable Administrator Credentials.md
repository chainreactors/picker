---
title: FreeIPA Flaw Chain Lets Anonymous Clients Create Reusable Administrator Credentials
url: https://thehackernews.com/2026/09/freeipa-flaw-chain-lets-anonymous.html
source: The Hacker News
date: 2026-09-08
fetch_date: 2026-09-09T06:56:58.808014
---

# FreeIPA Flaw Chain Lets Anonymous Clients Create Reusable Administrator Credentials

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

# [FreeIPA Flaw Chain Lets Anonymous Clients Create Reusable Administrator Credentials](https://thehackernews.com/2026/09/freeipa-flaw-chain-lets-anonymous.html)

**Swati Khandelwal**Sep 08, 2026Vulnerability / Linux

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSKAVaHcAsULrGXPVkGXRyf94eoG7Kv3X0wwK2lRC64l3Em-S4_H5iE8-poK04yzrAC18tuHqpZyHhJvFTgliu_z8jo4QR78Mi4ghhCA-cUVL4oj2zjoLGiWKmD16oV4i44VfY45DYll0Uij_Exf4U2JMSLJEyH8jZk_xXKq7O_7D73q7vTYCCc4hrTnQ/s1700-nu-rw-lo-l85-e365/freeipa.jpg)

A flaw in **FreeIPA** lets a client that has never logged in create a Kerberos identity of its own choosing in the directory and end up in the administrators group, Red Hat says.

FreeIPA is the system that determines who may log in across a Linux domain and maintains all identities in a 389 Directory Server database accessed via LDAP. The attack needs a second flaw in that database software.

The FreeIPA project has already fixed its side in [version 4.13.4](https://www.freeipa.org/release-notes/4-13-4.html). Red Hat says it reproduced the chain twice on a default installation, most recently on a machine with no access at all.

Red Hat tracks the FreeIPA flaw as [CVE-2026-76578](https://access.redhat.com/security/cve/CVE-2026-76578) and rates it critical, with a CVSS score of 9.8. The same page says that score is preliminary and subject to review.

Red Hat ships FreeIPA as its **Identity Management product**, where the package is called **ipa**.

FreeIPA ships an access control rule, called an ACI, that lets a user manage their own one-time-password token. The rule does not require the client to have logged in, nor does it limit what else may be written alongside the token.

That only becomes dangerous because of the second flaw. **389 Directory Server** has a rule type meant to say "only the authenticated owner of this entry." It compares the client's name against a stored value as plain text, and a client that has not logged in has an empty name, which matches an empty stored value.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

So an anonymous client can create a token entry with the ownership fields left blank, pass the ownership check by being nobody, and write a Kerberos identity and password alongside it.

Red Hat scores the directory-server flaw, [CVE-2026-76560](https://access.redhat.com/security/cve/CVE-2026-76560), at 7.5, and says **Red Hat Directory Server** ships no rule of that shape by default. On its own, the flaw matters only where a deployment has written such a rule.

FreeIPA is such a deployment. Its shipped default rule is exactly that shape, which is why the chain works against an untouched install. That connection is our reading of two advisories that describe the halves separately.

Red Hat also reproduced the directory-server defect on its own, on a plain 389-ds build with no FreeIPA parts installed, and a control test using a value that was not empty was correctly refused. That places the defect in the access-control engine rather than in anything FreeIPA does.

The technique first reported to Red Hat impersonated the real admin account by creating a Kerberos name that matched it. An earlier fix for CVE-2026-13097 blocked that collision but left the underlying unauthenticated write in place. The attack now works under a name the attacker picks instead, Red Hat says, "reaching the same practical outcome."

That earlier flaw, fixed in [FreeIPA 4.13.3](https://www.freeipa.org/release-notes/4-13-3.html), was a different problem. The check that Kerberos names are unique did not allow different ways of writing the same name, which allowed a user with write access to create a service identity that impersonated an existing privileged one.

The two projects describe the result differently. Red Hat calls it genuine administrator-group membership and reusable administrator credentials.

The FreeIPA project puts it more narrowly, stating that the injected identity must not already exist, that the CVE-2026-13097 fix prevents existing accounts from being taken over, and that the attack "may be used as a stepping stone" to administrative privileges.

Red Hat says it ran the chain against a stock FreeIPA container image running version 4.13.1 and checked the results with standard administrator-only commands rather than trusting the exploit's output. None of the advisories or [bug reports](https://bugzilla.redhat.com/show_bug.cgi?id=2519522) describe the flaw being used in a real attack.

For deployments using Windows-style security identifiers, Red Hat says the attacker can also obtain a Kerberos ticket containing authorization data, thereby extending access to the server's HTTP and Dogtag services. Dogtag is FreeIPA's built-in certificate authority.

### A Second, Separate Flaw

Red Hat disclosed a second FreeIPA flaw alongside these, [CVE-2026-79678](https://access.redhat.com/security/cve/CVE-2026-79678), which has nothing to do with the chain above. It rates this one important, with a score of 8.1.

The idp-add command passes two values the caller supplies, an organization name and a base URL, into a Python eval() call. That call runs before the permission check meant to limit the command to identity-provider administrators, so any account on the server can reach it, whatever its privileges.

The call is limited by a pattern that forbids brackets, which stops any function being called. Red Hat says "no code execution is possible."

What an attacker can do is read the server process's environment variables one at a time by observing the error the server returns, and use up the server's memory with a short arithmetic expression.

How much that matters depends on how FreeIPA was installed, Red Hat says. On a normal package-based install, the process environment holds only documented paths and settings. Container installs are different.

The official FreeIPA server image often takes the Directory Ma...