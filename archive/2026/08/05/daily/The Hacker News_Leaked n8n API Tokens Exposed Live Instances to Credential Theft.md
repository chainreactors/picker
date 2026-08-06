---
title: Leaked n8n API Tokens Exposed Live Instances to Credential Theft
url: https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html
source: The Hacker News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:52.627898
---

# Leaked n8n API Tokens Exposed Live Instances to Credential Theft

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

![cybersecurity](data:image/svg+xml;base64...)

# [Leaked n8n API Tokens Exposed Live Instances to Credential Theft](https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html)

**The Hacker News**Aug 05, 2026AI Security / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhx1pOdsqya8FoeUfRoysn2429wQSGELUYOuuaDRT5-pJMERQc7DY042ndusTV0UriGHrR98oyPe_HnR845R1hxSxKBTvYGTilYobQhIIXOCEc08FiKbhDluP0UoR6g3sw8QK-X1aPEJDKe-EZbDNOtlXR6ltGBvxsqfB_bo-jO4t63OvT7_C1mD7Bf4rM/s1700-e365/n8n-git.gif)

GitGuardian researchers found 321 n8n instances accepting API tokens exposed in public GitHub commits and demonstrated four ways attackers could use them to access sensitive data and downstream credentials without exploiting a software vulnerability.

We scanned public GitHub commits for exposed n8n API tokens and identified 4,576 unique credentials associated with 1,255 hostnames. Of the 896 instances reachable at the time of testing, 321 accepted at least one leaked token.

That means leaked credentials provided authenticated access to 36% of the reachable instances we tested, or roughly 26% of all hostnames identified in the commits.

The implications extend well beyond n8n. Organizations use the automation platform to connect databases, source code repositories, cloud environments, artificial intelligence services, customer support platforms, and other internal systems. A sufficiently privileged n8n token can expose workflow definitions and execution data, allow attackers to use stored credentials, and, in some configurations, enable them to extract the underlying credential values.

To measure the potential blast radius, we reproduced four practical attack techniques in a controlled n8n environment. Each required only documented REST API functionality and standard HTTP requests. No CVE exploitation or specialized tooling was necessary.

## Why n8n is a high-value target

n8n is an open-source, low-code workflow automation platform with AI agent support and hundreds of built-in integrations. Organizations use it to connect internal tools, automate pipelines, implement business logic, and orchestrate API integrations across their technology stacks.

The platform can be self-hosted or deployed through `n8n.cloud`, and its [open-source repository](https://github.com/n8n-io/n8n) has attracted nearly 200,000 GitHub stars.

An n8n instance runs workflows composed of nodes. Some nodes trigger workflows on a schedule or through webhooks, while others transform data, execute code, or connect to external services using stored credentials such as API keys, tokens, and database passwords.

Those credentials are encrypted at rest using a master secret called `N8N_ENCRYPTION_KEY`. But n8n still needs to decrypt and use them whenever a workflow runs. An attacker with sufficient API privileges may therefore be able to reference those credentials in new workflows and make the instance use them on the attacker's behalf.

With more than 100,000 instances visible through [Shodan](https://www.shodan.io/) and more than 50 security advisories published since January 2026, n8n has attracted the same attention as other high-value integration platforms.

As of March 31, 2026, 58% of the instances we scanned were running a version affected by at least one known security advisory. Several recent CVEs allowed attackers to escape execution sandboxes and gain arbitrary read or write access to the host filesystem.

`CVE-2025-68613`, an expression injection vulnerability with a CVSS score of 9.9, was added to the U.S. Cybersecurity and Infrastructure Security Agency's Known Exploited Vulnerabilities catalog on March 11, 2026, confirming exploitation in the wild.

Leaked API tokens create a separate risk. An attacker does not necessarily need to exploit an n8n vulnerability if a valid credential already provides authenticated access to the instance.

## We found 321 instances accepting leaked tokens

GitGuardian Public Monitoring scans public sources for exposed credentials. For this research, we collected every n8n API token it had identified in public GitHub commits since April 2025.

Our pipeline extracted the n8n hostname committed alongside each token, sent a read-only validation request to the associated instance, and recorded the response.

The scan produced:

|  |  |
| --- | --- |
| **Stage** | **Count** |
| Unique API tokens | 4,576 |
| GitHub commits containing tokens | 5,469 |
| Unique hostnames extracted | 1,255 |
| Publicly reachable instances | 896 |
| Instances accepting a leaked token | 321 |

The 321 confirmed instances represent approximately 36% of the 896 reachable instances and 26% of all 1,255 hostnames identified in the commits.

We ran the same process against n8n Model Context Protocol API keys found in the same commit set. MCP tokens allow AI assistants to call n8n workflows through the Model Context Protocol, making them a newer exposure surface than the REST API.

Of 372 MCP tokens identified, seven were still valid at the time of testing, or roughly 2%.

## Why leaked n8n tokens can remain valid

An n8n API key is a signed JSON Web Token with an `"aud": "public-api"` audience claim. A decoded token looks like this:

```
{
  "sub": "efdf9cca-049a-46aa-afdc-172f0824f6cb",
  "iss": "n8n",
  "aud": "public-api",
  "jti": "aac8a7a8-c8c4-4855-8e8b-2806e90b16e1",
  "iat": 1781551662
}
```

The token records its issuance time in the `iat` claim. Older n8n API keys frequently contain no `exp` claim defining when they expire.

n8n introduced a 30-day default expiration in version `1.78.0` in February 2025, but many of the tokens found during the research had been generated without an expiration date. A key committed to GitHub months earlier could therefore remain usable until someone explicitly deleted or revoked it.

In practice, n8n API keys behave differently from self-contained JWTs that can be validated using their signatures alone. The key must also still exist in the n8n database. A token exposed in GitHub remains dangerous as long as the instance continues to recognize it.

Testing a candidate token requires one read-only request with the key passed through the `X-N8N-API-KEY` header:

```
curl -s -o /dev/null -w "%{http_code}" \
-H "X-N8N-API-KEY: <token>" \
https://n8n.example.com/api/v1/wo...