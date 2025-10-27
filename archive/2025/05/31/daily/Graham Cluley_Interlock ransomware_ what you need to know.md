---
title: Interlock ransomware: what you need to know
url: https://www.tripwire.com/state-of-security/interlock-ransomware-what-you-need-know
source: Graham Cluley
date: 2025-05-31
fetch_date: 2025-10-06T22:37:24.226508
---

# Interlock ransomware: what you need to know

[Skip to main content](#main-content)

[![Fortra](https://static.fortra.com/fortra-global-assets/fortra-logo-full.svg?l=1189732032)
![Data Classification](https://static.fortra.com/fortra-global-assets/fortra-logo-small.svg?l=1952067292)

![Integrity and Compliance Monitoring](/themes/custom/tripwire/images/fta-integrity-and-compliance-monitoring-light.svg)](/ "Home")

[EN](/state-of-security/interlock-ransomware-what-you-need-know)

[EN](/state-of-security/interlock-ransomware-what-you-need-know)

Secondary Navigation

* [Customer Portal](https://customers.tripwire.com/customers)
* [Partner Portal](https://partners.tripwire.com/partners/)
* [GET A DEMO](/demo)

* Products
  Toggle Dropdown
  + [Tripwire Enterprise](/products/tripwire-enterprise)
  + [Tripwire ExpertOps](/products/tripwire-expertops)
  + [Tripwire IP360](/products/tripwire-ip360)
  + [Tripwire LogCenter](/products/tripwire-logcenter)
  + [View all products](/products)
* Solutions
  Toggle Dropdown
  + [Security Configuration Management](/solutions/security-configuration-management)
  + [File Integrity and Change Monitoring](/solutions/file-integrity-and-change-monitoring)
  + [Vulnerability Management](/solutions/vulnerability-and-risk-management)
  + [Cloud](/solutions/cloud-cybersecurity)
  + [Compliance](/solutions/compliance)
  + [Industries](/industries)
  + [View all solutions](/solutions)
* [Services](/services)
* Resources
  Toggle Dropdown
  + [Upcoming Events](/resources?f%5B0%5D=type%3A1333&f%5B1%5D=type%3A1340&f%5B2%5D=type%3A1341)
  + [On-Demand Webinars](/resources?f%5B1%5D=type%3A1339&f%5B2%5D=type%3A1342)
  + [Datasheets](/resources?f%5B0%5D=type%3A1335)
  + [Case Studies](/resources?f%5B0%5D=type%3A1334)
  + [Guides](/resources?f%5B0%5D=type%3A1337)
  + [Training](/services/training)
  + [View all resources](/resources)
* [Blog](/state-of-security)
* About
  Toggle Dropdown
  + [About](/about)
  + [Careers](https://www.fortra.com/about/careers)
  + [Leadership](https://www.fortra.com/about/our-leadership-team)
  + [Newsroom](https://www.fortra.com/about/newsroom)
  + [Partners](/about/partner)
  + [Contact Us](/contact-us)

Keywords

Sort
Best matchNewest firstOldest firstTitle A-ZTitle Z-A

1. [Home](/)
2. [Blog](/state-of-security)
3. Interlock ransomware: what you need to know

# Interlock ransomware: what you need to know

*Posted on May 30, 2025*

Image

[![interlock ransomware](/sites/default/files/2025-05/interlock.png)](https://www.tripwire.com/sites/default/files/2025-05/interlock.png "interlock ransomware")

Image

[![interlock ransomware](/sites/default/files/2025-05/interlock.png)](https://www.tripwire.com/sites/default/files/2025-05/interlock.png "interlock ransomware")

### What is the Interlock ransomware?

Interlock is a relatively new strain of ransomware, that first emerged in late 2024. Unlike many other ransomware families it not only targets Windows PCs, but also systems running FreeBSD.

If you are impacted, you will find that your files have not only been encrypted but have also had ".interlock" appended to their filenames. For example, a file named report.xlsx would become report.xlsx.interlock, visibly signaling that it has been encrypted by Interlock.

### And let me guess - it asks you to pay up for the decryption?

How did you know? Yes, as is so normal with cyber attacks these days, the malicious hackers will leave an extortion note on your system - telling you that you will need to pay a ransom for the decryption key that will unlock the encrypted files, and also to prevent the files from being published on the dark web.

Image

![ interlock-ransom-note](/sites/default/files/2025-05/interlock-ransom-note.jpeg)

### Do I need to take the threat seriously?

You would be sensible to treat any ransomware threat seriously.  Interlock's leak site on the dark web has made available terabytes of data stolen from scores of organisations.

### How do companies get hit by Interlock in the first place?

Interlock has been seen distributed via fake updates for browsers such as Google Chrome and Microsoft Edge, made available for download from compromised legitimate websites.

The fake installers for these updates run a PowerShell backdoor, and ultimately leads to the delivery of the ransomware.

### What makes Interlock different?

Aside from the ability to also attack FreeBSD systems, Interlock has also been observed using the ClickFix social engineering technique.

### ClickFix? What's that?

It is a social engineering tactic used by malicious hackers to trick users into copy-and-pasting malicious commands into their computers. The end result is often the installation of malware, remote access being granted to cybercriminals, or full system compromise.

For instance, a fake error webpage of CAPTCHA dialog may tell you to press a particular key sequence to verify yourself or "fix" a problem. Following the instructions actually sends a malicious command from your clipboard to the computer, which will end up with malicious code being run on your PC.

In October last year, the US Government [warned internet users to be vigilant of the ClickFix threat](https://www.hhs.gov/sites/default/files/clickfix-attacks-sector-alert-tlpclear.pdf "Link to US government warning"), giving the example of websites that impersonated Google, Facebook, reCAPTCHA, and others.

Every day thousands of people are falling for ClickFix scams, and helping their computers become infected as a result.

### Nasty. How do ransomware gangs like Interlock justify their activities?

In Interlock's case, they argue that they are trying to improve cybersecurity.

Image

![ interlock-manifesto](/sites/default/files/2025-05/interlock-manifesto.jpeg)

> We don’t just want payment; we want accountability. Our actions send a message to those who hide behind weak defenses and half-measures: your data is only as safe as the effort you put into protecting it. If you don’t take data security seriously, we will on your behalf. Pay attention or pay the price. In this digital age, there's no excuse for complacency. When companies neglect cybersecurity, we make them pay not just with ransoms, but with lessons they won’t forget. We are here to enforce the standards they fail to uphold.

### Does that justify what they do?

No, of course not. Notably hospitals and healthcare organisations have been amongst the ransomware's targets, which seems particularly callous.

### So how can my company protect itself from Interlock?

The [best advice](https://tripwire.com/state-of-security/ransomware-on-the-rise-how-to-keep-your-company-safe) is to follow the same recommendations on how to protect your organisation from any other type of ransomware. These include:

* making secure offsite backups.
* running up-to-date security solutions and ensuring that your computers are protected with the [latest security patches against vulnerabilities.](https://www.fortra.com/products/fortra-vulnerability-management)
* using hard-to-crack unique passwords to protect sensitive data and accounts, as well as enabling multi-factor authentication.
* encrypting sensitive data wherever possible.
* reducing the attack surface by disabling functionality that your company does not need.
* educating and informing staff about the risks and methods used by cybercriminals to launch attacks and steal data.

Stay safe folks.

---

***Editor’s Note: The opinions expressed in this and other guest author articles are solely those of the contributor and do not necessarily reflect those of Fortra.***

### Beating the Business of Ransomware

Learn how to beat cybercriminals’ ransomware business.

[Learn More](https://www.fortra.com/resources/guides/beating-the-business-of-ransomware)

[![Graham Cluley](/sites/default/files/styles/thumbnail/public/2022-10/graham-cluley_profile_pic.jpg?itok=ffTH8VnN)](/profile/graham-cluley)

Meet the Expert

#### [Graham Cluley](/profile/graham-cluley)

Cybercrime Researcher and Blogger

[View Profile](/profile/g...