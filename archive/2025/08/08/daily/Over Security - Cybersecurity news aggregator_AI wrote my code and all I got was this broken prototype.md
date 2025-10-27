---
title: AI wrote my code and all I got was this broken prototype
url: https://blog.talosintelligence.com/ai-wrote-my-code-and-all-i-got-was-this-broken-prototype/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-08
fetch_date: 2025-10-07T00:49:13.697650
---

# AI wrote my code and all I got was this broken prototype

# Cisco Talos Blog

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

# AI wrote my code and all I got was this broken prototype

By
[Martin Lee](https://blog.talosintelligence.com/author/martin-lee/)

Thursday, August 7, 2025 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

Vulnerabilities within software are a persistent challenge. Software engineers inadvertently tend to make the same mistakes repeatedly, with the same entries appearing in the [annual top 25](https://cwe.mitre.org/top25/) list of Common Weakness Enumerations each year.

The truth is, writing software is difficult. Software engineering is a craft demands concentration, knowledge and time, all coupled with extensive testing. Even the most skilled software engineer can get distracted or have a bad day, leading to a hidden vulnerability inadvertently making its way into a production codebase.

Identifying vulnerabilities early in the software development process is one of the promises of AI. The idea being that an AI agent would write perfect code under the direction of a software engineer or verify and correct code written by a human.

Last weekend, I decided to put this premise to the test. As a somewhat rusty software engineer, I resolved to see if AI could assist me with a personal software project. Initially, I was impressed, the AI agent offered an engaging discussion about high-level architecture and the trade-offs of various approaches. I was amazed at the lines of code that the AI generated on request. All the software for my project written at the press of a button!

Then came the testing. Although the code looked convincing, it failed to interface with the required libraries. Parameters were incorrect, it tried to call fictional functions. It seemed that the way the AI imagined the library to work didn’t reflect reality or the available documentation. Similarly, there were less sanity checks or verification of variable values than I was comfortable with; especially since many of these were derived from external inputs.

To be fair, the AI code resolved a tricky threading issue that had defeated me, and the ‘boilerplate’ code necessary to form the skeleton structure of the software was flawless. I felt that I achieved a productivity boost from the AI’s exposure to ‘frequently encountered’ coding issues. However, when it came to more esoteric APIs with which I was moderately familiar, the AI was unable to generate functional code or correctly diagnose reported errors.

After some debugging and manual rewriting, I managed to create a working prototype. The code is clearly not bulletproof, but then again, I hadn’t explicitly asked for code that was secured against all potential hacks. Like many software engineers, myself and my AI assistant focused on quickly delivering the desired functionality, rather than considering the long-term operation of the code in a potentially hostile environment.

I remain optimistic that AI assisted coding is the pathway to a software vulnerability free future. However, my recent limited personal experience leads me to think that we still have a considerable journey ahead before we can definitively resolve software vulnerabilities for good.

I hope you all have a tremendous time at Summer Camp, see a lot of old friends and make new ones and most importantly that you shower and use deodorant. Conference season is a marathon, it’s long, it’s arduous, it’s sweaty – be the hygienic change you want to see in the world.

## The one big thing

Continuing the AI theme, Guilherme describes how [AI LLM models](https://blog.talosintelligence.com/using-llm-as-a-reverse-engineering-sidekick/) can be used to assist in the reverse engineering of malware. Used correctly, LLMs can provide valuable insights and facilitate the analysis of malware.

### Why do I care?

Reverse engineering malware is the often time-consuming task of identifying the execution path of malicious software. Frequently malware writers obfuscate their code to make it difficult to understand and follow what their code is doing. Advances in technology that can speed up this process make fighting malware easier.

### So now what?

Investigate if the tools and approaches described in the blog can be used to improve your reverse engineering process, or as a means to begin learning about reverse engineering.

## Top security headlines of the week

### As ransomware gangs threaten physical harm, 'I am afraid of what's next,' ex-negotiator says

In an effort to increase the pressure on victims, ransomware gangs are now using threats of physical violence. ([T](https://www.theregister.com/2025/07/31/ransomware_physical_harm_threats/)[he Register](https://www.theregister.com/2025/07/31/ransomware_physical_harm_threats/))

### ‘Shadow AI’ increases cost of data breaches, report finds

Unmanaged and unsecured use of AI is leading to data breaches. ([Cybersecurity Dive](https://www.cybersecuritydive.com/news/artificial-intelligence-security-shadow-ai-ibm-report/754009/))

### **Enough to drive a cybersecurity officer mad: one rule here, a different rule there**

Chief information security officers call for less fragmentation in global cybersecurity regulations. ([ASPI](https://www.aspistrategist.org.au/enough-to-drive-a-cybersecurity-officer-mad-one-rule-here-a-different-rule-there/))

### **UK Online Safety Act promotes insecurity**

The implementation of the UK Online Safety Act requiring age verification for content deemed harmful to children introduces some security quandaries. ([Tech HQ](https://techhq.com/news/uk-online-safety-act-exposes-britons-to-internet-harm-data-loss-opinion/))

## Can’t get enough Talos?

### Cyber Analyst Series: Cybersecurity Overview and the Role of the Cybersecurity Analyst

A series of videos on the profe...