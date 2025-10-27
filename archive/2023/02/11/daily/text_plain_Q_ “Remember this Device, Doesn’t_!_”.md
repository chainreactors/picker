---
title: Q: “Remember this Device, Doesn’t?!?”
url: https://textslashplain.com/2023/02/10/q-remember-this-device-doesnt/
source: text/plain
date: 2023-02-11
fetch_date: 2025-10-04T06:20:57.936017
---

# Q: “Remember this Device, Doesn’t?!?”

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Q: “Remember this Device, Doesn’t?!?”

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-02-102023-02-14](https://textslashplain.com/2023/02/10/q-remember-this-device-doesnt/)Posted in[browsers](https://textslashplain.com/category/browsers/), [web](https://textslashplain.com/category/tech/web/)Tags:[browsers](https://textslashplain.com/tag/browsers/), [Chrome](https://textslashplain.com/tag/chrome/), [cookies](https://textslashplain.com/tag/cookies/), [Edge](https://textslashplain.com/tag/edge/), [privacy](https://textslashplain.com/tag/privacy/)

**Q:** *Many websites offer a checkbox to “Remember this device” or “Remember me” but it often doesn’t seem to work. For example, this option on AT&T’s website shown when prompting for a 2FA code:*

[![](https://textslashplain.com/wp-content/uploads/2023/02/image-5.png?w=634)](https://textslashplain.com/wp-content/uploads/2023/02/image-5.png)

*…doesn’t seem to work. What’s up with that?*

**A:** Unfortunately, there’s no easy answer here. There is no browser standard for how to implement a feature like this, so different websites implement it differently.

Virtually all of these systems are dependent upon storing some sort of long-lived token within one of the browser’s storage areas (cookies, DOM storage, IndexedDB, etc). Anything which interferes with your browser’s storage areas can interfere with the long-lived token:

* Depending upon how the site is coded, privacy features like Edge’s Tracking Prevention might interfere with storage of the token to begin with.
* There are [many different features and operations](https://textslashplain.com/2022/05/26/losing-your-cookies/) that can cause one or more storage items to subsequently be become inaccessible. For example, privacy controls, 3rd party utilities, user-actions, use of multiple browser channels, and so on. (*Please* see the [blog post](https://textslashplain.com/2022/05/26/losing-your-cookies/) for a more comprehensive list).

Even if the token is successfully stored by the website and is available on later site loads, the server might choose to ignore it.

* Some sites will ignore a cached token if the visitor appears to be coming from a significantly different geographic location, e.g. because you’ve either moved your laptop or enabled a VPN.
* Some sites will ignore a cached token if some element of the user’s environment changes: for instance, if the browser’s configured languages are different than when the token was stored.
* We encountered one site whose auth flow broke if the browser’s `User-Agent` string changed– this site broke when we tried to fix a compatibility issue by [automatically overriding the User-Agent](https://textslashplain.com/2022/08/04/understanding-browser-channels/#:~:text=Edge%20has%20a%20%E2%80%9C-,Domain%20Actions,-%E2%80%9D%20feature%20to%20accommodate) value.
* Some sites will expire a cached token after a certain (often undocumented) timeframe.
* Some sites will expire a cached token if some other security setting in the account is changed, or if there are signs that the account’s login is under bruce-force attack.
* Some sites simply change how they work over time. For example, Fidelity recently sent an email to customers with 2FA announcing that they’ll no longer respect a “remember this device” option:

[![](https://textslashplain.com/wp-content/uploads/2023/02/image-6.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/02/image-6.png)

* Some sites will expire a cached token if some other risk heuristic triggers (e.g. a user begins logging in at an unusual time of day, etc).

#### Debugging

Debugging problems like this is often non-trivial, but you might try things like:

* Watch the F12 Developer Tools’ console to look for any notes about storage being blocked by a browser privacy feature, or a JavaScript exception.
* See if the “Remember me” behavior works once from the same browser instance.
* See if the “Remember me” behavior works after restarting the browser.
* See if the “Remember me” behavior works properly in a different browser or [channel](https://textslashplain.com/2022/08/04/understanding-browser-channels/).
* Poke through the F12 Developer Tools’ `Application` tab to see what sorts of Storage the site’s login flow is writing.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2023/02/10/q-remember-this-device-doesnt/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2023/02/10/q-remember-this-device-doesnt/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-02-102023-02-14](https://textslashplain.com/2023/02/10/q-remember-this-device-doesnt/)Posted in[browsers](https://textslashplain.com/category/browsers/), [web](https://textslashplain.com/category/tech/web/)Tags:[browsers](https://textslashplain.com/tag/browsers/), [Chrome](https://textslashplain.com/tag/chrome/), [cookies](https://textslashplain.com/tag/cookies/), [Edge](https://textslashplain.com/tag/edge/), [privacy](https://textslashplain.com/tag/privacy/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Attack Techniques: Blended Attacks via Telephone](https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/)

[Next Post Next post:
Slow Seaside Half](https://textslashplain.com/2023/03/01/slow-seaside-half/)

### Leave a comment [Cancel reply](/2023/02/10/q-remember-this-device-doesnt/#respond)

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

* 2,396,375 hits

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

* [Comment](https://textslashplain.com/2023/02/10/q-remember-this-device-doesnt/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://secure.gravatar.com/blavatar/82d40d311a11c0cfe6d128d043693048c9216bb5abceef9296346a9b262f3f95?s=50&d=https%3A%2F%2Fs2.wp.com%2Fi%2Flogo%2Fwpcom-gray-white.png) text/plain](https://textslashplain.com)

  Join 264 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%2...