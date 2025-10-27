---
title: Chinese Gambling Spam Targets World Cup Keywords
url: https://blog.sucuri.net/2022/12/chinese-gambling-spam-targets-world-cup-keywords.html
source: Sucuri Blog
date: 2022-12-03
fetch_date: 2025-10-04T00:22:18.142504
---

# Chinese Gambling Spam Targets World Cup Keywords

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)

[Login](https://dashboard.sucuri.net/login/)

[Login](https://dashboard.sucuri.net/login)

New Customer?

[Sign up now.](https://sucuri.net/website-security-platform/signup/)

* [Submit a ticket](https://support.sucuri.net/support/?new)
* [Knowledge base](https://docs.sucuri.net/)
* [Chat now](https://sucuri.net/live-chat/)

Search for:

Search

* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [Website Security](https://blog.sucuri.net/category/website-security)

# Chinese Gambling Spam Targets World Cup Keywords

[![](https://secure.gravatar.com/avatar/292c42da0d9f929a9405e6ce269f101cc888f5c5cbcf8006e131c9bed042c80d?s=60&d=mm&r=g)](https://blog.sucuri.net/author/denis)

[Denis Sinegubko](https://blog.sucuri.net/author/denis)

* December 2, 2022

![Chinese Gambling Spam Leverages World Cup Keywords](https://blog.sucuri.net/wp-content/uploads/2022/12/BlogPost_Feature-Image_1490x700_Chinese-SEO-Gambling-Redirect-Spam-820x386.png)

Since 2018, our team has been tracking an interesting type of website infection where the **<title>** tag of a hacked website is changed to Chinese text — changes which are clearly seen in the website’s search results and source code. However, when you open the affected website in a JavaScript-enabled web browser, the site operates as normal and the original title presents itself without any modifications.

What’s going on behind the scenes turns out to be a pretty massive black hat SEO campaign promoting Chinese gambling, sports betting sites, and mobile apps. The attack affects mostly Chinese websites, but we’ve found a number of western websites also affected by the malicious injections. According to [PublicWWW data](#scope), the number of infected sites exceeds 50,000 at the time of writing.

While the SEO tricks that this attack employs have stayed (mostly) the same since 2018, the attackers regularly update both their redirect scripts and the spam title content to attract more search traffic and ensure the redirects are functional.

And in recent weeks, our research team has noticed a pivot for the campaign to leverage search traffic for the popular World Cup soccer championship.

**Contents:**

* **[Injected titles for World Cup keywords](#injected-titles)**
* **[Title switching](#title-switching)**
* **[Scope and impact](#scope)**
* **[Redirects and obfuscation techniques](#redirects-obfuscation)**
* **[External script variants](#external-scripts)**
* **[Examples of external script URLs](#examples)**
* **[Affected websites](#websites)**
* **[Mitigation steps](#mitigation)**

## Injected titles for World Cup keywords

Many of the compromised websites have been recently updated to include modified titles for keywords related to the Qatar 2022 FIFA World Cup.

For example:

* 卡塔尔世界杯赛事分析·(中国)世界杯赛事中心
   (translated: Qatar World Cup Event Analysis·(China) World Cup Event Center)
* 2022世界杯买球投注-世界杯安全买球网站【官方平台】
   (translated: 2022 World Cup Betting-World Cup Safe Betting Website [Official Platform]
* 世界杯赛事预测\_世界杯在线直播\_世界杯赛时间 – 体育新世界
   (translated: World Cup Match Prediction\_World Cup Online Live\_World Cup Time – Sports New World)

Furthermore, the intermediary sites that the attack redirects to are usually also World Cup themed, as seen below.

[![World Cup themed intermediary redirect for chinese gambling SEO spam](https://blog.sucuri.net/wp-content/uploads/2022/12/world_cup_intermediary_redirect_website.png)](https://blog.sucuri.net/wp-content/uploads/2022/12/world_cup_intermediary_redirect_website.png)

World Cup themed intermediary redirect website

### So, how does this SEO trick work?

If you check the HTML code of the infected web pages, you’ll immediately find the **<title>** tag and the **<meta>** tags for keywords and description filled with sequences of digits, ampersands, hashes, and semicolons like this:

![Title and meta tags on a compromised sites SEO gambling spam](https://blog.sucuri.net/wp-content/uploads/2022/12/title_meta_tags.png)

Title and meta tags on a compromised sites

These strange sequences are so-called [HTML entities](https://www.freeformatter.com/html-entities.html) that represent Unicode characters using their character codes in UTF-8 charset.

Let’s take this title tag for example:

```
<title>&#19990;&#30028;&#26479;&#22806;&#22260;&#32593;&#31449;&#45;&#105;&#111;&#115;&#47;&#23433;&#21331;&#47;&#25163;&#26426;&#29256;&#97;&#112;&#112;&#19979;&#36733;</title>
```

After decoding, we get a more readable representation in Chinese characters:

```
<title>世界杯外围网站-ios/安卓/手机版app下载</title>
```

And in case you don’t read Simplified Chinese, here is the same title translated into English by Google Translate: “**World Cup Peripheral Website-ios/Android/Mobile App Download**”

### Title switching

When opening the infected website in a web browser, you find the real site title — completely unrelated to World Cup or gambling, and in the site’s original language. How does that happen?

The answer to this question lies in the HTML script usually found right after the poisoned title and meta tags. The script is ...