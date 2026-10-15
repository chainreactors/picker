---
title: Smashing Security podcast #488: How a ransomware negotiator ended up arrested at his own conference
url: https://grahamcluley.com/smashing-security-podcast-488/
source: GRAHAM CLULEY
date: 2026-10-14
fetch_date: 2026-10-15T06:45:43.693707
---

# Smashing Security podcast #488: How a ransomware negotiator ended up arrested at his own conference

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

# Smashing Security podcast #488: How a ransomware negotiator ended up arrested at his own conference

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:06 am, October 15, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #488: How a ransomware negotiator ended up arrested at his own conference](https://grahamcluley.com/wp-content/uploads/2026/10/ss-episode-488.webp "Smashing Security podcast #488: How a ransomware negotiator ended up arrested at his own conference")

A ransomware negotiator attended a cybersecurity conference, only to be arrested by the FBI in connection with its investigation into the ShinyHunters gang.

Meanwhile, hackers get the keys to ASOS’s app and the chance to message every single customer. What did they say? And how did the company respond? We have thoughts.

All this and more is discussed in episode 488 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Paul Ducklin.

[![Podcast artwork](https://media.redcircle.com/images/2026/10/12/17/f78c01d1-e4c3-44ed-bf19-6bc89188d5b5_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #488

### [How a ransomware negotiator ended up arrested at his own conference](https://www.smashingsecurity.com/488)

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

GRAHAM CLULEY

Well, it could be unfashionable trousers.

PAUL DUCKLIN

Yeah, I suppose.

GRAHAM CLULEY

There is the potential for some sort of social embarrassment, maybe. When I was at school, I had some cord trousers, which these days would be very, very trendy.

But back when I was wearing them in the 1980s, they certainly weren't.

PAUL DUCKLIN

Yeah, there was no normcore back then, was there? Corduroy trousers. Yes, I had some when I was about 12, and I thought they were great.

But I quickly learned that that was not quite the case.

Unknown

Smashing Security, episode 488.

PAUL DUCKLIN

How a ransomware negotiator ended up arrested at his own conference, with Graham Cluley and special guest Paul Ducklin.

GRAHAM CLULEY

Hello, hello, and welcome to Smashing Security, episode 488. My name's Graham Cluley.

PAUL DUCKLIN

And I am Paul Ducklin.

GRAHAM CLULEY

Duck, welcome back to the show. Always a pleasure to have you here.

PAUL DUCKLIN

Always a pleasure to be on the show, Graham. It's fun. With a serious side, and I like both of those things.

GRAHAM CLULEY

Ah, fantastic. Well, before we kick off, let's thank this week's sponsors, HackTheBox, Origin, and Vanta. We'll be hearing more about them later on in the show.

PAUL DUCKLIN

This week on Smashing Security.

GRAHAM CLULEY

We're not gonna be talking about how the password 123456 let a hacker steal the details of 8.8 million people from Denmark's National Population Register.

You'll hear no discussion of How scammers are filling your calendar with fake meeting invites to phish you.

And we won't even mention— How Anthropic's AI sent Philadelphia police a made-up tip about an unsolved murder. So, Duck, what are you going to be talking about this week?

PAUL DUCKLIN

I am going to be asking the question, metaphorically of course, if you hacked into an industry giant and you had the chance to send a message to every single customer, what Would you tell them?

GRAHAM CLULEY

And I'm gonna be discussing the 7 degrees of separation between me and a ransomware gang. I say 7 degrees, it's probably more like 2.

All this and much more coming up in this episode of Smashing Security. Earlier this year.

JOE

Oh, here we go.

GRAHAM CLULEY

Inside the walls of OpenAI, inside Hugging Face, something was happening.

Agents talking to each other, dividing the work between themselves, leaving notes for one another in the dark where no human was watching.

JOE

They're AI agents doing a code review, Graham. It's not the Manhattan Project.

GRAHAM CLULEY

And when the sun came up on that incident, the finest engineering minds on the planet sat in a room and asked themselves one question.

JOE

What did our AI do? They didn't know. The people who built the machine didn't Know what the machine had done.

GRAHAM CLULEY

And that brings us to you, dear listener. One question, and I want you to think about this.

JOE

If an AI agent caused an incident at your company tomorrow, what evidence could you actually produce?

Because the terrible truth is, most of us have the prompt, we have the result, but what goes on in the middle? No clue.

The commands it ran, the files it touched, the credentials it helped itself to, all of it gone.

GRAHAM CLULEY

But not anymore.

JOE

Because there is a sensor.

GRAHAM CLULEY

On the machine, watching, always recording, capturing everything the agent does as one unbroken trace.

What was asked, what it reached, what it changed, laid out in order, start to finish.

JOE

This is Origin, endpoint AI observability.

GRAHAM CLULEY

Origin sees the agents that other tools walk straight past. Coding agents in a terminal, local agents, anything whispering to an MCP server on a laptop.

No cloud gateway, no blind spot. Origin is already there.

JOE

Somewhere right now, an agent is doing something nobody asked it to do.

GRAHAM CLULEY

But this time, someone will be able to prove it.

JOE

Origin. originhq.com/smashing.

GRAHAM CLULEY

That's originhq.com/smashing. And thanks to Origin for supporting the show. Now, chums, chums, imagine that you have written a book. Duck, have you ever written a book?

PAUL DUCKLIN

I have written part of a book, but in the modern AI era, self-publishing things, some fun stuff about malware, seems to be rather difficult.

So I'm biding my time, Graham, if I may say so.

GRAHAM CLULEY

Yeah, it's a tricky vocation these days, isn't it? But imagine you had written a book, 252 pages in fact, called Cyber Extortion Strategic Response. Very catchy name.

And according to its listing on Amazon, one of the key messages of the book is that talking to a cybercriminal isn't the same as negotiating a payment to a cybercriminal.

And furthermore, it says that nego...