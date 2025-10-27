---
title: Auditing GitLab: Public Gitlab Projects on Internal Networks
url: https://www.blackhillsinfosec.com/auditing-gitlab/
source: Black Hills Information Security
date: 2024-07-19
fetch_date: 2025-10-06T17:41:49.499813
---

# Auditing GitLab: Public Gitlab Projects on Internal Networks

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
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
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

18
Jul
2024

[External/Internal](https://www.blackhillsinfosec.com/category/red-team/external/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [InfoSec 201](https://www.blackhillsinfosec.com/category/infosec-201/)
[audit](https://www.blackhillsinfosec.com/tag/audit/), [GitLab](https://www.blackhillsinfosec.com/tag/gitlab/), [gitleaks](https://www.blackhillsinfosec.com/tag/gitleaks/), [leaks](https://www.blackhillsinfosec.com/tag/leaks/), [secrets](https://www.blackhillsinfosec.com/tag/secrets/)

# [Auditing GitLab: Public Gitlab Projects on Internal Networks](https://www.blackhillsinfosec.com/auditing-gitlab/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/07/PMiller-150x150.png)

| [Phil Miller](https://www.blackhillsinfosec.com/team/phil-miller/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/07/BLOG_chalkboard_00679-1.jpg)

A great place that can sometimes be overlooked on an internal penetration test are the secrets hidden in plain sight. That is, a place where no authentication is required in many circumstances throughout internal networks. I’m talking about source code management platforms, specifically Gitlab. Other self-hosted platforms are likely also susceptible to this unauthenticated technique as well, but we’ll be focusing on GitLab.

**A sequence of words that I’ve heard:**

*Mr. Senior Developer – “If an attacker already has access to our internal network, we’ve got bigger problems.”*

The biggest problem is this kind of thinking! Yes, a hacker inside your internal network is a problem that requires immediate attention, but the defensive measures you implement as an organization leading up to this kind of event are what really counts. It is a common misconception that once an adversary has gained initial access to an organization’s network, that it is already game over. Verily, I tell you, good neighbor, that this is not the case! There are many things that you can do to defend against attackers inside the internal network. For instance, security landmines at every turn via canary tokens and other awesome things. But in this blog post, we’ll be talking about attacking and defending (but mostly attacking) self-hosted GitLab instances.

I’ve come across internal GitLab instances in organizations’ internal networks countless times and many of them have one thing in common, many of their projects are set to “public.” One might think or blurt out, “Well, first you would need a valid account to log in to GitLab to access these projects,” and to that I say, with great vigor, “False!”

In GitLab, when a project scope is set to “public,” it is still accessible to anyone with network access. Better yet, it is discoverable via the GitLab projects API at the URL, https://<gitlab.example.com>/api/v4/projects.

Spoiler alert: The process of finding all public GitLab projects and downloading everything can be quickly automated with no authentication. On an amusing side-note anecdote, Nessus won’t tell you this, but your organization’s crown jewels are totally exposed! That’s because this is a feature, not a bug. But that’s not to say that Nessus isn’t totally barren of fruits altogether. Nessus will still identify all the GitLab instances for you, that is, if you’re using Nessus. Whether you’re using Nessus or not, we can still easily identify all the GitLab instances on an internal network using Nuclei, more specifically, a Nuclei GitLab workflow:

```
nuclei -l in-scope-cidrs-ips-hosts-urls-whatever.txt \

-w ~/nuclei-templates/workflows/gitlab-workflow.yaml \

-o gitlab-nuclei-workflow.log | tee gitlab-nuclei-workflow-color.log
```

The screenshot below shows a portion of the output from the command above.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/07/AuGit_01.png)

**Nuclei GitLab Workflow Partial Output (Redacted)**

There are many code-secret scanning tools such as Trufflehog, Gitleaks, NoseyParker, and others. We’ll be utilizing Gitleaks for this blog post, but, as an exercise, I encourage you to use all three and compare your results. One downside of many of these tools at the time of writing is the reliance on authentication for mass automated scanning, but this can be done from an unauthenticated context too (when the GitLab public repos api is accessible). If you have come across GitLab instances on internal penetration tests but weren’t sure how to automate and achieve that sweet juicy pwnage, then this blog is for you.

As Pastor Manul Laphroaig would say, PoC || GTFO!

### **Plundering GitLab**

Forgive me, neighbors, if this feature already exists in ...