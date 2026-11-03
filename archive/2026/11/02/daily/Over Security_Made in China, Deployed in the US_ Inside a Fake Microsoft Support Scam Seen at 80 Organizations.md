---
title: Made in China, Deployed in the US: Inside a Fake Microsoft Support Scam Seen at 80 Organizations
url: https://pixmsecurity.com/blog/blog/made-in-china-deployed-in-us-fake-microsoft-support-scam/
source: Over Security
date: 2026-11-02
fetch_date: 2026-11-03T08:51:19.186576
---

# Made in China, Deployed in the US: Inside a Fake Microsoft Support Scam Seen at 80 Organizations

[![Pixm Security Logo](https://pixmsecurity.com/wp-content/themes/Divi-Child/images/pixm-logo-header-white.png)](https://pixmsecurity.com)

* [About](https://pixmsecurity.com/about/)
* [About Us](https://pixmsecurity.com/about-us/)
* [Partners](https://pixmsecurity.com/partners/)
* Resources
  + [Blog](https://pixmsecurity.com/blog/)
  + [News](/news)
  + [Case Studies](https://pixmsecurity.com/case-studies/)
* [Login](https://app.pixm.net)
* [Book a Demo](https://pixmsecurity.com/request-demo/)
* [Free Install](https://chrome.google.com/webstore/detail/pixm-phishing-protection/flomofhkchlalfciiibgbfcpolhmglai?hl=en)
* [Free Install](https://apps.apple.com/app/pixm-phishing-protection/id1622871362)
* [Free Install](https://addons.mozilla.org/en-US/firefox/addon/pixm-web/)

Have a question for us?

Contact support at support@pixm.net

[Book a Demo](/request-free-trial/)

Open Menu

## Request Your Demo

"\*" indicates required fields

### Contact Information

First Name\*

Last Name\*

Company\*

Email\*

Work Phone

CAPTCHA

Request Demo

# Made in China, Deployed in the US: Inside a Fake Microsoft Support Scam Seen at 80 Organizations

Threat Investigation · Threat Research

# Made in China, Deployed in the US: Inside a Fake Microsoft Support Scam Seen at 80 Organizations

A large-scale fake Microsoft support scam, hosted on Azure, shielded by Cloudflare, and delivered through ads on US publishers, traces back to Chinese developers and a domain registered in Hubei, China.

**PIXM Threat Research**Published Nov 2, 20267 min read

### Summary

* Between March and October 2026, PIXM tracked a fake Microsoft support kit hosted on Microsoft’s own Azure cloud that reached users at **80 organizations**. New landing pages were still appearing daily as of November 2.
* The back end behind it, which was hidden behind Cloudflare, strongly suggests an organized operation that includes Mandarin-speaking developers and ad buyers, with ties back to Hubei, China.

[Indicators ↓](#ioc)

## Where we left off

In [Anatomy of a Phish: How Tech-Support Scams Buy Their Way Onto Your Screen](https://pixmsecurity.com/blog/blog/anatomy-of-a-phish-malvertising-tech-support-scams/), we traced how fake Microsoft support pages reach victims through paid ads. Those pages run on throwaway Azure Static Websites on Microsoft’s own cloud. The back end we trace here hides behind Cloudflare. This post follows the code of the pages themselves back to the infrastructure and operators behind them.

We start with the script that fetches each page’s phone number, then lay out the Chinese-language evidence behind the back end and what its code reveals about a team of ad buyers. From there we look at where the ads ran and what defenders can do.

## 1. The page that phones home

A victim clicks an ad on a legitimate website and lands on a randomly named Azure Static Website (`*.z13.web.core.windows[.]net`). The site fills the screen with fake “System Error” and “Windows Firewall” pop-ups and a fake Microsoft Support chat. Every element points to one toll-free number.

Below we examine the code used to generate the phone number on the page.

```
window.adsManagers = ["eooo","sooo","mooo","xiaofeng"];
window.currentAdsManager = "xiaofeng";
window.phoneNumber = "(888)XXX-XXXX"; // fallback number (redacted)

//跟踪展示 ("track impression")
function trackingImpression(phone){
 img.src = "https://adhelper[.]one/impression/ce895b1f-…?siteid=JS723-" + phone
 + "-" + campaign + "&domain=" + domain + "&exchange=" + exchange;
}

// JSONP 回调 ("JSONP callback")
function handlePhone(data){ if (data && data.phone) window.phoneNumber = data.phone; … }

// JSONP 请求 ("JSONP request")
script.src = 'https://call.adhelper[.]cc/api/get-phone.php?callback=handlePhone'
 + '&ads_manager=' + currentAdsManager;
script.onerror = function(){ console.log('获取号码失败，使用默认号码'); … };
 // "failed to get number, using default number"
```

**Figure 1.** The phone loader from a page captured on July 23, 2026 (abridged; phone number redacted). Comments are in the original Simplified Chinese.

The design shows several things:

* **Numbers are assigned centrally.** The operator can swap numbers across every live page at once without touching the pages, which keeps a number working even after it has been reported.
* **Every impression is tracked.** The pixel records which phone number was shown, which campaign, which publisher site the ad ran on, and which ad exchange sold the placement. That is the same data a legitimate pay-per-call marketer uses to work out which ads produce calls.
* **Calls are attributed to people.** The `ads_manager` value tells the back end whose page this is, so it returns that person’s number.

## 2. Clues pointing to China

Below we lay out evidence suggesting Mandarin-speaking developers and ties to mainland China.

**The developers’ comments.** The loader’s comments and error messages are in Simplified Chinese: 跟踪展示 (“track impression”), 加载 React 主程序 (“load the main React app”), 默认号码（兜底） (“default number (fallback)”).

**The registration.** `adhelper[.]one` was registered on March 10, 2026, through Gname, with a registrant address in Hubei province, China. The first adhelper-tracked page we captured followed two weeks later. Registration details are self-reported, so on its own this isn’t conclusive.

**The mistake victims could see.** On a separate family of pages, the kit draws a fake browser bar telling the victim the page is in full-screen mode. It makes a frozen browser look official. The developers copied that notice from their own browser, which was set to Chinese, so English-speaking victims were shown this:

 ![Fake Microsoft support page with a Chinese-language full-screen notice at the top](https://pixmsecurity.com/wp-content/uploads/2026/10/01-fake-fullscreen-chinese-banner-redacted.jpg)

**Figure 2.** A page captured on April 3, 2026. The bar at top center reads “…web.core.windows[.]net – 若要退出全屏模式，请按 esc”, Chrome’s “To exit full screen, press Esc” in Chinese. Phone numbers redacted by PIXM.

 ![Close-up of the Chinese full-screen notice](https://pixmsecurity.com/wp-content/uploads/2026/10/02-banner-closeup.jpg)

**Figure 3.** Close-up of the full-screen notice.

**The server panel.** The root of `call.adhelper[.]cc` shows 恭喜，站点创建成功！ (“Congratulations, the site was created successfully!”). That is the default page of BaoTa (宝塔), a server control panel popular in China. BaoTa has an English international edition, aaPanel, and the operator installed the Chinese one.

A fifth, softer signal: one of the ads managers in the loader is named `xiaofeng`, a common Chinese given name written in pinyin.

## 3. A team, not a lone scammer

The ads-manager list changes over time. In May the loader names three managers (`eooo`, `sooo`, `mooo`). In July a fourth, `xiaofeng`, is added. Across the pages we captured, users at 11 organizations saw pages from this back end, and three different managers are active. Each page is built for one manager, and the back end returns that manager’s number. The same fake page is also used by other operations. Of the 80 organizations where we saw it, the adhelper back end accounts for 11.

The phone numbers point the same way. For the numbers on these pages that we could look up in public toll-free registry data, most were controlled by the same toll-free provider, Fractel, in the month they appeared. Many were bought in sequential blocks. We have no indication that the provider is aware of the abuse. Customers of toll-free providers are often resellers.

Taken together, it looks like an organized operation. Developers maintain the back end, several ad buyers run campaigns, phone numbers come mostly from one provider, and each buyer gets their own number, so every call can be credited to the buyer who generated it. That is consistent with the pay-per-call model documented in US prosecutions of tech-support fraud, where pop-up publishers were paid for the calls they delivered to c...