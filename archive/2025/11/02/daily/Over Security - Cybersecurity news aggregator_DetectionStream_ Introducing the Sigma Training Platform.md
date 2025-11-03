---
title: DetectionStream: Introducing the Sigma Training Platform
url: https://kostas-ts.medium.com/detectionstream-introducing-the-sigma-training-platform-574721f18f45
source: Over Security - Cybersecurity news aggregator
date: 2025-11-02
fetch_date: 2025-11-03T03:15:39.787052
---

# DetectionStream: Introducing the Sigma Training Platform

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F574721f18f45&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fkostas-ts.medium.com%2Fdetectionstream-introducing-the-sigma-training-platform-574721f18f45&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fkostas-ts.medium.com%2Fdetectionstream-introducing-the-sigma-training-platform-574721f18f45&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# DetectionStream: Introducing the Sigma Training Platform

[![Kostas](https://miro.medium.com/v2/resize:fill:64:64/1*BtTfw89t0Sfap1SKrF3hvA.jpeg)](/?source=post_page---byline--574721f18f45---------------------------------------)

[Kostas](/?source=post_page---byline--574721f18f45---------------------------------------)

4 min read

·

2 hours ago

--

Listen

Share

Press enter or click to view image in full size

![]()

My goal in creating DetectionStream was to share my knowledge and help others discover the wide range of detection frameworks available. I’ve always wanted to transform learning detection engineering into an exciting, game-like experience. Watching our progress now, it feels as though that personal vision is truly coming to life.

I’ve been working on this for a while now, and it’s finally in a state that I’m happy to publish: introducing the [**Sigma Playground’s new Training Platform**](https://detectionstream.com/sigma/training/gamified). If you’ve ever wanted to get your hands dirty and really master detection engineering, this is for you. I’ve designed it to be a fun, gamified way to learn how to write, test, and validate Sigma rules.

For too long, learning defensive security has been a bit…dry. We read a lot of theory, but it’s hard to find a place to practice. I wanted to change that. The Training Platform is my answer, a space where you can learn by doing, in a hands-on, practical way.

## So, what exactly is the Training Platform?

It’s a gamified learning environment where you can tackle over 20 challenges right from the get-go. I have used the event logs from the [EVTX-ATTACK-SAMPLES](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES) repository to create those first challenges. Each challenge is a real-world scenario, complete with log snippets and a clear goal. Your mission, should you choose to accept it, is to write a Sigma rule that detects the simulated malicious activity.

When you submit your rule, you’ll get instant feedback on whether it worked and why. No more guessing if your logic is sound, you’ll know right away. It’s all about learning by doing, not just by reading.

## What’s Inside?

Press enter or click to view image in full size

![]()

Sigma Training Platform

I’ve packed the Training Platform with features to make learning as fun and effective as possible:

* **An Interactive Challenge System:** You’ll get to write Sigma rules against real-world log samples. Each of the 20+ challenges comes with a goal, hints, and a validation engine to test your work.
* **Real-Time Rule Evaluation:** Get instant feedback on your rules. I’ll tell you not just *if* your rule passed, but *why*, so you can learn from your mistakes.
* **Gamified Learning:** This is where the fun really starts. You’ll earn points for solving challenges, and the fewer attempts you take, the more points you get.
* **A Progressive Hint System:** If you get stuck, don’t worry. I’ve built in a hint system to give you a nudge in the right direction.
* **Difficulty Levels for Everyone:** Whether you’re just starting out or you’re a seasoned pro, there’s a challenge for you. I’ve categorized them as beginner, intermediate, and advanced.
* **Community-Powered Fun:** What’s a game without a little friendly competition? There’s a leaderboard to see how you stack up, and you can like, comment on, and even create your own challenges to share with everyone else.

## Your Playground, Your Rules

Press enter or click to view image in full size

![]()

Chellenge builder

I believe that the best way to learn is to teach, which is why I’ve also built a **Challenge Builder**. This isn’t just my platform; it’s ours. You can use the intuitive, wizard-based interface to create and submit your own detection challenges. Think you’ve got a great idea for a scenario? Build it, share it, and let the community learn from you.

This is perfect for:

* **Personal Growth:** Solidify your own knowledge by creating a challenge around a new technique you’ve learned.
* **Team Training:** Create a private set of challenges for your security team to work through. It’s a great way to run internal training exercises and level up your whole team’s skills.
* **Community Contribution:** Share your expertise with the wider security community. Your challenge could be the one that helps someone else have that “aha!” moment.

When you submit, you’ll receive an email immediately confirming that I’ve received your challenge. I’ll personally take a look at everything you’ve put together, the logs, the validation, the whole nine yards. If it’s good to go, I’ll publish it for the community to enjoy. If it needs a little tweaking, I’ll get in touch with you directly. Either way, you’ll get another email as soon as your challenge goes live.

## A Note on Your Privacy

This is important to me, so I want to be crystal clear about how your data is handled. Everything you do in the playground runs on the client-side, in your browser. **Nobody but you will know what you’re submitting.**

The only thing the platform does is check if your submitted rule is correct or incorrect for a given challenge, and we make a note of that so we can track your score. That’s it. Nothing you write is kept or stored. There is no statistic collection or anything like that to worry about. The platform is free for everyone, and I’ve designed it to require the absolute minimum amount of information to operate.

## Come Check it Out!

The Sigma Playground’s Training Platform is live now. I’ve put a lot of heart into making this a genuinely useful and fun tool for the community, and I’m excited for you to try it out. I hope it helps you level up your detection engineering skills.

Feel free to dive in and give the 20+ challenges a try. I’m looking forward to seeing you on the leaderboard!

Happy detecting!

## References

[1] SigmaHQ. (2025). *Sigma Conditions*. Retrieved from <https://sigmahq.io/docs/basics/conditions.html>

[2] SigmaHQ. (2025). *Sigma Modifiers*. Retrieved from <https://sigmahq.io/docs/basics/modifiers.html>

[Detection Engineering](https://medium.com/tag/detection-engineering?source=post_page-----574721f18f45---------------------------------------)

[Threat Hunting](https://medium.com/tag/threat-hunting?source=post_page-----574721f18f45---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----574721f18f45---------------------------------------)

--

--

[![Kostas](https://miro.medium.com/v2/resize:fill:96:96/1*BtTfw89t0Sfap1SKrF3hvA.jpeg)](/?source=post_page---post_author_info--574721f18f45-----------------------------------...