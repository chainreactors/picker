---
title: Hugging Face Diffusers Flaws Could Let Model Repositories Execute Arbitrary Code
url: https://thehackernews.com/2026/08/hugging-face-diffusers-flaws-could-let.html
source: The Hacker News
date: 2026-08-03
fetch_date: 2026-08-04T05:01:12.924614
---

# Hugging Face Diffusers Flaws Could Let Model Repositories Execute Arbitrary Code

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

# [Hugging Face Diffusers Flaws Could Let Model Repositories Execute Arbitrary Code](https://thehackernews.com/2026/08/hugging-face-diffusers-flaws-could-let.html)

**Ravie Lakshmanan**Aug 03, 2026Vulnerability / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWQmUt2QHxTfiXiolir9akmVh8dT5di3UBDtD7H2IJlkWQ4x4VmeTUEZo8CUvz2q2FXCvxTJDHenWPzqPeSbnlCYSRTNGULKdWRJnsmVg7SVJT_BBPABxqRuvr22Z9V2C6P51fRjSGzgAlHMzEn-MjA4yTMfCaM91ujVajF8GJqYg9ZaZELXsCc-GMnYq8/s1700-e365/hugging.jpg)

Three high-severity security flaws have been disclosed in Hugging Face's [Diffusers](https://pypi.org/project/diffusers/#description) library that could allow crafted model repositories to stealthily execute arbitrary code on machines that load it, opening the artificial intelligence (AI) supply chain to security risk.

"These vulnerabilities are bypassing trust\_remote\_code, the safeguard designed to stop unreviewed code from running in the custom pipelines loading process," Zafran Labs researchers Gal Zaban and Ido Shani [said](https://www.zafran.io/resources/facehugger-vulnerabilities-in-hugging-face-diffusers-open-door-to-supply-chain-attacks-on-enterprise-ai) in an analysis published last week.

The shortcomings have been collectively named **FaceHugger**.

With Hugging Face becoming the "GitHub of the AI era" and its libraries and repositories prevalent in enterprise environments, vulnerabilities in libraries like Diffusers can grant attackers extensive access owing to how the library is embedded into production pipelines, CI/CD systems, and container images.

Diffusers is a [Python package](https://huggingface.co/docs/diffusers/en/index) that serves as a library of state-of-the-art (SOTA) pretrained diffusion models for generating videos, images, and audio. According to statistics shared on pepy.tech, the package has been [downloaded](https://pepy.tech/projects/diffusers?timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=monthly&viewType=line&versions=Total%2C0.*) more than 8.1 million times in July 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

One of the key capabilities of the library is to locally load a model from a Hugging Face hub repository via the [DiffusionPipeline](https://huggingface.co/docs/diffusers/v0.39.0/en/api/pipelines/overview#diffusers.DiffusionPipeline) API, which, in turn, makes use of a configuration file to initialize specific pipeline and component classes, along with custom pipeline code.

The "trust\_remote\_code" parameter in Diffusers is a security safeguard that controls whether custom Python code hosted inside a model repository is allowed to execute during "from\_pretrained()" loading. Setting it to "True" permits custom code execution, while "False" or omitting it blocks unverified code from running.

"The root cause of all different RCE variants [...] is that the trust check lives entirely in the first phase," Zafran explained. "Therefore, any method that makes the loader see custom code that the gate did not, allows bypassing the trust\_remote\_code mechanism."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvM63veS-QQ4F95eiHeX_Vy-uoJ3R1_9WD1T6F3xiNh4knGqz1Jfpg3YP15O80DXp2-ohajtnpf-a4QbQmHrYsD8dAKlyRJtHufUdXesf1ndiQZuCCAXmoEJsddWA2jhd_pn38oqvZXLfDiGOgR5nO1h2ERCYe8S4TLDceUu6SD2b_E4VakXX7I_U09xyg/s1700-e365/poc.jpg)

Each variant has been traced back to a case of Time-of-Check to Time-of-Use (TOCTOU), with the model download designed as two sequential, non-atomic HTTP requests instead of one a "single atomic operation" and the "trust\_remote\_code" security gate configured to run only against the first.

The vulnerabilities are listed below -

* **[CVE-2026-44827](https://github.com/advisories/GHSA-j7w6-vpvq-j3gm)** (CVSS score: 8.8) - A code injection vulnerability that allows arbitrary code to be loaded through the custom\_pipeline flow from a Hub repository by means of a crafted pipeline with the name "None.py" despite passing trust\_remote\_code=False (or omitting it, which is the default).
* **[CVE-2026-45804](https://github.com/advisories/GHSA-7wx4-6vff-v64p)** (CVSS score: 7.5) - A race condition vulnerability that allows arbitrary code to be introduced to a repository by modifying the configuration between the hf\_hub\_download and snapshot\_download HTTP calls to the Hub, leading to code execution.
* **[CVE-2026-44513](https://github.com/advisories/GHSA-98h9-4798-4q5v)** (CVSS score: 8.8) - A code injection vulnerability that allows arbitrary code to be loaded through the custom\_pipeline flow from a Hub repository despite passing trust\_remote\_code=False (or omitting it).

Following responsible disclosure, the vulnerabilities were addressed in Diffusers version 0.38.0, released in early May 2026. Any user who invokes "DiffusionPipeline.from\_pretrained" with custom pipelines is impacted.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"The underlying problem is that artifacts pulled from AI repositories are frequently treated as passive data, when configuration files, loaders, and custom pipeline code can quietly cross into executable code and turn a routine model load into an initial-access vector," the researchers added.

If immediate patching is not an option, the project maintainers have recommended the following workarounds -

* Only call from\_pretrained with pretrained\_model\_name\_or\_path, custom\_pipeline, and local snapshot directories from fully trusted sources that have been audited.
* Do not pass custom\_pipeline= pointing at a Hub repository different from the primary pretrained\_model\_name\_or\_path before reading its pipeline.py.
* Before calling from\_pretrained on a local snapshot, inspect the snapshot for unexpected \*.py files, especially under component subdirectories (unet/, scheduler/, etc.) and at the snapshot root.

"These vulnerabilities underscore the critical need to treat AI model repositories as untrusted code, particularly as enterprise reliance on platforms like Hugging Face continues to grow," Zafran said. "A routine model download can easily become a vector for arbitrary code execution if security boundaries like trust\_remot...