---
title: Why Take9 Won’t Improve Cybersecurity
url: https://www.schneier.com/blog/archives/2025/05/why-take9-wont-improve-cybersecurity.html
source: Schneier on Security
date: 2025-05-31
fetch_date: 2025-10-06T22:28:57.549454
---

# Why Take9 Won’t Improve Cybersecurity

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Why Take9 Won’t Improve Cybersecurity

There’s a new cybersecurity awareness campaign: Take9. The idea is that people—you, me, everyone—should just pause for nine seconds and think more about the link they are planning to click on, the file they are planning to download, or whatever it is they are planning to share.

There’s a [website](https://pausetake9.org/)—of course—and a [video](https://www.youtube.com/watch?v=GlmplblxsGM), well-produced and scary. But the campaign won’t do much to improve cybersecurity. The advice isn’t reasonable, it won’t make either individuals or nations appreciably safer, and it deflects blame from the real causes of our cyberspace insecurities.

First, the advice is not realistic. A nine-second pause is an eternity in something as routine as using your computer or phone. Try it; use a timer. Then think about how many links you click on and how many things you forward or reply to. Are we pausing for nine seconds after every text message? Every Slack ping? Does the clock reset if someone replies midpause? What about browsing—do we pause before clicking each link, or after every page loads? The logistics quickly become impossible. I doubt they tested the idea on actual users.

Second, it largely won’t help. The industry should know because we tried it a decade ago. “[Stop. Think. Connect.](https://www.dhs.gov/xlibrary/assets/stop-think-connect-campaign-fact-sheet.pdf)” was an [awareness](https://www.stopthinkconnect.org/) [campaign](https://www.consumer.ftc.gov/sites/default/files/articles/pdf/pdf-0002-heads-up.pdf) from 2016, by the Department of Homeland Security—this was before CISA—and the National Cybersecurity Alliance. The message was basically the same: Stop and think before doing anything online. It didn’t work then, either.

Take9’s website says, “Science says: In stressful situations, wait 10 seconds before responding.” The problem with that is that clicking on a link is not a stressful situation. It’s normal, one that happens hundreds of times a day. Maybe you can train a person to count to 10 before punching someone in a bar but not before opening an attachment.

And there is no basis in science for it. It’s a folk belief, all over the Internet but with no actual research behind it—like the five-second rule when you drop food on the floor. In emotionally charged contexts, most people are already overwhelmed, cognitively taxed, and not functioning in a space where rational interruption works as neatly as this advice suggests.

### Pausing Adds Little

Pauses help us break habits. If we are clicking, sharing, linking, downloading, and connecting out of habit, a pause to break that habit works. But the problem here isn’t habit alone. The problem is that people aren’t able to differentiate between something legitimate and an attack.

The Take9 website says that nine seconds is “time enough to make a better decision,” but there’s no use telling people to stop and think if they don’t know what to think about after they’ve stopped. Pause for nine seconds and… do what? Take9 offers no guidance. It presumes people have the cognitive tools to understand the myriad potential attacks and figure out which one of the thousands of Internet actions they take is harmful. If people don’t have the right knowledge, pausing for longer—even a minute—will do nothing to add knowledge.

The three-part [suspicion, cognition, and automaticity model (SCAM)](https://journals.sagepub.com/doi/abs/10.1177/0093650215627483) is one way to think about this. The first is lack of knowledge—not knowing what’s risky and what isn’t. The second is habits: people doing what they always do. And third, using flawed mental shortcuts, like believing PDFs to be safer than Microsoft Word documents, or that mobile devices are safer than computers for opening suspicious emails.

These pathways don’t always occur in isolation; sometimes they happen together or sequentially. They can influence each other or cancel each other out. For example, a lack of knowledge can lead someone to rely on flawed mental shortcuts, while those same shortcuts can reinforce that lack of knowledge. That’s why meaningful behavioral change requires more than just a pause; it needs cognitive scaffolding and system designs that account for these dynamic interactions.

A successful awareness campaign would do more than tell people to pause. It would guide them through a [two-step process](https://www.penguinrandomhouse.com/books/710629/the-weakest-link-by-arun-vishwanath/). First trigger suspicion, motivating them to look more closely. Then, direct their attention by telling them what to look at and how to evaluate it. When both happen, the person is far more likely to make a better decision.

This means that pauses need to be context specific. Think about email readers that embed warnings like “EXTERNAL: This email is from an address outside your organization” or “You have not received an email from this person before.” Those are specifics, and useful. We could imagine an AI plug-in that warns: “This isn’t how Bruce normally writes.” But of course, there’s an arms race in play; the bad guys will use these systems to figure out how to bypass them.

This is all hard. The old cues aren’t there anymore. Current phishing attacks have evolved from those older Nigerian scams filled with grammar mistakes and typos. Text message, voice, or video scams are even harder to detect. There isn’t enough context in a text message for the system to flag. In voice or video, it’s much harder to trigger suspicion without disrupting the ongoing conversation. And all the false positives, when the system flags a legitimate conversation as a potential scam, work against people’s own intuition. People will just start ignoring their own suspicions, just as most people ignore all sorts of warnings that their computer puts in their way.

Even if we do this all well and correctly, we can’t make people immune to social engineering. Recently, both cyberspace activist [Cory Doctorow](https://doctorow.medium.com/how-i-got-scammed-0ae9bd453490) and security researcher [Troy Hunt](https://doctorow.medium.com/https-pluralistic-net-2025-04-05-troy-hunt-teach-a-man-to-phish-c2ab7956c026)—two people who you’d expect to be excellent scam detectors—got phished. In both cases, it was just the right message at just the right time.

It’s even worse if you’re a large organization. Security isn’t based on the average employee’s ability to detect a malicious email; it’s based on the worst person’s inability—the weakest link. Even if awareness raises the average, it won’t help enough.

### Don’t Place Blame Where It Doesn’t Belong

Finally, all of this is bad public policy. The Take9 campaign tells people that they can stop cyberattacks by taking a pause and making a better decision. What’s not said, but certainly implied, is that if they don’t take that pause and don’t ma...