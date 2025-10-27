---
title: Evilginx Pro 4.2 - Anti-phishing evasions and more!
url: https://breakdev.org/evilginx-pro-4-2/
source: BREAKDEV
date: 2025-08-15
fetch_date: 2025-10-07T00:48:02.237636
---

# Evilginx Pro 4.2 - Anti-phishing evasions and more!

[![BREAKDEV](https://breakdev.org/content/images/2022/08/breakdev_logo_with_title.png)](https://breakdev.org)

* [Home](https://breakdev.org/)
* [Evilginx Pro](https://evilginx.com)
* [Evilginx Mastery](https://academy.breakdev.org/evilginx-mastery)
* [Tools](https://github.com/kgretzky)
* [Contact](https://breakdev.org/contact/)

[evilginx](/tag/evilginx/)

 Featured

# Evilginx Pro 4.2 - Anti-phishing evasions and more!

The latest update includes a complete proxy engine rewrite, new anti-phishing evasions, added support for new DNS providers, custom hostnames for lure URLs, better Gophish integration and more!

* [![Kuba Gretzky](/content/images/size/w100/2022/08/avatar512.png)](/author/kuba/)

#### [Kuba Gretzky](/author/kuba/)

Aug 14, 2025
• 17 min read

![Evilginx Pro 4.2 - Anti-phishing evasions and more!](/content/images/size/w2000/2025/08/evilginx-pro-42-update.png)

It's been about five months, already, since the release of Evilginx Pro, and I'm proud to release the second major update. This release was hugely influenced by the feedback I received from multiple [**Evilginx Pro**](https://evilginx.com)users I met at the [x33fcon](https://www.x33fcon.com/) conference, which took place in Gdynia in June 2025. Being able to communicate with you directly to exchange ideas and learn how you use the tool gives me confidence that I'm moving in the right direction with the implementation of new features.

[Click here to learn more about Evilginx Pro](https://evilginx.com)

At **x33fcon** this year, I also had the opportunity to give a talk about the various anti-phishing techniques I've come across in recent years and how an attacker would approach to evade them. The video of the talk can be found below:

Wise Phishermen Never Trust the Weather - Kuba Gretzky @ x33fcon 2025

I've recently released the [4.2 update](https://help.evilginx.com/pro/changelog#420-2025-07-18) for [**Evilginx Pro**](https://evilginx.com)and thought it would be a good idea to share what's new and how to use the latest features.

Without further ado, let's jump into the changes, starting with the most significant ones.

## Proxy engine rewrite

The first and most significant change is the complete rewrite of the proxy engine. Back when I released [Evilginx 2.0](https://github.com/kgretzky/evilginx2), I had only just started learning programming in the Go language. The code quality I produced then was... mediocre at best 😅. The proxy code residing in `http_proxy.go` eventually took the form of spaghetti and quickly spiralled out of control. The code worked, but at times caused Evilginx to behave erratically.

The eight-year-old legacy code made it impossible to add any new features, because even the most minor additions risked causing the whole proxy logic to crumble like a Jenga tower. Since this part of the code became the core of Evilginx, I was pretty reluctant to touch it, in order not to break the tool's main functionality. With the release of **Evilginx Pro,** it became clear that the time had come for a complete rewrite.

The proxy engine rewrite was introduced with **Evilginx Pro** version [4.1](https://help.evilginx.com/pro/changelog#410-2025-04-30). All of the proxy components now work together much more reliably, and most importantly, the proxy code is now ready to give more power to the users who'd like to have complete control over the live modification of HTTP packets in transit. Full use of these changes will be made when **Phishlets 4.0** format is released in future updates.

**Phishlets 4.0** *(not yet available)* will allow you to:

* Capture data from the request & response HTTP headers.
* Capture data from the request & response HTTP content body.
* Inject custom headers into HTTP requests & responses.
* Modify the values of the request & response HTTP headers.
* Modify the content body in HTTP requests & responses.

Additionally, here are the most notable tweaks introduced with the proxy engine rewrite:

### Improved HTML injection

Evilginx, from the beginning, has utilised string pattern recognition to identify suitable locations for injecting its meta tags or JavaScript code blocks into proxied HTML content. This approach was very error-prone, as regular expressions would sometimes miss the pattern detection, resulting in crucial injections being omitted.

After the changes, Evilginx will now correctly parse the whole structure of the HTML document, looking for the specific object types. When performing the injection, rather than inserting a string into the HTML code, it will generate a new HTML object, which will later get properly formatted when the HTML content is rendered to a string.

This change now allows you to select the location where you'd like to inject your JavaScript `js_inject` injects.

```
js_inject:
  - trigger_domains: ["login.microsoftonline.com"]
    trigger_paths: [".*"]
    location: "<location_string>"
```

Where the `<location_string>` can be one of the following:

| Location | Description |
| --- | --- |
| `head` | Inject at the end of the `<head>` tag. |
| `body_top` | Inject at the beginning of the `<body>` tag. |
| `body_bottom` | Inject at the end of the `<body>` tag. |

### Phishlet collision fixes

One of the fixes, which needs mentioning, is the fix when handling multiple active phishlets which target the same destination hostnames.

Let's say you have two phishlets `phishlet1` and `phishlet2`. Both of them have the same hostname defined in `proxy_hosts`. Evilginx now allows you to enable both phishlets as it will now recognise the target hostname based on the defined phishlet's hostname, rather than the target hostname.

### Redirector fixes

If you had a redirector set up for your lure and you generated the lure URL with embedded custom parameters, Evilginx would lose the custom parameters and fail to forward them when the redirector redirected to the phishing page. The forwarding of custom parameters is now fixed, allowing you to use redirectors to their full potential.

## Anti-phishing evasion

One of the most prominent features, released in update [4.1](https://help.evilginx.com/pro/changelog#410-2025-04-30), was the option in phishlets to rewrite URL paths. Rewriting URL paths, while reverse proxying website content, allows you to protect your phishing pages from URL path pattern detection implemented by Google Chrome Safe Browsing protection.

Keep in mind that the following information is entirely speculative and the conclusion is based on my trial & error testing, rather than on reverse engineering the code of the detection engine.

If you reverse proxy the Google sign-in page and Safe Browsing kicks in, it will try to match the URL path and URL query to one of its known patterns. As an example, Safe Browsing will see the following phishing URL:

```
https://accounts.phishing.com/v3/signin/identifier?followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=ABCD01234&passive=0123456789&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=XYZXYZ1234
```

It will first detect the URL path, which it marks as the known URL path for the Google sign-in page: `/v3/signin/identifier`

Then it will try to match the keys and values of the URL query to look for known patterns. The keys it may match are as follows: `followup`, `ifkv`, `passive`, `flowName`, `flowEntry` or `dsh`.

Once it determines that the page, based on the URL path & query, must be the Google sign-in page, it will check the website's domain. That's when it will see `phishing.com`, instead of `google.com` and detection will be triggered.

![](https://breakdev.org/content/images/2025/07/chrome_warning.png)

Google Chrome Safe Browsing triggering the detection of the phishing page.

What I managed to figure out is that when the reverse proxy rewrites the URL path and modifies the URL query of the requests, Safe Browsing will have trouble detecting the phishing page, even with **Enhanced protection turned on** (it allegedly uses AI, so you know it must be good 😉...