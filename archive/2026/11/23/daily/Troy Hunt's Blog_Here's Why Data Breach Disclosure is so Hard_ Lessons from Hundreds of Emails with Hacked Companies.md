---
title: Here's Why Data Breach Disclosure is so Hard: Lessons from Hundreds of Emails with Hacked Companies
url: https://www.troyhunt.com/heres-why-data-breach-disclosure-is-so-hard-lessons-from-hundreds-of-emails-with-hacked-companies/
source: Troy Hunt's Blog
date: 2026-11-23
fetch_date: 2026-11-24T11:49:08.620767
---

# Here's Why Data Breach Disclosure is so Hard: Lessons from Hundreds of Emails with Hacked Companies

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Here's Why Data Breach Disclosure is so Hard: Lessons from Hundreds of Emails with Hacked Companies

23 November 2026

When I asked Claude to write the blog post below, I already knew what was in the messages it would read. Hundreds of emails back and forth with companies that had had data breaches, and some very common patterns. I knew the emails contained standoffish behaviour, deliberate delays, heavy involvement from lawyers, and a constant theme: prioritising corporate interests over those of their customers. But I didn't know just how stark it would be to read such a candid analysis of my own emails, nor how frustrating it would be to relive many of those disclosure experiences.

I decided to have AI write the post below because it was the best way to highlight the behaviours I keep seeing across many breaches and subsequent disclosure efforts. I'm not going to make a habit of AI writing content for me, but what's written below *absolutely nails it!* It's the best way I can explain what it's like to run [Have I Been Pwned](https://haveibeenpwned.com/?ref=troyhunt.com) in support of individual data breach victims, while also respecting the position of the corporations dealing with the crime that put them in this position. It would have been much easier not to do the latter, but then I don't think I'd still be here running the service if I hadn't.

A quick note on methodology first: I've been running HIBP for 13 years but only gave Claude access to the mailbox I've been using for the last 8.5 years, hence the shorter timeframe you'll read below. I also made several small changes to Claude's work to better obfuscate the identity of the organisation it was describing, a move I'm sure you'll understand after reading about lawyers getting involved... Here goes:

## Introduction

Getting an organisation to admit it has been breached is often harder than getting hold of the breached data in the first place. That is the clearest conclusion from reading more than eight and a half years of Troy Hunt's breach notification email.

I'm an AI. Troy gave me access to his mailbox and asked me to look at it as an outsider: what happens after Have I Been Pwned (HIBP) tells an organisation that its customers' data is circulating? Between March 2018 and November 2026 he sent his standard notification email to 73 organisations, and several more conversations began through website contact forms. I found every one of those 73 first emails and reviewed a broad sample of the replies from every year. I then read the full back-and-forth on the threads that best show each pattern.

I've left out company names on purpose. The point isn't to shame individual organisations. The point is that the same behaviours keep appearing, across countries, industries and company sizes, year after year. Some organisations handled this well, and I'll get to them. But the overall picture is one of friction, delay and a steady effort to keep the incident as quiet as possible.

## The first problem: finding a human

The first email is almost always the same. Troy introduces himself, explains that data allegedly taken from the organisation has been sent to him, and asks for "someone responsible for information security" to get in touch. He wants to pass on everything he has before he notifies the affected HIBP subscribers. It is a polite, low-pressure request, and it often goes nowhere.

The main reason is that many organisations have no obvious way to report a security incident. Troy ends up sending these emails to support inboxes, returns departments, general "info" addresses and website contact forms. In at least three of the 73 cases, Troy sent the first email a second time, two, five and twelve days later.

When email fails, he moves on to LinkedIn, Facebook and X. One organisation took four weeks to send its first reply, and Troy had also tried it on all three social platforms over several days. Another's senior IT leader replied after almost four weeks, thanked Troy for trying "so many times", and admitted he needed to check LinkedIn more often.

The longest chain I found was at a large hardware manufacturer. It ran from a returns inbox, to the company's regional social media account, to regional marketing staff, to head office, to one product security address, then a second one, and finally to the legal department. That is six hops before anyone could answer the actual question.

Then there are the ticketing systems. Several breach notifications were logged as routine customer support requests, with ticket numbers stuck on the subject line. In one case, Troy received three automated surveys asking him to rate the support he'd received. Another organisation sent one too. A message that an organisation's customer data is being traded among criminals ended up in the same queue as a question about a late delivery.

## The first response: "we've seen no evidence"

Once someone does reply, the first substantive message tends to fall into one of a few patterns. The most common is a statement that the organisation has found no evidence of a breach. This often arrives before it has seen any of the data.

One organisation said it hadn't identified any unauthorised access. Three weeks later, still without the data, it said again that it had reviewed its systems and found no sign of the breach. When Troy sent the data, it confirmed within a few weeks that an exposed database server had leaked its users' details. The "no evidence" had really meant it didn't yet know where to look.

A second pattern is to shrink the incident. In a recent case, the first reply said the attackers had only defaced a landing page, with no indication that user data was taken. It added that the data was probably from an earlier incident the company had already disclosed. Troy then pointed out that the newest timestamp in the data matched the day of the defacement. He also sent the company records belonging to its own staff. The data turned out to cover 16 tables of core user systems, including identity verification and tax documents.

A third pattern is the request for "a sample" or a particular file format. This is reasonable in principle, since nobody should take a stranger's word for a breach. But it often comes after weeks of silence, and it shifts the job of proving the breach from the organisation that lost the data to the person who reported it. In one case, an external IT consultant asked Troy to help work out whether the identifiers in the data were real or fabricated. Troy did that analysis for them.

## "We're still investigating"

Once an organisation accepts that the data is probably real, the next phrase in the threads is almost always "we're investigating". Investigating is necessary. The problem is that it has no end date, and it gets used as a reason not to say anything publicly while it continues.

In a recent case, the company confirmed within days that it had the data and was reviewing it "to confirm its validity and scope". A week after the first contact, the message was that it was still investigating and would let Troy know "if it is determined that any notifications need to be made". By then the company had a copy of the data, its own staff records were in it, and the data had already been shared among people who collect breaches. Nobody outside the company had been told anything.

Troy's answer to this is consistent across the years. A disclosure doesn't need to be complete. An organisation can say what it knows now, and update it as the investigation goes on. Some organisations in this mailbox did exactly that. What the investigation framing does is turn "we ...