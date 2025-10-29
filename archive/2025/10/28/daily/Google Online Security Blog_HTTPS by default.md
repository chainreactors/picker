---
title: HTTPS by default
url: http://security.googleblog.com/2025/10/https-by-default.html
source: Google Online Security Blog
date: 2025-10-28
fetch_date: 2025-10-29T03:14:36.310369
---

# HTTPS by default

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [HTTPS by default](https://security.googleblog.com/2025/10/https-by-default.html "HTTPS by default")

October 28, 2025

One year from now, with the release of Chrome 154 in October 2026, we will change the default settings of Chrome to enable “Always Use Secure Connections”. This means Chrome will ask for the user's permission before the first access to any public site without HTTPS.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXrS0w0j-B4TjCUWdtAUto_P-3BYetTEfuqTGuGkVli-e7O92UPFEjrIQuoGKGCyDZLkkfmr9PU1MAKbU9rEp8ZPoTTuG1jkoPSzSXx2QDPxNKkXUesNJfmY9HpN1AV5bUtTd27RiSafiDEGybf0M7cDIpi4XtlhXwiZizipeR2T2t77_r34JX8y-_s2ji/s1600/Screenshot%202025-10-28%20at%2011.11.00%E2%80%AFAM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXrS0w0j-B4TjCUWdtAUto_P-3BYetTEfuqTGuGkVli-e7O92UPFEjrIQuoGKGCyDZLkkfmr9PU1MAKbU9rEp8ZPoTTuG1jkoPSzSXx2QDPxNKkXUesNJfmY9HpN1AV5bUtTd27RiSafiDEGybf0M7cDIpi4XtlhXwiZizipeR2T2t77_r34JX8y-_s2ji/s1600/Screenshot%202025-10-28%20at%2011.11.00%E2%80%AFAM.png)

The “Always Use Secure Connections” setting warns users before accessing a site without HTTPS

[Chrome Security's mission](https://chrome.security) is to make it safe to click on links. Part of being safe means ensuring that when a user types a URL or clicks on a link, the browser ends up where the user intended. When links don't use HTTPS, an attacker can hijack the navigation and force Chrome users to load arbitrary, attacker-controlled resources, and expose the user to malware, targeted exploitation, or social engineering attacks. Attacks like this are not hypothetical—software to hijack navigations is readily available and attackers have previously used insecure HTTP to [compromise user devices](https://blog.google/threat-analysis-group/0-days-exploited-by-commercial-surveillance-vendor-in-egypt/#:~:text=exploit%20delivery%20via%20man-in-the-middle%20(mitm)) in a targeted attack.

Since attackers only need a single insecure navigation, they don't need to worry that many sites have adopted HTTPS—any single HTTP navigation may offer a foothold. What's worse, many plaintext HTTP connections today are entirely invisible to users, as HTTP sites may immediately redirect to HTTPS sites. That gives users no opportunity to see Chrome's "Not Secure" URL bar warnings after the risk has occurred, and no opportunity to keep themselves safe in the first place.

To address this risk, we [launched the “Always Use Secure Connections” setting](https://blog.chromium.org/2021/07/increasing-https-adoption.html) in 2022 as an opt-in option. In this mode, Chrome attempts every connection over HTTPS, and shows a bypassable warning to the user if HTTPS is unavailable. We also previously discussed our intent to move [towards HTTPS by default](https://blog.chromium.org/2023/08/towards-https-by-default.html). We now think the time has come to enable “Always Use Secure Connections” for all users by default.

## Now is the time.

For more than a decade, Google has published the [HTTPS transparency report](https://transparencyreport.google.com/https/overview?hl=en), which tracks the percentage of navigations in Chrome that use HTTPS. For the first several years of the report, numbers saw an impressive climb, starting at around 30-45% in 2015, and ending up around the 95-99% range around 2020. Since then, progress has largely plateaued.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXSN7f2wT1P2RGgK3pEEPW0Gelsge0JJ66bujFzrteRxegGfckgBc9glnCOcY6Ex5w64CKkcdjD2T3W2pDxNxMuPqMLDcnLt3qTGonkucdHnQuN8-ifXnDcbuXI7RpcdvZGv3agBBF8YrtxGLUhIIFm1jXKQFc2eC9jQHbTgT4DSovx8DJAKMhgxdi8161/s1600/Screenshot%202025-10-28%20at%2011.12.15%E2%80%AFAM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXSN7f2wT1P2RGgK3pEEPW0Gelsge0JJ66bujFzrteRxegGfckgBc9glnCOcY6Ex5w64CKkcdjD2T3W2pDxNxMuPqMLDcnLt3qTGonkucdHnQuN8-ifXnDcbuXI7RpcdvZGv3agBBF8YrtxGLUhIIFm1jXKQFc2eC9jQHbTgT4DSovx8DJAKMhgxdi8161/s1600/Screenshot%202025-10-28%20at%2011.12.15%E2%80%AFAM.png)

HTTPS adoption expressed as a percentage of main frame page loads

This rise represents a tremendous improvement to the security of the web, and demonstrates that HTTPS is now mature and widespread. This level of adoption is what makes it possible to consider stronger mitigations against the remaining insecure HTTP.

## Balancing user safety with friction

While it may at first seem that 95% HTTPS means that the problem is mostly solved, the truth is that a few percentage points of HTTP navigations is still *a lot* of navigations. Since HTTP navigations remain a regular occurrence for most Chrome users, a naive approach to warning on all HTTP navigations would be quite disruptive. At the same time, as the plateau demonstrates, doing nothing would allow this risk to persist indefinitely. To balance these risks, we have taken steps to ensure that we can help the web move towards safer defaults, while limiting the potential annoyance warnings will cause to users.

One way we're balancing risks to users is by making sure Chrome does not warn about the same sites excessively. In all variants of the "Always Use Secure Connections" settings, so long as the user regularly visits an insecure site, Chrome will not warn the user about that site repeatedly. This means that rather than warn users about 1 out of 50 navigations, Chrome will only warn users when they visit a new (or not recently visited) site without using HTTPS.

To further address the issue, it's important to understand what sort of traffic is still using HTTP. The largest contributor to insecure HTTP by far, and the largest contributor to variation across platforms, is insecure navigations to *private* sites. The graph above includes both those to public sites, such as `example.com`, and navigations to private sites, such as local IP addresses like `192.168.0.1`, single-label hostnames, and shortlinks like `intranet/`. While it is free and easy to get an HTTPS certificate that is trusted by Chrome for a public site, acquiring an HTTPS certificate for a private site unfortunately remains complicated. This is because private names are "non-unique"—private names can refer to different hosts on different networks. There is no single owner of `192.168.0.1` for a certification authority to validate and issue a certificate to.

HTTP navigations to private sites can still be risky, but are typically less dangerous than their public site counterparts because there are fewer ways for an attacker to take advantage of these HTTP navigations. HTTP on private sites can only be abused by an attacker also on your local network, like on your home wifi or in a corporate network.

If you exclude navigations to private sites, then the distribution becomes much tighter across platforms. In particular, Linux jumps from 84% HTTPS to nearly 97% HTTPS when limiting the analysis to public sites only. Windows increases from 95% to 98% HTTPS, and both Android and Mac increase to over 99% HTTPS.

In recognition of the reduced risk HTTP to private sites represents, last year we introduced a variant of “Always Use Secure Connections” for *public sites only*. For users who frequently access private sites (such as those in enterprise settings, or web developers), excluding warnings on private sites significantly reduces the volume of warnings those users will see. Simultaneously, for users who do not access private sites frequently, this mode introduces only a small reduction in protection. This is the variant we intend to enable for all users next year.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjihQPKh0xhxDHIaAhXaqpXq0chmBB9F5pdNcdRxxOlRjwzcjwaS4gZr0N9jGqXRBg8WawbCr...