---
title: Cybersecurity Blind Spots in IaC and PaC Tools Expose Cloud Platforms to New Attacks
url: https://thehackernews.com/2024/11/cybersecurity-flaws-in-iac-and-pac.html
source: The Hacker News
date: 2024-11-26
fetch_date: 2025-10-06T19:26:25.997553
---

# Cybersecurity Blind Spots in IaC and PaC Tools Expose Cloud Platforms to New Attacks

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

# [Cybersecurity Blind Spots in IaC and PaC Tools Expose Cloud Platforms to New Attacks](https://thehackernews.com/2024/11/cybersecurity-flaws-in-iac-and-pac.html)

**Nov 25, 2024**Ravie LakshmananCloud Security / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiB0CKqrj30wvmxyRVQB3UToSBNmrOHq5d4jWBQtrCvTRFIisnlCP70IKlwH2zBFM3B8q2vv0G9Kn4P3SklCSQYfvANL5XVpivD6Atyf-HTeWbc_eFK1NACkcF93cs0-uUbxHPz-dk7s8lMDepcB1j7qu0UfSpAWssArQPXjEDeyIwOZkY1recelg3kwAig/s790-rw-e365/cloud.gif)

Cybersecurity researchers have disclosed two new attack techniques against infrastructure-as-code (IaC) and policy-as-code (PaC) tools like HashiCorp's Terraform and Styra's Open Policy Agent (OPA) that leverage dedicated, domain-specific languages (DSLs) to breach cloud platforms and exfiltrate data.

"Since these are hardened languages with limited capabilities, they're supposed to be more secure than standard programming languages – and indeed they are," Tenable senior security researcher Shelly Raban [said](https://www.tenable.com/blog/the-dark-side-of-domain-specific-languages-uncovering-new-attack-techniques-in-opa-and) in a technical report published last week. "However, more secure does not mean bulletproof."

OPA is a popular, open-source policy engine that allows organizations to enforce policies across cloud-native environments, such as microservices, CI/CD pipelines, and Kubernetes. Policies are defined using a native query language called [Rego](https://www.openpolicyagent.org/docs/latest/policy-language/) which are then [evaluated](https://www.wiz.io/academy/open-policy-agent-opa) by OPA to return a decision.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack method devised by Tenable targets the supply chain, wherein an attacker gains unauthorized access through a compromised access key to insert a malicious Rego policy to an OPA server, which is subsequently used during the policy decision phase to allow malicious actions like credential exfiltration using a built-in function known as "[http.send](https://www.openpolicyagent.org/docs/latest/policy-reference/#http)."

Even in instances where an OPA deployment restricts the use of http.send, the cybersecurity firm found that it's possible to utilize another function named "[net.lookup\_ip\_addr](https://www.openpolicyagent.org/docs/latest/policy-reference/#builtin-net-netlookup_ip_addr)" to smuggle the data using DNS lookups via a technique referred to as DNS tunneling.

"So, the net.lookup\_ip\_addr function is another function you might consider restricting or at least looking out for in policies, since it also introduces the risk of data exfiltration from your OPA deployment," Raban said.

Terraform, similar to OPA, [aims](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code) to [simplify](https://www.wiz.io/academy/terraform-security-best-practices) the process of setting up, deploying, and managing cloud resources through code-based definitions. These configurations can be set up using another declarative DSL called HashiCorp Configuration Language ([HCL](https://developer.hashicorp.com/terraform/language/syntax/configuration)).

An attacker could target the open-source IaC platform by taking advantage of its "[terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan)" command, which are typically triggered as part of GitHub "[pull\_request](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#pull_request)" workflows, to execute unreviewed changes containing a malicious data source during the CI/CD process.

"Data sources run during 'terraform plan,' which significantly lowers the entry point for attackers," Tenable noted. "This poses a risk, as an external attacker in a public repository or a malicious insider (or an external attacker with a foothold) in a private repository could exploit a pull request for their malicious objectives."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

These data sources, in turn, could be a rogue external data source, a Terraform module shared via public or private registries, or a [DNS data source](https://registry.terraform.io/providers/hashicorp/dns/latest/docs), necessitating that only third-party components from trusted sources be used. Some of the other recommendations to mitigate such risks include -

* Implement a granular role-based access control (RBAC) and follow the principle of least privilege
* Set up application-level and cloud-level logging for monitoring and analysis
* Limit the network and data access of the applications and the underlying machines
* Prevent automatic execution of unreviewed and potentially malicious code in CI/CD pipelines

Furthermore, organizations can use [IaC scanning tools and solutions](https://www.wiz.io/academy/iac-scanning) like Terrascan and Checkov to preemptively identify misconfigurations and compliance issues prior to deployment.

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
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[CI/CD Pipeline](https://thehackernews.com/search/lab...