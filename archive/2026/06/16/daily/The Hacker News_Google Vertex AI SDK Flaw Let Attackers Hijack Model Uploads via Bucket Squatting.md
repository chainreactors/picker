---
title: Google Vertex AI SDK Flaw Let Attackers Hijack Model Uploads via Bucket Squatting
url: https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html
source: The Hacker News
date: 2026-06-16
fetch_date: 2026-06-17T07:04:11.616408
---

# Google Vertex AI SDK Flaw Let Attackers Hijack Model Uploads via Bucket Squatting

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Google Vertex AI SDK Flaw Let Attackers Hijack Model Uploads via Bucket Squatting](https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html)

**Swati Khandelwal**Jun 16, 2026Machine Learning / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpiAGZTnvo43enaVYkna4ZSp217mwwW5kW8kZOhaSiLAxicjvHQY-3d8rdLN47bsRvxUIj6R0h_Ttr8NcIJrgz6k_mbcx94KLuPD29KdhFcYQsrV8htgg_iDYMV9aXbr21kv6BdYTzLNOOqQLpsCfpDC4XxDPnu77uVQ3oCYbIUfIpUKdmqx-rZZWj6P0/s1700-e365/Google-Vertex-AI.jpg)

A flaw in the Google Cloud Vertex AI SDK for Python let an attacker with no access to a victim's project hijack the victim's machine learning model upload and run code inside Google's serving infrastructure.

Palo Alto Networks Unit 42, which found and [reported](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/) the bug through Google's bug bounty program, calls the technique "**Pickle in the Middle**" and said it saw no exploitation in the wild. Google has patched it; if you use the SDK, update to version 1.148.0 or later.

The attacker needed only a Google Cloud project of their own and the victim's project ID, which is often public. No credentials, no phishing, no foothold in the target.

The flaw was in how the SDK chose a temporary Cloud Storage bucket for model uploads. If a user did not set a bucket, the SDK generated a predictable name from the project ID and region, such as *project-vertex-staging-region*. It checked whether that bucket existed, but not whether the victim owned it.

Because bucket names are globally unique, an attacker could create the expected bucket first in their own project. The victim's SDK would then upload the model files to the attacker's bucket. The attacker could then replace the uploaded model with a malicious one.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Many Python ML models are saved with [pickle](https://docs.python.org/3/library/pickle.html) or [joblib](https://joblib.readthedocs.io/en/stable/), which can run code when a file is loaded. When Vertex AI later loaded the swapped model, the attacker's code executed inside the serving container.

The attack depended on speed. Unit 42 measured about 2.5 seconds between the victim's upload and Vertex AI reading the file. In its proof of concept, the attacker used a Cloud Function that triggered after upload and replaced the model in 1.4 seconds, before Vertex AI read it.

The payload then stole an OAuth token from the serving container's metadata server and sent it to the attacker. In Unit 42's test environment, that token was not limited to the compromised deployment. It could access other model artifacts in the same Google-managed tenant project, including a full TensorFlow model with trained weights, as well as BigQuery metadata, access lists, tenant logs, GKE cluster names, and internal container image paths.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi44arRHIBKBINb19ia9izN1ZJEdRQb66daWeR8Q_rIie27guF-8nPTb_9ndCjSgscxjYfM3o4UjYP6rRfs2N4hV9jHjN69IGI0dqkkVtiUtJMtYfDtF48MORBQUcQeOWJCCbCmIDLfhqZWqIOavaonpG82K4yiGCYV2w11W_fqzdps5UUrFsrzZgQEXmA/s1700-e365/bucket.jpg)

The attack worked only under specific conditions: the victim's default staging bucket did not already exist in that region, and the victim left the *staging\_bucket*parameter unset. The first is common for a new project in Vertex AI in a region.

The second depends on the developer relying on the SDK's default rather than naming their own bucket.

Unit 42 reported the flaw through Google's Vulnerability Reward Program on March 5, 2026. It tested versions 1.139.0 and 1.140.0, the latest available at the time, and found both vulnerable.

Google shipped an initial fix in [v1.144.0](https://github.com/googleapis/python-aiplatform/compare/v1.143.0...v1.144.0) on March 31, adding a random uuid4 to the bucket name. It completed the fix in [v1.148.0](https://github.com/googleapis/python-aiplatform/releases/tag/v1.148.0) on April 15, adding bucket ownership verification to block bucket squatting in Model.upload(). As of publication, neither Unit 42 nor Google's Vertex AI security bulletins list a CVE for the issue.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

Update to 1.148.0 or later so the ownership check is active. Also, set an explicit staging\_bucket to a Cloud Storage location you control when uploading models. Because the flawed logic lives in the client SDK, check the google-cloud-aiplatform version wherever it runs, including notebooks, CI jobs, and training pipelines, not only production services.

It is the second predictable-bucket-name flaw to surface in Vertex AI this year. Google patched [CVE-2026-2473](https://cloud.google.com/vertex-ai/docs/security-bulletins) in February, a separate bucket-squatting bug in Vertex AI Experiments that also allowed cross-tenant code execution, model theft, and poisoning.

Unit 42's earlier work on [Vertex AI's default service-agent permissions](https://thehackernews.com/2026/03/vertex-ai-vulnerability-exposes-google.html) traced a related path from a deployed AI agent into customer and tenant data.

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
[![Facebook Messe...