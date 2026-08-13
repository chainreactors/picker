---
title: Attack Technique: AI Clones
url: https://textslashplain.com/2026/08/12/attack-technique-ai-clones/
source: text/plain
date: 2026-08-12
fetch_date: 2026-08-13T04:03:42.836514
---

# Attack Technique: AI Clones

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Technique: AI Clones

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-08-122026-08-12](https://textslashplain.com/2026/08/12/attack-technique-ai-clones/)Posted in[browsers](https://textslashplain.com/category/browsers/), [security](https://textslashplain.com/category/security/)Tags:[AI](https://textslashplain.com/tag/ai/), [InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [scam](https://textslashplain.com/tag/scam/), [security](https://textslashplain.com/tag/security/)

Attackers are adept at using new technologies to enhance their attacks. Earlier this afternoon, for example, I got call from “American Express” suggesting that I needed to “verify a transaction.” The caller used a robotic voice similar to the one used by American Express’ automated systems, and only obvious signals that it was a scam were a) they didn’t have my name or card number, b) I have been using my Visa exclusively for the past few weeks, and c) I have their app, and I get push notifications from it.

Recently, there’s been some excited press about attackers abusing AI-powered “deepfake” technology to persuade users to take unsafe actions (for instance, sending money or sharing secrets) by using a trusted person’s voice or appearance to make the pitch more compelling. Attackers no longer need to limit themselves to [spoofed phone numbers or names](https://textslashplain.com/2023/08/12/sms-gift-card-scams/), they now can use a real-looking voice or video.

But is cloning still an advanced technique, or are we soon going to see it everywhere?

## Free Voice Cloning

The best AI models require money to use and I don’t have the time or attention span to fully explore them, but as a [browser lover/enthusiast](https://textslashplain.com/2020/02/09/demystifying-browsers/), I’m intrigued to look at how convincing a spoof I can do using an **in-browser speech cloning** tool.

Beyond being free, such a tool will allow an attacker to generate speech without calling a web service that might keep logs that could be used to catch the attacker. Behold [SoundTools.io](https://soundtools.io/voice-cloning/). It’s trivial to use and is very upfront about its market position and quality vs. competitors.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-54.png?resize=750%2C177&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-54.png?ssl=1)

To use it, you can either feed it previously recorded audio, or (preferably) a live recording of a paragraph of text:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-50.png?resize=750%2C318&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-50.png?ssl=1)

After collecting the audio sample, the page downloads several large models (just over a gigabyte, cached for later use), to generate a cloned voice. It then allows the user to provide text that should be read aloud, and a desired quality level (lower-quality reproduction is faster):

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-52.png?resize=750%2C537&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-52.png?ssl=1)

The time required depends on the quality chosen and the performance of the browser on your device. In my quick test, the “High quality” level, which requires 60 to 150 seconds per sentence, seems to generate pretty good results.

Finally, when the generation completes, the recording is available to play or download.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-51.png?resize=750%2C663&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-51.png?ssl=1)

Folks who have heard me speak would probably agree that the results are pretty plausible. While [my real voice](https://www.ericlawrence.com/dl/CodeMash2015-LuckingIn-64kbps.mp3) has more “ums”, “uhs”, variable pauses, and animation, careful preparation of the source text would yield even more compelling output. (*For example, the web app doesn’t currently handle “smart quotes” properly, voicing contractions like “Can’t” as “Can Tee”.*)

High Quality example (text from [this post](https://textslashplain.com/2026/08/05/fiddler-in-2026/#:~:text=Fiddler%20Book.-,First%2C%20a%20confession,-%E2%80%94the%20Fiddler%20Web)):

Ultra Quality example (text from [this post](https://textslashplain.com/2020/11/16/objectively-the-best-cat/)):

Both of these are pretty solid, and attackers who worry about the quality of the clone would also likely simulate the speaker being in a noisy environment or suffering from a poor phone signal.

## Not just voice, obviously

Don’t even get me started about how trivial [photo editing](https://photoeditorai.io/) has gotten:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-53.png?resize=750%2C498&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-53.png?ssl=1)

Dating profiles where guys hold a giant fish will never be believable again 🤣

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-56.png?resize=750%2C849&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-56.png?ssl=1)

Running with my buddy

Even today’s high schools can afford to generate [sizzle videos](https://www.youtube.com/watch?v=WDgzL8Z3SfM) for marching bands that would’ve cost millions of dollars to render when *I* was high school.

**Exciting** stuff! But **scary** in the hands of bad guys. I don’t even know what to suggest folks do to stay safe, other than **[slow down and think](https://textslashplain.com/2023/10/16/security-the-impact-of-time/#:~:text=fast%2Dmoving%20attackers.-,The%20Human%20Factor,-Many%20forms%20of)**, be extra skeptical of situations where someone unexpectedly contacts *you*, and be cautious of all non-in-person interactions, *especially* when it’s not a real-time conversation (which [can *still* be faked](https://www.youtube.com/playlist?list=PLxgMOEESA8vgmkkQM_jsD94AZfH9Ve2Vd), but it’s harder).

For years, it’s been easy to [fake an entire company](https://textslashplain.com/2025/04/24/attack-techniques-fake-literally-everything/), but today it’s not too hard to shallowly fake a family member or close friend. Perhaps in the future, we will all share a [Shibboleth](https://en.wikipedia.org/wiki/Shibboleth) with close friends, or demand out-of-band confirmations of all requests?

Stay safe out there, and **don’t believe everything you hear, or see**!

-Eric

### Share this:

* [Share on X (Opens in new window)
  X](https://textslashplain.com/2026/08/12/attack-technique-ai-clones/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2026/08/12/attack-technique-ai-clones/?share=facebook)

### Like this:

Like Loading…

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-08-122026-08-12](https://textslashplain.com/2026/08/12/attack-technique-ai-clones/)Posted in[browsers](https://textslashplain.com/category/browsers/), [security](https://textslashplain.com/category/security/)Tags:[AI](https://textslashplain.com/tag/ai/), [InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [scam](https://textslashplain.com/tag/scam/), [security](https://textslashplain.com/tag/security/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Fiddler in 2026](https://textslashplain.com/2026/08/05/fiddler-in-2026/)

### Leave a Reply[Cancel reply](/2026/08/12/attack-technique-ai-clon...