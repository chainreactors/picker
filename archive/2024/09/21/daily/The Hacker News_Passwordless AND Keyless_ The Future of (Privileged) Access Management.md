---
title: Passwordless AND Keyless: The Future of (Privileged) Access Management
url: https://thehackernews.com/2024/09/passwordless-and-keyless-future-of.html
source: The Hacker News
date: 2024-09-21
fetch_date: 2025-10-06T18:32:10.470423
---

# Passwordless AND Keyless: The Future of (Privileged) Access Management

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

# [Passwordless AND Keyless: The Future of (Privileged) Access Management](https://thehackernews.com/2024/09/passwordless-and-keyless-future-of.html)

**Sep 20, 2024**The Hacker NewsPrivileged Access Management

[![](data:image/png;base64...)](https://info.ssh.com/passwordless-keyless-white-paper?utm_source=paid_media&utm_medium=image_cta&utm_campaign=thehackernews_keyless)

In IT environments, some secrets are managed well and some fly under the radar. Here's a quick checklist of what kinds of secrets companies typically manage, including one type they should manage:

* Passwords [x]
* TLS certificates [x]
* Accounts [x]
* SSH keys ???

The secrets listed above are typically secured with privileged access management (PAM) solutions or similar. Yet, most traditional PAM vendors hardly talk about SSH key management. The reason is simple: they don't have the technology to do it properly.

We can prove it. All our SSH key management customers have had a traditional PAM deployed, but they realized that they couldn't manage SSH keys with it. At best, traditional PAMs can discover, let alone manage, 20% of all keys.

## **So, what's the fuss about SSH keys?**

SSH keys are access credentials in the Secure Shell (SSH) protocol. In many ways, they're just like passwords but functionally different. On top of that, keys tend to outnumber passwords, especially in long-standing IT environments, by the ratio of 10:1. While only some passwords are privileged, ***almost all SSH keys*** open doors to something valuable.

One key can also open doors to multiple servers, just like a skeleton key in old manors. A root key allows admin access to a single server or multiple ones. After conducting a risk assessment with us, one of our customers discovered a root key that allowed access to ALL their servers.

Another risk is that anyone can self-provision SSH keys. They aren't centrally managed, and it's by design. This is why key proliferation is a lingering problem in large-scale IT environments.

There's even more: Keys don't come with an identity by default, so sharing or duplicating them is very easy. Also, with third parties. By default, keys never expire.

On top of it all, there are interactive and automated connections, the latter of which are more prevalent. Millions of automated application-to-application, server-to-server, and machine-to-machine connections are being run using SSH every day, but not enough organizations (most of them our customers) have control over machine SSH credentials.

I'm sure you got the point: your IT environment might be littered with keys to your kingdom, but you don't know how many there are, who's using them, which ones are legit and which ones should be deleted, keys don't have a best-before date, and more can be created at will without proper oversight.

The key problem is your key problem.

## **Why can't traditional PAMs handle SSH keys**?

Because SSH keys are functionally different from passwords, traditional PAMs don't manage them very well. Legacy PAMs were built to vault passwords, and they try to do the same with keys. Without going into too much detail about key functionality (like public and private keys), vaulting private keys and handing them out at request simply doesn't work. Keys must be secured at the server side, otherwise keeping them under control is a futile effort.

Furthermore, your solution needs to discover keys first to manage them. Most PAMs can't. There are also key configuration files and other key(!) elements involved that traditional PAMs miss. Read more in the following document:

[![SSH Key Management: Why PAM Tools Fail in Managing SSH Keys?](data:image/png;base64... "SSH Key Management: Why PAM Tools Fail in Managing SSH Keys?")](https://info.ssh.com/why-pam-tools-fail-in-managing-ssh-keys?utm_source=paid_media&utm_medium=image_cta&utm_campaign=thehackernews_keyless)

## **Your PAM isn't complete without SSH key management**

Even if your organization manages 100% of your passwords, the chances are that you're still missing 80% of your critical credentials if you aren't managing SSH keys. As the inventors of the Secure Shell (SSH) protocol, we at SSH Communications Security are the original source of the access credential called the SSH key. We know the ins and outs of their management.

## **Your PAM is not future-proof without credential-less access**

Let's come back to the topic of passwords. Even if you have them vaulted, you aren't managing them in the best possible way. Modern, dynamic environments - using in-house or hosted cloud servers, containers, or Kubernetes orchestration - don't work well with vaults or with PAMs that were built 20 years ago.

This is why we offer modern ephemeral access where the secrets needed to access a target are granted just-in-time for the session, and they automatically expire once the authentication is done. This leaves no passwords or keys to manage - at all. Our solution is also non-intrusive: implementing it requires minimal changes to your production environment.

How's that for reducing the attack surface, eliminating complexity, saving on costs, and minimizing risk? Read more here:

[![Future of Cybersecurity is Passwordless & Keyless](data:image/png;base64... "Future of Cybersecurity is Passwordless & Keyless")](https://info.ssh.com/passwordless-keyless-white-paper?utm_source=paid_media&utm_medium=image_cta&utm_campaign=thehackernews_keyless)

So, the best way to manage passwords AND keys is ***not to have to manage them at all*** and move to ephemeral secrets management instead. Like this:

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpWm4DGDbDALtJIOPdXflZD-jt3BtHYPsfnGyXCkERtFecmFtdTnvySxYitw6JuqioBsHukIcFCGEqlMU9FlB6P2r8kKanrH8Hzo7uMT5nfKA_YvUiPNOHga0XAesHkYjzCsW-NUmjlGc-yfJWrFgL17M6oIG-bg19p0iEpBwmWznW8IMmk5_UJ6C1PXo/s790-rw-e365/ssh-3.png)

## **"I wish I was still rotating passwords and keys." Said no customer ever!**

Once you go credential-less, you don't go back. Take it...