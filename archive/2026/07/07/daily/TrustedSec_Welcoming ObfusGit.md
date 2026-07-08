---
title: Welcoming ObfusGit
url: https://trustedsec.com/blog/welcoming-obfusgit
source: TrustedSec
date: 2026-07-07
fetch_date: 2026-07-08T05:05:17.648206
---

# Welcoming ObfusGit

[Skip to Main Content](#main)

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Welcoming ObfusGit](https://trustedsec.com/blog/welcoming-obfusgit)

July 07, 2026

# Welcoming ObfusGit

Written by
Kevin Haubris

Artificial Intelligence (AI)
Demo

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/WelcomeObfusgit_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1783429855&s=9b7d73d78b292c7e4664edfb9d12728a)

Table of contents

* [How to Use](#How)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#211e5254434b4442551c624944424a0413114e54550413115549485204131140535548424d4404131147534e4c0413117553545255444572444204131007404c511a434e45581c76444d424e4c484f460413116e434754526648550412600413114955555152041260041367041367555354525544455244420f424e4c041367434d4e4604136756444d424e4c484f460c4e43475452464855 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwelcoming-obfusgit "Share on Facebook")
* [Share on X](https://twitter.com/share?text=Welcoming%20ObfusGit%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwelcoming-obfusgit "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwelcoming-obfusgit&mini=true "Share on LinkedIn")

###### Ever want to share your code online but wanted to keep AI companies and other mass consumers of online source code from being able to easily scrape your code to train their models or know what the code really has in it?

Well, if you answered yes to either of those, I got the project for you!

ObfusGit is a basic python script that allows you to set up a local repo and commit to it as usual, then you can run “obfusgit sync” and you have a fully encrypted/encoded copy of your repo you can just push up to a public location.

## Why Does This Exist?

A coworker and I were joking one day about how to obfuscate public repos to make it more difficult for scrapers from knowing what’s in the codebase. I thought that this would be pretty easy. So easy, in fact, a local LLM could do it. So, I decided that I would give it the requirements with basic specs and see what happens. An hour later, we have a basic python script that achieves most of the goals. Basically, you use your Git repo as is, then once you decide you want to push it out to the public, you can just run `obfusgit setup-repos --privateRepo /path/to/repo/ --encryptionKey YourSharedKey`. This will then set up the repo with a copy of obfusgit in the root directory and the public repo folder,`.obfusgit-public`, that you can add remote origin and push from, and the config file with your encryption key. Once uploaded, someone can just clone the repo and run `obfusgit reverse-repos --publicRepo /path/to/clonedRepo/ --privateRepoName clonedRepo_Plaintext --encryptionKey YourSharedKey` and boom! That folder will be created and you will be able to see the actual project code.

## How to Use

There are three steps you first need to setup the repo, you do this by running setup-repo pointing at a Git repo. This sets up the Git hooks and copies obfusgit.py to the base directory. You also need to have python3 installed, because the Git hook calls the obfusgit script with python3 every commit.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/WelcomeObfusGit_Haubris/Fig01_Haubris_ObfusGit.png?w=320&q=90&auto=format&fit=max&dm=1782845002&s=aa60cf9d2ec914f4d659dfafabe36a9c)

Figure 1 - Example of Setup

Once that’s done, you can set the remote origin for the public repo in `.obfusgit-public/` and push up. Then, you can clone it down like simulated here. One thing to note is that if you setup-repos in an in-use repository, you need to run “sync” once after setup to get the public repo setup.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/WelcomeObfusGit_Haubris/Fig02_Haubris_ObfusGit.png?w=320&q=90&auto=format&fit=max&dm=1782845004&s=d65b7e0b5c9eac6cab5632c24a2e1fd2)

Figure 2 - Example Cloning repo and Showing Obfuscated Content

Once cloned, you obviously can’t see the actual contents. to reverse it back to plaintext, you just run “reverse-repos” like below.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/WelcomeObfusGit_Haubris/Fig03_Haubris_ObfusGit.png?w=320&q=90&auto=format&fit=max&dm=1782845005&s=d5a8dbfbc3143b01488d8235c4fad948)

Figure 3 - Example of Reversing the repo Back to Plaintext

The final piece of this is to figure out how to distribute the encryption key that you setup. This will have to be an accompanying blog post, Tweet, or something accessible, but not directly from the Git repo.

## Conclusion

Please keep in mind that ObfusGit was built quickly using a local AI model and has only been quickly tested so don’t be surprised if there are issues. Additi...