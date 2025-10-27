---
title: “FakeGPT”: New Variant of Fake-ChatGPT Chrome Extension Stealing Facebook Ad Accounts with…
url: https://medium.com/@guardiosecurity/fakegpt-new-variant-of-fake-chatgpt-chrome-extension-stealing-facebook-ad-accounts-with-4c9996a8f282?source=rss-6a038e71ff0f------2
source: Over Security - Cybersecurity news aggregator
date: 2023-03-09
fetch_date: 2025-10-04T09:02:23.588934
---

# “FakeGPT”: New Variant of Fake-ChatGPT Chrome Extension Stealing Facebook Ad Accounts with…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4c9996a8f282&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40guardiosecurity%2Ffakegpt-new-variant-of-fake-chatgpt-chrome-extension-stealing-facebook-ad-accounts-with-4c9996a8f282&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40guardiosecurity%2Ffakegpt-new-variant-of-fake-chatgpt-chrome-extension-stealing-facebook-ad-accounts-with-4c9996a8f282&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# “F**akeGPT”: New Variant of Fake-ChatGPT Chrome Extension Stealing Facebook Ad Accounts with Thousands of Daily Installs**

[![Guardio](https://miro.medium.com/v2/resize:fill:64:64/1*s7SJaF9dODo7rWqa2rFQ6Q.png)](/%40guardiosecurity?source=post_page---byline--4c9996a8f282---------------------------------------)

[Guardio](/%40guardiosecurity?source=post_page---byline--4c9996a8f282---------------------------------------)

9 min read

·

Mar 8, 2023

--

4

Listen

Share

By [**Nati Tal**](https://www.linkedin.com/in/natital/)([Guardio Labs](http://www.guard.io/))

> A Chrome Extension propelling quick access to fake ChatGPT functionality was found to be hijacking Facebook accounts and installing hidden account backdoors. Particularly noticeable is the use of a malevolent silently forced Facebook app “backdoor” giving the threat actors super-admin permissions.
>
> By hijacking high-profile Facebook business accounts, the threat actor creates an elite army of Facebook bots and a malicious paid media apparatus. This allows it to push Facebook paid ads at the expense of its victims in a self-propagating worm-like manner.
>
> In this write-up, we will uncover the techniques used by this powerful stealer that started propagating on Facebook and the official Google Chrome Store early this month with thousands of new installations per day — and yet to be detected by either Facebook or Google.

**Update: March 22, 2023** — [Guardio](http://www.guard.io) Labs discovered another variant in this FakeGPT campaign, abusing open-source code and yet again hijacking Facebook profiles — [read about it here](https://labs.guard.io/fakegpt-2-open-source-turned-malicious-in-another-variant-of-the-facebook-account-stealer-d00ef9883d61).

**Update: March 9, 2023** — Following [Guardio’](http://www.guard.io)s report regarding this malicious extension to Google, the extension is now removed from Chrome’s store.

## The Vicious Circle of Hijacked Facebook Malvertising

Our security research team at [Guardio](https://www.guard.io) is constantly monitoring the activity surrounding ChatGPT’s brand abuse, with endless campaigns propagating malware and phishing for your credit cards. On 3/3/2023, our team detected a new variant of a malicious fake ChatGPT browser extension, part of a campaign started in early February with several other ChatGPT branded malicious extensions. This time upgraded with a threatening technique to take over your Facebooks accounts as well as a sophisticated worm-like approach for propagation.

Press enter or click to view image in full size

![]()

Malicious Sponsored Posts on Facebook leading to the Malicious “FakeGPT” extension

The malicious stealer-extension, titled “**Quick access to Chat GPT**” is promoted on [Facebook-sponsored posts](https://www.facebook.com/chatgpt.google/videos/719341863011965/) as a quick way to get started with ChatGPT directly from your browser. Although the extension gives you that (by simply connecting to the official ChatGPT’s API) it also harvests every information it can take from your browser, steals cookies of authorized active sessions to any service you have, and also employs tailored tactics to take over your Facebook account.

Press enter or click to view image in full size

![]()

From malvertising, extension installation, hijacking Facebook accounts, and back again to propagation

Once the Threat Actor takes ownership of your stolen data, it will probably sell it to the highest bidder as usual, yet while we dug deeper into this operation we’ve noticed their extra care on High-Profile Facebook business accounts. With this approach, the campaign can continue propagating with its very own army of hijacked Facebook bot accounts, publishing more sponsored posts and other social activities on behalf of its victim's profiles and spending business account money credits!

The above high-level campaign description hides inside it some sophisticated techniques to harvest victims' details and take over Facebook accounts. Those are abusing online services and powerful APIs from both Google and Facebook — giving those threat actors some very powerful tools for success.

## Abusing Victim Browser’s Context

Once the extension is installed, it gives you what’s advertised — a small popup window showing up after you click on the extension icon, with a prompt to ask ChatGPT whatever you want.

Yet, this is exactly where it starts to get fishy. The extension is now an integral part of your browser. Thus, it can send any request to any other service — as if the browser owner itself was initiating this from the same context. This is crucial — as the browser, in most cases, already has an active and authenticated session with almost all your day-to-day services, e.g. Facebook.

More specifically, this allows the extension to access [Meta’s Graph API for developers](https://developers.facebook.com/docs/graph-api/) — allowing the threat actor to quickly access all your details and also take actions on your behalf directly in your Facebook account using simple API calls.

Press enter or click to view image in full size

![]()

The “Quick Access” extension sends API calls from the authenticated browser context

There are of course limitations and security measures taken by Facebook— e.g., making sure the requests are originating from an authenticated user as well as from the relevant origin. The extension already has an authenticated session with Facebook, but what about the origin of the requests it sends? Well, thanks to Chrome’s `declarativeNetRequest` API, the extension has a simple way to circumvent Facebook’s protection.

The following piece of code is called on the malicious extension right on initiation, making sure all requests made to `facebook.com` by any source on your browser (including the extension itself) will have their headers modified to reflect the origin as “`facebook.com`” as well. This gives the extension the ability to freely browse any Facebook page (including making API calls and actions) using your infected browser and without any trace.

```
 yield chrome.declarativeNetRequest.updateDynamicRules({
      addRules: [{
              "id": 1,
              "priority": 1,
              "action": {
                  type: 'modifyHeaders',
                  requestHeaders: [
                      { header: 'origin', operation: 'set', value: `https://www.${d}` }
                  ],
              },
              "condition": { "urlFilter": `www.${d}`, "resourceTypes": ["xmlhttprequest"] }
          }
      ],
      removeRuleIds: [1]
  });java
```

Note that the variable `d` is holding the relevant domain (in our case...