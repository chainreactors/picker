---
title: ARToken: Inside an EvilTokens affiliate panel targeting Microsoft 365
url: https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/
source: Over Security
date: 2026-07-01
fetch_date: 2026-07-02T05:58:11.080657
---

# ARToken: Inside an EvilTokens affiliate panel targeting Microsoft 365

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# ARToken: Inside an EvilTokens affiliate panel targeting Microsoft 365

By
[Michael Kelley](https://blog.talosintelligence.com/author/michael-kelley/)

Wednesday, July 1, 2026 06:00

[Threat Advisory](https://blog.talosintelligence.com/category/threat-advisory/)

* Cisco Talos identified a fully-featured phishing-as-a-service (PhaaS) operator panel, branded "ARToken," that shares infrastructure, API contracts, and operational patterns with the EvilTokens platform documented by Sekoia and Microsoft in early 2026.
* The ARToken panel exposes 80+ API endpoints for device code phishing, Primary Refresh Token (PRT) persistence, email access, business email compromise (BEC) operations, and SharePoint exfiltration — all accessible to operators through a React-based dashboard.
* Analysis of the platform's publicly served JavaScript bundle reveals the complete post-compromise toolkit available to affiliates, including capabilities not previously detailed in public reporting on EvilTokens.
* The phishing kit deploys a seven-layer anti-analysis system combining client-side behavioral verification with XOR-encrypted payloads, a more sophisticated evasion approach than the server-side X-Antibot-Token mechanism documented in prior EvilTokens research.

## Background: EvilTokens and device code phishing-as-a-service

In March 2026, Sekoia published a two-part analysis of EvilTokens, a PhaaS platform that abuses Microsoft's OAuth 2.0 Device Authorization Grant (RFC 8628) to capture victim tokens while bypassing multi-factor authentication (MFA) entirely. Microsoft [confirmed the campaign's scale](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/) in April 2026, noting significantly higher success rates than previous device code attacks, AI-powered personalized lures, and a post-compromise pipeline that included automated device registration for persistent access.

By the time of Microsoft's publication, Sekoia had documented approximately 500 Cloudflare Workers domains and over 1,000 total phishing pages operating under the EvilTokens umbrella, with affiliates targeting finance professionals, HR staff, and logistics personnel across global regions.

EvilTokens' second-stage capabilities, revealed in [Sekoia's Part 2 research](https://blog.sekoia.io/eviltokens-an-ai-augmented-phishing-as-a-service-for-automating-bec-fraud-part-2/), include an AI-augmented BEC pipeline chaining Groq-hosted Llama models for financial exposure scoring and GPT-4o-mini for email translation, producing three tailored BEC scenarios per compromised mailbox. The platform sells access at $1,500 one-time plus $500/month, with a standalone "Portal Browser" for $500 lifetime.

## The lure in the wild: Vendor-impersonation invoice fraud

Most public reporting on EvilTokens covers the panel and the kit. What it has not shown is how an ARToken lure actually reaches an inbox. Talos recovered two near-identical messages, sent roughly four minutes apart on April 20, 2026, that initiate the chain. The tradecraft is targeted, not spray-and-pray.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/06/Picture1.png)

**Figure 1. A sample ARToken phishing email**

The messages spoof an accounts-payable contact at a legitimate Wisconsin contractor, addressed to an accounts-payable recipient at a U.S. life-sciences company — abusing a real vendor relationship rather than inventing a sender. The lure theme is an outstanding-invoice query ("the following invoices appear to still be outstanding… advise when this will be processed"), the kind of message accounts-payable staff are conditioned to act on. Other features of note in this email include:

* The From header presents the vendor's real domain, but Reply-To quietly redirects replies to an unrelated domain — a classic reply-pivot that keeps any victim response away from the spoofed organization.
* All three checks fail: SPF, DKIM (body-hash mismatch), and DMARC (compauth=none reason=405). The display identity is not authenticated from the sending path.
* Each message carries short random hex strings and an inline signature image (pumber.png), consistent with light per-message mutation to frustrate exact-match content rules.
* The visible anchor text reads as the vendor's genuine SharePoint tenant:
  “https[:]//mononapfp.sharepoint[.]com/:f:/document/INV-IgCx1X50pgUjR7iAjZL2fuQaAW4GfKVs6wHT3BYv9sgwW7g”

However, the actual href points to a near-identical look-alike tenant — the vendor's name with the .com folded directly into the tenant label — under a different, attacker-controlled Microsoft 365 workspace. Because the destination is still a genuine sharepoint.com host, it inherits SharePoint's clean reputation: “https[:]//mononapfpcom.sharepoint[.]com/:f:/g/IgAdH\_aaBPMcQbtINZzC1TsLARj3dHj63MnKjvnY-QJrKEc"

## Discovery: The ARToken Panel

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/06/Picture2.png)

**Figure 2. ARToken login page.**

During investigation of phishing infrastructure targeting a Talos IR engagement, we identified a management panel at “dashboard-bl.pamconj[.]com” serving a React single-page application (SPA) with a 1.7MB compiled JavaScript bundle. The page title reads "ARToken Panel."

SPA architecture exposes all client-side code including routes, UI labels, component logic, and API endpoint paths in the JavaScript bundle regardless of authentication state. No credentials were required or bypassed.

The associated command-and-control (C2) API operates at “spx.pamconj[.]com”, and phishing lures deploy through Cloudflare Workers accounts including “clear90489058903-document.workers[.]dev”.

## Linking ARToken to EvilTokens

The connection between ARToken and EvilTokens rests on multiple ...