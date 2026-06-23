---
title: Cloudflare teams up with big browsers to help websites tell welcome from unwelcome visitors
url: https://www.theregister.com/software/2026/06/22/cloudflare-teams-up-with-big-browsers-to-help-websites-tell-welcome-from-unwelcome-visitors/5259782
source: www.theregister.com - Articles
date: 2026-06-22
fetch_date: 2026-06-23T06:08:23.088795
---

# Cloudflare teams up with big browsers to help websites tell welcome from unwelcome visitors

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Software

# Cloudflare teams up with big browsers to help websites tell welcome from unwelcome visitors

Makers of Chrome, Edge, Firefox back bot-fraud defense called Private Access Control Tokens

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
Senior reporter

Published
mon 22 Jun 2026 // 21:02 UTC

Cloudflare on Monday said that it has joined with the three leading commercial browser makers to create a privacy-preserving protocol that websites can use to separate desirable web traffic from undesirable network requests.

Cloudflare, along with Google Chrome, Microsoft Edge, and Mozilla Firefox, have committed to develop Private Access Control Tokens (PACTs), a way for websites to generate a digital token that asserts a given browsing session is being run by a human or bot with legitimate intent, as opposed to network requests from people or software deemed abusive or improper.

PACTs will let websites "with strong knowledge of 'personhood'" issue anonymous tokens that browser users and designated bots can present at other websites, so that fewer identity checks are necessary.

REG AD

Think of PACTs as a shareable, privacy-preserving CAPTCHA test result, where the desirability of the web traffic is being tested rather than whether the visitor is a human or bot – an increasingly difficult distinction.

REG AD

While the [technical details](https://github.com/antifraudcg/proposals/issues/22) are still being hammered out and harmonized between [related proposals](https://ietf-wg-privacypass.github.io/draft-ietf-privacypass-expiration-extension/draft-ietf-privacypass-expiration-extension.html), it isn't immediately clear what constitutes "strong knowledge of 'personhood'" in this context, particularly since "personhood" appears to extend to software that has been authorized to act on behalf of a legitimate person for an authorized purpose.

It may be that the test criteria puts certain browsers, behaviors, or network signals at greater risk of being denied the dispensation of a PACT, though past technical discussion by developers from Google and Mozilla suggests that excluding certain hardware, platforms, or user-agents is not a goal.

Dane Knecht, CTO of Cloudflare, argues that the way people interact with the web is changing and increasingly may involve autonomous agents.

"As AI-powered traffic becomes widespread, existing tools to support its use are too generic and coarse," said Knecht in [a statement](https://cloudflare.net/news/news-details/2026/Cloudflare-Collaborates-With-Leading-Browsers-to-Develop-a-Privacy-First-Protocol-For-the-Global-Internet/default.aspx). "Now this collaboration lets us eliminate the friction caused by security protocols for every visitor – whether they are human or agent – without sacrificing privacy."

## MORE CONTEXT

* [### Nvidia gets all agentic about supercomputing for scientific research](/systems/2026/06/22/nvidia-gets-all-agentic-about-supercomputing-for-scientific-research/5259553)
* [### The database that refused to die: How Postgres survived its own creators](/databases/2026/06/22/the-database-that-refused-to-die-how-postgres-survived-its-own-creators/5259716)
* [### Ukraine puts its Russian war trophies online for allies to pick apart](/offbeat/2026/06/22/ukraine-puts-its-russian-war-trophies-online-for-allies-to-pick-apart/5259688)
* [### Inspired by musical greeting cards, DARPA demands tiny, cheap, self-modifying systems](/offbeat/2026/06/22/inspired-by-musical-greeting-cards-darpa-demands-tiny-cheap-self-modifying-systems/5259594)

The claim "without sacrificing privacy" is a bit of an overstatement. PACT tokens, it appears, will not contain personal details. But they won't do anything to repair all the other ways browsers can facilitate digital fingerprinting and tracking. And if implemented poorly, they may introduce novel risks. Fundamentally, they divide the internet traffic into welcome and unwelcome traffic – something already widely done through firewalls and other technical measures but not easily reconciled with the notionally open web.

"Mozilla is committed to defending openness and user privacy on the web," said Bobby Holley, CTO for Firefox at Mozilla, in a statement. "An avalanche of automated traffic is pushing sites to adopt blunt defenses – paywalls, identity checks, CAPTCHAs, and invasive tracking – simply to tell whether a request comes from a human."

While Cloudflare touts the privacy benefits of PACTs, it's clear from the company's announcement that the technology is designed to "empower businesses to identify genuine visitors, ensuring they can focus their resources on the traffic that matters to them." Essentially, this is an anti-fraud initiative.

Many website operators have co...