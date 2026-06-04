---
title: Auditing GitLab: The CI/CD Kill Chain
url: https://www.blackhillsinfosec.com/auditing-gitlab-the-ci-cd-kill-chain/
source: Black Hills Information Security, Inc.
date: 2026-06-03
fetch_date: 2026-06-04T06:30:46.094698
---

# Auditing GitLab: The CI/CD Kill Chain

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-consultants/)
  + [Admin Team](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [Active SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [Antisyphon Training](https://www.blackhillsinfosec.com/about/antisyphon/)
  + [BHIS Tribe of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://bhispodcasts.transistor.fm/)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

3
Jun
2026

[Blue Team Tools](https://www.blackhillsinfosec.com/category/blue-team/tool-blue-team/), [External/Internal](https://www.blackhillsinfosec.com/category/red-team/external/), [InfoSec 301](https://www.blackhillsinfosec.com/category/infosec-301/), [Recon](https://www.blackhillsinfosec.com/category/red-team/recon/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[attacking](https://www.blackhillsinfosec.com/tag/attacking/), [cicd](https://www.blackhillsinfosec.com/tag/cicd/), [Defending](https://www.blackhillsinfosec.com/tag/defending/), [devops](https://www.blackhillsinfosec.com/tag/devops/), [GitLab](https://www.blackhillsinfosec.com/tag/gitlab/), [gogatoz](https://www.blackhillsinfosec.com/tag/gogatoz/), [Phil Miller](https://www.blackhillsinfosec.com/tag/phil-miller/)

# [Auditing GitLab: The CI/CD Kill Chain](https://www.blackhillsinfosec.com/auditing-gitlab-the-ci-cd-kill-chain/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/06/PMiller-1-150x150.png)

| [Phil Miller](https://www.blackhillsinfosec.com/team/phil-miller/)

Phil has been a BHIS Security Consultant for 4 years. He currently serves in a development-focused role and enjoys building offensive security tools. Outside of work, Phil enjoys the arts (drumming & music, drawing & painting), as well as sports (golfing, bowling, and basketball).

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/06/cicd_header-1.png)

In [Part I](https://www.blackhillsinfosec.com/auditing-gitlab/) of this series, we talked about plundering self-hosted GitLab instances on internal networks — cloning public repos, running **Gitleaks**, and combining it all into a nice spreadsheet of secrets. We used Python scripts and a Go program, duct-taped together with the enthusiasm of a developer who just learned what **subprocess.call** does. At the end of that post, I mentioned that all that logic really *should* be combined into a single tool.

Well, good neighbors, I took my own advice.

Welcome to GoGatoZ — a purpose-built Go tool for GitLab CI/CD security auditing that can perform and automate the entire CI/CD kill chain along with everything those one-off scripts did and then some. In this blog post, we’re going to do something a little ambitious: we’re going to point GoGatoZ at **gitlab.com** and run three large-scale scans: first a broad sweep using generic DevOps keywords, then a targeted scan of public projects associated with Fortune 500 companies from a public 2023 dataset on GitHub, and finally an industry-targeted scan of law firms, financial services, logistics, and trucking companies. We’ll also walk through how we built a false positive analysis workflow to separate real findings from noise. Across all three scans, we analyzed 3,757 public projects and found 7,331 security findings, including 1,580 HIGH severity issues.

But first, we must give credit where credit is due. I’d like to take a moment to shout out these amazing presentations on CI/CD hacking GitHub Actions. Without these talks and tools, this blog/tool would not have been possible. *GoGatoZ was built on the shoulders of giants*:

* RomHack 2024 – Adnan Khan – [The dark side of GitHub actions](https://www.youtube.com/watch?v=76NEylOsOS0)
* DEF CON 32 – Adnan Khan, John Stawinski – [Grand Theft Actions Abusing Self Hosted GitHub Runners](https://www.youtube.com/watch?v=5P7KatZBr_I)

**A sequence of words that I’ve heard:**

> *Our CI/CD pipelines are fine. Nobody is looking at those YAML files.*
>
> *– Mr. Senior DevOps Engineer*

Verily, I tell you good neighbor, that we are *absolutely* looking at those YAML files.

## Why CI/CD Pipelines?

In Part I, we focused on secrets buried in source code (hardcoded credentials, API keys, the usual suspects). But here’s the thing: the **.gitlab-ci.yml** file is where a lot of the *“real”* magic happens. It’s the blueprint for your entire build, test, and deployment pipeline. And if it’s misconfigured, an attacker doesn’t need your source code secrets. They can inject commands, poison artifacts, hijack runners, maintain persistent access, and exfiltrate CI variables that never touch a single line of application code.

**Spoiler alert:** A shocking number of public GitLab projects have CI/CD misconfigurations that are totally exploitable.

Supply chain attacks are all the rage these days and I have debated quite a bit on whether I should release this tool, as it can be abused in the wrong hands… but so can pretty much everything else. Let’s just hope I don’t get Nightmare Eclipsed.

## The Tool: GoGatoZ

[GoGatoZ](https://githu...