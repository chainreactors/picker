---
title: Anthropic’s bug-hunting Mythos was greatest marketing stunt ever, says cURL creator
url: https://www.theregister.com/security/2026/05/11/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/5238111
source: www.theregister.com - Articles
date: 2026-05-11
fetch_date: 2026-05-12T05:39:14.576126
---

# Anthropic’s bug-hunting Mythos was greatest marketing stunt ever, says cURL creator

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
  + [PaaS + IaaS](/paas_iaas)
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
  + [AI + ML](/ai_ml)
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

# Anthropic’s bug-hunting Mythos was greatest marketing stunt ever, says cURL creator

After all that hype, AI scanner found one low-severity cURL flaw

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)

Published
mon 11 May 2026 // 17:30 UTC

cURL developer Daniel Stenberg has seen Anthropic’s Mythos, a model the AI biz has suggested is too capable at finding security holes to release publicly, scan his popular open source project. But after the system turned up just a single vulnerability, he concluded the hype around Mythos was “primarily marketing” rather than a major AI security breakthrough.

Stenberg [explained](https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/) in a Monday blog post that he was promised access to Anthropic’s Mythos model - sort of - through the AI biz’s Project Glasswing program. Part of Glasswing involves giving high-profile open source projects access via the Linux Foundation, but while Stenberg signed up to try Mythos, he said he never actually received direct access to the model. Instead, someone else with access ran Mythos against curl’s codebase and later sent him a report.

“It’s not that I would have a lot of time to explore lots of different prompts and doing deep dive adventures anyway,” Stenberg explained. “Getting the tool to generate a first proper scan and analysis would be great, whoever did it.”

REG AD

That scan, which analyzed curl’s git repository at a recent master-branch commit, was sent back to him earlier this month, and it found just five things that it claimed were “confirmed security vulnerabilities” in cURL. Saying he had expected an extensive list of vulnerabilities, Stenberg wrote that the report “felt like nothing,” and that feeling was further validated by a review of Mythos’ findings.

REG AD

“Once my curl security team fellows and I had poked on this short list for a number of hours and dug into the details, we had trimmed the list down and were left with one confirmed vulnerability,” Stenberg said, bringing us back to the aforementioned number.

As for the other four, three turned out to be false positives that pointed out cURL shortcomings already noted in API documentation, while the team deemed the fourth to be just a simple bug.

“The single confirmed vulnerability is going to end up a severity low CVE planned to get published in sync with our pending next curl release 8.21.0 in late June,” the cURL meister noted. “The flaw is not going to make anyone grasp for breath.”

That said, Mythos did find several other non-security bugs that Stenberg said the team is working on fixing, and he notes that their description and explanation were well done. Mythos can do good work, in other words, but it’s [not a ground-breaking, game-changing AI model](https://www.theregister.com/security/2026/04/22/anthropic-mythos-shaping-up-as-nothingburger/5225649) like Anthropic has claimed.

“My personal conclusion can however not end up with anything else than that the big hype around this model so far was primarily marketing,” Stenberg said in the blog post. “I see no evidence that this setup finds issues to any particular higher or more advanced degree than the other tools have done before Mythos.”

### cURL code is no stranger to AI

To say cURL has become widely used in its nearly three decades of existence would be an understatement. Its wide reach has meant that its team has been running it through all sorts of static code analyzers and fuzz testing it since well before the dawn of the AI age. With AI’s rise, the cURL team has adapted, meaning Mythos is hardly the first AI to get its fingers on cURL’s codebase.

“These tools and the analyses they have done have triggered somewhere between two and three hundred bugfixes merged in curl through-out the recent 8-10 months or so,” Stenberg said of tools like AISLE, Zeropath, and OpenAI Codex Security that’ve tested cURL code. “A bunch of the findings these AI tools reported were confirmed vulnerabilities and have been published as CVEs. Probably a dozen or more.”

REG AD

Stenberg’s experience with AI testing cURL, in other words, makes it a great candidate to see how effective Mythos can really be at finding more than the average AI.

As Stenberg noted elsewhere in his blog post, Mythos isn’t doing anything particularly novel when it comes to security discoveries: It might be a bit better at finding things than previous models, but “it is not better to a degree that seems to make a significant dent in code analyzing,” the cURL author noted.

Stenberg isn’t an AI doomer when it comes to its ability to improve software design, though. Yes, he may have [closed the cURL bug bounty](https://www.theregister.com/security/2026/01/21/curl-shutters-bug-bounty-p...