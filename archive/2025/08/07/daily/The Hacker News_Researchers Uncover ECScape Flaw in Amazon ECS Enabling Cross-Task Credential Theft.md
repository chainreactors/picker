---
title: Researchers Uncover ECScape Flaw in Amazon ECS Enabling Cross-Task Credential Theft
url: https://thehackernews.com/2025/08/researchers-uncover-ecscape-flaw-in.html
source: The Hacker News
date: 2025-08-07
fetch_date: 2025-10-07T00:51:06.141257
---

# Researchers Uncover ECScape Flaw in Amazon ECS Enabling Cross-Task Credential Theft

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

# [Researchers Uncover ECScape Flaw in Amazon ECS Enabling Cross-Task Credential Theft](https://thehackernews.com/2025/08/researchers-uncover-ecscape-flaw-in.html)

**Aug 06, 2025**Ravie LakshmananDevOps / Container Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYTMVGaxiUh2FuoVz3ONU5yqS60j7X-DEbJuKciWoxgQcpfQy5Yx64DnkKex95pBOK1ZlTU4rnCS4GUZjmnPFhTnU4tWaOiW3P_nWaxzasVmSIN-cLjckph-LfoSRMQE_TagPecfbrun8YI4YrrSDEWyqxhnzE_l5IEKFxRSJSEbRVQUBKvUJ111qpXDa2/s790-rw-e365/amazon-ecs.jpg)

Cybersecurity researchers have demonstrated an "end-to-end privilege escalation chain" in Amazon Elastic Container Service ([ECS](https://aws.amazon.com/ecs/)) that could be exploited by an attacker to conduct lateral movement, access sensitive data, and seize control of the cloud environment.

The attack technique has been codenamed ECScape by [Sweet Security](https://www.sweet.security/) researcher Naor Haziz, who [presented](https://www.blackhat.com/us-25/briefings/schedule/#ecs-cape--hijacking-iam-privileges-in-amazon-ecs-45686) the findings today at the Black Hat USA security conference that's being held in Las Vegas.

"We identified a way to abuse an undocumented ECS internal protocol to grab AWS credentials belonging to other ECS tasks on the same EC2 instance," Haziz [said](https://www.sweet.security/blog/ecscape-understanding-iam-privilege-boundaries-in-amazon-ecs) in a report shared with The Hacker News. "A malicious container with a low‑privileged IAM [Identity and Access Management] role can obtain the permissions of a higher‑privileged container running on the same host."

Amazon ECS is a fully-managed container orchestration service that allows users to deploy, manage, and scale containerized applications, while integrating with Amazon Web Services (AWS) to run container workloads in the cloud.

The vulnerability identified by Sweet Security essentially allows for privilege escalation by allowing a low-privileged task running on an ECS instance to hijack the IAM privileges of a higher-privileged container on the same EC2 machine by stealing its credentials.

In other words, a malicious app in an ECS cluster could assume the role of a more privileged task. This is facilitated by taking advantage of a [metadata service running at 169.254.170[.]2](https://www.sweet.security/blog/under-the-hood-of-amazon-ecs-on-ec2-agents-iam-roles-and-task-isolation) that exposes the temporary credentials associated with the task's IAM role.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While this approach ensures that each task gets credentials for its IAM role and they are delivered at runtime, a leak of the ECS agent's identity could permit an attacker to impersonate the agent and obtain credentials for any task on the host. The entire sequence is as follows -

* Obtain the host's IAM role credentials (EC2 Instance Role) so as to impersonate the agent
* Discover the ECS control plane endpoint that the agent talks to
* Gather the necessary identifiers (cluster name/ARN, container instance ARN, Agent version information, Docker version, ACS protocol version, and Sequence number) to authenticate as the agent using the Task Metadata endpoint and ECS introspection API
* Forge and sign the Agent Communication Service (ACS) WebSocket Request impersonating the agent with the sendCredentials parameter set to "true"
* Harvest credentials for all running tasks on that instance

"The forged agent channel also remains stealthy," Haziz said. "Our malicious session mimics the agent's expected behavior – acknowledging messages, incrementing sequence numbers, sending heartbeats – so nothing seems amiss."

"By impersonating the agent's upstream connection, ECScape completely collapses that trust model: one compromised container can passively collect every other task's IAM role credentials on the same EC2 instance and immediately act with those privileges."

ECScape can have severe consequences when running ECS tasks on shared EC2 hosts, as it opens the door to cross-task privilege escalation, secrets exposure, and metadata exfiltration.

Following responsible disclosure, Amazon has emphasized the need for customers to adopt stronger isolation models where applicable, and make it clear in its [documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) that there is no task isolation in EC2 and that "containers can potentially access credentials for other tasks on the same container instance."

As mitigations, it's [advised](https://aws.amazon.com/blogs/security/security-considerations-for-running-containers-on-amazon-ecs/) to avoid deploying high-privilege tasks alongside untrusted or low-privilege tasks on the same instance, use AWS Fargate for true isolation, disable or restrict the instance metadata service (IMDS) access for tasks, limit ECS agent permissions, and set up CloudTrail alerts to detect unusual usage of IAM roles.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9Xr-GTE602kO7J75RVaRREDoIQMUl59NHu1kvxTVVDSljCOIwYboUD4OHMJhU8u8vNNY8xmfO0NlBGW0YAMxY7qV63uoTBjvz7f96immEpKgTIdGGNFTgslCJzWhdktMG9B55_4ctei3URiV9PDd-DYqhErPHppwEHOH-ONglsXphnnvo-se-zzWXh45E/s790-rw-e365/attack.png)

"The core lesson is that you should treat each container as potentially compromiseable and rigorously constrain its blast radius," Haziz said. "AWS's convenient abstractions (task roles, metadata service, etc.) make life easier for developers, but when multiple tasks with different privilege levels share an underlying host, their security is only as strong as the mechanisms isolating them – mechanisms which can have subtle weaknesses."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes in the wake of several cloud-related security weaknesses that have been reported in recent weeks -

* A [race condition](https://adnanthekhan.com/posts/cloud-bui...