---
title: Close Encounters of the Human Kind
url: https://blog.talosintelligence.com/close-encounters-of-the-human-kind/
source: Over Security
date: 2026-06-18
fetch_date: 2026-06-19T07:08:53.053244
---

# Close Encounters of the Human Kind

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

# Close Encounters of the Human Kind

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Thursday, June 18, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s Threat Source newsletter.

I love a Spielberg summer. His ability to imbue a sense of wonder, awe, curiosity, and connection means he’s in a league of his own. Granted, I haven’t felt that from him in a while, but when he hits? Oof. I feel like I need somebody to reach across and take off my sunglasses.

So, *Disclosure Day* then. A group of friends and I visited a thankfully packed-out cinema at the weekend to bear witness to Spielberg’s latest dalliance with extra-terrestrial beings.

Thar be no spoilers here, but I do want to touch on one of the film’s central themes: the idea that a group of people (let’s call them “the government”) believes they can predict how humanity will react to world-changing information based on historical data patterns.

We often assume that information influences behaviour. Surely, if people have the right information, they'll make the right decision? If people understand the risk, they'll act.

However, the older I get, the less convinced I am that human beings are rational creatures.

Organisations know they should patch. People know they should use MFA. Leaders know they should practice an incident before it happens for real.

And yet.

Life is messy. Life, uh, finds a way.

Most people aren't making decisions in a vacuum. They need to contend with limited budgets, workloads, competing business priorities, and a hundred other things demanding their attention. "Knowing" what they should do is the easy part. The hard part is finding the time, resources, urgency, and collective will to actually do it.

As one of my colleagues [recently wrote](https://blogs.cisco.com/security/security-in-the-post-mythos-era), even in a post-Mythos world, many of the controls most likely to protect organisations are the same ones we've been talking about for years. Segmentation. Backups. MFA everywhere. Understanding if your controls are doing what they’re supposed to be doing.

And people can react to the exact same situation in very different ways.

Take the film itself. One of my friends remarked on the way out, "What a load of twaddle." (Do you use "twaddle" much in the U.S.? If not, I recommend introducing it into more sentences.) Another friend thought it was entertaining, exciting, and thought-provoking.

As Colin Firth’s character finds out in Disclosure Day, humans don’t always react the way you expect them to. I think that’s so important to acknowledge and work with, rather than against, in the cybersecurity field. Information is only one piece of the puzzle. Experience, priorities, personality, context, and a hundred other factors shape how people interpret and respond to that information.

So, this message probably won’t land with 99% of you. But for the 1% that it might, go ahead and do that MFA install you’ve been putting off.

Also, you’re running low on milk. Best pick some up on your way home.

## The one big thing

Cisco Talos [detailed a new approach](https://blog.talosintelligence.com/scripting-the-disassembler) to reverse engineering that pairs local AI agents with traditional analysis tools like the VB6 disassembler vbdec. Instead of awkwardly bolting AI onto the software, vbdec exposes its parsed data through a live Component Object Model (COM) interface. Analysts can simply use natural language prompts to automate complex tasks like decompiling functions or building call graphs. This transforms the disassembler from a static viewer into a highly interactive, queryable data server.

### Why do I care?

This methodology empowers analysts to generate custom workflows on the fly, completely bypassing the wait for new vendor features. It also solves a massive privacy hurdle: because the AI agent and disassembler share a local machine, sensitive binaries never leave your workstation. This architectural shift proves that any analysis tool holding structured data behind a GUI can become a powerhouse for agentic automation, saving defenders countless hours of tedious reverse engineering.

### So now what?

Tool developers should start exposing their application data through external scripting interfaces like COM or other inter-process communication (IPC) protocols. If you are analyzing VB6 binaries, enable remote scripting in vbdec and point your preferred local AI agent at the provided operator briefing to start automating your tasks. Security teams need to lean into this paradigm shift, letting agents handle the exhaustive, repeatable grunt work while analysts focus on the actual analysis. [Read the blog for more](https://blog.talosintelligence.com/scripting-the-disassembler)[.](https://blog.talosintelligence.com/scripting-the-disassembler)

## Top security headlines of the week

**ShinyHunters** **claims Council of Europe hack**
On Sunday, ShinyHunters added the Council of Europe to its Tor-based leak site, threatening to release more than 297GB of data allegedly stolen from the organization’s network. ([SecurityWeek](https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/))

**Sweeping credential-harvesting heist compromises +30K Fortinet devices**
A large-scale cyber espionage and credential-harvesting operation is actively targeting Fortinet firewalls and VPN gateways, and has already compromised more than 30,000 Internet-facing devices across nearly 200 countries. ([Dark Reading](https://www.darkreading.com/cyberattacks-data-breaches/sweeping-credential-harvesting-heist-compromises-30k-fortinet-devices))

**Fileless Phantom Stealer targets browser credentials**
In addition to executing entirely in memory, the malware's infection cha...