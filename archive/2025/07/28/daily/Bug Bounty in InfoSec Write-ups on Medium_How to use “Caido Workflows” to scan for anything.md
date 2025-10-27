---
title: How to use “Caido Workflows” to scan for anything
url: https://infosecwriteups.com/how-to-use-caido-workflows-to-scan-for-anything-07eed72ba06a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-28
fetch_date: 2025-10-06T23:17:29.023819
---

# How to use “Caido Workflows” to scan for anything

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F07eed72ba06a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-use-caido-workflows-to-scan-for-anything-07eed72ba06a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-use-caido-workflows-to-scan-for-anything-07eed72ba06a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-07eed72ba06a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-07eed72ba06a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Press enter or click to view image in full size

![]()

Caido Workflow Coloring

# How to use “Caido Workflows” to scan for anything

[![Mostafa Alrefai](https://miro.medium.com/v2/resize:fill:64:64/1*Pn_PiqosLY-mT1QrIWI7kg.jpeg)](https://the7th.medium.com/?source=post_page---byline--07eed72ba06a---------------------------------------)

[Mostafa Alrefai](https://the7th.medium.com/?source=post_page---byline--07eed72ba06a---------------------------------------)

3 min read

·

Jul 26, 2025

--

1

Listen

Share

How to build Caido passive workflows to scan all HTTP requests & responses…

In this tutorial, I will guide you through the steps to build your custom Caido Workflows, which can help you identify bugs based on your methodology…

You can scan for patterns like API keys or tokens, or take it to the next level by integrating it with “Match & Replace” rules to inject payloads and match for high-impact bugs, such as OS command injection.

## Steps to create a new workflow

**There are two types of Caido workflows:**

* **Passive workflows** will run on all requests that will pass through Caido.
* **Active workflows** will wait until you choose a request and run that workflow manually on it.

In this tutorial, we will create a simple “passive workflow” that will scan for JWTs (JSON Web Tokens) in all responses. When it finds a token, it assigns the request a special color and creates a new finding.

1. First, go to the “Workflows tab”, choose the passive tab, and click “New Workflow”
2. By default, you will find the first step in the workflow layers as “On intercept request”; in our case, we want to scan the responses, so we will replace this first step with “On Intercept Response”.

Press enter or click to view image in full size

![]()

Make sure to choose the “On Intercept Response” as first step

3. The second step in the workflow is “Matches HTTPQL”. In the query (code), we will match for JWTs using the following regex query:

```
resp.raw.regex:/eyJ[a-zA-Z0-9]{10,}\.eyJ[a-zA-Z0-9]{10,}\.[a-zA-Z0-9_\-]{10,}/
```

Press enter or click to view image in full size

![]()

Step 3

4. After that, we will add the “Create Finding” and fill in the finding details like the following:

![]()

5. The last step is the “Set Color” step, which will change the color of the request that matches the query in the HTTP history tab. Here we can use a website like <https://htmlcolorcodes.com/> to choose our preferred colors. In this example, we can pick a blue color with code (#2874a6)

Press enter or click to view image in full size

![]()

The code is the string after the #

We can test the final setup with the new feature in Caido V0.50.0, or we can test it with the following JWT PortSwigger [lab](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature).

Press enter or click to view image in full size

![]()

New Caido future to test the new workflow

Finally, this is a very simple example to make it easy for you to set up your scans, which can be more advanced.

## Additional Tip

If you want to test for bugs like IDOR (Insecure Direct Object Reference) or Web Cache Deception, you should test each endpoint that will respond with the user’s email address.

To easily filter these endpoints, you can create a new Caido passive workflow, but you will change the “Matches HTTPQL” to match the email that you used to create the account. Normally, if you are doing bug bounty, you will sign up with the platform’s hunting email, so I created the following HTTPQL regex query that will match for the hunting emails of HackerOne, Bugcrowd, and Intigriti.

```
resp.raw.regex:"([a-zA-Z1-9]{1,}[+]{0,1}[a-zA-Z1-9]{0,}@bugcrowdninja[.]com|[a-zA-Z1-9]{1,}[+]{0,1}[a-zA-Z1-9]{0,}@wearehackerone[.]com|[a-zA-Z1-9]{1,}[+]{0,1}[a-zA-Z1-9]{0,}@intigriti[.]me)"
```

If you don’t want to create a full Caido workflow, you can use this HTTPQL query in the Caido search tab to filter these endpoints quickly.

For more info on Caido workflows, you can take a look at the [Caido docs](https://docs.caido.io/guides/workflows).

If you want to follow for more -> <https://x.com/__the7th>

[Hacking](https://medium.com/tag/hacking?source=post_page-----07eed72ba06a---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----07eed72ba06a---------------------------------------)

[Caido](https://medium.com/tag/caido?source=post_page-----07eed72ba06a---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----07eed72ba06a---------------------------------------)

[Web Development](https://medium.com/tag/web-development?source=post_page-----07eed72ba06a---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--07eed72ba06a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--07eed72ba06a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--07eed72ba06a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--07eed72ba06a---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--07eed72ba06a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updat...