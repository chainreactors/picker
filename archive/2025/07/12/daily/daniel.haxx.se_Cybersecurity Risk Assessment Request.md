---
title: Cybersecurity Risk Assessment Request
url: https://daniel.haxx.se/blog/2025/07/11/cybersecurity-risk-assessment-request/
source: daniel.haxx.se
date: 2025-07-12
fetch_date: 2025-10-06T23:28:43.362675
---

# Cybersecurity Risk Assessment Request

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/07/world-map-curl-2000.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Cybersecurity Risk Assessment Request

[July 11, 2025](https://daniel.haxx.se/blog/2025/07/11/cybersecurity-risk-assessment-request/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [6 Comments](https://daniel.haxx.se/blog/2025/07/11/cybersecurity-risk-assessment-request/#comments)

With the new EU legislation Cyber Resiliency Act (CRA), there are new responsibilities and requirements put on *manufacturers* of digital products and services in Europe.

Going forward these manufacturers must be able to know and report the exact contents of their software, called a Software Bill of Material (SBOM) and they have requirements to check for vulnerabilities in those components etc. This implies that they need to have full control and knowledge about all of their Open Source components in their stack. (See the [CRA Hub](https://github.com/orcwg/cra-hub) for a good resource on CRA for Open Source people.)

As a maintainer of a software component that is widely used, I have been curious to see how this will materialize for us. Today I got a first glimpse of what I can only guess will happen more going forward.

This multi-billion-dollar Fortune-500 company that I have no contract with and with which I have had no previous communication, sent me this email asking for a lot of curl information. A slightly redacted version is shown below.

Now that my curiosity has been satisfied a little bit I instead await the future and long to see how many more of these that will come. And how they will respond to my replies.

```
CRA_request_counter = 1;
```

## The request

> Hello,
>
> I hope this message finds you well.
>
> As part of our ongoing efforts to comply with the EU Cyber Resilience Act (CRA), we are currently conducting a cybersecurity risk assessment of third-party software vendors whose products or components are integrated into our systems.
>
> To support this initiative, we kindly request your input on the following questions related to your software product “libcurl” with version 7.87.0. Please provide your responses directly in the table below and do reply to all added in this email,
>
> Additional Information:
>
> * Purpose: This security assessment is part of our due diligence and regulatory compliance obligations under the EU CRA.
> * Confidentiality: All information shared will be treated as confidential and used solely for the purpose of this assessment.
> * Contact: Should you have any questions or need further clarification, please feel free to reach out by replying directly to this email.
>
> We kindly request your response by Friday, July 25, 2025, to ensure timely completion of our assessment process. Thank you for your cooperation and continued partnership in maintaining a secure and resilient digital environment.

## My reaction and response

I am not their *vendor* without having a more formal relationship established and I am certainly not going to spend a few hours of my spare time gathering a lot of information for them for free for their commercial benefit.

They “kindly” want me to respond within two weeks.

Their use of double quotes around “libcurl” feels odd, and they claim to be using a version that is now more than 2.5 years old.

Most if not all of the information they are asking for is already publicly and openly accessible and readable. I suspect they want the information in this more formal way to make it appear more reliable or trustworthy perhaps. Or maybe it just follows their processes better.

(It also reminded me of the [NASA emails](https://daniel.haxx.se/blog/2020/12/17/curl-supports-nasa/).)

I responded like this

> Hello,
>
> I will be happy to answer all curl and libcurl related questions and assist you with this inquiry as soon as we have a support contract setup. You can get the process started immediately by emailing support@wolfssl.com.
>
> Thanks, I’m looking forward to future cooperation.
>
> / Daniel

I will let you know if they take me up on my offer .

## The screenshot

This snapshot of how it looked also shows the actual nine-question form table.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/07/Cybersecurity-Risk-Assessment.png)

Email screenshot

## Why the company name is redacted

I’m looking forward to eventually do business with this company, I don’t want them to feel targeted or “ridiculed”. I also suspect that there will be many more emails like this going forward. The company name is not the interesting part of this story.

[CRA](https://daniel.haxx.se/blog/tag/cra/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous Postmore views on curl vulnerabilities](https://daniel.haxx.se/blog/2025/07/10/more-views-on-curl-vulnerabilities/)[Next PostSponsor my laptop!](https://daniel.haxx.se/blog/2025/07/12/sponsor-my-laptop/)

## 6 thoughts on “Cybersecurity Risk Assessment Request”

1. ![](https://secure.gravatar.com/avatar/293641f2b3850fcc193294554f5cb61a358fcca74c9053d26aea3a92101cb960?s=34&d=monsterid&r=g) **[Bernd](https://itblog.eckenfels.net)** says:

   [July 11, 2025 at 19:34](https://daniel.haxx.se/blog/2025/07/11/cybersecurity-risk-assessment-request/#comment-27214)

   Having seen many of those requests over the years, I almost can gurantee that such emails are the doing of a not really authorized Analyst or developer, most likely even outsourced, who was tasked to compile the info but took a shortcut.

   1. ![](https://secure.gravatar.com/avatar/b33104dac391c4c76ac4e8e13449636286d0f710c44146282311692ccbb2999b?s=34&d=monsterid&r=g) **dsr** says:

      [July 12, 2025 at 05:16](https://daniel.haxx.se/blog/2025/07/11/cybersecurity-risk-assessment-request/#comment-27216)

      On the contrary, my wife compiles the report for a large but not F500 corporation. It is an annual process which takes several months (because they have so, so many dependencies…) and results in a document vetted by a lawyer. Discovering that they need a license or are otherwise violating the terms of a license is a defect they need to cure.
2. ![](https://secure.gravatar.com/avatar/273b992af6be87f42c417f5bc2e8e2e1547668d9e1d11b22fdf467d252facb62?s=34&d=monsterid&r=g) **Ross** says:

   [July 11, 2025 at 21:18](https://daniel.haxx.se/blog/2025/07/11/cybersecurity-risk-assessment-request/#comment-27215)

   It’s just as likely the request comes from some compliance officer in the company who has one of those notorious checklists they have to complete, but themselves know little to nothing about how most free software projects operate.
3. ![](https://secure.gravatar.com/avatar/946ec3e715a11a47c6e4dcde17567c98009cbb1949d90c49bc2cef431cc466c8?s=34&d=monsterid&r=g) **[Piotr P. Karwasz](https://github.com/ppkarwasz/)** says:

   [July 14, 2025 at 08:36](https://daniel.haxx.se/blog/2025/07/11/cybersecurity-risk-assessment-request/#comment-27218)

   Great post, Daniel!

   I’m especially curious how you’d respond to the question: “Are there any vulnerabilities in the latest version that are not publicly disclosed?” I know some open source projects (like Jetty) offer private notifications about security issues to commercial partners. But in communities like the Apache Software Foundation, that kind of practice is strongly frowned upon.

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [J...