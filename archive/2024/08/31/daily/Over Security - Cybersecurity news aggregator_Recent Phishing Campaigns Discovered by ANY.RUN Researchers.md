---
title: Recent Phishing Campaigns Discovered by ANY.RUN Researchers
url: https://any.run/cybersecurity-blog/phishing-campaigns-august-24/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:06:19.012682
---

# Recent Phishing Campaigns Discovered by ANY.RUN Researchers

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![Recent Phishing Campaigns Discovered by ANY.RUN Researchers](/cybersecurity-blog/wp-content/uploads/2024/08/phishrecap_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Recent Phishing Campaigns Discovered by ANY.RUN Researchers

August 21, 2024

[Add comment](#comments-8645)
8544 views
8 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Recent Phishing Campaigns Discovered by ANY.RUN Researchers

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1370
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3016
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3014
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Recent Phishing Campaigns Discovered by ANY.RUN Researchers

At [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=phishing_campaigns_august24&utm_term=210824&utm_content=linktolanding), we’re committed to staying at the forefront of cybersecurity threats. Our team continuously monitors and analyzes emerging phishing campaigns to keep our users informed and protected. We regularly share our findings on our X (formerly Twitter) account.

In this article, we’ve compiled a selection of the most notable phishing campaigns we’ve seen recently. Let’s dive right in!

## Tycoon 2FA

**Original sources:**

* [X post](https://x.com/anyrun_app/status/1818972716659093913).

* [Linkedin post](https://www.linkedin.com/posts/any-run_tycoon-amazon-explorewithanyrun-activity-7224738509478113280-L48D?utm_source=share&utm_medium=member_desktop).

We’ve identified an ongoing campaign involving the Tycoon 2FA Phish-kit, which attacks via compromised Amazon Simple Email Service accounts.

Here’s how the [attack chain](https://app.any.run/tasks/6fa7c7d7-a8fb-4c5d-87fb-1531c95d1465) works:

Amazon-SES EML → CIS Social Network → India Times → Custom Redirector → Main Phish Engine → Email/Password Sent to C2.

### Initial Phishing Email

The phishing email originates from an Amazon-SES client and often includes a valid signature. The main characteristic of this email is that it contains two empty PDF files as attachments.

In some cases, the emails fail to pass SPF and DKIM checks, but it is not recommended to rely solely on these checks as the source email may be compromised.

![](/cybersecurity-blog/wp-content/uploads/2024/08/image-5-1024x623.png)

The email typically features a header from Docusign with the text: “You have received a document to review and sign.

![](/cybersecurity-blog/wp-content/uploads/2024/08/image-1024x485.jpg)

### Redirection chain

The phishing link is often rewritten by Symantec Click-time URL Protection service. When a victim clicks the “Review Document” link, they are redirected through a long chain of redirects. This technique is employed to keep the final phishing domain hidden and avoid raising suspicion.

![](/cybersecurity-blog/wp-content/uploads/2024/08/image8-3-1024x195.png)

We’ve traced the entire path of this attack, from the initial click in the email to the submission of the stolen user data, as it unfolds in the victim’s browser.

Analyze phishing and malware in ANY.RUN sandbox

[Sign up for free](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=phishing_campaigns_august24&utm_term=210824&utm_content=linktoregistration#register/)

### **Domains in the Attack Chain**

**Redirecting/Rejecting:**

|  |  |
| --- | --- |
| Clicktime.symantec[.]com | Rewritten email link |
| Away.vk[.]com | Social media redirect abuse |
| Brandequity.economictimes.indiatimes[.]com | News outlet redirect abuse |
| Jyrepresentacao[.]com | Custom unconditional target-domain-masking redirect |
| T4yzv.vereares[.]ru | Custom conditional redirect |
| Challenges.cloudflare[.]com | Turnstile Cloudflare Challenge |

**Content Delivery Networks / Services:**

|  |  |
| --- | --- |
| Code.jquery[.]com | jQuery script storage |
| Cdn.socket[.]io | Socket script storage |
| Github[.]com | Randexp script storage |
| Dnjs.cloudflare[.]com | Crypto-js script storage |
| Httpbin[.]org | External IP lookup service |
| Ipapi[.]co | IP information service |
| Ok4static.oktacdn[.]com | Static CDN storage |
| Aadcdn.msauthimages[.]net | Brand logo storage |

**Phishing Engine and C2**

The phishing operation relies on two main domains:

|  |  |
| --- | --- |
| V4l3n.delayawri[.]ru | Attackers' C2 server |
| Keqil.ticemi[.]com | Tycoon 2FA phish-kit's core engine |

The main engine code is split into two parts and obfuscated in two ways – the first part with XOR, the second with the obfuscator[.]io service.

### C2 Communication protocol

Request to C2 after entering victim’s email:

```
/<email>/<item>/<app>/<ipapi ...