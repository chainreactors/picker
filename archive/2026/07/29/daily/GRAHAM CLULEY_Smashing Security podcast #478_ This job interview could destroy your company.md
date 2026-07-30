---
title: Smashing Security podcast #478: This job interview could destroy your company
url: https://grahamcluley.com/smashing-security-podcast-478/
source: GRAHAM CLULEY
date: 2026-07-29
fetch_date: 2026-07-30T04:52:30.695892
---

# Smashing Security podcast #478: This job interview could destroy your company

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

# Smashing Security podcast #478: This job interview could destroy your company

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:09 am, July 30, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #478: This job interview could destroy your company](https://grahamcluley.com/wp-content/uploads/2026/07/ss-episode-478.webp)

You’ve been headhunted for a great job in cryptocurrency. All you have to do is complete a short online assessment – with your webcam on, of course, so they can verify who you really are. Which is ironic, because the person recruiting you doesn’t exist. And North Korean hackers using this trick have already made off with $643 million in crypto this year alone.

Meanwhile, researchers at UC San Diego have discovered that 2.2 million cars across the United States can be unlocked or immobilised by anyone with a bit of Bluetooth kit – thanks to one aftermarket car alarm that made a truly spectacular cryptographic blunder. The bug has been sitting there since 2017. Nobody noticed.

All this and more in episode 478 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Paul Ducklin.

[![Podcast artwork](https://media.redcircle.com/images/2026/7/29/18/d42a0f05-7568-44f3-a2c8-0c1c27ac0c32_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #478

### [This job interview could destroy your company](https://www.smashingsecurity.com/478)

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

I was in a car park and I found my car, at least what I thought was my car. And I thought, why isn't my key working? And I tried the door and it was only unlocked.

Only when I saw how clean the car was that I realised it couldn't possibly be mine.

PAUL DUCKLIN

You looked in the back and there were no food wrappers and discarded cardboard boxes from three months ago.

Unknown

How dare you! I don't know if I'm getting a little bit old.

Smashing Security, Episode 478: This Job Interview Could Destroy Your Company, with Graham Cluley and special guest Paul Ducklin.

Hello, hello, and welcome to Smashing Security, Episode 478. My name's Graham Cluley.

PAUL DUCKLIN

And my name is Paul Ducklin.

GRAHAM CLULEY

Duck, welcome back to the show.

PAUL DUCKLIN

Thank you very much, Graham. Pleasure to be back.

GRAHAM CLULEY

There's been big news actually on the cybersecurity front since our last episode.

PAUL DUCKLIN

I can't think what you're talking about, Graham. What could it be?

GRAHAM CLULEY

Unfortunately, due to the schedule of Smashing Security, we recorded last week's episode just before the whole OpenAI going rogue, attacking Hugging Face story, which made a thousand headlines.

PAUL DUCKLIN

Now you know how Microsoft feels when Nightmare Eclipse Smashing Security publishes an exploit minutes after Patch Tuesday's dropped.

GRAHAM CLULEY

We're not going to talk about this very much because frankly, everyone else has spoken about it. I've blogged about it. It feels like old hat by the time this episode comes out.

But people are asking, is this the end of the world as we know it? But some people have also thought that maybe there's a bit of hype around this.

Maybe it's working to the advantage of the AI company's PR machine. Have you seen anything like that?

PAUL DUCKLIN

We do seem to have had that quite a few times recently with these AI companies, haven't we?

Wasn't it Anthropic that said, oh, we've got this product, it's so dangerous, we can't release it.

And then when the government turned around in the US and said, okay, we are going to regulate it, it's like, what? You're going to regulate it? But we're libertarians.

If there's any regulation to be done, we'll do it. How dare you? You said, well, you spent ages hyping up how dangerous it was because it's so clever. You can't have it both ways.

But you're right, Graham, I think. There have been at least a few people who have been somewhat cynical about this.

So may I read you a post that I saw from a chap in Cambridge, UK, by the name of Graham Bell.

Now, I don't necessarily agree with all of this, just to make it clear, but by golly, I laughed so hard.

Unknown

Okay.

PAUL DUCKLIN

And here is what he wrote, Graham.

So it turns out that if you train an AI model on hacking and then you train it on sci-fi stories about AIs being total dicks, and then you set it loose in a fairly secure sandpit with safety and sanity settings deliberately set to zero, it runs off to hack your biggest competitors and acts like a total dick.

Who could possibly have guessed that might happen exactly in time to fit in with the week's political PR campaign about the competition posed by Chinese and non-US AI models?

What are the odds of that?

GRAHAM CLULEY

Well, it's an excellent question.

PAUL DUCKLIN

It did make me laugh.

GRAHAM CLULEY

Before we kick off, let's thank this week's wonderful sponsors, Arctic Wolf, NordLayer, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security. We won't be talking about how spies hid malware commands inside Microsoft 365 calendar meetings scheduled for the year 2050.

You'll hear no discussion of how a ransomware gang called The Gentlemen is holding a famous Dutch ice skating rink hostage.

And we won't even mention how a flaw in Shark robot vacuums lets attackers remotely access your camera, steal your Wi-Fi password, and download a map of your home.

So, Duck, what are you going to be talking about this week?

PAUL DUCKLIN

I'm going to be asking two questions, Graham. Firstly, how safe is your car alarm? But more importantly, how do you know if you've even got one?

GRAHAM CLULEY

Normally it goes off at 2 o'clock in the morning. That's how I know if I've got a car alarm.

PAUL DUCKLIN

Yes, and you find out because your neighbours have put a brick through your windscreen the next morning.

GRAHAM CLULEY

And I'll be asking, could a fake job interview drain your bank account and fund a nuclear weapons programme? All this and much more coming up on this episode of Smashing Security.

JOE

Graham, am...