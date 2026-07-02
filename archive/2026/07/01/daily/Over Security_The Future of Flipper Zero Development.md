---
title: The Future of Flipper Zero Development
url: https://blog.flipper.net/future-of-flipper-zero-development/
source: Over Security
date: 2026-07-01
fetch_date: 2026-07-02T05:58:02.464748
---

# The Future of Flipper Zero Development

[![Flipper Blog](https://blog.flipper.net/content/images/2022/07/orange_text_transpar-2.png)](https://blog.flipper.net)

* [Home](https://flipper.net/)
* [Products](https://flipper.net/collections)
* [Docs](https://docs.flipper.net/)
* [Downloads](https://flipper.net/pages/downloads)
* [Community](https://flipper.net/pages/community)

Subscribe to notifications of new posts:

You're subscribed

Oops! Please try again

Subscribe

[Flipper Zero](/tag/zero/)

# The Future of Flipper Zero Development

* [![Pavel Zhovner](/content/images/size/w100/2020/10/9a8180b4-80fa-4c50-9e83-bee59e3bc348-1.png)](/author/zhovner/)

#### [Pavel Zhovner](/author/zhovner/)

01 Jul 2026
• 6 min read

[Share](#/share)

![The Future of Flipper Zero Development](/content/images/size/w2000/2026/07/Flipper-Zero-Development-Main.png)

We've seen the strong reaction from the community over the idea that we've stopped developing the Flipper Zero firmware. We want to address this and let you know that we've heard all your feedback and have decided to rethink our approach to maintaining the project and engaging with the community.

**TL;DR: We've allocated resources to maintain Flipper Zero firmware and support community contributions.** From now on, community requests and contributions will be reviewed under new rules: voting for feature requests in GitHub Discussions, clearer pull request guidelines, and mandatory integration testing.

# How it all started — Kickstarter 2020

![](https://blog.flipper.net/content/images/2026/07/c295d2deb3030a06ecfc54a82d5e795e_original.webp)

When Flipper Zero launched on Kickstarter, we were overwhelmed by the community's support. That support came with a responsibility to deliver what we had promised. At the same time, we faced a wave of skepticism. We were called scammers and told the project would never ship.

A year and a half later, our entire team worked with the fear of letting our backers down and becoming another crowdfunding project remembered for taking $5 million and never delivering. We were hit by post-COVID component shortages, soaring supply chain costs, and political turmoil. On top of that, we were still dealing with thousands of accusations, insults, and threats.

We worked as hard as we could while trying to ignore the constant storm of criticism around us. But we have to admit that it was incredibly difficult. Today, we can look back and say that we made the right decisions: we planned our resources carefully, took risks, and worked really hard.

In the end, we made it through every challenge: from hardware and manufacturing to supply chains, logistics, firmware, and software development. We feel empathy for the teams behind crowdfunding projects that tried to copy Flipper Zero, but ended up shipping nothing. We could easily have been one of them, but today we can say with confidence:

* **We delivered on all Kickstarter promises** — every backer received the Flipper Zero they paid for, even if it took much longer than anyone had expected.
* **All features were implemented** — everything we stated in our Kickstarter campaign works as promised. This took us years of development.
* **We built a platform and infrastructure** — we're proud that Flipper Zero has become a hardware platform with software tools, APIs, and an SDK that developers genuinely enjoy using. That’s exactly why there are so many community-driven projects around Flipper Zero: alternative firmware, apps, and scripts.
* **Flipper Zero is available worldwide (almost)** — it may not be the most visible achievement, but we invested an enormous amount of effort into getting regulatory certifications, customs approvals, and all the paperwork required to officially import Flipper Zero into most countries. That's why there are now so many devices in people's hands.

## Thanks to everyone who supports us

![Flipper OS Icon](https://blog.flipper.net/content/images/2026/06/love--1--1.png)

We are deeply grateful to everyone who has supported us since the Kickstarter campaign and believed in our team. Without your support back in 2020, Flipper Zero would probably never have happened. Together with you, we built something far bigger than we ever imagined.

# Stable firmware 1.0

It’s important to understand that Flipper Zero has only 700 KB of flash memory available for firmware. And we ran into this limit very quickly, making it impossible to add new features. To work around it, we came up with dynamic apps loading from the microSD card — it allowed us to move device functions (including core features) outside the firmware into apps.

![](https://blog.flipper.net/content/images/2026/07/Flipper-Zero-dynamic-apps-loading--1-.png)

Firmware 1.0: a new approach to firmware architecture

This architecture became the foundation of the [stable firmware 1.0](https://blog.flipper.net/released-firmware-1/), which was released in 2024 following the [Apps Catalog](https://lab.flipper.net/apps) launch. We polished the user interface and [documentation](https://docs.flipper.net/zero). We also stabilized the firmware API and SDK for app developers, so they no longer had to rebuild their apps every month due to some API changes.

Since the firmware no longer required major changes, we decided to limit our work to maintaining the infrastructure and fixing critical bugs, while shifting our focus to building new devices (after all, we're called Flipper Devices).

By that point, an entire ecosystem of alternative firmware projects and communities had already existed, with people implementing every feature they could think of — even the weirdest ones. We consider our mission accomplished: we built an accessible development platform, and communities can now shape it into whatever they want.

# New approach to community contribution

We didn’t expect so many people to care so deeply about the development of the official Flipper Zero firmware. It's genuinely moving that this project and everything we’ve built together matters to you. That's why we’re ready to revisit some of our past decisions. We decided to allocate resources to continue supporting community contributions, but with a new approach.

What this means in practice:

* **Limited team resources** — our team is still small, and all our attention right now is on building new **DEVICES**. We can no longer hang out in chats, jump on calls, and talk in real time the way we used to. From the outside, it might look like we're ignoring the community, but in reality, it's just focused work.
* **Async communication only** — from now on, all communication with the development team will happen through requests in [GitHub Discussions](https://github.com/flipperdevices/flipperzero-firmware/discussions). You can vote on topics, and we commit to reviewing the requests that get the most votes. But these have to be concrete feature requests, formatted [according to the rules](https://github.com/flipperdevices/flipperzero-firmware/discussions/4395). Abstract questions, general discussion, and help requests stay on Discord, Reddit, and social media.
* **New contribution rules** — we'll now evaluate pull requests more strictly, as reflected in our [updated contribution guide](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/CONTRIBUTING.md). This applies especially to AI-generated code that touches low-level libraries that is hard to verify, as well as changes that affect the device's UI and require edits in the documentation.
* **Integration and regression testing** — it's important that code changes don't break existing features. That's why we're making public the [integration test cases](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/testing/integration_tests.md) that our QA team used to test the firmware. These tests will need to be run for every change to the firmware code, and we'll bring the community in to help with part of the regression testing.

# Feature requests now only via GitHub Discussions

On...