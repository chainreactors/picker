---
title: Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers
url: https://thehackernews.com/2026/07/bing-images-flaws-let-crafted-svgs-run.html
source: The Hacker News
date: 2026-07-24
fetch_date: 2026-07-25T05:00:48.850681
---

# Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers

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

# [Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers](https://thehackernews.com/2026/07/bing-images-flaws-let-crafted-svgs-run.html)

**Swati Khandelwal**Jul 24, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirbs2h3QyfDG1ChFBHv8CQNwf9JrDdDWLaZ0AZ2WTiJrsjmmeQUXSFc8FM4OvPgxDig-z2H1Di7OMqCC_0mHbicAvDw6TGF-1jWihJ458GYQBKznb3VOehlOPqWfALnkz8k3DBfehWG2z5nmpu77OgRxJ1iQxL7lsrd1IH3YR6ZHPpSUns-tdmDYScHck/s1700-e365/bing-image.jpg)

A crafted SVG submitted to Bing's image search ran commands as `NT AUTHORITY\SYSTEM` on Microsoft's production image-processing workers, and as root on the Linux machines in the same fleet.

XBOW's testing got the same result on workers across different hosts and network ranges, so the problem sat in Bing's image tier, not on one bad machine. Microsoft issued two critical CVEs, CVE-2026-32194 and CVE-2026-32191, and rated both 9.8 on the CVSS scale.

XBOW, the autonomous offensive security startup, found both and reported them privately. Bing users have no patch or mitigation to apply: Microsoft fixed both server-side before the advisories went out in March, and the records state there is "no customer action to resolve."

Neither advisory recorded exploitation or public disclosure when they went up on March 19. XBOW published the exploit mechanics on July 23, after holding them back at Microsoft's request until the remediation had landed.

What outlives the fix is the shape of the bug. The application believed it was handling an image; the helper underneath read part of that image as a command.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

If your own stack pipes uploads or server-fetched URLs through ImageMagick or anything ImageMagick-compatible, your exposure turns on whether attacker-controlled content can still reach a delegate-enabled path. Deny the delegates, cut the formats you accept, and keep the worker off the network, and the same SVG does nothing.

Bing's reverse image search fetches an image URL from the backend, because that is what the feature does. On its own, that is a blind SSRF: nothing comes back to the client. The tell was the error. Some workers returned a 500 to the browser and still fetched and parsed what they retrieved, which pointed at something downstream doing the parsing.

SVG answered that question. It is XML, not pixels: it can reference other images, and a renderer that follows those references goes and gets them. Underneath, conversion suites hand formats they do not process themselves to a delegate, an external program invoked through a shell.

On the path [XBOW reached](https://xbow.com/blog/bing-images-rce-vulnerabilities), that layer was still enabled, so an image reference beginning with a pipe character went to the shell rather than being read as a filename. The payload was a one-pixel SVG whose reference ran a command on the worker and curled the output back to a collector XBOW controlled.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwKclHOHAs710OQCt4hRM6khnaPyUdL9lZ8DVRhuKjrDb41lsLnzTjE5LtG4IbmHtVhx-uVqe2SOKV9BHErT6QKFmjnOrrfOcQocUf0hsnChv7xy1oo2sk4IhgigZtIGLk3GIycYgQEi8ANwHhX5wkTy_U5tf7FuqkUnQqpRe0yz7z2nlK1akqr8lMV7M/s1700-e365/bing.jpg)

That gave two routes into the same conversion tier and two CVEs.

* [CVE-2026-32194](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32194), filed as command injection under CWE-77, is the public "Search by Image" upload, with the SVG going in base64 as the `imageBin` field to `/images/kblob`.
* [CVE-2026-32191](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32191), filed as OS command injection under CWE-78, is the crawler route: host the SVG anywhere, hand its URL to the search through the `imgurl` parameter, and `bingbot/2.0` fetches it into the same pipeline. Neither needs authentication, cookies, session state or a click.

The Hacker News checked both CVE records on July 24. Both still carry Microsoft's March status of no public disclosure, which XBOW's writeup has overtaken, and Microsoft still lists them as not exploited.

The proof had to come out of band. The frontend could return an error while the worker executed anyway. Linux workers returned uid=0 and gid=0. On Windows, `systeminfo` named Windows Server 2022 Datacenter, `whoami /all` showed SeImpersonatePrivilege and SeDebugPrivilege enabled, and directory listings put execution inside Bing's multimedia image-processing components. The firm says it ran only benign read-only commands and touched no customer data.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnP2BIJTKZ31v-Y_pyvFqC1s6LD-Bo8UNy3UHgqojpVezgaGWw5-sPe5uRK0dfSm3gmDvoKCdHoJnGx1BiTP6Y0qit7D7TCZU_LckTDpdu9eeyuelmJKndEkOxZP6oNPwzguLBCTkAnNkIEvSYaWamKLqYLrJPjnea1V_lz7UcfQkavBo2g3OEGoLyz7mD/s728-e100/sygnia-d-4.png)](https://thn.news/sygnia-webinar)

Narrowing it to that path took dozens of probes. ImageMagick pseudo-protocols came back differently depending on the coder: `label:` rendered text and `xc:` produced a color image, while `text:`, `caption:` and direct file reads failed. Shell metacharacters inside `label:` rendered as text rather than executing, which ruled that coder out. The path that did reach a delegate was the image reference inside the SVG itself.

## Turn the delegates off

An image-processing worker handling untrusted files should not reach a shell, run as SYSTEM, or have a way out to the internet. Bing's pipeline did all three.

[ImageMagick's own guidance](https://imagemagick.org/security-policy/) is explicit that the default policy is open and meant for sandboxed or firewalled use, not a public website. For anything touching untrusted images, deny delegates outright in `policy.xml`:

`<policy domain="delegate" rights="none" pattern="*" />`

Then, in order of what buys you most:

1. Cut the formats...