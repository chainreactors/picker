---
title: Data exfiltration in Keepa Price Tracker
url: https://palant.info/2021/08/02/data-exfiltration-in-keepa-price-tracker/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-23
fetch_date: 2025-10-04T04:36:15.354957
---

# Data exfiltration in Keepa Price Tracker

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Data exfiltration in Keepa Price Tracker

2021-08-02
 [Privacy](/categories/privacy/)/[Keepa](/categories/keepa/)/[Add-Ons](/categories/add-ons/)
 10 mins
 [9 comments](/2021/08/02/data-exfiltration-in-keepa-price-tracker/#comments)

As readers of this blog [might remember](/2020/10/28/what-would-you-risk-for-free-honey/), shopping assistants arenât exactly known for their respect of your privacy. They will typically use their privileged access to your browser in order to extract data. For them, this ability is a competitive advantage. You pay for a free product with a privacy hazard.

Usually, the vendor will claim to anonymize all data, a claim that can rarely be verified. Even if the anonymization actually happens, itâs [really hard to do this right](/2020/02/18/insights-from-avast/jumpshot-data-pitfalls-of-data-anonymization/). If anonymization can be reversed and the data falls into the wrong hands, this [can have severe consequences for a personâs life](https://www.washingtonpost.com/religion/2021/07/20/bishop-misconduct-resign-burrill/).

![Meat grinder with the Keepa logo on its side is working on the Amazon logo, producing lots of prices and stars](/2021/08/02/data-exfiltration-in-keepa-price-tracker/keepa.png)

*Image credits:
[Keepa](https://keepa.com/),
[palomaironique](https://openclipart.org/detail/29021/meat-mincing-machine),
[Nikon1803](https://de.wikipedia.org/wiki/Datei%3AAmazon_logo.svg)*

Today we will take a closer look at a browser extension called âKeepa â Amazon Price Trackerâ which is used by at least two million users across different browsers. The extension is being brought out by a German company and the privacy policy is refreshingly short and concise, suggesting that no unexpected data collection is going on. The reality however is: not only will this extension extract data from your Amazon sessions, it will even use your bandwidth to load various Amazon pages in the background.

#### Contents

* [The server communication](#the-server-communication)
* [What does Keepa learn about your browsing?](#what-does-keepa-learn-about-your-browsing)
* [Extension getting active on its own](#extension-getting-active-on-its-own)
* [The serverâs effective privileges](#the-server-s-effective-privileges)
* [Privacy policy](#privacy-policy)
* [Conclusions](#conclusions)

## The server communication

The Keepa extension keeps a persistent [WebSocket connection](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) open to its server `dyn.keepa.com`. The server parameters include your unique user identifier, stored both in the extension and as a cookie on keepa.com. As a result, this identifier will survive both clearing browse data and reinstalling the extension, youâd have to do both for it to be cleared. If you choose to register on keepa.com, this identifier will also be tied to your user name and email address.

Looking at the messages being exchanged, youâll see that these are binary data. But they arenât encrypted, itâs merely [deflate-compressed](https://en.wikipedia.org/wiki/Deflate) JSON-data.

![Developer tools showing binary messages being exchanged](/2021/08/02/data-exfiltration-in-keepa-price-tracker/websocket.png)

You can see the original message contents by copying the message as a Base64 string, then running the following code in the context of the extensionâs background page:

```
pako.inflate(atob("eAGrViouSSwpLVayMjSw0FFQylOyMjesBQBQGwZU"), {to: "string"});
```

This will display the initial message sent by the server:

```
{
  "status": 108,
  "n": 71
}
```

## What does Keepa learn about your browsing?

Whenever I open an Amazon product page, a message like the following is sent to the Keepa server:

```
{
  "payload": [null],
  "scrapedData": {
    "tld": "de"
  },
  "ratings": [{
    "rating": "4,3",
    "ratingCount": "2.924",
    "asin": "B0719M4YZB"
  }],
  "key": "f1",
  "domainId": 3
}
```

This tells the server that I am using Amazon Germany (the value 3 in `domainId` stands for `.de`, 1 would have been `.com`). It also indicates the product I viewed (`asin` field) and how it was rated by Amazon users. Depending on the product, additional data like the sales rank might be present here. Also, the page scraping rules are determined by the server and can change any time to collect more sensitive data.

A similar message is sent when an Amazon search is performed. The only difference here is that `ratings` array contains multiple entries, one for each article in your search results. While the search string itself isnât being transmitted (not with the current scraping rules at least), from the search results itâs trivial to deduce what you searched for.

## Extension getting active on its own

Thatâs not the end of it however. The extension will also regularly receive instructions like the following from the server (shortened for clarity):

```
{
  "key": "o1",
  "url": "https://www.amazon.de/gp/aod/ajax/ref=aod_page_2?asin=B074DDJFTH&â¦",
  "isAjax": true,
  "httpMethod": 0,
  "domainId": 3,
  "timeout": 8000,
  "scrapeFilters": [{
    "sellerName": {
      "name": "sellerName",
      "selector": "#aod-offer-soldBy div.a-col-right > a:first-child",
      "altSelector": "#aod-offer-soldBy .a-col-right span:first-child",
      "attribute": "text",
      "reGroup": 0,
      "multiple": false,
      "optional": true,
      "isListSelector": false,
      "parentList": "offers",
      "keepBR": false
    },
    "rating": {
      "name": "rating",
      "selector": "#aod-offer-seller-rating",
      "attribute": "text",
      "regExp": "(\\d{1,3})\\s?%",
      "reGroup": 1,
      "multiple": false,
      "optional": true,
      "isListSelector": false,
      "parentList": "offers",
      "keepBR": false
    },
    â¦
  }],
  "l": [{
    "path": ["chrome", "webRequest", "onBeforeSendHeaders", "addListener"],
    "index": 1,
    "a": {
      "urls": ["<all_urls>"],
      "types": ["main_frame", "sub_frame", "stylesheet", "script", â¦]
    },
    "b": ["requestHeaders", "blocking", "extraHeaders"]
  }, â¦, null],
  "block": "(https?:)?\\/\\/.*?(\\.gif|\\.jpg|\\.png|\\.woff2?|\\.css|adsystem\\.)\\??"
}
```

The address `https://www.amazon.de/gp/aod/ajax/ref=aod_page_2?asin=B074DDJFTH` belongs to an air compressor, not a product Iâve ever looked at but one that Keepa is apparently interested in. The extension will now attempt to extract data from this page despite me not navigating to it. Because of `isAjax` flag being set here, this address is loaded via [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest), after which the response text is being put into a frame of extensionsâs background page. If `isAjax` flag werenât set, this page would be loaded directly into another frame.

The `scrapeFilters` key sets the rules to be used for analyzing the page. This will extract ratings, prices, availability and any other information via CSS selectors and regular expressions. Here Keepa is also interested in the sellerâs name, elsewhere in the shipping information and security tokens. There is also functionality here to read out contents of the Amazon cart, I didnât look too closely at that however.

The `l` key is also interesting. It tells the extensionâs background page to call a particular method with the given parameters, here [chrome.webRequest.onBeforeSendHeaders.addListener](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeSendHeaders) method is being called. The `index` key determines which of the predefined listeners should be used. The purpose of the predefined listeners seems to be removing some security headers as well as making sure headers like `Cookie` are set correctly.

## The serverâs effective privileges

Letâs take a closer look at the privileges gr...