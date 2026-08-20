---
title: Clop-Linked Windchill Web Shell Decrypts Credentials and Maps Engineering Data
url: https://thehackernews.com/2026/08/clop-linked-windchill-web-shell.html
source: The Hacker News
date: 2026-08-19
fetch_date: 2026-08-20T02:56:57.226639
---

# Clop-Linked Windchill Web Shell Decrypts Credentials and Maps Engineering Data

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Clop-Linked Windchill Web Shell Decrypts Credentials and Maps Engineering Data](https://thehackernews.com/2026/08/clop-linked-windchill-web-shell.html)

**Ravie Lakshmanan**Aug 19, 2026Vulnerability / Ransomware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEit3cCqpn48W_lqEDCb9ewKFToGQcvhUjO939N0Gja-aTvCvRTz8kdOPZG1bhyphenhyphenED2XNeB82rjCIeVO3Nw9akDlMnQZqc7keiel8H82zgtf1A7fhb6DP3z6Qh3Ehk6AGrMt77rXkoNhLaDeEl692kDHAHVsNb7AOcDxpsavM0Hj9TZRLLJsuQ-OT3oQOvFMi/s1700-e365/ptc.jpg)

A JavaServer Pages (JSP) web shell deployed following the exploitation of a critical security flaw in PTC Windchill and FlexPLM servers is specifically designed for the enterprise Product Lifecycle Management (PLM) software, according to [new findings](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign) from ReliaQuest.

The cybersecurity company characterized the web shell as a fully equipped extortion platform capable of mapping sensitive vault data, decrypting every credential in the Windchill keystore, and running additional code by means of a custom Java class loader, turning the tool into a backdoor for remote access and post-exploitation activity, such as lateral movement, ransomware, or persistence.

While threat actors are typically known to deploy lightweight web shells (or reuse open-source variants like Behinder or China Chopper) as a way to maintain remote access to compromised systems and enable basic command execution capabilities, the latest development signals the use of a bespoke web shell that's tailored to the software being exploited.

The web shell is deployed following the weaponization of [CVE-2026-12569](https://thehackernews.com/2026/06/cisa-adds-exploited-ptc-windchill-rce.html) (CVSS score: 9.3), which relates to a case of improper input validation that could allow an attacker to execute arbitrary code by sending a malicious request to the network.

An advisory [released](https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html) by Ransom-ISAC along with eCrime.ch and Defused last month attributed the malicious activity to the Clop (aka Cl0p) ransomware operation, with the threat actor dropping JSP web shells against susceptible systems.

"The web shell gives attackers a direct path to credential theft and large-scale data exfiltration, with no additional tooling required," ReliaQuest said in a report shared with The Hacker News. "Unlike generic command shells, this implant decrypts credentials, delivers malware, and maps stored files for exfiltration."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The web shell is assessed to be an application-specific evolution of Cl0p's tried-and-tested mass-exploitation playbook, purpose-built to single out vulnerable PTC Windchill and FlexPLM instances.

"It embeds detailed knowledge of the application's APIs, database schema, keystore, and file-vault structure, enabling rapid movement from access to data theft, without external commands or additional tools," researchers John Dilgen and Connor Short said. "References to 'Clop' throughout reflect this highly likely attribution."

Because the targeted applications are used to store engineering data and product designs, a successful compromise can allow the attackers to obtain proprietary data from victims, as well as sensitive credentials that could be abused to laterally move into the network and reach other systems.

One of the notable features of the web shell is a single "S" command that returns Windchill's directory-management and administrative credentials in plaintext by making use of a built-in function called gs that performs the following steps -

* Reads Windchill's "ieStructProperties.txt" configuration file
* Decrypts the Lightweight Directory Access Protocol (LDAP) manager password from the application keystore
* Iterates through all stored local properties, decrypting additional encrypted values including administrative account credentials, object storage credentials, and all site administrator keys

In the case of active compromise, the "S" command can also be used to extract the credentials used to manage the organization's LDAP directory. A separate command is then used to exfiltrate the results.

"Because LDAP credentials typically govern access to Active Directory, email systems, VPN, and other enterprise services tied to directory authentication, their exposure could turn a single application compromise into an enterprise-wide credential compromise," ReliaQuest said. "The resulting privileged access fuels data theft from additional applications and storage locations, as well as persistence for follow-on attacks."

ReliaQuest told The Hacker News that the web shell supports the following commands -

* **S** — Returns Windchill credentials in plaintext
* **E** — Returns the parameter value directly, likely used to test connectivity
* **O** — Returns the operating system name
* **J** — Loads and executes a Java class from a ZIP via the class loader
* **D** — Runs the file download function
* **S** — Runs the credential harvesting function
* **L** — Runs the file vault enumeration and writes "flst.txt"
* **G** — Reads an arbitrary file from the file system
* **R** — Deletes a file; used for cleanup

What's more, the ability of the web shell to run attacker-supplied code in memory offers a pathway for deploying secondary payloads on demand, including tools for long-term persistence, network traversal, or data encryption. The payload takes the form of a Base64-encoded ZIP file containing compiled Java bytecode that's loaded directly into memory and executed.

Some of the functions baked into the web shell are as follows -

* A vault enumeration capability that targets the application database to identify high-value engineering data without executing manual discovery commands
* Executing queries through Windchill's existing database identity rather t...