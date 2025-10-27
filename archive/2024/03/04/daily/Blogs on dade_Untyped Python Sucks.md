---
title: Untyped Python Sucks
url: https://0xda.de/blog/2024/03/untyped-python-sucks/
source: Blogs on dade
date: 2024-03-04
fetch_date: 2025-10-04T12:08:47.064205
---

# Untyped Python Sucks

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/03/untyped-python-sucks/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

3 minutes

# [Untyped Python Sucks](https://0xda.de/blog/2024/03/untyped-python-sucks/)

Untyped Python sucks. I’ve been writing Python for something like 10 years now, and looking back I can’t believe how bad the developer experience was compared to how it can be with appropriate type hinting. I noticed this recently while trying to work on a slack bot using the Slack Bolt SDK, which uses a decorator syntax to wrap functions to handle events, but what each event passes to the wrapped function is… well, it lacks some definition in the documentation. I’ll probably write something else about type annotation patterns for Slack Bolt in the near future.

At work I have been a prolific contributor towards type checking our codebase, some couple hundred thousand lines. This may seem strange, since I am a security engineer whose charter is much more focused on application security, infrastructure security, product security features, etc. But before I was a security engineer, before I worked in security at all, I was a QA engineer. This combination of jobs has given me a holistic view towards the eradication of bugs.

![Security Bugs Venn Diagram](https://0xda.de/blog/2024/03/untyped-python-sucks/img/security-bugs-venn-diagram.67e472c2e18055aa3d8ef89a32c83228.png)

By reducing the volume of software bugs as a whole, it has a positive impact on reducing the number of security bugs. Now, not all security flaws are software bugs, so this isn’t going to eliminate all security problems. And [no matter what the Linux Foundation says](https://jericho.blog/2024/02/26/the-linux-cna-red-flags-since-2022/), not all bugs are security flaws. But if we can have a positive impact on bug reduction, it can pay dividends in reducing security flaws as well.

We moved our code base to an explicit [mypy](https://mypy-lang.org/) ignore pre-commit rule maybe 2 years ago now, so that every new line should be typed (or explicitly ignored in certain circumstances). This means that every typing problem in our code base can easily be identified. It is easy to search the whole code base, it is easy to count by ignore type to see what the most common problems are, and it is easy to see the problems when editing existing files so that we can try to fix it opportunistically.

This deployment pattern helped us to immediately stop the bleeding and start to turn things around, and we’ve tackled tens of thousands of type ignores in the time since enacting this enforcement. I would often find myself bored on a flight or something and just hunt down `no-untyped-def` ignores, which is the mypy ignore rule for [Untyped Function Definitions](https://mypy.readthedocs.io/en/stable/error_code_list2.html#check-that-every-function-has-an-annotation-no-untyped-def).

`no-untyped-def` is, in my opinion, the most important place to start with typing a large code base. It vastly improves developer experience and enables rapidly identifying typing bugs that were otherwise masked by the untyped definition. Even if you only type the definition and then add type ignores for every type problem in the body of the function, it still has a meaningful improvement on the code base.

One thing that I’ve noticed since getting aggressive about annotating our code base is that a considerably high proportion of our Sentry errors now tend to have a close alignment to some type ignore in a nearby line of code or in a nearby function. Type checking could have prevented hundreds, perhaps thousands of bugs from being introduced into the code base over the years, and it has certainly prevented hundreds or thousands of bugs from being introduced in the time since we started enforcing it.

I still love the flexibility of Python, and sometimes the type checking can be a bit annoying to deal with, especially when working with third party code or some particularly advanced dynamic programming patterns. But for the majority of cases, type annotations are easy to add and provide a significantly better developer experience, while simultaneously reducing the likelihood of bugs being introduced.

---

Share this page

`https://0xda.de/blog/2024/03/untyped-python-sucks/`

[python](https://0xda.de/tags/python)

614 Words

Date Published

2024-03-03 17:00 +0000

32fc96e @ 2024-03-17

---

[â
NixOS, ESXi, & Secure Boot](https://0xda.de/blog/2024/03/nixos-esxi-secure-boot/)

[I don't want to, but that's why I will
â](https://0xda.de/blog/2024/02/i-dont-want-to-but-thats-why-i-will/)

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

© 2025
[Privacy](https://0xda.de/privacy/)
[Colophon](https://0xda.de/colophon/)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/03/untyped-python-sucks/ "Tor")
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

[Rss](https://0xda.de/blog/index.xml "RSS")
[JSON Feed](https://0xda.de/blog/index.json "JSON Feed")