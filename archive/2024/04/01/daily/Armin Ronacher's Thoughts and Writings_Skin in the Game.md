---
title: Skin in the Game
url: http://lucumr.pocoo.org/2024/3/31/skin-in-the-game
source: Armin Ronacher's Thoughts and Writings
date: 2024-04-01
fetch_date: 2025-10-04T12:14:30.493045
---

# Skin in the Game

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Skin in the Game

written on March 31, 2024

There was a bit of a [kerfuffle](https://www.openwall.com/lists/oss-security/2024/03/29/4) about
subverting open source projects recently. That incident made me think
about something that’s generally on my mind. That thought again was
triggered by that incident but is otherwise not in response to it. I want
to talk about some of the stresses of being an Open Source contributor and
maintainer but specifically about something that have been unsure over the
years about: anonymity and pseudonymity.

Over the years it has been pretty clear that some folks are contributing
in the Open Source space and don’t want to have their name attached to
their contributions. I’m not going to judge if they have legitimate
reasons for doing so or if pseudonymity a good or bad thing. That it is
happening, is simply a fact of life. The consequences of that however are
quite interesting and I think worth discussing.

When I talk about names, I primarily think about the ability to associate
an online handle and a contribution to a real human being. That does not
imply that it should be necessarily trivial for people to find that
information, but it should be something that is at least in principle be
possible. There is obviously a balance to all of this, but given that
there are real consequences to “doing stuff on the internet” there has to
be a way to get in contact with the person behind it. So as far as
“naming a person” here is concerned it’s not so much about a particular
name, but as in being able to identify the human being behind it.

While we might get away with believing nothing on the internet matters and
laws do not apply, that’s not really true. In fact particularly with Open
Source we’re all leveraging copyright laws and the ability to enforce
contracts to work together. And no matter how much we write “THIS
SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND
ANY EXPRESS OR IMPLIED WARRANTIES” not all legal consequences can be waived.

Which leads me to some development in internet anonymity I have observed
over the last 20 years which I find worth reflecting on. When I got
started with Open Source, pseudonyms felt much less common. The distance
to the legal system at least to me felt much closer than today. I give
you a handful examples of this: When I got started doing stuff on the
internet and you did something really stupid, someone called your ISP and
you had an angry conversation. Because the subscriber of that line was
known. A lot of the systems on the earlier internet were based on a lot
more trust than would be acceptable today. An angry ISP was not the worst
that would happen to you, a lot of people got charged with wire-fraud for
things that today are just being ignored because they have become too
commonplace (like probably most DDOS attacks these days). When I created
my first SourceForge account, the “real name” field was not optional, CLAs
talked about names and asked for signatures. When my stuff was packaged
up in Debian some of the first things that came my way were folks
explaining me some legal stuff about licenses I was unaware before. After
I started getting involved with Ubuntu I went to a key signing party where
I showed my passport to other human beings to demonstrate that I exist.
When I became a Python core contributor I signed a physical paper for the
CLA.

A lot of this feels quite untypical today. We no longer do a lot of these
things and I believe it mostly just works because people don’t go to court
much about Open Source projects any more. It probably also works because
over time Open Source became more established. If you contribute via
GitHub today, even the terms of service probably help resolving copyright
issues by being quite explicit about how contributions to public
repositories happen (you contribute under the license of the repository).

But sometimes people do go to court. Open Source projects in many ways
are an unclear amalgamation of different contributions and we just
collectively hope that we all agree that contributions come in under the
same licenses as the file in the root of the project. The Linux kernel
once did not accept contributions from pseudonymous users. It did so for
good reasons. They need to know who the person is that contributes so
they know what to do in case of a licensing conflict and there was more
than one lawsuit involving Linux. This was true even after the [DCO](https://en.wikipedia.org/wiki/Developer_Certificate_of_Origin) was put
in place. Today, pseudonyms are accepted. Not just in Linux, but also in
many large projects. An example of that is the CNCF which found a nice
middle ground on the name and what you sign off with: “A real name does
not require a legal name, nor a birth name, nor any name that appears on
an official ID (e.g. a passport). Your real name is the name you convey
to people in the community for them to use to identify you as you.”

Most important however is this part: “Your real name should not be an
anonymous id or false name that misrepresents who you are.” The need of
getting in contact with the person exists and did not go away. It always
existed and it quite likely will continue to exist. There are good
reasons why you want to know who the person is. Maybe the person
contributed code they did not own the copyright of, maybe their employer
writes you an angry email. Concerns about licensing are a common reason
for why people want to know who the people are that contribute. Maybe
sanctions or other legal restrictions prevent to accept contributions from
that person. Another reason you might need to get in contact with the
author is to change the license. You might remember that a lot of
projects tried to move from GPL v2 to GPL v2 or later. A change that
required the agreement of every person that contributed before. Reaching
out to people sometimes is not the easiest of tasks.

However in addition to pseudonymous contributions, there is also a sharp
increase of anonymous contributions. Particularly thanks to GitHub pull
requests it’s incredibly common that you get commits now from folks whose
only identity is a made up user name, no visible email address and some
default avatar that GitHub generated.

This is not necessarily a problem, but to me it feels like a trend that
I’m not sure how to work with. It creates a somewhat complex form of
interaction where one person might be out in the open, the other person
might be entirely anonymous. Many of us old timers who went into Open
Source in former times have a pretty well established online identity
(either via a “real name” or pseudonym). I also think that many of us who
are in this for a while feel quite a bit of stress and responsibility for
the things we created, at least that is very much true for me. Multiple
times over the years did I hear or read online that a person chooses to
contribute anonymously is because their employer bans Open Source work.
One the one hand it’s great that people find a way to avoid these
restrictions, on the other hand if that ever gets found out you probably
are going to have some unfriendly talks with someone else’s legal team.
While in practice none of my code is important enough that I think
something like this will happen, I can absolutely see this happen to large
Open Source projects where a rogue employee contributes on their
employer’s time or otherwise proprietary code.

I have a heard the sentiment a few times now that one should vet the
contributions, not the contributors. That’s absolutely true. Yet at the
same time many of us are quite frankly assuming good actors and just happy
to get contributions. We sometimes merge pull requests not in the best
state of mind, sometimes we feel pressured. It can be quite hard to spot
back doors a...