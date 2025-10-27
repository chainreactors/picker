---
title: So, you want to get into bug bounties?
url: http://shubs.io/so-you-want-to-get-into-bug-bounties/
source: Shubham Shah
date: 2022-11-27
fetch_date: 2025-10-03T23:53:17.758842
---

# So, you want to get into bug bounties?

[![shubs](https://shubs.io/content/images/2025/01/1689076935525.jpeg)](https://shubs.io)

# [shubs](https://shubs.io)

Co-founder of Assetnote, security researcher.

###### [Assetnote](https://assetnote.io/)

###### [Home](https://shubs.io/)

###### [Github](https://github.com/infosec-au)

###### [Twitter](https://twitter.com/infosec_au)

###### [LinkedIn](https://www.linkedin.com/in/shubhamshah/)

# So, you want to get into bug bounties?

November 26 2022

I've been doing bug bounties for over 10 years now and over time, I have grown fonder of the life changing effects it has had for me. From job prospects, to being able to financially support those around me and myself. I believe that if you're passionate about information security and you take pride in your work, you can also find success in bug bounties, and hopefully it causes a ripple of positivity in your career and life.

I'm writing this blog post because I genuinely believe that hard work and a dedication to learning will lead you to success in bug bounties. Additionally, I am eternally grateful for the number of free resources that I have relied on to teach myself the skills to be good at bug bounties. I hope that this blog post explains the many learnings I have had over the last ten years.

---

# What is this guide, and why should I listen to you?

This guide is not necessarily going to give you a blueprint of exactly what you need to learn and when. I want this guide to be a realistic understanding of what it is like to be a bug bounty hunter and what it involves in order to be successful. The learning journey that will make you successful in bug bounties can be different for everyone.

There are a lot of things I've worked out regarding being a successful bug bounty hunter that I wanted to communicate to the broader community. Some of these things may seem obvious to seasoned bug bounty hunters, but this guide is really for those who love the idea of being a bug bounty hunter, but may not understand what it involves and how to find success.

For those looking for structured learning, I recommend checking out [PentesterLab](https://pentesterlab.com/?ref=shubs.io) and [Web Security Academy](https://portswigger.net/web-security?ref=shubs.io). Most importantly, I recommend you spend as much time actually hacking, because it is not time wasted even if you do not find any valid issues. Every failure is a learning experience. You will eventually find security vulnerabilities.

As for why you should listen to me, as I've mentioned earlier, I've been doing bug bounties for just over ten years now. My first bug I got paid for was an SSRF vulnerability in PayPal. Back then, bug bounty platforms did not really exist and no real community existed. At that time, I was working at a fast food restaurant for $6.50 an hour. The first bug bounty payout I received was more than I had made after working for eight months. It changed my life, and I think it has the power to change other peoples lives too.

I'm [ranked #1 in Australia](https://hackerone.com/leaderboard/country?year=2022&ref=shubs.io) (for the last two years) on HackerOne, and [ranked about #30](https://hackerone.com/leaderboard/all_time_reputation?ref=shubs.io) in the world on HackerOne (all time leaderboard). Over the years I have done bug bounties as a hobby in my free time, but also spent some time doing it full time.

---

# Fundamentals

In my opinion, in order to be successful at bug bounties, you do not need to be an excellent programmer, or know how everything works down to the most granular level. This can of course be an advantage if you have this knowledge, but I do not believe that you need to spend years studying before you can get your feet wet in bug bounties.

The truth is, most bug bounty hunters are interacting with so many assets and technologies, that it is near impossible to understand the intricacies of each of them before you start hunting. The good news is, if you're curious and open to learning, you can build up your knowledge and skills as you are hunting for vulnerabilities.

I do encourage that you learn how to build, not just break things. This can be a major advantage in bug bounties as it allows you to potentially better understand how systems are built, so you can formulate attacks to break them. But, I am aware of many hackers that have never written a single line of code and are some of the best hackers in our industry and community. Hence, for some people this is not necessary.

Having experience in engineering can sometimes be a double-sided sword as you may make assumptions or have cognitive biases as to how something works, preventing you from testing certain things in some scenarios. If you are an engineer or have an engineering background and are reading this, I urge you to always challenge your assumptions when participating in bug bounties.

---

# I'm xyz, can I do bug bounties?

The best thing about bug bounties is that they are accessible to everyone. Whether you're a budding engineer that is looking for a hobby, to a teenager that is interested in offensive security.

If you're reading this and you're a pentester who has worked on web application security, let me tell you that your application security skills that you have applied in your day to day job are extremely relevant in bug bounties. Bug bounties may seem daunting to you because there is often so much to look at, but the skill of recon is just like any other skill that you can hone. Doing bug bounties may not only bring in some extra cash, but it will most definitely also make you better at your job.

If you're reading this and you're an engineer who has made web applications before, the great news is that you understand a lot of the basic knowledge required to dive right in. It's likely that you will have to pick up some application security skills and concepts, but for most engineers, they find this quite fun and exciting to learn about. Doing bug bounties and learning more about application security will most definitely make you a better engineer (releasing code with less security issues) and you might have some fun looking for bugs as well.

And lastly, if you're reading this and you don't have much engineering or security experience but really love the idea of bug bounties, all I can say is that the most important skill you can have in bug bounties is your mindset, which if you work on, you will also be successful. This blog post later discusses what this mindset looks like. There can be a lot of pre-requisite knowledge you will need to find your first bug, but if you are persistent and willing to learn, it is not out of reach. The road to success is paved with failure.

---

# Mindset

Vulnerabilities exist everywhere. That may be depressing to realise, but it is an important point. In society, companies advertise how excellent their security is all the time. This builds a perception to most people that these companies are actually secure, even if they may not be.

If someone came up to you and asked you if you could find a security vulnerability in Facebook or Google, your knee-jerk reaction may be to explain how hard that would be because of how much money these companies spend on security and how many staff they have securing their applications.

As a bug bounty hunter, you cannot have this mentality. It is extremely prohibitive, and as you find yourself finding security issues in the largest corporations in the world, you will soon realise that it is possible to find vulnerabilities in anything (given enough time and resources).

What you may find is that some companies are harder to find vulnerabilities in (how long it takes to find security issues), and you may give up before you find anything, but you need to understand that there are still vulnerabilities yet to be found for any attack surface.

The other quality I have found that leads to consistent results, is persistence. Being persistent in looking for and exploiting ...