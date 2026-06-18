---
title: I Could've Rickrolled the Entire FIFA World Cup. All I Needed Was My ID.
url: https://bobdahacker.com/blog/fifa-hack
source: Over Security
date: 2026-06-17
fetch_date: 2026-06-18T06:51:16.243751
---

# I Could've Rickrolled the Entire FIFA World Cup. All I Needed Was My ID.

[bobdahacker](/)

☰

* [home](/)
* [blog](/blog)

# I Could've Rickrolled the Entire FIFA World Cup. All I Needed Was My ID.

June 16, 2026

BobDaHacker

*They fixed it without ever responding to me. I had to call FIFA, MediaKind, HBS, CISA, and the FBI at 3am Tokyo time just to get someone to listen. This is that story.*

## It Started With a Football Agent Registration

So FIFA has this thing called the [FIFA Agent Platform](https://agents.fifa.org). It's a public portal where you can register to become a licensed football agent. You submit your ID, verify your email, and you're in. Simple enough.

What I didn't expect was what happened next.

When you register on agents.fifa.org, FIFA adds your account to their Microsoft Entra tenant (formerly Azure AD). That's the same tenant that powers **all** of FIFA's internal platforms. And I mean all of them.

My first two attempts actually failed because the lighting on my ID photos wasn't good enough:

![FIFA registration failed](/static/images/blogs/fifa/registration_failed.png)
*"Registration failed during the last step of checking your identification." - apparently FIFA has higher standards for my selfie than my actual security*

But the third attempt went through. And I received this beautiful email:

![FIFA FAP confirmation email](/static/images/blogs/fifa/fap_confirmation.png)
*Subject line: "FIFA - FAP - CONFIRMATION". Yes, FIFA's Agent Platform is officially called FAP. I cannot make this up. FAP CONFIRMATION. Moving on.*

## The "Access Denied" That Wasn't

After registration, I tried navigating to `fdp.fifa.org` - FIFA's Football Data Platform. The app authenticated me through the shared Entra tenant, checked my roles, found I had none, and showed me:

*"Sorry, you do not have any FIFA Football Data Platform role assigned to your account."*

Looks like it works, right? Access denied. Go away. Nothing to see here.

Except this was all **client-side**. The Angular app checked the JWT for a `NO_ROLES` marker and rendered the access-denied page. The backend APIs? They didn't check anything. They just served whatever you asked for.

## Welcome to the Streaming Management Panel

After bypassing the client-side guards, I landed on the Streaming Management panel. And my jaw hit the floor.

![Streaming Management panel showing all World Cup matches](/static/images/blogs/fifa/streaming_panel_overview.png)
*Every single FIFA World Cup 2026 match. With streaming controls.*

This wasn't some dev environment. This wasn't test data. This was the **live production Streaming Management panel** for the FIFA World Cup 2026. Every match. Every camera angle. Every RTMP ingest URL. Every stream key.

Let me expand one of those matches so you can see what I mean:

![Expanded match showing all five camera RTMP URLs](/static/images/blogs/fifa/streaming_panel_expanded.png)
*Five camera angles per match: PGM, Tactical, Camera1, High Behind Left, High Behind Right*

Each match had five camera feeds, each with:

* An **RTMP ingest URL** (where the camera sends video TO)
* A **preview manifest** (where you can WATCH the feed)
* An **output URL** (the HLS manifest that goes to broadcast partners)

The RTMP ingest URLs looked like this:

```
rtmp://in-6c81fc99-513f-4c76-82c2-877e0b93f2ea.westeurope.streaming.mediakind.com:1935/96886a14-9987-420f-814c-2f7cec5408ae
```

That UUID at the end? `96886a14-9987-420f-814c-2f7cec5408ae`. That's the **stream key** (not a real one). It's shared across all five camera angles for the same match. One key to rule them all.

The streaming infrastructure is hosted on [MediaKind](https://mediakind.com), FIFA's streaming technology partner. These are production endpoints. The same ones receiving live camera feeds from stadiums across the US, Mexico, and Canada.

## I Opened VLC. It Was Live.

I had to confirm the preview manifests actually worked. So I copied one into VLC.

![VLC playing a live World Cup tactical camera feed](/static/images/blogs/fifa/vlc_live_feed.png)
*That's a live tactical camera feed from an active FIFA World Cup 2026 match. Playing in VLC. On my PC. In Tokyo.*

I closed it immediately. But the damage was done (to my brain). Those preview URLs serve live video. During active matches. To anyone with the URL.

## I Could Have Stopped the Streams

It wasn't just read access. The Streaming Management panel had full controls. Start, stop, schedule. For every match. Every camera angle.

![Stream control confirmation dialog](/static/images/blogs/fifa/stream_control.png)
*One click. That's all it would take to kill a live World Cup camera feed.*

I did not touch any of these controls. But they were there. Functional. Waiting for anyone with a NO\_ROLES account to press them.

## The Nuclear Option

Let me spell out what this means.

Those RTMP ingest URLs are the literal pipe from the stadium cameras to FIFA's broadcast distribution chain. Camera -> RTMP ingest -> MediaKind -> broadcast partners -> your TV.

If an attacker pushed video to one of those RTMP endpoints with the stream key (which is RIGHT THERE in the URL), they would **replace the camera feed**. The PGM (Program) feed is the main broadcast output. Replace that, and every TV network receiving the FIFA feed shows whatever you pushed.

The stream key is shared across all five camera angles per match. A single attacker could hijack every camera simultaneously.

An attacker could have rickrolled the entire FIFA World Cup. Or played Subway Surfers gameplay. Live. On every TV network worldwide. During an active match.

I did not test this. I did not push anything to any RTMP endpoint. But the infrastructure was wide open.

## But Wait, There's More

The Streaming Management panel wasn't the only thing exposed. My NO\_ROLES account had access to the entire platform.

![FDP navigation showing full access](/static/images/blogs/fifa/fdp_full_nav.png)
*Competitions, Matches, Teams, Tools, Exchange Platform, Analysis Dashboard, Commentator Information System, FIFA AI Pro, Admin. All accessible.*

The platform also had a full live match dashboard with an embedded video player, real-time event timeline, and match officials data:

![FDP match overview with live video](/static/images/blogs/fifa/fdp_match_overview.png)
*Côte d'Ivoire vs Ecuador, live. Embedded video feed, yellow card timeline, match officials. The "LIVE" badge isn't decorative.*

### Advanced Analytics (Live Match)

![Advanced Analytics showing live possession and attempt data](/static/images/blogs/fifa/advanced_analytics.png)
*Live possession control, attempt creation breakdowns, ball recovery timing, distance covered, and FIFA AI Pro integration*

### Match Management (Write Access)

Here's where it gets worse. The Management tab on fdp.fifa.org has write operations. And the backend accepts them from a NO\_ROLES account.

![Update Live Stats modal with Edit and Publish button](/static/images/blogs/fifa/update_live_stats.png)
*"Update Live Stats" with a rich text editor, match time, match score fields, and an "Edit and Publish" button*

![Match management buttons](/static/images/blogs/fifa/management_buttons.png)
*Attendance, Possession, Post Match Statistics, Team Registration Statistics, Analysis Finished, Score and Statistics, Adjust Kick-off Moment, Performance Data, Send Tactical Lineup, Event Ingress Details*

An attacker could:

* Modify editorial commentary notes and publish them to broadcast systems
* Adjust the official kick-off moment
* Send tactical lineup data
* Change scores and match statistics

This data feeds into the Commentator Information System and gets displayed on live television.

## The Commentator Information System

`cis.fifa.org` was also accessible with the NO\_ROLES account. This is the real-time dashboard that broadcast commentators use during live matches.

![CIS main dashboard](/static/images/blogs/fifa/cis_dashboard.png)
*The FIFA World Cup 2026 dashboard. Live scores, upcoming matches, results.*

![CIS live match view](/static/imag...