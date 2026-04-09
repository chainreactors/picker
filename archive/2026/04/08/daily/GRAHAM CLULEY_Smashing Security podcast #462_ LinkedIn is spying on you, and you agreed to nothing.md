---
title: Smashing Security podcast #462: LinkedIn is spying on you, and you agreed to nothing
url: https://grahamcluley.com/smashing-security-podcast-462/
source: GRAHAM CLULEY
date: 2026-04-08
fetch_date: 2026-04-09T04:32:28.359762
---

# Smashing Security podcast #462: LinkedIn is spying on you, and you agreed to nothing

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

# Smashing Security podcast #462: LinkedIn is spying on you, and you agreed to nothing

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:27 am, April 9, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #462: LinkedIn is spying on you, and you agreed to nothing](https://grahamcluley.com/wp-content/uploads/2026/04/ss-episode-462.webp)

LinkedIn has been secretly scanning your browser for over 6,000 installed extensions – on every single click you make. It can tell if you’re job hunting, what religion you are, and whether you have ADHD. And none of this is mentioned anywhere in their privacy policy.

Meanwhile, California’s crypto millionaires are learning that no amount of encryption can protect you from someone who knocks on your door pretending to deliver a pizza.

All this and more in episode 462 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, joined this week by special guest Dave Bittner.

[![Podcast artwork](https://media.redcircle.com/images/2026/4/7/20/e24bf815-6990-40bb-a8a7-479ac745307f_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Episode 462

### [LinkedIn is spying on you, and you agreed to nothing](https://www.smashingsecurity.com/462)

↺
15

↻
30
0:000:00
1×

[ApplePodcasts](https://www.smashingsecurity.com/applepodcasts "Link to Smashing Security on Apple Podcasts")
[Spotify](https://www.smashingsecurity.com/spotify "Link to Smashing Security on Spotify")
[PocketCasts](https://pca.st/podcast/4da3e600-b831-0134-106e-25324e2a541d "Link to Smashing Security on Pocket Casts")
[RSS](https://www.smashingsecurity.com/rss "Link to RSS feed")

[Listenad-free](https://www.smashingsecurity.com/plus "Link to Smashing Security PLUS on Patreon")

Show full transcript
▼

![Transcript](https://grahamcluley.com/wp-content/uploads/2026/04/transcript.webp)

Graham Cluley
0:03

So what should I say?

Dave Bittner
18:01

Let's say, say, looking forward to this week's Smashing Security podcast.

Graham Cluley
0:10

Yes.

Dave Bittner
0:11

With my co-host.

Graham Cluley
0:13

Co-host?

Dave Bittner
0:13

Or my special guest, Dave Bittner.

Graham Cluley
18:12

Stand down, Dave.

Dave Bittner
18:13

Thank you. Sorry. I got ahead of myself.

Unknown
0:29

Smashing Security, Episode 462: LinkedIn is Spying on You, and You Agreed to Nothing, with Graham Cluley and special guest Dave Bittner. Hello, hello, and welcome to Smashing Security, Episode 462. My name is Graham Cluley.

Dave Bittner
0:45

And I'm Dave Bittner.

Graham Cluley
0:47

Dave Bittner from the CyberWire, back on the podcast again. We can't get you away from a microphone, can we?

Dave Bittner
0:53

I know, I'm like a terrible rash and difficult to get rid of.

Graham Cluley
0:58

Do you ever feel like, you know, I've had enough of this, it's time to hang up my spurs? Well, I suppose they're not spurs, are they?

Dave Bittner
1:04

Time to hang up my XLR cables.

Graham Cluley
1:07

My XLR cables, yeah.

Dave Bittner
1:11

Not so much that, but I will tell you there are times when I smash my head against the desk and say, I need a vacation. I need a break. I need to get away from the bad news.

Graham Cluley
1:20

Yeah. I mean, I find it tough doing one podcast a week, but you do about 89 a week.

Dave Bittner
1:27

I do. I do. I have to learn how to navigate it so it doesn't take too hard a toll on you emotionally, but I'm, you know, I'm mostly there, but there are days, Graham, there are days.

Graham Cluley
1:39

Well, we certainly do appreciate you coming on the Smashing Security podcast today. And before we kick off, let's thank this week's wonderful sponsors, Meta, ESET, and Vanta. We'll be hearing more about them later on in the podcast. This week on Smashing Security. We won't be talking about how hackers working for the Russian government broke into thousands of home routers to steal passwords. You'll hear no discussion of how tourists traveling to Hong Kong have been warned that it's now a criminal offense to refuse to hand over to police the passwords for all your personal devices. And we won't even mention how after authorities cracked down on the use of Telegram, WhatsApp, and VPNs, Russian citizens have switched to using two other apps for instant message and video call, including in some cases smart cat feeders. So Dave, what are you going to be talking about this week?

Dave Bittner
2:35

I'm talking about some wealthy California crypto holders who are being targeted in wrench attacks.

Graham Cluley
2:41

And I'm going to be shining a light on how LinkedIn is shining a light on its users. All this and much more coming up on this episode of Smashing Security. Well, before we kick off, we've just got a moment to thank one of this episode's sponsors, ESET. Now, there's no shortage of cybersecurity vendors claiming to be the best, of course, but ESET is one of the few that's proven it for 30 years. Research has always been at the core of what ESET does. Their threat intelligence teams are actively tracking APT groups and ransomware affiliates and publishing findings that the security community actually reads and references. That's not a marketing line — that's 30 years of doing the work. And here's what makes it interesting: 3 decades of research means that ESET has built up global telemetry that most vendors simply don't have access to. They combine that telemetry with AI-native technology and human expertise, and that's what powers both their products and their MDR service. Real intelligence behind the protection, not just pattern matching. 110 million users worldwide trust ESET with their endpoints, cloud, email, and mobile devices. That number doesn't happen by accident. So why don't you check them out right now? Go to smashingsecurity.com/ESET. That's smashingsecurity.com/ESET. And thanks to ESET for supporting the show. Now, chums, LinkedIn. Don't you love it? I love it. Oh boy, it's great.

Dave Bittner
4:25

If by love you mean hate and do everything in my power to avoid it, then yes, I love it.

Graham Cluley
4:31

Oh, Dave, it's a wonderful service. It's a fantastic place — it's a platform where people I've never met can endorse me for skills that I don't have.

Dave Bittner
4:39

Right.

Graham Cluley
4:40

Right? Have you ever been told you are excellent at being an astronaut? You know, b...