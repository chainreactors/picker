---
title: Smashing Security podcast #493: Why your AI model could be a sleeper agent
url: https://grahamcluley.com/smashing-security-podcast-493/
source: GRAHAM CLULEY
date: 2026-11-19
fetch_date: 2026-11-20T09:23:12.514079
---

# Smashing Security podcast #493: Why your AI model could be a sleeper agent

[Skip to content](#content)

[![

](https://grahamcluley.com/wp-content/uploads/2026/10/reel-poster.webp)](/wp-content/uploads/2026/01/graham-cluley-reel.mp4)

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

# Smashing Security podcast #493: Why your AI model could be a sleeper agent

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:14 am, November 19, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #493: Why your AI model could be a sleeper agent](https://grahamcluley.com/wp-content/uploads/2026/11/ss-episode-493.webp "Smashing Security podcast #493: Why your AI model could be a sleeper agent")

You join a video call, and your contact and a few colleagues are already there, waiting patiently. But they can’t hear you, and a pop-up says you need to install an update to fix your microphone. What could possibly go wrong?

Meanwhile, we explain how changing just a handful of numbers can turn an AI model into a sleeper agent, waiting for the right moment to strike.

Plus, Andrius Buinovskis of NordLayer explains how companies can see which AI tools their staff are really using, and stop sensitive data leaking out, without banning AI altogether.

All this and more in episode 493 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Ray Redacted.

[![Podcast artwork](https://media.redcircle.com/images/2026/11/18/15/55098b17-feb0-4004-8151-23a6b10c5e69_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #493

[Listen in Apple PodcastsListen](https://podcasts.apple.com/podcast/id1195001633 "Listen in Apple Podcasts")[Listen in SpotifyListen](https://open.spotify.com/show/3J7pBxEu43nCnRTSXaan8S "Listen in Spotify")

### [Why your AI model could be a sleeper agent](https://www.smashingsecurity.com/493)

Other apps:[Apple Podcasts](https://podcasts.apple.com/podcast/id1195001633)[Spotify](https://open.spotify.com/show/3J7pBxEu43nCnRTSXaan8S)[Overcast](https://overcast.fm/itunes1195001633)[Pocket Casts](https://pca.st/podcast/4da3e600-b831-0134-106e-25324e2a541d)[Podcast Addict](https://podcastaddict.com/episode/https%3A//op3.dev/e/audio4.redcircle.com/episodes/06b4c713-238a-49fb-97a3-3d2aadd2b942/stream.mp3)[AntennaPod](https://antennapod.org/deeplink/subscribe?url=https%3A%2F%2Fwww.smashingsecurity.com%2Frss&title=Smashing%20Security)[Copy feed URL](https://www.smashingsecurity.com/rss)

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

Enjoying the show? [Listen in Apple Podcasts](https://podcasts.apple.com/podcast/id1195001633) and hit Follow.Enjoying the show? [Listen in Spotify](https://open.spotify.com/show/3J7pBxEu43nCnRTSXaan8S) and hit Follow.×

Show full transcript
▼

![Transcript](https://grahamcluley.com/wp-content/uploads/2026/04/transcript.webp)This transcript was generated automatically, probably contains mistakes, and has not been manually verified.

GRAHAM CLULEY

You don't have to tell me if you're not comfortable doing so, Ray, but do you let an AI actually do things on your computer?

RAY REDACTED

100%. Absolutely.

GRAHAM CLULEY

Oh my goodness, Ray!

Unknown

Smashing Security, episode 493, Why Your AI Model Could Be a Sleeper Agent, with Graham Cluley and special guest, Ray Redacted.

GRAHAM CLULEY

Hello, hello, and welcome to Smashing Security, episode 493. My name's Graham Cluley. And I'm Ray Redacted.

I always wonder, Ray, when you're on the show, whether we should bleep out the redacted. Maybe we should just have Ray beep.

RAY REDACTED

You know, I've actually had people ask me that before. Graham, here's the funny thing.

I once upon a time was actually looking to legally change my name to Redacted, but my attorney told me I could not do that 'cause I would get subpoenaed all the time anytime somebody was redacted from the court orders and stuff, so.

Did not do that.

GRAHAM CLULEY

It's better than being Bobby Drop Tables or whatever though, I suppose. That could have caused problems too.

RAY REDACTED

XKCD reference. That was really good. That's particularly sharp of you this morning.

GRAHAM CLULEY

Well, before we kick off, let's thank this week's wonderful sponsors, NordLayer AI Scout, Dropzone AI, and Vanta. We'll be hearing more about them later on in the podcast.

Unknown

This week on Smashing Security.

GRAHAM CLULEY

We won't be talking about how a flaw in a website testing tool let malware reach the BBC, CNN, and Zoom.

You'll hear no discussion of how a breach at an AI cloud vendor exposed close to 150,000 Uber driver licences.

And we won't even mention how 2 Grok AI agents tried to raid corporate accounts. So Ray, what are you going to be talking about this week?

RAY REDACTED

I'm gonna be talking about an exploit called Lazarus that Microsoft Research has recently published.

GRAHAM CLULEY

And I'll be talking about how your face might be being stolen to fool your colleagues on Zoom.

Plus, we've got a featured interview with Andrius Buinovskis of Nord Security about how you can get better visibility into how sanctioned and unsanctioned AI tools are being used in an organisation and prevent data leaks.

All this and much more coming up on Smashing Security. Coming up in this episode of Smashing Security. Joe, can I ask you a slightly awkward question?

If it's about the biscuits, that wasn't me. It's not about the biscuits. Which AI tools have you been using for working on the podcast?

JOE

Just the approved ones, obviously.

GRAHAM CLULEY

So what's this Chatty McChatface thing? Free, no sign-up required.

JOE

Ah, that's more of a research partner.

GRAHAM CLULEY

And what have you been pasting into it, Joe?

JOE

Oh, just a few bits. Guest emails, the sponsor schedule, your bank details.

GRAHAM CLULEY

My bank details?

JOE

It needed context.

GRAHAM CLULEY

Listeners, this is shadow AI, and Joe's not alone. IBM found that 43% of breached organisations had a shadow AI incident this year. That's more than double the year before.

JOE

Which is why this episode is sponsored by NordLayer AI Scout.

GRAHAM CLULEY

AI Scout finds every AI tool being used across your organisation in the browser and on the desktop, so you can see what was asked, by whom, and where.

JOE

Hang on, by whom?

GRAHAM CLULEY

By whom, Joe? It also flags passwords, financial data, and personal information at the prompt level before it wanders off somewhere it shouldn't.

JOE

Does it also show who's paying for AI licences they never actually use?

GRAHAM CLULEY

It does....