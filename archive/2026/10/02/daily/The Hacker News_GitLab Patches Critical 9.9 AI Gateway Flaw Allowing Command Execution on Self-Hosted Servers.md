---
title: GitLab Patches Critical 9.9 AI Gateway Flaw Allowing Command Execution on Self-Hosted Servers
url: https://thehackernews.com/2026/10/gitlab-patches-critical-self-hosted-ai.html
source: The Hacker News
date: 2026-10-02
fetch_date: 2026-10-03T07:13:21.277758
---

# GitLab Patches Critical 9.9 AI Gateway Flaw Allowing Command Execution on Self-Hosted Servers

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [GitLab Patches Critical 9.9 AI Gateway Flaw Allowing Command Execution on Self-Hosted Servers](https://thehackernews.com/2026/10/gitlab-patches-critical-self-hosted-ai.html)

**Swati Khandelwal**Oct 02, 2026Vulnerability / Application Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXhnbLdlAtkMBrrXYLiOxfbEdXI4PrEIq6dy3SL8Xa5SzPF6if9sf8GGu4PtkUTI3EYQHqBde4cDp4Y60OjgQBmqtZHTlL_gvgvlxNSeZ6nrRnriOmH3m23vq7f2bpylilVl39c_X-RNpvYQlRrC91gU_oHbk6e_ZbZ-7_fglpsQCFoLFp3sHkcn44960/s1700-nu-rw-lo-l85-e365/gitlab-rce.jpg)

A critical flaw in GitLab's AI Gateway could let a logged-in user with Duo Agent Platform access run commands on the gateway under certain conditions, GitLab [said in an advisory](https://docs.gitlab.com/releases/patches/other-patches/patch-release-gitlab-ai-gateway-19-4-1-released/).

The gateway is the service that connects a GitLab instance to AI models, and only organizations that host their own gateway need to act. The flaw is fixed in gateway versions 19.2.4, 19.3.2, and 19.4.1.

The flaw is tracked as [CVE-2026-90970](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/90xxx/CVE-2026-90970.json). GitLab disclosed it on October 2 and rated it critical, with a CVSS score of 9.9 out of 10.

GitLab runs AI Gateways for its customers and has already fixed them. Customers on GitLab.com, GitLab Dedicated, and self-managed instances that use a GitLab-hosted gateway do not need to act, the company said.

Self-managed customers can instead [host their own gateway](https://docs.gitlab.com/administration/gitlab_duo_self_hosted/), an option GitLab offers for keeping AI request and response data inside the customer's own environment. GitLab strongly recommends that those customers update immediately. It sent that guidance to customers with self-hosted gateways before it published the advisory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The advisory does not say whether the flaw has been used in attacks. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added an assessment to the CVE record on October 2 that lists exploitation as "none." CISA's other two values cover a public proof of concept and active exploitation.

### Affected and Fixed Versions

The versions below are AI Gateway versions. The gateway is installed as its own Docker image or Helm chart and has its own update steps.

| Gateway version in use | First fixed version |
| --- | --- |
| 18.1.6 or later, before 19.2.4 | 19.2.4 |
| 19.3, before 19.3.2 | 19.3.2 |
| 19.4, before 19.4.1 | 19.4.1 |

To [update a Docker deployment](https://docs.gitlab.com/install/install_ai_gateway/#upgrade-the-ai-gateway-docker-image), stop and remove the running container, then pull and run the new image tag, for example self-hosted-v19.4.1-ee. Helm deployments set the new tag in the chart's image setting.

No fixed version is listed below 19.2.4. That leaves every gateway release from 18.1.6 through the 19.1 line inside the affected range.

GitLab's install guide tells administrators to use the gateway image that matches their GitLab minor version. The advisory does not say whether a 19.2.4 gateway works with GitLab 19.1 or earlier, or whether fixes for the older lines are planned.

As of October 2, GitLab's [maintenance policy](https://docs.gitlab.com/policy/maintenance/#maintained-versions) listed 19.4, 19.3, and 19.2 as the GitLab releases that get security fixes. Those are the same three lines that got the gateway fix.

No workaround is listed for gateways that cannot be updated yet. The advisory also gives no way to check whether a gateway was attacked before it was updated.

### What Is Known About the Flaw

The flaw is in the prompt template of a custom flow, according to the advisory's title. A custom flow is an AI-powered workflow that users create on the Duo Agent Platform to automate multi-step tasks.

A logged-in user with Duo Agent Platform access could have used the flaw to "escape the prompt template sandbox via a specially crafted flow configuration," GitLab said. The escape could lead to arbitrary command execution on the gateway.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The conditions the attack needs are not described, and no user role is named beyond Duo Agent Platform access.

A self-hosted gateway holds signing keys for JSON Web Tokens (JWT), which GitLab's install guide says must be treated as sensitive credentials. It also connects to the GitLab instance and to the organization's AI model providers.

GitLab credited the HackerOne user invisiblemeerkat with reporting the flaw.

In February, GitLab [fixed another gateway flaw](https://docs.gitlab.com/releases/patches/other-patches/patch-release-gitlab-ai-gateway-18-8-1-released/), CVE-2026-1868, which it also rated 9.9. A logged-in user could reach that flaw through a crafted flow definition, and it could lead to denial of service or code execution on the gateway.

Both flaws are template engine weaknesses of the same class, CWE-1336. The new advisory does not mention the February flaw.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#lin...