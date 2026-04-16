---
title: Smashing Security podcast #463: This AI company leaked its own code. It’s also built something terrifying
url: https://grahamcluley.com/smashing-security-podcast-463/
source: GRAHAM CLULEY
date: 2026-04-15
fetch_date: 2026-04-16T04:54:27.280321
---

# Smashing Security podcast #463: This AI company leaked its own code. It’s also built something terrifying

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

# Smashing Security podcast #463: This AI company leaked its own code. It’s also built something terrifying

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:24 am, April 16, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #463: This AI company leaked its own code. It's also built something terrifying](https://grahamcluley.com/wp-content/uploads/2026/04/ss-episode-463.webp)

A hacking group claims to have broken into the flood defence system protecting Venice’s Piazza San Marco – and is offering to sell access to whoever wants it. The asking price? A frankly insulting $600.

Meanwhile, Anthropic accidentally leaked the source code for Claude Code via a basic packaging mistake. Oh, and by the way, they’ve also just revealed they’ve built an AI model called Mythos that can find and chain together software vulnerabilities faster than any human. Sleep well.

All this and more in episode 463 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, joined this week by special guest Tanya Janca.

[![Podcast artwork](https://media.redcircle.com/images/2026/4/15/12/a7db8317-1e47-449e-84b2-f95cab0fc9ab_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #463

### [This AI company leaked its own code. It's also built something terrifying](https://www.smashingsecurity.com/463)

↺
15

↻
30
0:00

0:00
0:00

0:00

1×

Show full transcript
▼

![Transcript](https://grahamcluley.com/wp-content/uploads/2026/04/transcript.webp)

Tanya Janca
0:03

I had my data stolen once, Graham, from a governmental organization I worked at.

Graham Cluley
0:08

Right.

Tanya Janca
0:08

And they were selling it online for the bitcoin equivalent of $50 Canadian. And that made me feel very humiliated.

Graham Cluley
0:17

Were you like, please, please sell it for more?

Tanya Janca
0:20

I know, I was like, aren't we worth more than that?

Unknown
0:31

463. This AI company leaked its own code. It's also built something terrifying. With Graham Cluley and special guest Tanya Janca. Hello, hello, and welcome to Smashing Security episode 463. My name's Graham Cluley.

Tanya Janca
0:47

And I'm Tanya Janca.

Graham Cluley
0:47

Tanya Janca, first time on Smashing Security. Hello. How the flip are you?

Tanya Janca
0:56

I am wonderful, Graham. How are you?

Graham Cluley
0:58

I'm gorgeous. Now, you are dialing in today from the beautiful Canadia. Thank you very much for doing that. Now, you are a famous name, right? You're a pretty big deal in the world of cybersecurity. So if people haven't heard of you, how can you describe what you do and what you're all about?

Tanya Janca
1:17

So I am a software developer turned application security expert who really likes to write. And now has written a bunch of books and tons of blogs. I really like to speak, so I speak at conferences, and right now I'm giving secure coding training to large organizations and then kind of just doing contracts here and there, helping people change their application security program so it's more AI aware.

Graham Cluley
1:41

Okay, so you are going into organizations and you're helping those developers code more securely, which is a pretty good idea, I think, because we don't want software which is full of security holes like Swiss cheese.

Tanya Janca
1:53

Well, we have a lot of that right now all over the internet. Right now, that is a giant problem, and especially not on the internet, embedded devices. You know, you go into an emergency room, a hospital, all of those places, the security is usually much worse than it is on the internet, and it's not great on the internet.

Graham Cluley
2:10

Now, a little birdie tells me, Tanya, that you have recently set up a rival podcast to Smashing Security, and you are basically I'm thinking that you can come in here and tell everyone about your podcast. Is that correct?

Tanya Janca
2:25

It's 100% correct, Graham. Right, right. My completely different topic podcast is called DevSecStation, and it's 5 to 10 minute mini lessons for software developers about security. So, this month I'm covering the supply chain and how to secure the supply chain and how software developers they're a target now. Malicious actors are actually targeting the actual developer, the human, and they need to know.

Graham Cluley
2:54

That's interesting actually, isn't it? Because of course, it's easy to imagine how hackers could target people who work in the finance department, for instance.

Tanya Janca
3:01

Mm-hmm.

Graham Cluley
3:01

But if they're targeting the developers themselves, the idea, I presume, is to try to implant code within the code which these developers are writing, because eventually it will roll out to many, many organizations and could cause absolute mayhem.

Tanya Janca
3:16

Absolutely. So, often, the past couple years, people will say, oh, there was a software supply chain breach. But if we look at maybe half of those, it was actually the software developer that was compromised. And then as a result, multiple parts of the supply chain was breached because they have superpowers, because they can control the CI, and they control their IDE, and they control the repo, and they can go to prod, and, and, and. And so, you get the developer's credentials and suddenly you have everything. And then on top of that, what some of the malicious actors have been doing, Graham, is then they rob the developer as well.

Graham Cluley
3:21

Oh.

Tanya Janca
3:53

So they go and they try to empty their crypto wallets because why don't we just kick people while we're down?

Graham Cluley
3:58

Developers are the kind of people who quite often would have crypto wallets, wouldn't they?

Tanya Janca
4:02

Yep.

Graham Cluley
4:02

And so they understand the technology and so they may have a few thousand dollars or perhaps more.

Tanya Janca
4:07

They'd be significantly more likely to have a crypto wallet than the average person.

Graham Cluley
4:12

And I'm also thinking that, I mean, my background is I used to be a developer many years ago, used to write antivirus software. And I remember from way back then that the programmers are also the kind of people who would demand to have admin privileges on their computers because they feel they have godlike capabilities anyway. And so they would be arguing with th...