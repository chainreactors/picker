---
title: Smashing Security podcast #465: This developer wanted to cheat at Roblox. It cost millions
url: https://grahamcluley.com/smashing-security-podcast-465/
source: GRAHAM CLULEY
date: 2026-04-29
fetch_date: 2026-04-30T05:30:45.154134
---

# Smashing Security podcast #465: This developer wanted to cheat at Roblox. It cost millions

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

# Smashing Security podcast #465: This developer wanted to cheat at Roblox. It cost millions

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:15 am, April 30, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #465: This developer wanted to cheat at Roblox. It cost millions](https://grahamcluley.com/wp-content/uploads/2026/04/ss-episode-465.webp)

A developer at an AI startup wanted to cheat at Roblox. They downloaded a dodgy script on their work laptop. That one decision triggered a cascade of failures that ended with a $2 million data breach affecting hundreds of thousands of organisations. All for some free in-game currency.

Meanwhile, there’s a 1980s phone protocol called SS7 that lets shadowy surveillance companies track anyone, anywhere, via their mobile phone. Governments know about it. Telecoms know about it. Nobody’s fixing it.

All this and more in episode 465 of the “Smashing Security” podcast with cybersecurity keynote speaker and industry veteran Graham Cluley, joined this week by special guest James Ball.

Plus! Don’t miss our featured interview with Rob Edmondson of CoreView, discussing how to lock down Microsoft 365 before it’s too late.

[![Podcast artwork](https://media.redcircle.com/images/2026/4/29/13/b4789322-5042-49ff-a272-23588ea8e96e_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #465

### [This developer wanted to cheat at Roblox. It cost millions](https://www.smashingsecurity.com/465)

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

JAMES BALL

What's the security analogy? It's a Swiss cheese. The idea being that Swiss cheese has holes in it, but you get more and more layers of it in the hopes that the holes won't line up.

Unknown

Smashing Security, episode 465. Smashing Security 465. This developer wanted to cheat at Roblox.

JAMES BALL

It cost millions.

Unknown

With Graham Cluley and special guest James Ball. Hello, hello, and welcome to Smashing Security episode 465. My name's Graham Cluley.

JAMES BALL

And I'm James Ball.

GRAHAM CLULEY

James, welcome back on the show. Lovely to have you on yet again. What have you been up to?

JAMES BALL

I've been running around all over the place. I spend about half my week being a political journalist and the other half working on tech. And the political half is really creeping up.

GRAHAM CLULEY

It's a crazy world politically.

You know, I had some feedback from a listener just in the last couple of days actually saying, you love the podcast, been listening to the podcast forever, but oh my God, Graham, can you stop talking about politics?

And my reaction was, look, thank you very much for listening and all the rest of it, but it feels to me that technology and politics are more intertwined than ever before.

You can't really extract them from each other, can you?

JAMES BALL

I mean, horribly so. It feels a bit like a monkey's paw thing. You know, I've been interested in tech since I was a kid.

I've sort of always gone, I wish people would pay more attention to this. This is transformative. I sort of came of age with the internet.

You're kind of going, no, we need to look at this. This is really huge.

And now tech and politics have merged so much and are in the discourse so much and are crashing together in so many ways. It's I was really stupid to want this.

Why can't this go back to being in its nice own lovely corner where I can just think about how the technology works or, you know, the principles of it instead of what stupid way is this going to be used to upend our politics yet again?

Unknown

Yeah.

GRAHAM CLULEY

And the world of technology has become so huge that the people in charge of these technological companies have an enormous amount of influence over our politicians.

How can you extricate them? I don't know that you can.

JAMES BALL

I mean, we haven't had this kind of dominance really since you look back at the Gilded Age.

It's when the railway monopolies were there or the early oil monopolies, because the biggest companies and the biggest tech companies is synonymous.

9 of the world's 10 biggest listed companies are tech companies. Essentially, this domination by one sector is pretty much unheard of in either of our lifetimes.

And so politics is going to be weird until tech is kind of normal again. And that might be bad for someone who reports on and covers tech, but might be good for the world.

It might be good for our blood pressure and it might be good for your listener. I promise I haven't brought a load of political things this week.

Well, not very political, small p political.

GRAHAM CLULEY

One thing I will say to any other listeners who are concerned about this as well is if they're doing the wrong thing, I'm gonna have a go at them regardless of what side of the political chamber they might be on.

Well, before we kick off, let's thank this week's wonderful sponsors, CoreView, Elastic, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security, we won't be talking about how home security firm ADT has been burgled by the Shiny Hunters gang.

You'll hear no discussion of how ransomware negotiator has pleaded guilty to helping hackers by leaking victims' insurance details.

And we won't even mention how Elon Musk's Grok chatbot told researchers pretending to be delusional that there was indeed a doppelganger in their mirror and they should drive an iron nail through the glass while reciting a psalm backwards.

So James, what are you going to be talking about this week?

JAMES BALL

So this week I want to talk about how wronguns are still tracking us on our mobile phones and why this is proving so intractably difficult to sort out.

GRAHAM CLULEY

And I'm going to be talking about a corporate hack that all started because someone wanted to cheat at Roblox. Plus, we're going to be talking to Rob Edmondson of CoreView.

He'll be joining us as we take a look at how hackers have been turning essential tools like Microsoft 365 against their targets and what you can do to lock down your environments before it's too late.

All this and much more coming up on this episode of Smashing Security.

JOE

This episode of Smashing Security is brought t...