---
title: New Chrome Zero-Day
url: https://www.schneier.com/blog/archives/2024/09/new-chrome-zero-day.html
source: Schneier on Security
date: 2024-09-11
fetch_date: 2025-10-06T18:30:08.460341
---

# New Chrome Zero-Day

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

## New Chrome Zero-Day

According to Microsoft researchers, North Korean hackers have been [using](https://www.microsoft.com/en-us/security/blog/2024/08/30/north-korean-threat-actor-citrine-sleet-exploiting-chromium-zero-day/) a Chrome [zero-day exploit](https://nvd.nist.gov/vuln/detail/CVE-2024-7971) to steal cryptocurrency.

Tags: [Chrome](https://www.schneier.com/tag/chrome/), [cryptocurrency](https://www.schneier.com/tag/cryptocurrency/), [Microsoft](https://www.schneier.com/tag/microsoft/), [North Korea](https://www.schneier.com/tag/north-korea/), [zero-day](https://www.schneier.com/tag/zero-day/)

[Posted on September 10, 2024 at 7:04 AM](https://www.schneier.com/blog/archives/2024/09/new-chrome-zero-day.html) •
[4 Comments](https://www.schneier.com/blog/archives/2024/09/new-chrome-zero-day.html#comments)

### Comments

Clive Robinson •
[September 10, 2024 9:56 AM](https://www.schneier.com/blog/archives/2024/09/new-chrome-zero-day.html/#comment-440437)

How many times has North Korea pinched the contents of crypto coin wallets?

If it was turned into an Olympic Sport they would be “Front runners” based on what has been claimed in the past…

But Microsoft say,

> *“CVE-2024-7971 is a type confusion vulnerability in the V8 JavaScript and WebAssembly engine …”*

An RCE via JavaScript/WebAssembly,

“Who’d have thunk?”

Well readers here should know by now that JavaScript, WebAssembly, and a big chunk of HTML5 really should not be used for various “in-security” reasons. Not least because they all allow a system to be used in ways most users would not like at all.

Several people here, have pointed this out for years if not decades in the case of JavaScript…

Lazaro •
[September 11, 2024 1:12 PM](https://www.schneier.com/blog/archives/2024/09/new-chrome-zero-day.html/#comment-440454)

I agree with Clive about Javascript. If one had it disabled, one wouldn’t have been affected by this bug. Unfortunately, one would also be unable to read about it in issues.chromium.org; or, at least, I’m assuming that’s why the page has nothing but a “Sign in” button (and the HTML has a lot of obfuscated Javascript).

The Microsoft link is telling me “We are currently experiencing high demand. Please wait and try again later.” Perhaps they should try hosting it on some reliable cloud service… anyway, [here’s an archive.org link for that post](https://web.archive.org/web/20240910013317/https%3A//www.microsoft.com/en-us/security/blog/2024/08/30/north-korean-threat-actor-citrine-sleet-exploiting-chromium-zero-day/). It links to a page about a Windows kernel sandbox-escape exploit, which says “You need to enable JavaScript to run this app” (wait, what app? I’m just trying to view a page).

Sandboxing is kind of a weak point in modern operating systems. As far as I know, most implementations have sandboxed and non-sandboxed programs using the same kernel entry points, each of which is expected to properly enforce the sandbox if necessary. Microsoft could probably fix this more readily than the Linux developers, who need to deal with internal politics and distributors. Swap the interrupt vector table for sandboxed processes, or even put the whole OS under a hypervisor and run them that way (they’ve got Hyper-V, after all, plus a well-funded research division who might enjoy making Windows run under something like seL4).

Bruce Schneier •
[September 11, 2024 4:30 PM](https://www.schneier.com/blog/archives/2024/09/new-chrome-zero-day.html/#comment-440456)

@ Clive:

Hi. Can you please email me.

Clive Robinson •
[September 14, 2024 1:10 PM](https://www.schneier.com/blog/archives/2024/09/new-chrome-zero-day.html/#comment-440489)

@ Bruce,

I have not done private EMail for years, so don’t have anything set up.

Over the W’kend I’m looking into a way to get a message to you, that does not involve any of the idiocy and privacy invasion required by many methods these days.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2024/09/new-chrome-zero-day.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2024/09/new-chrome-zero-day.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2024%2F09%2Fnew-chrome-zero-day.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required):

Comments:
![](https://www.schneier.com/wp-content/themes/schneier/assets/images/loader.gif)

**Allowed HTML**
<a href="URL"> • <em> <cite> <i> • <strong> <b> • <sub> <sup> • <ul> <ol> <li> • <blockquote> <pre>
**Markdown Extra** syntax via <https://michelf.ca/projects/php-markdown/extra/>

Δ

[← Australia Threatens to Force Companies to Break Encryption](https://www.schneier.com/blog/archives/2024/09/australia-threatens-to-force-companies-to-break-encryption.html) [Evaluating the Effectiveness of Reward Modeling of Generative AI Systems →](https://www.schneier.com/blog/archives/2024/09/evaluating-the-effectiveness-of-reward-modeling-of-generative-ai-systems-2.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EFF](https://www.eff.org/), and the Chief of Security Architecture at [Inrupt, Inc.](https://inrupt.com/) This personal website expresses the opinions of none of those organizations.

### Related Entries

* [Microsoft Still Uses RC4](https://www.schneier.com/blog/archives/2025/09/microsoft-still-uses-rc4.html)
* [Zero-Day Exploit in WinRAR File](https://www.schneier.com/blog/archives/2025/08/zero-day-exploit-in-winrar-file.html)
* [First Sentencing in Scheme to Help North Koreans Infiltrate US Companies](https://www.schneier.com/blog/archives/2025/08/first-sentencing-in-scheme-to-help-north-koreans-infiltrate-us-companies.html)
* [Microsoft SharePoint Zero-Day](https://www.schneier.com/blog/archives/2025/07/microsoft-sharepoint-zero-day.html)
* [Signal ...