---
title: Smashing Security podcast #482: This hacker leaked GTA 6 – and launched their own cryptocurrency
url: https://grahamcluley.com/smashing-security-podcast-482/
source: GRAHAM CLULEY
date: 2026-08-26
fetch_date: 2026-08-27T12:14:31.146028
---

# Smashing Security podcast #482: This hacker leaked GTA 6 – and launched their own cryptocurrency

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

# Smashing Security podcast #482: This hacker leaked GTA 6 – and launched their own cryptocurrency

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:10 am, August 27, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #482: This hacker leaked GTA 6 - and launched their own cryptocurrency](https://grahamcluley.com/wp-content/uploads/2026/08/ss-episode-482.webp)

A hacker calling themselves “CYBERLEEK” has been leaking gameplay footage from GTA 6 ahead of its official reveal this week – but they’re not asking Rockstar Games for a ransom. Instead, they’ve launched their own cryptocurrency, promising to release ever more juicy clips from a virtual strip club…

Meanwhile, your smart TV might be doing more than binge-watching Netflix while you sleep. We explore the shadowy world of “residential proxies” – how they end up inside home routers, smart TVs, and IoT devices, and why an entire criminal economy is quietly running through your internet connection.

All this and more in episode 482 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Paul Ducklin.

[![Podcast artwork](https://media.redcircle.com/images/2026/8/26/13/000a2cf6-697c-454d-b8e4-ba79212d5d92_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #482

### [This hacker leaked GTA 6 - and launched their own cryptocurrency](https://www.smashingsecurity.com/482)

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

He takes his gun and he sort of shoots the word leek, L-E-E-K. I apologise to any English teachers who are listening to this, into a wall as if to prove it really is him.

PAUL DUCKLIN

Leek is a legitimate word. I mean, it's a type of onion. What's wrong with that?

GRAHAM CLULEY

Well, I suppose so.

PAUL DUCKLIN

I mean, Cyber Onion wouldn't sound great, but Cyber Leek—

GRAHAM CLULEY

It wouldn't be so good.

PAUL DUCKLIN

It is a pun, Graham, whether you approve of it or not.

Unknown

Smashing Security, episode 482.

PAUL DUCKLIN

This hacker leaked GTA 6 and launched their own cryptocurrency with Graham Cluley and special guest Paul Ducklin.

Unknown

Hello, hello, and welcome to Smashing Security, episode 482. My name's Graham Cluley.

PAUL DUCKLIN

And I am Paul Ducklin. Hello, Duck.

GRAHAM CLULEY

Great to have you back on the show again.

PAUL DUCKLIN

Thank you, Graham.

GRAHAM CLULEY

We parachuted you in this week actually, 'cause that person we were intending to come on hasn't managed. Not that you are by any means a pale substitute.

PAUL DUCKLIN

I'm not pale at all these days. We've had so much sunshine.

GRAHAM CLULEY

No, that's true.

PAUL DUCKLIN

As you can see, I've had a bit too much lately, if those of us who can see me on video.

GRAHAM CLULEY

Well, it's always great to have you here. Before we kick off, let's thank this week's wonderful sponsors, ThreatLocker, BlackKite, and Vanta.

We'll be hearing more about them later on in the podcast. This week on Smashing Security.

We're not going to be talking about how Iranian hackers managed to shut down a UK power plant.

PAUL DUCKLIN

You'll hear no discussion of—

GRAHAM CLULEY

How a ransomware crook silently ripped off his own gang by posing as a recovery firm and pocketed the victims' payments for himself.

And we won't even mention how the Toxic Panda Trojan is quietly taking over Android phones to steal banking PINs and passwords.

Now, Duck, what are you going to be talking about this week?

PAUL DUCKLIN

Well, Graham, if your smart TV isn't spying on you, what else might it be doing behind your back?

GRAHAM CLULEY

And the tyres are going to be hitting the tarmac as I enter the world of Grand Theft Auto 6. All this and much more coming up in this episode of Smashing Security.

Unknown

This episode of Smashing Security is supported by ThreatLocker. Agentic AI is beginning to change the tempo of cyberattacks.

GRAHAM CLULEY

That's right. We've seen research into autonomous ransomware, adaptive AI worms, and agents chaining tools without waiting for a human operator.

Unknown

Which is all very interesting, just so long as it isn't your network they're experimenting on.

GRAHAM CLULEY

When enumeration, exploitation, and lateral movement happen at machine speed, relying on somebody to notice an alert and respond quickly begins to look rather optimistic.

Well, ThreatLocker puts default deny and least privilege between the agent and its next action.

So application allowlisting controls execution, ring-fencing restricts what trusted applications can access or launch, and privileged access management removes unnecessary elevation.

Unknown

The attacker may be moving faster, but the controls are already in place. Agentic AI doesn't make established security principles obsolete.

It makes getting them right considerably more urgent.

GRAHAM CLULEY

So make sure that you are prepared for machine speed attacks with ThreatLocker. Visit threatlocker.com/smashing today to learn more and schedule your free demo.

Unknown

That's threatlocker.com/smashing. And thanks to ThreatLocker for supporting the show.

GRAHAM CLULEY

Now, chums, chums, Grand Theft Auto. It's one of the most successful entertainment products ever made. Duck, have you ever played Grand Theft Auto?

PAUL DUCKLIN

No, because when I had my own grand theft bicycle from outside my own flat—

GRAHAM CLULEY

Yes.

PAUL DUCKLIN

That was enough to convince me that this is not a laughing matter, Graham.

GRAHAM CLULEY

No, no, not a laughing matter.

PAUL DUCKLIN

I mean, it's more than a year ago. I'm almost over it now.

GRAHAM CLULEY

I've never played Grand Theft Auto.

PAUL DUCKLIN

I've seen it.

GRAHAM CLULEY

Yes, exactly. I've seen it. I've looked over people's shoulders while they're playing it, and it does seem very impressive. It's a huge, open-world game.

It's all about a life of crime. It has earned over $8 billion — billion with a B — since it launched in 2013. It's made more cash than any Hollywood movie.

It's still being played by millions of people more than a decade later. And that's really a testament to how m...