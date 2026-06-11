---
title: How has use of framing protection security headers changed in the past 3 years&#x3f;, (Wed, Jun 10th)
url: https://isc.sans.edu/diary/rss/33068
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-10
fetch_date: 2026-06-11T06:36:50.809458
---

# How has use of framing protection security headers changed in the past 3 years&#x3f;, (Wed, Jun 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/33064)

Click HERE to learn more about classes Jan is teaching for SANS

# [How has use of framing protection security headers changed in the past 3 years?](/forums/diary/How%2Bhas%2Buse%2Bof%2Bframing%2Bprotection%2Bsecurity%2Bheaders%2Bchanged%2Bin%2Bthe%2Bpast%2B3%2Byears/33068/)

**Published**: 2026-06-10. **Last Updated**: 2026-06-10 08:29:21 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/How%2Bhas%2Buse%2Bof%2Bframing%2Bprotection%2Bsecurity%2Bheaders%2Bchanged%2Bin%2Bthe%2Bpast%2B3%2Byears/33068/#comments)

Back in 2023, I wrote a diary[[1](https://isc.sans.edu/diary/29698)] discussing how commonly X-Frame-Options and CSP headers containing the frame-ancestors directive were used on 1 million most popular domains on the internet (based on the Tranco list[[2](https://tranco-list.eu/)]), and how they were set. Given that three years have passed since then, I thought it might be interesting to repeat the analysis and see what – if anything – has changed in the meantime.

Before we get to the data, however, let’s briefly recap what the headers in question do and why they are important.

Both headers basically serve the same fundamental purpose – they inform a browser whether the content of a given web page may be embedded in an iframe or similar object on another web page. Without either of these headers in place, any web page may freely load any other web page in an iframe, which can be quite beneficial in some instances, but also provides a functionality that is commonly abused by phishing actors[[3](https://isc.sans.edu/diary/29638)].

The most common abuse scenario is related to a generic framing attack, and leads to what is sometimes called an “overlay phishing”. It is based on an attacker creating a malicious page which loads a legitimate website (usually the official company website of the recipient of the phishing) in a full-screen iframe, then overlays a fake login prompt on top of it. The result is that the victim sees what may appear to be the real login page. Setting either X-Frame-Options or CSP with the frame-ancestors directive on the legitimate site effectively mitigates this approach, because the browser will refuse to load the page inside an iframe in the first place, and all that would be displayed would be a fake login form over a browser message informing the user that a page cannot be loaded (which should make the credential stealing form apper less than trustworthy to most people).

This is a good reason why these headers are worth implementing on any organization's web site, regardless of how prominent or otherwise “interesting” the organization might consider itself to be.

For completeness’ sake, it should be mentioned that although the two security headers serve a similar purpose, they are not exactly equal. The X-Frame-Options header is the older of the two mechanisms and, while functional, is relatively limited in what it can express. It supports three directives: DENY (the page may not be framed by anyone), SAMEORIGIN (the page may only be framed by pages on the same origin/domain), and ALLOW-FROM (the page may be framed by a specific origin/domain).

Although the header in general is still widely supported and does its job well, its ALLOW-FROM directive was never universally supported by all browsers and is now considered obsolete[[4](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options#allow-from_origin)]. More importantly, however, the X-Frame-Options header as a whole has been basically superseded by the Content Security Policy frame-ancestors directive.

The CSP frame-ancestors directive offers considerably more flexibility than X-Frame-Options. It supports the same basic use cases (frame-ancestors 'none' being equivalent to DENY, frame-ancestors 'self' being equivalent to SAMEORIGIN), but also enables some additional ones (such as  supporting wildcard matching for subdomains etc.). Modern browsers therefore generally treat frame-ancestors as the authoritative directive, ignoring X-Frame-Options entirely when both are present[[5](https://w3c.github.io/webappsec-csp/#frame-ancestors-and-frame-options)]. That said, X-Frame-Options remains relevant for legacy browser compatibility and – in practice – both headers can be sent simultaneously without any harm, which is what many HTTP servers actually do.

With this context in mind, let us look at how the use of these headers has evolved since 2023.

The data was gathered using the same approach that I used in 2023 – I used a simple Python script that went through the current Tranco list of the 1 million most popular domains and attempted to connect to each one over HTTPS, recording which security-related headers were present in the response. The script performed no retries on failure, and the following numbers are therefore not completely precise. Nevertheless, based on a few tests, I would estimate the error rate to be significantly less than 0.5%, which I consider sufficient for our purposes of seeing whether and how the use of both “framing protection” headers has changed over time.

And as you may see from the following charts, which include both the 2023 and 2026 data for comparison, the numbers have indeed moved in an interesting way over the past three years (and the direction of movement is not entirely consistent across different sample sizes).

[![](https://isc.sans.edu/diaryimages/images/26-06-10-x-frame-or-csp.png)](https://isc.sans.edu/diaryimages/images/26-06-10-x-frame-or-csp.png)

In the top 1 thousand most popular domains, the overall coverage by either X-Frame-Options or CSP frame-ancestors directive has actually decreased – from 27.1% in 2023 to 23.1% in 2026. On the other hand, in the top 100 thousand domains, the coverage has increased significantly – from 20.6% to 37.4% – and in the full top 1 million domains it has grown from 14.4% to 29.7%. The divergence between the top 1k and the larger samples is somewhat puzzling at first glance, though it likely reflects the fact that the composition of the top 1k list has changed quite a bit over three years, with domains of some security-conscious organizations dropping out of the top 1k and being replaced by domains that don't serve web content in the traditional sense (CDN endpoints, infrastructure domains, API backends, and so on) and therefore don't send security headers at all.

Looking at the breakdown of specific X-Frame-Options directives in use, SAMEORIGIN remains the most common choice across all sample sizes, which is not surprising, as it is generally the most practical option for most web applications.

[![](https://isc.sans.edu/diaryimages/images/26-06-10-x-frame.png)](https://isc.sans.edu/diaryimages/images/26-06-10-x-frame.png)

In the top 1 thousand domains, SAMEORIGIN has actually declined (from 19.4% to 15.3%), while in the top 100 thousand and top 1 million, it has increased notably – from 16.9% to 20.8% and from 12.4% to 19.4% respectively. The DENY directive has seen modest increases across all sample sizes, and the ALLOW-FROM directive remains at negligible levels in the larger samples and is completely absent from the 1k sample.

When it comes to CSP with the frame-ancestors directive, the numbers tell an encouraging story across all sample sizes. In the top 1k, usage has grown from 7.9% to 9.4%. In the top 100k, it has more than doubled – from 3.8% to 7.9%. And in the full 1 million sample, the increase is even more dramatic, from 1.9% to 7.1%.

[![](https://isc.sans.edu/diaryimages/images/26-06-10-csp.png)](https://isc.sans.edu/diaryimages/images/26-06-10-csp.png)

This, next to the aforementioned more than doubling of domains that use either CSP frame-ancestors or X-Frame-Options, is one o...