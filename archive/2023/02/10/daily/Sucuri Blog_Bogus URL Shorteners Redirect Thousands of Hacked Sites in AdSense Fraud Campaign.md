---
title: Bogus URL Shorteners Redirect Thousands of Hacked Sites in AdSense Fraud Campaign
url: https://blog.sucuri.net/2023/02/bogus-url-shorteners-redirect-thousands-of-hacked-sites-in-adsense-fraud-campaign.html
source: Sucuri Blog
date: 2023-02-10
fetch_date: 2025-10-04T06:13:31.811219
---

# Bogus URL Shorteners Redirect Thousands of Hacked Sites in AdSense Fraud Campaign

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

# Bogus URL Shorteners Redirect Thousands of Hacked Sites in AdSense Fraud Campaign

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* February 9, 2023

![Bogus Short URLs Redirect Thousands of Hacked Sites in AdSense Fraud Campaign](https://blog.sucuri.net/wp-content/uploads/2023/02/23-BlogPost_Feature-Image_1490x700_Bogus-Short-URLs-Redirect-Thousands-of-Hacked-Sites-in-AdSense-Fraud-Campaign-820x386.jpg)

Late last year we reported on a malware campaign targeting thousands of WordPress websites to [redirect visitors to bogus Q&A websites](https://blog.sucuri.net/2022/11/massive-ois-is-black-hat-redirect-malware-campaign.html). The sites themselves contained very little useful information to a regular visitor, but — more importantly — also contained Google Adsense advertisements. It appeared to be an attempt to artificially pump ad views to generate revenue.

Since September, our SiteCheck remote scanner has detected this campaign on **10,890** infected sites. More recently activity has surged with over 70 new malicious domains masquerading as URL shorteners. At the time of writing, over **2,600+** sites in 2023 alone have been detected.

In this post we’ll be reviewing the scope of this malware, how it works, and what to do if your website has been affected by this infection.

**Contents:**

* **[Bogus short URL domains](#short-urls)**
* **[Migration from CloudFlare to DDoS-Guard](#migration)**
* **[Bing & Twitter redirects](#bing-twitter)**
* **[AdSense IDs](#adsense-ids)**
* **[Motives](#motives)**
* **[Malware analysis](#malware-analysis)**
* [**Mitigation**](#mitigation)

## Variations on a theme

As seen in the last wave, hacked website traffic is redirected to a series of low-quality websites built on the [Question2Answer](https://www.question2answer.org/) CMS. The topics of “discussion” appear to be mostly based on crypto currency and blockchain.

![Question2Answer blockchain website](https://blog.sucuri.net/wp-content/uploads/2023/02/question2answer-crypto-website-traffic.png)

Website traffic redirected to low-quality crypto themed websites built on the Question2Answer CMS.

Whether or not this is intentionally designed to also advertise new cryptocurrencies as part of pump-and-dump ICO (initial coin offering) fraud is certainly possible, but it appears that the main objective is still ad fraud by artificially increasing traffic to pages which contain the AdSense ID which contain Google ads for revenue generation.

![AdSense fraud revealed with page inspection](https://blog.sucuri.net/wp-content/uploads/2023/02/google-adsense-generate-revenue.png)

## Bogus short URL domains

Over the course of the last two months we’ve identified over 75 pseudo-short URL domains associated with these redirects:

```
0-4[.]top/GQH0r3
012[.]bond/lUg0r3
5pm[.]am/BZl0r8
77w[.]pw/ZTe0r7
7la[.]la/ywI0r0
99pw[.]pw/Epo0r2
9ge[.]ge/bwN0c6
b-d[.]bond/wpZ0r1
b-i-t-l-y[.]co/bNA0r5
b-ly[.]link/pge0r3
b-y[.]by/prB0r7
bit-ly[.]is/UBz0r9
bit-ly[.]mobi/cMq0r0
bitly[.]best/oMR0r0
bitly[.]email/liy0r3
bitly[.]gold/hNL0r9
bitly[.]host/MOA0r3
bitly[.]network/VKu0r1
c-lick[.]click/Cau0r1
c-you[.]cyou/hIK0r7
cc-z[.]cz/jGA0r4
co-o[.]co/Fja0r8
cr-7[.]cc/rfl0r0
cutlinks[.]biz/Hwa0r9
cutlinks[.]ca/63H5U
cutlinks[.]mobi/sdr0r8
cutlinks[.]org/63H5U
cutlinks[.]pw/Gvt0r8
cuturls[.]net/zVU0r0
d-ev[.]dev/xgL0r1
fco[.]to/vUC0r7
fmo[.]fm/KFS0r2
g-l[.]gl/TlX0r9
g-y[.]gy/Pvd0r5
gob.co[.]il/Vym0r1
gov-cn[.]cloud/YsL0r9
gov.co[.]ve/WEQ0r1
h-air[.]hair/eWP0r1
i-cu[.]icu/Twa0r4
i-io[.]io/CgD0r2
i-n-fo[.]info/bPX0r6
i-s[.]is/ixF0r7
icx[.]cx/oaC0r7
ii-ii[.]ru/yjh0r6
ilc[.]lc/vQO0r3
isn[.]is/63H5U
isx[.]sx/mqJ0r3
j-e[.]je/DDn0c1
l-o[.]loan/AKI0r1
l-ol[.]lol/DiB0r3
lbz[.]bz/cro0r5
m-n[.]mn/DrG0r6
mvc[.]vc/nMo0r3
n-g[.]ng/Vwi0r2
n-z[.]nz/KoC0r8
obz[.]bz/HqD0r5
oo-o[.]co/Ocv0c1
oo[.]coffee/Dxw0r3
psu[.]su/sDy0r2
s-k[.]sk/pHH0r7
s-b[.]sb/QvS0r2
s-sh[.]sh/QAP0r9
sy-s[.]systems/hwE0r1
t-o[.]to/MMn0r9
tiny-url[.]mobi/ACE0r0
u-mu[.]mu/Dwk0r8
uxe[.]luxe/jfA0r6
vms[.]ms/dmc0r0
vv-vip[.]vip/GkE0r9
vvg[.]vg/yDY0r4
w-me[.]me/hRM0r9
w-tw[.]tw/Oki0r9
w-ws[.]ws/ONk0r3
wac[.]ac/wXB0r4
wci[.]ci/Zpm0r0
wco[.]pw/Eox0r5
wst[.]st/prQ0r9
xx-yz[.]xyz/YNB0r6
```

All of the malicious URLs pretend to look like they belong to some URL shortening service. Some of them even mimic names of reputable URL shorteners like Bitly (e.g **bitly[.]best**, **b-i-t-l-y[.]co**, **bit-ly[.]mobi**, etc).

If you enter any ...