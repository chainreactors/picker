---
title: Next.js Ships Out-of-Band Patch for Two Critical RCE Flaws in Caching and SVG Processing
url: https://thehackernews.com/2026/10/nextjs-ships-out-of-band-patch-for-two.html
source: The Hacker News
date: 2026-10-15
fetch_date: 2026-10-16T06:37:55.132819
---

# Next.js Ships Out-of-Band Patch for Two Critical RCE Flaws in Caching and SVG Processing

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Next.js Ships Out-of-Band Patch for Two Critical RCE Flaws in Caching and SVG Processing](https://thehackernews.com/2026/10/nextjs-ships-out-of-band-patch-for-two.html)

**Swati Khandelwal**Oct 15, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9mXutJ2QPpC1NUCUZWdHjUDUGPSD3DaDY4b-T1EXbg07sNWADsV43EvUacKzn4Ohp2bRbD93t8kXBpv513XdMZEnMh8eNkY1bBaSuGICWbituq_jgWNCjQa_Cq6Ur0jInsfEwsHfdInKq4Tcp2kmfuYoCIMrgWcWwtzFlRPePDpW9gwemIkQpJXEVaHU/s1700-nu-rw-lo-l85-e365/nextjs-rce.jpg)

Next.js released an [out-of-band security update](https://nextjs.org/blog/nextjs-security-update-october-14-2026) on October 14 that fixes two critical flaws allowing unauthenticated remote code execution, along with a high-severity denial-of-service flaw.

One code-execution flaw is in React Server Components, and the other in librsvg, the open-source library Next.js uses through the sharp package to handle SVG images.

The fixes are in Next.js 16.4.1 and 15.5.28, the current Active and Maintenance long-term support (LTS) releases.

### What Was Fixed

The update covers three separate issues. Vercel, which develops Next.js, rated both code-execution flaws critical, each with a CVSS score of 9.5. The table lists the versions each issue affects and the version that fixes it.

| Issue | Affected versions | Fixed in | Who is exposed |
| --- | --- | --- | --- |
| Code execution through `use cache` ( [GHSA-673q-mjm6-r5xr](https://github.com/vercel/next.js/security/advisories/GHSA-673q-mjm6-r5xr) ) | 16.0.0 through 16.4.0 | 16.4.1 | App Router apps with Cache Components enabled, where a `use cache` function returns more than one typed array |
| Code execution through SVG images (CVE-2026-96889, [GHSA-2464-fhr4-w9xw](https://github.com/vercel/next.js/security/advisories/GHSA-2464-fhr4-w9xw) ) | 10.0.0 through 15.5.27, and 16.0.0 through 16.4.0 | 16.4.1, or 15.5.28 with `sharp` 0.35.5 or later | Apps that pass attacker-supplied SVG files to `sharp` on glibc-based Linux |
| Denial of service through Server Actions ( [GHSA-p3m5-59mp-jv5r](https://github.com/vercel/next.js/security/advisories/GHSA-p3m5-59mp-jv5r) ) | 13.0.0 through 15.5.27, and 16.0.0 through 16.4.0 | 15.5.28, 16.4.1 | App Router apps with at least one Server Action |

### Who Is Affected

The first code-execution flaw is in React Server Components, the React feature that runs user-interface components on the server. [React's advisory](https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3) covers three packages, react-server-dom-webpack, react-server-dom-parcel, and react-server-dom-turbopack, in versions 19.0.0 through 19.3.0. It describes the flaw as affecting "extremely rare cases where responses transport multiple typed arrays and an attacker-controlled value."

In a Next.js app, the trigger is a `use cache` function that returns more than one typed array, so only version 16 apps that enable Cache Components, the feature behind `use cache`, are exposed. Vercel says to upgrade even if your app has no such function.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The second flaw is a memory bug in librsvg, the library that renders SVG images, which Next.js reaches through the bundled `sharp` package. Code execution is possible when Next.js runs on glibc-based Linux, according to the advisory.

By default, Next.js does not optimize SVG files. Serving them through the image optimizer requires turning on a setting called [`dangerouslyAllowSVG`](https://nextjs.org/docs/app/api-reference/components/image). The same library also renders images for `next/og`, the feature that builds social-preview images, when that feature runs on the Node.js runtime.

The third flaw is a denial-of-service issue. In App Router apps that define at least one Server Action, crafted requests can push one server process to full CPU use and stop it from handling other requests. Apps on the Pages Router, or with no Server Actions, are not affected.

Exposure can differ by host. Netlify [said](https://www.netlify.com/changelog/2026-10-14-nextjs-react-security-vulnerabilities/) its platform does not run the image-optimizer code path and that the flaws have limited impact on its setup, while still recommending the upgrade.

### What to Do

Upgrade to Next.js 16.4.1 if you run version 16, or 15.5.28 if you run version 15, then rebuild and redeploy.

Vercel's advisory says upgrading Next.js makes package managers supply the fixed `sharp` automatically. On version 16 that holds, because 16.4.1 requires `sharp` 0.35.5.

On version 15 it may not. 15.5.28 still accepts the older, affected `sharp` 0.34.x, and upgrading over an existing install can leave that version in place. Check with `npm ls sharp` and update `sharp` to 0.35.5 or later if it is older.

If you cannot upgrade Next.js right away, the image flaw has an interim option: make sure `sharp` is 0.35.5 or later, or block SVG rendering in `sharp` with `sharp.block({ operation: ["VipsForeignLoadSvg"] })`, as the [sharp advisory](https://github.com/advisories/GHSA-wq5f-xc86-pv6w) describes. The `use cache` and Server Actions flaws have no workaround, and only the upgrade closes them.

As of October 15, the `use cache` and Server Actions advisories had no CVE and did not appear in the npm advisory feed that `npm audit` uses, so dependency scanners may not warn you about them. The image flaw does surface, through `sharp`'s own advisory.

### Why the Image Flaw Keeps Returning

This is the third time since August that image processing in Next.js has produced a code-execution flaw. In August, a bug in libheif, reached through `sharp`, allowed code execution when the optimizer handled a crafted [AVIF image](https://thehackernews.com/2026/08/nextjs-patches-critical-avif-and.html). In September, a flaw in [`next/og`](https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-ca...