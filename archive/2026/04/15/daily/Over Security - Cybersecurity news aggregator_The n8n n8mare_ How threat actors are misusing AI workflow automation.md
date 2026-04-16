---
title: The n8n n8mare: How threat actors are misusing AI workflow automation
url: https://blog.talosintelligence.com/the-n8n-n8mare/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-15
fetch_date: 2026-04-16T04:54:16.574512
---

# The n8n n8mare: How threat actors are misusing AI workflow automation

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

# The n8n n8mare: How threat actors are misusing AI workflow automation

By
[Sean Gallagher](https://blog.talosintelligence.com/author/sean-gallagher/),
[Omid Mirzaei](https://blog.talosintelligence.com/author/omid/)

Wednesday, April 15, 2026 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)

* Cisco Talos research has uncovered agentic AI workflow automation platform abuse in emails. Recently, we identified an increase in the number of emails that abuse n8n, one of these platforms, from as early as October 2025 through March 2026.
* In this blog, Talos provides concrete examples of how threat actors are weaponizing legitimate automation platforms to facilitate sophisticated phishing campaigns, ranging from delivering malware to fingerprinting devices.
* By leveraging trusted infrastructure, these attackers bypass traditional security filters, turning productivity tools into delivery vehicles for persistent remote access.

---

AI workflow automation platforms such as Zapier and n8n are primarily used to connect different software applications (e.g., Slack, Google Sheets, or Gmail) with AI models (e.g., OpenAI’s GPT-4 or Anthropic’s Claude). These platforms have been applied to different application domains, including cybersecurity over the past few months, especially with the progress that has been made in new avenues like large language models (LLMs) and agentic AI systems. However, much like other legitimate tools, AI workflow automation platforms can be weaponized to orchestrate malicious activities, like delivering malware by sending automated emails.

This blog describes how n8n, one of the most popular AI workflow automation platforms, has been abused to deliver malware and fingerprint devices by sending automated emails.

## What is n8n?

N8n is a workflow automation platform that connects web applications and services (including Slack, GitHub, Google Sheets, and others with HTTP-based APIs) and builds automated workflows. A community-licensed version of the platform can be self-hosted by organizations. The commercial service, hosted at n8n.io, includes AI-driven features that can create agents capable of using web-based APIs to pull data from documents and other data sources.

Users can register for an n8n developer account at no initial charge. Doing so creates a subdomain on “tti.app.n8n[.]cloud” from which the user’s applications can be accessed. This is similar to many web-based AI-aided development tools, and one that malicious actors have harnessed elsewhere in the past; earlier this year, Talos observed another AI-oriented web application service, Softr.io, being used for the creation of phishing pages used in a series of targeted attacks.

## How n8n’s webhooks work

Talos' investigation found that a primary point of abuse in n8n’s AI workflow automation platform is its URL-exposed webhooks. A webhook, often referred to as a “reverse API,” allows one application to provide real-time information to another. These URLs register an application as a “listener” to receive data, which can include programmatically pulled HTML content. An example of an n8n webhook URL is shown in Figure 1.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/AI_flow_automation_URL.jpg)

Figure 1. Anatomy of an example n8n webhook URL.

When the URL receives a request, the subsequent workflow steps are triggered, returning results as an HTTP data stream to the requesting application. If the URL is accessed via email, the recipient’s browser acts as the receiving application, processing the output as a webpage.

Talos has observed a significant rise in emails containing n8n webhook URLs over the past year. For example, the volume of these emails in March 2026 was approximately 686% higher than in January 2025. This increase is driven, in part, by several instances of platform abuse, including malware delivery and device fingerprinting, as we will discuss in the next sections.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/AI_flow_automation.jpg)

Figure 2. The prevalence of n8n webhook URLs in emails over the past few months.

## Abusing n8n for malware delivery

Because webhooks mask the source of the data they deliver, they can be used to serve payloads from untrusted sources while making them appear to originate from a trusted domain. Furthermore, since webhooks can dynamically serve different data streams based on triggering events — such as request header information — a phishing operator can tailor payloads based on the user-agent header.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/Figure_3.png)

Figure 3. Example of a malicious email that delivers malware to the victim’s device by abusing the n8n platform.

Talos observed a phishing campaign (shown in Figure 3) that used an n8n-hosted webhook link in emails that purported to be a shared Microsoft OneDrive folder. When clicked, the link opened a webpage in the targeted user’s browser containing a CAPTCHA.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/Figure_4.png)

Figure 4. HTML document delivered by the webhook presenting a CAPTCHA.

Once the CAPTCHA is completed, a download button appears, triggering a progress bar as the payload is downloaded from an external host. Because the entire process is encapsulated within the JavaScript of the HTML document, the download appears to the browser to have come from the n8n domain.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/Figure_5.png)

Figure 5. HTML and JavaScript payload of the webhook downloads an executable file from a malicious URL.

In this case, the payloa...