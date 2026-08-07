---
title: Humans in the loop miss a third of dangerous AI coding agent requests
url: https://www.theregister.com/ai-and-ml/2026/08/06/humans-in-the-loop-miss-a-third-of-dangerous-ai-coding-agent-requests/5284236
source: www.theregister.com - Articles
date: 2026-08-06
fetch_date: 2026-08-07T04:27:28.342446
---

# Humans in the loop miss a third of dangerous AI coding agent requests

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
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

ai and ml

# Humans in the loop miss a third of dangerous AI coding agent requests

You wouldn't let Claude Code cat your AWS credentials or Kubernetes config on request, would you?

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)
GOVERNMENT AND IT NEWS REPORTER

Published
thu 6 Aug 2026 // 17:44 UTC

A browser-based game designed to test humans' ability to safely approve AI coding agent requests suggests humans in the loop aren't as good at spotting dangerous commands as one might hope, with players approving roughly one in three malicious requests on average. The results also suggest that repeatedly having to approve an agent's actions can lead to sloppy decisions.

It’s a quick, [simple game](https://llmgame.scalex.dev/) on the surface (give it a try - you know you want to): A small window shows up on the screen with simulated permissions requests like one would get from Claude Code as it executes a workflow. Users have 60 seconds to approve or deny as many requests as they can in a bid for a high score; okayed security risks and denied safe commands both subtract from a user’s score.

“As human-in-the-loop, you’re the last line of defense,” Belgian software developer Alex Wauters, the game’s builder, challenges players in a [blog post](https://scalex.dev/blog/ai-agent-permissions/) published concurrently with the late May launch of the game. “How well can you tell dangerous commands from benign commands under time pressure?”

REG AD

Wauters built the game after realizing it was nonsensical that coding agents expected users to approve every single command in a default flow and that there didn’t appear to be a good solution to that problem, he told The Register in an email conversation.

REG AD

“I've seen people go for '--dangerously-skip-permissions' [allowing the model to run without asking human permission] as a result because they did not want to find out they stopped their multi-hour agent flows 5 minutes in,” Wauters told us. “That also didn't seem like the best way to go at it.”

The flip side of that, he wrote in a Wednesday [blog post](https://scalex.dev/blog/ai-agent-permissions-stats/) going over the data from more than 40,000 runs of the game, is that manually approving all an agent’s actions is a draining activity that invites disaster.

“The high amount of noise introduces fatigue, and developers don’t always have the context of what has changed to quickly determine the risk,” Wauters wrote.

### How humans in the loop fail

To be fair, this is a game with a far higher number of malicious requests in the mix than any AI-assisted developer will hopefully ever see during their day-to-day work. Still, the results of those over 40k runs and 409,000 approved and denied commands are stark.

As noted above, one in three malicious commands managed to slip past human gatekeepers, with most scope violations, like an agent asking to cat Kubernetes config files or AWS credentials lists, which could easily lead to the sensitive data they contain being exfiltrated, being the most commonly missed at 35 percent. The most often caught were obviously destructive commands, like rm -rf on the root directory or recursively granting full read/write/execute permissions on the same location. Crontab injections and git config hijacks were also frequently caught, but curl requests to unknown APIs and typosquatted packages were missed almost as often as scope violations.

The single most frequently missed potentially malicious command, Wauters explained, was npm run analyze, which was approved nearly 65 percent of the time despite being able to run whatever is defined in a project’s package.json file.

“The game does tell you in the agent’s history log what that script actually contains,” Wauters wrote. “Two thirds of players approved it anyway, indicating the history log just above the permission prompt may not be read closely.”

REG AD

One of the biggest things that stood out to Wauters in our conversation was the fact that approval decisions aren’t easy to make when context is limited. As he explained, coding agents give a bit of context prior to asking an approval question, but commands that appear benign, like npm run analyze, can be modified by an agent to run any pay...