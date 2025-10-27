---
title: CrowdStrike Reveals Root Cause of Global System Outages
url: https://thehackernews.com/2024/08/crowdstrike-reveals-root-cause-of.html
source: The Hacker News
date: 2024-08-08
fetch_date: 2025-10-06T18:08:43.254416
---

# CrowdStrike Reveals Root Cause of Global System Outages

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

# [CrowdStrike Reveals Root Cause of Global System Outages](https://thehackernews.com/2024/08/crowdstrike-reveals-root-cause-of.html)

**Aug 07, 2024**Ravie LakshmananCybersecurity / Incident Response

[![CrowdStrike](data:image/png;base64... "CrowdStrike")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1-x3BuKhJJZfpYpFbt1Av2bF8bIJVj_x5hn7CAmzHPMB_EVe7b1TIpyG_-FFWoxx_kKjfiekCEkopm9EST_AwXGfJlzKmDmttVpaS55ipVGwAwWs1D2lLsXCCZPwLGhTZiIVLE5ma7OluQuQXUX3UfwMokiDEIb0W_RVaLRePyA5tVimD1qDToxg7xtSw/s790-rw-e365/crash.png)

Cybersecurity company CrowdStrike has [published](https://www.crowdstrike.com/blog/channel-file-291-rca-available/) its root cause analysis detailing the Falcon Sensor software update crash that crippled millions of Windows devices globally.

The "Channel File 291" incident, as [originally highlighted](https://thehackernews.com/2024/07/crowdstrike-explains-friday-windows.html) in its Preliminary Post Incident Review (PIR), has been traced back to a content validation issue that arose after it introduced a new Template Type to enable visibility into and detection of novel attack techniques that abuse named pipes and other Windows interprocess communication (IPC) mechanisms.

Specifically, it's related to a problematic content update deployed over the cloud, with the company describing it as a "confluence" of several shortcomings that led to a crash – the most prominent of them is a mismatch between the 21 inputs passed to the Content Validator via the IPC Template Type as opposed to the 20 supplied to the Content Interpreter.

CrowdStrike said the parameter mismatch was not discovered during "multiple layers" of the testing process, in part due to the use of wildcard matching criteria for the 21st input during testing and in the initial IPC Template Instances that were delivered between March and April 2024.

In other words, the new version of Channel File 291 pushed on July 19, 2024, was the first IPC Template Instance to make use of the 21st input parameter field. The lack of a specific test case for non-wildcard matching criteria in the 21st field meant that this was not flagged until after the Rapid Response Content was shipped to the sensors.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Sensors that received the new version of Channel File 291 carrying the problematic content were exposed to a latent out-of-bounds read issue in the Content Interpreter," the company said.

"At the next IPC notification from the operating system, the new IPC Template Instances were evaluated, specifying a comparison against the 21st input value. The Content Interpreter expected only 20 values. Therefore, the attempt to access the 21st value produced an out-of-bounds memory read beyond the end of the input data array and resulted in a system crash."

Besides validating the number of input fields in the Template Type at sensor compile time to address the issue, CrowdStrike said it also added runtime input array bounds checks to the Content Interpreter to prevent out-of-bounds memory reads and corrected the number of inputs provided by the IPC Template Type.

"The added bounds check prevents the Content Interpreter from performing an out-of-bounds access of the input array and crashing the system," it noted. "The additional check adds an extra layer of runtime validation that the size of the input array matches the number of inputs expected by the Rapid Response Content."

On top of that, CrowdStrike said it plans to increase test coverage during Template Type development to include test cases for non-wildcard matching criteria for each field in all (future) Template Types.

Some of the sensor updates are also expected to resolve the following gaps -

* The Content Validator is being modified to add new checks to ensure that content in Template Instances does not include matching criteria that match over more fields than are being provided as input to the Content Interpreter

* The Content Validator is being modified to only allow wildcard matching criteria in the 21st field, which prevents the out-of-bounds access in the sensors that only provide 20 inputs

* The Content Configuration System has been updated with new test procedures to ensure that every new Template Instance is tested, regardless of the fact that the initial Template Instance is tested with the Template Type at creation

* The Content Configuration System has been updated with additional deployment layers and acceptance checks

* The Falcon platform has been updated to provide customers with increased control over the delivery of Rapid Response Content

Last but not least, CrowdStrike said it has engaged two independent third-party software security vendors to conduct further review of the Falcon sensor code for both security and quality assurance. It's also carrying out an independent review of the end-to-end quality process from development through deployment.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It has further pledged to work with Microsoft as Windows introduces new ways to perform security functions in user space as opposed to relying on a kernel driver.

"CrowdStrike's kernel driver is loaded from an early phase of system boot to allow the sensor to observe and defend against malware that launches prior to user mode processes starting," it said.

"Providing up-to-date security content (e.g., CrowdStrike's Rapid Response Content) to these kernel capabilities enables the sensor to defend systems against a rapidly evolving threat landscape without making changes to kernel code. Rapid Response Content is configuration data; it is not code or a kernel driver."

The release of the root cause analysis comes as Delta Air Lines [said](https://www.cnbc.com/2024/07/29/delta-hires-david-boies-to-seek-damages-from-crowdstrike-microsoft-.html) it has "no choice" but to seek damages from CrowdStrike and Microsoft for causing massive disruptions and costing...