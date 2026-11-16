---
title: tl;dv (Too Lazy; Didn't Validate): 181,874 Meetings Left Wide Open
url: https://pentester.ca/blog/tldv-hack
source: Over Security
date: 2026-11-15
fetch_date: 2026-11-16T08:48:46.121743
---

# tl;dv (Too Lazy; Didn't Validate): 181,874 Meetings Left Wide Open

[Skip to main content](#main)

[](/assets/images/Orbs/PT_Orb_LoopDark.webm)
![](/assets/images/Logos/Pentester.ca_Full_Logo_Dark.svg)

[](/assets/images/Orbs/PT_DarkPink_Orb.webm)

* Based in Tokyo,
  [E: [email protected]](/cdn-cgi/l/email-protection#9deaf5f4e9f8f5fce9ddedf8f3e9f8eee9f8efb3fefc)
* Japan
  --:--:-- (GMT+9)

* [Home](/)
* [What You Get](/#what-you-get)
* [Why Hire Me?](/#why-hire-me)
* [Who Have I Helped?](/#who-helped)
* [The Feedback](/#feedback)
* [Blog](/blog)
* [Contact](#contact)

[![Pentester.ca - home](/assets/images/Logos/Pentester.ca_Full_Logo_Light.svg)](/)

[![](/assets/images/Title_Element_Black.svg)
BLOG](/blog)

# tl;dv (Too Lazy; Didn't Validate): 181,874 Meetings Left Wide Open

By Kaeden | Pentester.ca | August 4, 2026

*I reported this on January 28th, 2026. It is now July 2026. Six months later. The Firestore database is still wide open. The CTO never responded. I guess my emails were too long and they didn't view them.*

## What is tl;dv?

tl;dv (Too Long; Didn't View) is an AI meeting recording platform. It drops a bot into your Google Meet, Zoom, or Teams call, records everything, transcribes it, and generates summaries with AI. Over 2 million users. Backed by investors. Endorsed by half of LinkedIn's sales influencer community.

They store your sales calls, job interviews, performance reviews, internal strategy sessions. The kind of content where someone says "this call is being recorded" and everyone nervously laughs and then shares trade secrets for 45 minutes.

## The Vulnerability

When you sign up for tl;dv, the platform authenticates you with a JWT and exchanges it for a Firebase token via `gw.tldv.io/v1/users/firebase/token`. That token lets you query their Firestore database at `projects/lmi-store/databases/(default)`.

The `meetings` collection has no tenant isolation. Any authenticated tl;dv user can query every meeting across every account on the platform. Each meeting record hands you the creator's email address, the conference ID (which is a joinable Google Meet or Teams room), the provider, the recording status, and timestamps.

For meetings in `recording` status, that conference ID is a live, active call. You can watch the collection in real time, see a meeting start recording, grab the ID, and walk into someone's call uninvited. At any given time there are roughly **1,000 meetings with `status: recording`** sitting in the collection. A thousand live calls with exposed conference IDs. An attacker with a bot could join all of them simultaneously.

![A call thats being recorded](/assets/images/blogs/tldv/firebase.png)

## I Joined 2 Meetings

I did it.

Grabbed a conference ID from Firestore and joined a live Google Meet belonging to the **Malaysian Ministry of Education**. A lady was presenting to over 157 participants. The tl;dv bot was already in the participant list. I was in the same call. Nobody invited me. The Firestore database did.

![Call 1](/assets/images/blogs/tldv/meeting1.png)

I also joined a call where students from a major US university were building a startup app. 21 people in the call. They were screen-sharing their entire project, discussing prototypes, and, I kid you not, talking about how they needed to add client-side validation for `.edu` email addresses. They were also setting up Supabase live on screen, and all I could think was "please set up RLS policies" because most people don't, and then you end up like tl;dv.

I wanted to say something so badly. "Hey, you might want server-side validation too." But this was a proof of concept, not a consultation.

![Call 1](/assets/images/blogs/tldv/meeting2.png)

## The Scale

I queried the Firestore `meetings` collection and saw there were **181,874 meeting records** belonging to **84,312 unique users** across **35,003 email domains**.

Government meetings from **23 countries**: Brazil, Colombia, Peru, Ukraine, El Salvador, the Philippines, Chile, Indonesia, Mexico, the United States, Qatar, Malaysia, Uzbekistan, Sri Lanka, Haiti, South Africa, Jamaica, Honduras, Argentina, Thailand, Japan, Israel, and Belize. All `.gov` domains. Government employees recording calls on a platform that lets any free-tier user enumerate the whole thing.

University meetings from Berkeley, the University of Tokyo, De La Salle, Universidad Nacional de Colombia. Dozens of `.edu` and `.ac` domains.

Corporate meetings from all 35,000 remaining domains. Mitsui-Soko (484 meetings across four regional offices), Mitsui Fudosan, HubSpot, Confluent, Mekari, AnyMind Group. Every company that ever used tl;dv had their meeting metadata in the same unprotected collection.

Peak month was **July 2025 with 43,209 meetings**. Busiest time slot: **Wednesday at 2pm UTC**, 7,804 meetings. Hump-day standup hour.

## But Wait, There's More

I wanted to know how much actual content was accessible too, by default meetings are private (Meaning you cant watch the video or see the transcript), so I scraped 27,334 meeting IDs and checked which ones were public. Over **1,000 were.** **715 invitee emails** exposed across **228 domains**.

Highlights: a Brazilian government conservation meeting (PACTO Mata Atlântica) with participants from WWF, The Nature Conservancy, Conservation International, WRI, and the São Paulo state government. Meetings from Ukraine's Ministry of Digital Transformation. A HubSpot sales call. Sessions involving Universidad Nacional de Colombia and Chile's Cámara Verde.

## The Pasta Infrastructure

tl;dv names their microservices after pasta. A subdomain scan reveals **cappellini**, **carbonara**, **fusilli**, **pasta**, **penne**, **puttanesca-v0**, and **ravioli**, all under tldv.io. An entire Italian restaurant worth of Express servers.

## Too Long; Didn't Score

While exploring their subdomains I found **https://worldcup.tldv.io**. A FIFA World Cup 2026 vibecoded prediction game built on Base44 for tl;dv employees. It's called "World Cup Pick'em" and their internal squad is named "Too Long; Didn't Score." Cute.

The Player entity API has zero authentication. `GET /api/entities/Player` returns every player record without a session cookie. **43 players.** **19 @tldv.io employees** with full names and corporate emails.

Raphael Allstadt, my disclosure contact who gave vague reassurances and then went quiet, came in 2nd place with 298 points. His personal Gmail was also in the API response. Player #5 on the global leaderboard is "Super Duper CEO." I'll let you guess who that is.

The Prediction and Fixture entities are also wide open. A company that records millions of people's meetings vibecoded an internal fun app that leaks their own employee directory. The irony is al dente.

![A vibecoded world cup slop app](/assets/images/blogs/tldv/worldcup_slop.png)

## Disclosure

On January 28th I messaged Raphael Allstadt on LinkedIn and told him I'd found a huge vulnerability that leaks user data. He responded within minutes: "thank you! can you report it to our CTO and we will look at it immediately?" I sent the email. He said "thank you!" I asked about a reward. "My CTO will come back to you," he said.

The CTO never came back to me.

January 29th: "your cto hasnt reached out yet btw and its not fixed." January 30th, Raphael: "I am sure the team is reviewing it very very soon ❤️" February 14th: "havent got an email and the vulnerability stilll works." Raphael: "He'll come back ☺️" I told him to maybe fix the vulnerability and not leave customers exposed. February 19th: "We're on it. It needs some time, but rest assured we're following through. For further communication, i'll recommend reaching out to our CTO."

The CTO who never responded. That CTO.

March 6th: "still not fixed." Seen by Raphael at 5:42 PM. No reply.

July 22nd: "still not fixed..." No reply.

Their security page is a trophy case. SOC2 compliant. GDPR compliant. EU AI Act compliant. Hosted in the EU. AES-256 encryption. A founder commitment video. Six compliance badges lined up in a row. Bu...