---
title: Dahua Camera Backdoor Survives Password Changes and Factory Resets on Compromised Devices
url: https://cybersecuritynews.com/dahua-camera-backdoor/
source: Instapaper: Unread
date: 2026-09-08
fetch_date: 2026-09-09T06:57:03.728942
---

# Dahua Camera Backdoor Survives Password Changes and Factory Resets on Compromised Devices

[Linkedin](https://www.linkedin.com/company/cybersecurity-news/ "Linkedin")

[Naver](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en "Naver")

[RSS](https://cybersecuritynews.com/feed/ "RSS")

[Twitter](https://twitter.com/The_Cyber_News "Twitter")

* [Home](https://cybersecuritynews.com/)
* [Threats](https://cybersecuritynews.com/category/threats/)
* [Cyber Attacks](https://cybersecuritynews.com/category/cyber-attack/)
* [Vulnerabilities](https://cybersecuritynews.com/category/vulnerability/)
* [Breaches](https://cybersecuritynews.com/category/data-breaches/)
* [Top 10](https://cybersecuritynews.com/category/top-10/)

Search

[![Cyber Security News](https://cybersecuritynews.com/wp-content/uploads/2025/05/Cyber-Security-News-Logo.webp "Cyber Security News")Cyber Security NewsLatest Cyber Security News](https://cybersecuritynews.com/ "Cyber Security News")

Wednesday, September 9, 2026

[Linkedin](https://www.linkedin.com/company/cybers%E4%B8%80security%E4%B8%80news/ "Linkedin")

[RSS](https://cybersecuritynews.com/feed/ "RSS")

[Twitter](https://x.com/The_Cyber_News "Twitter")

[WhatsApp](https://whatsapp.com/channel/0029VbDC7Ji8PgsNa4m6J82w "WhatsApp")

[Google News](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en "Google News")[Google News](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en)

[![Cyber Security News](https://cybersecuritynews.com/wp-content/uploads/2025/05/Cyber-Security-News-Logo.webp "Cyber Security News")Cyber Security NewsLatest Cyber Security News](https://cybersecuritynews.com/ "Cyber Security News")

* [Home](https://cybersecuritynews.com/)
* [Threats](https://cybersecuritynews.com/category/threats/)
* [Cyber Attacks](https://cybersecuritynews.com/category/cyber-attack/)
* [Vulnerabilities](https://cybersecuritynews.com/category/vulnerability/)
* [Breaches](https://cybersecuritynews.com/category/data-breaches/)
* [Top 10](https://cybersecuritynews.com/category/top-10/)

[Follow on LinkedIn](https://www.linkedin.com/company/cybers%E4%B8%80security%E4%B8%80news/ "Follow on LinkedIn")

Search

[Home](https://cybersecuritynews.com/)[Cyber Security News](https://cybersecuritynews.com/category/cyber-security-news/ "View all posts in Cyber Security News")

# Dahua Camera Backdoor Survives Password Changes and Factory Resets on Compromised Devices

[![Tushar Subhra Dutta](https://secure.gravatar.com/avatar/f8bc0247220c7d4dea6c8b5a77d910613305ead17b13c2a7920b400435a848dd?s=26&d=mm&r=g)](https://cybersecuritynews.com/author/tushar/ "Tushar Subhra Dutta")

By [Tushar Subhra Dutta](https://cybersecuritynews.com/author/tushar/)

September 4, 2026

[![](https://cybersecuritynews.com/wp-content/uploads/2026/04/Google-Prefered.svg "Google Prefered")](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2Fpreferences%2Fsource%3Fq%3Dcybersecuritynews.com&dsh=S-1711039385%3A1777114446800583&hl=en-IN&rip=1&sacu=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AT1y2_WJowZHdf0E80itpn_VjD7EqSL_cDLxwrMfAAoXv5E9mGOhMTOdqeDczZHvxM8Lfmw6HNjt)[![](https://cybersecuritynews.com/wp-content/uploads/2026/04/Google-news.svg "Google news")](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en)

[![Dahua Camera Backdoor Survives Password Changes and Factory Resets on Compromised Devices](https://cybersecuritynews.com/wp-content/uploads/2026/09/Dahua-Camera-Backdoor-Survives-Password-Changes-and-Factory-Resets-on-Compromised-Devices-696x392.webp "Dahua Camera Backdoor Survives Password Changes and Factory Resets on Compromised Devices")](https://cybersecuritynews.com/wp-content/uploads/2026/09/Dahua-Camera-Backdoor-Survives-Password-Changes-and-Factory-Resets-on-Compromised-Devices.webp)

A large campaign has compromised more than 14,000 internet-connected Dahua cameras, exposing how vulnerable surveillance equipment can become a gateway to video feeds and device settings.

The operation ran for 35 days, and hit devices worldwide, with confirmed compromises centered in Ukraine and Russia. It shows how unattended devices can create durable, long-lasting hidden access for intruders.

The operator scanned for exposed camera management services, tried weak credentials, and used two known authentication-bypass flaws against unpatched devices.

It also used a cloud relay path that can reach cameras behind network address translation by serial number, so even non-public devices could be targeted.

Analysts at Hunt.io identified the activity after finding an openly exposed operator directory containing 2,616 files and campaign tooling.

[Hunt.io said in a report](https://hunt.io/blog/operation-cameraswarm-dahua-cameras-compromised) shared with Cyber Security News (CSN) the recovered material revealed parallel attack paths, persistent access, and an unrelated Windows payload.

The impact goes beyond unauthorized viewing. The toolkit collected credentials, captured camera snapshots, and exported device records in a format designed for large-scale administration.

![Attack chain (Source - Hunt.io)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiigS0ARS9ZF-XJ1l7sTyCc1bLFun_-zwbVsCkwenHu2RyMdQSu4XtSws7KYe3OjK2ctzkTjvdyDK29l6b4oQFPn3Pv1Oqy2D7GG5arNXFmox9lnfGrMiwMmALPeUKfmPeQRneUvOWIHZbrCP7QjX4lBHgN8H9DtXxAHoZYFBHKaTIAnJP0R9TLrTQgR3c/s1600/Attack%20chain%20(Source%20-%20Hunt.io).webp)

Attack chain (Source – Hunt.io)

Researchers also found offline recovery-code generation, creating a route to administrative resets that can remain useful even after a device owner changes a password.

## **Dahua Camera Backdoor Survives Password Changes**

The most serious finding is persistence. After gaining administrator access through CVE-2021-33044 or CVE-2021-33045, the tool adds a separate account through the camera’s remote management interface.

That account is stored independently from the main administrator password, so changing the password does not remove it. On most affected firmware, a factory reset also fails to erase the hidden access. Hunt.io counted 1,923 cameras carrying the account.

That changes the response from a routine password reset into a compromise investigation, especially for organizations using cameras at sensitive sites.

The two flaws used for initial entry have patches available, yet exposed and unpatched cameras remain attractive targets. Readers can see why direct exposure matters in this coverage of [threat actors targeting IP cameras](https://cybersecuritynews.com/threat-actors-intensify-targeting-of-ip-cameras/), which also tracks authentication weaknesses affecting surveillance devices.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2ok3bLiU-DaNGHLOc4F2zDKU_NRrH8dXFBwS1h1MUeqpxjI2J28i9Y04OaVgq0Bj9I9vgPy7MyQoHkFATEr9GeI3GMP_UI-l5HK3m2X3TzM5rgXCLo98ZcA0vHKWFyGU5wI_BMmypeYhEb71IudSBJy8nCHkb75Dg7pORrMB2QOpdMatdKc-dwvJJBNM/s1600/async_brute.py%20(Source%20-%20Hunt.io).webp)

async\_brute.py (Source – Hunt.io)

One exploit path impersonates a trusted hardware controller, while the other claims the request came from the camera itself. Both can provide administrator access without a valid password.

Researchers cautioned that a label used in the toolkit for the persistent-account technique points to an unrelated vulnerability, so defenders should focus on the observed behavior rather than that incorrect identifier.

## **Recovery Codes Expand Risk**

The campaign also abused a cloud relay capability to find and contact cameras using serial numbers. According to the recovered logs, 89.4 percent of live serials tested returned a channel that did not require authentication.

That route can bypass the protection normally offered by placing a camera behind a...