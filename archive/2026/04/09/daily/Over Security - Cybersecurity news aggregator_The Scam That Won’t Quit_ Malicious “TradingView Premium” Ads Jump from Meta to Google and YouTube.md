---
title: The Scam That Won’t Quit: Malicious “TradingView Premium” Ads Jump from Meta to Google and YouTube
url: https://www.bitdefender.com/en-us/blog/labs/the-scam-that-wont-quit-malicious-tradingview-premium-ads-jump-from-meta-to-google-and-youtube
source: Over Security - Cybersecurity news aggregator
date: 2026-04-09
fetch_date: 2026-04-10T04:46:53.073893
---

# The Scam That Won’t Quit: Malicious “TradingView Premium” Ads Jump from Meta to Google and YouTube

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

7 min read

# The Scam That Won’t Quit: Malicious “TradingView Premium” Ads Jump from Meta to Google and YouTube

[![Alin MOLOCE](https://blogapp.bitdefender.com/labs/content/images/size/w100/2025/09/photo.JPG "Alin MOLOCE")](/en-us/blog/labs/author/moloce "Alin MOLOCE")[![Ionut Alexandru BALTARIU](https://blogapp.bitdefender.com/labs/content/images/size/w100/2023/10/BSP_3250.jpg "Ionut Alexandru BALTARIU")](/en-us/blog/labs/author/ionut-baltariu "Ionut Alexandru BALTARIU")[![Alina BÎZGĂ](https://blogapp.bitdefender.com/labs/content/images/size/w100/2023/12/Capture.JPG "Alina BÎZGĂ")](/en-us/blog/labs/author/alina-bizga "Alina BÎZGĂ")

[Alin MOLOCE](/en-us/blog/labs/author/moloce "Alin MOLOCE")[Ionut Alexandru BALTARIU](/en-us/blog/labs/author/ionut-baltariu "Ionut Alexandru BALTARIU")[Alina BÎZGĂ](/en-us/blog/labs/author/alina-bizga "Alina BÎZGĂ")

September 25, 2025

  ![The Scam That Won’t Quit: Malicious “TradingView Premium” Ads Jump from Meta to Google and YouTube](https://blogapp.bitdefender.com/labs/content/images/size/w600/2025/09/The-Scam-That-Won-t-Quit-Malicious--TradingView-Premium--Ads-Jump-from-Meta-to-Google-and-YouTube.jpeg "The Scam That Won’t Quit: Malicious “TradingView Premium” Ads Jump from Meta to Google and YouTube")

Over the past year, Bitdefender researchers have been monitoring a persistent malicious campaign that initially spread via Facebook Ads, promising “free access” to TradingView Premium and other trading or financial platforms.

According to researchers at Bitdefender Labs, this campaign has now expanded beyond Meta platforms, infiltrating both YouTube and Google Ads, exposing content creators and regular users alike to increased risks.

![](https://blogapp.bitdefender.com/labs/content/images/2025/09/data-src-image-28a538b4-0aa6-42aa-b011-6dbed457fdf3.png)![](https://blogapp.bitdefender.com/labs/content/images/2025/09/data-src-image-d93c9e92-bf59-423e-9602-e5d71c7b03bb.png)

Unlike legitimate ads, these malicious campaigns redirect users to malware-laced downloads aiming to steal credentials and compromise accounts.

You can read more about these global malvertising campaigns here:

* [Malvertising Campaign on Meta Expands to Android, Pushing Advanced Crypto-Stealing Malware to Users Worldwide](https://www.bitdefender.com/en-us/blog/labs/malvertising-campaign-on-meta-expands-to-android-pushing-advanced-crypto-stealing-malware-to-users-worldwide)
* [Weaponizing Facebook Ads: Inside the Multi-Stage Malware Campaign Exploiting Cryptocurrency Brands](https://www.bitdefender.com/en-us/blog/labs/weaponizing-facebook-ads-inside-the-multi-stage-malware-campaign-exploiting-cryptocurrency-brands)
* [Pi2Day Scams: Crypto Users Targeted in Coordinated Facebook Ad Campaign Delivering Malware and Stealing Wallets](https://www.bitdefender.com/en-au/blog/hotforsecurity/pi2day-scams-crypto-users-target%5B%E2%80%A6%5Dacebook-ad-campaign-delivering-malware-and-stealing-wallets)
* [Facebook Ad Scam Tricks Investors with Fake Messages and Malware Disguised as ‘Verified Facebook App’](https://www.bitdefender.com/en-au/blog/hotforsecurity/facebook-ad-scam-tricks-investor%5B%E2%80%A6%5Dake-messages-and-malware-disguised-as-verified-facebook-app)

## Hijacked Google Ads account and TradingView Impersonation on YouTube: How the Scam Works

Looking into the specifics of the scam impersonating TradingView, researchers found that threat actors hijacked the Google advertiser account of a design agency in Norway. Separately, the cybercrooks also took over a YouTube account to which they could begin redirecting victims through Google’s ads system. Once again, the verified status of the compromised YouTube channel, combined with its new branding and TradingView visuals, allowed cybercriminals to impersonate the official TradingView channel. The rebranded channel was designed to be nearly indistinguishable from TradingView’s by:

* **Reusing official branding**, with logos, banners, and visual elements identical to the real TradingView.
* **Mirroring playlists** – playlists on the homepage are linked from the official TradingView channel, making the fake channel look active, even though it has no videos of its own.
* **Abusing the verified badge on YouTube** – since the channel was previously verified for legitimate reasons, users assume authenticity without checking deeper.

You may also want to read: [Malicious Facebook Ads Push Fake ‘Meta Verified’ Browser Extensions to Steal Accounts](https://www.bitdefender.com/en-us/blog/hotforsecurity/malicious-facebook-ads-push-fake-meta-verified-browser-extensions-to-steal-accounts)

![](https://blogapp.bitdefender.com/labs/content/images/2025/09/data-src-image-4fbbf995-5b6f-458e-8d98-730baea1ef40.png)![](https://blogapp.bitdefender.com/labs/content/images/2025/09/data-src-image-d8964934-c136-4843-8201-531e57c84032.png)

Upon closer inspection, several red flags emerge:

* The **channel handle** is different (not @TradingView);
* The channel itself contains **no original content,** only having 96 registered views, which would be impossible for a legitimate channel given Tradingview’s popularity**;**
* The impersonation relies entirely on **unlisted ad videos** shown only through paid placements, avoiding public scrutiny;

One ad video is titled *“Free TradingView Premium – Secret Method They Don’t Want You to Know”*. Despite being unlisted, it gained over **182,000 views in just a few days** through aggressive advertising.

![](https://blogapp.bitdefender.com/labs/content/images/2025/09/image.png)

The video’s generic promotional content mentions the capabilities of the TradingView application. The description of the unlisted video includes a link where the user can download the malicious executable. Just as in the Meta ads, the user might end up on a benign page if the attackers don’t think the requests were made from a valid target.

Why unlisted videos?The unlisted status is deliberate, of course. By not being publicly searchable, these malicious videos avoid casual reporting and platform moderation. Instead, they are shown exclusively through ad placements, ensuring they reach their targets while remaining hidden from public view.

The description promises benefits such as simplified trading, personalized indicators, and “reasonable” trading strategies. To build trust, it even includes disclaimers about financial risks. However, these messages mask the real intent:

* Redirecting victims to **malware downloads**;
* Using phishing pages to steal credentials;
* Spreading across multiple channels and domains.

## How Business Accounts Become Weapons

This case highlights a growing risk: when a company’s Google account is compromised, its connected YouTube channel can be stripped of all original content and repurposed for scam and other malicious activities.

Here’s how compromise can occur:

1. You or your staff members fall for a phishing email, malicious attachment, or credential-stealing campaign that gives attackers access to the Google account.
2. Since YouTube is tied to Google, the attackers gain control of the channel.
3. To erase any trace of the original business identity, attackers delete existing videos, branding, and playlists.
4. The account is rebranded to impersonate a popular brand such as TradingView. Verified badges and existing subscriber counts lend credibility.
5. Instead of building organic reach, attackers exploit Google Ads to push malware-laden unlisted videos directly to users.

## ***Malware Analysis***

Upon analyz...