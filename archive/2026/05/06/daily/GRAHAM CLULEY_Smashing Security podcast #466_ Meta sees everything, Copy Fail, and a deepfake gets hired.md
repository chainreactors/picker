---
title: Smashing Security podcast #466: Meta sees everything, Copy Fail, and a deepfake gets hired
url: https://grahamcluley.com/smashing-security-podcast-466/
source: GRAHAM CLULEY
date: 2026-05-06
fetch_date: 2026-05-07T05:35:25.050155
---

# Smashing Security podcast #466: Meta sees everything, Copy Fail, and a deepfake gets hired

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

# Smashing Security podcast #466: Meta sees everything, Copy Fail, and a deepfake gets hired

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:30 am, May 7, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #466: Meta sees everything, Copy Fail, and a deepfake gets hired](https://grahamcluley.com/wp-content/uploads/2026/05/ss-episode-466.webp)

Meta’s smart glasses promise privacy “designed for you” – but everything they record was being beamed off to workers in Nairobi to label by hand. When those workers blew the whistle, Meta sacked all 1,108 of them.

Meanwhile, the IT press is in a frenzy over a new Linux bug called “Copy Fail” – complete with logo, dedicated website, and a marketing-friendly name. But is it really the disaster everyone’s making it out to be?

And in our featured interview, Jake Moore of ESET explains how he tricked a company into offering his deepfake clone a job – after a perfectly normal-looking video interview.

All this and more in episode 466 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, joined this week by special guest Paul Ducklin.

[![Podcast artwork](https://media.redcircle.com/images/2026/5/4/22/2ed65a5b-8574-400c-aac4-e90cb66cfa83_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #466

### [Meta sees everything, Copy Fail, and a deepfake gets hired](https://www.smashingsecurity.com/466)

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

Unknown

So these employees, they're drawing little boxes around things to say, this is a flower pot, this is a traffic cone, this is a coffee tender, whatever it may be.

PAUL DUCKLIN

And my name is Paul Ducklin.

GRAHAM CLULEY

Hello, Paul. Good to have you back on again.

PAUL DUCKLIN

Hello, Graham. I always forget that when you do that pregnant pause, I'm supposed to give my name, even though I've done it many times before, I make the blunder every time.

GRAHAM CLULEY

You're not the only one. Sometimes I have to whisper and sometimes the whisper is edited out afterwards, say, "Say who you are." Yeah.

PAUL DUCKLIN

So, oh no, if it gets that bad with me in any future episode, I'm happy for you to leave the stage whisper in because that will focus my mind for next time.

GRAHAM CLULEY

How has the world of cybersecurity been in the last Well, since we last spoke?

PAUL DUCKLIN

Well, it has been a lot more of the same, hasn't it? More AI panics, more bugs, more patches, more social engineering attacks, more of everything.

GRAHAM CLULEY

It's always been that way, hasn't it? It's always been on that direction. You can't ever say, "Oh, it's been really, really quiet.

This whole cybersecurity business seems to be shutting down. Maybe we'll have to find ourselves a new job."

PAUL DUCKLIN

We'll get into fishmongery. Well, phish with a PH would come after us, I'm sure.

GRAHAM CLULEY

Well, before we kick off, let's thank this week's wonderful sponsors, Action1, ESET, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security, we're not going to be talking about how a Brazilian firm that protects businesses from DDoS attacks was found to be helping a botnet that launched massive DDoS attacks.

You'll hear no discussion of how Microsoft Defender started mistakenly detecting DigiCert root certificates as a Windows Trojan horse.

And we won't even mention how hackers managed to steal source code from cybersecurity giant Trellix. So, Duck, what are you going to be talking about this week?

PAUL DUCKLIN

Graham, I am going to be talking about the latest BWAIN.

GRAHAM CLULEY

Oh?

PAUL DUCKLIN

And when I say "BWAIN," it is bug with an impressive name.

And if you've been looking at the IT media at all in the last week or two, you will probably have seen the words "copy fail." And I'm going to be talking about another reason why you should probably steer well clear of Meta's smart glasses.

GRAHAM CLULEY

Plus, we'll be talking about the danger of deepfakes with Jake Moore of ESET, who actually tricked a company into giving his deepfake a job offer after online interview.

All this and much more coming up in this episode of Smashing Security. Well, we've got time now to chat about one of the sponsors of this week's show, Action1.

Now then, if you are a systems administrator managing endpoints every day, you've probably postponed patching at least once, not because you forgot, but because you didn't feel like gambling with uptime.

JOE

Meanwhile, the backlog grows, vulnerabilities pile up and patching stays stuck in manual mode.

GRAHAM CLULEY

Well, Action1 fixes that. Action1 is a cloud-native patch management platform for Windows, macOS, Linux, and third-party apps, all from one place. No VPN needed.

JOE

Curious on how easy it is to start with Action1? Well, you can use it on your first 200 endpoints for free forever with no functional limits.

GRAHAM CLULEY

First 200 endpoints for free forever? That's bonkers. Incredible, Joe.

JOE

So if you're looking to automate patching at scale and get weeks, even months of your time back, go to smashingsecurity.com/action1 and sign up for patching that just works.

GRAHAM CLULEY

That's right. It's not a disguise-free trial. There's no credit card required. There's no hidden limits. All you have to do is visit smashingsecurity.com/action1 and get started today.

And thanks to Action 1 for supporting the show. So, Duck, I need to make an apology. Not specifically to you, to the listeners, I think.

Back in February, I had a bit of a rant with James Ball about the smart glasses made by Meta, and I explained how Mark Zuckerberg's company was planning to turn on facial recognition within the glasses and how it had been reported that there was this secret internal memo inside the company that said—

PAUL DUCKLIN

I thought you were going to say inside the glasses, which would be more exciting.

GRAHAM CLULEY

No memo inside the glasses. They had this secret memo where they said, "Look, there's going to be a bit of aggro when we launch this.

You know, people who care about privacy and stuff are going to object." And so they said, "The best thing that we can do is time this to be when there's some ...