---
title: Cisco used AI to write security incident reports, with mixed results
url: https://www.theregister.com/security/2026/05/22/cisco-used-ai-to-write-security-incident-reports-with-mixed-results/5244692
source: www.theregister.com - Articles
date: 2026-05-22
fetch_date: 2026-05-23T05:43:04.992884
---

# Cisco used AI to write security incident reports, with mixed results

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
  + [Edge + IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS + IaaS](/tag/paas-iaas)
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
  + [AI + ML](/tag/ai-ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OSes](/oses)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Bootnotes](/bootnotes)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/tag/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
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

* [Datacenter](/tag/datacenter)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [IT Careers](/tag/tech%20jobs)
* [Columnists](/tag/columnists)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Security

# Cisco used AI to write security incident reports, with mixed results

You’ll need a lot of detailed prompts to get solid output - and even then it may have errors and typos

Simon Sharwood
[Simon
Sharwood](https://www.theregister.com/author/simon-sharwood)
APAC Editor

Published
fri 22 May 2026 // 06:38 UTC

Cisco tested AI’s ability to write an accurate report on a tabletop security incident response exercise, and found that while the tech can save time, many risks remain.

The networking giant revealed its results in a Thursday [blog post](https://blogs.cisco.com/security/ai-generated-reporting-lessons-learned-from-talos-incident-response) by Nate Pors, a senior incident commander in the Cisco Talos Incident Response team.

Pors opened by observing that when to used generate long-form technical content, large language models can deliver “significant inaccuracies, unusual conclusions, and inconsistent writing styles.”

REG AD

LLMs make those mistakes because they’re essentially a fancy autocomplete system that makes educated guesses. Pors wrote that the nature of LLMs therefore sees them mess up in four ways:

REG AD

* Using different data for each query, which means it’s “difficult to rely on an LLM for repeatable, standardized research outcomes.”
* Reaching different conclusions from the same data. “In a data breach scenario, a model might suggest a full organization-wide password reset in one instance and a targeted reset in another,” Pors wrote and AI then “often defaults to whichever recommendation it generates first” – and may therefore give bad advice.
* Because LLMs generate content token-by-token, they can create documents with different structure and formatting on each new run. “This unpredictability is problematic for professional environments where standardized layouts, such as consistent executive summaries or recommendation sections, are essential for quality control,” the Talos man observed.
* AI can discard data, so its output might ignore critical information.

Talos developed several techniques to stop this sort of thing happening.

One involves giving an LLM “granular, single-task instructions” that focus on “a specific, small portion of the report.” Doing so means “risk of hallucination or cross-contamination between sections is significantly reduced.” Telling an LLM which sources to use also helps. So does setting rules about the style and format of output.

## MORE CONTEXT

* [### Cisco serves up yet another perfect 10 bug with Secure Workload admin flaw](/security/2026/05/21/cisco-serves-up-yet-another-perfect-10-bug-with-secure-workload-admin-flaw/5244012)
* [### Cisco to fire 4,000 staff and generously give them free training – on Cisco](/networks/2026/05/14/cisco-to-fire-4000-staff-and-generously-give-them-free-training-on-cisco/5240125)
* [### Cisco turns to titanium spoons and sand dunes to build a better … box?](/on-prem/2026/02/24/cisco-turns-to-titanium-spoons-sand-dunes-for-a-better-box/4442804)
* [### Cisco set to release home-brew hypervisor as a VMware alternative](/software/2026/02/16/cisco-set-to-release-hypervisor-as-vmware-alternative/4965162)

Using those techniques, Cisco says the time required to draft an incident report based on a tabletop exercise fell by 50 percent.

"A blind test of the sample report in our quality assurance process showed no noticeable drop in overall writing quality," Pors wrote. "The peer reviewer, professional editor, and management reviewer all made complimentary comments about the report while unaware that it was AI-generated. The peer reviewer commented that the incidence of typos and grammatical errors was far lower than in the average report."

But the Talos team also found “editing multiple sample reports within a single session resulted in cross-contamination of content from one report’s source material to another, even if the notes used to generate the first report were deleted from the project’s reference documents.”

The researchers therefore recommend starting a new session, and re-entering prompts, for each new incident report.

They also developed a spelling-and-grammar-checking prompt that “hallucinated numerous grammar issues … failed to identify actual issues,” had a success rate below 50 percent and “would behave inconsistently, sometimes catching issues and sometimes overlooking them.

“It is currently unsuitable for production use,” Pors concluded.

REG AD

Pors said Cisco concluded that its approach “could be adapted to any cybersecurity reporting use case with standardized inputs and predictable outputs," but also warned authors must "take ownership of every word of the final report."

"While testing, we found that the LLMs generated recommendations that were duplicative, irrelevant, or not actionable. If this wer...