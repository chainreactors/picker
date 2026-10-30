---
title: Smashing Security podcast #490: How Jared Kushner’s iPhone was allegedly hacked twice
url: https://grahamcluley.com/smashing-security-podcast-490/
source: GRAHAM CLULEY
date: 2026-10-29
fetch_date: 2026-10-30T07:56:42.524691
---

# Smashing Security podcast #490: How Jared Kushner’s iPhone was allegedly hacked twice

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

# Smashing Security podcast #490: How Jared Kushner’s iPhone was allegedly hacked twice

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:16 am, October 29, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #490: How Jared Kushner's iPhone was allegedly hacked twice](https://grahamcluley.com/wp-content/uploads/2026/10/ss-episode-490.webp "Smashing Security podcast #490: How Jared Kushner's iPhone was allegedly hacked twice")

Dutch spies, Russian hackers and Jared Kushner’s iPhone. It sounds like the ingredients for a thriller, but according to claims in a new book the US President’s son-in-law may have been hacked twice. Is any of it true, and what does it tell us about the phones in our pockets?

Meanwhile, James Ball explains that of the internet’s most trusted security keys were protected by numbers so small that one of them was… four. Yes, “4”. And then, of course, to make the week worse we suffered a PHPocalpyse…

Plus, Chuck Randolph of 360 Privacy explains how the internet has made it scarily easy to put company executives and public officials in danger.

All this and more in episode 490 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest James Ball.

[![Podcast artwork](https://media.redcircle.com/images/2026/10/27/16/170461f7-f806-44a1-99dc-74cec9c1023f_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #490

### [How Jared Kushner's iPhone was allegedly hacked twice](https://www.smashingsecurity.com/490)

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

JAMES BALL

For example, for Secure DNS, every three months they do a little ceremony to renew the keys. And I've stood in and watched one of these.

GRAHAM CLULEY

Oh, wow.

JAMES BALL

And of course, once a journalist was in a room and I had a camera person with me, it all went wrong. They messed it up. They got locked in a cage.

They had to set off the fire alarm to get let out. It turned into total slapstick. Smashing Security, episode 490.

How Jared Kushner's iPhone was allegedly hacked twice, with Graham Cluley and special guest James Ball. Hello, hello, and welcome to Smashing Security, episode 490.

My name's Graham Cluley.

JAMES BALL

And I'm James Ball.

GRAHAM CLULEY

James, welcome back to the show. Super to have you.

JAMES BALL

You are suffering a little bit, not that our listeners will be able to tell, but if anyone sees you on video.

Yes, I apologise to anyone looking at this on video who has to see my eyes, which look as if I'm sort of either auditioning for a sort of cold and flu advert, or else that I've been crying all day.

I promise you neither is true, but yeah, I've been better.

GRAHAM CLULEY

All right, well, we won't keep you for too much longer than we need you, but we are gonna need you for the next 45 minutes or so as we look at some of the biggest security stories of the last week.

But before we kick off, let's thank this week's wonderful sponsors, 360 Privacy, Origin, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security. We're not gonna be talking about how a bug in Signal could let someone keep listening after you've hung up.

You'll hear no discussion of how more than 4,500 Bluesky accounts were compromised by a phishing attack that posed as a government payment.

And we won't even mention how a massive Chinese crime ring hacked the Staples retail giant to steal millions. So James, what are you going to be talking about this week?

JAMES BALL

Well, I thought I would talk about some scary news from the world of TLS.

GRAHAM CLULEY

And I'm gonna be talking about how Dutch spies allegedly hitched a ride on a Russian hack of Jared Kushner's iPhone.

Plus, we've got a featured interview with Chuck Randolph of 360 Privacy about how the internet has made it scarily easy to put company executives and public officials in danger.

All this and much more coming up in this episode of Smashing Security.

Today's episode of Smashing Security is sponsored by 360 Privacy, and to explain what they do, I've brought in Joe.

JOE

Happy to help.

GRAHAM CLULEY

Joe, why are you wearing a balaclava?

JOE

You said I was playing a cybercriminal.

GRAHAM CLULEY

And?

JOE

Well, that's the uniform, isn't it? I assumed it was in the contract.

GRAHAM CLULEY

Joe, real cybercriminals dress like accountants. Most of them are sitting in open-plan offices eating a meal deal.

JOE

Now you tell me. I've walked here like this. The neighbours saw me.

GRAHAM CLULEY

Well, what did you say to them?

JOE

That I've been skiing.

GRAHAM CLULEY

It's October, Joe, and we're in the UK.

JOE

I said it was an indoor slope.

GRAHAM CLULEY

Fine, leave it on. And why the bobble hat?

JOE

It's cold in the studio.

GRAHAM CLULEY

Okay, okay, Joe, back to business. You've got one task. Find out everything you can about me using only the internet. Go!

JOE

Right, searching. Oh. Oh wow, that was quick. Your home address, family members, property records, social media accounts—

GRAHAM CLULEY

Hang on, that was under 10 seconds you managed that?

JOE

And I've got a few of the places you regularly visit. Honestly, it's a bit embarrassing how many times you go to Greggs for a sausage roll.

GRAHAM CLULEY

Oh, come on. Individually, those details seem harmless. Nobody's panicking over a coffee order.

JOE

But put them together and I now have a surprisingly clear picture of who you are, where you live, and how to find you. I haven't even finished my tea.

GRAHAM CLULEY

And that, listeners, is the problem that 360 Privacy is built to address.

JOE

360 Privacy is a digital exposure reduction firm.

They help executives, high-profile individuals, and the organisations behind them shrink the digital exposure that turns into real-world risk.

GRAHAM CLULEY

Because threat actors don't separate cybersecurity, privacy, and physical security. They use whatever information is available.

JOE

Data brokers, social media, public records, and AI — it's all making it faster ...