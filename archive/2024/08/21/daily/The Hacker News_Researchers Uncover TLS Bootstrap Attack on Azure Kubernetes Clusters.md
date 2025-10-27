---
title: Researchers Uncover TLS Bootstrap Attack on Azure Kubernetes Clusters
url: https://thehackernews.com/2024/08/researchers-uncover-tls-bootstrap.html
source: The Hacker News
date: 2024-08-21
fetch_date: 2025-10-06T18:08:48.974540
---

# Researchers Uncover TLS Bootstrap Attack on Azure Kubernetes Clusters

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

# [Researchers Uncover TLS Bootstrap Attack on Azure Kubernetes Clusters](https://thehackernews.com/2024/08/researchers-uncover-tls-bootstrap.html)

**Aug 20, 2024**Ravie LakshmananVulnerability / Container Security

[![Azure Kubernetes](data:image/png;base64... "Azure Kubernetes")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8n3JaKI-HfMw_oWz_IL2shiXqjADOmqYRdSz5gg04Vab7AMbzSxqapjFca2xU3xwJpxV-wyWzdUvCSZRPfxnIZ_EityNnolA8kHXxKQc-wWz5Nn98zorsyLTJFskT6-dUiwoPDM_Wh6_g2_z-LasWTg_GjbNURySQu7h0HznEsVT5SUN9VQAOhjZ-YmCY/s790-rw-e365/cluster.png)

Cybersecurity researchers have disclosed a security flaw impacting Microsoft Azure Kubernetes Services that, if successfully exploited, could allow an attacker to escalate their privileges and access credentials for services used by the cluster.

"An attacker with command execution in a pod running within an affected Azure Kubernetes Services cluster could download the configuration used to provision the cluster node, extract the transport layer security (TLS) bootstrap tokens, and perform a TLS bootstrap attack to read all secrets within the cluster," Google-owned Mandiant [said](https://cloud.google.com/blog/topics/threat-intelligence/escalating-privileges-azure-kubernetes-services/).

Clusters using "Azure CNI" for the "Network configuration" and "Azure" for the "Network Policy" have been found to be impacted by the privilege escalation bug. Microsoft has since addressed the issue following responsible disclosure.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack technique devised by the threat intelligence firm hinges on accessing a little-known component called Azure WireServer to request a key used to encrypt protected settings values ("wireserver.key") and use it to decode a provisioning script that includes several secrets such as follows -

* KUBELET\_CLIENT\_CONTENT (Generic Node TLS Key)
* KUBELET\_CLIENT\_CERT\_CONTENT (Generic Node TLS Certificate)
* KUBELET\_CA\_CRT (Kubernetes CA Certificate)
* TLS\_BOOTSTRAP\_TOKEN (TLS Bootstrap Authentication Token)

"KUBELET\_CLIENT\_CONTENT, KUBELET\_CLIENT\_CERT\_CONTENT, and KUBELET\_CA\_CRT can be Base64 decoded and written to disk to use with the Kubernetes command-line tool kubectl to authenticate to the cluster," researchers Nick McClendon, Daniel McNamara, and Jacob Paullus said.

"This account has minimal Kubernetes permissions in recently deployed Azure Kubernetes Service (AKS) clusters, but it can notably list nodes in the cluster."

TLS\_BOOTSTRAP\_TOKEN, on the other hand, could be used to enable a [TLS bootstrap attack](https://rhinosecuritylabs.com/cloud-security/kubelet-tls-bootstrap-privilege-escalation/) and ultimately gain access to all secrets used by running workloads. The attack does not require the pod to be running as root.

"Adopting a process to create restrictive NetworkPolicies that allow access only to required services prevents this entire attack class," Mandiant said. "Privilege escalation via an undocumented service is prevented when the service cannot be accessed at all."

The disclosure comes as Kubernetes security platform ARMO highlighted a new high-severity Kubernetes flaw ([CVE-2024-7646](https://nvd.nist.gov/vuln/detail/CVE-2024-7646), CVSS score: 8.8) that affects the ingress-nginx controller and could permit a malicious actor to gain unauthorized access to sensitive cluster resources.

"The vulnerability stems from a flaw in the way ingress-nginx validates annotations on Ingress objects," security researcher Amit Schendel [said](https://www.armosec.io/blog/cve-2024-7646-ingress-nginx-annotation-validation-bypass/).

"The vulnerability allows an attacker to inject malicious content into certain annotations, bypassing the intended validation checks. This can lead to arbitrary command injection and potential access to the ingress-nginx controller's credentials, which, in default configurations, has access to all secrets in the cluster."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It also follows the discovery of a design flaw in the Kubernetes [git-sync project](https://github.com/kubernetes/git-sync) that could allow for command injection across Amazon Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS), Google Kubernetes Engine (GKE), and Linode.

"This design flaw can cause either data exfiltration of any file in the pod (including service account tokens) or command execution with the git\_sync user privileges," Akamai researcher Tomer Peled [said](https://www.akamai.com/blog/security-research/2024-august-kubernetes-gitsync-command-injection-defcon). "To exploit the flaw, all an attacker needs to do is apply a YAML file on the cluster, which is a low-privilege operation."

There are no patches being planned for the vulnerability, making it crucial that organizations audit their git-sync pods to determine what commands are being run.

"Both vectors are due to a lack of input sanitization, which highlights the need for a robust defense regarding user input sanitization," Peled said. "Blue team members should be on the lookout for unusual behavior coming from the gitsync user in their organizations."

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
[![Facebook Messenger](data:image/png;base64...)Share on Face...