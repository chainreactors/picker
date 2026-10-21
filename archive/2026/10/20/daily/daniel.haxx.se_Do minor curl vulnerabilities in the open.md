---
title: Do minor curl vulnerabilities in the open
url: https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/
source: daniel.haxx.se
date: 2026-10-20
fetch_date: 2026-10-21T06:49:26.433420
---

# Do minor curl vulnerabilities in the open

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2020/02/http3-for-everyone-audience.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Security](https://daniel.haxx.se/blog/category/tech/security/)

# Do minor curl vulnerabilities in the open

[October 20, 2026](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/#respond)

The curl project has decided to alter its vulnerability disclosure program procedure and starting ***October 26 2026***, we insist that all vulnerability reports submitted to us that are deemed to be severity LOW or MEDIUM should instead be submitted as issues in [our GitHub repository](https://github.com/curl/curl).

Only vulnerabilities deemed to be HIGH or CRITICAL will be kept private in [the HackerOne tracker](https://hackerone.com/curl).

Security researchers in doubt can still submit the issue on HackerOne and we can tell them what severity we deem it to be. Over the last few years, over 90% of all submissions could quickly be assessed to be less than HIGH.

Issues submitted to HackerOne we deem are LOW or MEDIUM will be requested to be resubmitted on GitHub and will be closed as informative on HackerOne (and publicly disclosed).

## Avalanche survival tricks

This policy change is entirely triggered by the current avalanche of vulnerability reports that keep pouring in. We see no end to them and we do not anticipate this flood to decrease within the next several months.

We are struggling as a project as all key maintainers feel strained, overloaded and brought to the brink of what we can muster. We *must* act to survive. This is our next step in a survival strategy. It might not be our last. We aim to not drown.

## Public vs private

By opening up the process we allow the whole world to participate. Both in the assessment and understanding of the report and claimed vulnerability, but also in the creating and writing the advisory and figuring out details of when the issues was introduced etc.

Ideally we get better help to make sure the fix is the correct one, that it fixes the problem, and any other related problem that is similar and that it does not miss a related problem sitting next to this.

An obvious recent trend is that the moment we announce a new set of CVEs and their associated fixes, there is an army of AI-using researchers who throw all those at their models and harnesses to find similar mistakes or omissions in the fixes. By taking this process to the public all the way, ideally we get more help to do that scrutiny better *before* we ship releases.

We recognize that the amount of work needed per received vulnerability report does not shrink by doing them in public, but we think that we might share the burden among more people easier, and we hope that lessons and documentation brought up in these discussions will be easier to spot and learn from.

The open process can also allow distros and other users of curl to keep up with security fixes earlier and better.

## The risks

Several people have suggested there is a risk that researchers mistakenly submit severity HIGH issues on GitHub thinking they are LOW or MEDIUM. It is basically unheard of that a researcher would have *understated* a reported problem so I consider that a low risk scenario. Also: there was already before this a risk that someone would submit a vulnerability report in the public, it is not a new risk.

Handling some vulnerabilities in the public of course makes the immediately available for both good and bad people. This policy will give bad people a slightly longer window of opportunity to exploit weaknesses at the expense of existing curl users. That is unfortunate but we see no way of avoiding this. We limit this practice to less than HIGH for this reason: at least these problems are not terrible.

## Severity LOW

We have discussed simply dismissing all severity LOW issues, but within the CVE program there is an appeals process and if we don’t hand out a CVE to an actual vulnerability, then someone else will do it. We thus cannot ignore true vulnerabilities, or they will come back to bite us nonetheless.

We *can* however resist and refuse silliness and I personally aim to deny and decline more vulnerabilities harder on the basis that they do not actually hurt any users or existing applications.

## Crazy combos

A clear trend these days is that many newly reported vulnerabilities are figured out by AI models that create crazy sequences or option combinations that do something unexpected, but the sequence is something that aren’t likely to ever be used in the real world, or the unexpected that happens is something that occurs *every time* so applications doing this would spot the problem immediately. I.e problems that have almost no risk to actually trigger in the real world. We save no users by insisting on doing the CVE dance for those issues. We only get work for ourselves and a whole world that has to act on them.

## Flow control it

There is an almost infinite number of combinations you can use libcurl’s many options, protocol mixes and flexible API to do things that might not be clearly documented and the AIs will continue to try them all and together with the humans driving these checks they are super eager to treat every minor discrepancy as a vulnerability. We can’t continue down this spiraling path with our sanity intact.

We don’t have the bandwidth, manpower or even will to handle a never-ending vulnerability reporting stream at this pace. I believe few software projects can stand this kind of prolonged high volume deluge for extended periods. Something needs to give way.

## How to assign severity

We only use these for levels in the curl project: LOW, MEDIUM, HIGH and CRITICAL. Often we refer back to recently managed vulnerabilities to see how we judged them, but we also provide a [set of basic guidelines](https://curl.se/dev/vuln-disclosure.html#severity-levels). I’m sure we can also make them better and clearer.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[hackerone](https://daniel.haxx.se/blog/tag/hackerone/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous PostOSI approved the curl license](https://daniel.haxx.se/blog/2026/10/15/osi-approved-the-curl-license/)

### Leave a Reply [Cancel reply](/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
1seventwothree9

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [Do minor curl vulnerabilities in the open](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/)
  October 20, 2026
* [OSI approved the curl license](https://daniel.haxx.se/blog/2026/10/15/osi-approved-the-curl-license/)
  October 15, 2026
* [A curl audit by Aisle](https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/)
  October 14, 2026
* [A UAF turned RCE](https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/)
  October 14, 2026
* [curl 8.23.0](https://daniel.haxx.se/blog/2026/10/14/curl-8-23-0/)
  October 14, 2026
* [A slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/)
  October 13, 2026

# Recent Comme...