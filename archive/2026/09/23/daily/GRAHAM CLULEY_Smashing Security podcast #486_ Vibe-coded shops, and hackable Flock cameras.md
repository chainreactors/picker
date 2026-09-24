---
title: Smashing Security podcast #486: Vibe-coded shops, and hackable Flock cameras
url: https://grahamcluley.com/smashing-security-podcast-486/
source: GRAHAM CLULEY
date: 2026-09-23
fetch_date: 2026-09-24T07:08:25.755300
---

# Smashing Security podcast #486: Vibe-coded shops, and hackable Flock cameras

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

# Smashing Security podcast #486: Vibe-coded shops, and hackable Flock cameras

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:15 am, September 24, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #486: Vibe-coded shops, and hackable Flock cameras](https://grahamcluley.com/wp-content/uploads/2026/09/ss-episode-486.webp "Smashing Security podcast #486: Vibe-coded shops, and hackable Flock cameras")

A store in Auckland vibe-coded itself a new website. Within hours, its inventory had somehow expanded to include a pair of crusty socks, an $850 banana, and all of New Zealand’s national parks. What could possibly have gone wrong?

Meanwhile, a hacker collective backed a truck into one of the license-plate-reading Flock safety cameras popping up on American street corners, and took a very close look inside.

All this and more in episode 486 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Dave Bittner.

[![Podcast artwork](https://media.redcircle.com/images/2026/9/20/15/64f221a1-b62a-44d2-af57-dbe5b41869b0_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #486

### [Vibe-coded shops, and hackable Flock cameras](https://www.smashingsecurity.com/486)

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

DAVE BITTNER

I have to say, what this reminds me of is there was a glitch on Amazon for a while.

I don't know if it's still there, where if you went to buy condoms, it would ask you, would you like to buy this item used?

GRAHAM CLULEY

Smashing Security. Smashing Security, episode 486, Vibe-Coded Shops and Hackable Flock Cameras, with Graham Cluley and special guest Dave Bittner.

Hello, hello, and welcome to Smashing Security, episode 486. My name's Graham Cluley.

DAVE BITTNER

And I'm Dave Bittner.

GRAHAM CLULEY

Dave, always lovely to have you back on the show. Star of The Cyber Wire, Hacking Humans, that other one I've forgotten the name of.

DAVE BITTNER

Caveat.

GRAHAM CLULEY

Caveat, thank you.

DAVE BITTNER

It's all good, Graham.

GRAHAM CLULEY

The good news is, Dave, actually, is I'm going to be recommending that all of our listeners go and check out your podcasts, particularly next week, because there isn't going to be an episode of Smashing Security next week.

I am grabbing a map, a compass, and a rucksack full of cheese sandwiches, and I am going to be venturing into the wilds of Britain because I'm moving house.

I'm going to a different part of the UK.

DAVE BITTNER

Wow.

GRAHAM CLULEY

And I won't have a chance to put out an episode next week.

What I will be doing is I'll be really busy contacting the CEO of Openreach and asking why it's so hard to get me a fibre internet connection to my house when there's a box just 5 feet away from me.

DAVE BITTNER

Just put a Y cable in there. What could go wrong?

GRAHAM CLULEY

Yeah, exactly. What could possibly go wrong? But never fear, folks.

If you can hold your breath until Thursday, the 8th of October, there'll be a new episode of Smashing Security then.

And in the meantime, check out Caveat and Hacking Humans and The Cyber Wire and all the other — well, thank you.

Well, before we kick off, let's thank this week's wonderful sponsors, ThreatLocker, Origin, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security, we won't be talking about how researchers managed to take over the accounts of staff at OpenAI using Anthropic's Claude.

You'll hear no discussion of how Dutch police have asked for the public's help after releasing a recording of what they believe to be the voice of a member of the Shiny Hunters hacking group.

And we won't even mention how North Korea has been posing as recruiters to infect job seekers during fake coding tests and then waiting for them to get hired somewhere real.

So Dave, what are you going to be talking about this week?

DAVE BITTNER

I'm talking about a bunch of researchers who are asking the question, what the flock?

GRAHAM CLULEY

And I'm gonna be going online to buy a laser-equipped kiwi. All this and much more coming up on this episode of Smashing Security.

GRAHAM CLULEY

This episode of Smashing Security is sponsored by Vanta.

GRAHAM CLULEY

It's 2:00 AM. Somewhere, a security team is drowning.

DAVE BITTNER

Graham!

GRAHAM CLULEY

The spreadsheets. There are so many spreadsheets. Vendor risk assessments unread. Audit evidence scattered like ash in the wind.

I've filled out the same questionnaire 4 times this week, Graham. 4 times! Some men choose to face this alone, but not tonight.

JOE

Okay, Graham, this is a bit much.

GRAHAM CLULEY

Yeah, fair point. Anyway, Vanta—

JOE

Thank God.

GRAHAM CLULEY

Vanta's a trust management platform that automates the mind-numbing stuff that makes you want to poke your eyes out with a fork.

No more manual evidence chasing, no more questionnaire hell. It continuously monitors your systems and keeps you audit ready for SOC 2, ISO 27001, HIPAA, GDPR, the works.

And it uses AI. Yes, Joe, it does.

JOE

To flag risks and streamline evidence collection so your whole security program stays in shape, not just the week before an audit.

GRAHAM CLULEY

No more 2:00 AM dread. No more spreadsheet purgatory. Just peace.

JOE

And $1,000 off if you demo it right now.

GRAHAM CLULEY

$1,000?

JOE

vanta.com/smashing. Go now before it's too late.

GRAHAM CLULEY

That's vanta.com/smashing.

JOE

And thanks to Vanta for supporting the show.

GRAHAM CLULEY

Now, chums, there are important questions to be asked of this week's guest, Mr. Dave Bittner. I won't beat around the bush, Dave. How do you feel about crusty socks?

DAVE BITTNER

How do I feel about crusty socks?

GRAHAM CLULEY

Yes, how do you feel about them?

DAVE BITTNER

I try to avoid them whenever possible.

GRAHAM CLULEY

You're not growing any in Chez Bittner right now?

DAVE BITTNER

No, no, no. But when I was a teenager, I think I had issues with crusty socks, but it's been a while.

GRAHAM CLULEY

I imagine they are pretty fresh and clean, those beautiful feet of yours these days.

I'm asking becau...