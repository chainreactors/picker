---
title: Lenovo P1, Gen7
url: https://textslashplain.com/2024/10/28/lenovo-p1-gen7/
source: text/plain
date: 2024-10-29
fetch_date: 2025-10-06T18:50:01.655820
---

# Lenovo P1, Gen7

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Lenovo P1, Gen7: Meh

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-10-282024-11-14](https://textslashplain.com/2024/10/28/lenovo-p1-gen7/)Posted in[reviews](https://textslashplain.com/category/reviews/), [tech](https://textslashplain.com/category/tech/)Tags:[hardware](https://textslashplain.com/tag/hardware/), [Lenovo](https://textslashplain.com/tag/lenovo/)

I’ve been a loyal user of Thinkpads for over twenty-five years now, and I currently own four (with another on loan from Microsoft).

In July, the screen on my Lenovo X1 Yoga Gen 6 [failed](https://x.com/ericlaw/status/1809250450300149914) at an inopportune time, and my 8yo broke the screen on my backup (T480S), so I rush-ordered a Lenovo P1 Gen7 workstation laptop (22 cores, 64gigs of memory) to stand in while awaiting warranty replacement on the Yoga’s screen. After massive discounts, the cost with tax fell to a still-spendy $2,890. (*The Yoga screen replacement went well, and I later replaced the T480S’ screen myself for ~$79 from LaptopScreen.com*).

Unfortunately, when my new P1 workstation arrived, I discovered to my dismay that it had the same problems as my nearly-unused X1 Extreme Gen 3 — the OLED touchscreen, while mostly beautiful, had super-distracting quirks — it seemed to flicker, and almost have a screen door effect under certain conditions (the newer laptop might be the same panel as on the older one). Fortunately, these screens have now been in the market long enough that I wasn’t gaslit into thinking it was “*just a* me *problem*,” and searches turned up the explanation — the screendoor effect comes from the touch-digitizer, and the flicker comes from the way OLED power-management is implemented. Fortunately, I was able to rush-order the same machine with the non-touch-LCD (21KV001CUS) for $2,381 so I could do a side-by-side comparison. Sure enough, the regular LCD seems fine, and saving $500 for a lower-end screen and a cheaper GPU (Ada 3000, RTX 4070) that seemed to benchmark almost as well.

The Gen7 is pretty fast (although building Chrome still takes *ages*) and the keyboard and big screen are great. The fans seem to run more than they should, (although bizarrely they’re silent as I write this post for the first time in weeks) and it’s not *too* crazy heavy. Replacing physical buttons for the trackpoint with a tiny section at the top of the trackpad was a surprisingly-annoying downgrade.

Unfortunately, the laptop’s reliability has been poor. First, the Nvidia drivers were blue-screening the system and I remembered why I don’t like gaming GPUs– I don’t play games, and their drivers tend to prioritize performance over stability. So I disabled the Nvidia and started using just the integrated (Intel) GPU.

More recently, the system started ignoring all input shortly after boot — the trackpoint/trackpad wouldn’t move the cursor, wouldn’t accept clicks, the keyboard wouldn’t work, etc. I *thought* I had narrowed down the problem to the [“Virtual Lock” feature](https://ellipticlabs.com/mfn_news/elliptic-labs-and-lenovo-jointly-launch-first-software-only-human-presence-detection-ai-virtual-presence-sensor-on-top-selling-thinkpad-t14/) that aims to automatically lock the PC when you walk away. I’d never enabled the feature and even after turning off “User Presence Sensing” in the UEFI Settings the problem continued. Setting the Services (`Virtual Lock Sensor` and `Elliptic Human Presence Detection`) to `Disabled` in Windows Services and disabling the Virtual Lock Sensor in Device Manager’s `Software Components` appears to have helped…

[![](https://textslashplain.com/wp-content/uploads/2024/10/image-14.png?w=500)](https://textslashplain.com/wp-content/uploads/2024/10/image-14.png)

Fingers crossed!

Update: It didn’t. There’s *something* else that seems to be causing this. I’ve killed off some more of Lenovo’s preloaded software, and learned that the hard hang lasts for ~100 seconds before the system becomes responsive again, forcing me to just “wait” rather than hard-rebooting.

Some recent update to the system also started causing terrible echo for my Teams calls, which I’m working around by using an external speaker/microphone. *Lame*.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2024/10/28/lenovo-p1-gen7/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2024/10/28/lenovo-p1-gen7/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-10-282024-11-14](https://textslashplain.com/2024/10/28/lenovo-p1-gen7/)Posted in[reviews](https://textslashplain.com/category/reviews/), [tech](https://textslashplain.com/category/tech/)Tags:[hardware](https://textslashplain.com/tag/hardware/), [Lenovo](https://textslashplain.com/tag/lenovo/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:](https://textslashplain.com/2024/10/25/defensive-technology-antimalware-scan-interface-amsi/)

[Next Post Next post:](https://textslashplain.com/2024/11/11/on-politics/)

### Leave a comment [Cancel reply](/2024/10/28/lenovo-p1-gen7/#respond)

Δ

## Search Text/Plain

Search for:

## Pages

* [About](https://textslashplain.com/about/)
* [Browse All Posts](https://textslashplain.com/browse-all-posts/)
* [Categories](https://textslashplain.com/categories/)
* [Cruises](https://textslashplain.com/cruises/)
* [IEInternals Archive](https://textslashplain.com/ieinternals-archive/)
* [Races](https://textslashplain.com/races/)

## RSS

[![RSS Feed](https://textslashplain.com/i/rss/orange-small.png)](https://textslashplain.com/feed/ "Subscribe to Posts") [RSS - Posts](https://textslashplain.com/feed/ "Subscribe to Posts")

## Blog Stats

* 2,392,671 hits

## Categories

Categories
Select Category
bluebadge  (16)
books  (3)
browsers  (183)
design  (21)
dev  (84)
fiddler  (25)
life  (52)
perf  (20)
politics  (2)
privacy  (26)
reviews  (2)
running  (18)
security  (158)
storytelling  (47)
tech  (34)
travel  (9)
Uncategorized  (16)
web  (151)
windmills  (12)

![ericlaw](https://2.gravatar.com/avatar/89c27d27b73dd3690b3dad59f3a539d1?s=320)

#### [ericlaw](https://gravatar.com/ericlaw1979)

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity.

[View Full Profile →](https://gravatar.com/ericlaw1979)

[text/plain](https://textslashplain.com/),
[A WordPress.com Website](https://wordpress.com/?ref=footer_custom_acom).

* [Comment](https://textslashplain.com/2024/10/28/lenovo-p1-gen7/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)

  Join 264 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Ftextslashplain.com%252F2024%252F10%252F28%252Flenovo-p1-gen7%252F)
* + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)
  + Subscribe
    Subscribed
  + [Sign up](https://wordpress.com...