---
title: Smashing Security podcast #492: How hackers turned Russian cars into pumpkins
url: https://grahamcluley.com/smashing-security-podcast-492/
source: GRAHAM CLULEY
date: 2026-11-12
fetch_date: 2026-11-13T09:07:29.409244
---

# Smashing Security podcast #492: How hackers turned Russian cars into pumpkins

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

# Smashing Security podcast #492: How hackers turned Russian cars into pumpkins

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:32 am, November 12, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #492: How hackers turned Russian cars into pumpkins](https://grahamcluley.com/wp-content/uploads/2026/11/ss-episode-492.webp "Smashing Security podcast #492: How hackers turned Russian cars into pumpkins")

You’re driving your new Chinese SUV when the dashboard goes dark. Ten minutes later, your phone rings. A stranger says they’ve got the digital key to your car, and would you like it back? Of course you would. That’ll be $550.

Meanwhile, three men have been charged over a scheme that used deepfakes of company bosses to steal around $130 million. Hear more about what happened, and the simple human trick that can foil the fakes.

All this and more in episode 492 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Danny Palmer.

[![Podcast artwork](https://media.redcircle.com/images/2026/11/11/13/02b7b895-2812-4e9a-9783-2210d6144870_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #492

[Listen in Apple PodcastsListen](https://podcasts.apple.com/podcast/id1195001633 "Listen in Apple Podcasts")[Listen in SpotifyListen](https://open.spotify.com/show/3J7pBxEu43nCnRTSXaan8S "Listen in Spotify")

### [How hackers turned Russian cars into pumpkins](https://www.smashingsecurity.com/492)

Other apps:[Apple Podcasts](https://podcasts.apple.com/podcast/id1195001633)[Spotify](https://open.spotify.com/show/3J7pBxEu43nCnRTSXaan8S)[Overcast](https://overcast.fm/itunes1195001633)[Pocket Casts](https://pca.st/podcast/4da3e600-b831-0134-106e-25324e2a541d)[Podcast Addict](https://podcastaddict.com/episode/https%3A//op3.dev/e/audio4.redcircle.com/episodes/abe16c1e-2fd8-47c2-9b22-4906b35f9b8a/stream.mp3)[AntennaPod](https://antennapod.org/deeplink/subscribe?url=https%3A%2F%2Fwww.smashingsecurity.com%2Frss&title=Smashing%20Security)[Copy feed URL](https://www.smashingsecurity.com/rss)

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

DANNY PALMER

How do you take a screenshot in a car?

GRAHAM CLULEY

You can take screenshots on a car if you press down the clutch pedal while inserting a thumb down the exhaust pipe. I think I'm not suggesting people try this.

And also, you'd have to be a bit like Mr. Tickle to reach so far around.

DANNY PALMER

Smashing Security, episode 492. How Hackers Turned Russian Cars into Pumpkins with Graham Cluley and special guest Danny Palmer.

Hello, hello, and welcome to Smashing Security episode 492. My name's Graham Cluley.

DANNY PALMER

And I'm Danny Palmer.

GRAHAM CLULEY

Danny, another busy week in cybersecurity. All the stories, they just keep on coming, don't they?

DANNY PALMER

Loads of them. And I was away on a trip in Cornwall for the last few days as well, so I came back and checked what's happened. Turns out quite a lot.

GRAHAM CLULEY

Quite a lot's been going on, and we'll be talking about some of those things which have been going on this week, including some things which maybe haven't been making the headlines quite as much.

But before we kick off, let's thank this week's wonderful sponsors, HackTheBox, Dropzone AI, and Vanta. We'll be hearing more about them later on in the podcast.

DANNY PALMER

This week on Smashing Security.

GRAHAM CLULEY

We won't be talking about how Binance is warning users that an iOS flaw could leak their crypto wallet secrets.

Unknown

You'll hear no discussion of—

GRAHAM CLULEY

How Donald Trump has chosen an executive from Palantir to head up the US Cybersecurity and Infrastructure Security Agency.

DANNY PALMER

And we won't even mention—

GRAHAM CLULEY

How Wyndham Hotels exposed customer data after leaving a password inside the source code of its Android app. So Danny, what are you going to be talking about this week?

DANNY PALMER

I'm going to be talking about how 3 men have been charged with using deepfake AI scams to steal millions of dollars from companies around the world.

GRAHAM CLULEY

And I'm going to be discussing how Russian cars are being turned into pumpkins — well, metaphorical pumpkins at least — and why a stranger on the phone is selling the owners their keys back.

All this and much more coming up on this episode of Smashing Security.

Somewhere in your security team right now, there's a worker who's never slept, never taken a holiday, never once said, I'll leave this until Monday.

JOE

Is this about Geoff?

GRAHAM CLULEY

No, Joe, it's not about Geoff.

JOE

Because Geoff actually does sleep. I've seen him do it.

GRAHAM CLULEY

It's not Geoff, Joe. It's an agent. Because your security team isn't just humans anymore. It's humans and AI agents working the same shifts, touching the same systems.

JOE

2 kinds of worker on the same team.

GRAHAM CLULEY

And here's the question no one's asking in the budget meeting. Do you actually know whether both of them can do the job?

JOE

You trust your analysts because they've got certifications, experience, a CV you have interviewed against.

GRAHAM CLULEY

And your agent? Got hired on a vibe after a product demo.

JOE

We've been letting it mark its homework this whole time.

GRAHAM CLULEY

This is where HackTheBox comes in. They help organisations build one connected cyber workforce strategy for humans and agents alike.

JOE

For the humans, it's hands-on training, the real skills needed to secure AI systems and fight back against AI-accelerated threats. Not slides, not theory — the actual job.

GRAHAM CLULEY

And for the agents, HackTheBox lets you appraise them, test them against realistic cybersecurity work the way you'd test a new hire, and reappraise them because the model changes, the tools change, the environments change,...