---
title: Smashing Security podcast #480: This is the AI service you should never sign up to
url: https://grahamcluley.com/smashing-security-podcast-480/
source: GRAHAM CLULEY
date: 2026-08-12
fetch_date: 2026-08-13T04:05:22.038246
---

# Smashing Security podcast #480: This is the AI service you should never sign up to

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

# Smashing Security podcast #480: This is the AI service you should never sign up to

Hacking stories and cybersecurity insights.

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:12 am, August 13, 2026

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2025/06/linkedin-icon-48.png "LinkedIn") [/ grahamcluley](https://www.linkedin.com/in/grahamcluley/ "Follow Graham Cluley on LinkedIn")

![Smashing Security podcast #480: This is the AI service you should never sign up to](https://grahamcluley.com/wp-content/uploads/2026/08/ss-episode-480.webp)

Would you like access to Anthropic’s Claude at 90% off the normal price? All you have to do is redirect your traffic to a mysterious service called “Poison Claude”. Only problem is that it’s run by fraudsters…

Meanwhile, a phishing-as-a-service platform called “Greatness” has come up with something rather nasty: a phishing attack that doesn’t need a fake website, a suspicious URL, or your password. Just a real Microsoft login page and a moment of misplaced trust – and the attackers walk off with full access to your emails, your files, and your entire organisation.

All this and more in episode 480 of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Lianne Potter.

[![Podcast artwork](https://media.redcircle.com/images/2026/8/8/17/b1a507eb-f66c-4fe5-a541-dfc73f7aa89d_smashing-security-logo-3000px.jpg)](https://www.smashingsecurity.com)

Smashing Security #480

### [This is the AI service you should never sign up to](https://www.smashingsecurity.com/480)

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

LIANNE POTTER

Name ten punctuation marks. Ten? Ten.

GRAHAM CLULEY

Well, you have an exclamation point. You have a colon. You have a semicolon. You have an em dash. You have a hyphen. You have a Spanish upside down exclamation mark. You have a comma.

You have a full stop. You have a slash. A colon. Have I said? He said colon.

LIANNE POTTER

Polly. You got two more to go. Two more to go.

Unknown

Smashing Security, episode 480. This is the AI service you should never sign up to, with Graham Cluley and special guest Lianne Potter.

Hello, hello, and welcome to Smashing Security, episode 480. My name is Graham Cluley.

LIANNE POTTER

And I'm Lianne Potter.

GRAHAM CLULEY

Lianne, welcome back to the show. Lovely to have you here again. For those people who are not familiar with your work, what do you do and what have you been up to lately?

LIANNE POTTER

Well, it has been a long time, so I'm going to hold you very responsible for this, Graham.

GRAHAM CLULEY

Oh dear.

LIANNE POTTER

And for those of you who don't know me, my name is Lianne Potter.

I am currently the Chief AI Security and Ethics Officer at NovStar Intelligence, which is a new gig for me since I last was on this show.

I've also got another new podcast, which finally came about. I know we discussed that on my last episode, but it's here. It's here.

GRAHAM CLULEY

Okay, so what's the name of your new podcast? Because you were doing Compromising Positions, weren't you? What's the new one?

LIANNE POTTER

Compromising Positions is still going great guns, so it's there for you to enjoy, which is my cybersecurity podcast.

Not the same as this one, but variety is the spice of life, right?

GRAHAM CLULEY

Yeah.

LIANNE POTTER

But the new podcast is a lot more lighthearted.

It's called Tech Film Noir, and on it, me and two other techies review the technology in science fiction films to see if it predicted the future.

And the latest episode, which will be out when this episode airs, is for Strange Days, which is a 1995 classic, in my opinion, that no one has ever heard of.

It's all about VR and living other people's memories and stuff. It's quite dark, very cyberpunk, but very fun.

GRAHAM CLULEY

I found it quite disturbing, I think.

LIANNE POTTER

It's really disturbing, yeah.

GRAHAM CLULEY

And you've been doing something with incels lately. Very good of you, very charitable.

LIANNE POTTER

I mean, as a woman, yeah, I'm not sure I'm the type of person they want to hang out with.

I am currently finishing off my master's in AI, and for my dissertation project, I have been building synthetic incels.

The reason being is because I just can't get hold of any real ones. Incel stands for involuntary celibate.

It's a subgroup of the manosphere that believe that they're incapable of having romantic or sexual relationships because society is against them.

GRAHAM CLULEY

Yeah.

LIANNE POTTER

And so I've been thinking a lot about how do we de-escalate this de-radicalisation? Because it's all connected with how they engage online. It's a very online community.

Incels are an issue because they come with a lot of negative violence and danger.

And compared to the rest of the male population, which has a suicide rate of about 3%, incels tend to have a suicide rate between 43% and 62%.

GRAHAM CLULEY

Oh my goodness.

LIANNE POTTER

Yeah. So there's a high rate of mental health issues within that community.

And they're also seeing a lot of incels use things like AI companions and AI girlfriends to enact violent tendencies.

So I thought if incels are using AI companions to practise and rehearse negative interactions with women, how about we get that AI companion to challenge these beliefs?

So I'm doing a thing where this AI companion, if it detects this incel is starting to veer off into radicalisation, it will then start challenging those beliefs.

Unknown

Right.

LIANNE POTTER

I've done 4 or 5 different experiment tropes. So, one version is it uses persuasion techniques to try and convince them to maybe not think like that. Another is Socratic prompting.

So, getting people to reflect back on the reason why they think that.

Unknown

Yes.

LIANNE POTTER

And various other means of behavioural science to kind of understand what would be the best approach if we were to apply this AI companion in the real world.

And the results are that it does slowly de-radicalise these incels. Now, you're probably thinking, how did you make an incel?

Well, unfortunately, I had to troll through absolutely loads, and there is loads of datasets out there of 4chan, Reddit subposts.

GRAHAM CLULEY

Oh my goodness.

LIANNE POTTER

From these fellas. Not the nicest discussions to read, but all made a very ...