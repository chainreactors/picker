---
title: Critical Next.js ImageResponse Flaw Can Lead to Server Code Execution via Crafted SVG Input
url: https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html
source: The Hacker News
date: 2026-09-23
fetch_date: 2026-09-24T07:08:25.213866
---

# Critical Next.js ImageResponse Flaw Can Lead to Server Code Execution via Crafted SVG Input

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Critical Next.js ImageResponse Flaw Can Lead to Server Code Execution via Crafted SVG Input](https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html)

**Swati Khandelwal**Sep 23, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBxfEfPNHZcocTp156lW-VbOENuCxmLM_7xUUY5QWEppPDsL04KhbN7yaT52b_XTCXW6ensPqjF8QBXuQWUgna8jerFExtxAfkCd4NqOGcQwUn8088DU87PMD7cgYhQ-dY2_xFdwPyaKU-kD9HBx_YcjAzvzwEQzLoKUu1cRRpOT5A1luhBCE6e6ChORw/s1700-nu-rw-lo-l85-e365/next.jpg)

A new security vulnerability in Next.js could allow attackers to run code on a server via [ImageResponse](https://nextjs.org/docs/app/api-reference/functions/image-response), the feature that generates Open Graph and other social preview images, Vercel said.

The risk applies when an app puts values an attacker controls, such as text read from the request URL, into the image. Vercel, which develops Next.js, [fixed the flaw](https://nextjs.org/blog/nextjs-security-update-september-22-2026) on September 22 in version 16.3.6.

The flaw, tracked as **CVE-2026-94545**, affects Next.js 16.2.0 through 16.3.5 when ImageResponse runs on the Node.js runtime, which Next.js [uses by default](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config). Vercel's [advisory](https://github.com/vercel/next.js/security/advisories/GHSA-vcvr-r3jv-pc5j) rates it critical, with a CVSS score of 9.5. The Edge version of ImageResponse is not affected, and neither is Next.js 15.

ImageResponse uses [Satori](https://github.com/vercel/satori), a Vercel library, to convert the image layout into SVG code before the final PNG is generated. Affected apps are those that "pass attacker-controlled values into SVG content, attributes, or styles during image generation", according to the advisory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The advisory's example takes a value from the request URL and places it inside an SVG title element. It does not say whether text in ordinary elements, such as a heading inside a div, also counts.

To find where an app uses the feature, look for ImageResponse imported from next/og, for example in route handlers and in opengraph-image files. Route handlers make the image when a request arrives. An opengraph-image file can make it at build time or when a request arrives.

As of September 23, The Hacker News found no public reports of attacks using the flaw and no public exploit code.

The fix is Next.js 16.3.6, the only patched version, installed with npm install next@16.3.6. As of September 23, the npm registry listed no fixed release for the 16.2 line, so apps on 16.2 need to move to 16.3.6. Next.js 15.5.26 adds extra security hardening for next/og on the 15.5 line.

If upgrading has to wait, the advisory's workaround is to keep attacker-controlled values out of the SVG content, attributes, and styles that the Node.js ImageResponse renders. The advisory does not suggest switching to the unaffected Edge version, and the Next.js documentation marks the Edge runtime as deprecated.

In checks by The Hacker News on September 23, npm audit did not flag Next.js 16.3.5, an affected version. The advisory was also not yet listed in the GitHub Advisory Database, and no CVE record for CVE-2026-94545 had been published.

Check the Next.js version directly. Satori is bundled inside the Next.js package, so a lockfile does not list it as a dependency of Next.js.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

Vercel's advisory and announcement do not say whether apps hosted on Vercel are protected. For [two critical Next.js flaws fixed in August](https://thehackernews.com/2026/08/nextjs-patches-critical-avif-and.html), the company said hosted apps were protected and needed no upgrade.

Vercel's advisory and announcement also provide no way to check whether an affected route was abused before the patch. Affected versions have been available since [Next.js 16.2](https://nextjs.org/blog/next-16-2) was released on March 18.

The bug itself is in Satori. Satori's [own advisory](https://github.com/vercel/satori/security/advisories/GHSA-wx4j-mvgx-mqwp), published the same day, says certain values reached its SVG output without being properly escaped. A specially made value could then be read as SVG code instead of plain text.

In Next.js, such values could reach vulnerabilities in other libraries that Next.js depends on and lead to code execution, Vercel said. It has not named those libraries.

Satori's advisory rates the same CVE as moderate, with a score of 5.3, and says the impact depends on how the SVG output is used. Developers who use Satori directly should update it to version 0.33.5, which has the fix.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Open Source](https://thehackernews.com/search/label/Open%20Source), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Claude ...