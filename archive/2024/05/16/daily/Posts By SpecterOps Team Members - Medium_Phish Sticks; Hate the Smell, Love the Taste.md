---
title: Phish Sticks; Hate the Smell, Love the Taste
url: https://posts.specterops.io/phish-sticks-hate-the-smell-love-the-taste-f4db9de888f7?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-05-16
fetch_date: 2025-10-06T17:17:47.855551
---

# Phish Sticks; Hate the Smell, Love the Taste

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff4db9de888f7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fphish-sticks-hate-the-smell-love-the-taste-f4db9de888f7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fphish-sticks-hate-the-smell-love-the-taste-f4db9de888f7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-f4db9de888f7---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-f4db9de888f7---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

## Phishing School

# Phish Sticks; Hate the Smell, Love the Taste

## I’ll Make You Great at Phishing or Your Money Back

[![Forrest Kasler](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*twL-x8eyh-Q1_GWn)](https://medium.com/%40fakasler?source=post_page---byline--f4db9de888f7---------------------------------------)

[Forrest Kasler](https://medium.com/%40fakasler?source=post_page---byline--f4db9de888f7---------------------------------------)

8 min read

·

May 15, 2024

--

Listen

Share

I am already making you better at phishing.

Right now.

How could that be possible? Please, don’t worry about specifics right now. Just trust that I am making you better at phishing.

Why would I be so selfless to boost your phishing skills free of charge? Again, you don’t need to know. Just know that this is our agreement: you keep reading my words, and I will make you better at phishing. Nay. Great at phishing! It will only hurt a little, but the pain will be well worth it. Sounds like a bargain? Then welcome to my school of phish! Now please open your textbooks to lesson number 1…

## Don’t Give Up Before You Start!

If you’ve done penetration testing for any extended length of time, you’ll regularly hear the phrase, “no one likes phishing” in regards to client requests to perform social engineering as part of a penetration test or red team operation.

For many, this request always seems to entail the mind-numbingly banal task of setting up phishing infrastructure, choosing a pretext scenario, testing the scenario, and crossing your frustrated fingers in the hopes that you’ll dupe someone into clicking a malicious link. The overall approach is blunt, half-hearted, and can leave you feeling either guilty for ruining someone else’s day or just downright bored.

Here are some other general gripes I’ve heard from my fellow pen-testers regarding phishing:

* **One Phish —** Phishing is a total crapshoot, especially since you can’t consistently replicate your results
* **No Phish** — Since impact happens in post-exploitation, the phishing portion of the assessment is nothing but a waste of time
* **Gross Phish** — Social engineering can make red teamers feel icky about themselves, so they prefer to avoid it entirely
* **Eventual Phish** — If we follow the concept of “assume breach”, phishing seems pointless because something is inevitably bound to work and infiltrate the environment
* **Struggle Phish** — My client just wants me to flounder (pun intended)

These are all valid points, and I’ve probably used each of these arguments myself on multiple occasions to either explain to my boss or client why we shouldn’t do phishing. ***However*, I would like to challenge you with a simple question**:

Let’s assume your phishing attempt is actually successful. Some poor unsuspecting target clicked your link or file, you delivered a payload that called home and you just got the alert that you have a shell. **On a scale from,** “**Ugh. This is so boring! I’ll just take my lunch break and deal with this later…” to, “Holy crap! It worked! I’m going to dance around the office and look for someone to high five!”, how do you feel?**

![meterpreter dance]()

If an outside observer saw your reaction to getting an “organic” shell, they might be fooled into thinking you really **like** phishing. They may even think you …love… it?

![phishsticks: love’m]()

If you are in the right industry, you love shells, and you better be honest with me that you feel like a beast when you cede access for yourself. So…does everyone hate phishing? Not really! In fact, most of us may like it a thousand times more than we think we do! When we say we “hate phishing,” that’s only because we don’t want to admit something else:

What we *actually* hate is **losing**!

![Loooosers]()

Penetration testing isn’t a game, but it can still “feel” like it is and it’s extremely hard to let go of that feeling. We also want to do a good job and if our phish fries and dies versus catching the target hook, line, and sinker; it can feel like we’ve done a bad job. And here’s the worst part: I know it hurts to hear, but if you “hate phishing”, it’s most likely because your phishing campaigns suck. That may sting a little, but please just let that sink in for a minute. Let’s use that feeling as motivation to improve.

If you are completely new to penetration testing, a dead in the water phishing attempt may not even be your fault. You were likely thrown into the deep end without any formal training (or worse: had a bad teacher and only learned some bad or outdated techniques). However, in a field of highly curious self-learners, I think that “I’m a complete guppy at this” has limited reach. At some point, we need to face the fact that most phishing campaigns don’t work because we don’t put the same level of effort into them as we do post-exploitation. If you’re still with me at this point, let’s talk about how we as a “grouper” can do better.

## “Phishing is Hard”

Yes, *winning* at phishing is hard, but it’s a lot easier than evading the latest ERD/XRD/AI endpoint defenses; so don’t kid yourself into thinking you can’t do it. As red teamers, we bypass endpoint defense products every day and many of the same methodologies and techniques we use to bypass those products can be applied to bypass email security as well.

Often, it’s the unknowns that bug us the most when it comes to failed phishing attempts. There are multiple steps that all have to go right to have a successful phishing campaign. To give ourselves the best chance of success, we need to identify potential failure points and address each one. Let’s drag all of these lurking failure points out into the light where we can see and analyze them:

* **Bad Email List (“Sparse Waters”)** — You can’t find good contacts to target
* **Sender Reputation Block (“Smelling Phishy”)** — Before the mail server even lets you send a message, they might not trust you; this could be because your IP or domain have a bad reputation or no reputation at all
* **Content Block** **(“Bad Bait”)** — You try sending any reference to “Nigeria” and “prince” in...