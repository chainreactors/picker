---
title: Compromised IAM Credentials Power a Large AWS Crypto Mining Campaign
url: https://thehackernews.com/2025/12/compromised-iam-credentials-power-large.html
source: The Hacker News
date: 2025-12-16
fetch_date: 2025-12-17T03:20:27.808549
---

# Compromised IAM Credentials Power a Large AWS Crypto Mining Campaign

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Compromised IAM Credentials Power a Large AWS Crypto Mining Campaign](https://thehackernews.com/2025/12/compromised-iam-credentials-power-large.html)

**Dec 16, 2025**Ravie LakshmananMalware / Threat Detection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidILz5c0w2u5MowpqpDcKaSi80yphNWTH5E6d3P9RbsKmrW49tTXLVGax2PmBg1tqbV05p_KchUWn15gqUmKNvzGPFUTa8QpmLO5zAAdT91Gcs0SbpZlMLPrf7cRmAoA_zULMCb1nIVGPp1w_yLPRclMOLJUQgH-safnADcwg3SkHT_Qfn3xbcKlDkOiub/s790-rw-e365/aws.jpg)

An ongoing campaign has been observed targeting Amazon Web Services (AWS) customers using compromised Identity and Access Management ([IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)) credentials to enable cryptocurrency mining.

The activity, first detected by Amazon's GuardDuty managed threat detection service and its automated security monitoring systems on November 2, 2025, employs never-before-seen persistence techniques to hamper incident response and continue unimpeded, according to a new report shared by the tech giant ahead of publication.

"Operating from an external hosting provider, the threat actor quickly enumerated resources and permissions before deploying crypto mining resources across ECS and EC2," Amazon [said](https://aws.amazon.com/blogs/security/cryptomining-campaign-targeting-amazon-ec2-and-amazon-ecs/). "Within 10 minutes of the threat actor gaining initial access, crypto miners were operational."

The multi-stage attack chain essentially begins with the unknown adversary leveraging compromised IAM user credentials with admin-like privileges to initiate a discovery phase designed to probe the environment for EC2 service quotas and test their permissions by invoking the [RunInstances API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) with the "DryRun" flag set.

This enabling of the "DryRun" flag is crucial and intentional as it enables the attackers to validate their IAM permissions without actually launching instances, thereby avoiding racking up costs and minimizing their forensic trail. The end goal of the step is to determine if the target infrastructure is suitable for deploying the miner program.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/filefix-d)

The infection proceeds to the next stage when the threat actor calls [CreateServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceLinkedRole.html) and [CreateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html) to create IAM roles for autoscaling groups and AWS Lambda, respectively. Once the roles are created, the "[AWSLambdaBasicExecutionRole](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)" policy is attached to the Lambda role.

In the activity observed to date, the threat actor is said to have created dozens of ECS clusters across the environment, in some cases exceeding 50 ECS clusters in a single attack.

"They then called RegisterTaskDefinition with a malicious DockerHub image yenik65958/secret:user," Amazon said. "With the same string used for the cluster creation, the actor then created a service, using the task definition to initiate crypto mining on ECS Fargate nodes."

The DockerHub image, which has since been taken down, is configured to run a shell script as soon as it's deployed to launch cryptocurrency mining using the [RandomVIREL](https://github.com/virel-project/randomvirel) mining algorithm. Additionally, the threat actor has been observed creating autoscaling groups that are set to scale from 20 to 999 instances in an effort to exploit EC2 service quotas and maximize resource consumption.

The EC2 activity has targeted both high-performance GPU and machine learning instances and compute, memory, and general-purpose instances.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgehfPgIHB0JsA1L1z3EwASD8FySwWPL_NKdBCl-tXGZbhzcxYT_a6xijAJ99gwxbg7W643T9SwawRnCSbxrhjeO8iA6fBDK6sRud1130-ngINw_rCJQgfnUGFo6-g1VtNQPt6tpCIEWc7OmQ8KqGFirbz93BwN7WJUMqXEhS4IaI3-4H_FlWtLlwU64ylT/s2600/aww.jpg)

What makes this campaign stand apart is its use of the [ModifyInstanceAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceAttribute.html) action with the "disableApiTermination" parameter set to "True," which prevents an instance from being terminated using the Amazon EC2 console, command line interface, or API. This, in turn, has the effect of requiring victims to re-enable API termination before deleting the impacted resources.

"Instance termination protection can impair incident response capabilities and disrupt automated remediation controls," Amazon said. "This technique demonstrates an understanding of common security response procedures and intent to maximize the duration of mining operations."

This is not the first time the security risk associated with ModifyInstanceAttribute has come to light. In April 2024, security researcher Harsha Koushik [demonstrated](https://medium.com/kernel-space/the-dangers-of-modifyinstanceattribute-d4290ca7a457) a proof-of-concept (PoC) that detailed how the action can be abused to take over instances, exfiltrate instance role credentials, and even seize control of the entire AWS account.

Furthermore, the attacks entail the creation of a [Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) that can be invoked by any principal and an IAM user "user-x1x2x3x4" to which the AWS managed policy "[AmazonSESFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSESFullAccess.html)" is attached, granting the adversary complete access over the Amazon Simple Email Service (SES) to likely carry out phishing attacks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

To secure against the threat, Amazon is urging AWS customers to follow the steps below -

* Enforce strong identity and access management con...