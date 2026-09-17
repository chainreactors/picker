---
title: Smashing Security podcast #485: These researchers got drunk to hack an LG TV
url: https://grahamcluley.com/smashing-security-podcast-485/
source: GRAHAM CLULEY
date: 2026-09-16
fetch_date: 2026-09-17T07:00:07.609362
---

# Smashing Security podcast #485: These researchers got drunk to hack an LG TV

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

# Smashing Security podcast #485: These researchers got drunk to hack an LG TV

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:07 am, September 17, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #485: These researchers got drunk to hack an LG TV](https://grahamcluley.com/wp-content/uploads/2026/09/ss-episode-485.webp "Smashing Security podcast #485: These researchers got drunk to hack an LG TV")

Researchers wanted to test if LG’s smart TVs come with any security risks – but their lawyers noticed a snag: the terms and conditions would forbid it. So they came up with a solution. They got plastered before setting up the TV, on the reasoning that you can’t be legally bound to a contract you agreed to while drunk. What they discovered will make you look at your TV rather differently…

Meanwhile, awful Android malware with the audacious name “Awesome” (in Indonesian) is doing the rounds, stealing your data, demanding a ransom, and then giving you a “jump scare”…

Plus, in our featured interview, Andy Hornegold of Intruder explains why the mid-market is where cybercriminals are having the most fun right now – and how AI is helping attackers get from “first foot in the door” to “full ransomware disaster” in less than a working day.

All this and more in episode 485 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Lianne Potter.

[![Podcast artwork](https://media.redcircle.com/images/2026/9/16/15/78ce50ea-cdaa-474a-93b1-ae78b727cd9c_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #485

### [These researchers got drunk to hack an LG TV](https://www.smashingsecurity.com/485)

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

RESEARCHER

So we're gonna have a private conversation about our next crypto scam, and it would really be unfortunate if anyone had a recording of this.

ROBOT

Smashing Security, episode 485. These researchers got drunk to hack an LG TV with Graham Cluley and special guest Lianne Potter.

GRAHAM CLULEY

Hello, hello, and welcome to Smashing Security. Smashing Security, episode 485. My name's Graham Cluley.

LIANNE POTTER

And I'm Lianne Potter.

GRAHAM CLULEY

Lianne, welcome back to the show. Always great to have you here. Now, you are, of course, quite the aficionado when it comes to podcasts.

You've got podcasts coming out of your ears, haven't you?

LIANNE POTTER

I'm a millennial. You have to have multiple podcasts.

GRAHAM CLULEY

But you haven't just got one podcast, you've got multiple podcasts. So you've got your Compromising Positions podcast, all about cybersecurity. Excellent, groovy stuff there.

But you also do Tech Film Noir, where you are looking at old movies and seeing how well they've predicted future tech in particular, right?

LIANNE POTTER

It's just an excuse to watch the films I absolutely adore, mostly Arnold Schwarzenegger sci-fi movies.

GRAHAM CLULEY

Well, the latest episode you've put out is all about Weird Science, which was from about 1985, which hit me at precisely the right time. It was in my formative teenage years.

LIANNE POTTER

So does that explain it all then, Graham?

GRAHAM CLULEY

For anyone who hasn't seen it, it's about a couple of teenagers who decide to use technology to magic up the perfect woman in the shape of Kelly LeBrock.

LIANNE POTTER

And what a shape. That's all I have to say. Loving controversy on the podcast.

GRAHAM CLULEY

Goodness gracious me.

GRAHAM CLULEY

They were like, Lianne, you know, we can't really do this podcast 'cause it's not age-grade. And I said, well, that's the whole point of this podcast, that it's not age-grade.

The technology hasn't aged great and neither has the ethical quandaries.

GRAHAM CLULEY

Oh, well, I haven't seen it for a while, but I remember I enjoyed it at the time.

These couple of nerds, they boot up a Memotech MTX computer, a home computer, which wasn't very popular. And with it, they managed to create Kelly LeBrock.

Now, the thing I have to tell you, Lianne, is I had a Memotech MTX computer.

LIANNE POTTER

Boom! My head just exploded. No, you didn't. Really?

GRAHAM CLULEY

I really did.

LIANNE POTTER

We should have got you on the episode.

GRAHAM CLULEY

My original home computer was the Sinclair ZX81.

LIANNE POTTER

Yeah.

GRAHAM CLULEY

But my dad actually got us a Memotech MTX. I can't remember if it was the 500 or the 512. They had different amounts of RAM in them.

LIANNE POTTER

Yeah, yeah.

GRAHAM CLULEY

And I wrote games for them. I have to say, the graphics were nothing like as good as— That was my next question. How does it compare?

But it is a very nostalgic movie for me, 'cause it's like, oh my goodness, I remember this computer.

LIANNE POTTER

That's your life.

GRAHAM CLULEY

This was where I was at. It was fantastic.

LIANNE POTTER

Were you living the high life with 3 screens though, like this young lad does in the film?

GRAHAM CLULEY

Oh no.

LIANNE POTTER

'Cause I remember just thinking when I saw that, I was like, 3 screens, wow.

GRAHAM CLULEY

Who would need 3 screens? You've only got 2 eyes, haven't you?

LIANNE POTTER

I mean, it's—

GRAHAM CLULEY

2 feels like an extravagance to me.

LIANNE POTTER

Do you still have it or?

GRAHAM CLULEY

No, long gone, unfortunately.

LIANNE POTTER

Oh, such a shame, because we could do a follow-up episode and we could literally try and rebuild Kelly LeBrock from it.

GRAHAM CLULEY

I suspect that they go for a fortune on eBay now. They're probably very collectible.

LIANNE POTTER

I bet they are as well. Oh, that's so cool, Graham. That's really, really cool.

GRAHAM CLULEY

Anyway, before we kick off, let's thank this week's wonderful sponsors, ThreatLocker, Intruder, and Vanta. We'll be hearing more about them later on in the podcast.

This week on Smashing Security. We won't be talking about how scammers tricked Revolut into handing over customer data by posing as a government agency.

You'll hear no discussion of how the Reddit account of HBO Max was hijacked by hackers to spread malware.

And we won't even mention how the UK and United States ...