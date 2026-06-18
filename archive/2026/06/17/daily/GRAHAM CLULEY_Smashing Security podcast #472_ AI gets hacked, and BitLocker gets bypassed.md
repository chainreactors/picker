---
title: Smashing Security podcast #472: AI gets hacked, and BitLocker gets bypassed
url: https://grahamcluley.com/smashing-security-podcast-472/
source: GRAHAM CLULEY
date: 2026-06-17
fetch_date: 2026-06-18T06:52:00.275355
---

# Smashing Security podcast #472: AI gets hacked, and BitLocker gets bypassed

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

# Smashing Security podcast #472: AI gets hacked, and BitLocker gets bypassed

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:10 am, June 18, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #472: AI gets hacked, and BitLocker gets bypassed](https://grahamcluley.com/wp-content/uploads/2026/06/ss-episode-472.webp)

What if your AI coding assistant could be tricked into stealing your own company’s secrets – by reading a single booby-trapped bug report? No phishing email. No malware. No password ever stolen. Just an AI doing exactly what it was told.

Meanwhile, someone calling themselves Nightmare Eclipse has decided to teach Microsoft a lesson. The result? Three zero-days dropped on the internet, one of which lets a thief with a USB stick walk straight past BitLocker. Microsoft is furious.

Plus don’t miss our featured interview with Son Nguyen Kim of Proton Pass, who explains why plugging AI agents into your email and calendar without thinking twice is rather like hiring a new employee with the keys to everything – and skipping the background check.

All this and more in episode 472 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Paul Ducklin.

[![Podcast artwork](https://media.redcircle.com/images/2026/6/16/16/aa5f34b1-bf18-4cb0-87b6-a80f51725304_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #472

### [AI gets hacked, and BitLocker gets bypassed](https://www.smashingsecurity.com/472)

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

PAUL DUCKLIN

How does that poem go? Great fleas have lesser fleas upon their backs to bite them, and lesser fleas have smaller fleas, and so ad infinitum.

Unknown

Finally, some culture on the program. Hahaha. Smashing Security, episode 472. AI gets hacked, and BitLocker gets bypassed. With Graham Cluley and special guest Paul Ducklin.

Hello, hello, and welcome to Smashing Security episode 472. My name's Graham Cluley.

PAUL DUCKLIN

And my name is Paul Ducklin.

GRAHAM CLULEY

Hello, Duck. How are you?

PAUL DUCKLIN

I'm great, Graham. Thank you very much.

GRAHAM CLULEY

Well, it's fabulous to have you back on the show yet again. Of course, both of us, we've been at this a long time, haven't we?

I think over 60 years combined, maybe, in cybersecurity. Would that be right?

PAUL DUCKLIN

I think that's putting it kindly to both of us, erring on the side of making us sound younger than perhaps we are.

GRAHAM CLULEY

Well, before we kick off, let's thank this week's wonderful sponsors: ProtonPass, CoreView, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security, we're not going to talk about how Cisco, the world's largest food distributor, has been hit by an extortion threat from hackers, the second one in just a few weeks.

You'll hear no discussion of how a UK police officer is being investigated for allegedly using AI to fabricate evidence.

And we won't even mention how someone used Maine's official data breach portal to file completely fake data breaches. So, Duck, what are you going to be talking about this week?

PAUL DUCKLIN

I am going to be talking about bug disclosure and whether we really want to go back to the bad old days of 1999.

GRAHAM CLULEY

And I'm going to be talking about how your AI tools can be hijacked to leak passwords without a single phishing email or malware involved in the process.

Plus, don't miss our featured interview with Son Nguyen Kim of ProtonPass about the hidden security risks of AI agents and why connecting them to your email or calendar without a second thought could be handing attackers the keys to your business.

All this and much more coming up on this episode of Smashing Security. This episode is sponsored by ProtonPass.

JOE

ProtonPass, the password manager from the team behind ProtonMail, the world's largest end-to-end encrypted email service.

GRAHAM CLULEY

Now, Joe, you and I both know the grubby little secret of how a lot of businesses actually share passwords.

JOE

A spreadsheet? A Post-it note? Sending it to a colleague via Slack and hoping for the best?

GRAHAM CLULEY

That's pretty much it. All of the above. And every one of them is a breach waiting to happen. ProtonPass is built to fix exactly that.

Letting teams store and share credentials securely with end-to-end encryption baked into every feature.

JOE

It's open source and fully auditable. It runs on Swiss infrastructure, so your data sits outside US jurisdiction, and it's backed by a nonprofit.

No venture capitalists, no pressure to chase a quick exit.

GRAHAM CLULEY

Which is the bit I like. You know, it's built to serve you, not investors.

So it will never be pressured to cut security corners or rush towards a liquidity event that could change ownership, pricing, or priorities overnight.

It's trusted by over 100 million people, ISO 27001 certified, SOC 2 audited, and it helps you tick the boxes for NIST 2, DORA, and the UK's Cybersecurity and Resilience Bill.

JOE

And crucially, people actually use it. One Swiss customer told Proton, and I quote, "It works. It works perfectly." High praise indeed.

GRAHAM CLULEY

So why not start your business's free trial right now at proton.me/smashing.

JOE

And thanks to Proton Pass for supporting the show.

GRAHAM CLULEY

Now, chums, I want to talk today about a type of attack which, like I said, doesn't require any malware, doesn't rely upon a stolen password, where there's no phishing emails, no bypass of your antivirus or a firewall or any other security tool you could have paid good money for.

It works by turning your AI coding assistant against you. Duck, where do you stand on AI coding assistants?

PAUL DUCKLIN

Graham, I tend not to stand. My choice is to sit down and to hold on to my chair very, very firmly after bolting it to the floor. Right.

I think the problem is that they're not so much assistants anymore, are they? They're replacements.

They're, hey, look something up, get some results and turn data into code and run it. What could possibly go wrong?

GRAHAM CLULE...