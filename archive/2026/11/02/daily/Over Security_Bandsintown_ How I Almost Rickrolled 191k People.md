---
title: Bandsintown: How I Almost Rickrolled 191k People
url: https://bobdahacker.com/blog/bandsintown
source: Over Security
date: 2026-11-02
fetch_date: 2026-11-03T08:51:37.420049
---

# Bandsintown: How I Almost Rickrolled 191k People

[bobdahacker](/)

☰

* [home](/)
* [blog](/blog)

# Bandsintown: How I Almost Rickrolled 191k People

December 25, 2025

BobDaHacker

They fixed it fast and sent me swag and 200$. Rick Astley's 191k followers were almost rickrolled for real.

## What Happened

I was poking around Bandsintown's artist platform and noticed something interesting. I tried to request access to Justin Bieber's team (which was already claimed):

![Request access modal for Justin Bieber showing 6.2M followers](/static/images/blogs/bandsintown/request_access.png)

This sent a POST request to `/api/artists/{artistId}/managers/{myUserId}` and notified his team admins for approval - working as intended.

Then I tried to claim Rick Astley's page, which had no existing team. The UI prompted me to verify my identity by linking my Facebook, X, or Instagram:

![Claim your artist page modal showing verification options](/static/images/blogs/bandsintown/claim_artist_page.png)

But wait... what if I just use the same API endpoint I found from the Bieber request?

## The Vulnerability

```
POST https://artists.bandsintown.com/api/artists/{artistId}/managers/{yourUserId}
```

It just worked. Completely bypassed the verification UI. No OAuth. No Facebook check. No "are you actually Rick Astley?"

Just send the POST request and you're in.

The crazy part? Just because an artist hasn't claimed their page doesn't mean they don't have followers. Rick Astley had 191k followers who signed up to get notified about his concerts - complete with their emails, names, and locations. All sitting there waiting for whoever claimed the page first.

![API response showing successful manager addition to Rick Astley's account](/static/images/blogs/bandsintown/api_response.png)

## What Could I Do?

With manager access to any artist, I could:

* **Send push notifications and emails to all their followers** - Rick Astley has 191k followers. Imagine the chaos.
* **Post on their behalf** to Bandsintown, Facebook, and X
* **Access their entire contact list** - emails, names, locations of fans who opted in
* **Manage their events, campaigns, and integrations**
* **Access fan insights and analytics**

![Rick Astley's Fan Manager dashboard with post composer](/static/images/blogs/bandsintown/fan_manager.png)

I had the ability to send "i will never give you up, i will never let you down, i love you all, rick roll am I right? Pickle Rick." to 191,000 people. I did NOT do this. But I could have.

The contacts page was especially concerning - 8.6k fans with their emails, names, and locations exposed:

![Contacts page showing fan emails, names, and locations](/static/images/blogs/bandsintown/contacts.png)

## Testing At Scale

To confirm this wasn't a one-off, I tested with multiple artists. It worked on every artist who hadn't already claimed their page.

![Diddy's Fan Manager dashboard showing 373.5K followers](/static/images/blogs/bandsintown/diddy_fan_manager.png)

Diddy's page? One API call and I was invited to the party. 373.5K followers ready to receive whatever messages I wanted to send. No baby oil required.

For artists like Justin Bieber who already had their pages claimed by their actual teams, the API correctly sent a request for approval instead of granting instant access. The terminal output below shows me cleaning up - removing myself from all the unclaimed artists I tested on, plus canceling my pending requests to the claimed ones:

![Terminal showing successful manager removal from multiple artists](/static/images/blogs/bandsintown/mass_test.png)

Rick Astley. Fall Out Boy. My Chemical Romance. Bob Marley. The Chicks. Dave Matthews Band. Billy Talent. All unclaimed and all instantly accessible with a single API call.

I removed myself from all of them after confirming the vulnerability.

## The Timeline

**October 2025:** Reported the vulnerability with full details and screenshots.

**Same Day:** They confirmed receipt and started investigating.

**Shortly After:** Fixed. They identified and addressed the problem quickly.

**Bounty:** They send $200 and Bandsintown swag to my apartment.

## To Bandsintown

Thanks for the quick fix and the honest response about bounty limitations. Not every company can do $10k payouts, and that's fine - what matters is taking the report seriously and fixing it fast. You did both.

Also thanks for shipping swag internationally. That's more effort than most companies put in.

## Found Another One:

While writing this blog post, I discovered another vulnerability. I'm currently in the process of responsibly disclosing this to Bandsintown. I'll update this post once it's fixed with the details.

Never gonna give up reporting bugs. Never gonna let security issues go unreported. 🎵

[home](/)
[blog](/blog)

© 2025 bobdahacker