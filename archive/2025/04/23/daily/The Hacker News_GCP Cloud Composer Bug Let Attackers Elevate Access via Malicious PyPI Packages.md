---
title: GCP Cloud Composer Bug Let Attackers Elevate Access via Malicious PyPI Packages
url: https://thehackernews.com/2025/04/gcp-cloud-composer-bug-let-attackers.html
source: The Hacker News
date: 2025-04-23
fetch_date: 2025-10-06T22:09:30.055604
---

# GCP Cloud Composer Bug Let Attackers Elevate Access via Malicious PyPI Packages

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

# [GCP Cloud Composer Bug Let Attackers Elevate Access via Malicious PyPI Packages](https://thehackernews.com/2025/04/gcp-cloud-composer-bug-let-attackers.html)

**Apr 22, 2025**Ravie LakshmananVulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLtmF7171FSylSNlTW3Um2CO9i9YEB53VEICr-B3GDvpr7BVZvz4OZBtpzQorEViSSBKIHQuJF-olB81d_5GuXBAujUXy5rhpbazW-r7JSA_enH_rC1-AWp603FzExYkA245zeyx2ausSAs19pDbe116tOWbg7DZ0uUWxIxuChPuU6MxFRVfN_kKS9DXd5/s790-rw-e365/google.gif)

Cybersecurity researchers have detailed a now-patched vulnerability in Google Cloud Platform (GCP) that could have enabled an attacker to elevate their privileges in the [Cloud Composer](https://cloud.google.com/composer/docs/composer-3/composer-overview) workflow orchestration service that's based on Apache Airflow.

"This vulnerability lets attackers with edit permissions in Cloud Composer to escalate their access to the default Cloud Build service account, which has high-level permissions across GCP services like [Cloud Build](https://cloud.google.com/build) itself, Cloud Storage, and Artifact Registry," Liv Matan, senior security researcher at Tenable, [said](https://www.tenable.com/blog/confusedcomposer-a-privilege-escalation-vulnerability-impacting-gcp-composer) in a report shared with The Hacker News.

The shortcoming has been codenamed ConfusedComposer by the cybersecurity company, describing it as a variant of [ConfusedFunction](https://thehackernews.com/2024/07/experts-expose-confusedfunction.html), a privilege escalation vulnerability impacting GCP's Cloud Functions service that an attacker could exploit to access other services and sensitive data in an unauthorized manner.

The disclosure comes weeks after Tenable detailed another privilege escalation vulnerability in GCP Cloud Run dubbed [ImageRunner](https://thehackernews.com/2025/04/google-fixed-cloud-run-vulnerability.html) that could have allowed a malicious actor to access container images and even inject malicious code -- creating cascading effects.

Like ImageRunner, ConfusedComposer is another example of the Jenga concept, which causes security issues to be inherited from one service to the other when cloud service providers build new services atop existing ones.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The exploit hinges on the attacker having permission to edit a Cloud Composer environment (i.e., composer.environments.update), which could be exploited to inject a malicious Python Package Index (PyPI) package that's capable of escalating privileges through Cloud Build.

The attack is made possible due to the fact that Cloud Composer allows users to install custom PyPI packages in their environments, thereby enabling an adversary to execute arbitrary code within the associated Cloud Build instance by using installation scripts inside their malicious package.

"ConfusedComposer is important because it exposes how behind-the-scenes interactions between cloud services can be exploited through privilege escalation," Matan explained. "In this case, an attacker only needs permission to update a Cloud Composer environment to gain access to critical GCP services like Cloud Storage and Artifact Registry."

Successful exploitation of the flaw could permit an attacker to siphon sensitive data, disrupt services, and deploy malicious code within CI/CD pipelines. Furthermore, it could pave the way for the deployment of backdoors that can grant persistent access to compromised cloud environments.

Following responsible disclosure by Tenable, Google has addressed the vulnerability as of April 13, 2025, by eliminating the use of the Cloud Build service account to install PyPI packages.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhubCWxvnGLW_kUa_Ze0WlaP7o_zAILqY_N7XfQhqO_hyYiwP7PuregEsQo_vK2gVIY75ut9LyklQfiPnoI0lza1Ostf-5leQnIYeuwraGmRUQbYA3Am_bswPsak_PfeybgLcGET72x6yOzcadyZMuiQMXOPtp4eLV8asYmhBSU2nbuEk_-9QqoFBMfs6ce/s790-rw-e365/cloud.png)

"The environment's service account will be used instead," Google [said](https://cloud.google.com/composer/docs/release-notes#January_15_2025) in an announcement on January 15, 2025. "Existing Cloud Composer 2 environments that previously used the default Cloud Build service account will change to using the environment's service account instead."

"Cloud Composer 2 environments created in versions 2.10.2 and later already have this change. Cloud Composer 3 environments already use the environment's service account, and are not impacted by this change."

The disclosure comes as Varonis Threat Labs uncovered a vulnerability in Microsoft Azure that could have allowed a threat actor with privileged access to an Azure SQL Server to alter configurations in a manner that causes data loss upon admin action. Microsoft has fully remediated the issue as of April 9, 2025, after it was made aware of it on August 5, 2024.

The Destructive Stored URL Parameter Injection vulnerability, the company said, stems from a lack of character limitation for server firewall rules created using Transact-SQL ([T-SQL](https://learn.microsoft.com/en-us/azure/azure-sql/database/transact-sql-tsql-differences-sql-server)).

"By manipulating the name of server-level firewall rules through T-SQL, a threat actor with privileged access to an Azure SQL Server can inject an implant that, based on specific user actions, deletes arbitrary Azure resources that the user has permissions for," security researcher Coby Abrams [said](https://www.varonis.com/blog/malicious-firewall-rules-in-azure-sql).

"The impact of a threat actor exploiting this vulnerability could be large-scale data loss in the affected Azure account."

It also comes as Datadog Security Labs shed light on a bug in Microsoft Entra ID restricted administrative units that could enable an attacker to prevent selected users from being modified, deleted, or disabled, even by a Global Administ...