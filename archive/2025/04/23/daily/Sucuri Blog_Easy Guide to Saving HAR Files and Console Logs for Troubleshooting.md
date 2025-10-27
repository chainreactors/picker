---
title: Easy Guide to Saving HAR Files and Console Logs for Troubleshooting
url: https://blog.sucuri.net/2025/04/easy-guide-to-saving-har-files-and-console-logs-for-troubleshooting.html
source: Sucuri Blog
date: 2025-04-23
fetch_date: 2025-10-06T22:05:23.446256
---

# Easy Guide to Saving HAR Files and Console Logs for Troubleshooting

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

* [HTTP Errors](https://blog.sucuri.net/category/http-errors)
* [Security Education](https://blog.sucuri.net/category/security-education)
* [Website Security](https://blog.sucuri.net/category/website-security)

# Easy Guide to Saving HAR Files and Console Logs for Troubleshooting

[![](https://blog.sucuri.net/wp-content/uploads/2025/04/avatar_user_115_1745352070-60x60.jpg)](https://blog.sucuri.net/author/msinghtoor)

[Maninder Toor](https://blog.sucuri.net/author/msinghtoor)

* April 22, 2025

![Easy Guide to save HAR Files and Console Logs for Troubleshooting](https://blog.sucuri.net/wp-content/uploads/2025/04/Easy-Guide-to-save-HAR-Files-and-Console-Logs-for-Troubleshooting-820x385.png)

When something goes wrong with a website – whether it is a broken design, slow performance, shows an error message or something else, it is sometimes difficult to find the exact cause of the issue just by looking at the page. That’s where the HAR files or browser console errors come into play. These in-built browser features allow the tech experts or developers to dig deeper into what’s happening behind the scenes. In some cases, our support team may ask for the HAR file and console logs to help troubleshoot the issue.

In this blog, we’ll show you a simple and step-by-step guide on how to generate and save the HAR file and browser console logs so you can share that with your developer or Sucuri support team for troubleshooting.

## What is a HAR file?

When you visit a website, the browser loads various resources like images, scripts, styles and more to display the website. A HAR (HTTP Archive) file keeps a detailed record of all the requests that browser makes to the server during the website visit. It captures things like the time it takes for each request, server response, the IP address of the server where the request was sent, the size of the data, headers, cookies, and other useful data.

## How to generate a HAR file?

You can export the HAR file on all modern web browsers. Here’s how to generate and save an HAR file on different browsers.

*Please note that the HAR file may contain sensitive information. Before sharing it, we suggest removing things like authentication tokens, cookies or personal details from the HAR file. You can use a text editor to edit the HAR file.*

### Google Chrome

1. Open Chrome and right-click anywhere on the page and select **Inspect Element**
    or press **Ctrl + Shift + I** on Windows/Linux or **Cmd + Option + I** on Mac as a shortcut.
2. In the Developer Tools window, go to the **Network** tab.
3. Make sure the **Preserve Log** option is checked.
4. If you’re facing cache issues, check the **Disable cache** box.![chrome preserve log disable cache](https://blog.sucuri.net/wp-content/uploads/2025/04/chrome-preserve-log-disable-cache-e1745352251368.png)
5. Replicate the issue you’re experiencing. You’ll see all requests in the Network tab.
6. Click on the **Export HAR (sanitized)** button to save the HAR file.![chrome export HAR](https://blog.sucuri.net/wp-content/uploads/2025/04/chrome-export-har-e1745352274424.png)

### Mozilla Firefox

1. Open Firefox and right-click anywhere on the page and choose **Inspect**
    or press **Ctrl + Shift + I** on Windows/Linux or **Cmd + Option + I** on Mac as a shorcut
2. Go to the **Network** tab in the Developer Tools.![firefox network tab](https://blog.sucuri.net/wp-content/uploads/2025/04/firefox-network-tab.png)
3. Now replicate the issue that you are experiencing.
4. Once the page is fully loaded, right-click in the network log area and select **Save All as HAR**.![firefox save HAR](https://blog.sucuri.net/wp-content/uploads/2025/04/firefox-save-har.png)

### Microsoft Edge

1. Right-click anywhere on the page and select **Inspect**.
    or press **Ctrl + Shift + I** on Windows/Linux or **Command + Option + I** on Mac as a shortcut.
2. Go to the **Network** tab and check the **Preserve** option.
3. Replicate the issue that you are facing so that the requests can be captured in the Network tab.
4. Click on the **Export HAR file** button to save the HAR file.![microsoft edge export HAR](https://blog.sucuri.net/wp-content/uploads/2025/04/microsoft-edge-export-har-e1745352304566.png)

### Safari

1. Open Safari and click **Develop** in the menu bar and choose **Show Web Inspector**.
    or press **Command + Option + I** on Mac and **Ctrl + Shift + I on Windows** as a shortcut.
2. If you don’t see the **Develop** menu, go to **Safari** > **Preferences** > **Advanced** and check **Show Develop menu in menu bar**.
3. Go to the **Network** tab and select the **Preserve Log** option.![safari preserve log](https://blog.sucuri.net/wp-content/uploads/2025/04/safari-preserve-log.png)
4. Now replicate the issue...