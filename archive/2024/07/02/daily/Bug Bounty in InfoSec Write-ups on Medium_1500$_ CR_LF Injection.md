---
title: 1500$: CR/LF Injection
url: https://infosecwriteups.com/1500-cr-lf-injection-0d2a75f02ef3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-02
fetch_date: 2025-10-06T17:42:26.570610
---

# 1500$: CR/LF Injection

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0d2a75f02ef3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1500-cr-lf-injection-0d2a75f02ef3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1500-cr-lf-injection-0d2a75f02ef3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40a13h1)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0d2a75f02ef3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0d2a75f02ef3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 1500$: CR/LF Injection

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:64:64/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---byline--0d2a75f02ef3---------------------------------------)

[Abhi Sharma](https://medium.com/%40a13h1?source=post_page---byline--0d2a75f02ef3---------------------------------------)

3 min read

·

Mar 23, 2024

--

9

Listen

Share

Hi Everyone, How you all doing. In this article, I’m going to talk about a CR/LF bug I discovered in an private program which i m going to represent as Exahub that allowed me to get paid 1500$ in bounty.

Press enter or click to view image in full size

![]()

> **Understanding CR/LF (Carriage Return/Line Feed) Injection**

CR/LF (Carriage Return/Line Feed) injection is a type of security vulnerability. CR/LF refers to a sequence of two ASCII control characters: Carriage Return (CR, ASCII code 13) and Line Feed (LF, ASCII code 10). These characters are used in text files to signify the end of a line and control the positioning of the cursor or print head when displaying or printing text. CR/LF injection vulnerabilities occur when attackers insert CR/LF characters into input fields, file extensions or file uploads to manipulate application behavior. This can lead to exploits such as altering headers, injecting malicious code, or manipulating file content.

> **Understanding the target: Exahub**

ExaHub (Virtual name of private program) is a platform tailored for enthusiasts and professionals alike who work with the Exa programming language. Exa, a high-level programming language renowned for its speed and performance, has gained significant traction in fields like scientific computing, machine learning, and data science. ExaHub serves as a centralized hub where users can access a range of resources, collaborate on projects, and leverage tools tailored to the Julia ecosystem. From project management to data visualization, ExaHub provides a suite of features designed to streamline development workflows and foster community engagement.

> **Understanding the Issue:**

The vulnerability identified in ExaHub revolves around CR/LF injection during file uploads. This flaw allows malicious actors to manipulate headers, potentially leading to cookie manipulation and forced logout of other users. The root cause of this issue lies in inadequate input validation during the file upload process.

## Steps to Reproduce:

1. Access your ExaHub account.
2. Navigate to the “Files” section.
3. Upload a file and intercept the uploading request.
4. Modify the Content-Disposition header by appending the payload %0AClear-Site-Data%3A%22cookies%22%0A after the filename.
5. Send the modified request and attempt to download the uploaded file.
6. When other user download the file they got locked out this is one of the multiple task which can be performed by cr/lf injection.

Press enter or click to view image in full size

![]()

> **Potential Exploits:**

Apart from forced logout and session manipulation, attackers can exploit this vulnerability to manipulate and set cookies of other users. By injecting payloads such as %0ASet-Cookie%3A+crlfinjection%3D+value+ , or for xss

```
 • /%3f%0d%0aLocation:%0d%0aContent-Type:text/html%0d%0aX-XSS-Protection%3a0%0d%0a%0d%0a%3Cscript%3Ealert%28document.domain%29%3C/script%3E ``
```

they can hijack sessions, gain unauthorized access, or execute other malicious activities.

> **Response and Resolution:**

Upon reporting the issue, the ExaHub security team promptly acknowledged its validity and initiated a fix. While the severity was initially classified as critical, further analysis revealed a high severity rating. As a token of appreciation for the responsible disclosure, EXAHub awarded a $1,500 bounty to the individual who identified the vulnerability.

![]()

> **Takeaway:**

Always be thorough in your testing and try injecting various payloads, including special characters like CR/LF. You never know what vulnerabilities you might uncover, and by testing comprehensively, you can discover and address potential security risks before they can be exploited by malicious actors. Remember, thorough testing is key to ensuring the security and integrity of your systems and applications.

> *Leave some clap if you enjoyed this read, leave your feedback in comment and consider following me for more exciting findings.*

[buymeacoffee.com/a13h](https://www.buymeacoffee.com/a13h1)1

![]()

> *Find me on Twitter:* [*@a13h1\_*](https://twitter.com/a13h1_)

## Thank you everyone

Keep Supporting, Keep Clapping, Keep Commenting.

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----0d2a75f02ef3---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----0d2a75f02ef3---------------------------------------)

[Crlf Injection](https://medium.com/tag/crlf-injection?source=post_page-----0d2a75f02ef3---------------------------------------)

[Programming](https://medium.com/tag/programming?source=post_page-----0d2a75f02ef3---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----0d2a75f02ef3---------------------------------------)

--

--

9

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0d2a75f02ef3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0d2a75f02ef3---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0d2a75f02ef3---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--0d2a75f02ef3---------------------------------------)

·[Last p...