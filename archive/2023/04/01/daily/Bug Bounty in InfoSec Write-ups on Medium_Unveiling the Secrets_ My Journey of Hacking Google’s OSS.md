---
title: Unveiling the Secrets: My Journey of Hacking Google’s OSS
url: https://infosecwriteups.com/unveiling-the-secrets-my-journey-of-hacking-googles-oss-cdd9ef3c7aa?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-04-01
fetch_date: 2025-10-04T11:21:33.616008
---

# Unveiling the Secrets: My Journey of Hacking Google’s OSS

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcdd9ef3c7aa&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funveiling-the-secrets-my-journey-of-hacking-googles-oss-cdd9ef3c7aa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funveiling-the-secrets-my-journey-of-hacking-googles-oss-cdd9ef3c7aa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-cdd9ef3c7aa---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-cdd9ef3c7aa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Unveiling the Secrets: My Journey of Hacking Google’s OSS

[![7h3h4ckv157](https://miro.medium.com/v2/resize:fill:64:64/1*vBGOxG8iMbnWIrk7-RzBgg@2x.jpeg)](https://7h3h4ckv157.medium.com/?source=post_page---byline--cdd9ef3c7aa---------------------------------------)

[7h3h4ckv157](https://7h3h4ckv157.medium.com/?source=post_page---byline--cdd9ef3c7aa---------------------------------------)

4 min read

·

Mar 31, 2023

--

1

Listen

Share

- **August 22, 2022**

Press enter or click to view image in full size

![]()

Let’s dive into it!

Dear Infosec,

I am excited to share with you my experience of discovering a security vulnerability in Google’s open-source software (OSS) last year. Imagine acquiring an acknowledgement from one of the biggest tech companies in the world for uncovering a security vulnerability in their open-source software. It was an exhilarating experience, but also one that taught me a lot about the importance of security research and the challenges that come with it.

In this blog post, I want to share my journey of hacking Google’s OSS, from the initial discovery to the reporting process and beyond. I hope that by sharing my experience, others will be inspired to pursue similar work and contribute to the ongoing effort to keep our digital world safe and secure.

Google Cloud Platform (GitHub) contain code samples used on **cloud.google.com** Here’s the [*GitHub link*](https://github.com/GoogleCloudPlatform)*.* I decided to put my skills to the test by reviewing a Python repository *(***REDACTED***)* because it’s a language I’m acquainted with and have some experience.

### About the Vulnerability

Upon reviewing the code, I found unsanitized input can be accepted from the HTTP request inside the below function where it is used to render an HTML page returned to the user.

```
def exam_task_handler():

    payload = request.get_data(as_text=True) or '(empty payload)'
    print('Received task with payload: {}'.format(payload))
    return'Printed task payload: {}'.format(payload)
```

Press enter or click to view image in full size

![]()

Proof

```
<py-script>
```

```
PyScript is a framework that allows users to create rich Python applications
in the browser using HTML's interface and the power of Pyodide
WASM, and modern web technologies.

The PyScript framework provides users at every experience level
with access to an expressive, easy-to-learn programming language with
countless applications.

(Copied)
```

```
</py-script>
```

But the function bears value through a POST request, If the endpoint only abides by the payload through a POST request, this vulnerability would indeed fall under the classification of Self-XSS. To prevent the execution of JS in the browser it’s essential to sanitize all input from the HTTP request before using it in any context, including rendering an HTML page. Sanitization can involve removing or encoding any potentially malicious characters to prevent them from being executed as code.

### Making Impact

* CSRF + Self-XSS

By chaining these two bugs together, I was able to demonstrate the potential risks of even seemingly minor vulnerabilities in the code. Self-XSS with CSRF permits me to bypass this restriction and trigger an impactful XSS.

Steps that I used:

```
1. Visit the service

2. Navigate to the /example_task_handler endpoint

3. You will receive a "Method not allowed" error
   because only HTTP POST requests are allowed.

4. Intercept the request and change the method type from GET to POST.

5. Trigger the XSS payload
   which will allow you to execute malicious code on your own system
   (Self-XSS)

6. Chain the Self-XSS vulnerability with a CSRF attack
   (meaningful impact)
```

While performing the CSRF attack: The malicious POST request from victim’s browser to a vulnerable web application, and the request appears to come from a legitimate user. The victim’s browser is then tricked into submitting the request, which can cause the application to perform an unintended action on behalf of the user. If the POST request contains a payload that includes a Self-XSS vulnerability, then the script will execute in the victim’s browser, allowing the attacker to execute arbitrary code and potentially steal sensitive information or perform unauthorized actions.

I reported this issue to Google, as usual I have some conversations with them through comments and then finally they accepted my report.

```
triaged
14:17 | 22.08.2022

closed
15:59 | 22.08.2022

triaged
17:56 | 22.08.2022

accepted
19:38 | 23.08.2022

fixed
05:53 | 22.09.2022
```

This was something I get back from them.

> ks…@google.com 26.09.2022 | 12:46 | #34

Hello! For credit you can be visible on Honorable mentions

Press enter or click to view image in full size

![]()

Honorable Mention

The decision to participate in bug bounty programs or disclose vulnerabilities should be driven by a desire to improve security and promote responsible disclosure practices, rather than solely by the potential for financial reward. Honorable mention is a valuable recognition in building a reputation within the security community and can lead to future opportunities for collaboration, networking, and career advancement.

> It’s true that securing code samples in open-source projects may not always result in a monetary bounty from the project maintainers or companies that offer bug bounty programs. But it’s important to improve the security of software systems that people rely on. Many security researchers and professionals participate in bug bounty programs or disclose vulnerabilities as a way to give back to the community and help make the internet a safer place. Even if there is no financial reward, the recognition and sense of accomplishment that comes with discovering and mitigating a security risk can be a powerful motivator.

Therefor I reported another bug directly through GitHub Issues.

> Check this out: [Link](https://github....