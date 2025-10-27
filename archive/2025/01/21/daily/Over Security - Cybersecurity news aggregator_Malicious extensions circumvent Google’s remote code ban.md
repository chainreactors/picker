---
title: Malicious extensions circumvent Google’s remote code ban
url: https://palant.info/2025/01/20/malicious-extensions-circumvent-googles-remote-code-ban/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-21
fetch_date: 2025-10-06T20:12:28.078701
---

# Malicious extensions circumvent Google’s remote code ban

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Malicious extensions circumvent Googleâs remote code ban

2025-01-20
 [Add-Ons](/categories/add-ons/)/[Security](/categories/security/)/[Google](/categories/google/)
 23 mins
 [11 comments](/2025/01/20/malicious-extensions-circumvent-googles-remote-code-ban/#comments)

As [noted last week](/2025/01/13/chrome-web-store-is-a-mess/#how-did-google-get-into-this-mess) I consider it highly problematic that Google for a long time allowed extensions to run code they downloaded from some web server, an approach that Mozilla prohibited long before Google even introduced extensions to their browser. For years this has been an easy way for malicious extensions to hide their functionality. When Google finally [changed their mind](https://developer.chrome.com/docs/extensions/develop/migrate/remote-hosted-code), it wasnât in form of a policy but rather a technical change introduced with Manifest V3.

As with most things about Manifest V3, these changes are meant for well-behaving extensions where they in fact improve security. As readers of this blog probably know, those who want to find loopholes will find them: Iâve already written about the Honey extension [bundling its own JavaScript interpreter](/2020/10/28/what-would-you-risk-for-free-honey/#the-highly-flexible-promo-code-applying-process) and malicious extensions essentially [creating their own programming language](/2023/06/02/how-malicious-extensions-hide-running-arbitrary-code/). This article looks into more approaches I found used by malicious extensions in Chrome Web Store. And maybe Google will decide to prohibit remote code as a policy after all.

![Screenshot of a Google webpage titled âDeal with remote hosted code violations.â The page text visible in the screenshot says: Remotely hosted code, or RHC, is what the Chrome Web Store calls anything that is executed by the browser that is loaded from someplace other than the extension's own files. Things like JavaScript and WASM. It does not include data or things like JSON or CSS.](/2025/01/20/malicious-extensions-circumvent-googles-remote-code-ban/remote_code.png)

**Update** (2025-01-20): Added two extensions to the bonus section. Also indicated in the tables which extensions are currently featured in Chrome Web Store.

**Update** (2025-01-21): Got a sample of the malicious configurations for Phoenix Invicta extensions. Added [a section describing it](#the-payload) and removed âBut what do these configurations actually doâ section. Also added a bunch more domains to the [IOCs section](#iocs).

**Update** (2025-01-28): Corrected the âNetflix Partyâ section, Flipshope extension isnât malicious after all. Also removed the attribution subsection here.

#### Contents

* [Summary of the findings](#summary-of-the-findings)
* [Phoenix Invicta](#phoenix-invicta)
  + [Injecting HTML code into web pages](#injecting-html-code-into-web-pages)
  + [Abusing declarativeNetRequest API](#abusing-declarativenetrequest-api)
  + [Opening new tabs](#opening-new-tabs)
  + [The scheme summarized](#the-scheme-summarized)
  + [The payload](#the-payload)
  + [Who is behind these extensions?](#who-is-behind-these-extensions)
  + [The affected extensions](#the-affected-extensions)
* [Netflix Party](#netflix-party)
  + [Spying on the users](#spying-on-the-users)
  + [The bogus rule processing](#the-bogus-rule-processing)
  + [The affected extensions](#the-affected-extensions-1)
* [Sweet VPN](#sweet-vpn)
  + [Anti-debugging protection](#anti-debugging-protection)
  + [Guessing further functionality](#guessing-further-functionality)
  + [The affected extensions](#the-affected-extensions-2)
* [Bonus section: more malicious extensions](#bonus-section-more-malicious-extensions)
  + [The affected extensions](#the-affected-extensions-3)
* [IOCs](#iocs)

## Summary of the findings

This article originally started as an investigation into Phoenix Invicta Inc. Consequently, this is the best researched part of it. While I could attribute only 14 extensions with rather meager user numbers to Phoenix Invicta, thatâs likely because theyâve only started recently. I could find a large number of domain names, most of which arenât currently being used by any extensions. A few are associated with extensions that have been removed from Chrome Web Store but most seem to be reserved for future use.

It can be assumed that these extensions are meant to inject ads into web pages, yet Phoenix Invicta clearly put some thought into plausible deniability. They can always claim their execution of remote code to be a bug in their otherwise perfectly legitimate extension functionality. So it will be interesting to see how Google will deal with these extensions, lacking (to my knowledge) any policies that apply here.

The malicious intent is a bit more obvious with Netflix Party and related extensions. This shouldnât really come as a surprise to Google: the most popular extension of the group was a topic on this blog back in 2023, and a year before that McAfee already flagged two extensions of the group as malicious. Yet here we are, and these extensions are still capable of spying, [affiliate fraud](https://www.investopedia.com/terms/a/affiliate-fraud.asp) and [cookie stuffing](https://en.wikipedia.org/wiki/Cookie_stuffing) as described by McAfee. If anything, their potential to do damage has only increased.

Finally, the group of extensions around Sweet VPN is the most obviously malicious one. To be fair, what these extensions do is probably best described as obfuscation rather than remote code execution. Still, they download extensive instructions from their web servers even though these arenât too flexible in what they can do without requiring changes to the extension code. Again there is spying on the users and likely affiliate fraud as well.

In the following sections I will be discussing each group separately, listing the extensions in question at the end of each section. There is also a complete list of websites involved in downloading instructions [at the end of the article](#iocs).

## Phoenix Invicta

Letâs first take a look at an extension called âVolume Booster - Super Sound Booster.â It is one of several similar extensions and it is worth noting that the extensionâs code is neither obfuscated nor minified. It isnât hiding any of its functionality, relying on plausible deniability instead.

For example, in its manifest this extension requests access to all websites:

```
"host_permissions": [
  "http://*/*",
  "https://*/*"
],
```

Well, it *obviously* needs that access because it might have to boost volume on any website. Of course, it would be possible to write this extension in a way that the `activeTab` permission would suffice. But it isnât built in this way.

Similarly, one could easily write a volume booster extension that doesnât need to download a configuration file from some web server. In fact, this extension works just fine with its default configuration. But it will still download its configuration roughly every six hours just in case (code slightly simplified for readability):

```
let res = await fetch(`https://super-sound-booster.info/shortcuts?uuid=${userId}`,{
    method: 'POST',
    body: JSON.stringify({installParams}),
    headers: { 'Content-Type': 'text/plain' }
});
let data = await res.json();
if (data.shortcuts) {
    chrome.storage.local.set({
        shortcuts: {
            list: data.shortcuts,
            updatedAt: Date.now(),
        }
    });
}
if (data.volumeHeaders) {
    chrome.storage.local.set({
        volumeHeaderRules: data.volumeHeaders
    });
}
if (data.newsPage) {
    this.openNewsPage(data.newsPage.pageId, data.newsPage.options);
}
```

This will send a unique user ID to a server which might then respond with a JSON file. Conveniently, the three possible values in this configur...