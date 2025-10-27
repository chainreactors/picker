---
title: The FBI Identified a Tor User
url: https://www.schneier.com/blog/archives/2023/01/the-fbi-identified-a-tor-user.html
source: Schneier on Security
date: 2023-01-18
fetch_date: 2025-10-04T04:11:34.180160
---

# The FBI Identified a Tor User

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

## The FBI Identified a Tor User

[No details](https://www.vice.com/en/article/z34dx3/fbi-wont-say-hacked-dark-web-isis-site-nit), though:

> According to the complaint against him, Al-Azhari allegedly visited a dark web site that hosts “unofficial propaganda and photographs related to ISIS” multiple times on May 14, 2019. In virtue of being a dark web site—­that is, one hosted on the Tor anonymity network—­it should have been difficult for the site owner’s or a third party to determine the real IP address of any of the site’s visitors.
>
> Yet, that’s exactly what the FBI did. It found Al-Azhari allegedly visited the site from an IP address associated with Al-Azhari’s grandmother’s house in Riverside, California. The FBI also found what specific pages Al-Azhari visited, including a section on donating Bitcoin; another focused on military operations conducted by ISIS fighters in Iraq, Syria, and Nigeria; and another page that provided links to material from ISIS’s media arm. Without the FBI deploying some form of surveillance technique, or Al-Azhari using another method to visit the site which exposed their IP address, this should not have been possible.

There are lots of ways to de-anonymize Tor users. Someone at the NSA gave a [presentation](https://www.theguardian.com/world/interactive/2013/oct/04/tor-stinks-nsa-presentation-document) on this ten years ago. (I [wrote about it](https://www.theguardian.com/world/2013/oct/04/tor-attacks-nsa-users-online-anonymity) for the *Guardian* in 2013, an essay that reads so dated in light of what we’ve learned since then.) It’s unlikely that the FBI uses the same sorts of broad surveillance techniques that the NSA does, but it’s certainly possible that the NSA did the surveillance and passed the information to the FBI.

Tags: [dark web](https://www.schneier.com/tag/dark-web/), [de-anonymization](https://www.schneier.com/tag/de-anonymization/), [FBI](https://www.schneier.com/tag/fbi/), [hacking](https://www.schneier.com/tag/hacking/), [NSA](https://www.schneier.com/tag/nsa/), [privacy](https://www.schneier.com/tag/privacy/), [surveillance](https://www.schneier.com/tag/surveillance/), [Tor](https://www.schneier.com/tag/tor/)

[Posted on January 17, 2023 at 7:02 AM](https://www.schneier.com/blog/archives/2023/01/the-fbi-identified-a-tor-user.html) •
[29 Comments](https://www.schneier.com/blog/archives/2023/01/the-fbi-identified-a-tor-user.html#comments)

### Comments

thorvold •
[January 17, 2023 8:27 AM](https://www.schneier.com/blog/archives/2023/01/the-fbi-identified-a-tor-user.html/#comment-415732)

The filing mentions that it is referencing a purported Top Secret document “Exhibit 2” from the timeframe of 2013. Based on that info, I am assuming this is a document purportedly from the Edward Snowden leak. The current policy of the government is that a classified document that is leaked is still classified until officially de-classified at a later date. Public access != Unclassified. The government is not going to acknowledge that the document is indeed classified in an open context because that would then confirm that the information contained in the document is likely true. Potentially the “fact of” information that the lawyer obtained in that document and then references in his motion may also be classified.

This would make the motion a derivatively classified document based on the inclusion of classified information in it. If the government managed to convince the judge that the information was still classified, then that would show the need required to seal the motion, without actually stating in open writing that the document was indeed true.

Will •
[January 17, 2023 9:29 AM](https://www.schneier.com/blog/archives/2023/01/the-fbi-identified-a-tor-user.html/#comment-415741)

The gist of the article is that the US government could have compromised the website, or the website may have been a honeypot, or they may have ways of unmasking TOR traffic generally.

But isn’t it more likely that they compromised the machine he used to access the dark web instead?

Winter •
[January 17, 2023 9:44 AM](https://www.schneier.com/blog/archives/2023/01/the-fbi-identified-a-tor-user.html/#comment-415742)

A known way to re-identify an IP address over Tor is when the user enables javascript support. If you do so, it is advised to use the browser in a VM with the IP address shielded. This is especially true when the user does not use the Tor browser, but accesses Tor using SOCKS5 on a regular browser.

If the FBI already had access to the dark web site, it could install Javascript code to get at the IP address.

Another, fairly unlikely way, is to look for searches on public fora in the open for certain websites just before the access.

A real killer would be asking for translating the offending page in open Google Translate just after you accessed it via Tor. Google can be fickle when used over Tor, it generally blocks access from Tor.

Clive Robinson •
[January 17, 2023 10:46 AM](https://www.schneier.com/blog/archives/2023/01/the-fbi-identified-a-tor-user.html/#comment-415743)

@ Bruce, ALL,

Re : The cost of catching a tiddler.

> “There are lots of ways to de-anonymize Tor users.”

Yes there are[1] but non of them are “resource inexpensive”, thus as with angling,

“You only throw the bait where you’ve a good idea there is a fish that will bite.”

Thus I’d be more interested in what the suspect allegedly did to first attract attention to themselves.

After that we know it’s more likely to be “Methods” rather than “sources”.

It’s knowing if the first flagging up event was just technical or involved human agency. If the latter wether it was an error by the suspect or somebody else “provided confidential information”.

1, If technical, We all have a problem.

The last does not overly concern me on the “If you can’t do the time…” principle I avoid doing that sort of “crime” thing.

The second I suspect is actuall quite probable on the “Johnny can’t encrypt” principle. This unfortunately is a major failing of most encryption systems going all the way to BC times.

If it’s the first then I’m very concerned because that has the implication that there is a fault in the standards, protocols or algorithms, which is likely to effect a great number of other systems not just Tor.

Hopefully we get to find out, and find out fairly soon.

[1] When you think about it at a fundemental level there are two issues,

1.1, All traffic is point to point.
1.2, All traffic is bidirectional.

Together these guarenty that all such connections are tracable, with enough resources to gather the needed information.

Due to Tors fixation with “low latency” this makes “tracking in the time domain” relatively painless and no amount of encryption no matter how clever can hide the time domain information. Nor can encryption hide the data flow domain information, all it can hide and often not w...