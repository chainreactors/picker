---
title: Nearly 1 in 10 Exposed LiteLLM Gateways Accepted the Example "sk-1234" Admin Key
url: https://thehackernews.com/2026/09/nearly-1-in-10-exposed-litellm-gateways.html
source: The Hacker News
date: 2026-09-10
fetch_date: 2026-09-11T06:53:20.497968
---

# Nearly 1 in 10 Exposed LiteLLM Gateways Accepted the Example "sk-1234" Admin Key

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Nearly 1 in 10 Exposed LiteLLM Gateways Accepted the Example "sk-1234" Admin Key](https://thehackernews.com/2026/09/nearly-1-in-10-exposed-litellm-gateways.html)

**Swati Khandelwal**Sep 10, 2026Cloud Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfjbI1DXHJ4wQzSRFbddkmgQ9CTLSPPGP8fcQ6a37qbwKvgd4JxU51YhADR8S4IsWaiQ4fRApn-ih4m0AhsizM3wa6aJ3P8MlgBztNQm-oH4bE_TkPsmUZHhblcNMrQFxGdWnDHePCQDcSz-AJeWMoKH6YVcXXFCjK2ajZfbmObdeVkWmvv8O_fufqsl0/s1700-nu-rw-lo-l85-e365/litellm.jpg)

Nearly one in ten of the internet-facing LiteLLM servers that [Wiz Research](https://www.wiz.io/blog/off-guard-breaking-litellm-from-authentication-bypass-to-cloud-compromise) scanned in February accepted **sk-1234**, the example admin key in LiteLLM's own setup guide.

LiteLLM is an open-source AI gateway, the software a company puts between its applications and the model providers it pays for. That key is the gateway's administrator credential.

Anyone who holds it can read every model provider's API key stored on the server. In Wiz's tests, it also reached the cloud IAM credentials of the machine the gateway runs on.

Changing the key needs no upgrade, and it closes every path in Wiz's report that depends on holding it.

### Where the Number Comes From

Wiz ran one scan. It found 3,074 LiteLLM gateways on Shodan in February, and 294 of them accepted the key.

In 191 of those 294, no key was set at all, so they would have accepted anything. The rest had the setup guide's value left in place.

A second scan in August found more than 85,000 instances, but Wiz says most of them appear to be honeypots or test systems, so the two counts cannot be compared. There is no current figure.

As of September 9, LiteLLM's [setup guide](https://docs.litellm.ai/docs/proxy/docker_quick_start) still uses sk-1234, above a comment telling operators to replace it with a long random value before any real use.

### Why One Key Matters This Much

The master key does two jobs at once, and that is what makes a default value serious. It is the admin credential and the switch that enables authentication.

Before version 1.82.0-stable, a gateway that started without a master key granted every incoming request full admin rights.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

An admin on one of these servers has a lot in reach. The gateway can hold an API key for every provider it routes to, see every prompt and reply passing through, and connect to internal tools via the Model Context Protocol (MCP).

It also usually runs with the cloud permissions of the workload it is deployed in. Stolen provider keys alone let an attacker run model workloads on the victim's bill, an abuse known as LLMjacking.

### How the Key Reaches the Cloud Account

LiteLLM lets an administrator create a pass-through endpoint, a route that forwards requests to any URL the admin chooses.

The target URL is not checked against private address ranges, localhost, or cloud metadata addresses. An admin can therefore point a route at the instance metadata service and read back the IAM credentials it returns.

Switching to IMDSv2 does not stop this. LiteLLM [documents](https://docs.litellm.ai/docs/proxy/forward_client_headers) that any header sent with an x-pass- prefix is passed to the target with the prefix removed, and Wiz used that to send the headers IMDSv2 requires.

No source reports anyone doing this against a real deployment. It is a demonstration, and it needs admin access first.

Wiz says the feature is arguably working as intended, because LiteLLM's threat model treats administrators as trusted. It has no CVE and no fix.

The project says much the same about the way in. Its published [security policy](https://github.com/BerriAI/litellm/security) lists attacks that need a setup mistake, such as not setting a master key, as "explicitly not in scope" and not treated as vulnerabilities.

### The Guardrail Flaw, and a Disputed Severity

The one code execution flaw in Wiz's report is **CVE-2026-59821**, and the researchers and the maintainers describe it very differently.

Wiz calls it post-authentication code execution at root level, and shows a test returning uid=0(root) inside the gateway container. LiteLLM's [advisory](https://github.com/BerriAI/litellm/security/advisories/GHSA-72m8-9m7m-h278) for the same CVE rates it as Low (2.1 on the CVSS scale), describing it as a flaw that requires a high-privilege account.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpU2rukp1jjFWyu8vP5sXJ3jadCsUoPIiEf_MnD7vdAysJzDDn76uld5KDwZnbwwhEVTua9GS4Q4q8aYU91PfaH5VR527LhxL_DYXLfACQ7H6f48rPbFxvHkmRuWyXTODU4ZnfgYkYbUeTUlwiRyzSuG06Gr6Fw1Rk7Tkfj_NOSHz2iAmqRR4x2RXRKNk/s1700-nu-rw-lo-l85-e365/gaurd.png)

Both describe the same behavior. Before 1.82.0-stable, the endpoints that create and update custom code guardrails skipped the sandbox and pattern checks the test endpoint applied, so anyone who could reach them could submit Python that ran inside the container.

The advisory adds that a deployment with no master key treated callers as proxy administrators, which is what put those endpoints within reach.

Wiz's report states that after 1.82.0, an attacker with the default key could only run code within a sandbox. LiteLLM's own record does not support that for every release.

A separate [advisory](https://github.com/BerriAI/litellm/security/advisories/GHSA-wxxx-gvqv-xp7p) published in May, **CVE-2026-40217**, says that the sandbox could be escaped using bytecode techniques by running code in the proxy process, which the advisory notes runs as root in the default Docker image.

It covers versions from 1.81.8 up to, but not including, 1.83.10, and reaching the endpoint needs a proxy-admin credential. The master key is that credential.

Both flaws Wiz reported were fixed months before its September 9 report, in February and ...