---
title: Analyzing an American Express Phishing Campaign
url: https://blog.spookysec.net//amex-phish-analysis/
source: Ronnie's Blog
date: 2026-01-20
fetch_date: 2026-01-21T03:31:38.931609
---

# Analyzing an American Express Phishing Campaign

λ

* 1
* /amex-phish-analysis/
* ⌘ blogspace λ
* \* Menu

* utf-8
* web
* .html

* 1

   [home](https://blog.spookysec.net//)
* 2

   [my posts](https://blog.spookysec.net//posts)
* 3

   [tags](https://blog.spookysec.net//tags)

### \*Posts\*

[## Analyzing-an-American-Express-Phishing-Campaign.md](/amex-phish-analysis/ "Open the post")

[## 2024-CISA-ICS-CTF---Register-the-Dots.md](/CISA-ICS-CTF-Reg-the-Dots.md/ "Open the post")

[## 2024-CISA-ICS-CTF---Read-Askew-Manuscripts.md](/CISA-ICS-CTF-RAM.md/ "Open the post")

[## 2024-CISA-ICS-CTF---Mission-Inconceivable.md](/CISA-ICS-CTF-Mission-Inconceivable.md/ "Open the post")

[## 2024-CISA-ICS-CTF---Modeling-Trains.md](/CISA-ICS-CTF-Mdl-Trains.md/ "Open the post")

[## 2024-CISA-ICS-CTF---Follow-the-Charts.md](/CISA-ICS-CTF-Follow-the-Charts.md/ "Open the post")

[## 2024-CISA-ICS-CTF---Extend-Your-Stay.md](/CISA-ICS-CTF-Extend-Your-Stay.md/ "Open the post")

[## ROP-Emporium---Split.md](/ROP-Emporium-Split32/ "Open the post")

[## ROP-Emporium---Ret2Win.md](/ROP-Emporium-ret2win/ "Open the post")

[## Deception-in-Depth---Overview-of-Kerberos,-Service-Accounts-&-Attacks---Part-1.5.md](/DnD-Kerberos-Service-Accounts-%26-Attacks-pt-1.5/ "Open the post")

[## Deception-in-Depth---Hiding-AD-Users-and-Groups---Part-1.md](/DnD-Hiding-Users-and-Groups/ "Open the post")

[## Backdooring-KeePass-for-Fun-and-Profit.md](/Backdooring-KeePass/ "Open the post")

[## Deploying-BloodHound-Community-Edition-for-Pentesters.md](/Deploying-BHCE/ "Open the post")

[## Enriching-BloodHound-Data.md](/Enriching-BloodHound-Data/ "Open the post")

[## Programming-with-Impacket---Working-with-SMB.md](/Programming-with-Impacket.md/ "Open the post")

[## Source-Zero-Con-Writeup---Biscuits.md](/2023-SZC-Biscuits/ "Open the post")

[## Source-Zero-Con-Writeup---Compromised.md](/2023-SZC-Compromised/ "Open the post")

[## Recovering-Your-Straight-Talk-Account-Number.md](/recovering-straighttalk-account-number/ "Open the post")

[## Deception-in-Depth---Building-Deceptions-from-Breaches.md](/DnD-building-from-breaches/ "Open the post")

[## Deceiving-Bloodhound---Remote-Registry-Session-Spoofing.md](/DnD-Deceiving-BH/ "Open the post")

[## Analyzing-a-Brute-Ratel-Badger.md](/analyzing-brc4-badgers/ "Open the post")

[## Cobalt-Strike-Beacon-Analysis-from-a-Live-C2.md](/cs-beacon-analysis/ "Open the post")

[## Source-Zero-Con-CTF---STL-Killer.md](/szc-stl-killer/ "Open the post")

[## Source-Zero-Con-CTF---Baby-XBee-1-2.md](/szc-rev-eng/ "Open the post")

[## Building-an-Active-Directory-Lab---Part-2.md](/ad-lab-2/ "Open the post")

[## Deception-in-Depth---Spoofing-SMB-User-Sessions-Improved.md](/DnD-SMB-Session-Spoofing-Improved/ "Open the post")

[## Staged-vs-Stageless-Payloads.md](/stage-v-stageless-1/ "Open the post")

[## Building-an-Active-Directory-Lab---Part-1.md](/ad-lab-1/ "Open the post")

[## Email-Spoofing---A-Full-Guide.md](/email-spoofing/ "Open the post")

[## OverWolfHelperx64---DLL-Injection-LOLBAS.md](/overwolf-dllinjection/ "Open the post")

[## Deception-in-Depth---LSASS-Injection.md](/DnD-LSASS-Injection/ "Open the post")

[## Deception-in-Depth---Spoofing-Logged-in-Users.md](/DnD-Spoofing/ "Open the post")

[## How-Secure-is-Kali-Out-of-the-Box?.md](/kali-ootb/ "Open the post")

[## Remote-NTLM-Relaying-via-Meterpreter.md](/remote-ntlm-relaying/ "Open the post")

[## Certification-Talk.md](/certifications/ "Open the post")

[## Google-Is-Your-Best-Friend.md](/google/ "Open the post")

[## Decrypting-TACACS+-Traffic-in-Wireshark.md](/tacacs-wireshark/ "Open the post")

[## CVE-2020-12447-LFI-Within-Onkyo-TX-NR585-Web-Interface.md](/onkyo-lfi/ "Open the post")

[## CVE-2020-11799---Z-Cron-Lack-of-Access-Control.md](/zcron/ "Open the post")

[## Finding-API-Keys-on-Github.md](/api-keys/ "Open the post")

[## DC-Sync---The-Downfall-of-your-Network.md](/domain-controller-sync/ "Open the post")

[## Quering-and-Cracking-Kerberos-Tickets!.md](/kerberos-abuse/ "Open the post")

[## CTF---B-Sides-Fredericton-CTF.md](/bsides-writeup/ "Open the post")

[## Linksys-EA6100-Firmware-Reverse-Engineering.md](/linksysre/ "Open the post")

[## The-BlueKeep-Module.md](/bluekeep/ "Open the post")

[## Web---IP-Grabbing-Redirects.md](/redirects/ "Open the post")

[## Post-Exploitation---Pivoting-with-SSHuttle.md](/Pivoting/ "Open the post")

[## Post-Exploitation---File-Transfer.md](/file-transfer/ "Open the post")

[## Exploitation-and-Post---Maintaining-Access.md](/post-exploit/ "Open the post")

20 Jan 2026

# Analyzing an American Express Phishing Campaign

**This post was written as part of my internship with SANS Internet Storm Center.**

To stay in tune with current threats in the cybersecurity landscape, it’s important to periodically review the various threat actors attacking organizations. Having a good working relationship with your Cyber Threat Intelligence (CTI) team can certainly help educate you on the current landscape, but nothing quite beats looking at an actual phishing campaign itself. Phishing is a massive threat to organizations of all sizes, from small businesses to large enterprises. The severity and impact of these campaigns vary, ranging from the execution of malware to the harvesting of credentials and personal data.

Today, we’ll be performing an analysis of a phishing campaign targeting personal and financial data. This specific campaign impersonates American Express and was sent on January 2, 2026.

## Email Analysis

The email employs a sense of urgency, a common tactic in Phishing campaigns. It claims that if the end-user doesn’t act by clicking the link and entering their data, they will lose access to their account. This is designed to lure the victim into an emotional state, hoping they will act without thinking to ensure their access isn’t disrupted. This theme is consistent throughout the body and the subject line of the email.

![Pasted image 20260102224658.png](https://blog.spookysec.net/img/Pasted image 20260102224658.png)

On the surface, it may look like a standard email from American Express, but a thorough evaluation of the text reveals several mistakes. It contains grammatical errors that should stand out as anomalous to the user, such as: `For your security, Verification Link is only active for 17hours` (which should be “the verification link is only active for 17 hours”) and `after one-time verification, Your access to your American Express account will continue to be active`(which should be “after a one-time verification, your access…”), and so on.

### Header Analysis

Email headers can provide additional insight, as they may showcase adversary infrastructure crucial to an investigation. In this case, the sender’s email domain was `secure.net`. This is not an American Express domain, nor is it their email provider, which is an immediate red flag.

![Pasted image 20260103131314.png](https://blog.spookysec.net/img/Pasted image 20260103131314.png)

ProofPoint reported that an IP address (204[.]199[.]139[.]130) was likely forged during email delivery; a PTR lookup on that IP attributes it to CenturyLink and Cirion Technologies Solutions.

![Pasted image 20260103132251.png](https://blog.spookysec.net/img/Pasted image 20260103132251.png)

In addition, the mail server that delivered the mail was not attributable to mx record for secure.net. With that said there are no SPF or DMARC records governing who can send mail and what to do with it for the domain secure.net either, this can be seen in the email header at the time of receipt, or looked up online via [mxtoolbox](https://mxtoolbox.com/), or manually inspecting DNS records using a tool like `dig` or `nslookup`.

![Pasted image 20260103133022.png](https://blog.spookysec.net/img/Pasted image 20260103133022.png)

The last notable piece of information that can be found while reviewing the email headers is that the victim’s User ID is contained within the senders email address. This is an interesting indicator for threat hunters: insta...