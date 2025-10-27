---
title: Trust in transparency: Private Compute Core
url: http://security.googleblog.com/2022/12/trust-in-transparency-private-compute.html
source: Google Online Security Blog
date: 2022-12-09
fetch_date: 2025-10-04T00:58:40.725549
---

# Trust in transparency: Private Compute Core

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Trust in transparency: Private Compute Core](https://security.googleblog.com/2022/12/trust-in-transparency-private-compute.html "Trust in transparency: Private Compute Core ")

December 8, 2022

Posted by Dave Kleidermacher, Dianne Hackborn, and Eugenio Marchiori

We care deeply about privacy. We also know that trust is built by transparency. This blog, and the technical paper reference within, is an example of that commitment: we describe an important new Android privacy infrastructure called Private Compute Core (PCC).

Some of our most exciting machine learning features use continuous sensing data — information from the microphone, camera, and screen. These features keep you safe, help you communicate, and facilitate stronger connections with people you care about. To unlock this new generation of innovative concepts, we built a specialized sandbox to privately process and protect this data.

## Android Private Compute Core

PCC is a secure, isolated data processing environment inside of the Android operating system that gives you control of the data inside, such as deciding if, how, and when it is shared with others. This way, PCC can enable features like [Live Translate](https://support.google.com/pixelphone/answer/11209263) without sharing continuous sensing data with service providers, including Google.

PCC is part of [Protected Computing](https://blog.google/technology/safety-security/how-we-make-every-day-safer-with-google/)*,* a toolkit of technologies that transform how, when, and where data is processed to technically ensure its privacy and safety. For example, by employing cloud enclaves, edge processing, or end-to-end encryption we ensure sensitive data remains in exclusive control of the user.

## How Private Compute Core works

PCC is designed to enable innovative features while keeping the data needed for them confidential from other subsystems. We do this by using techniques such as limiting Interprocess Communications (IPC) binds and using isolated processes. These are included as part of the Android Open Source Project and controlled by publicly available surfaces, such as Android framework APIs. For features that run inside PCC, continuous sensing data is processed safely and seamlessly while keeping it confidential.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsDlw8jTGTcp5vKnjg5nSbtYI8rQs1dF95BUtciXfDxZ5TYyOoWXXjezrQcC_T6MEJ0SkdGmqkUWqEQUWOvHEJZtS06K_LntdZOlF2_RDbkL0rZS4XqoUBdn_t9y3wMbfrzhdZF3KEDzMml56VxCYhsXfGAuq3kN0OKuG6TTKdqKUqUEQYR9l-KRyxnw/s1600/Screenshot%202022-12-07%207.33.17%20PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsDlw8jTGTcp5vKnjg5nSbtYI8rQs1dF95BUtciXfDxZ5TYyOoWXXjezrQcC_T6MEJ0SkdGmqkUWqEQUWOvHEJZtS06K_LntdZOlF2_RDbkL0rZS4XqoUBdn_t9y3wMbfrzhdZF3KEDzMml56VxCYhsXfGAuq3kN0OKuG6TTKdqKUqUEQYR9l-KRyxnw/s1600/Screenshot%202022-12-07%207.33.17%20PM.png)

To stay useful, any machine learning feature has to get better over time. To keep the models that power PCC features up to date, while still keeping the data private, we leverage [federated learning and analytics](https://federated.withgoogle.com/). Network calls to improve the performance of these models can be monitored using [Private Compute Services](https://play.google.com/store/apps/details?id=com.google.android.as.oss).

## Let us show you our work

The publicly-verifiable architectures in PCC demonstrate how we strive to deliver confidentiality and control, and do it in a way that is verifiable and visible to users. In addition to this blog, we provide this transparency through public documentation and open-source code — we hope you'll have a look below.

To explain in even more detail, we’ve published [a technical whitepaper](https://arxiv.org/abs/2209.10317) for researchers and interested members of the community. In it, we describe data protections in-depth, the processes and mechanisms we’ve built, and include diagrams of the privacy structures for continuous sensing features.

Private Compute Services was recently [open-sourced](https://github.com/google/private-compute-services) as well, and we invite our Android community to inspect the code that controls the data management and egress policies. We hope you'll examine and report back on PCC's implementation, so that our own documentation is not the only source of analysis.

## Our commitment to transparency

Being transparent and engaged with users, developers, researchers, and technologists around the world is part of what makes Android special and, we think, more trustworthy. The paradigm of distributed trust, where credibility is built up from verification by multiple trusted sources, continues to extend this core value. Open sourcing the mechanisms for data protection and processes is one step towards making privacy verifiable. The next step is verification by the community — and we hope you'll join in.

We'll continue sharing our progress and look forward to hearing feedback from our users and community on the evolution of Private Compute Core and data privacy at Google.

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

Labels:

[android](https://security.googleblog.com/search/label/android)
,
[android security](https://security.googleblog.com/search/label/android%20security)
,
[private compute core](https://security.googleblog.com/search/label/private%20compute%20core)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/5206538704090237226)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2022/12/announcing-osv-scanner-vulnerability.html "Newer Post")

[**](https://security.googleblog.com/2022/12/enhanced-protection-strongest-level-of.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [#sharethemicincyber](https://security.googleblog.com/search/label/%23sharethemicincyber)
* [#supplychain #security #opensource](https://security.googleblog.com/search/label/%23supplychain%20%23security%20%23opensource)
* [AI Security](https://security.googleblog.com/search/label/AI%20Security)
* [android](https://security.googleblog.com/search/label/android)
* [android security](https://security.googleblog.com/search/label/android%20security)
* [android tr](https://security.googleblog.com/search/label/android%20tr)
* [app security](https://security.googleblog.com/search/label/app%20security)
* [big data](https://security.googleblog.com/search/label/big%20data)
* [biometrics](https://security.googleblog.com/search/label/biometrics)
* [blackhat](https://security.googleblog.com/search/label/blackhat)
* [C++](https://security.googleblog.com/search/label/C%2B%2B)
* [chrome](https://security.googleblog.com/search/label/chrome)
* [chrome enterprise](https://security.googleblog.com/search/label/chrome%20enterprise)
* [chrome security](https://security.googleblog.com/search/label/chrome%20security)
* [connected devices](https://security.googleblog.com/search/label/connected%20devices)
* [CTF](https://security.googleblog.com/search/label/CTF)
* [diversity](https://security.googleblog.com/search/label/diversity)
* [encryption](https://security.googleblog.com/search/label/encryption)
* [federated learning](https://security.googleblog.com/search/label/federated%20learning)
* [fuzzing](https://security.googleblog.com/search/label/fuzzing)
* [Gboard](https://security.googleblog.com/search/label/Gboard)
* [google play](https://security.googleblog.com/se...