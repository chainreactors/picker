---
title: PyPI now supports archiving projects
url: https://blog.trailofbits.com/2025/01/30/pypi-now-supports-archiving-projects/
source: Trail of Bits Blog
date: 2025-01-31
fetch_date: 2025-10-06T20:08:01.705157
---

# PyPI now supports archiving projects

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# PyPI now supports archiving projects

Facundo Tuesca

January 30, 2025

[engineering-practice](/categories/engineering-practice/), [open-source](/categories/open-source/), [supply-chain](/categories/supply-chain/)

PyPI now supports marking projects as archived. Project owners can now archive their project to let users know that the project is not expected to receive any more updates.

Project archival is a single piece in a larger supply-chain security puzzle: by exposing archival statuses, PyPI enables downstream consumers to make more informed decisions about which packages they depend on. In particular, an archived project is a **clear signal** that a project intends to make no future security fixes or perform ongoing maintenance.

Thanks to this signal, downstream consumers can make better-informed decisions about whether to limit or migrate away from their use of a particular package **without having to resort to heuristics** around project activity or maintenance status. This results in a **virtuous double-effect**: downstreams are better informed about the status of their supply chain, and upstreams should receive fewer distracting, superfluous requests for maintenance information from upstreams.

This work is a continuation of our ongoing efforts to bring supply-chain security improvements to [PyPI](https://pypi.org/), as well as Python packaging more generally. For more information about our previous efforts, check out some of our earlier writeups:

* November 2024: [Attestations: A new generation of signatures on PyPI](https://blog.trailofbits.com/2024/11/14/attestations-a-new-generation-of-signatures-on-pypi/)
* November 2023: [Our audit of PyPI](https://blog.trailofbits.com/2023/11/14/our-audit-of-pypi/)
* May 2023: [Trusted Publishing: a new benchmark for packaging security](https://blog.trailofbits.com/2023/05/23/trusted-publishing-a-new-benchmark-for-packaging-security/)
* November 2022: [ABI compatibility in Python: How hard could it be?](https://blog.trailofbits.com/2022/11/15/python-wheels-abi-abi3audit/)
* June 2019: [Getting 2FA Right in 2019](https://blog.trailofbits.com/2019/06/20/getting-2fa-right-in-2019/)

Finally, project archival is just the beginning: we’re also looking into additional maintainer-controlled project statuses, as well as additional PyPI features to improve both upstream and downstream experiences when handling project “lifecycles.” Stay tuned for additional progress on those fronts!

### Why statuses matter

The ability to mark the status of projects on PyPI has been a [long-standing](https://github.com/pypi/warehouse/issues/345) [feature](https://github.com/pypi/warehouse/issues/4021) [request](https://github.com/pypi/warehouse/issues/8659). This is for projects that are abandoned, unmaintained, feature-complete, deprecated, etc., where the maintainer wants to correctly set expectations for users of the package about expected future updates and even endorsement of use.

An interesting problem that comes up then is: which statuses should be supported, and what are their semantics? Ideally, a project should have a single “main” status, but some of these statuses overlap semantically (like “abandoned” and “unmaintained”), while others are not mutually exclusive (a project can be both feature-complete and unmaintained).

There is an [open discussion](https://github.com/pypi/warehouse/issues/16844) on PyPI’s issue tracker about what statuses should be added or not. As a first step, there was agreement that “archived” is useful and has clear enough semantics to be the first status added.

### Archiving a project

Owners of a project can archive it by navigating to the project’s settings page and scrolling down near the end to the following section:

![](/img/wpdump/ba1d075ad78938bce0e18cf364585228.png)

Figure 1: Archiving a project

This lets the owner know the semantics (no further updates expected), and recommends a way to give users more context via a final release.

After archiving the project, users will see the following notice in the project’s main PyPI page:

![](/img/wpdump/990e9a712f243c9a5086a39fc31f1fdd.png)

Figure 2: Project has been archived

Finally, the project owners can always unarchive a project if needed.

Importantly: project archival is not the same thing as [yanking](https://pypi.org/help/#yanked) or outright deletion. An archived project is never deleted and, unlike projects that are yanked, can still be resolved by default. PyPI will also never delete or prune projects based on their archival status: archiving is intended *solely* to empower project maintainers to communicate their project’s status to downstream consumers.

### Under the hood

[Behind the scenes](https://github.com/pypi/warehouse/pull/17005), maintainer-controlled project statuses are a specialization of a larger feature also recently added to PyPI: project quarantine. Thanks to the [LifecycleStatus model](https://github.com/pypi/warehouse/blob/5c8c415d056837a555ea0eda759d3a253c91d689/warehouse/packaging/models.py#L166-L169) and state machine developed for the quarantine feature, we were able to rapidly extend PyPI’s project statuses to include a new “archived” state. We expect future state additions to be similarly easy!

More information about project quarantine can be found [on the PyPI blog](https://blog.pypi.org/posts/2024-12-30-quarantine/).

### Where do we go from here?

Project archivals are currently recorded and presented on PyPI’s web interface. This is great for humans making decisions about whether to use (or discontinue use of) a package, but doesn’t immediately help *installers* (like `pip` and `uv`) alert developers when their dependencies become archived.

In other words: this feature will help users but it doesn’t yet help the machine-readable case. That’s something we’re working on!

The “archived” state is also not the end-all, be-all of packaging statuses: as mentioned above, there are numerous other states (“deprecated,” “feature-complete,” etc.) that project maintainers want to express in a consistent fashion. Now that we have a blueprint for doing that with the “archived” state, we’ll be looking into those as well.

### Acknowledgements

We would like to thank the PyPI administrators and maintainers for reviewing our work and offering us invaluable feedback throughout development. In particular, we thank [Mike Fiedler](https://github.com/miketheman) (as PyPI’s Safety and Security Engineer) and [Dustin Ingram](https://github.com/di) (as one of PyPI’s maintainer-administrators) for their time and consideration.

Our development on this feature is part of our ongoing work on PyPI and Python packaging, as funded by [Alpha-Omega](https://alpha-omega.dev/). Alpha-Omega’s mission is to protect society by catalyzing sustainable security improvements to the most critical open-source software projects and ecosystems.

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethi...