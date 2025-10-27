---
title: I received a bounty of $60 for finding a critical bug in the patient management system.
url: https://infosecwriteups.com/i-received-a-bounty-of-60-for-finding-a-critical-bug-in-the-patient-management-system-560446c534e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-07-10
fetch_date: 2025-10-04T11:52:46.514802
---

# I received a bounty of $60 for finding a critical bug in the patient management system.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F560446c534e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-received-a-bounty-of-60-for-finding-a-critical-bug-in-the-patient-management-system-560446c534e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-received-a-bounty-of-60-for-finding-a-critical-bug-in-the-patient-management-system-560446c534e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-560446c534e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-560446c534e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# I received a bounty of $60 for finding a critical bug in the patient management system.

[![Krishnadev P Melevila](https://miro.medium.com/v2/resize:fill:64:64/1*QpBWYV2bZ8JJS9ZIHz-17A.png)](https://krishnadevpmelevila.medium.com/?source=post_page---byline--560446c534e---------------------------------------)

[Krishnadev P Melevila](https://krishnadevpmelevila.medium.com/?source=post_page---byline--560446c534e---------------------------------------)

2 min read

·

Jul 4, 2023

--

2

Listen

Share

Hi hackers,

My name is Krishnadev P Melevila, To know more about me, Just search “Who is Krishnadev P Melevila” On Google or Ask your Google Assistant.

Press enter or click to view image in full size

![]()

In my ongoing efforts to enhance the security landscape of web applications, I recently discovered a critical vulnerability on a healthcare platform. This vulnerability, which I reported on July 3rd, 2023, could potentially lead to an account takeover, posing a significant risk to patient data privacy. In this write-up, I aim to outline the details of the vulnerability while maintaining the confidentiality of the target platform.

**Vulnerability Details:**

Vulnerability Type: Account Takeover

Platform: Confidential

Impact Level: Critical

Risk: Patient account takeover leading to sensitive data loss

Priority: P1

**Steps to Reproduce the Vulnerability:**

1. Visit the platform’s website and navigate to the relevant login section.
2. Click on the “Forgot Password” option.
3. Enter a valid mobile number that is already registered as a user on the platform.
4. Enter the valid attacker’s OTP and click “Submit.”
5. Set a new password and submit the request while intercepting it using a web interceptor tool.

The Intercepted Request:

Below is an example of the intercepted request that exposes the vulnerability. Please note that specific details and target information have been redacted to ensure responsible disclosure.

**[Intercepted Request]**

> POST [URL] HTTP/2 Host: [Host] Cookie: [Redacted] Content-Length: 63 Cache-Control: max-age=0 Sec-Ch-Ua: “Not:A-Brand”;v=”99", “Chromium”;v=”112" Sec-Ch-Ua-Mobile: ?0 Sec-Ch-Ua-Platform: “Linux” Upgrade-Insecure-Requests: 1 Origin: [Origin] Content-Type: application/x-www-form-urlencoded User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7 Sec-Fetch-Site: same-origin Sec-Fetch-Mode: navigate Sec-Fetch-User: ?1 Sec-Fetch-Dest: document Referer: [Referer] Accept-Encoding: gzip, deflate Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
>
> mobile=[Redacted]&isdcode=91&pwd=Hello%402002&cpwd=Hello%402002

**Exploitation and Impact:**

It’s time to exploit:

By exploiting this vulnerability, an attacker can bypass proper authentication on the platform. The vulnerability stems from improper validation of the “**mobile**” parameter, allowing an attacker to reset the password of any user account by modifying the request. This could result in unauthorized access to sensitive user information, including personal and private data.

I reported it to the affected organization, and they triaged my report in minimum time and rewarded me with a bounty of $60.

***Don’t forget to follow me on medium and other social media. Also please give your 50 claps for this write-up and that’s my inspiration to write more!!***

*My Instagram handle:* [*https://instagram.com/krishnadev\_p\_melevila*](https://instagram.com/krishnadev_p_melevila)

*My Twitter handle:* [*https://twitter.com/Krishnadev\_P\_M*](https://twitter.com/Krishnadev_P_M)

*My LinkedIn handle:* [*https://www.linkedin.com/in/krishnadevpmelevila/*](https://www.linkedin.com/in/krishnadevpmelevila/)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----560446c534e---------------------------------------)

[Burpsuite](https://medium.com/tag/burpsuite?source=post_page-----560446c534e---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----560446c534e---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----560446c534e---------------------------------------)

[Broken Authentication](https://medium.com/tag/broken-authentication?source=post_page-----560446c534e---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--560446c534e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--560446c534e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--560446c534e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--560446c534e---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--560446c534e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Krishnadev P Melevila](https://miro.medium.com/v2/resize:fill:96:96/1*QpBWYV2bZ8JJS9ZIHz-17A.png)](https://krishnadevpmelevila.medium.com/?source=post_page---post_author_info--56...