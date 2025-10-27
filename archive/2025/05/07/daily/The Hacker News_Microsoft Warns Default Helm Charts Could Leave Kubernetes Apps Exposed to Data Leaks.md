---
title: Microsoft Warns Default Helm Charts Could Leave Kubernetes Apps Exposed to Data Leaks
url: https://thehackernews.com/2025/05/microsoft-warns-default-helm-charts-for.html
source: The Hacker News
date: 2025-05-07
fetch_date: 2025-10-06T22:30:56.745725
---

# Microsoft Warns Default Helm Charts Could Leave Kubernetes Apps Exposed to Data Leaks

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

# [Microsoft Warns Default Helm Charts Could Leave Kubernetes Apps Exposed to Data Leaks](https://thehackernews.com/2025/05/microsoft-warns-default-helm-charts-for.html)

**May 06, 2025**Ravie LakshmananCloud Security / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifHQNQ4yEVwpcKrysUFr1YJLED2EbDxBZftaCcFKDEWNEEsMkHdAm1TLSVCOc2ihRjP9Vl49i5fDFX1bQzw-Yom3UPoDmsuC3P2T5xb3Kbndr-R-F-oZlHt1O6J0Jb4CErKMVJ9IDPX0SQjJAm6vm1ELxLdVlUMFg1kyh65Rceqd5E-PHA2KpCKGWcU64y/s790-rw-e365/helm.jpg)

Microsoft has warned that using pre-made templates, such as out-of-the-box Helm charts, during [Kubernetes](https://kubernetes.io) deployments could open the door to misconfigurations and leak valuable data.

"While these 'plug-and-play' options greatly simplify the setup process, they often prioritize ease of use over security," Michael Katchinskiy and Yossi Weizman from the Microsoft Defender for Cloud Research team [said](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/the-risk-of-default-configuration-how-out-of-the-box-helm-charts-can-breach-your/4409560).

"As a result, a large number of applications end up being deployed in a misconfigured state by default, exposing sensitive data, cloud resources, or even the entire environment to attackers."

Helm is a package manager for Kubernetes that allows developers to package, configure, and deploy applications and services onto Kubernetes clusters. It's part of the Cloud Native Computing Foundation (CNCF).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Kubernetes application packages are structured in the Helm packaging format called [charts](https://helm.sh/docs/topics/charts/), which are YAML manifests and templates used to describe the Kubernetes resources and configurations necessary to deploy the app.

Microsoft pointed out that open-source projects often include default manifests or pre-defined Helm charts that prioritize ease of use over security, particularly leading to two major concerns -

* Exposing services externally without proper network restrictions
* Lack of adequate built-in authentication or authorization by default

As a result, organizations using these projects without reviewing YAML manifests and Helm charts can end up inadvertently exposing their applications to attackers. This can have serious consequences when the deployed application facilitates querying sensitive APIs or permitting administrative actions.

Some of the identified projects that could put Kubernetes environments at risk of attacks are as follows -

* Apache Pinot, which [exposes](https://docs.pinot.apache.org/basics/getting-started/kubernetes-quickstart) the OLAP datastore's main components, pinot-controller and pinot-broker, to the internet via Kubernetes LoadBalancer services without any authentication by default
* Meshery, which [exposes](https://meshery.io/) the app's interface via an external IP address, thereby allowing anyone with access to the IP address to sign up with a new user, gain access to the interface, and deploy new pods, ultimately resulting in arbitrary code execution
* Selenium Grid, which [exposes](https://github.com/kubernetes/examples/blob/master/staging/selenium/selenium-hub-svc.yaml) a NodePort service on a specific port across all nodes in a Kubernetes cluster, making external firewall rules the only line of defense

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

To mitigate the risks associated with such misconfigurations, it's advised to review and modify them according to security best practices, periodically scan publicly facing interfaces, and monitor running containers for malicious and suspicious activities.

"Many in-the-wild exploitations of containerized applications originate in misconfigured workloads, often when using default settings," the researchers said. "Relying on 'default by convenience' setups pose a significant security risk."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Container Security](https://thehackernews.com/search/label/Container%20Security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Data Exposure](https://thehackernews.com/search/label/Data%20Exposure)[DevOps](https://thehackernews.com/search/label/DevOps)[Kubernetes](https://thehackernews.com/search/label/Kubernetes)[Microsoft](https://thehackernews.com/search/label/Microsoft)[Open Source](https://thehackernews.com/search/label/Open%20Source)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to S...