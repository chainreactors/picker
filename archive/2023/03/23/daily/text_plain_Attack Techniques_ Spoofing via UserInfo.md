---
title: Attack Techniques: Spoofing via UserInfo
url: https://textslashplain.com/2023/03/22/attack-techniques-spoofing-via-userinfo/
source: text/plain
date: 2023-03-23
fetch_date: 2025-10-04T10:22:30.770096
---

# Attack Techniques: Spoofing via UserInfo

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: Spoofing via UserInfo

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-03-222024-04-16](https://textslashplain.com/2023/03/22/attack-techniques-spoofing-via-userinfo/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[authentication](https://textslashplain.com/tag/authentication/), [InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [passwords](https://textslashplain.com/tag/passwords/), [phishing](https://textslashplain.com/tag/phishing/), [SecurityBugsThatArent](https://textslashplain.com/tag/securitybugsthatarent/), [URIs](https://textslashplain.com/tag/uris/)

I received the following phishing lure by SMS a few days back:

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-43.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/03/image-43.png)

The syntax of URLs is complicated, and even tech-savvy users often [misinterpret them](https://www.usenix.org/conference/enigma2019/presentation/stark). In the case of the URL above, the actual site’s **hostname** is `brefjobgfodsebsidbg.com`, and the misleading `www.att.net:911` text is just a phony `username:password` pair making up the **UserInfo** component of the URL.

[![](https://textslashplain.com/wp-content/uploads/2024/04/image-14.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/04/image-14.png)

Because users aren’t accustomed to encountering urls with UserInfo, they often will assume that tapping this URL will load `att.net`, which it certainly does not.

The [Guidelines for Secure URL Display](https://textslashplain.com/2019/01/11/securely-displaying-urls/) call for hiding the UserInfo data from UI surfaces where the user is expected to make a security decision (for example, the browser’s address bar/omnibox), and you’ll notice if you load this URL, the omnibox doesn’t show the spoofy portion. However, by the time that the user taps, the phisher likely has already successfully primed the user into expecting that the link is legitimate.

### Test Links

Test Link: <https://guest:guest@jigsaw.w3.org/HTTP/Digest/>
Test Link: <https://guest:guest@jigsaw.w3.org/HTTP/Basic/>

If the page shows “Your browser made it!” without popping an authentication dialog, your browser automatically sent the credentials in response to the server’s HTTP/401.

Note that the UserInfo component of the URLs is visible in both [NetLogs](https://textslashplain.com/2020/01/17/capture-network-logs-from-edge-and-chrome/) and browser extension events.

### Browser Behavior

Nineteen years ago ([April 2004](https://web.archive.org/web/20041021044441/http%3A//support.microsoft.com/kb/834489)), **Internet Explorer 6** stopped supporting URLs containing userinfo, with the justification that this URI component wasn’t actually formally a part of the specification for HTTP/HTTPS URLs and it was primarily used for phishing. Last summer, RFC9110 [made it official](https://datatracker.ietf.org/doc/html/rfc9110#name-deprecation-of-userinfo-in-), suggesting:

```
Before making use of an "http" or "https" URI reference received from an untrusted source, a recipient SHOULD parse for userinfo and treat its presence as an error; it is likely being used to obscure the authority for the sake of phishing attacks.
```

The guidance goes on to note the risk of *legitimately* relying upon this URL syntax (it’s easy for the credentials to leak out due to bugs or careless handling).

In contrast to IE’s choice, Firefox went a different way, showing the user a modal prompt:

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-46.png?w=825)](https://textslashplain.com/wp-content/uploads/2023/03/image-46.png)

… which seems like a solid mitigation. However, the attacker can make the warning less scary by returning a HTTP/401 challenge, causing the text of the dialog to change to:

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-47.png?w=824)](https://textslashplain.com/wp-content/uploads/2023/03/image-47.png)

Chrome’s Security team reluctantly deems the acceptance of UserInfo as “[Working as Intended](https://chromium.googlesource.com/chromium/src/%2B/master/docs/security/faq.md#Is-Chrome_s-support-for-userinfo-in-HTTP-URLs-e_g_http_user_password_example_com_considered-a-vulnerability).” While allowed for top-level navigations, Chromium disallows UserInfo in many [niches](https://bugs.chromium.org/p/chromium/issues/detail?id=696446), including the [subresource fetches](https://source.chromium.org/chromium/chromium/src/%2B/main%3Athird_party/blink/renderer/core/loader/worker_fetch_context.cc;l=169;drc=182afeebbd982e27cfa6da80e3c0e0a35898b132) (which helps protects against a different class of attack). [The crbug issue](https://bugs.chromium.org/p/chromium/issues/detail?id=435547) tracking that restriction includes some interesting conversation from folks encountering scenarios broken by the prohibition.

While it’s tempting to just disallow UserInfo everywhere (and I’d argue that all vendors probably *should* get RFC9110-compliant ASAP),it’s difficult to know how many real-world sites would break. Some browser vendors are probably reluctant to “go first” because in doing so, they might lose any inconvenienced users to a competitor that still allows the syntax. Just today, one security expert [noted](https://mastodon.social/%40Ericlaw/110068556820374811):

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-45.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/03/image-45.png)

Ugh. Stay safe out there!

-Eric

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2023/03/22/attack-techniques-spoofing-via-userinfo/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2023/03/22/attack-techniques-spoofing-via-userinfo/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-03-222024-04-16](https://textslashplain.com/2023/03/22/attack-techniques-spoofing-via-userinfo/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[authentication](https://textslashplain.com/tag/authentication/), [InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [passwords](https://textslashplain.com/tag/passwords/), [phishing](https://textslashplain.com/tag/phishing/), [SecurityBugsThatArent](https://textslashplain.com/tag/securitybugsthatarent/), [URIs](https://textslashplain.com/tag/uris/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:](https://textslashplain.com/2023/03/20/going-electric-solar/)

[Next Post Next post:](https://textslashplain.com/2023/03/25/how-microsoft-edge-updates/)

### Leave a comment [Cancel reply](/2023/03/22/attack-techniques-spoofing-via-userinfo/#respond)

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

* 2,396,387 hits
...