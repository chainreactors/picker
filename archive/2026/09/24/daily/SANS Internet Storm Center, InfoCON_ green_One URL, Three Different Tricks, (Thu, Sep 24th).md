---
title: One URL, Three Different Tricks, (Thu, Sep 24th)
url: https://isc.sans.edu/diary/rss/33366
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-24
fetch_date: 2026-09-25T06:53:29.052087
---

# One URL, Three Different Tricks, (Thu, Sep 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/33360)
* [next](/diary/33368)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [One URL, Three Different Tricks](/forums/diary/One%2BURL%2BThree%2BDifferent%2BTricks/33366/)

**Published**: 2026-09-24. **Last Updated**: 2026-09-24 06:25:06 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/One%2BURL%2BThree%2BDifferent%2BTricks/33366/#comments)

Yesterday, we received a phishing email with an interesting link. At first sight, it looks like garbage, but every piece of it has been carefully crafted to confuse basic security controls. Here is the defanged link:

```

hxxps://YKZjqa7A@gynd--[.]koncar-hr[.]com/[email protected]
```

Let's break it down...

The first trick is the old "userinfo" field. According to RFC 3986[[1](https://www.rfc-editor.org/info/rfc3986/)], everything between the scheme and an "@" inside the authority is treated as credentials ("user:password@host"). Browsers silently ignore it, but it has two advantages for the attacker. The random string ("YKZjqa7A") makes every URL unique, which defeats exact-match blocklists and URL reputation lookups. It probably also acts as a tracking token per victim or campaign. As a side effect, the whole thing now looks like an email address to any tool that doesn't parse URLs strictly.

The second trick is the hostname itself: "gynd--.koncar-hr.com". Per the classic hostname rules (RFC 952/1123[[2](https://www.rfc-editor.org/info/rfc952/)]), a label can't start or end with a hyphen. DNS doesn't care, and browsers happily resolve and visit it. However, strict validators, regex-based URL extractors, and some link-rewriting or sandboxing solutions may consider it invalid and simply skip it. A URL that is never extracted is never scanned. The random subdomain also suggests wildcard DNS, so each victim gets a brand-new hostname that no blocklist knows. The parent domain is a lookalike of the legitimate "koncar.hr" (a Croatian industrial group), with the ccTLD turned into a hyphenated ".com".

The last trick is the victim's email address, appended in the path. This is common with phishing kits: the page reads the path, pre-fills the login form with the victim's address, and sometimes adapts the branding to the email domain. There is another benefit, though. A poorly written parser that splits the string on the *last* "@" will conclude that the host is "isc.sans.edu", the recipient's own trusted domain! Per the WHATWG[[3](https://url.spec.whatwg.org)] URL standard, the authority ends at the first "/", so the browser correctly connects to the attacker's server.

The result is a single string that tells three different stories. A naive filter sees two email addresses or a link to your own domain. A strict validator sees an invalid hostname and drops it. The browser sees a perfectly valid URL and takes the victim straight to the phishing page. Attackers aren't exploiting a vulnerability here but the differences between parsers.

Tip: If you want to hunt for this kind of link, look for URLs with more than one "@", hostname labels starting or ending with a hyphen, and paths containing the recipient's own email address.

[1] <https://www.rfc-editor.org/info/rfc3986/>
[2] <https://www.rfc-editor.org/info/rfc952/>
[3] <https://url.spec.whatwg.org>

Xavier Mertens (@xme)
Senior ISC Handler | SANS Principal Instructor | Freelance Consultant
[Xameco](https://xameco.be) | [PGP Key](https://xameco.be/pgpkey.txt)

Keywords: [Phishing](/tag.html?tag=Phishing) [URL](/tag.html?tag=URL)

[0 comment(s)](/diary/One%2BURL%2BThree%2BDifferent%2BTricks/33366/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33360)
* [next](/diary/33368)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)