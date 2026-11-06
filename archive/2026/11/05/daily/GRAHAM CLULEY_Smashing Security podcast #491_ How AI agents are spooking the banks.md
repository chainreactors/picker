---
title: Smashing Security podcast #491: How AI agents are spooking the banks
url: https://grahamcluley.com/smashing-security-podcast-491/
source: GRAHAM CLULEY
date: 2026-11-05
fetch_date: 2026-11-06T08:42:05.103369
---

# Smashing Security podcast #491: How AI agents are spooking the banks

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

# Smashing Security podcast #491: How AI agents are spooking the banks

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:15 am, November 5, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #491: How AI agents are spooking the banks](https://grahamcluley.com/wp-content/uploads/2026/11/ss-episode-491.webp "Smashing Security podcast #491: How AI agents are spooking the banks")

Bank of America has a message for its customers: please, for the love of God, stop handing your banking passwords to your AI assistant. And if your robot does something daft with your money? That’s your problem, not theirs.

Meanwhile, a company that promised to rescue ransomware victims without paying the criminals stands accused of… paying the criminals. ProPublica’s Renee Dudley was on the case years before the indictment.

Plus, Dropzone AI’s Edward Wu asks what happens when AI models break out of their test environment and go hacking, and whether AI agents can help overstretched security teams keep up.

All this and more in episode 491 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Renee Dudley.

[![Podcast artwork](https://media.redcircle.com/images/2026/11/4/23/c701b48a-49d9-4668-91ec-d0d626bcc7f5_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #491

### [How AI agents are spooking the banks](https://www.smashingsecurity.com/491)

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

And you get this, hello, I am definitely a human. Can you help me? To be honest, it wouldn't be a surprise if it's one robot talking to another robot.

When are humans going to start talking to each other again? Smashing Security, episode 491, How AI Agents Are Spooking the Banks, with Graham Cluley.

Hello, hello, and welcome to Smashing Security, episode 491. My name's Graham Cluley.

RENEE DUDLEY

I'm Renee Dudley.

GRAHAM CLULEY

Hey, Renee, welcome to the show. Lovely to have you on. First time on Smashing Security.

RENEE DUDLEY

Yes, long-time listener, first-time caller.

GRAHAM CLULEY

So for anyone who doesn't know who you are, Renee, explain yourself.

RENEE DUDLEY

I'm a reporter at the New York-based investigative news outlet ProPublica, where I report on technology and cybersecurity.

For those who don't know, ProPublica is an investigative news site. We tend to take one topic and focus on it for a long time.

GRAHAM CLULEY

And for a while, your topic was ransomware, wasn't it?

RENEE DUDLEY

Very much.

GRAHAM CLULEY

You even did a podcast about ransomware as well.

RENEE DUDLEY

I did a podcast about ransomware. I even wrote an entire book about ransomware. So when I mean we stick with the topic for a long time, I mean literally years in some cases.

GRAHAM CLULEY

Very cool. Well, before we kick off, let's thank this week's wonderful sponsors, HackTheBox, DropZone AI, and Vanta. We'll be hearing more about them this week on Smashing Security.

We won't be talking about how fake job interviews helped hackers steal $6.34 billion from Binance.

You'll hear no discussion of how GCHQ has lost track of thousands of USB sticks and external hard drives.

And we won't even mention how it's not just supermarkets who've had their freezers hacked. Ones at US military bases are malfunctioning too.

So Renee, what are you going to be talking about this week?

RENEE DUDLEY

I will be talking about a Florida man who was recently indicted on federal charges in the US of defrauding clients of his ransomware data recovery business.

GRAHAM CLULEY

And I'm going to be discussing how AI agents have started calling banks on your behalf without asking.

Plus, we'll have a featured interview with Edward Wu of Dropzone AI to discuss what happens when AI models break out of their test environments and go hacking, and whether AI agents can help overstretched security teams keep up with attacks happening at unprecedented speed.

All this and much more coming up on this episode of Smashing Security.

GRAHAM CLULEY

This episode of Smashing Security is sponsored by Dropzone AI.

GRAHAM CLULEY

Ladies and gentlemen, welcome to Alert Quiz. Our contestant today is Joe. Joe, are you ready?

JOE

I think so.

GRAHAM CLULEY

Right then. Question 1 for 10 points. What is a security alert?

JOE

It's a flag that something might be wrong.

JOE

Correct. Question 2, give me an example.

JOE

Someone's lost their lanyard.

GRAHAM CLULEY

Oh dear, oh dear, oh dear. Answers I would've accepted include an odd sign-in from abroad or someone clicking a dodgy-looking email.

Question 3, what does each alert need before anyone knows that it matters?

JOE

Crumbs. A person pulling evidence from several different tools.

GRAHAM CLULEY

Correct! And when there are more alerts than hours in the day, some of them—

JOE

Get ignored?

JOE

Correct! Right, bonus question. What is Dropzone AI?

JOE

Ah, I know this. It's a collective of specialised AI agents that investigates every alert start to finish around the clock using the tools your team already has.

GRAHAM CLULEY

10 bonus points. And what do analysts get when they run Dropzone AI?

JOE

A vague something's up?

GRAHAM CLULEY

No, Joe, that's what they get now. With Dropzone AI, they get a finding with the reasoning and evidence already assembled. It shows its work.

So checking a finding becomes a decision rather than a second investigation. And who decides where the agents stop?

GRAHAM CLULEY

The agents?

GRAHAM CLULEY

No, Joe, the team decides where the agents stop and the analysts own every verdict. Now, final, final question. Finish this quote.

Kevin Turnbull, Global IT Director at Asala Energy, says, with Dropzone, we don't get this is a problem.

JOE

We get, this is a problem, and here's why. Huzzah!

GRAHAM CLULEY

Correct, Joe. You have won the self-guided demo, and what's more, so has everyone who's listening. To watch a real investigation unfold, go to smashingsecurity.com/dropzoneai.

JOE

That's smashingsecurity.com/dropzoneai.

GRAHAM CLULEY

Dropzon...