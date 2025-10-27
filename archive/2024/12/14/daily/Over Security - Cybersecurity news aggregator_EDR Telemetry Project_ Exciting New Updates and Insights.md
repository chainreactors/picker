---
title: EDR Telemetry Project: Exciting New Updates and Insights
url: https://kostas-ts.medium.com/edr-telemetry-project-exciting-new-updates-and-insights-2feb693bb4ba
source: Over Security - Cybersecurity news aggregator
date: 2024-12-14
fetch_date: 2025-10-06T19:41:57.330372
---

# EDR Telemetry Project: Exciting New Updates and Insights

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2feb693bb4ba&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fkostas-ts.medium.com%2Fedr-telemetry-project-exciting-new-updates-and-insights-2feb693bb4ba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fkostas-ts.medium.com%2Fedr-telemetry-project-exciting-new-updates-and-insights-2feb693bb4ba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# EDR Telemetry Project: Exciting New Updates and Insights

[![Kostas](https://miro.medium.com/v2/resize:fill:64:64/1*BtTfw89t0Sfap1SKrF3hvA.jpeg)](/?source=post_page---byline--2feb693bb4ba---------------------------------------)

[Kostas](/?source=post_page---byline--2feb693bb4ba---------------------------------------)

6 min read

·

Dec 13, 2024

--

1

Listen

Share

The **EDR Telemetry Project** is back with another round of updates! This project is all about helping security researchers, threat hunters, and organizations understand the strengths and gaps in Endpoint Detection and Response (EDR) solutions.

In our latest updates, we’ve added support for new platforms, refined our scoring, and improved the way telemetry data is categorized. What’s even more exciting is seeing EDR vendors actively engaging with the project and enhancing their products based on our findings.

Let’s break down the key changes, why they matter, and how you can get involved!

## What’s New in the EDR Telemetry Project?

### Elastic 8.16 Support

We’ve ensured that our telemetry now supports the latest version of Elastic Stack, **Elastic 8.16**. This means that if you’re using Elastic for security analytics, you’ll continue to get accurate telemetry data for your investigations.

🔗 **Pull Request:** [Update WMI for Elastic 8.16 (#87)](https://github.com/tsale/EDR-Telemetry/pull/87)

### FortiEDR Integration

We’re thrilled to add **FortiEDR** to the project! This addition helps broaden our visibility and understanding of how FortiEDR handles telemetry collection.

🔗 **Pull Request:** [EDR Addition — FortiEDR (#84)](https://github.com/tsale/EDR-Telemetry/pull/84)

### Uptycs EDR Integration

Another big win — **Uptycs EDR** is now part of the project. This addition offers fresh insights into Uptycs’ telemetry collection capabilities and helps expand our coverage.

🔗 **Pull Request:** [Addition of Uptycs EDR (#66)](https://github.com/tsale/EDR-Telemetry/pull/66)

### Trend Micro and Qualys Updates

We’ve refined telemetry descriptions and scoring for both **Trend Micro** and **Qualys**. These changes reflect the latest improvements made by these vendors, showing their commitment to enhancing their products based on our findings.

🔗 **Pull Requests:**

* [Trend Micro EDR Updates (#73)](https://github.com/tsale/EDR-Telemetry/pull/73)
* [Updated EDR Telemetry for Qualys (#71)](https://github.com/tsale/EDR-Telemetry/pull/71)

### Contributors Wall

We’re excited to announce the addition of the **Contributors Wall** to recognize those who have made significant contributions to the project. A special shoutout to

[SecurityAura](https://medium.com/u/8b1f55b0ed95?source=post_page---user_mention--2feb693bb4ba---------------------------------------)

, who made it into the Contributors Wall thanks to their amazing contributions and ongoing support! Their dedication has helped improve the project, and we are grateful for their involvement.

🔗 **Pull Request:** [Update Contributors Wall (#96)](https://github.com/tsale/EDR-Telemetry/pull/96)

Press enter or click to view image in full size

![]()

## Moving to a New Website and Building a Community

We’ve transitioned from displaying project results on a Google Spreadsheet to a dedicated [**website**](https://www.edr-telemetry.com/). This move makes the information easier to access, navigate, and future-proof for additional features and improvements. We’ve put significant effort into ensuring the website is **accessible and user-friendly**.

We’ve also launched a **Discord community** where members can discuss everything related to EDR telemetry, ask questions, and share insights. To maintain an active and high-quality community, participation is available to those who:

* [Contribute to the project](https://github.com/tsale/EDR-Telemetry/wiki#contribution-guidelines),
* [Provide a one-off donation](https://www.edr-telemetry.com/sponsorship.html#one-time) or
* Sponsor the project.

This approach helps ensure that the Discord server remains a space for **valuable discussions** and meaningful engagement.

![]()

The image is cropped for brevity. Full results [here](https://www.edr-telemetry.com/windows.html)

## Refining Telemetry Descriptions: What’s New?

In this round of updates, we’ve made important changes to how we categorize telemetry collection methods. These updates ensure clearer, more accurate descriptions of how EDRs capture telemetry. **The scoring for the “Via EventLogs”** has also been updated to reflect these refined definitions. This change improves clarity by ensuring more precise evaluations of each EDR solution’s capabilities, adjusting the score from **0.75 to 0.5** to better align with the updated categorization criteria.

### 🪵Via EventLogs

Telemetry, categorized as “Via EventLogs,” refers to data that is collected from Windows Event Logs — but only if event logging is enabled at the system level. The EDR itself does not independently collect this telemetry through **Event Tracing for Windows (ETW)**. This distinction helps clarify the reliance on system-level logging configurations.

### 🎚️ Via EnablingTelemetry

**“Via EnablingTelemetry”** describes telemetry that an EDR can collect, but only if an additional feature or setting is enabled. This capability is **not turned on by default** and often requires administrative action to activate. Understanding this helps users differentiate between out-of-the-box capabilities and those that need manual configuration.

🔗 **Scores:** <https://www.edr-telemetry.com/scores.html>

## Telemetry Events vs. Inferred Activity

We’ve also defined the difference between **Telemetry Events** and **Inferred Activity** in the project.

* **Telemetry Events** are direct, observable data points collected by the EDR.
* **Inferred Activity** refers to conclusions the EDR draws based on existing telemetry data rather than direct observation.

You can read more about this distinction in our [Telemetry Events vs. Inferred Activity](https://github.com/tsale/EDR-Telemetry/wiki/Telemetry-Events-vs.-Inferred-Activity) guide. A detailed blog post explaining this further will be coming soon!

## Telemetry Definition Clarification

For clarity, we’ve also updated how **telemetry** is defined in the context of this project. This updated definition reflects our commitment to providing precise and consistent terminology for telemetry collection. It helps ensure everyone understands what data is captured during installation processes and how it contributes to the overall EDR evaluation.

You can check out the detailed explanation in our [FAQ section](https://github.com/tsale/EDR-Telemetry/wiki...