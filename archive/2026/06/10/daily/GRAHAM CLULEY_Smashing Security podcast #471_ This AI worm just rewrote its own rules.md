---
title: Smashing Security podcast #471: This AI worm just rewrote its own rules
url: https://grahamcluley.com/smashing-security-podcast-471/
source: GRAHAM CLULEY
date: 2026-06-10
fetch_date: 2026-06-11T06:37:01.899674
---

# Smashing Security podcast #471: This AI worm just rewrote its own rules

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

# Smashing Security podcast #471: This AI worm just rewrote its own rules

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:15 am, June 11, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #471: This AI worm just rewrote its own rules](https://grahamcluley.com/wp-content/uploads/2026/06/ss-episode-471.webp)

Researchers at the University of Toronto have built a worm that thinks for itself. Using free off-the-shelf AI models it works out how to break into each new computer it encounters, and hijacks the powerful ones to host its own AI brain. And then the researchers discovered their creation had quietly removed the list of machines it wasn’t supposed to attack.

Meanwhile, Meta’s shiny new AI customer support agent has been cheerfully helping hackers help themselves to other people’s Instagram accounts. Just keep asking, politely but firmly, to have a password reset sent to a different email address – and the AI will eventually agree.

All this and more in episode 471 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest James Ball.

[![Podcast artwork](https://media.redcircle.com/images/2026/6/10/14/8211c3e1-9b9c-406c-9456-f0bfba7f81cb_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #471

### [This AI worm just rewrote its own rules](https://www.smashingsecurity.com/471)

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

Hang on a minute, James. You're suggesting that Instagram ever had human support stuff?

JAMES BALL

So it was a little bit akin to rituals to summon a demon or speak to the dead.

But if you went through Meta's escalating procedures in exactly the right way on the right day of the week, wearing a yellow sash with a finger in an ear, you could actually get through to a human.

Unknown

Smashing Security, episode 471. This AI worm just rewrote its own rules. With Graham Cluley and special guest James Ball. Hello, hello, and welcome to Smashing Security episode 471.

My name is Graham Cluley.

JAMES BALL

And I'm James Ball.

GRAHAM CLULEY

James, welcome back to the show. Always a delight to have you here.

JAMES BALL

Always a pleasure to be here.

GRAHAM CLULEY

Oh, I better, before I carry on, thank everyone who came to see me speaking at Infosecurity Europe at the Excel Center last week. I was talking all about the horrors of AI.

There may be some more of that today, actually, to be honest.

I was talking about how AI can blackmail you and how the billionaires are maybe not the people to have in charge of the AI, as if having billionaires in charge of anything was actually a good idea.

But that was good fun and lovely to meet some listeners there. Now, James, you're normally busy writing for The New World and things that.

You pop up on podcasts and things, but you've also been working on a PhD, haven't you?

JAMES BALL

Yeah, I've decided I should actually know something about technology after about 15 years of covering it.

So I'm doing a PhD on how legal systems look at artificial intelligence and AI. So I'm very nervous.

I've got sort of first day at school energy because I'm presenting a paper at a PhD conference later this week.

It's not the biggest audience I've done, but it's my first time as an academic, whatever that means. So kind of terrified.

GRAHAM CLULEY

Is this about how lawyers and the law uses AI, or is this about how they regard AI?

Because there's a lot of lawyers using AI these days that may be putting some lawyers out of a job.

JAMES BALL

Yeah, it's quite fun seeing AI pop up in cases, but mine is about when governments end up hauled in front of the law.

We've had sort of surveillance cases ever since the Edward Snowden revelations that look at, hey, is it a big deal when an algorithm reads your emails instead of a human spy?

You know, does it make a difference if that algorithm is really clever or if it's random instead of fixed.

So it's cases that and comparing those to how it thinks about AI in copyright cases, because you get this kind of fascinating effect where in surveillance, lots of courts have said, well, obviously it's not as big a deal if an algorithm scans your emails as if a human reads them.

You know, it might invade your privacy, but it's less likely to. There's less protection because it's different. Right.

Whereas in copyright, a lot of the big cases so far have said, okay, an algorithm looked at 100 books, synthesized them, and came up with an output that's kind of got bits of all of them in, but not their wording.

If that's not legal for an algorithm to do, then it wouldn't be legal for a human to do. Yes. And therefore journalism would be out, authorship would be out.

So they go, well, it's the same as the human, isn't it? So therefore we've got to allow it.

GRAHAM CLULEY

Huh.

JAMES BALL

And so you've got these completely different attitudes to, oh, it's an algorithm, so it's different. Oh, it's an algorithm, so it's the same. And so I'm doing a PhD on that.

GRAHAM CLULEY

Well done. Sounds very impressive. Well, good luck speaking at this conference.

JAMES BALL

Thank you. I may need it.

GRAHAM CLULEY

Well, before we kick off, let's thank this week's wonderful sponsors, Opswat, Expo, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security. We won't be talking about how the METV Awards left its access keys out in the open for anyone to see, leaking data including award submissions.

You'll hear no discussion of how an AI agent has found over 20 zero-day vulnerabilities in FFmpeg, some of them 23 years old.

And we won't even mention how hackers have stolen $1.7 million worth of condoms after hijacking a shipment to Walmart. So James, what are you going to be talking about this week?

JAMES BALL

This week I'm talking about helpful AI, maybe too helpful AI, which is the Meta AI, which seems to have been giving anyone who asked nicely anyone else's password.

GRAHAM CLULEY

And continuing the AI theme, I'm going to be talking about an AI worm that appears to think for itself. All this ...