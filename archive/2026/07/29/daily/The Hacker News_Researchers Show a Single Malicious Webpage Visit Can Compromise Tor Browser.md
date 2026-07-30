---
title: Researchers Show a Single Malicious Webpage Visit Can Compromise Tor Browser
url: https://thehackernews.com/2026/07/researchers-show-single-malicious.html
source: The Hacker News
date: 2026-07-29
fetch_date: 2026-07-30T04:52:44.364499
---

# Researchers Show a Single Malicious Webpage Visit Can Compromise Tor Browser

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Researchers Show a Single Malicious Webpage Visit Can Compromise Tor Browser](https://thehackernews.com/2026/07/researchers-show-single-malicious.html)

**Swati Khandelwal**Jul 29, 2026Vulnerability / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOwFIxqT8kRBNj9LdZBZhO1g2RPJwUttxQosrS_mPoNXkIR-JB-yM87HPzuPZ1tazourGhRg9Sco6YQEGZkC77DSqXBYjp0DkNDAUHOaAOnIisRYNPAQfNWwqnmoILXOgR0wwyGVNlU3kSVRU6TcfyAx5ztaAWZfbKnCDJYgUeIVsM7n7O2zq7fGc-xnI/s1700-e365/tor-exploit.gif)

Nebula Security says a patched Firefox JIT flaw could be triggered by simply visiting a malicious webpage and was also used to compromise Tor Browser.

Tracked as **CVE-2026-10702**, the bug provides arbitrary code execution inside the browser's renderer process. Mozilla rated it High and fixed it in the [Firefox 151.0.3 update](https://www.mozilla.org/en-US/security/advisories/mfsa2026-54/).

"No settings or additional user interaction are required," Eten Zou, CEO of Nebula Security, told The Hacker News. "Visiting a malicious webpage is enough to trigger it," Zou said every Tor Browser release that incorporated a vulnerable Firefox version was affected, though researchers have not identified the exact Tor releases.

On its own, the bug runs code only inside Firefox's sandboxed content process. Nebula [released public exploit material](https://github.com/NebuSec/CyberMeowfia/commits/main/IonStack/CVE-2026-10702) and used the flaw as the first stage of IonStack, a browser-to-kernel chain built for an ARM64 device running Android 17. The released end-to-end code targets one supported Google build, although Zou said the browser flaw itself is not ARM-specific.

The public code contains Firefox 151.0 offsets for the supported ARM64 Android 17 build. Zou said each exploitation step is architecture-independent and described the x86 path as more stable, although Nebula has not completed the full chain for that architecture.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Firefox users should update to the latest release. The Hacker News traced the faulty alias declaration through Mozilla's source history to [Bug 1995077](https://bugzilla.mozilla.org/show_bug.cgi?id=1995077), which landed for Firefox 147. The override is present in [Firefox 151.0.2](https://raw.githubusercontent.com/mozilla-firefox/firefox/FIREFOX_151_0_2_RELEASE/js/src/jit/MIR.h) and absent from [Firefox 151.0.3](https://raw.githubusercontent.com/mozilla-firefox/firefox/FIREFOX_151_0_3_RELEASE/js/src/jit/MIR.h). That places the affected stable-release range at Firefox 147 through 151.0.2.

Mozilla's advisory does not list Firefox ESR, and the faulty override is absent from [Firefox ESR 140.12](https://raw.githubusercontent.com/mozilla-firefox/firefox/FIREFOX_140_12_0esr_RELEASE/js/src/jit/MIR.h). As of July 28, 2026, the available primary-source record does not establish exploitation against users in the wild.

In its [technical analysis](https://nebusec.ai/research/ionstack-part-1-cve-2026-10702/), Nebula traces the issue to MObjectToIterator when it runs with skipRegistration set to true. Firefox's just-in-time (JIT) compiler turns frequently run JavaScript into native machine code, and to do that safely it has to track which operations can touch memory.

Firefox treated the operation as a read even though resolving a lazy property can allocate a replacement dynamic-slots buffer and free the old one.

Global value numbering then treated a later slots-buffer load as redundant and reused the earlier pointer after it had become stale. Nebula's [released exploit](https://github.com/NebuSec/CyberMeowfia/blob/main/IonStack/CVE-2026-10702/exploit.html) reclaims the freed allocation, leaks a hidden-class pointer, builds a fake object, and corrupts a Uint8Array to gain arbitrary memory read and write. The Android code then changes memory protections and redirects a WebAssembly function entry point to ARM64 shellcode.

The failure turns on a narrow compiler contract: an operation capable of replacing the object's dynamic-slots buffer was labelled as a read. That incorrect contract let otherwise valid optimisation logic preserve a pointer the runtime had already invalidated.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnP2BIJTKZ31v-Y_pyvFqC1s6LD-Bo8UNy3UHgqojpVezgaGWw5-sPe5uRK0dfSm3gmDvoKCdHoJnGx1BiTP6Y0qit7D7TCZU_LckTDpdu9eeyuelmJKndEkOxZP6oNPwzguLBCTkAnNkIEvSYaWamKLqYLrJPjnea1V_lz7UcfQkavBo2g3OEGoLyz7mD/s728-e100/sygnia-d-4.png)](https://thn.news/sygnia-webinar)

Mozilla's [source-level fix](https://github.com/mozilla-firefox/firefox/commit/e43e678) removes the custom read-only alias handling from ObjectToIterator and adjusts the related iterator operation. That prevents the optimiser from treating a mutation-capable step as a harmless load and retaining the stale pointer.

IonStack's second stage is CVE-2026-43499, a separate Linux kernel futex flaw that Nebula calls [GhostLock](https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html). CVE-2026-10702 provides the remote browser foothold; CVE-2026-43499 carries it to root on the supported Android build.

Zou said GhostLock is invoked directly from Firefox. He added that Android's weaker sandbox makes exploitation easier, but Nebula does not believe a stronger desktop sandbox would prevent the attack.

Updating Firefox blocks the documented browser entry point, but it does not patch GhostLock itself.

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
[**S...