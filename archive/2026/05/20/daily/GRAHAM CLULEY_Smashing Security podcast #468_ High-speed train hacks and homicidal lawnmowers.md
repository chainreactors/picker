---
title: Smashing Security podcast #468: High-speed train hacks and homicidal lawnmowers
url: https://grahamcluley.com/smashing-security-podcast-468/
source: GRAHAM CLULEY
date: 2026-05-20
fetch_date: 2026-05-21T06:04:45.488375
---

# Smashing Security podcast #468: High-speed train hacks and homicidal lawnmowers

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

# Smashing Security podcast #468: High-speed train hacks and homicidal lawnmowers

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:04 am, May 21, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #468: High-speed train hacks and homicidal lawnmowers](https://grahamcluley.com/wp-content/uploads/2026/05/ss-episode-468.webp)

A 23-year-old radio enthusiast spent £300 on a piece of kit from the internet, and used it to bring four packed high-speed trains to a screeching halt. His defence in court? Possibly the most creative excuse we’ve heard all year.

Meanwhile, owners of $4,000 robot lawnmowers are discovering that their gadget can be hijacked over the internet, redirected at journalists who foolishly lie down in front of it, and used to harvest Wi-Fi passwords, email addresses, and GPS coordinates. Change the default password? Sure – until the next firmware update silently resets it back.

Plus – don’t miss our featured interview with XBOW’s Brendan Dolan-Gavitt about how AI is transforming penetration testing.

All this and more in episode 468 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Geoff White.

[![Podcast artwork](https://media.redcircle.com/images/2026/5/20/10/93e90640-8103-4285-b4bf-f682026670cf_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #468

### [High-speed train hacks and homicidal lawnmowers](https://www.smashingsecurity.com/468)

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

GEOFF WHITE

Why am I tempting fate? Don't do this at home. Oh, oh yeah. No, that's not comfortable. That is not comfortable.

Unknown

Smashing Security, episode 468: High-Speed Train Hacks and Homicidal Lawnmowers. With Graham Cluley and special guest Geoff White. Hello, hello, and welcome to Smashing Security.

GEOFF WHITE

Hi, and I'm Geoff White.

GRAHAM CLULEY

Geoff, welcome back to the show. Always a pleasure to have you on. Of course, our listeners know you well from your books, your podcasts.

Unknown

Mm-hmm.

GRAHAM CLULEY

Have you got anything else bubbling away, waiting to surprise us?

GEOFF WHITE

There is going to be— I think I can talk about this. Yes, no, I can talk about this because we trailed it. There's going to be a new season of The Lazarus Heist.

GRAHAM CLULEY

Fantastic.

GEOFF WHITE

Which the BBC has renamed Cyberhack.

The problem we had was it was called The Lazarus Heist because, as some of your listeners will know, it's about the Lazarus Group, the famous North Korean elite hacking team.

And so obviously the podcast was about that, but the BBC and all of us really wanted to do things other than North Korea. And so I think the challenge was, well, how do we do that?

So they renamed it basically was the end result.

So Joe Tidy, the great Joe Tidy, with another BBC journalist called Sarah Rainsford, did a series about the Zeus gang and about a guy called Maxim Yakubets.

That was series 3, basically, of Lazarus Heist.

GEOFF WHITE

We are doing series 4, which is gonna be out, I think early July, late June, early July. But if people subscribe to Cyberhack, you can get it.

And I can't go into details of what we've got, but it's—

GRAHAM CLULEY

It's juicy. It's juicy, isn't it?

GEOFF WHITE

It is juicy. Yeah, we've got some absolutely banging stuff. It's really great.

GRAHAM CLULEY

Oh, I can't wait for it. Well, before we kick off, let's thank this week's wonderful sponsors, Expo, Opswat, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security, we won't be talking about how open-source toolmaker Grafana Labs told hackers who demanded a ransom to get stuffed after they threatened to release code that is largely already public.

You'll hear no discussion of how a man pled guilty to stealing hard drives containing unreleased tracks by music star Beyoncé.

GRAHAM CLULEY

And we won't even mention how the gang behind the Shai Halud worm have released its code as open source, providing a blueprint for other attackers.

So Geoff, what are you going to be talking about this week?

GEOFF WHITE

I'm gonna be talking about garden implements that fight back this week.

GRAHAM CLULEY

And I'm gonna be telling how a student with a £300 radio brought high-speed trains to a halt.

Plus, don't miss our featured interview with Brendan Dolan-Gavitt from Expo about how AI is transforming penetration testing, what it's already better than humans at, and what it means for defenders racing to keep up.

All this and much more coming up on this episode of Smashing Security.

JOE

This episode is supported by OpsWatch.

GRAHAM CLULEY

Joe, here's a question for you. What if the entire cybersecurity industry has been doing it wrong?

JOE

The entire industry? That's a bit of a stretch, isn't it?

GRAHAM CLULEY

Well, that's the argument Benny Czarny makes in his new book, Cybersecurity Upside Down.

Benny is the founder and CEO of Opswat, and he's spent more than two decades protecting critical infrastructure, you know, nuclear facilities, defense networks, energy grids, the stuff that quite literally keeps the lights on.

JOE

OK, so what's his big idea?

GRAHAM CLULEY

Well, he says the industry is obsessed with detecting threats. But detection can never be perfect. One dodgy file slips through and your network is toast.

JOE

I like toast. So what's the alternative?

GRAHAM CLULEY

To toast?

JOE

No, to detecting threats.

GRAHAM CLULEY

Ah, well, how about not even trying to spot the malware? Instead, take files apart, throw away anything that isn't strictly needed, and rebuild a clean version from the safe bits.

The user gets a sanitized working document. The malware ends up in the bin.

JOE

But hang on, who decides what's safe?

GRAHAM CLULEY

That's the clever part. You do. Macros might be allowed for your automation team, but stripped out for finance. JavaScript ripped out of every PDF everywhere.

EXIF data scrubbed from images leaving HR. It's not an on-off switch. It's a policy that you can tune to your business.

So even a brand new attack no one's ever seen before doesn't survive the rebuild. Exactly. There's nothing to detect because it's already gone.

Whethe...