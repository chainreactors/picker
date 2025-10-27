---
title: Content-Blocking in Manifest v3
url: https://textslashplain.com/2024/10/13/content-blocking-in-manifest-v3/
source: text/plain
date: 2024-10-14
fetch_date: 2025-10-06T18:47:27.739179
---

# Content-Blocking in Manifest v3

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Content-Blocking in Manifest v3

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-10-132025-05-27](https://textslashplain.com/2024/10/13/content-blocking-in-manifest-v3/)Posted in[browsers](https://textslashplain.com/category/browsers/), [dev](https://textslashplain.com/category/dev/), [web](https://textslashplain.com/category/tech/web/)Tags:[dev](https://textslashplain.com/tag/dev/), [extensions](https://textslashplain.com/tag/extensions/), [privacy](https://textslashplain.com/tag/privacy/), [security](https://textslashplain.com/tag/security/)

I’ve written about selectively blocking content in browsers [several](https://textslashplain.com/2015/06/10/collateral-damage/) [times](https://web.archive.org/web/20101205015334/http%3A//blogs.msdn.com/b/ie/archive/2010/11/30/selectively-filtering-content-in-web-browsers.aspx#:~:text=Evaluation%20of%20Blocking%20Mechanisms) over the last two decades. *In this post, I don’t aim to convince you that ad-blocking is good or bad, instead focusing on one narrow topic.*

Circa 2006, I was responsible for changing IE so that you could simply add an advertising site to the Restricted Sites zone and none of its script would load. Later, [in 2010](https://web.archive.org/web/20101205015334/http%3A//blogs.msdn.com/b/ie/archive/2010/11/30/selectively-filtering-content-in-web-browsers.aspx#:~:text=Evaluation%20of%20Blocking%20Mechanisms), I wrote a bit about the landscape of ad-blocking on the IEBlog.

More recently, Apple introduced [Content-Blocking framework](https://textslashplain.com/2015/06/10/collateral-damage/) for their browser in 2015, and in 2019 the Edge team released [Tracking Prevention](https://learn.microsoft.com/en-us/microsoft-edge/web-platform/tracking-prevention), which blocks many ads in its Strict Mode.

### Manifest v3

Recently, there’s been a bit of an outcry about Google’s move to require Chrome extensions be built atop a new platform named Manifest v3. This *long overdue* change attempts to mitigate the overprivileged Chrome extensions framework. V2 poses [security, privacy, and performance risks](https://textslashplain.com/2024/03/07/browser-extensions-powerful-and-potentially-dangerous/) to users, and has been abused (intentionally and unintentionally) by extension authors over the years.

No good deed goes unpunished, however, and conspiracy theorists have argued that Google is doing this to prevent ad-blockers from working. These theories aren’t *entirely* crazy — Google is, after all, first-and-foremost an advertising company. Where the theory falls apart, however, is that Google’s ads are among the easiest to block. While MV3 may make it more challenging to block some ad providers, you can still trivially choke off more than half of Google’s ad revenue in under a dozen lines of code. *If MV3* were *a conspiracy on Google’s part, it’s a jaw-droppingly ineffective one.*

### Step-by-Step: Blocking Google Ads

To save myself some typing, let’s start with a trivial MV3 extension I built for web developers (which should [soon be obsolete](https://chromium-review.googlesource.com/c/chromium/src/%2B/5923046) 🤞).

Clone [the code](https://github.com/ericlaw1979/NoLocalHSTS) to your local disk. Create a new file named `adsense.json`:

```
[{
    "id" : 1,
    "priority": 1,
    "action" : {
        "type" : "block"
    },
    "condition" : {
        "urlFilter" : "||pagead2.googlesyndication.com",
        "resourceTypes" : ["script"]
  }
}]
```

As you can see, Manifest v3 makes it utterly trivial to block requests to Google’s ad network.

Modify the existing `manifest.json` file with new values:

[![](https://textslashplain.com/wp-content/uploads/2024/10/image-7.png?w=738)](https://textslashplain.com/wp-content/uploads/2024/10/image-7.png)

Remove the old `localhost.json` and add the new `adsense.json` file:

[![](https://textslashplain.com/wp-content/uploads/2024/10/image-6.png?w=877)](https://textslashplain.com/wp-content/uploads/2024/10/image-6.png)

## Testing the Extension

First, visit a page that has a Google ad on it to ensure that it loads as expected:

[![](https://textslashplain.com/wp-content/uploads/2024/10/image-9.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/10/image-9.png)

Now, inside Chrome, visit `chrome://extensions`, toggle the `Developer Mode` toggle, and click the `Load Unpacked` button. Select your extension’s folder:

[![](https://textslashplain.com/wp-content/uploads/2024/10/image-8.png?w=758)](https://textslashplain.com/wp-content/uploads/2024/10/image-8.png)

Revisit the page with the Google ad and observe that it no longer loads. The Developer Tools console notes that the request for the JavaScript was blocked:

[![](https://textslashplain.com/wp-content/uploads/2024/10/image-10.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/10/image-10.png)

The MV3 ad-blocking approach is very easy to work with. Simply declare which sites you want to block, and they’re blocked. No slow and complicated network parsing or anything like that.

## But…but… but…

Skeptical readers will note that this trivial approach blocks *one* type of Google’s ads, but not *every* type of Google ads. And that’s certainly true.

Fifteen years ago, I described the cat and mouse game between ad-hating users and advertising platforms as “***a grenade fight, where both sides get infinite grenades***.” Nothing has changed.

**Economics rules everything around us.**

Because sites need ad revenue to survive, they rely on ads not being blocked. Thus, ad networks have incentives to disrupt ad blockers. When a new blocking technique is adopted, the ad network responds. There are entire businesses built around trying to coax/annoy users to allow ads; one of the biggest is a platform called [Admiral](https://www.getadmiral.com/). Because I browse with Edge’s Tracking Prevention: Strict enabled, almost every ad-supported site I visit pops a banner like this one:

[![](https://textslashplain.com/wp-content/uploads/2024/10/image-11.png?w=876)](https://textslashplain.com/wp-content/uploads/2024/10/image-11.png)

Some sites allow a “Continue without supporting us” link, and some do not. It’s the site’s choice. Major publishers might not rely on third-party frameworks and instead perform their own ad-blocking detection.

In response, some ad-blockers introduce ad-blocker-blockers, and the publishers then have ad-blocker-blocker-blockers. And the battle rages on, with dueling JavaScript files burning your battery while a quiet war rages under the surface.

-Eric

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2024/10/13/content-blocking-in-manifest-v3/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2024/10/13/content-blocking-in-manifest-v3/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-10-132025-05-27](https://textslashplain.com/2024/10/13/content-blocking-in-manifest-v3/)Posted in[browsers](https://textslashplain.com/category/browsers/), [dev](https://textslashplain.com/category/dev/), [web](https://textslashplain.com/category/tech/web/)Tags:[dev](https://textslashplain.com/tag/dev/), [extensions](https://textslashplain.com/tag/extensions/), [privacy](https://textslashplain.com/tag/privacy/), [security](https://textslashplain.com/tag/security/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Attack Techniques: Encrypted Archives](https://tex...