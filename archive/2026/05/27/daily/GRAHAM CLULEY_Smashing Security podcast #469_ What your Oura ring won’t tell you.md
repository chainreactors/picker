---
title: Smashing Security podcast #469: What your Oura ring won’t tell you
url: https://grahamcluley.com/smashing-security-podcast-469/
source: GRAHAM CLULEY
date: 2026-05-27
fetch_date: 2026-05-28T06:03:49.848728
---

# Smashing Security podcast #469: What your Oura ring won’t tell you

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

# Smashing Security podcast #469: What your Oura ring won’t tell you

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:05 am, May 28, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #469: What your Oura ring won't tell you](https://grahamcluley.com/wp-content/uploads/2026/05/ss-episode-469.webp)

CISA, the US government agency whose entire job is keeping America’s critical infrastructure safe from hackers, has had a contractor publish dozens of plain-text credentials to a public GitHub profile.

Meanwhile, your Oura ring is quietly transmitting some of its data unencrypted – and when one journalist asked the company how often it hands user data to law enforcement, the answer was quite telling.

Plus don’t miss our featured interview with OPSWAT’s Benny Czarny about his new book “Cybersecurity Upside Down.”

All this and more in episode 469 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Lesley Carhart.

[![Podcast artwork](https://media.redcircle.com/images/2026/5/27/13/ce3343e6-b4d2-4dcd-8241-10f2b8790620_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #469

### [What your Oura ring won't tell you](https://www.smashingsecurity.com/469)

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

LESLEY CARHART

Cronyism does nothing for cybersecurity. Politics do nothing for cybersecurity.

Unknown

Smashing Security, Episode 469: What Your Oura Ring Won't Tell You, with Graham Cluley and special guest Lesley Carhart. Hello, hello, and welcome to Smashing Security, Episode 469.

My name's Graham Cluley.

LESLEY CARHART

And I'm Lesley Carhart, and I'm so chuffed to be back.

GRAHAM CLULEY

It's lovely to have you back, Lesley. And of course, we know you from the world of cybersecurity, but you're much more than that, aren't you?

Because one of the things, I don't know how many people know this, but you are actively into martial arts.

LESLEY CARHART

I am. Obviously moving to another country has set me back quite a lot. My joy is teaching kids.

I love teaching middle schoolers to primary students, and I was very fortunate to find a place that would take me to teach in Australia.

So, getting back into their style of teaching and hopefully onto new and interesting competitions and challenges and gradings.

GRAHAM CLULEY

And the particular martial arts you're into, taekwondo, isn't it? Or is there more than that?

LESLEY CARHART

I have a black belt in taekwondo, as one who wants to make any kind of income doing martial arts has to. And my love is tang soo do and tang soo tao, the older Korean martial arts.

GRAHAM CLULEY

Aha. This is a complete mystery to me, I must admit. So I don't know if it's really crass of me to suggest you're not just a keyboard ninja then.

Is it ninjas who do those martial arts? I don't know. You see, I'm just embarrassing myself now.

LESLEY CARHART

Ninjas have their own martial art, actually. I don't know if it's a real martial art, but I don't want to get in that argument with anybody.

So we're going to just say it's a real martial art called ninjutsu, and they do their own thing.

And no, I will never be a fantastic action hero fighting the bad guys with my fists, but I do love teaching kids and coaching kids.

It gives me a lot of joy in life to teach little people how to hit things and yell loudly.

GRAHAM CLULEY

Yeah, I bet the kids absolutely love that. Well, thank you for joining us today.

We won't be talking too much about martial arts during the course of this podcast, but we will be tapping your brain for cybersecurity advice and wisdom.

Before we kick off, let's thank this week's wonderful sponsors, Expo, Opswat, and Vanta. We'll be hearing about them more later on in the podcast. This week on Smashing Security.

We won't be talking about how a 23-year-old Canadian man has been charged with running HimWolf, fast-spreading IoT botnet that enslaved millions of devices for DDoS attacks.

You'll hear no discussion of how more than 700 legitimate websites have been compromised by a critical vulnerability in the Ghost CMS to launch a click-fix malware campaign.

And we won't even mention how hackers have breached and leaked sensitive documents from a Russian group exposing details of disinformation campaigns designed to stir hate towards migrants and support far-right political groups.

Lesley, what are you going to be talking about this week?

LESLEY CARHART

One of the interesting privacy topics that I keep seeing coming up is wearables.

Wearables for kids, wearables for adults, wearables for fitness and for health and for location tracking. And they always end up in catastrophe, so I've got another one.

GRAHAM CLULEY

And I'm gonna be talking about America's cyber defense agency, which had one job and, well, just how well do you think that they did it?

Plus, don't miss our featured interview with Benny Czarny of Ops SWAT about his new book, Cybersecurity Upside Down.

All this and much more coming up on this episode of Smashing Security.

JOE

This episode is supported by Ops SWAT.

GRAHAM CLULEY

Joe, here's a question for you. What if the entire cybersecurity industry has been doing it wrong?

JOE

The entire industry? That's a bit of a stretch, isn't it?

GRAHAM CLULEY

Well, that's the argument Benny Czarny makes in his new book, Cybersecurity Upside Down.

Benny is the founder and CEO of Ops SWAT, and he spent more than two decades protecting critical infrastructure, you know, nuclear facilities, defense networks, energy grids, the stuff that quite literally keeps the lights on.

JOE

Okay, so what's his big idea?

GRAHAM CLULEY

Well, he says the industry is obsessed with detecting threats. But detection can never be perfect. One dodgy file slips through and your network is toast.

JOE

I like toast. So what's the alternative?

GRAHAM CLULEY

To toast?

JOE

No, to detecting threats.

GRAHAM CLULEY

Oh, well, how about not even trying to spot the malware? Instead, take files apart, throw away anything that isn't strictly needed, and rebuild a clean version from the safe bits.

The user gets a sanitized working document. The malware ends up in the bin.

JOE

But hang on, who decides wh...