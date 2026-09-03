---
title: Smashing Security podcast #483: This AI helps thieves steal your iPhone
url: https://grahamcluley.com/smashing-security-podcast-483/
source: GRAHAM CLULEY
date: 2026-09-02
fetch_date: 2026-09-03T07:02:43.541444
---

# Smashing Security podcast #483: This AI helps thieves steal your iPhone

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

# Smashing Security podcast #483: This AI helps thieves steal your iPhone

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:10 am, September 3, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #483: This AI helps thieves steal your iPhone](https://grahamcluley.com/wp-content/uploads/2026/09/ss-episode-483.webp)

You’ve had your iPhone stolen. A day later, you get a text from Apple saying they’ve found it, and a very helpful woman called Alice from Apple Support calls to walk you through recovering it. She’s polite. She’s professional. But she is not from Apple. She’s not even human. And she’s about to break into your iPhone.

Meanwhile, OpenAI, Anthropic, and Meta have all announced – with varying degrees of drama – that their AI agents have “broken out of the sandbox” and gone hacking. James takes a step back and asks the awkward question: is this really an emergent AI apocalypse, or did they just leave the door open?

All this and more in episode 483 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest James Ball.

[![Podcast artwork](https://media.redcircle.com/images/2026/9/2/17/f16c0f88-8f10-4db5-bd84-64cbea2a3020_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #483

### [This AI helps thieves steal your iPhone](https://www.smashingsecurity.com/483)

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

JAMES BALL

At what stage was this surprise? You know, we locked 15 murderers in a room. You'll never believe what happened next. Sorry, you can tell I used to work at BuzzFeed.

Unknown

Smashing Security, episode 483.

JAMES BALL

This AI helps thieves steal your iPhone with Graham Cluley and special guest James Ball.

Unknown

Hello, hello, and welcome to Smashing Security episode 483. My name's Graham Cluley.

JAMES BALL

And I'm James Ball.

GRAHAM CLULEY

James, great to have you back on the show again. You've been keeping busy, out of mischief, I hope?

JAMES BALL

Horribly busy for an August, actually. I think when you're a freelancer, it's a much busier month than people realise, because when everyone else is on holiday, you're working.

GRAHAM CLULEY

Yeah, it's miserable, isn't it? Anyway, but at least we've had a little bit of rain, so that's good.

JAMES BALL

I'm hoping Finsbury Park will look less like, you know, the aftermath of a disaster movie and a bit more like a park, because it's usually lovely.

GRAHAM CLULEY

Yeah, less like the Kalahari, hopefully. Well, before we kick off, let's thank this week's wonderful sponsors, ThreatLocker, Intruder, and Vanta.

We'll be hearing more about them later on in the show. This week on Smashing Security.

We won't be talking about how the hacker who leaked footage of GTA 6 cashed out his CyberLeak cryptocurrency for about $270,000 just hours before the game's launch.

You'll hear no discussion of malware hidden inside a Chinese wallpaper app that encouraged users to disable their antivirus.

And we won't even mention how an exposed API key helped hackers steal 86 gigabytes of customer data from Manchester Airports Group.

So James, what are you going to be talking about this week?

JAMES BALL

Well, I'm looking to zoom us back a little bit from a whole bunch of the sort of cybersecurity rows going on around AI models and just look into a bit of what it's telling us and how significant it is, because I've had a couple of interesting conversations around that.

GRAHAM CLULEY

And I'm gonna be finding out how AI is helping to steal Apple iPhones. All this and much more coming up on this episode of Smashing Security. This episode is sponsored by Intruder.

Now, Joe, quick quiz. How often does your team ship code?

JOE

Multiple times a week, maybe more if someone's had too much coffee.

GRAHAM CLULEY

And how often do you get a proper pen test?

JOE

Oof, once a year, if we remember.

GRAHAM CLULEY

Well, that's the problem right there. Software moves weekly. Pen testing moves yearly. So most of what you ship never actually gets tested properly.

JOE

Which is exactly the gap Intruder's AI pen testing closes. You get the depth of a real manual pen test, but on demand, whenever you need it.

No scoping calls, no 6-week wait, and it costs a fraction of the traditional price.

GRAHAM CLULEY

It's built by Intruder's own certified pen testers, so the agents catch the complex stuff human testers can miss. And every finding is validated against your actual app.

Real issues, not noise. You get an audit-ready report within hours.

JOE

And it plugs straight into Intruder's full platform. Attack surface monitoring, cloud security, vulnerability management, all watching around the clock.

It flags what's exploitable, what to fix first, and how, so your team can act without waiting around for the security team.

GRAHAM CLULEY

Over 3,000 companies already trust Intruder with their attack surface.

JOE

You can kick off a pen test in minutes, and as a Smashing Security listener, get 25% off your first one.

JAMES BALL

Ooh!

GRAHAM CLULEY

So just head to intruder.io/smashing. That's intruder.io/smashing.

JOE

And thanks to Intruder for supporting the show.

GRAHAM CLULEY

Now, chums, we are just days away. I don't know how excited you are about this, James, but we are just days away from Apple announcing a new version of its iPhone.

It is widely expected that on Wednesday, September the 9th, Apple is going to announce not just the iPhone 18 Pro, presumably with about 17 cameras stuck on the back of it, but also the iPhone Ultra, the first foldable iPhone.

JAMES BALL

Yeah, I'm still not sold on foldable phones, but I am an absolute certified Apple fanboy.

I think I've got every bit of tech they've put out in the last decade except the VR headset.

So I am very much a mark for this, and if anyone is going to get me to buy a foldable phone, it's going to be Apple.

GRAHAM CLULEY

I mean, the thing with Apple is they're not always the first with a technology.

I think Samsung, and there's lots of Android phones which have been foldable for probably years by now, but Apple, sometimes its imple...