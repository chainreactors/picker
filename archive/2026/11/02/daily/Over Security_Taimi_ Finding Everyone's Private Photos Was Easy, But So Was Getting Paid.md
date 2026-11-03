---
title: Taimi: Finding Everyone's Private Photos Was Easy, But So Was Getting Paid
url: https://bobdahacker.com/blog/taimi-idor
source: Over Security
date: 2026-11-02
fetch_date: 2026-11-03T08:51:37.195397
---

# Taimi: Finding Everyone's Private Photos Was Easy, But So Was Getting Paid

[bobdahacker](/)

☰

* [home](/)
* [blog](/blog)

# Taimi: Finding Everyone's Private Photos Was Easy, But So Was Getting Paid

December 25, 2025

BobDaHacker

They fixed everything fast and paid a solid bounty. This is one of the good ones.

## What Happened

So I was poking around the Taimi app (it's a dating/social app for the LGBTQ+ community) and noticed something weird in the API requests. When you send a video message, there's an `attach` parameter with an ID. What happens if you just... change that ID?

## The Vulnerabilities

### 1. Video IDOR - Watch Anyone's Private Videos

The messaging API at `https://app.taimi.com/thread/message` had zero permission checks on video attachments. Here's how it worked:

The Attack:

* Send a message with a video attachment
* Intercept the request, find the `attach` parameter with the video ID
* Decrement that ID by 1
* Congratulations, you just sent someone else's private "expiring" video to some random person's DMs

The API response would happily return the full video URL:

```
{
  "message": {
    "text": "sent an expiring video",
    "attach": {
      "id": 12321851,
      "url": "https://vm.taimi.com/v/takimi.[redacted].mp4",
      "duration": 23.85
    }
  }
}
```

Those "expiring" videos that users thought would disappear? Anyone could grab them by just guessing IDs. Oh, and they didn't actually expire either, the video URLs stayed valid forever. "Expiring" was just a UI lie.

![API request showing video attachment vulnerability](/static/images/blogs/taimi/taimi_video_idor.png)

![Proof of accessing another user's private video](/static/images/blogs/taimi/taimi_video_proof.png)

### 2. Location Photo IDOR - The Dumbest Bypass Ever

Okay so this one was hilarious in a terrifying way.

Here's the thing: the actual image/photo message type? That had permission checks. They did the work. Good job Taimi.

But when you send your location... for some ungodly reason... Taimi generates a map preview image CLIENT-SIDE, uploads it to their servers, and references it with a `photoId`. Then when you click on it, it loads the actual map client-side anyway. Why? WHY? Why does sending "I'm in Tokyo" need to generate a preview image on your phone, upload it to the server, just for a thumbnail... when clicking it renders the map client-side anyway? Just render the preview client-side too like every other app on the planet???

So naturally, the `photoId` parameter uses the same ID space as actual photos. And naturally, the location endpoint DOESN'T have the same permission checks as the photo endpoint.

Decrement that ID and you get someone else's private photos. Not map images - ACTUAL private photos. The location feature was basically an accidental backdoor to the entire photo system.

The best part? When you clicked on the photo in chat, it opened a map view centered on whatever lat/long coordinates you specified in the request. So you could make someone's private photo appear to be "located" anywhere you wanted.

"Oh look, here's where this dick pic was taken!" *points to coordinates in Tokyo*

![Location and photo injection in Taimi Live Support chat](/static/images/blogs/taimi/taimi_location_injection.png)
*(the image crossed out in red is someone else's private photo retrieved via the photoId parameter)*

They essentially said "let's add permission checks to photos" and then created a completely separate path to photos that bypassed all of it. Security architecture speedrun any%.

![Location API request showing photoId parameter](/static/images/blogs/taimi/taimi_location_api.png)

### 3. System Message Injection

You could send messages that appeared as "System messages" - the same style Taimi uses for official communications. Perfect for phishing:

* Fake "Appeal" buttons
* Fake policy notifications
* Basically anything you wanted users to click

I had some fun with this one, including a message that said "Please click 🏳️‍⚧️ to become woke."

![System message injection with fake Appeal buttons](/static/images/blogs/taimi/taimi_system_message_injection.png)

### 4. Message Type Fuckery

By messing around with different `type` values in the API, I found you could send message types that normal users should NEVER be able to send.

Like this one:

![Raid Shadow Legends sponsorship system message](/static/images/blogs/taimi/taimi_raid_shadow_legends.png)

Yes, that's a fake sponsored system message. "This message is sponsored by Raid Shadow Legends" followed by a fake A/B testing rating prompt with stars.

You could also trigger things like "Group chat has been created" notifications in regular DMs. The API just... trusted whatever message type you sent it.

### 5. App Crasher (Bonus Round)

By sending malformed message types with invalid attachments, you could crash other users' apps entirely. Their messages tab just wouldn't load anymore. Classic denial of service through bad input validation.

## The Disclosure Timeline

**October 1, 2025:** I emailed Taimi support with all the details, proof-of-concept screenshots, and even offered my phone number for questions.

**Same Day:** Tetiana from Taimi confirmed receipt and escalated to their tech team.

**A Few Days Later:** They asked if I had any other findings (I didn't at the time).

**Shortly After:** They validated the bugs and offered a **$10,000 USD bounty**.

They also refunded my subscription since I'd gotten banned while testing.

**Everything Fixed:** All vulnerabilities patched.

## Why This Matters

Dating apps handle some of the most sensitive data imaginable:

* Private photos and videos people expect to "expire"
* Location data
* Personal messages
* Sexual orientation and identity information (especially sensitive for LGBTQ+ users in certain regions)

An IDOR vulnerability on a dating app isn't just embarrassing - it could literally endanger users' lives in countries where being LGBTQ+ is criminalized.

## To Taimi

Credit where it's due: Taimi handled this well.

* Fast response time
* Professional communication
* Proper bounty payout
* Quick fixes

This is how vulnerability disclosure should work. No lawyers, no threats, no 14-month timelines. Just "thanks for finding this, here's your bounty, we fixed it."

Thanks to Taimi for taking security seriously. Your users are safer because of it.

---

[home](/)
[blog](/blog)

© 2025 bobdahacker