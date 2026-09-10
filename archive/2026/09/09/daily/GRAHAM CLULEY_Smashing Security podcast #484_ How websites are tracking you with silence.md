---
title: Smashing Security podcast #484: How websites are tracking you with silence
url: https://grahamcluley.com/smashing-security-podcast-484/
source: GRAHAM CLULEY
date: 2026-09-09
fetch_date: 2026-09-10T06:53:02.092241
---

# Smashing Security podcast #484: How websites are tracking you with silence

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

# Smashing Security podcast #484: How websites are tracking you with silence

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:05 am, September 10, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #484: How websites are tracking you with silence](https://grahamcluley.com/wp-content/uploads/2026/09/ss-episode-484.webp "Smashing Security podcast #484: How websites are tracking you with silence")

When a chap called Matt noticed his Bluetooth headphones wouldn’t switch to his phone, he was surprised to realise the reason was a single AliExpress webpage sitting open in his browser – playing nothing at all, at zero volume. And yet somehow his hardware could hear it. Audio fingerprinting is one of the sneakiest tracking tricks on the web.

Meanwhile, the intelligence agencies of the “Five Eyes” (not Five Guys) have got together and published advice on how companies should communicate after a cyber attack. The summary? For the love of God, stop calling every breach “sophisticated.”

All this and more in episode 484 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Danny Palmer.

[![Podcast artwork](https://media.redcircle.com/images/2026/9/9/17/8dcd83d0-ac0e-43c4-b2a8-27223dc2340b_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #484

### [How websites are tracking you with silence](https://www.smashingsecurity.com/484)

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

As I'm sure you've seen, in many cases a company will put out a rather generic statement saying they've been hit by a sophisticated cyberattack.

Unknown

Yeah, no one wants to get hit by a dumb attack, do they? No one wants to. No.

Smashing Security, episode 484: How Websites Are Tracking You with Silence with Graham Cluley and special guest Danny Palmer.

Hello, hello, and welcome to Smashing Security episode 484. My name's Graham Cluley.

DANNY PALMER

And I'm Danny Palmer.

GRAHAM CLULEY

Danny, thank you so much for joining us once again. Always a pleasure to see you here on the podcast.

DANNY PALMER

My pleasure. Thanks for having me once more.

GRAHAM CLULEY

Terrific to have you here. Well, before we kick off, let's thank this week's wonderful sponsors, ThreatLocker, Intruder, and Vanta.

We'll be hearing more about them later on in the podcast.

DANNY PALMER

This week on Smashing Security.

GRAHAM CLULEY

We won't be talking about how Berlin city government's ransomware attack started with a fake Cloudflare CAPTCHA.

DANNY PALMER

You'll hear no discussion of—

GRAHAM CLULEY

How France has arrested 2 suspects for hacking the country's tax agency. And we won't even mention how hackers are stealing Claude tokens from subscribers.

So Danny, what are you going to be talking about this week?

DANNY PALMER

I'll be talking about new advice from cyber intelligence agencies which encourages companies which fall victim to cyberattacks to avoid using PR fluff to describe what happened.

GRAHAM CLULEY

And I'll be finding out how the sound of silence could be helping to track you across the internet. All this and much more coming up on this episode of Smashing Security.

JOE

This episode of Smashing Security is supported by ThreatLocker. Agentic AI is beginning to change the tempo of cyberattacks.

GRAHAM CLULEY

Ransomware that thinks for itself, worms that rewrite their own playbook mid-attack, agents happily chaining exploits together without ever pausing to ask a human, is this alright?

JOE

Which is all very interesting, just so long as it isn't your network they're experimenting on.

GRAHAM CLULEY

And that's the problem.

When a machine can scope out your network, break in, and start creeping sideways through it faster than you can finish your coffee, you can't rely on the hope that someone will notice the alert eventually.

And this is where ThreatLocker earns its keep. Default deny and least privilege sit right in the agent's path, so nothing runs just because it asks nicely.

Application allowlisting decides what's even allowed to execute. Ring-fencing keeps trusted apps from wandering off and touching things they shouldn't.

JOE

And privileged access management quietly confiscates the elevated access. The attacker may be moving faster, but the controls are already in place.

Agentic AI doesn't make established security principles obsolete. It makes getting them right considerably more urgent.

GRAHAM CLULEY

So while the attacks are picking up speed, make sure ThreatLocker is already standing in the way. Head to threatlocker.com/smashing to find out more and grab your free demo.

JOE

That's threatlocker.com/smashing. And thanks to ThreatLocker for supporting the show.

GRAHAM CLULEY

Now, Danny, quick question for you before we get started today. How good is your hearing? Have you got quite good hearing?

DANNY PALMER

I don't think I do, you know, which is not a great thing because my eyesight is terrible to begin with.

So you'd hope that my ears would pick up a bit more, like Daredevil, the superhero. He's blind and he can hear and sense things really well.

GRAHAM CLULEY

Yes.

DANNY PALMER

I don't have that ability. I get by in the world, but I don't think you need me for listening for something really, really far away.

GRAHAM CLULEY

Maybe you have another super sense though. Even if your eyesight isn't that great and your hearing isn't that great, maybe you got, I dunno, a fantastic sense of taste.

DANNY PALMER

I can identify certain types of food. I'm not talking about, oh, that's a curry and that's spaghetti.

But no, I could probably tell you what sort of beer was what, vaguely, if you gave me some blind tasting. But no, nothing useful there, I'm afraid.

GRAHAM CLULEY

Well, I'm not gonna give you a beer-related game today. Instead, what I'm gonna do is I'm gonna play you a string of short sounds. And I want you to tell me what they are.

And this is a game that I like to call Name That Chime. Listeners, you can play along as well and see how you do compared to Danny. So Danny, are you ready for round 1?

DANNY PALMER

I am ready....