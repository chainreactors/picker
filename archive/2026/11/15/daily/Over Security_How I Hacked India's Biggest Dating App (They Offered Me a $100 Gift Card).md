---
title: How I Hacked India's Biggest Dating App (They Offered Me a $100 Gift Card)
url: https://pentester.ca/blog/indias-biggest-dating-app-hacked
source: Over Security
date: 2026-11-15
fetch_date: 2026-11-16T08:48:43.722013
---

# How I Hacked India's Biggest Dating App (They Offered Me a $100 Gift Card)

[Skip to main content](#main)

[](/assets/images/Orbs/PT_Orb_LoopDark.webm)
![](/assets/images/Logos/Pentester.ca_Full_Logo_Dark.svg)

[](/assets/images/Orbs/PT_DarkPink_Orb.webm)

* Based in Tokyo,
  [E: [email protected]](/cdn-cgi/l/email-protection#f08798998495989184b080959e849583849582de9391)
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

# How I Hacked India's Biggest Dating App (They Offered Me a $100 Gift Card)

By Kaeden | Pentester.ca | August 19, 2025

*Flutrr, backed by The Times of India, has critical security flaws that expose all user data. They knew about it since November 2024 and still haven't fixed it.*

## What I Found

Every single API endpoint has the same problem: they just trust what the client tells them, No authentication checks. Nothing.

Here's what I could do:

**1. Login to Anyones account:**

The Google login API just takes the users email you wanna login to:

![Flutrr Login Request](/assets/images/blogs/flutrr/login_request.png)

**2. Send messages as anyone:**

![Flutrr WebSocket Message](/assets/images/blogs/flutrr/websocket_message.png)

Just connect to their WebSocket, put any user ID you want in the sender field, and boom - you're messaging as them. I had a fake conversation with my now new wife.

![Flutrr Message Between me and my new Wifey](/assets/images/blogs/flutrr/message_convo.png)

**3. Swipe for other people:**

![Flutrr Swipe Request User 1](/assets/images/blogs/flutrr/swipe_request1.png)
![Flutrr Swipe Request Match](/assets/images/blogs/flutrr/swipe_match.png)

The `/api/v4/user/swipeuser` endpoint lets you swipe left or right as any user. Want to match two random people? Just swipe right for both of them.

**4. Get any Profiles Data**

![Flutrr User Profile Data](/assets/images/blogs/flutrr/user_profile.png)

The API returns essentially everything in the Database for that user - full names, emails, phone numbers, coordinates, device info, even Firebase tokens.

**5. Delete anyones Account**

You can delete anyones account with a custom reason haha funny

![Deleting CTO's Account for Testing Purposes](/assets/images/blogs/flutrr/delete_account.png)

and more, all the apis are dogshit, see for yourself if you're infosec like me 💪🤓

### The Timeline of Incompetence

**November 25, 2024**: First reported these vulnerabilities via email

**March 10th 2025**: After being ignored, I publicly responded to one of the ceo's posts on social media.

**March 17, 2025**: Suddenly they responded to my email offering a $100 Amazon gift card (paid via Stripe)

**August 18, 2025**: Still not fixed. Every vulnerability still works.

### To Flutrr and The Times of India

This is embarrassing. You're India's biggest dating app, backed by a major media company, and you don't check if users are who they say they are.

Your users trust you with:

* Their real names and photos
* Phone numbers and emails
* Private conversations
* Location data

And anyone can access all of it.

$100 for vulnerabilities this severe is insulting. But more importantly - fix your app. Your users deserve better.

### For Flutrr Users

Your data is completely exposed. Anyone can:

* Login to your Account
* Read your private messages
* Send messages as you
* Change your profile
* See your matches and conversations
* Swipe for you

Consider deleting your account until this is fixed.

# Update (2025-08-21) They fixed everything but Sending Messages as someone, and signing in as anyone thru facebook id or email albeit sloppily

They seemed to have tried to fix the sending messages as someone but they check the wrong one, they now check if "sender" matches the signed in user id on the websocket but they use "msgByUserId" to decide who sends the message 💀

I will update once they fixed the message as anyone vuln and login to anyones account vuln.

---

*They've known about this for 9 months. Still not fixed. The Times of India should be ashamed of sponsoring this.*

[Get a Free Consultation
![](/assets/images/Top_Right_Arrow_Black.svg)](https://cal.com/whitehat/30min?user=whitehat)
[![](/assets/images/Top_Right_Arrow_Black.svg)Back to all posts](/blog)

## Read About My Work

* [![](/assets/images/Top_Right_Arrow_Black.svg)Blog](/blog)

© 2026 Designed by [PixelPonderer](https://pixelponderer.com/)

## Got Security?

[[email protected]](/cdn-cgi/l/email-protection#5d2a35342938353c291d2d383329382e29382f733e3c)

[Let's Connect
![](/assets/images/Top_Right_Arrow_Black.svg)](https://cal.com/whitehat/30min?user=whitehat)

## Where to Find Me

* [![](/assets/images/Top_Right_Arrow_Black.svg) LinkedIn](https://www.linkedin.com/in/kaeden69420/)

Based in Tokyo, Japan

Disclaimer: Got Vulnerabilities?® is a parody. Got Milk?® is a registered trademark of the California Milk Processor Board.