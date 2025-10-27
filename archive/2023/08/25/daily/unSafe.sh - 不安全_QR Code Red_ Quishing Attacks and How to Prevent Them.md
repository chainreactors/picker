---
title: QR Code Red: Quishing Attacks and How to Prevent Them
url: https://buaq.net/go-175313.html
source: unSafe.sh - 不安全
date: 2023-08-25
fetch_date: 2025-10-04T11:59:29.443002
---

# QR Code Red: Quishing Attacks and How to Prevent Them

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/8afeb61b48d342c4181b3942b4444c15.jpg)

QR Code Red: Quishing Attacks and How to Prevent Them

Scan at Your Own Risk: QR Code as a ThreatQR codes that re-emerged into our lives during th
*2023-8-24 22:42:16
Author: [perception-point.io(查看原文)](/jump-175313.htm)
阅读量:16
收藏*

---

## **Scan at Your Own Risk: QR Code as a Threat**

QR codes that re-emerged into our lives during the COVID-19 pandemic have given rise to a new wave of advanced phishing attacks targeting thousands of organizations worldwide. These evasive threats also known as **quishing** (QR phishing), lure end users into scanning a QR code sent to them via email using their mobile device camera, redirecting them to malicious websites aiming to steal their login credentials, harvest financial information, or infect their devices with malware.

Recently, quishing has become a highly popular tool among cybercriminals, as it lets them easily bypass traditional email security systems and phishing filters to deliver their malicious payload directly to their targets. The [FBI issued an official warning](https://www.ic3.gov/Media/Y2022/PSA220118) in 2022, highlighting the increasing use of QR codes by threat actors.

*Quishing kill-chain – how QR code phishing attack looks like*

## **The Quishing Quandary: Phishing Evolved**

In 2019, receiving an email containing a QR code would have likely raised some eyebrows, appearing strange and suspicious to the recipient. Fast forward to the year 2023, and the situation has dramatically changed. The widespread adoption of QR codes for everything from viewing restaurant menus to online payments and public transport apps has conditioned many of us to respond almost instinctively. The sight of a QR code in an email or text message acts like a “Pavlovian cue,” prompting us to unthinkingly reach for our phones, ready to scan.

This shift in human behavior was noticed by threat actors, who are now capitalizing on the “conditioned” trust in QR codes to launch increasingly sophisticated phishing attacks. Despite the fact that the core principles of phishing remain largely unchanged, quishing makes the threat more complex and much harder to detect. By hiding the malicious link behind a QR code, threat actors force the victims to move from a laptop or a desktop to their mobile devices, which in most cases have much weaker cyber defenses.

Quishing utilizes another psychological maneuver that greatly benefits the attackers and increases their success rates. Quishing moves the “playground” onto a mobile phone where the victims are primed for additional steps that involve their personal device. **With the phone in their hands, the cognitive journey users must take for going through Multi-Factor Authentication (MFA) is significantly shorter, and the chances of the user inserting SMS verification codes, tapping a prompt on the screen or using biometric authentication (facial recognition or fingerprint scanning) are much higher.**

![](https://lh5.googleusercontent.com/IQR_mexrvkzgAvxDeB90F63-Hci37Ngz47Kn8JqCjxjEABCECzM3Yg5okQvyRn8LlokZg9iUwcUan2RTHTKP2kzXt9JMHBUmPjgx4S6XQC5ZAc7DAbAlqqMOedrH_YI-jnHhiwf93s3rTihlThOYAY4)

*The CEO almost fell victim to quishing attack – a tale from a /sysadmin sub-Reddit*

## **Undetectable? The Deceptive Simplicity of Malicious QR Codes in Emails**

Quick Response (QR) codes are essentially a graphical representation of data, mostly used to encode URLs, the process of converting a link into a QR code takes seconds and can be easily done by anybody with online access (there are hundreds of free QR generators available).

When a malicious URL is hidden behind a QR code, the link becomes an image file, not a clickable element. Traditional email security systems like [secure email gateways](https://perception-point.io/blog/segs-vs-ices-solutions-the-complete-guide/) (SEGs) and even the most modern email security solutions scan for suspicious links in the email body of the message to prevent phishing attacks (relying on domain reputation and other indicators), but may overlook embedded URLs within images or file attachments. ***Most security solutions are unable to extract and dynamically scan links from QR codes.***

Quishing campaigns present a unique challenge to defenders. By embedding the phishing link within a QR code, the threat is effectively concealed, rendering security measures ineffective and allowing malicious emails to slip through and reach the inbox of targeted end users.

In addition to the technicalities involving the malicious URL delivery, threat actors often craft their QR codes, the look and feel of the email, and the associated phishing site to impersonate known and trusted brands. It is very common to see logos and domain names that mimic Microsoft or Google in quishing campaigns. Social engineering techniques also play a major role in quishing where cybercriminals employ scare tactics and incite urgency (“your password is about to expire”) to encourage the users to scan the QR code without questioning its legitimacy.

## **Quishing Impossible: a Look at Examples From the Wild**

Perception Point’s security research team has observed a substantial increase in quishing campaigns. Let’s review 2 examples caught by Perception Point to better understand the modus operandi of threat actors that employ quishing attacks.

**Quishing 1: QR Code Embedded Within the Email Body as an Image**

* Email subject: <COMPANY NAME>, Multi-Factor Auth
* Sender display name: <COMPANY NAME> 2FA Security <[[email protected]](https://perception-point.io/cdn-cgi/l/email-protection) DOMAIN>

![](https://lh3.googleusercontent.com/odYPHFa5v1QTNYd1qbB1TwN34dc5r5RTNluJ_oMq4Xg1SuY8kCD48KAxkW8lZKF7g1FzsmBj1tHtbQxFmSzv_yPhKH5kdDIbuZih7sS7cUvxnLjBXRHEi9UxRsomu5zCGM57Px0oywVJQKnvjixTcq8)

In this particular quishing campaign sent to multiple targets within many organizations, the threat actors impersonate Microsoft 365 and alert the end user about their “network password” that has expired. The message encourages the recipient to scan the QR code using their mobile camera for “connecting” MFA method to their Microsoft account. The sender’s name and email subjects were altered to fit the target company.

**The text, logos and the QR code are actually a single image and the email body contains no textual data at all.**

End users that would have fallen for the quishing scam and actually scan the code would have been presented with a Microsoft lookalike page that automatically redirects them to a fake login page aimed to steal their account credentials.

![](https://lh4.googleusercontent.com/qmAMEEPdOlWX5N1sxgrK0L9uz9_OWpSjydOFWJs4YIb50nKV5w7IH4ZghKqf7ewxb5alIAgtiIXttv4kzsQKvZDGmTw5Y3iYhvKoMGIzEK5jkjSfeO58JBrsPxE5PldpsMrEEM_5DPVW8XTQpuSii8c)

**Quishing 2: QR Code Inside a PDF attachment**

* Email subject: <COMPANY NAME> 2FA Salary Report For <TARGET NAME> Completed August 22, 2023
* Sender display name: Payroll UPDATE
* File attachment name: 2FA <TARGET NAME> Salary Authenticator August 22, 2023.pdf

![](https://lh6.googleusercontent.com/TOgyDAZ3_2l3NPRh9hGwAbBUZFjm6XM16vSdIwFp0VcNjQpCaQ-lJHyaNdfuFc1lvR6uyrjBIW9G-3-_CZ-A2dxsmrRrEc5v6TXUYmZ-OCs3jUajNmuM8C6Xc_5nFyITax-QtRWMDzs99Bx_sfZGhSg)

Here we have another quishing sample where the malicious QR code is hidden inside an attachment to the email – a PDF file. The social engineering behind this campaign revolves around the financial motivation of the targets. The email subject, sender’s name and the PDF file attached all indicate a vague requirement to complete some sort of Two-Factor authentication (2FA) regarding the target’s...