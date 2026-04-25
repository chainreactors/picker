---
title: Trust Boundary of SaaS Will Include Customers' AI Agents
url: https://zeltser.com/saas-ai-agent-trust-boundary
source: Lenny Zeltser
date: 2026-04-24
fetch_date: 2026-04-25T04:38:30.756342
---

# Trust Boundary of SaaS Will Include Customers' AI Agents

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# Trust Boundary of SaaS Will Include Customers' AI Agents

SaaS vendors should assess whether their trust boundary includes customers' AI agents. Liability has pushed banks toward securing the customer's device four times, and the fifth wave is forming around AI agents.

![Trust Boundary of SaaS Will Include Customers' AI Agents - illustration](/assets/saas-ai-agent-trust-boundary.DuHgOWNm_ZtMjc6.webp)

As SaaS vendors make their products usable by customers’ AI agents, they’ll face a trust-boundary decision. Is the vendor responsible for securing any aspect of the customer’s client system? The answer might seem like an easy “no,” but financial services have answered it four times, always with some form of “yes.”

Banks now fingerprint browsers, shield mobile apps, score typing rhythm, and bind credentials to device hardware. Each security measure followed a specific threat, loss, or legal action. This pattern will repeat for customers’ AI agents, and the last four rounds inform how we should prepare for the next one.

## Agent infrastructure is shipping ahead of its defenses.

AI agents are a [new endpoint for interacting with SaaS](/designing-for-humans-and-ai), but the threats against them lack strong defenses. For example, [OpenAI flagged](https://openai.com/index/hardening-atlas-against-prompt-injection/) that prompt injection is unlikely to ever be fully “solved.” Simon Willison’s “[lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)” of sensitive data access, untrusted content, and outbound connectivity describes the capabilities that enable exploitation.

Every SaaS product that interacts with a customer’s AI agent inherits that attack surface. The exposure is greatest for consumer-facing products because enterprise customers are subject to security controls from their organizations.

In the meantime, vendors are making increasingly powerful capabilities accessible natively to AI agents. In banking, for example, Meow lets customers open and run business accounts [through AI agents](https://www.meow.com/blog/ai-agents-can-now-open-and-run-your-business-bank-account) with customer-controlled restrictions. GoCardless targets bank-payment integration, [introducing MCP](https://gocardless.com/blog/gocardless-introduces-ai-native-tool/) as groundwork for agentic commerce.

Card networks are starting to write the rules for agent commerce before the defenses take shape. [Visa Trusted Agent Protocol](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21716.html) and [Mastercard Agent Pay](https://www.mastercard.com/us/en/news-and-trends/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai.html) were announced in 2025. American Express followed in April 2026 with a [network-level liability commitment](https://www.americanexpress.com/en-us/newsroom/articles/innovation/american-express-debuts-agentic-commerce-experiences--ace--devel.html) that covers agent-initiated purchases.

How should vendors decide whether, when, and how to invest in securing customers’ AI agent systems? We can extrapolate from how the banking industry has answered versions of that question over recent decades.

## Four drivers push providers toward the customer’s device.

Four drivers have shaped when and how banks extended security measures onto the customer’s device:

* **Liability:** The US [Regulation E](https://www.consumerfinance.gov/rules-policy/regulations/1005/) in 1979 and the [UK APP reimbursement rule](https://www.psr.org.uk/publications/policy-statements/ps247-faster-payments-app-scams-reimbursement-requirement-confirming-the-maximum-level-of-reimbursement/) in 2024 pushed fraud loss onto banks. Banks funded defensive controls in response.
* **Regulatory standard of care:** Actions from [FFIEC 2005](https://www.fdic.gov/news/inactive-financial-institution-letters/2005/fil10305.html) through the [EBA RTS on SCA](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32018R0389) in 2018 each raised the minimum controls banks had to deploy.
* **Customer inability to self-protect:** [Banking trojans in the late 2000s](https://archives.fbi.gov/archives/news/stories/2010/october/cyber-banking-fraud) and [mobile malware in the early 2010s](https://www.ftc.gov/news-events/events/2013/06/mobile-security-potential-threats-solutions) pushed banks toward device fingerprinting, transaction signing, and out-of-band confirmation.
* **Loss economics:** Losses grew costly enough to justify app shielding and behavioral biometrics at scale, since liability assigned them to banks.

These drivers produced four waves of customer-device controls. A fifth wave is forming around AI agents, and history predicts how it’ll play out.

## Four waves pushed banks onto the customer’s device.

The following four waves pushed banks to deploy new security measures on customers’ devices. The pressure came from a mix of threats, research, court cases, and regulations:

* **Wave 1 (2005-2008):** The [FFIEC’s 2005 authentication guidance](https://www.fdic.gov/news/inactive-financial-institution-letters/2005/fil10305.html) pushed banks toward stronger authentication. Banks [rolled out SiteKey](https://www.finextra.com/newsarticle/13731/bank-of-america-to-introduce-passmark-authentication-technology) for consumer banking, while RSA hardware tokens became common for business customers. Research [demonstrated a proxy attack](https://www.cr-labs.com/publications/SiteKey-20060718.pdf) within a year, and [user studies found](https://ieeexplore.ieee.org/document/4223213/) customers ignored the missing SiteKey image.
* **Wave 2 (2008-2013):** Banking trojans such as [Zeus](https://krebsonsecurity.com/2015/02/fbi-3m-bounty-for-zeus-trojan-author/), [SpyEye](https://en.wikipedia.org/wiki/SpyEye), and [Gozi](https://krebsonsecurity.com/2013/01/three-men-charged-in-connection-with-gozi-trojan/) operated from inside authenticated browser sessions, where SiteKey and tokens offered no defense. Courts testing [UCC Article 4A](https://www.law.cornell.edu/ucc/4a) in [Experi-Metal](https://www.govinfo.gov/content/pkg/USCOURTS-mied-2_09-cv-14890/pdf/USCOURTS-mied-2_09-cv-14890-3.pdf), [Patco](https://law.justia.com/cases/federal/appellate-courts/ca1/11-2031/11-2031-2012-07-03.html), and [Choice Escrow](https://law.justia.com/cases/federal/appellate-courts/ca8/13-1879/13-1879-2014-06-11.html) applied a commercially reasonable security standard. Banks whose defenses fell short bore the loss.
* **Wave 3 (2013-2020):** Mobile malware such as [Marcher](https://www.securityweek.com/thousands-android-devices-infected-marcher-trojan/) and [Anubis](https://www.bleepingcomputer.com/news/security/anubis-android-malware-returns-to-target-394-financial-apps/) moved the attack surface to phones, prompting app shielding and behavioral biometrics. SIM swap eroded SMS OTP, as the FCC’s [2023 Report and Order](https://docs.fcc.gov/public/attachments/FCC-23-95A1.pdf) acknowledged.
* **Wave 4 (2019-2026):** [PSD2 SCA](https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-opinion-elements-strong-customer-authentication) required dynamic linking, phasing out static OTPs. Apple, Google, and Microsoft [committed to passkeys](https://fidoalliance.org/apple-google-and-microsoft-commit-to-expanded-support-for-fido-standard-to-accelerate-availability-of-passwordless-sign-ins/) across consumer platforms, and Germany’s [chipTAN](https://en.wikipedia.org/wiki/Transaction_authentication_number) signed transactions off-device. The [UK APP reimbursement rules](https://www.psr.org.uk/publications/policy-statements/ps247-faster-payments-app-scams-reimbursement-requirement-confirming-the-maximum-level-of-reimbursement/) required banks to reimburse scam victims.

Regulation and liability are the constants across all four wav...