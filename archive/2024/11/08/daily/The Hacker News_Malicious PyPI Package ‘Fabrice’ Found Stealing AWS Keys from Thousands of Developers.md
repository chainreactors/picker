---
title: Malicious PyPI Package ‘Fabrice’ Found Stealing AWS Keys from Thousands of Developers
url: https://thehackernews.com/2024/11/malicious-pypi-package-fabrice-found.html
source: The Hacker News
date: 2024-11-08
fetch_date: 2025-10-06T19:21:41.762683
---

# Malicious PyPI Package ‘Fabrice’ Found Stealing AWS Keys from Thousands of Developers

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

# [Malicious PyPI Package 'Fabrice' Found Stealing AWS Keys from Thousands of Developers](https://thehackernews.com/2024/11/malicious-pypi-package-fabrice-found.html)

**Nov 07, 2024**Ravie LakshmananVulnerability / Cloud Security

[![Stealing AWS Keys](data:image/png;base64... "Stealing AWS Keys")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlqOisrbs23lBeGf62GBId24Zz-61Bg6hyphenhyphenimkO8ZJo-SkbZCTo9aLUGPP7E9t9xJ4dJTSS-I_DQLsTgAuie_Pz-qTKh2g3UfV6rX4TFG5knhrC62BpasbvlSW9b8SW3zLTUoVK7Pg4jlPsmQywm0tW1Ihcdakfq8MDB_fz_lbD00ztYJQb9Zoi4lmGZUoe/s790-rw-e365/aws.png)

Cybersecurity researchers have discovered a malicious package on the Python Package Index (PyPI) that has racked up thousands of downloads for over three years while stealthily exfiltrating developers' Amazon Web Services (AWS) credentials.

The package in question is "[fabrice](https://pypi.org/project/fabrice/)," which typosquats a popular Python library known as "[fabric](https://pypi.org/project/fabric/)," which is designed to execute shell commands remotely over SSH.

While the legitimate package has over 202 million downloads, its malicious counterpart has been [downloaded](https://secure.software/pypi/packages/fabrice) more than 37,100 times to date. As of writing, "fabrice" is still available for download from PyPI. It was first published in March 2021.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The typosquatting package is designed to exploit the trust associated with "fabric," incorporating "payloads that steal credentials, create backdoors, and execute platform-specific scripts," security firm Socket [said](https://socket.dev/blog/malicious-python-package-typosquats-fabric-ssh-library).

"Fabrice" is designed to carry out its malicious actions based on the operating system on which it's installed. On Linux machines, it uses a specific function to download, decode, and execute four different shell scripts from an external server ("89.44.9[.]227").

On systems running Windows, two different payloads – a Visual Basic Script ("p.vbs") and a Python script – are extracted and executed, with the former running a hidden Python script ("d.py") stored in the Downloads folder.

"This VBScript functions as a launcher, allowing the Python script to execute commands or initiate further payloads as designed by the attacker," security researchers Dhanesh Dodia, Sambarathi Sai, and Dwijay Chintakunta said.

The other Python script is designed to download a malicious executable from the same remote server, save it as "chrome.exe" in the Downloads folder, set up persistence using scheduled tasks to run the binary every 15 minutes, and finally delete the "d.py" file.

The end goal of the package, regardless of the operating system, appears to be credential theft, gathering AWS access and secret keys using the [Boto3](https://pypi.org/project/boto3/) AWS Software Development Kit (SDK) for Python and exfiltrating the information back to the server.

"By collecting AWS keys, the attacker gains access to potentially sensitive cloud resources," the researchers said. "The fabrice package represents a sophisticated typosquatting attack, crafted to impersonate the trusted fabric library and exploit unsuspecting developers by gaining unauthorized access to sensitive credentials on both Linux and Windows systems."

### Update

The "fabrice" package is no longer available for download from the PyPI repository. An AWS spokesperson provided the below statement with The Hacker News following the publication of the story -

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

*We recommend customers who use the legitimate software "fabric" for SSH interactions ensure they are not inadvertently using the malware "fabrice." AWS customers who suspect malicious activity within their AWS accounts or credentials should follow guidance for* [*remediating potentially compromised AWS credentials*](https://docs.aws.amazon.com/guardduty/latest/ug/compromised-creds.html) *or* [*contact AWS Support*](https://aws.amazon.com/contact-us/) *for assistance. Maintaining proper software supply chain security, including validating the correct source code and name of any software or dependency installed, reduces the risk posed by packages that abuse credentials.* [*AWS contributes to the software supply chain security*](https://aws.amazon.com/blogs/opensource/securing-pypi-for-the-future/) *of Python’s open source ecosystem through an industry-first Python Package Index (PyPi) Security Sponsorship with Python Software Foundation.*

*(The story was updated after publication on November 16, 2024, to include a response from AWS.)*

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

[AWS](https://thehackernews.com/search/label/AWS)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Python](https://thehackernews.com/search/label/Pyth...