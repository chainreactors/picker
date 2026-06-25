---
title: Smashing Security podcast #473: How a hacker could have Rickrolled the entire World Cup
url: https://grahamcluley.com/smashing-security-podcast-473/
source: GRAHAM CLULEY
date: 2026-06-24
fetch_date: 2026-06-25T06:10:28.231763
---

# Smashing Security podcast #473: How a hacker could have Rickrolled the entire World Cup

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

# Smashing Security podcast #473: How a hacker could have Rickrolled the entire World Cup

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:10 am, June 25, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #473: How a hacker could have Rickrolled the entire World Cup](https://grahamcluley.com/wp-content/uploads/2026/06/ss-episode-473.webp)

A polite caller from your bank says there is a problem with your account. Don’t worry – they’ll send someone round to help. They’ll even take your cards away to keep them safe. The scam has run rampant, until Dutch police plastered blurred photos of 100 suspects across billboards, supermarkets, and TikTok, with a two-week ultimatum to turn themselves in… or else.

Meanwhile, a security researcher called Bob DaHacker got her hands on the live broadcast controls for every match of the 2026 FIFA World Cup. She could have Rickrolled the entire planet, but actually spent days trying to find anyone at FIFA who would pick up the phone.

Plus! Don’t miss our featured interview with Black Kite’s Jeffrey Wheatman exploring ransomware and extortion attacks across Europe.

All this and more in episode 473 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Danny Palmer.

[![Podcast artwork](https://media.redcircle.com/images/2026/6/24/14/ecee3082-626a-4611-aaf8-6c10102b3158_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #473

### [How a hacker could have Rickrolled the entire World Cup](https://www.smashingsecurity.com/473)

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

Unknown

Did she think of sending a Truth Social message to the winner of the inaugural FIFA Peace Prize?

Because he's normally online, and I believe he probably has the mobile phone number of the FIFA president.

Smashing Security, Episode 473: How a Hacker Could Have Rickrolled the Entire World. World Cup with Graham Cluley and special guest Danny Palmer.

Hello, hello, and welcome to Smashing Security episode 473. My name's Graham Cluley.

DANNY PALMER

And I'm Danny Palmer.

GRAHAM CLULEY

Danny, great to have you on the show again. As regular listeners know, you are a cybersecurity journalist. Busy month, isn't it?

I mean, there's lots of events going on and things like that. You must be going from event to event, writing story after story.

DANNY PALMER

It has been busy, of course, as you well know as well. It was Infosecurity Europe this month and you were on stage hosting. I saw you on the stage. I didn't get to see you in person.

I did see you in person at one point, actually. Did you? But—

GRAHAM CLULEY

You should have given me a wave.

DANNY PALMER

Well, this is from behind and you turned into the toilets. So I thought you wouldn't want a tap on the shoulder at that point.

But no, I could have sprinted up, but I doubt it would have been welcomed. But no, it was a good show. It's one of the biggest cybersecurity events in, well, Europe.

But this time I was working at Infosecurity Magazine. So I was covering it from that side. So it was very, very hands-on.

Lots of people seem to enjoy the talks, good feedback from sessions. People like you, obviously, there's always nice things said about you and feedback from the events.

GRAHAM CLULEY

Oh, thank you.

DANNY PALMER

So that's good. But yeah, it was grand.

GRAHAM CLULEY

Well, before we kick off, let's thank this week's wonderful sponsors, Black Kite, ProtonPass, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security.

We won't be talking about how Brazil suspended its mobile phone emergency alert system after a hacker sent false warnings to phones across the country.

You'll hear no discussion of how tech site Gizmodo has been caught hitting readers with click-fix malware prompts.

And we won't even mention how two men have pled guilty to the £39 million cyberattack on Transport for London, which impacted 10 million commuters.

So Danny, what are you going to be talking about this week?

DANNY PALMER

I'm going to be talking about a security issue at FIFA which could have got everyone rickrolled.

GRAHAM CLULEY

And I'm going to be talking about a devastating Dutch fraud epidemic that has forced police into a bold response involving motorway billboards.

Plus, don't miss our featured interview with Jeffrey Wheatman, where we'll be looking at Black Kite's report into ransomware and extortion attacks across Europe.

All this and much more coming up on this episode of Smashing Security.

JOE

Graham, what's this about a new report from one of our sponsors?

GRAHAM CLULEY

Yes, Black Kite have just put out their first ever European Cyber Risk Report.

And oh my goodness, they've been looking into ransomware attacks across Europe for the last year and a half or so.

JOE

And let me guess, everything is fine and we have nothing to worry about?

GRAHAM CLULEY

Well, ransomware is up 55% year on year in the first 4 months of 2026 alone.

JOE

So, not fine.

GRAHAM CLULEY

No, Joe, not fine at all. Nearly 70% of all European ransomware activity is concentrated in just 5 countries.

And this report from Black Kite breaks down exactly where the attacks are hitting hardest and which hacking groups are responsible.

JOE

So is there anything in there beyond the headline numbers?

GRAHAM CLULEY

The bit that really struck me is what they found about third-party risks. A lot of companies aren't being attacked directly.

Instead, they're being caught in the blast radius of an attack on one of their suppliers.

JOE

Right. You're only as secure as the weakest link in your supply chain.

GRAHAM CLULEY

And the report has some real-world examples that illustrate this perfectly.

For instance, there's a Swedish company, it has an unpronounceable name, they got hit and that ended up causing huge problems at hundreds of organisations, exposing the data of over a million people.

JOE

All from one incident.

GRAHAM CLULEY

All from one incident. And the report also covers how regulations like NIS2 and DORA are forcing European businesses to get muc...