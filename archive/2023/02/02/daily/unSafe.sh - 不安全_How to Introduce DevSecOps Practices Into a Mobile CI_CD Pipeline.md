---
title: How to Introduce DevSecOps Practices Into a Mobile CI/CD Pipeline
url: https://buaq.net/go-147551.html
source: unSafe.sh - 不安全
date: 2023-02-02
fetch_date: 2025-10-04T05:28:04.559703
---

# How to Introduce DevSecOps Practices Into a Mobile CI/CD Pipeline

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/de6410ecee901123adcd9fa854bb1857.jpg)

How to Introduce DevSecOps Practices Into a Mobile CI/CD Pipeline

The consequences of a mobile application security issue can be detrimental, and mobile teams must p
*2023-2-1 20:30:0
Author: [www.nowsecure.com(查看原文)](/jump-147551.htm)
阅读量:28
收藏*

---

The consequences of a mobile application security issue can be detrimental, and mobile teams must prepare for everything from third-party bugs to cloud security issues and beyond. However, [NowSecure MobileRiskTracker](https://mobilerisktracker.nowsecure.com/#7992b51e-79d3-437b-80e6-c9f51b6d82b7) data finds that a shocking 85% mobile apps found in the Apple App Store and Google Play contain security and privacy issues.

## Work With CI/CD Pipelines for Mobile Apps

Before we get into DevSecOps best practices, let’s introduce DevOps and the use of CI/CD  (continuous integration/ continuous deployment) pipelines for mobile apps. DevOps best practices help mobile engineers to **optimize workflows** and practices to **improve release cadence**, **optimize development cycles**, and more.

With [Mobile DevOps](https://bitrise.io/why/features/mobile-devops) and mobile CI/CD pipelines, mobile engineers can manage workflows, run mobile builds, and release faster and better mobile apps. A mobile CI/CD pipeline could include [steps and workflows for mobile engineers](https://bitrise.io/why/features/steps-and-workflows) to set up environments, perform UI and unit testing, deploy to app stores, and more. The goal of mobile CI/CD pipelines is to provide a frictionless experience for the developers and engineers who build mobile apps, while remaining safe and secure.

There are platforms like Bitrise — a fully-hosted [Mobile DevOps](https://bitrise.io/why/features/mobile-devops) and CI/CD platform — that are **specifically designed for mobile apps**. Bitrise helps mobile engineers build, test, and release [iOS](https://bitrise.io/why/technologies/ios-continuous-integration), [Android](https://bitrise.io/why/technologies/android-continuous-integration), and cross-platform apps with third-party integrations with mobile tooling. These processes are often different and more complex than building traditional web apps.

## Think Like a Mobile Attacker

In order to address mobile app security, you need to know what you’re protecting against. As Brian mentioned in the webinar, there are five main targets that mobile attackers are interested in:

1. Credentials
2. Personal data
3. Financial account data
4. Access to the backend system
5. Trade secrets

“As a mobile app developer, it’s your responsibility to write secure code and test that code to ensure proper protections are in place.” advises Reed.

When it comes to mobile app security, you need to think like a mobile attacker because [mobile apps have unique security challenges](https://discover.nowsecure.com/c/web-vs-mobile-app-security-testing-tools?x=9z-j5n#page=1) that web apps don’t often face. For instance, mobile apps have a broader attack surface than web apps do. And, mobile apps tend to strive for shorter release cycles with speed and frequency in mind, which can introduce security challenges. Getting inside the mind of a mobile attacker allows you to reverse engineer potential threats and prioritize security.

## Share the Responsibility for Mobile Security

Mobile teams should adopt the **“everyone is responsible for security**” mindset by sharing security responsibilities across teams and injecting security checks earlier in the app lifecycle.

### Shift-left Testing

Mobile apps should be tested **early and often**. It helps mobile teams to fail fast and learn early to save production and development time. **Shift-left testing** involves moving mobile testing to the left in the delivery pipeline — in other words, testing the software earlier in the development lifecycle than is historically typical.

“It’s really important nowadays to get quick feedback,” says Megremis. “We should add security tests and get a security report in the early stages to understand that code has something that could cause a high-security vulnerability. That’s the whole point of DevOps.”

### Balance Security and Speed

**The DevSecOps** framework expands the impact of DevOps by adding security practices to the software development and delivery process. It also resolves the tension between [Mobile DevOps](https://bitrise.io/why/features/mobile-devops) teams that want to release software quickly and security teams that prioritize security over all else.

![](https://lh5.googleusercontent.com/gQIqmLvVjuWIgr3iddigRdvvs_Ax7I3ns131rYH7KJf28UWsjfS8RH1pQ0CdeRMh2n5tDReZEm-ytQf8yUgWK5XNYDBUVODWOMgeWM2hAfYUFC0Bw-CUVQrqkWDM-dyRreTqZJ9MK4Mb1gefvMaiPXU)

Alt: Creating a DevSecOps strategy involves finding the right balance between app quality, security, and speed of development. Teams need to iterate quickly while remaining secure.

“If both security and development teams have a ‘what’s best for the business’ mindset, then they are more likely to be in sync throughout processes,” says Reed.

## Choose a Suitable Security Testing Method

A successful mobile testing program includes aspects of the following four security testing methods.:

1. **Look for coding errors with Static App Security Testing (SAST):** Analyze application source code to test for a range of known security vulnerabilities.
2. **Run the application and monitor for security defects with Dynamic App Security Testing (DAST):** Analyze by physically running the app to test for a range of known security vulnerabilities.
3. **Collect security telemetry with Interactive App Security Testing (IAST):** Insert security libraries/services into the app to analyze the application as it runs during dev, test, and/or production.
4. **Test back-end APIs with API Security Testing (APISec):** Probing backend API endpoints and services to find security vulnerabilities.

> The goal of mobile CI/CD pipelines is to provide a frictionless experience for the developers and engineers who build mobile apps, while remaining safe and secure.

## Introduce DevSecOps Practices in your Mobile CI/CD Pipeline

By introducing these DevSecOps best practices into your [mob](https://bitrise.io/blog/post/mobile-ci-cd-a-noobs-guide-for-mobile-app-developers)[i](https://bitrise.io/blog/post/mobile-ci-cd-a-noobs-guide-for-mobile-app-developers)[le CI/CD](https://bitrise.io/blog/post/mobile-ci-cd-a-noobs-guide-for-mobile-app-developers) pipelines, you address mobile threats while releasing with speed and efficiency.

### Standardize Policies

Establish a set of written policies for security and development teams to follow. These policies should establish SLAs that determine how PMs write, how architects design, how developers code, etc. Follow industry standards like [OWASP MASVS](https://owasp.org/www-project-mobile-app-security/) to set policies that meet security requirements.

**💡TIP:** Deploy a policy engine in your mobile pipeline to automate controls. It helps streamline and automate policies, so developers get requirements that are automatically tested based on policy.

### Provide Security Training for Employees

Continuous security training helps developers address app store updates, language updates, and the rapidly changing mobile landscape. Proactive security training helps developers write more secure code. Security training should be role-based and should focus on mobile app security, leveraging OWASP MASVS.

### Set Security Requirements

Security requirements help address vulnerabilities. Make sure to treat security requirements lik...