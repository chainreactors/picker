---
title: Is that link phishing? Meet the StalkPhish URL scanner (closed beta)
url: https://stalkphish.com/2026/10/27/stalkphish-url-scanner-beta/
source: Over Security
date: 2026-10-27
fetch_date: 2026-10-28T07:49:13.501911
---

# Is that link phishing? Meet the StalkPhish URL scanner (closed beta)

[Skip to content](#main)

[![StalkPhish](/_astro/logo-black.CenBZhy0_18YWso.webp)](/)

[StalkPhish.io](/products/)

* [Platform overviewFeatures, use cases and integrations](/products/stalkphish-io/)
* [Web SearchFree lookup on stalkphish.io, no account](https://www.stalkphish.io)
* [PricingPlans and 7-day free trial, on stalkphish.io](https://www.stalkphish.io/pricing/)
* [API documentationREST API reference, on stalkphish.io](https://www.stalkphish.io/documentation/fullapi/)

[Open Source](/community/)

* [PhishingKit-Yara-RulesYARA rules to identify phishing kits](/products/phishingkit-yara-rules/)
* [StalkPhish-OSSThe phishing kits stalker](/products/stalkphish/)
* [PhishingKitHunterFind kits using your own website files](/products/phishingkithunter/)
* [Le Dico du ScamGlossary of francophone scammer slang](/products/dico-du-scam/)
* [All projects on GitHub](https://github.com/t4d)

[Blog](/blog/)

[Company](/about/)

* [About](/about/)
* [In the News](/press-media/)
* [Contact](/contact/)
* [Legal notice](/legal-notice/)

[fr](/2026/10/27/scanner-url-stalkphish-beta/?lang=fr "Version française")[Try StalkPhish.io](https://www.stalkphish.io)

[StalkPhish.io](/products/)[Platform overview](/products/stalkphish-io/)[Web Search ↗](https://www.stalkphish.io)[Pricing ↗](https://www.stalkphish.io/pricing/)[API documentation ↗](https://www.stalkphish.io/documentation/fullapi/)

[Open Source](/community/)[PhishingKit-Yara-Rules](/products/phishingkit-yara-rules/)[StalkPhish-OSS](/products/stalkphish/)[PhishingKitHunter](/products/phishingkithunter/)[Le Dico du Scam](/products/dico-du-scam/)[All projects on GitHub ↗](https://github.com/t4d)

[Blog](/blog/)

[Company](/about/)[About](/about/)[In the News](/press-media/)[Contact](/contact/)[Legal notice](/legal-notice/)

[Try StalkPhish.io ↗](https://www.stalkphish.io)

1. [StalkPhish](/)
2. /
3. [Blog](/blog/)
4. /
5. [phishing](/category/phishing/)

Thomas Damonneville·27 October 2026·6 min read

# Is that link phishing? Meet the StalkPhish URL scanner (closed beta)

[StalkPhish.io](/category/stalkphish-io/)[phishing](/category/phishing/)[tool](/category/tool/)[threat analysis](/category/threat-analysis/)[hunting](/category/hunting/)[soc](/category/soc/)[CERT](/category/cert/)[CSIRT](/category/csirt/)

![Scan result of the StalkPhish URL scanner: 93/100, CRITICAL](/_astro/scan-cover.B9D498uY_Z22JqCB.webp)

A link arrives by SMS, e-mail or chat, and someone has to decide quickly whether it is phishing. Opening it in a browser is risky and often useless: today’s phishing pages are protected by **traffic filters** that show the real page to the targeted victim and something harmless to everyone else, starting with security analysts and their tools.

That is the problem the **[StalkPhish URL scanner](https://scan.stalkphish.io/)** was built for. It is powered by the same detection engine as [StalkPhish.io](/products/stalkphish-io/), our phishing detection and investigation platform, and it has been open to a first group of testers since September. It is still in **closed beta**: if you want to try it, [ask us for an access code](/contact/).

**In short:**

* Paste a suspicious URL, even defanged, and get a **threat score from 0 to 100** and a verdict in seconds.
* The scanner **follows the whole redirect chain**, renders the page in a real browser and keeps a screenshot, from isolated infrastructure.
* It **detects cloaking**: when scammers hide their page from analysts, the hiding itself becomes evidence.
* Every score comes with **the signals that justify it** and the forensic data needed for a takedown.
* A **JSON API** lets SOC, CERT and anti-fraud teams plug it into their own tools.

To show what it does, here is a real result, section by section: a link that looks like nothing, and turns out to be a well-hidden phishing route.

## The verdict first: a score out of 100

![Score and verdict of the scan](/_astro/scan-score.DGWPTElb_aqd6x.webp)

Every scan ends with a **threat score from 0 to 100** and a verdict, from *VERY LOW* to *CRITICAL*. A higher score means more evidence of phishing, not more trust. This one scored **93/100, CRITICAL**, in less than ten seconds.

Just below, the scanner says plainly what it could and could not see. Here, after **10 hops**, the destination answered but served nothing: that is how a traffic filter turns away a visitor it does not want. A targeted victim would have been sent to the real page. The scanner does not pretend otherwise: its findings describe the route and its hosts, and it says so.

This honesty matters. A low score on a page that could not be reached means “nothing was examined”, not “nothing is wrong”, and the report makes the difference visible.

## What the browser saw

![Screenshot rendered by the scanner](/_astro/scan-screenshot.BAHGDkDH_Za41EP.webp)

The scanner renders each page in a real browser and keeps a **screenshot**, taken from isolated infrastructure: neither your browser nor your IP address ever touch the suspicious site. Here, the capture shows TikTok, which is exactly the point: this is where the scammers’ filter chose to send a visitor it had identified as an analyst.

## The decoy: anti-analysis cloaking

![Anti-analysis cloaking detected](/_astro/scan-cloaking.D2OE8rS9_1i9vKo.webp)

Instead of the phishing page, the chain ended on `tiktok.com/explore?id=youarecloaked`. The scammers did not even hide it: *you are cloaked*. This **decoy redirect** to an unrelated, perfectly legitimate site is a hallmark of anti-analysis cloaking, and the scanner treats it as what it is: **evidence**, not a dead end. A legitimate link has no reason to send automated visitors somewhere else.

## Following the whole route

![Hosts of the redirect chain](/_astro/scan-chain-hosts.CRAH6yvr_ejp70.webp)

The link started on a bucket hosted on **Google Cloud Storage**, a trusted platform that scammers like precisely because its reputation is excellent. From there, the visitor was passed from host to host:

* a free subdomain of a public domain service;
* a domain registered almost four years earlier, recycled as a relay;
* tracking domains with random word combinations on recent TLDs such as `.run` and `.autos`, typical of a **traffic distribution system** (TDS);
* and finally the decoy.

Each host is labelled: the entry point, known legitimate sites, and unknown hosts that have no reason to sit in the middle of a redirection.

![Full HTTP redirect chain](/_astro/scan-redirect-chain.DX-d9A7U_Z2w9EtW.webp)

The complete **HTTP redirect chain** is kept, hop by hop, with the status code of each answer. Every hostile URL is **defanged** (`hxxps://…[.]com`) so it cannot be clicked by accident when the report is shared in a ticket or a chat.

## Reading the scammers’ parameters

![Parameters decoded from the redirect chain](/_astro/scan-chain-params.By2IiwD8_Zj9pk8.webp)

Traffic distribution systems pass information from one hop to the next in their URLs, often encoded in base64. The scanner **decodes these parameters** for readability: other tracking domains of the same network, campaign identifiers, timestamps. These are valuable leads to find the rest of the infrastructure. When a parameter contains an e-mail address, it is masked: it is the address of the targeted victim.

## The detections, explained

![Signals detected and their score](/_astro/scan-detections.CRMxhAyr_1SYmt5.webp)

The score is not a black box: the report lists **the signals that fired**, each with its share of the score. In this case: the decoy redirect, a chain laundered through unknown hosts, a traffic filter that identified the visitor as an analyst, evasion patterns in the page, hosting on an abused platform, a TLS certificate anomaly…

Behind these labels is the engine of StalkPhish.io, the one that also identifies the [phishing kit family](/2024/10/10/stalkphish-io-phishing-kit-family-enrichment/) of each kit we collect. The labels are deliberately generic. We explain *what* was found, n...