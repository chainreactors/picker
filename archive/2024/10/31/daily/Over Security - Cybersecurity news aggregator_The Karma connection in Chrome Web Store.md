---
title: The Karma connection in Chrome Web Store
url: https://palant.info/2024/10/30/the-karma-connection-in-chrome-web-store/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-31
fetch_date: 2025-10-06T18:56:53.301331
---

# The Karma connection in Chrome Web Store

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# The Karma connection in Chrome Web Store

2024-10-30
 [Security](/categories/security/)/[Privacy](/categories/privacy/)/[Add-Ons](/categories/add-ons/)/[Google](/categories/google/)
 11 mins
 [13 comments](/2024/10/30/the-karma-connection-in-chrome-web-store/#comments)

Somebody [brought to my attention](https://gist.github.com/c0m4r/45e15fc1ec13c544393feafca30e74de) that the Hide YouTube Shorts extension for Chrome changed hands and turned malicious. I looked into it and could confirm that it contained two undisclosed components: one performing [affiliate fraud](https://www.investopedia.com/terms/a/affiliate-fraud.asp) and the other sending usersâ every move to some Amazon cloud server. But that wasnât all of it: I discovered eleven more extensions written by the same people. Some contained only the affiliate fraud component, some only the user tracking, some both. A few donât appear to be malicious yet.

While most of these extensions were supposedly developed or bought by a person without any other traces online, one broke this pattern. Karma shopping assistant has been on Chrome Web Store since 2020, the company behind it founded in 2013. This company employs more than 50 people and secured tons of cash in venture capital. Maybe a mistake on my part?

After looking thoroughly this explanation seems unlikely. Not only does Karma share some backend infrastructure and considerable amounts of code with the malicious extensions. Not only does Karma Shopping Ltd. admit to selling usersâ browsing profiles in their privacy policy. There is even more tying them together, including a mobile app developed by Karma Shopping Ltd. whereas the identical Chrome extension is supposedly developed by the mysterious evildoer.

![Screenshot of the karmanow.com website, with the Karma logo visible and a yellow button âAdd to Chrome - Itâs Freeâ](/2024/10/30/the-karma-connection-in-chrome-web-store/karma.png)

#### Contents

* [The affected extensions](#the-affected-extensions)
* [Hiding in plain sight](#hiding-in-plain-sight)
* [Affiliate fraud functionality](#affiliate-fraud-functionality)
* [Browsing profile collection](#browsing-profile-collection)
* [Who is behind this?](#who-is-behind-this)
* [What does Karma Shopping want with the data?](#what-does-karma-shopping-want-with-the-data)

## The affected extensions

Most of the extensions in question changed hands relatively recently, the first ones in the summer of 2023. The malicious code has been added immediately after the ownership transfer, with some extensions even requesting additional privileges citing bogus reasons. A few extensions have been developed this year by whoever is behind this.

Some extensions from the latter group donât have any obvious malicious functionality at this point. If there is tracking, it only covers the usage of the extensionâs user interface rather than the entire browsing behavior. This can change at any time of course.

| Name | Weekly active users | Extension ID | Malicious functionality |
| --- | --- | --- | --- |
| Hide YouTube Shorts | 100,000 | aljlkinhomaaahfdojalfmimeidofpih | Affiliate fraud, browsing profile collection |
| DarkPDF | 40,000 | cfemcmeknmapecneeeaajnbhhgfgkfhp | Affiliate fraud, browsing profile collection |
| Sudoku On The Rocks | 1,000 | dncejofenelddljaidedboiegklahijo | Affiliate fraud |
| Dynamics 365 Power Pane | 70,000 | eadknamngiibbmjdfokmppfooolhdidc | Affiliate fraud, browsing profile collection |
| Israel everywhere | 70 | eiccbajfmdnmkfhhknldadnheilniafp | â |
| Karma | Online shopping, but better | 500,000 | emalgedpdlghbkikiaeocoblajamonoh | Browsing profile collection |
| Where is Cookie? | 93 | emedckhdnioeieppmeojgegjfkhdlaeo | â |
| Visual Effects for Google Meet | 1,000,000 | hodiladlefdpcbemnbbcpclbmknkiaem | Affiliate fraud |
| Quick Stickies | 106 | ihdjofjnmhebaiaanaeeoebjcgaildmk | â |
| Nucleus: A Pomodoro Timer and Website Blocker | 20,000 | koebbleaefghpjjmghelhjboilcmfpad | Affiliate fraud, browsing profile collection |
| Hidden Airline Baggage Fees | 496 | kolnaamcekefalgibbpffeccknaiblpi | Affiliate fraud |
| M3U8 Downloader | 100,000 | pibnhedpldjakfpnfkabbnifhmokakfb | Affiliate fraud |

**Update** (2024-11-11): Hide YouTube Shorts, DarkPDF, Nucleus and Hidden Airline Baggage Fees have been taken down. Two of them have been marked as malware and one as violating Chrome Web Store policies, meaning that existing extension users will be notified. I cannot see the reason for different categorization, the functionality being identical in all of these extensions. The other extensions currently remain active.

**Update** (2024-12-12): By now Dynamics 365 Power Pane, Israel everywhere, Quick Stickies and M3U8 Downloader are gone as well, all removed on November 17 apparently. The first one also marked as malware, so that it will be disabled for existing users. Only three extensions remain active now, which includes the two most popular extensions on my list.

## Hiding in plain sight

Whoever wrote the malicious code chose not to obfuscate it but to make it blend in with the legitimate functionality of the extension. Clearly, the expectation was that nobody would look at the code too closely. So there is for example this:

```
if (window.location.href.startsWith("http") ||
    window.location.href.includes("m.youtube.com")) {
  â¦
}
```

It *looks* like the code inside the block would only run on YouTube. Only when you stop and consider the logic properly you realize that it runs on every website. In fact, thatâs the block wrapping the calls to malicious functions.

The malicious functionality is split between content script and background worker for the same reason, even though it could have been kept in one place. This way each part looks innocuous enough: there is some data collection in the content script, and then it sends a `check_shorts` message to the background worker. And the background worker âchecks shortsâ by querying some web server. Together this just *happens* to send your entire browsing history into the Amazon cloud.

Similarly, there are some complicated checks in the content script which eventually result in a `loadPdfTab` message to the background worker. The background worker dutifully opens a new tab for that address and, strangely, closes it after 9 seconds. Only when you sort through the layers it becomes obvious that this is actually about adding an affiliate cookie.

And of course there is a bunch of usual complicated conditions, making sure that this functionality is not triggered too soon after installation and generally doesnât pop up reliably enough that users could trace it back to this extension.

## Affiliate fraud functionality

The affiliate fraud functionality is tied to the `kra18.com` domain. When this functionality is active, the extension will regularly download data from `https://www.kra18.com/v1/selectors_list?&ex=90` (90 being the extension ID here, the server accepts eight different extension IDs). Thatâs a long list containing 6,553 host names:

![Screenshot of JSON data displayed in the browser. The selectors key is expanded, twenty domain names like drinkag1.com are visible in the list.](/2024/10/30/the-karma-connection-in-chrome-web-store/selectors.png)

**Update** (2024-11-19): As of now, the owners of this server disabled the endpoints mentioned here. You can still see the original responses [on archive.today](https://archive.is/www.kra18.com) however.

Whenever one of these domains is visited and the moons are aligned in the right order, another request to the server is made with the full address of the page you are on. For example, the extension could request `https://www.kra18.com/v1/extension_selectors?u=https://www.tink.de/&ex=90`:

![Screenshot of JSON data displayed in the browser. There are keys shortsNavBu...