---
title: Smashing Security podcast #470: This AI security flaw might be impossible to fix
url: https://grahamcluley.com/smashing-security-podcast-470/
source: GRAHAM CLULEY
date: 2026-06-03
fetch_date: 2026-06-04T06:32:24.391376
---

# Smashing Security podcast #470: This AI security flaw might be impossible to fix

[Skip to content](#content)

[

](/wp-content/uploads/2026/01/graham-cluley-reel.mp4)

[CHECK AVAILABILITY](/#form "Hire cybersecurity expert Graham Cluley to speak at your event")

[GRAHAM CLULEY](https://grahamcluley.com/)

Cybersecurity keynote speaker

×

[Graham Cluley](/ "Graham Cluley")

[Speaking](/ "Speaking")  ⦁  [Writing](/writing/ "Writing")  ⦁  [Podcast](/podcasts/ "The Smashing Security podcast")  ⦁  [Contact](/contact/ "Contact Graham Cluley")  ⦁  [About](/about-this-site/ "About Graham Cluley")

[CHECK AVAILABILITY](/#form "Hire cybersecurity expert Graham Cluley to speak at your event")

[CHECK AVAILABILITY](/#form "Hire cybersecurity expert Graham Cluley to speak at your event")

MENU

[Speaking](/ "Home") ·
[Writing](/writing/ "Writing") ·
[Podcast](/podcasts/ "Podcast") ·
[Contact](/contact/ "Contact") ·
[About](/about-this-site/ "About")

⁠This week's sponsor: [Browse privately with a secure VPN that safeguards your privacy. Unblock content worldwide. Get 64% Off Proton VPN.](https://grahamcluley.com/go/protonvpn/)

[ⓘ](/sponsorship/ "Learn more about sponsoring this website")

# Smashing Security podcast #470: This AI security flaw might be impossible to fix

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:15 am, June 4, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #470: This AI security flaw might be impossible to fix](https://grahamcluley.com/wp-content/uploads/2026/06/ss-episode-470.webp)

A website called “UK visa portal” has been quietly collecting passport scans, selfies, and personal data from thousands of travellers who thought they were applying through official channels. They weren’t. And when a journalist tried to warn the company, it was lawyers who responded.

Meanwhile, a paper from Cornell suggests that prompt injection – the technique malicious actors use to trick AI agents into doing things they really shouldn’t – may be fundamentally unsolvable. Which is err… awkward, because everyone is rushing to plug AI agents into their email, files, and corporate networks.

Plus don’t miss our featured interview with Andrea Sivieri of CoreView, who tells us how hackers can lock your entire organisation out of its Microsoft 365 environment… without having to trick you into running a single piece of malicious code or handing over a password.

All this and more in episode 470 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Tanya Janca.

[![Podcast artwork](https://media.redcircle.com/images/2026/6/3/21/4e353ce3-5876-49bd-891f-ce2a1f50ea64_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #470

### [This AI security flaw might be impossible to fix](https://www.smashingsecurity.com/470)

↺
15

↻
30
0:00

Learn more

0:00
0:00

0:00

1×

Show full transcript
▼

![Transcript](https://grahamcluley.com/wp-content/uploads/2026/04/transcript.webp)

GRAHAM CLULEY

So it's spin doctors, it's lawyers, because that's what you do when you have a serious security hole, isn't it?

TANYA JANCA

That's what they used to do though. When you used to report a bug, companies would sue you.

Unknown

Yes, you must be a hacker. Yeah, we're going to send the cops around. Smashing Security, Episode 470.

TANYA JANCA

And I'm Tanya Janca.

GRAHAM CLULEY

Tanya, great to have you back on the show. Real delight to have you here. Now, you were on the show a little while ago, but you've got some exciting news.

You're going to be signing copies of your new book. Tell us about it.

TANYA JANCA

Yes, I recently met some of the wonderful people at ESET. We were discussing how I was coming down to Vegas, 'cause I'm going to do a bunch of things at DEF CON.

And they said, well, we have a booth at Black Hat. Did you want to show up at our booth and sign some books? So they have bought a ton of books.

And so both days at Black Hat, I'm going to hang out at their booth and just give tons of books away and sign books and hang out. And I'm really excited.

The folks at ESET are so great.

GRAHAM CLULEY

Oh, they're a nice bunch. Yeah, I've done some work with them in the past and they're actually sponsoring this episode of the podcast.

They've got a really good antivirus product, but it's good to know that they'll also be handing out copies of your book. So this is the latest book from She Hacks Purple, right?

TANYA JANCA

Yes, it's Alice and Bob Learn Secure Coding.

And so if you write code or quite frankly, if you're working with an LLM and it's writing code for you and you need to make sure that code is actually safe, this is the book for you for sure.

GRAHAM CLULEY

Yeah, make sure you go and visit the ESET booth at Black Hat and you may well bump into Tanya and get her to sign you a free copy of her book. Very nice. Not bad.

TANYA JANCA

At all, right?

GRAHAM CLULEY

Now, before we kick off, let's thank this week's wonderful sponsors, CoreView, Vanta, and ESET. We'll be hearing more about them later on in the podcast.

JOE

This week on Smashing Security, we're not going to be talking about how hackers were able to get Meta's AI to help them hack into Meta Instagram accounts.

GRAHAM CLULEY

You'll hear no discussion of how Canon has released firmware updates to fix security holes in more than 200 of its enterprise printers.

JOE

That could allow remote hackers to steal local domain passwords.

And we won't even mention how hackers managed to steal the encrypted password vaults of some customers of password manager Dashlane after brute-forcing two-factor authentication.

GRAHAM CLULEY

So Tanya, what are you going to be talking about this week?

TANYA JANCA

I want to talk about how prompt injection might be forever. Cornell University wrote a paper and I think it's pretty interesting.

GRAHAM CLULEY

And I'm going to be asking you to take a deep breath if you've ever uploaded a passport scan to a website.

Plus, don't miss our featured interview with Andrea Sivieri of CoreView, where he'll be discussing how hackers can lock your entire organization out of its Microsoft 365 environment without having to trick you into running a single piece of malicious code or handing over a password.

All this and much more coming up on this episode of Smashing Security. Smashing Security. Now time for a quick word from our friends at CoreView. Joe, quick question for you.

How confident are you in your Microsoft 365 security posture?

JOE

Graham, I don't even have a Microsoft 365 tenant.

GRAHAM CLULEY

Oh, for goodness sake, Joe, it's for our sponsor. Just play along with me, right? Picture the scene. It's Monday morning.

You've got your coffee, you're wearing your second best hoodie, you're feeling pretty good about your Microsoft 365 setup because you checked Purview, you tightened conditional access, and frankly, you deserve a biscuit.

JOE

Biscuits? Okay, I'm in. I'll play along with you. Thank goodness for that. So, and then someone forwards you a breach report about a company that did all of that too.

So how did they get hacked?

Turns out some quiet little permission that crept wider over 3 years, a policy exception that nobody had reviewed, the kind of thing that's invisible until it isn't.

GRAHAM CLULEY

And this is exactly the stuff that CoreView's free Microsoft 365 Security Posture Check tool is designed to sniff out.

It's the drift, the exceptions, the little permissions you stopped looking at because, well, you assumed ...