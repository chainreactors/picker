---
title: Smashing Security podcast #475: JadePuffer – the AI that ran a ransomware attack all by itself
url: https://grahamcluley.com/smashing-security-podcast-475/
source: GRAHAM CLULEY
date: 2026-07-08
fetch_date: 2026-07-09T06:03:34.966435
---

# Smashing Security podcast #475: JadePuffer – the AI that ran a ransomware attack all by itself

[Skip to content](#content)

[

](/wp-content/uploads/2026/01/graham-cluley-reel.mp4)

[CHECK AVAILABILITY](/#form "Hire cybersecurity expert Graham Cluley to speak at your event")

[GRAHAM CLULEY](https://grahamcluley.com/)

Cybersecurity keynote speaker

×

[Graham Cluley](/ "Graham Cluley")

[Speaking](/ "Speaking")  ⦁  [Writing](/writing/ "Writing")  ⦁  [Podcast](/podcasts/ "The Smashing Security podcast")  ⦁  [Contact](/contact/ "Contact Graham Cluley")  ⦁  [About](/about/ "About Graham Cluley")

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

# Smashing Security podcast #475: JadePuffer – the AI that ran a ransomware attack all by itself

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:19 am, July 9, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #475: JadePuffer - the AI that ran a ransomware attack all by itself](https://grahamcluley.com/wp-content/uploads/2026/07/ss-episode-475.webp)

A 15-year-old boy asked a chatbot for help – and cancelled nearly 47,000 anime streaming subscriptions in under four hours. Meanwhile, researchers have documented the first fully autonomous, agentic AI-driven ransomware attack, “JadePuffer”. What does this tell us about the future of cybersecurity?

Also, Apple’s “Hide My Email” feature turns out to hide rather less than it promises – despite Apple knowing it has a problem for over a year.

All this and more in this episode of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Zoë Rose.

[![Podcast artwork](https://media.redcircle.com/images/2026/7/7/20/26134167-edbd-43c4-a731-40baa3e7960c_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #475

### [JadePuffer - the AI that ran a ransomware attack all by itself](https://www.smashingsecurity.com/475)

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

![Transcript](https://grahamcluley.com/wp-content/uploads/2026/04/transcript.webp)This transcript was generated automatically, probably contains mistakes, and has not been manually verified.

ZOE ROSE

We need an LLM that says, here's how to do it. And don't forget to consider these things.

Unknown

No, no, we don't need that actually, Zoe. We don't need any help for the criminals in covering up the tracks. Interesting. Interesting that you should suggest that.

Smashing Security, episode 475. JadePuffer, the AI that ran a ransomware attack all by itself. With Graham Cluley and special guest Zoe Rose.

Hello, hello, and welcome to Smashing Security episode 475. My name's Graham Cluley.

ZOE ROSE

And I'm Zoe Rose.

GRAHAM CLULEY

Hello, Zoe. Welcome back to the show. It's been a while since you've been on. How are you doing?

ZOE ROSE

Well, usually when I join, something massive has happened.

GRAHAM CLULEY

Right.

ZOE ROSE

At the moment, I have not acquired another child or a pet.

GRAHAM CLULEY

So, well done.

ZOE ROSE

Yeah.

GRAHAM CLULEY

So for those who don't know Zoe, what are you? I mean, people who haven't heard of you before, what do you do exactly?

ZOE ROSE

That's a good question. What do I do? I work in security and pretend I know what I'm talking about half the time.

GRAHAM CLULEY

Oh, okay. It seems fair enough. And you work for a big company?

ZOE ROSE

I have a bloody long title now, actually. That's the change. That's what's new. My title has massively increased.

GRAHAM CLULEY

Okay, give us your title. Let's hear it.

ZOE ROSE

All right. It is C-Cert, which if you know what that stands for, it has more words, but we'll just stick to some letters. Security Operations Development Manager.

GRAHAM CLULEY

Wow.

ZOE ROSE

Yeah.

GRAHAM CLULEY

Security Operations Development Manager, like SODOM, is basically what you're saying.

Unknown

Yeah, sure.

GRAHAM CLULEY

Interesting. Well, before we kick off, let's thank this week's wonderful sponsors, Arctic Wolf, NordLayer, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security, we're not going to be talking about how a Greek politician investigating spyware had his own mobile phone hacked.

You'll hear no discussion of how a US Department of Homeland Security information sharing database has been accessed by hackers.

And we won't even mention how hackers are using a fake World Cup t-shirt offer to spread malware. So Zoe, what are you going to be talking about this week?

ZOE ROSE

I'm going to talk about Apple's Hide My Email isn't actually as hidden as it sounds like.

GRAHAM CLULEY

And I'm going to be telling the tale of how a 15-year-old with a chatbot became a cybercriminal and what happens when the AI just does the whole job itself.

All this and much more coming up on this episode of Smashing Security.

JOE

Graham, am I right in thinking that Arctic Wolf are sponsoring the show this week?

GRAHAM CLULEY

You are right, Joe.

They've just published a new report, 2026 State of the Cybersecurity Attack Surface, and they analysed over 800,000 real IT assets to find out how exposed organisations actually are.

JOE

And I'm guessing everything is hunky-dory.

GRAHAM CLULEY

No, not so much. The reality is they found 1 in 3 IT assets is missing at least one critical security control.

JOE

One in three? That's terrible.

GRAHAM CLULEY

Isn't it just? 10% of assets have no endpoint security at all. 17% are completely invisible to the tools that are supposed to be monitoring them.

JOE

So the tools don't even know those assets exist?

GRAHAM CLULEY

Right. Ghost assets wandering around your network, unprotected, unmonitored.

JOE

Like a retired geography teacher who's somehow still on the school network.

Nobody added him, nobody removed him, and he's been quietly in there for 11 years downloading maps of Paraguay.

GRAHAM CLULEY

Yeah, yeah, I guess so, Joe. The point is, your attackers will find him before you do because they are specifically looking for the forgotten, the unpatched, the invisible.

That's the path of least resistance.

JOE

So what does the report tell us to actually do about it?

GRAHAM CLULEY

Arctic Wolf's report covers how to prioritize the exposures that actually matter. Cut through all that noise and verify that when you fix something, it actually stays fixed.

And the report is free to download.

JOE

Free! I like that. Where do I get it?

GRAHAM CLULEY

SmashingSecurity.com/ArcticWolf.

JOE

That's SmashingSecurity.com/ArcticWolf. And thanks to Arctic Wolf for supporting the show. And please keep an eye on your IT assets and retired geography teachers.

GRAHAM CLULEY

So, chums, I want to tell you about two stories really this week. On the surface, they don't seem connected.

One of them involves a fully automated, sophisticated, AI-driven ransomware attack against a company. Nasty stuff.

The other involves a 15-year-old lad in Japan who just wanted to cause some chaos on an animation str...