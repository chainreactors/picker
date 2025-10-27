---
title: Ultralytics Supply-Chain Attack
url: https://www.schneier.com/blog/archives/2024/12/ultralytics-supply-chain-attack.html
source: Schneier on Security
date: 2024-12-14
fetch_date: 2025-10-06T19:43:25.080290
---

# Ultralytics Supply-Chain Attack

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Ultralytics Supply-Chain Attack

Last week, we saw a supply-chain attack against the Ultralytics AI library on GitHub. A [quick summary](https://www.reversinglabs.com/blog/compromised-ultralytics-pypi-package-delivers-crypto-coinminer):

> On December 4, a malicious version 8.3.41 of the popular AI library *ultralytics* ­—which has almost 60 million downloads—was published to the Python Package Index (PyPI) package repository. The package contained downloader code that was downloading the *XMRig* coinminer. The compromise of the project’s build environment was achieved by exploiting a known and previously reported GitHub Actions script injection.

Lots more details at that link. Also [here](https://blog.yossarian.net/2024/12/06/zizmor-ultralytics-injection).

Seth Michael Larson—the security developer in residence with the Python Software Foundation, responsible for, among other things, securing PyPi—has a good [summary](https://blog.pypi.org/posts/2024-12-11-ultralytics-attack-analysis/) of what should be done next:

> From this story, we can see a few places where PyPI can help developers towards a secure configuration without infringing on existing use-cases.
>
> * API tokens are allowed to go unused alongside Trusted Publishers. It’s valid for a project to use a mix of API tokens and Trusted Publishers because Trusted Publishers aren’t universally supported by all platforms. However, API tokens that are being unused over a period of time despite releases continuing to be published via Trusted Publishing is a strong indicator that the API token is no longer needed and can be revoked.* GitHub Environments are optional, but recommended, when using a GitHub Trusted Publisher. However, PyPI doesn’t fail or warn users that are using a GitHub Environment that the corresponding Trusted Publisher isn’t configured to require the GitHub Environment. This fact didn’t end up mattering for this specific attack, but during the investigation it was noticed as something easy for project maintainers to miss.

There’s also a more general “What can you do as a publisher to the Python Package Index” list at the end of the blog post.

Tags: [supply chain](https://www.schneier.com/tag/supply-chain/)

[Posted on December 13, 2024 at 11:33 AM](https://www.schneier.com/blog/archives/2024/12/ultralytics-supply-chain-attack.html) •
[2 Comments](https://www.schneier.com/blog/archives/2024/12/ultralytics-supply-chain-attack.html#comments)

### Comments

Clive Robinson •
[December 14, 2024 8:23 PM](https://www.schneier.com/blog/archives/2024/12/ultralytics-supply-chain-attack.html/#comment-442117)

@ Bruce, ALL,

If you think about it,

“If you make a wall of untested bricks from brickworks of unknown repute, do not be surprised if the edifice you build descends when least desired.”

Not being nasty to Open Source Development or nice to Closed Source development. At a basic level they are the same process and the outcome is dependent not on unfounded mantras but actual real tested and proven engineering. There is no place for artisanal craftsmanship using questionable “guild” patterns. I thought people had “seen the light” with regards to this as it is actually the reason “Software BOMs” are seen as a foundational activity.

On a more general note it is a well established engineering principle that the strength of a structure you build, rests in the mechanism by which load and stress is transmitted down through the structure and dissipated by being transmitted away.

This means that you really have to pay attention not just to the base foundations but what is both above and below them, they are integral to sound functioning. And like every link in a chain, it’s strength and weight within the whole is important if failure is to be avoided.

Those not just designing, but building systems, need to stop with the “Slap a bit of muck in” or “Just bolt/weld another bit on” almost “auto-reflex” behaviours.

Sure they can get things done quickly but by and large what they build up all to quickly is “Technical Debt”, “Complexity”, and really bad interfacing. Oh and a rather distinct lack of “Effective Error and Exception handling” and all the bad that results.

Just one bad of which is “Easy Supply Chain Vulnerabilities”, another is unwanted “Side Channels” hemorrhaging information that should not be disclosed. But “One that burns” is when “tools get abused” as all to often happens with tools these days.

Like much else that goes wrong in the Software Development Industry, all of these failings and most of what causes them are well known.

Thus you have to wonder why people are not questioning the processes that are quite obviously “Currently Failing Us?”…

Clive Robinson •
[January 4, 2025 2:39 PM](https://www.schneier.com/blog/archives/2024/12/ultralytics-supply-chain-attack.html/#comment-442377)

Originaly Sent Mon 30th Dec ~0755UTC

<https://www.schneier.com/blog/archives/2024/12/ultralytics-supply-chain-attack.html>

@ Bruce, ALL,

Taking the,

“If you make a wall of untested bricks from brickworks of unknown repute, do not be surprised if the edifice you build descends when least desired.”

A little further,

“Even if the bricks you use are tested and from a source of good repute you have to consider what they are laid upon.”

All structures are in effect built in layers thus you have rather more to think upon,

“Even a solid foundation layer will fail if the solum (ground) upon which it rests is not sound, with the solum resting in turn on the geological that too has to be sound.”

It’s why we have metaphors of “feet of clay” and “building on shifting sands”.

In essence all engineering and science is built in layers that form recognised “stacks” that are so implicit we oft forget about them and thus assume all is well.

But not if things are not sound?

In the past I’ve talked about “bubbling up attacks” in hardware and below CPU level DMA and MMU attacks are known almost since the techniques were invented and deployed back in the 1970’s. With more recently “RowHammer” and similar showing how very low level faults way down in the computing stack can be used by users “reaching around” all the security mechanisms.

Which brings us around to the lower layers of the stack.

In the past I’ve pointed out that the US NSA, UK GCHQ and other National SigInt Agencies attack “Implementation and algorithms” in various ways not least by aranging side channel attacks to appear in implementations but by critically effecting Standards, Protocols, and their underlying algorithms.

Non od these very low level attacks are unique to SigInt Agencies, many people design algorithms, and right them into standards. The example of the IEE, WiFi, and RC4 should be sufficient to demonstrate this. The IETF has likewise had it’s own issues, as have many others. It’s kind of a “Chicken and egg” problem, you have to have algorithms, to make protoco...