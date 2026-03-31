---
title: The State of Secrets Sprawl 2026: 9 Takeaways for CISOs
url: https://thehackernews.com/2026/03/the-state-of-secrets-sprawl-2026-9.html
source: The Hacker News
date: 2026-03-30
fetch_date: 2026-03-31T04:37:37.389951
---

# The State of Secrets Sprawl 2026: 9 Takeaways for CISOs

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [The State of Secrets Sprawl 2026: 9 Takeaways for CISOs](https://thehackernews.com/2026/03/the-state-of-secrets-sprawl-2026-9.html)

**The Hacker News**Mar 30, 2026DevOps / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4tVpFBDvdU-vz8vM1T6SJZwd3AiySFqEyonUutxGPNimXEqTVOKN-pCI_lF5Ti2GngFUPtEphVI4Qep03CBciF7NhaWEIKYdDfkVY-VleTTcqYJvcMTKrd-EJ4kh2zLk3cY7pqqxI7bfEghuxGAV7lwUPjTD6nTa5dKj5e8_RJD9UjHn12015puG8P4o/s1700-e365/key.gif)

*Secrets sprawl isn't slowing down: in 2025, it accelerated faster than most security teams anticipated. [GitGuardian's State of Secrets Sprawl 2026 report](https://www.gitguardian.com/files/the-state-of-secrets-sprawl-report-2026) analyzed billions of commits across public GitHub and uncovered 29 million new hardcoded secrets in 2025 alone, a 34% increase year over year and the largest single-year jump ever recorded.*

This year's findings reveal three core trends: AI has fundamentally reshaped how and where credentials leak, internal systems are far more exposed than most organizations realize, and remediation continues to be the industry's Achilles heel.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7TTJOaUu01nuUn-1nszxtRy-gywqOqWfSYlXnAu8berV_SYtUseBWiiWKSMnbsdjXpISdHYZNiTFw6a-R_B8SMxUJ-bQUNThd40hsiWNwfHFylXFv4JQkIhmKhQN6BDeu0JQxe0w5ZUfKdM7xcm0mlupwveG97fltpFfq3efY_3dWe3fMId62ca9u8cg/s1700-e365/1.png)

**Here are nine strategic takeaways that matter.**

## 1. Secrets are growing faster than the developer population

Since 2021, leaked secrets have grown 152%, while GitHub's public developer base expanded 98%. More developers and more AI-assisted code generation mean more credentials in circulation, and detection alone can't keep pace.

## 2. AI services drove 81% more leaks year over year

GitGuardian detected 1,275,105 leaked secrets tied to AI services in 2025, up 81% from 2024. Eight of the ten fastest-growing categories of leaked secrets were AI-related. This isn't just about OpenAI or Anthropic keys. The real explosion is happening in LLM infrastructure: retrieval APIs like Brave Search (+1,255%), orchestration tools like Firecrawl (+796%), and managed backends like Supabase (+992%). Every new AI integration introduces another machine identity, and each one expands the attack surface. Deploying AI safely requires a proper secrets security strategy.

## 3. Internal repositories are 6x more likely to leak than public ones

While public GitHub gets the attention, internal repositories are where the highest-value credentials live. GitGuardian's research found that 32.2% of internal repos contain at least one hardcoded secret, compared to just 5.6% of public repos. These aren't test keys. They're CI/CD tokens, cloud access credentials, and database passwords, the exact assets attackers target once they gain a foothold. Security through obscurity has failed. Treat internal repos as first-class leak sources.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_OvmKrTLLUqQ5pVs_ovpMia3_NUkJKgy15k4f_AB6ByXoJrGAC252W8_ysTL6UoW9UcdfK-HH8tSG-PgsGNfgKMXeq4e7X9d-6trdDoit5WnaVWIvXXzy6qUcDG6LtssVrfgnF4ldzV_DGdl5lWKbrC5gtJDiku7j9SDyphUh56zf5I2O9TWm157Od1Y/s1700-e365/2.png)

## 4. 28% of leaks happen entirely outside code

Secrets don't only live in repositories. GitGuardian found that 28% of incidents in 2025 originated entirely outside source code, in Slack, Jira, Confluence, and similar collaboration tools. These leaks are more dangerous: **56.7% of secrets found only in collaboration tools were rated critical**, compared to 43.7% for code-only incidents. Teams share credentials during incident response, troubleshooting, and onboarding. If you're only scanning code, you're missing a quarter of your exposure. And the credentials leaking in collaboration tools are usually more critical and severe.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0lgO08_CQqOlPFjzen2FSjKz5lkjCQ6napoKymbcFUzst92AuzjmqfzILEJsoCjk4jM-o55uxoVqIIib2zGdtjbp9UteR4NMMs9_Lj-AC7j8_N9ZtHaMXyUZAwXUPr_BVnTHSZP7g6HBe3FOkNw_YNJi01_LS_rxXLUADiBn_JLeVJeLoffFcyf0-xAk/s1700-e365/3.png)

## 5. Self-hosted GitLab and Docker registries expose secrets at 3-4x the rate of public GitHub

GitGuardian discovered thousands of unintentionally exposed self-hosted GitLab instances and Docker registries in 2025. Scanning these systems revealed 80,000 credentials, with 10,000 still valid. Secrets in Docker images were particularly troubling: 18% of scanned Docker images contained secrets, and 15% of those were valid, compared to 12% of GitLab repositories with a 12% validity rate. Docker secrets are also more production-adjacent. **The perimeter between private and public is porous.**

## 6. 64% of secrets leaked in 2022 remain valid today

Detection is not remediation. GitGuardian retested secrets confirmed as valid in 2022 and found that 64% are still exploitable four years later. This is not a rounding error. It's proof that rotation and revocation are not routine, owned, or automated in most organizations. Credentials embedded across build systems, CI variables, container images, and vendor integrations are hard to replace without breaking production. For many teams, the safest short-term choice is to do nothing, leaving attackers with durable access paths.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhP7n8Bj_V61Ktsts8Km8mGFIxpGjyF5Pe1jhNy6BsZ_R3BtTNOvmjXiiUeC0AOkkej1zjMd5lbeqkYvv-YyCr-OrI1ZYl0c15VyCiMnQG1JEc0EzX63XBjXP7Kq8q_sZu4S-Et4DazMC13OxWGE5mGAKdF9wE6oySm1QvCeIc2kSL6sXlgN1_J3IFC8ps/s1700-e365/4.png)

## 7. Developer endpoints are the new credential aggregation layer

The [Shai-Hulud 2 supply chain attack](https://blog.gitguardian.com/shai-hulud-2/) gave researchers rare visibility into what secrets actually look like on [compromised developer machines](https:...