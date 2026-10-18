---
title: Hackers Use Compromised ConnectWise Credential to Sign In to 173 Microsoft 365 Tenants
url: https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html
source: The Hacker News
date: 2026-10-17
fetch_date: 2026-10-18T06:47:37.943065
---

# Hackers Use Compromised ConnectWise Credential to Sign In to 173 Microsoft 365 Tenants

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Hackers Use Compromised ConnectWise Credential to Sign In to 173 Microsoft 365 Tenants](https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html)

**Ravie Lakshmanan**Oct 17, 2026Cloud Security / Cyberattack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgel6whr7-1_Lf62w6AJwYfEyic0x1lJ0c-qOfOprMUdm83xpM7rqXbJzplx7BPBUBDD4yUcLWoPvFBhF6HIDORPNNXYj7NfDOTf7YN5lT7p80jxtN6VrTxMjWT0OplFNx0BdjoMmFzk3ssVlbapm7Qfl0Z9_1T7jA_zwz2tbjrxzRircL28mr0zcsci98x/s1700-nu-rw-lo-l85-e365/connectwise.jpg)

Cybersecurity researchers are sounding the alarm related to an active campaign in which [unknown threat actors](https://www.reddit.com/r/msp/comments/1x7gw61/cwskykick_breach/) are [abusing](https://www.reddit.com/r/msp/comments/1x7wbwf/connectwise_skykick_update/) a compromised Microsoft 365 (M365) credential belonging to ConnectWise Cloud Backup (formerly SkyKick) to gain unauthorized access to customers' M365 environments.

[ConnectWise Cloud Backup](https://www.connectwise.com/platform/bcdr/cloud-backup) is a cloud-based backup and recovery service built for managed service providers (MSPs) to secure their clients' Microsoft 365 or Google Workspace data. To accomplish its tasks, the application is granted broad access to mailboxes, OneDrive, SharePoint, Teams, and directory data in every tenant on which it's installed.

Huntress said it has observed confirmed unauthorized sign-ins within 173 partner/customer tenants using the compromised vendor credential. The incident impacts every organization that has the app installed, and the credential works against every tenant the app is consented in.

"The app's credential is in hostile hands," security researcher Jonathan Semon [said](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access). "It was used to obtain Microsoft Graph tokens in customer tenants from 144.172.64[.]128 on October 15, between 06:13 and 08:34 UTC. The actor moved through tenants in sorted GUID order, a few seconds apart, which points to a script working from a target list."

In the observed attackers, the adversary has been observed authenticating to the app using their own tooling, in a manner analogous to the backup service, and obtains tokens with the app's existing permissions. Given that the app has extensive permissions to access customer data, an attacker in possession of the tokens can read mailboxes, files, and directory data the backup service can.

Huntress said the same IP address engaged in password spraying against four law firm tenants on October 13 and 14, 2026, although it said it detected no successful user sign-ins in its telemetry.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

In at least one partner tenant, the cybersecurity company said it found a separate ConnectWise app assigning itself Global Administrator privileges and adding credentials to other trusted applications within this environment, thereby opening a pathway to other privileged apps within customer environments. This effectively extends the risk beyond the vendor account.

"The ConnectWise Cloud Management app for Microsoft Teams (application ID 24205314-2b89-4e07-a2a4-579e898a5640) added itself to the Global Administrator role, then ran a Python script (User-Agent Python-urllib/3.12) that modified two other applications in the tenant: an MSP management application, and Huntress's own application (Huntress Security Platform), adding new client secrets to both," Semon explained.

"The two applications that received new secrets are trusted, privileged tools. Adding a credential to an MSP management application can extend access beyond the one tenant, because those applications are often consented into the MSP's customers' tenants. A credential on a security tool's application gives the holder whatever that tool is permitted to do."

Todyl, in a similar analysis, said it detected an unauthorized party authenticating to Microsoft Graph as the ConnectWise Cloud Backup application.

"The access inherited the app's existing consent, which permits read/write access to mail and attachments (full mailbox access through Exchange Web Services), OneDrive and SharePoint files, and Teams chats, including the ability to restore data," Nicholas Koken, Todyl's head of Detection Engineering, [said](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app).

"Revoking user sessions does not end this access. Disabling the app in a tenant stops new tokens from being issued there, though tokens already issued stay valid for up to 90 minutes. Any tenant where the app is still enabled stays exposed until ConnectWise rotates the credential."

In response to the incident, ConnectWise [has taken the step](https://www.connectwise.com/company/trust/advisories) of closing Cloud Backup application access until further notice. The company said it has found no evidence that Cloud Backup partner backup data has been compromised. It has also shared the following steps to look for indicators of compromise -

* In the Microsoft Entra Admin Center, navigate to Monitoring → Sign-in logs, select the Service principal sign-ins tab, and filter by Application ID 506e08f9-6e9a-4da4-942b-a099a03644ae.
* The default User sign-ins tab will not display the required information.
* In the IP address column, review authentication activity originating from IP addresses outside expected Microsoft/Azure ranges. The application's normal egress has been identified as Azure private IPv6.
* Suspicious IP address: 144.172.64[.]128

"The backup service needs broad access to do its job, and an attacker using its credentials will inherit that level of access for every tenant where the app is installed," Huntress explained.

"Depending on the permissions in the tenant, that can include mailboxes, OneDrive and SharePoint files, Teams data, and director...