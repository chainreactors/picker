---
title: You Don't Know Where Your Secrets Are
url: https://thehackernews.com/2023/01/you-dont-know-where-your-secrets-are.html
source: The Hacker News
date: 2023-02-01
fetch_date: 2025-10-04T05:26:03.355591
---

# You Don't Know Where Your Secrets Are

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [You Don't Know Where Your Secrets Are](https://thehackernews.com/2023/01/you-dont-know-where-your-secrets-are.html)

**Jan 31, 2023**The Hacker NewsSecret Management / DevSecOps

[![secrets management maturity model](data:image/png;base64... "secrets management maturity model")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhq0WHe2t0zN31XdVJPPAC2r29Ouw1_FeYjuYaDb1iUueVkOezh2eKzIsKEPtx8DGIBSQlhLgYvtSiEoAZ79TFzs2cWyadR2oQbsn4Qy3s59VlwZW1lNljV8YQvNy4gby1bxsBnvpJNmxiodaJIwft1moNqFB5tXmkMJJC2UNz1Pg2s37BDAu3gH_b0hg/s790-rw-e365/saas.png)

Do you know where your secrets are? If not, I can tell you: you are not alone.

Hundreds of CISOs, CSOs, and security leaders, whether from small or large companies, don't know either. No matter the organization's size, the certifications, tools, people, and processes: secrets are not visible in 99% of cases.

It might sound ridiculous at first: keeping secrets is an obvious first thought when thinking about security in the development lifecycle. Whether in the cloud or on-premise, you know that your secrets are safely stored behind hard gates that few people can access. It is not just a matter of common sense since it's also an essential compliance requirement for security audits and certifications.

Developers working in your organization are well-aware that secrets should be handled with special care. They have put in place specific tools and procedures to correctly create, communicate, and rotate human or machine credentials.

Still, do you know where your secrets are?

Secrets sprawl everywhere in your systems, and faster than most realize. Secrets are copied and pasted into configuration files, scripts, source code, or private messages without much thought. Think about it: a developer hard-codes an API key to test a program quickly and accidentally commits and pushes their work on a remote repository. Are you confident that the incident can be detected in a timely manner?

Insufficient audit and remediation capabilities are some of the reasons why secrets management is hard. They are also the least addressed by security frameworks. Yet these grey areas—where unseen vulnerabilities remain hidden for a long time—are blatant holes in your defense layers.

Recognizing this gap, we developed a self-assessment tool to evaluate the size of this unknown. To take stock of your *real* security posture regarding secrets in your organization, take five minutes to answer [the eight questions](https://www.gitguardian.com/secrets-management-maturity-questionnaire) (it's completely anonymous).

So, how much do you *not* know about your secrets?

## Secrets Management Maturity Model

Sound secrets management is a crucial defensive tactic that requires some thought to build a comprehensive security posture. We built a framework (you can find the white paper [here](https://www.gitguardian.com/files/secrets-management-maturity-model)) to help security leaders make sense of their actual posture and adopt more mature enterprise secrets management practices in three phases:

1. Assessing secrets leakage risks
2. Establishing modern secrets management workflows
3. Creating a roadmap to improvement in fragile areas

The fundamental point addressed by this model is that secrets management goes well beyond how the organization stores and distributes secrets. It is a program that not needs to align people, tools, and processes, but also to account for human error. Errors are *not* evitable! Their consequences are. That's why detection and remediation tools and policies, along with secrets storage and distribution, form the pillars of our maturity model.

The secrets management maturity model considers four attack surfaces of the DevOps lifecycle:

* Developer environments
* Source code repositories
* CI/CD pipelines & artifacts
* Runtime environments

We then built a maturity ramp-up over five levels, going from 0 (Uninitiated) to 4 (Expert). Going 0 to 1 is mostly about assessing the risks posed by insecure software development practices, and starting auditing digital assets for hardcoded credentials. At the intermediate level (level 2), secrets scanning is more systematic, and secrets are cautiously shared across the DevOps lifecycle. Levels 3 (Advanced) and 4 (Expert) are focused on risk mitigation with clearer policies, better controls, and increased shared responsibility for remediating incidents.

Another core consideration for this framework is that making it hard to use secrets in a DevOps context will inevitably lead to the bypassing of the protective layers in place. As with everything else in security, the answers lay between protection and flexibility. This is why the use of a vault/secrets manager starts at the intermediate level only. The idea is that the use of a secrets manager should not be seen as a stand-alone solution but as an additional layer of defense. To be effective, it requires other processes, like continuous scanning of pull requests, to be mature enough.

Here are some questions that this model should raise in order to help you evaluate your maturity: how frequently are your production secrets rotated? How easy is it to rotate secrets? How are secrets distributed at the development, integration, and production phase? What measures are put in place to prevent the unsafe dissemination of credentials on local machines? Do CI/CD pipelines' credentials adhere to the least privileges principle? What are the procedures in place for when (not if) secrets are leaked?

Reviewing your secrets management posture should be top of mind in 2023. First, everyone working with source code has to handle secrets, if not daily, at least once in a while. Secrets are no longer the prerogative of security or DevOps engineers. They are required by more and more people, from ML engineers, data scientists, product, ops, and even more. Second, if you don't find where your secrets are, hackers will.

## Hackers will find your secrets

The risks posed to organizations failing to adopt mature secrets mana...