---
title: Experts Uncover Severe AWS Flaws Leading to RCE, Data Theft, and Full-Service Takeovers
url: https://thehackernews.com/2024/08/experts-uncover-severe-aws-flaws.html
source: The Hacker News
date: 2024-08-10
fetch_date: 2025-10-06T18:07:47.401048
---

# Experts Uncover Severe AWS Flaws Leading to RCE, Data Theft, and Full-Service Takeovers

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

# [Experts Uncover Severe AWS Flaws Leading to RCE, Data Theft, and Full-Service Takeovers](https://thehackernews.com/2024/08/experts-uncover-severe-aws-flaws.html)

**Aug 09, 2024**Ravie LakshmananCloud Security / Data Protection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwkUNCjPX0J48EMTA7L5vrNf1dZp6YlQ8jWhCO622Jz-PZHmKGLt0JTZ-41EnhIkjALacLAR9AOl4b07t_qH-qk7SkxZc67wrNh33XZH9TCla6lnFbM_Dz_LJ0jPqPvRWAjUFSoZRtHblPUYOAyCwurGPrpX6G4JEc0h0e2GyZrvG6nwl6xRn0NS57qfkr/s790-rw-e365/cloud.png)

Cybersecurity researchers have discovered multiple critical flaws in Amazon Web Services (AWS) offerings that, if successfully exploited, could result in serious consequences.

"The impact of these vulnerabilities range between remote code execution (RCE), full-service user takeover (which might provide powerful administrative access), manipulation of AI modules, exposing sensitive data, data exfiltration, and denial-of-service," cloud security firm Aqua said in a detailed [report](https://www.aquasec.com/blog/bucket-monopoly-breaching-aws-accounts-through-shadow-resources/) shared with The Hacker News.

Following responsible disclosure in February 2024, Amazon addressed the shortcomings over several months from March to June. The findings were [presented](https://www.blackhat.com/us-24/briefings/schedule/#breaching-aws-accounts-through-shadow-resources-39706) at Black Hat USA 2024.

Central to the issue, dubbed Bucket Monopoly, is an attack vector referred to as Shadow Resource, which, in this case, refers to the automatic creation of an AWS S3 bucket when using services like CloudFormation, Glue, EMR, SageMaker, ServiceCatalog, and CodeStar.

The S3 bucket name created in this manner is both unique and follows a predefined naming convention (e.g., "cf-templates-{Hash}-{Region}"). An attacker could take advantage of this behavior to set up buckets in unused AWS regions and wait for a legitimate AWS customer to use one of the susceptible services to gain covert access to the contents of the S3 bucket.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Based on the permissions granted to the adversary-controlled S3 bucket, the approach could be used to escalate to trigger a DoS condition, or execute code, manipulate or steal data, and even gain full control over the victim account without the user's knowledge.

To maximize their chances of success, using Bucket Monopoly, attackers can create unclaimed buckets in advance in all available regions and store malicious code in the bucket. When the targeted organization enables one of the vulnerable services in a new region for the first time, the malicious code will be unknowingly executed, potentially resulting in the creation of an admin user that can grant control to the attackers.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjScic1EWimsGHexiZzxBo9zkVCw9Iz1kn_PkscTmry0-t6D85cJldtzDs8gO5FiFPAC6P-rDEqbj1NOQ0xfQ-rAnkF3BBkHPjEfK64BuwpOf21tsEVL_OjOZsAQKHpj36XCapOk3WSV_QQJHYOtGhyphenhyphen3hnyNGcjm-MTvdsx7Hu2I0pFlJ3lE-3sV9kDSKDB/s790-rw-e365/1.png) |
| Overview of CloudFormation vulnerability |

However, it's important to consider that the attacker will have to wait for the victim to deploy a new CloudFormation stack in a new region for the first time to successfully launch the attack. Modifying the CloudFormation template file in the S3 bucket to create a rogue admin user also depends on whether the victim account has permission to manage IAM roles.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqbM736d8Ql9UtaSHJ0yLcBRA4A4pNg6XrdaZhaVK2goQBgeE7nwmHzbDga4_AAUxMQhDSYmYsHd5WFnzlfIs26G5gdoPDg94MtS9zgYF_PB7easOXne9hY02_EjL_l-d4nNKslBpSMe17EYwYl5Bf0D9vDTwKgP-XVCzjemvDLB6opduw0eqHMVvkvpjP/s790-rw-e365/2.png) |
| Overview of Glue vulnerability |

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9GSm_0Iw3-55S0zsqH-I8-EAmtOdNd8qJrnqyeVfxGV7MdJm9UZ0Hn0bsFEeUm7KgOJg8WdmfwcPHHCVAPFUMxHM5bZsWXTFoP29NUt-IgPHeugFwJ4hz66DcjFQKrkw5edu_LTI7HE53M29x-d_sVYJMZCQIAdXv1dvoGA2rZ5K_kjNpFaEdpMyhCsFv/s790-rw-e365/3.png) |
| Overview of CodeStar vulnerability |

Aqua said it found five other AWS services that rely on a similar naming methodology for the S3 buckets – {Service Prefix}-{AWS Account ID}-{Region} – thereby exposing them to Shadow Resource attacks and ultimately permitting a threat actor to escalate privileges and perform malicious actions, including DoS, information disclosure, data manipulation, and arbitrary code execution -

* AWS Glue: aws-glue-assets-{Account-ID}-{Region}
* AWS Elastic MapReduce (EMR): aws-emr-studio -{Account-ID}-{Region}
* AWS SageMaker: sagemaker-{Region}-{Account-ID}
* AWS CodeStar: aws-codestar-{Region}-{Account-ID}
* AWS Service Catalog: cf-templates-{Hash}-{Region}

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The company also noted that AWS account IDs should be considered a secret, contrary to what Amazon [states](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html) in its documentation, as they could be used to stage similar attacks.

What's more, hashes used for AWS accounts can be uncovered using [GitHub regular expression searches](https://github.com/search?type=code&auto_enroll=true) or [Sourcegraph](https://sourcegraph.com/search), or, alternately, by scraping open issues, thus making it possible to piece together the S3 bucket name even in the absence of a way to calculate the hash directly from the account ID or any other account-related metadata.

"This attack vector affects not only AWS services but also many open-source projects used by organizations to deploy resources in their AWS environments," Aqua said. "Many open-source projects create S3 buckets automatically as part of their functionality or instruct their users to deploy S3...