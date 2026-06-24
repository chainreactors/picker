---
title: Ghost Stories: investigating an undocumented ClickFix C2 in Ghost CMS
url: https://blog.sicuranext.com/ghost-stories-investigating-an-undocumented-clickfix-c2-in-ghost-cms/
source: Over Security
date: 2026-06-23
fetch_date: 2026-06-24T06:06:00.775555
---

# Ghost Stories: investigating an undocumented ClickFix C2 in Ghost CMS

[![Sicuranext Blog](https://blog.sicuranext.com/content/images/2026/03/sicuranext_h-accent-2.png)](https://blog.sicuranext.com)

* [Home](https://blog.sicuranext.com/)
* [WAAP](https://blog.sicuranext.com/tag/waap/)
* [SOC](https://blog.sicuranext.com/tag/soc/)
* [PWNPress](https://blog.sicuranext.com/tag/pwnpress/)
* [AI](https://blog.sicuranext.com/tag/ai/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

# Ghost Stories: investigating an undocumented ClickFix C2 in Ghost CMS

#### [claudio bono](/author/claudio/)

23 Jun 2026
• 17 min read

[Share](#/share)

![Ghost Stories: investigating an undocumented ClickFix C2 in Ghost CMS](/content/images/size/w2000/2026/06/ghost-clickfix-cover.png)

*Read-only research into an active campaign that exploits CVE-2026-26980 in Ghost CMS. Every result below comes from public GET requests. We did not exploit the flaw, did not authenticate, and did not write anything. The main scan ran on 2026-06-11.*

## Key findings

* An active campaign is exploiting **CVE-2026-26980**, a SQL injection in the public Content API of Ghost CMS (versions 3.24.0 to 6.19.0, fixed in 6.19.1, released February 2026). The attackers use it to plant a JavaScript loader that sends visitors into a *ClickFix/FakeCAPTCHA* social-engineering chain.
* Using only **read-only GET requests**, with no exploitation and no login attempts, we scanned **3,153 Ghost hostnames** indexed by Shodan. **287 results (251 unique domains)** contained the injection, and **281 were confirmed again** in a second, independent pass (97.9%).
* **284 of the 287** point to a single command-and-control (C2) domain, `restrictes[.]com`. At the time of our scan (2026-06-11) it did not appear in the public indicator sources we consulted. We found it by decoding base64 strings in the page content, not by matching a list of known C2 domains. See the dated note under *A C2 surfaced from the data* for its status at publication.
* **17 of the compromised sites had already updated Ghost to a fixed version.** Updating does not remove an injection that is already stored in the site content. Fixing a site means patching, cleaning the content, and rotating the Admin API key.
* The victims have no narrow profile. Most are outdated Ghost **5.x** blogs, spread across about 25 country-code TLDs. Hosting is more concentrated: about **42% sit on DigitalOcean**. The injection is always in **post content, never on the homepage**.
* The activity splits into **two toolchain clusters**, one of them clearly dominant. We group them by tooling and shared infrastructure, and we do not name a threat group.
* We also found **887 sites that run a vulnerable Ghost version but show no sign of compromise yet**. Preventive action can still help these.

## Background

Ghost is a widely used CMS for blogs and newsletters. CVE-2026-26980 is a SQL injection in its public Content API. That endpoint is meant to be queried without authentication, so the flaw can be exploited without credentials. Ghost fixed it in version 6.19.1 in February 2026. The affected versions are 3.24.0 to 6.19.0.

The mechanics matter, because they explain why the compromise is so persistent. The injection itself only reads. The Content API stays read-only. But what it reads is the site's **Admin API key**, which is stored in the database. With that key, the operator logs in to Ghost's separate Admin API, which can write, and edits stored posts in bulk to insert the loader into their bodies. So the chain has two stages: read the key through the Content API, then write through the Admin API. That is why the loader lives in the post records and survives a Ghost upgrade. We come back to this below.

The flaw is used in a financially motivated campaign called *ClickFix* (or *FakeCAPTCHA*). On a compromised site, a small JavaScript loader sits in the page content. When a visitor opens the page, the loader downloads second-stage code from a C2 server and shows a fake "verify you are human" prompt. The prompt tries to trick the visitor into running commands or installing malware. What happens when a visitor actually follows that prompt is its own story: we reconstructed a full ClickFix intrusion, from the fake CAPTCHA to a blocked malware loader on the victim's machine, in [a separate case study](https://blog.sicuranext.com/one-paste-to-rule-them-all-inside-a-clickfix-etherhiding-guloader-intrusion/).

Incident responders know the hard part here: most affected operators do not know they are compromised. The site keeps working normally, because the injection only runs in the visitor's browser.

This is the question that guided our work. How many publicly exposed Ghost sites are already compromised by this campaign, and how can we prove it in a way others can check, without attacking anyone, so the victims can be told?

## Methodology: read-only by design

One rule shaped the whole project. We do not exploit the flaw, we do not attempt access, and we do not write anything. The scanner sends only GET requests to public pages, the same requests any visitor's browser would send, and looks for traces of the attack in content the site already serves.

This is not a technical compromise. It keeps the work on more defensible legal ground and makes it repeatable and publishable. The proof that a site is compromised is the malicious loader in its pages. Re-exploiting the flaw against third-party sites would put us in the same legal position as the attacker and would add nothing to the evidence. Read-only access does not answer every legal question on its own, since data-protection and computer-misuse rules differ between countries. That is also why we do not publish any detail that could identify a victim. See *A note on disclosure*.

The scanner uses a User-Agent with a contact address, so operators can recognize the activity as harmless in their logs.

### Discovery

We did not start from a prepared list of domains. We queried **Shodan** with the application fingerprint of Ghost:

```
http.component:"Ghost"
```

This returned **2,450 hosts** at the time of the scan. Expanding the DNS names tied to each host gave us **3,153 hostnames** to analyze. The discovery step is interchangeable. The same pipeline can also be fed from Censys, FOFA, Netlas, or Certificate Transparency logs, with deduplication applied afterwards.

### Per-domain pipeline

For each hostname, in this order:

1. resolve DNS, then fetch the homepage (HTTPS, with an HTTP fallback);
2. fingerprint Ghost (generator meta tag, assets, markup, RSS) and extract the version;
3. classify the version against the vulnerable range;
4. if the site is Ghost, sample several articles through the sitemap or RSS;
5. scan the homepage and the articles for the signatures;
6. aggregate, then decide the verdict.

Verdict and version status are two separate properties. A site can be `clean` but `vulnerable`, which makes it a candidate for a preventive notification, or `patched` but still `compromised`. As we show below, the second case is not just theoretical.

### Data-driven detection

The signatures live in a versioned data file, not in the code, and each one has a confidence level (`high`, `medium`, or `low`). The indicators come from published threat intelligence on the campaign (XLab/QiAnXin) and fall into four groups.

* Known C2 domains. High confidence when found in the page content.
* String and regex markers: the loader identifier (`ghost_once_footer_`), the `btoa(location.origin)` fingerprint, and patterns tied to a second actor.
* Base64-encoded C2 URLs: the encoded literal used by the loader.
* Decoded-text indicators: stable fragments such as the path `/11z77u3.php`, which stay the same even when the C2 domain changes.

Aggregation rule: a site is marked `compromised` on at least one `high` hit, or two `medium` hits, or one `medium` plus one `low`. Weak signals on their own give a `suspicious` verdict.

The key design choice is **in-page base64 decoding**. The scanner pulls out the...