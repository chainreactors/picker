---
title: The State of Data Breaches, Part 2: The Trilogy of Players
url: https://www.troyhunt.com/the-state-of-data-breaches-part-2-the-trilogy-of-players/
source: Troy Hunt's Blog
date: 2024-07-01
fetch_date: 2025-10-06T17:42:10.034016
---

# The State of Data Breaches, Part 2: The Trilogy of Players

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# The State of Data Breaches, Part 2: The Trilogy of Players

01 July 2024

Last week, I wrote about [The State of Data Breaches](https://www.troyhunt.com/the-state-of-data-breaches/) and got loads of feedback. It was predominantly sympathetic to the position I find myself in running HIBP, and that post was mostly one of frustration: lack of disclosure, standoffish organisations, downplaying breaches and the individual breach victims themselves making it worse by going to town on the corporate victims. But the other angle that's been milling around in my brain is the one represented by the image here:

![](https://www.troyhunt.com/content/images/2024/06/ezgif-7-1be934c9f0.jpg)

Running HIBP has become a constant balancing act between a trilogy of three parties: hackers, corporate victims and law enforcement. Let me explain:

### Hackers

This is where most data breaches begin, with someone illegally accessing a protected system and snagging the data. That's a high-level generalisation, of course, but whether it's exploiting software vulnerabilities, downloading exposed database backups or phishing admin credentials and then grabbing the data, it's all in the same realm of taking something that isn't theirs. And sometimes, they contact me.

This is a hard position to find myself in, primarily because I need to weigh the potentially competing objectives of notifying impacted HIBP subscribers whilst simultaneously not pandering to the perverse incentives of likely criminals. Sometimes, it's easy: when someone reports exposed data or a security vulnerability, the advice is to contact the company involved and not turn it into a data breach. But when they already *have* the data, by definition it's now a breach and inevitably a bunch of my subscribers are in there. It's awkward, talking to the first party responsible for the breach.

There are all sorts of circumstances that may make it even more awkward, for example if the hacker is actively trying to shake the company down for money. Perhaps they're selling the data on the breach market. Maybe they also still have access to the corporate system. Having a discussion with someone in that position is delicate, and throughout it all, I'm conscious that they may very well end up in custody and every discussion we've had will be seen by law enforcement. Every single word I write is predicated on that assumption. And eventually, being caught is a very likely outcome; just as we say that as defenders we need to get it right every single time and the hacker only needs to get it right once, as hackers, they need to get their opsec right every single time and it only takes that one little mistake to bring them undone. A dropped VPN connection. An email address, handle or password used somewhere else that links to their identity. An incorrect assumption about the anonymity of cryptocurrency. One. Little. Mistake.

However, I also need to treat these discussions as confidential. The expectation when people reach out is that they can confide in me, and that's due to the trust I've built over more than a decade of running this service. Relaying those conversations without their permission could destroy that reputation in a heartbeat. So, I often find myself brokering conversations between the three parties mentioned here, providing contact details back and forth or relaying messages with the consent of each party.

This sort of communication gets messy: you've got the hacker (who's often suspicious of big corp) trying to draw attention to an issue, but they're trying to communicate with a party who's also naturally suspicious of anonymous characters who've accessed their data! And law enforcement is, of course, interested in the hacker because that's their job, but they're also respectful of the role I play and the confidence with which data is shared with me. Meanwhile, law enforcement is also often engaged by the corporate victim and now we've got all players conversing with each other and me in the middle.

I say this not to be grandiose about what I do, but to explain the delicate balance with which many of these data breaches need to be handled. Then, that's all wrapped in with the observations from the previous post about lack of urgency etc.

### Corporate Victims

I choose to use this term because it's all too easy for people to point at a company that's suffered a data breach and level blame at them. Depending on the circumstances, some blame is likely warranted, but make no mistake: breached companies are usually the target of intentional, malicious, criminal activity. And when I say "companies", we're ultimately talking about individuals who are usually doing the best they can at their jobs and, during a period of incident response, are often having the worst time of their careers. I've heard the pain in their voices and seen the stress on their faces on so many prior occasions, and I want to make sure that the human element of this isn't lost amidst the chants of angry customers.

The way in which corporate victims engage with hackers is particularly delicate. They're understandably angry, but they're also walking the tightrope of trying to learn as much as they can about the incident (the vector by which data was obtained often isn't known in the early stages), whilst listening to often exorbitant demands and not losing their cool. It's *very* easy for the party who has always worked on the basis of anonymity to simply "go dark" and disappear altogether, and then what? We can see this balancing act in many of the communications later released by hackers, often after they've failed to secure the expected ransom payment; you have *extremely* polite corporations... who you know want nothing more than to have the guy thrown into prison!

The law enforcement angle, or perhaps, to put it more broadly, the interactions with government authorities in general, is an interesting one. Beyond the obvious engagements around the criminal activity of hackers, the corporate victims themselves have legal responsibilities. This is obviously highly dependent on jurisdiction and regulatory controls, but it may mean reporting the breach to the appropriate government entity, for example. It may even mean reporting to *many* government entities (i.e. state-based) depending on where they are in the world. Then there's the question of their own culpability and whether the actions they took (or didn't take) both pre and post-breach may result in punitive measures being taken. I had a headline in the previous post that included the term "covering their arses" and this doesn't just mean from customer or shareholder backlash, but increasingly, from massive corporate fines.

I suspect, based on many previous experiences, that corporations have a love-hate relationship with law enforcement. They obviously want their support when it comes to dealing with the criminals, but they're *extraordinarily* cautious about what they disclose lest it later contribute to the basis on which penalties are levelled against them. Imagine the balancing act involved when the corporate victims suspects the breach occurred due to some massive oversights on their behalf and they approach law enforcement for support: "So, how do you think they got in? Uh..."

Like I've already said so many times in this post: "delicate".

### Law Enforcement

This is the most multidimensional player in the trilogy, interfacing backwards and forwards with each party in various ways. Most obviously, they're there to bring criminals to justice, and that clearly puts hackers well within their remit. I've often referred to "the FBI and friends" ...