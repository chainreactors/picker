---
title: Alleged TeamPCP Hackers Charged in Australia Over Major Supply Chain Attacks
url: https://thehackernews.com/2026/08/alleged-teampcp-hackers-charged-in.html
source: The Hacker News
date: 2026-08-27
fetch_date: 2026-08-28T13:37:58.973936
---

# Alleged TeamPCP Hackers Charged in Australia Over Major Supply Chain Attacks

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Alleged TeamPCP Hackers Charged in Australia Over Major Supply Chain Attacks](https://thehackernews.com/2026/08/alleged-teampcp-hackers-charged-in.html)

**Swati Khandelwal**Aug 27, 2026Cybercrime / Supply Chain Attacks

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6Ze_JyLo4PQxJMbwu8Mn_aCoLWiD2dgbGmzOPcYcdrN8wunKZu2SZll2fiHcAOFoA0h9N5TYPOY_IvrPpGqTpnXdyd5bXHRtyHqb3t3junXDMotOAD43Y0jzA9wkCSjoOIo1knFjtTVRAeOSjpHqLzfMGceCcHYGb6cE1HD-Y5mtY9hyphenhyphenHT9PeUk3TV68/s1700-e365/TeamPCP-arrest.gif)

The Australian Federal Police (AFP) has charged two Western Australian men with a combined total of 14 offences over their alleged role in **TeamPCP**, the cybercrime group behind the March 2026 compromise of the open-source security scanners Trivy and Checkmarx KICS and the AI gateway LiteLLM.

**Louis Michael Gaebler**, 23, and **Ruben Ian Thomson**, 21, appeared in Perth Magistrates Court on August 27, 2026, a day after the AFP and the Western Australia Police Force (WAPF) executed search warrants at properties in Cottesloe, Hamilton Hill, and Mandurah and seized electronic devices for forensic analysis.

Police allege the two men were principal participants in the syndicate and received payments in cryptocurrency, the value of which is still under investigation.

The Federal Bureau of Investigation (FBI) said in a July 2 advisory that organizations impacted by the campaign should treat exfiltrated data and credentials as a persistent risk, since affiliated threat actors are "likely to weaponize them long after the initial compromise." It advised rotating all continuous integration and continuous delivery (CI/CD) secrets, publishing tokens, and cloud credentials accessible during the exposure windows.

FBI Cyber Division Assistant Director Brett E. Leatherman said in [a joint media release](https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global) that the two men are allegedly members of TeamPCP, whose malicious code "potentially compromised more than a thousand organizations worldwide."

The Cottesloe man, 21, was charged with one count of possessing data with intent to commit a computer offence, four counts of unauthorized modification of data with intent to commit a serious offence, one count of supplying data with intent to commit a computer offence, one count of failing to comply with a section 3LA order, and one count of dealing with proceeds of crime worth $100,000 or more.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The Mandurah man, 23, was charged with one count of possessing data with intent, four counts of unauthorized modification of data with intent to commit a serious offence, and one count of supplying data with intent to commit a computer offence.

The section 3LA count, brought under the Crimes Act 1914 (Cth), carries a maximum penalty of 10 years' imprisonment, and the proceeds of crime count carries a maximum of 20 years.

None of the 14 charges names a specific compromised project.

The syndicate worked by stealing publishing credentials from trusted open-source projects and pushing poisoned versions out through the projects' own release channels. The campaign spanned five distribution ecosystems, GitHub Actions, Docker Hub, npm, PyPI, and OpenVSX.

The compromise of one project supplied the credentials used against the next. Credentials taken during [the Trivy scanner compromise](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html) were turned on [the Checkmarx KICS actions](https://thehackernews.com/2026/03/teampcp-hacks-checkmarx-github-actions.html) days later.

LiteLLM's own build pipeline installed Trivy without pinning it to a verified version. The poisoned scanner then took the project's publishing token.

The actor used that token to push [the backdoored LiteLLM releases](https://thehackernews.com/2026/03/teampcp-backdoors-litellm-versions.html) in late March. LiteLLM routes requests across large language model (LLM) providers, and sits where an organization's provider keys are consolidated.

The AFP said the malicious code potentially compromised more than 1,000 organizations globally, enabled the theft of more than 500,000 credentials, and led to the exfiltration of at least 300 gigabytes of data. Unit 42 published the same two figures in March, hedged as what the actor "may have exfiltrated."

CloudSEK and Hudson Rock published [the August exposure figures](https://thehackernews.com/2026/08/malicious-litellm-releases-tied-to.html) for the same campaign, with CloudSEK putting reconstructed exposure at more than 2,500 organizations and roughly 434,000 CI/CD pipelines, and Hudson Rock attributing 118,829 CI runner dumps to 2,488 corporate domains from a 153GB archive of the attackers' own exfiltrated data.

CloudSEK said credential theft is not proof that a company was successfully compromised, and the confirmed victim count is the 16 organizations TeamPCP published on its leak site as of late March.

StepSecurity said its analysis of the CloudSEK dataset found GitLab led the affected platforms with 1,064 organizations, ahead of GitHub Actions on 618, Azure DevOps on 233, Jenkins on 105, Bitbucket Pipelines on 94, and CircleCI on 15.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The Hacker News confirmed via PyPI on August 27 that the two malicious LiteLLM builds no longer appear in the package's release history, and that both still return HTTP 200 from PyPI's content delivery network at their direct package URLs five months after removal from the index.

TeamPCP-linked infrastructure has been [traced back to 2020](https://thehackernews.com/2026/08/teampcp-linked-to-redis-attacks-dating.html), Oligo Security said in an August 5 report, tying the group to activity previously tracked as TA-NATALSTATUS and IronErn through overlapping domains, malware deployment pa...