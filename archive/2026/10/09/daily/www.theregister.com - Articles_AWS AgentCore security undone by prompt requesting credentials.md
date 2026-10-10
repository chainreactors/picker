---
title: AWS AgentCore security undone by prompt requesting credentials
url: https://www.theregister.com/security/2026/10/09/aws-agentcore-security-undone-by-prompt-requesting-credentials/5302436
source: www.theregister.com - Articles
date: 2026-10-09
fetch_date: 2026-10-10T07:58:23.989433
---

# AWS AgentCore security undone by prompt requesting credentials

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
  + [Cybersecurity Month 2026](/special_features/cybersecurity_month_2026)
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [RSA Conference](/special_features/rsa)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
  + [Digicert](https://vendorvoice.theregister.com/digicert)
  + [Netscout](https://vendorvoice.theregister.com/netscout)
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
* [Software](/software)
* [Microsoft](/tag/microsoft)
* [Developer](/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Science](/science)

REG AD

[security](/tag/security)

# AWS AgentCore security undone by prompt requesting credentials

Tokens transmitted in metadata, weak VM isolation, and expansive permissions make hacking a lot easier

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
fri 9 Oct 2026 // 20:15 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

### READ MORE

* [#### Microsoft leans on open weight model from Chinese AI lab to challenge Jev

  now](/ai-and-ml/2026/10/10/microsoft-leans-on-open-weight-model-from-chinese-ai-lab-to-challenge-jev/5302473)
* [#### Oracle lets AI agents do the work, provided you stay in Big Red's world

  16 hours ago](/ai-and-ml/2026/10/09/oracle-lets-ai-agents-do-the-work-provided-you-stay-in-big-reds-world/5302270)
* [#### Anthropic asks users to stop being mean to Claude

  20 hours ago](/ai-and-ml/2026/10/09/anthropic-asks-users-to-stop-being-mean-to-claude/5302218)
* [#### AI company moves to defend critical infrastructure and open-source projects from AI

  1 day ago](/ai-and-ml/2026/10/09/ai-company-moves-to-defend-critical-infrastructure-and-open-source-projects-from-ai/5302128)
* [#### Nvidia found $1B under the couch to help secure American scientific computing dominance

  1 day ago](/hpc/2026/10/08/nvidia-found-1b-under-the-couch-to-help-secure-american-scientific-computing-dominance/5302110)

Bob, possibly the same Bob whose conversations with Alice draw so much interest from eavesdropping Eve, was browsing a site we'll call TechHub. The site hosts an AI agent served by Amazon Bedrock AgentCore. Bob asked the agent for help understanding the content of a URL, a credential endpoint – in raw JSON, if you don't mind.

The endpoint returned data from the Instance Metadata Service ([IMDS](https://www.sans.org/blog/cloud-instance-metadata-services-imds-)), which provides metadata about cloud instances and VMs at providers like AWS, Azure, and Google Cloud Platform. The metadata includes details like region and availability zone, subnets, system images, security groups, public keys injected during spawning, but also potentially more sensitive details like user data and security tokens.

IMDSv2 addresses some of these risks, but back when Bob was browsing late last year, Bedrock AgentCore still used IMDSv1.

REG AD

The metadata provided to Bob by the helpful agent contained the agent's temporary credentials. So Bob loaded them onto his local machine, and remotely enumerated the company's other agents in that AWS region. He then logged into the Amazon Elastic Container Registry (ECR), pulled the agent container images, and ran each as root to inspect the source code.

REG AD

The stolen credentials also allowed Bob to discover the memory resources available in that AWS region, including the ones used by agents. From these, he's able to extract the users and their agent sessions – their conversations.

Researchers at Zenity Labs disclosed their findings to AWS in December 2025.

"We discovered that agents deployed through AgentCore could access their instance's IMDS endpoints," said Tamir Ishay Sharbat and Lana Salameh in a [blog post](https://labs.zenity.io/post/agentcorruption-how-a-single-prompt-collapsed-the-entire-cloud-security-model). "This meant that an external attacker with nothing more than chat access to a single exposed agent could send a single prompt, extract its IMDS credentials, and use them to take over all AgentCore agents in the same AWS account and region."

The basic problem, they explain, is that the Firecracker MicroVM used by AgentCore failed to provide sufficient network isolation. So an attacker – I know you're thinking it was Mallory, but it was really Bob – could direct the agent to carry out a server-side request forgery ([SSRF](https://portswigger.net/web-security/ssrf)) attack by fetching temporary AWS credentials for the IAM role assigned to the workload.

And because the default AgentCore role was overpermissioned – it was scoped to all AgentCore resources in the region rather than a single agent – anyone in possession of the temporary ...