---
title: Chaining a DOM XSS Sink, WAF Bypass, Cross-Origin Smuggling, and SDK Abuse into One Click Account…
url: https://infosecwriteups.com/chaining-a-dom-xss-sink-waf-bypass-cross-origin-smuggling-and-sdk-abuse-into-one-click-account-6c1a7095f8e1?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-07
fetch_date: 2026-07-08T05:04:09.681626
---

# Chaining a DOM XSS Sink, WAF Bypass, Cross-Origin Smuggling, and SDK Abuse into One Click Account…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fchaining-a-dom-xss-sink-waf-bypass-cross-origin-smuggling-and-sdk-abuse-into-one-click-account-6c1a7095f8e1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fchaining-a-dom-xss-sink-waf-bypass-cross-origin-smuggling-and-sdk-abuse-into-one-click-account-6c1a7095f8e1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6c1a7095f8e1---------------------------------------)

·

1. [1. Finding the Sink](/?source=post_page-----6c1a7095f8e1---------------------------------------#b7b4 "1. Finding the Sink")
2. [2. The Wall](/?source=post_page-----6c1a7095f8e1---------------------------------------#2513 "2. The Wall")
3. [3. The Payload](/?source=post_page-----6c1a7095f8e1---------------------------------------#12e8 "3. The Payload")
4. [4. The SDK](/?source=post_page-----6c1a7095f8e1---------------------------------------#993a "4. The SDK")
5. [5. The Chain](/?source=post_page-----6c1a7095f8e1---------------------------------------#52f1 "5. The Chain")
6. [6. Four Bugs, Not One](/?source=post_page-----6c1a7095f8e1---------------------------------------#2024 "6. Four Bugs, Not One")
7. [Takeways](/?source=post_page-----6c1a7095f8e1---------------------------------------#84c2 "Takeways")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6c1a7095f8e1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Chaining a DOM XSS Sink, WAF Bypass, Cross-Origin Smuggling, and SDK Abuse into One Click Account Takeover

[![Alvin Ferdiansyah](https://miro.medium.com/v2/resize:fill:64:64/1*jCQW4Dcioim59s1E0JwOqQ@2x.jpeg)](https://alvinferd.medium.com/?source=post_page---byline--6c1a7095f8e1---------------------------------------)

[Alvin Ferdiansyah](https://alvinferd.medium.com/?source=post_page---byline--6c1a7095f8e1---------------------------------------)

8 min read

·

Jun 27, 2026

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D6c1a7095f8e1&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fchaining-a-dom-xss-sink-waf-bypass-cross-origin-smuggling-and-sdk-abuse-into-one-click-account-6c1a7095f8e1&source=---header_actions--6c1a7095f8e1---------------------post_audio_button------------------)

Share

> There’s a browser property called **window.name** that’s easy to overlook because it behaves differently from what most browser state does, it persists across navigations. Whatever you set it to on your own page arrives intact in the next origin the tab visits, and if that origin evaluates it as code, you never had to put your payload in a URL at all. That’s the part Akamai never saw, and honestly one of the cleanest bypasses I’ve come across

I’ve been hunting on this large platform’s bug bounty program on HackerOne for a while. They have a broad wildcard scope and run Akamai in front of everything meaningful. That combination produces a specific kind of bug: the sink is usually there, the WAF is usually in the way, and the interesting question is always whether you can thread the payload through the gap between them.

This writeup is about a chain that took four independent defects to complete: *a DOM XSS* sink with no scheme validation, an *Akamai WAF* rule with a structural flaw, the *window.name property*’s unusual cross-origin behavior, and a first-party *authentication SDK* that hands over signed credentials to whoever executes JavaScript in its origin. Any one of those four things is a bug report on its own. Together they were a one-click account takeover that handed me the victim’s signed JWT and live AWS STS credentials in two separate AWS accounts.

## 1. Finding the Sink

I was reading the application’s JavaScript bundles looking for **open redirect sinks**, anything that consumes a URL parameter and passes it directly to location.assign, location.replace, or location.href. The error-page component stood out immediately.

The application handles a set of named error conditions, clock drift, filter failures, auth service timeouts, with a shared React component that renders a user-facing message and an action button. The button’s onClick handler reads a **backURL query parameter** and calls **window.location.assign** on it. Here’s the relevant function from the minified production bundle:

```
A = function(e){
var r = e.id, t = (0, k.zy)(), n = new URLSearchParams(t.search);
function o(e){
e.preventDefault();
var r = n.get("backURL");
("Reload Page" !== f && "Please try again." !== f) || !r
? window.location.assign(g || t.pathname)
: window.location.assign(r); // no validation
}
var s = O.$D[r], u = s.img, d = s.title, p = s.description, f = s.action, g = s.linkText;
return …<button onClick={o}>{f}</button>…;
}
```

window.location.assign executes a javascript: URL synchronously in the calling document’s origin. There is no scheme check, no host check, no sanitization. The only gate is that the button’s action label must be “*Reload Page*” or “*Please try again.*”, determined by the error type in the URL path, for the dangerous branch to run.

The cleanest entry point was an error path whose rendered button reads *“Reload Page”* and presents itself as a routine timing error. Nothing suspicious about the URL bar. It’s a real application domain throughout.

The sink is there. The problem is getting a javascript: payload through Akamai.

## 2. The Wall

Akamai’s WAF sits in front of the application. Send backURL=javascript:alert(1) and you get HTTP 403. Expected. The interesting question is what the rule actually looks like.

I started mapping it **systematically**, every encoding trick I knew:

```
javascript:alert(1) → 403
javascript:alert%28%29 → 403 (percent-encoded parens)
javascript:%2528%2529 → 403 (double-encoded)
javascript:eval(name) → 403
javascript:Function(name)() → 403
javascript:setTimeout(name) → 403
javascript:[].constructor.constructor(name)() → 403
javascript:({}).valueOf.constructor(name)() → 403
javascript:new Function(name)() → 403
javascript:document.body.innerHTML=… → 403
javascript:location='https://…' → 403
javascript:alert(1) → 403 (unicode escapes)
java%E2%80%8Bscript:alert(1) → 403 (zero-width space)
java%C0%80script:alert(1) → 403 (overlong UTF-8)
```

Getter tricks, backtick calls, throw expressions. All 403. After about eighty probes I stopped trying variants and started looking at the data differently. I wrote down what every blocked payload had in common, and separately what every passing payload had in common.

The pass...