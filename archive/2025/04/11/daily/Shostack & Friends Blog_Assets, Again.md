---
title: Assets, Again
url: https://shostack.org/blog/assets-again/
source: Shostack & Friends Blog
date: 2025-04-11
fetch_date: 2025-10-06T22:05:19.998662
---

# Assets, Again

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
* [Services](/training/)
  + [Training](/training/)
  + [Accelerator](/secure-design-accelerator/)
  + [Expert Witness](/expert-witness/)
  + [Consulting](/consulting/)
* [Resources](/resources/)
  + [Overview](/resources/)
  + [Threat Modeling](/resources/threat-modeling/)
  + [Books](/books/)
  + [Games](/tm-games/)
  + [Cyber Public Health](/resources/cyber-public-health/)
  + [Lessons Learned](/resources/lessons/)
  + [Videos](/resources/videos/)
  + [Whitepapers](/resources/whitepapers/)
* [Blog](/blog/)
* [Contact](/contact/)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. Assets, Again

Shostack + Friends Blog

# Assets, Again

What's wrong with this process?
![A random dataflow diagram sort of thing](/images/blog/img/2025/random-dfd-1-1000w.png)

Appsec leaders come to me all the time, looking for feedback on their threat modeling approach. A recent request exemplified a couple of the problems that we see over and over:

> The system model provides a framework for identifying and analyzing potential threats by thoroughly describing the assets, attributes, and their interactions within the information system. These assets include infrastructure, software, protocols, and data storage, among others.
>
>
> [...] Identify and classify the organization's assets, including network devices, servers, endpoints, and applications. Explore the key functions of each asset and understand their roles in the organization's business processes.

In [Threat Modeling](https://shostack.org/books/threat-modeling-book), I talk about there being three types of assets: things you want to protect, things attackers care about, and stepping stones. I talk — at length — about why the term asset doesn’t help us threat model. This approach magnifies those problems, and adds more.

* Why are “protocols” assets?
* What sort of “classification” is involved, and what goal does it serve?
* Why is “infrastructure” an “assets?” Can’t we have the ops team threat model it and assume that it works, especially when we’re talking about the business processes?
* In the second list, can’t you just say “computers and applications?” What does jargoning it up as “assets” do for you?
* Why do you need to understand the functions or the business process at this stage? (Not saying you don’t, I’m saying that you need to justify it.)

What’s more, what’s the value of ‘thoroughness?’ How thorough do we need to be?

These problems are addressed by starting with the question “what are we working on?” If you’re not working on infrastructure... you don’t need to ask questions about it. That’s someone else’s job and threat model. If you’re not working on the whole organization, you don’t need to identify all its assets and go develop and understanding of them...

By the way folks, I can’t do these for the whole world as a hobby project. When we do it for a customer, the request and response are private, and when they're not, sometimes they end up in the blog. If you’d like my team to do a review, please get in touch using the [contact us](https://shostack.org/contact) form. Be warned: our rabid sales team will never stop calling (unless you ask them to).

Originally published by Adam on 10 Apr 2025

Categories:
  [threat modeling](/blog/category/threat-modeling)
  [threat model thursday](/blog/category/threat-model-thursday)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling/)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder/)

[Other Star Wars blog posts](/blog/category/star-wars/)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives/)

[Doing science with near misses](/blog/doing-science-with-near-misses/)

[Posts about Adam’s “Threats” book](/blog/category/threats-book/)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book/)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school/)

[About this blog](/blog/about/)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read/).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact/) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![a photograph of a robot, sitting in a library, working on a jigsaw puzzle](/images/blog/img/2025/appsec-roundup-aug-2025-175w.png)](/blog/appsec-roundup-sept-2025/)

### [Secure By Design roundup - September 2025](/blog/appsec-roundup-sept-2025/)

01 Oct 2025

The secret service, the CSRB, the CMMC, Sept was pretty busy in government. Plus Apple's Memory Integrity and a nice short paper on prompt-based attacks.

[![Thumbnail for podcast episode](/images/blog/img/2025/medtech-innovation-podcast-175w.png)](/blog/medtech-innovation-podcast/)

### [Adam Featured on Inside MedTech Innovation](/blog/medtech-innovation-podcast/)

29 Sep 2025

Learn from the past and advance your threat modeling skills!

[![A moon buggy model at the Museum of Flight](/images/blog/img/2025/moon-buggy-museum-of-flight-175w.png)](/blog/lunar-rover-vehicle-redux/)

### [Lunar Rover Vehicle, Redux](/blog/lunar-rover-vehicle-redux/)

17 Sep 2025

What can the moon buggy teach us about modeling?

[![Astronaut Jim Irwin in front of Apollo 15 and a moon rover](/images/blog/img/2025/as15-88-11866-signed-175w.jpeg)](/blog/apollo-15-lrv-boeing/)

### [Apollo 15 Lunar Rover Vehicle](/blog/apollo-15-lrv-boeing/)

15 Sep 2025

What can a signed Apollo 15 print teach us about modern threat modeling and risk management?

## Popular Blog Topics

[Threat Model Thursday](/blog/category/threat-model-thursday/),
exploring specific published threat models

[Threat Modeling](/blog/category/threat-modeling/) (general topic)

[Application Security](/blog/category/application-security/)

[Software Engineering](/blog/category/software-engineering/)

[Cloud Security](/blog/category/cloud-security/)

[Compliance](/blog/category/compliance/)

[AI](/blog/category/ai/) + [ChatGPT](/blog/category/chatgpt/)

[Privacy](/blog/category/privacy/) + [Personal Security](/blog/category/personal-security/)

[Research](/blog/category/research-papers/) + [Reports](/blog/category/reports-and-data/)

[Book Reviews](/blog/category/book-reviews/)

[News](/blog/category/news/)

[Podcasts](/blog/category/podcasts/), [Videos](/blog/category/videos/) + [Webinars](/blog/category/webinars/)

Our site works best with Javascript enabled, however we have done our best to minimize any negative impacts to your experience without it.

* [Shostack on LinkedIn](https://www.linkedin.com/in/shostack/)
* [Shostack on Github](https://github.com/adamshostack/)
* [Stostack Videos on YouTube](https://youtube.com/c/shostack)
* © 2021-2025 Shostack + Associates  |  [Privacy Policy](/privacy-policy/)
* [Contact Shostack and Associates](/contact/)
* Call +1 866-APP-SECURE
* [Sitemap](/sitemap/)