---
title: Smashing Security podcast #489: How a brand new crypto wallet came with a spy inside
url: https://grahamcluley.com/smashing-security-podcast-489/
source: GRAHAM CLULEY
date: 2026-10-21
fetch_date: 2026-10-22T06:47:01.904964
---

# Smashing Security podcast #489: How a brand new crypto wallet came with a spy inside

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

# Smashing Security podcast #489: How a brand new crypto wallet came with a spy inside

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:12 am, October 22, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![How a brand new crypto wallet came with a spy inside](https://grahamcluley.com/wp-content/uploads/2026/10/ss-episode-489.webp "How a brand new crypto wallet came with a spy inside")

Imagine buying a brand new hardware wallet for your cryptocurrency with the shrink-wrap still on… what could possibly be hiding inside? We break out a Geiger counter and a cat to find out.

Meanwhile, malicious ads are targeting journalists with zero-click attacks.

Plus, Origin’s Spencer Thompson reveals what AI agents are really getting up to on your employees’ laptops when nobody’s looking.

All this and more in episode 489 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Lianne Potter.

[![Podcast artwork](https://media.redcircle.com/images/2026/10/21/16/1baa59bf-a21c-40af-8073-7cef4ea1f65c_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #489

### [How a brand new crypto wallet came with a spy inside](https://www.smashingsecurity.com/489)

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

LIANNE POTTER

One of those spyware companies is called Candiru. Now, do you know what a candiru is, Graham?

GRAHAM CLULEY

Is that a kangaroo with a sweet tooth? Is that a candiru?

LIANNE POTTER

I can totally see that. It's a tiny parasitic catfish. It's known as the toothpick fish.

GRAHAM CLULEY

Ooh.

LIANNE POTTER

And reputedly, if you take a wee in Amazon, the river, not Jeff Bezos's gaff—

GRAHAM CLULEY

Although, I mean, frankly, if you've got the choice—

LIANNE POTTER

Well, if you've got the choice.

GRAHAM CLULEY

Smashing Security, episode 489, How a Brand New Crypto Wallet Came with a Spy Inside, with Graham Cluley and special guest Lianne Potter.

Hello, hello, and welcome to Smashing Security, episode 489. My name's Graham Cluley.

LIANNE POTTER

And I'm Lianne Potter.

GRAHAM CLULEY

Lianne, welcome back to the show.

LIANNE POTTER

Hi.

GRAHAM CLULEY

Super to see you and to hear your dulcet tones as well.

LIANNE POTTER

Well, you know, the fans ask for it all the time, I'm sure. They do.

GRAHAM CLULEY

They always say, we've had the King of the North, obviously, who's entered Downing Street now, but are you the Cyber Queen of the North? Have you branded yourself in any way?

You're from Yorkshire, right?

LIANNE POTTER

Correct. Correct. So a bit of a War of the Roses thing going on there with that reference to Burnham. But we will slide past that.

If you want to call me the Queen of the North, I'll take it.

GRAHAM CLULEY

For anyone who's not British, Yorkshire, practically in the Arctic Circle.

LIANNE POTTER

Practically, yes. That's why I'm wearing a cardigan. But the heating is not on yet, which is also very Yorkshire.

GRAHAM CLULEY

Oh, yes. Well done to you. Before we kick off, let's thank this week's wonderful sponsors, 360 Privacy, Origin, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security. We're not gonna be talking about how a cyberattack hit Romania's stock market agency.

Unknown

You'll hear no discussion of—

GRAHAM CLULEY

How a Ukrainian hacktivist defaced Russia's school testing system. And we won't even mention how police are claiming scammers used AI to deepfake a sheriff's voice.

So, Lianne, what are you going to be talking about this week?

LIANNE POTTER

So you buy one washing machine, and then for months the internet thinks that's your entire personality.

But that washing machine ad might not just want your money, it might also want access to your phone.

GRAHAM CLULEY

And we're gonna play Click or Treat and discover your crypto wallet may not be as safe as you imagine.

Plus, we've got a featured interview with Spencer Thompson of Origin, who reveals what AI agents are really getting up to on your employees' laptops when nobody is watching.

All this and much more coming up in this episode of Smashing Security.

GRAHAM CLULEY

Earlier this year, oh, here we go.

JOE

Inside the walls of OpenAI, inside Hugging Face, something was happening.

Agents talking to each other, dividing the work between themselves, leaving notes for one another in the dark where no human was watching.

GRAHAM CLULEY

They're AI agents doing a code review, Graham.

JOE

It's not the Manhattan Project. And when the sun came up on that incident, the finest engineering minds on the planet sat in a room and asked themselves one question.

GRAHAM CLULEY

What did our AI do?

JOE

They didn't know.

GRAHAM CLULEY

The people who built the machine didn't know what the machine had done.

JOE

And that brings us to you, dear listener. One question, and I want you to think about this.

If an AI agent caused an incident at your company tomorrow, what evidence could you actually produce?

GRAHAM CLULEY

Because the terrible truth is, most of us have the prompt.

JOE

We have the result.

GRAHAM CLULEY

But what goes on in the middle?

JOE

No clue.

GRAHAM CLULEY

The commands it ran, the files it touched, the credentials it helped itself to — all of it gone.

JOE

But not anymore, because there is a sensor on the machine watching, always recording, capturing everything the agent does as one unbroken trace. What was asked?

What it reached, what it changed, laid out in order, start to finish.

GRAHAM CLULEY

This is Origin, endpoint AI observability.

JOE

Origin sees the agents that other tools walk straight past. Coding agents in a terminal, local agents, anything whispering to an MCP server on a laptop.

No cloud gateway, no blind spot. Origin is already there.

GRAHAM CLULEY

Somewhere right now, an agent is doing something nobody asked it to do.

JOE

But this time, someone will be able to prove it.

GRAHAM CLULEY

Origin — originhq.com/smashing.

JOE

That's originhq.com/smashing. And thanks to Origin for supporting the show. Now, chums, chums, w...