---
title: Smashing Security podcast #487: Clippy’s crypto comeback
url: https://grahamcluley.com/smashing-security-podcast-487/
source: GRAHAM CLULEY
date: 2026-10-07
fetch_date: 2026-10-08T08:08:25.296819
---

# Smashing Security podcast #487: Clippy’s crypto comeback

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

# Smashing Security podcast #487: Clippy’s crypto comeback

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:10 am, October 8, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #487: Clippy's crypto comeback](https://grahamcluley.com/wp-content/uploads/2026/10/ss-episode-487.webp "Smashing Security podcast #487: Clippy's crypto comeback")

Microsoft’s Twitter account, with its 13 million followers, was hijacked by a paperclip. There was no ransomware or data theft, just Clippy, a dodgy crypto coin, and a corporate apology that wasn’t from Microsoft either.

Meanwhile, UK losses from hacked email and social media accounts have rocketed by 417%, as scammers pose as your friends to flog you tickets to gigs that don’t exist.

Plus, Hack The Box’s Christine Bartlett joins us for a featured interview to ask what happens when AI agents join your security team, and whether anyone has thought to give them a performance review.

All this and more in episode 487 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Danny Palmer.

[![Podcast artwork](https://media.redcircle.com/images/2026/10/7/21/003e575b-7b96-4e33-818b-5d276b0826c0_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #487

### [Clippy's crypto comeback](https://www.smashingsecurity.com/487)

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

DANNY PALMER

It's October, which means it's Cybersecurity Awareness Month.

GRAHAM CLULEY

Oh no, the one month of the year we have to care about cybersecurity, and then the 11 months we can have off. Yes, yes, it is, isn't it?

DANNY PALMER

I've got up all my decorations, sent my cards. Very exciting times.

GRAHAM CLULEY

Smashing Security, episode 487. Clippy's Crypto. Welcome back with Graham Cluley and special guest Danny Palmer. Hello, hello, and welcome to Smashing Security episode 487.

My name's Graham Cluley.

DANNY PALMER

And I'm Danny Palmer.

GRAHAM CLULEY

Danny, great to have you back. I also have to say, great also to be sitting in the seat again here at the podcast palace, newly relocated.

Thanks to everyone who listens to the show for their kind words as I took a week off recently in order to undergo a house move.

So it wasn't possible to do the podcast and move house and change cities at the same time.

DANNY PALMER

You weren't doing it while driving the van to your new house then?

GRAHAM CLULEY

I could have done, couldn't I? I could have livestreamed or something like that. I did used to know a guy. I remember once he was driving me around.

This was, oh gosh, 25, 30 years ago or so. And he was driving me around London and I thought, oh, that's an interesting radio programme.

It appears that he's listening to an episode of Dad's Army.

And I looked over at him and I saw that he actually had balanced on top of his steering wheel where the speedometer was or whatever.

He actually had one of those mini televisions with an aerial and he was bloody well watching TV while driving me around. Some friend he turned out to be.

DANNY PALMER

I suppose that's those times where the laws hadn't caught up with the technology yet. Yes.

GRAHAM CLULEY

Yes. He would have been caught these days.

DANNY PALMER

I'm glad everything's gone successfully and you've got your important bookshelf behind you as well in your camera. That's the most important thing.

GRAHAM CLULEY

Yes.

Anyone who's watching the video will be able to see, yes, got the all-important bookshelf, sufficiently blurred out so you can't see that it's mostly Doctor Who books and Doctor Who videos and the occasional chess book as well.

Well, before we kick off, let's thank this week's wonderful sponsors, HackTheBox, Origin, and Vanta. We'll be hearing more about them later on in the podcast.

Unknown

This week on Smashing Security.

GRAHAM CLULEY

We won't be talking about how AI agents are suspected of hacking seven South Korean banks.

Unknown

You'll hear no discussion of—

GRAHAM CLULEY

How ASOS customers found out the site had been hacked from an app notification posted by the hackers themselves.

DANNY PALMER

And we won't even mention—

GRAHAM CLULEY

How AI coding agents leaked 13,000 internal screenshots from over 300 companies onto public GitHub just to be helpful. So Danny, what are you going to be talking about this week?

DANNY PALMER

Well, I'm going to be talking about a big rise in cyber scams stealing social media accounts of maybe your friends.

GRAHAM CLULEY

And I'm going to be exploring a cyberattack involving one of the most reviled characters in history.

Plus, we're also going to be joined by Christine Bartlett of Hack The Box for a featured interview. All this and much more coming up in this episode of Smashing Security.

Somewhere in your security team, right now, there's a worker who's never slept, never taken a holiday, never once said, I'll leave this until Monday.

JOE

Is this about Geoff?

GRAHAM CLULEY

No, Joe, it's not about Geoff.

JOE

Because Geoff actually does sleep. I've seen him do it.

GRAHAM CLULEY

It's not Geoff, Joe. It's an agent. Because your security team isn't just humans anymore. It's humans and AI agents working the same shifts, touching the same systems.

JOE

Two kinds of worker. On the same team.

GRAHAM CLULEY

And here's the question no one's asking in the budget meeting. Do you actually know whether both of them can do the job?

JOE

You trust your analysts because they've got certifications, experience, a CV you interviewed against.

GRAHAM CLULEY

And your agent got hired on a vibe after a product demo.

JOE

We've been letting it mark its homework this whole time.

GRAHAM CLULEY

This is where HackTheBox comes in. They help organisations build one connected cyber workforce strategy for humans and agents alike.

JOE

For the humans, it's hands-on training, the real skills needed to secure AI systems and fight back against AI-accelerated threats. Not slides, not theory, the actual job.

GRAHAM CLULEY

And for the agents, HackTheBox lets you...