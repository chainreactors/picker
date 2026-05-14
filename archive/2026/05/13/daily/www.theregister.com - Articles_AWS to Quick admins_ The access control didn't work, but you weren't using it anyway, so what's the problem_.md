---
title: AWS to Quick admins: The access control didn't work, but you weren't using it anyway, so what's the problem?
url: https://www.theregister.com/paas-and-iaas/2026/05/13/aws-patched-quick-auth-bypass-says-customers-werent-using-control/5240041
source: www.theregister.com - Articles
date: 2026-05-13
fetch_date: 2026-05-14T05:47:25.048969
---

# AWS to Quick admins: The access control didn't work, but you weren't using it anyway, so what's the problem?

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

PaaS + IaaS

# AWS to Quick admins: The access control didn't work, but you weren't using it anyway, so what's the problem?

If a setting fails in the forest and nobody hears it ...

Corey Quinn, special to El Reg
[Corey
Quinn, special to El Reg](https://www.theregister.com/author/Corey-Quinn)

Published
wed 13 May 2026 // 23:56 UTC

Most users put up with AWS the way you put up with the DMV. I say this with love, but it's hard to disagree that the UI is awful. The console is a UX time capsule if time capsules weren't allowed to ever look like other time capsules. The pricing pages were designed by someone who hates you personally, and you accept all of it because the one thing AWS has historically gotten right is the boring, important stuff. The security model. The IAM language no one likes, but everyone trusts. The boundary between your account and someone else's. Get that wrong, and the whole bargain collapses.

So when Fog Security [disclosed](https://www.fogsecurity.io/blog/authorization-bypass-in-amazon-quick-ai-agents) an authorization bypass in Amazon Quick on May 12 (that's the [BI service](https://www.theregister.com/software/2026/04/29/aws-plants-more-tombstones-in-the-application-graveyard/5225226) formerly known as QuickSight, briefly known as Quick Suite, and now apparently just Quick, but check back next week) and AWS responded with a statement claiming "no customer data was at risk," it's fair to ask which definition of customer data they're using. Because it isn't an obvious one, and it certainly isn't mine.

### What Fog found

REG AD

Fog reports that when an Amazon Quick administrator (which is an absolutely devastating personal insult) uses "custom permissions" to explicitly deny access to AI Chat Agents, the UI correctly hides the feature. Great! Awesome! I sure wish to hell I could do that with S3 buckets to which I do not have access! Notably, there's no other way for an admin to do this - it's custom permissions or naught.

REG AD

The API, however, was perfectly willing to keep answering chat requests for any user in the account who knew how to send them. Fog's proof-of-concept was a non-admin asking the agent "Tell me about mangoes" from a session that was, on paper, locked out of the agent entirely. The agent told them about mangoes.

AWS deployed the fix between March 11 and March 12, eight days after Fog reported it via HackerOne. So far, so coordinated. Seriously, for a company of this scale, that's underpants-outside-the-pants superhero speed. Good for you; gold star.

### What came next

Where this gets uncomfortable is the response. AWS classified the severity as "none." It issued no customer notification. It published no advisory.

After Fog disclosed the HackerOne report and published a blog post, AWS provided a statement to Fog Security reading, in full: "We appreciate Fog Security's coordinated disclosure. This issue was addressed in March 2026. No customer data was at risk and there is no customer action required. As always, customers can contact AWS Support with any questions or concerns about the security of their account."

Take that sentence apart and see how much work "no customer data was at risk" is doing.

Amazon Quick is described on its own product page as an AI assistant that "connects Slack, Microsoft Teams and Outlook, CRMs, databases, and documents in one place" and "grounds every answer in your real business data." The default chat agent, which is automatically and annoyingly provisioned the instant Quick is enabled whether the customer wants those AI features or not, is the front end for that data. It is the whole point of the front end for that data.

Now consider the actual scenario AWS just patched. An administrator at, say, a regulated bank (an unregulated bank is called "a criminal enterprise that hasn't been caught yet") configures custom permissions denying chat agent access to a large group of users. Maybe those users are contractors. Maybe they're in a business unit that isn't cleared for AI tools. Maybe the bank's compliance posture flat-out prohibits shadow AI usage on top of internal data. Until two months ago, every one of those users could send an HTTP request directly to the agent endpoint and get a response.

REG AD

Fog asked about mangoes because they're a security firm doing a clean disclosure, not a malicious insider. A malicious insider would not have asked about mangoes.

The question to AWS, with no rhetoric attached: In what sense was customer data not at risk? Either the chat agent doesn't actually have access to the data the product page says it does (in which case the marketing department has some serious splainin' to do) or unauthorized users could query an agent wired into customer data, in which case "customer data was at risk" is the corr...