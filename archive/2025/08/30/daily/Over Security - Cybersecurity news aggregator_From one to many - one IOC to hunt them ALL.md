---
title: From one to many - one IOC to hunt them ALL
url: https://viuleeenz.github.io/posts/2025/08/from-one-to-many-one-ioc-to-hunt-them-all/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-30
fetch_date: 2025-10-07T00:49:34.619543
---

# From one to many - one IOC to hunt them ALL

[>
$ cd /home/Viuleeenz](../../../../)

* [About](../../../../about/)
* [Posts](../../../../posts/)
* [Whitepapers](../../../../whitepapers/)

14 minutes

# [From one to many - one IOC to hunt them ALL](https://Viuleeenz.github.io/posts/2025/08/from-one-to-many-one-ioc-to-hunt-them-all/)

*If you are a threat researcher reading a blog post about a novel threat that could potentially impact your organization, or if you need to investigate this threat to enrich your internal telemetry for better tracking and detection, how would you proceed?*

This was the question that come up in my mind, out of the blue, reading an article from Unit42 where they start to talk about a novel malware sold in the underground named [Gremlin stealer](https://unit42.paloaltonetworks.com/new-malware-gremlin-stealer-for-sale-on-telegram/). As always the article is very well detailed, carefully explaining the malware’s characteristics and objectives while also providing the SHA-256 hash of the analyzed sample.

Generally speaking, shared IOCs are invaluable resources for the security community, as detection capabilities often depend on the breadth of threat intelligence available in your platform. However, IOC collections can vary dramatically in quality and scope. Sometimes you’ll find comprehensive lists containing everything from phishing email hashes and malware stages to domains and JavaScript files. Other times, you’re left with minimal intelligence—perhaps just a single hash and a brief description—making threat hunting significantly more challenging.

> 💡*When you encounter a new threat and there aren’t many resources to rely on, you must leverage your own internal data to collect additional intelligence. This allows you to extract valuable IOCs, pivot across related malware infrastructures, and discover additional hidden samples.*

In this blog post, we’ll walk through a **threat-hunting methodology** using **Gremlin Stealer** as our primary case study. We’ll explore how to extract **meaningful intelligence** from a single malware sample — **without heavily relying on reversing activities** — and transform that knowledge into **actionable hunting strategies** capable of detecting broader threat actor operations.

## Understanding Sample Relationships

Effective threat hunting begins with understanding how malware samples relate to each other. **Static characteristics** form the foundation of this analysis. File hash relationships are particularly valuable—searching for samples with the same **imphash** (import hash) can reveal binaries that use similar API patterns, while **ssdeep** and other fuzzy hashing techniques help identify files with comparable byte-level structures, even when their exact hashes differ due to minor modifications or repacking.

In addition to hashes, **file metadata** can provide another valuable layer of similarity indicators, helping connect samples that may belong to the same malware family or campaign. However, similarity analysis shouldn’t stop at static attributes. From a **behavioral standpoint**, distinctive indicators often emerge, such as: **File creation paths, Command-line arguments, Registry modifications, Network communication patterns,** etc..

When multiple samples shows overlapping behavioral traits — for instance, reaching out to the same C2 infrastructure or using identical file paths — it becomes much easier to **cluster them under the same threat actor’s activity**. In fact, for hunting purposes, **behavioral indicators are often more reliable than static characteristics**, since they reflect what the malware **must** do to achieve its objectives.

> 💡 *Static characteristics are **easily modified** by threat actors, but behavioral requirements are **functionally constrained**. A threat actor can change how malware looks, but it’s much harder to change what it needs to do to succeed.*

### Static Indicators

When examining our Gremlin Stealer sample in VirusTotal, several metadata characteristics immediately caught the attention. Each of these anomalies not only serves as a detection opportunity but also provides clues about the malware author’s techniques and intentions:

* **Anomalous Timestamp**

  The file’s reported creation date — **2041-06-29 19:48:00 UTC** — is set in the future. This is a **common anti-analysis technique** used by malware authors to bypass certain detection mechanisms or confuse automated analysis pipelines.
* **Misleading Copyright Information**

  + “LLC ‘Windows’ & Copyright © 2024” ( Attempts to mimic legitimate Microsoft software )
* **.NET Assembly Metadata**

  Since **Gremlin Stealer** is a **.NET binary**, it exposes rich metadata that can be extremely useful for clustering related samples. Notably:

  + **Module Version ID (MVID):** `8f855bb2-4718-4fa4-be9c-87ed0b588b5c`
  + **TypeLib ID:** `7c11697d-caad-4bae-8b2a-0e331680a53b`

  These identifiers are **generated during compilation** and often remain **consistent across samples built from the same source code or development environment**. As such, they can be powerful static indicators for **connecting related binaries** within the same malware family

![Figure 1: Gremlin Stealer Information](../../../../img/threat_hunt/gremlin_info.png)

Figure 1: Gremlin Stealer Information

### Behavioral indicators

While static analysis provides valuable initial insights, behavioral analysis through sandbox execution reveals how the malware actually operates in a live environment. VirusTotal’s sandbox capabilities allow us to observe Gremlin Stealer’s runtime behavior, uncovering network communications, file system interactions, and process execution patterns that static analysis alone cannot reveal.

![Figure 2: Gremlin Stealer URLs](../../../../img/threat_hunt/gremlin_urls.png)

Figure 2: Gremlin Stealer URLs

Gremlin Stealer’s **behavior tab** reveals distinct networking fingerprints:

* **IP Discovery Services**: The malware reaches out to:

  + `api.ipify.org`
  + `ip-api.com`

  These requests are used to **determine the victim’s external IP address**, a common tactic among info-stealers for **geolocation** and **target profiling**.
* **Telegram API Endpoints**: Connections to `api.telegram.org/bot` could suggest that **Telegram is used for data exfiltration**.

  + It’s worth mentioning that this technique has become increasingly **popular among cybercriminals** due to **encryption**, **ease of automation**, and **resilience against takedowns**.
* **Hardcoded C2 Server**: `207.244.199[.]46` is embedded as a **command-and-control endpoint**.

  + This serves as both an **immediate IOC** and a **pivot point** for uncovering related infrastructure used by the same threat actor.

Moreover, digging deeper into the **behavior tab** reveals how Gremlin Stealer systematically **harvests sensitive data** from multiple browsers, including **Chrome**, **Brave**, **Edge**, and other Chromium-based derivatives. One particularly interesting technique involves launching browser instances with **remote debugging enabled.**

![Figure 3: VirusTotal behvaior tab for Gremlin Stealer sample](../../../../img/threat_hunt/behvaioral_info.png)

Figure 3: VirusTotal behvaior tab for Gremlin Stealer sample

> 💡 *There is **no single indicator** you can always rely on. Threat hunting success depends on **how much information you can extract** from a sample and how effectively you **correlate it with other intelligence**. This process requires **iterative analysis** and cannot be treated as a one-time or “spot” activity.*

### Exploring VT Queries to collect more samples

Crafting effective VirusTotal hunting queries is both an art and a science. The challenge lies in balancing precision with coverage—queries that are too narrow will miss related variants, while overly broad searches generate overwhelming false positives. The sweet spot lies in identifying characteristics that are:

* **Likely to remain consistent** across the threat actor’s campaigns
* **Unique enoug...