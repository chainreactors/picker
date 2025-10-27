---
title: Adding Chrome Browser Cloud Management remediation actions in Splunk using Alert Actions
url: http://security.googleblog.com/2023/05/adding-chrome-browser-cloud-management.html
source: Google Online Security Blog
date: 2023-06-01
fetch_date: 2025-10-04T11:45:04.356040
---

# Adding Chrome Browser Cloud Management remediation actions in Splunk using Alert Actions

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Adding Chrome Browser Cloud Management remediation actions in Splunk using Alert Actions](https://security.googleblog.com/2023/05/adding-chrome-browser-cloud-management.html "Adding Chrome Browser Cloud Management remediation actions in Splunk using Alert Actions")

May 31, 2023

Posted by Ashish Pujari, Chrome Enterprise Security Team

**Introduction**

Chrome is trusted by millions of business users as a secure enterprise browser. Organizations can use [Chrome Browser Cloud Management](https://chromeenterprise.google/browser/management/) to help manage Chrome browsers more effectively. As an admin, they can use the Google Admin console to get Chrome to report critical security events to third-party service providers such as [Splunk](https://splunk.com/)® to create custom enterprise security remediation workflows.

Security remediation is the process of responding to security events that have been triggered by a system or a user. Remediation can be done manually or automatically, and it is an important part of an enterprise security program.

**Why is Automated Security Remediation Important?**

When a security event is identified, it is imperative to respond as soon as possible to prevent data exfiltration and to prevent the attacker from gaining a foothold in the enterprise. Organizations with mature security processes utilize automated remediation to improve the security posture by reducing the time it takes to respond to security events. This allows the usually over burdened Security Operations Center (SOC) teams to avoid alert fatigue.

**Automated Security Remediation using Chrome Browser Cloud Management and Splunk**

Chrome integrates with [Chrome Enterprise Recommended](https://chromeenterprise.google/recommended/#security-&-trust) partners such as Splunk® using [Chrome Enterprise Connectors](https://support.google.com/chrome/a/answer/11375053) to report security events such as malware transfer, unsafe site visits, password reuse. Other supported events can be found on our [support page](https://support.google.com/a/answer/9393909?hl=en).

The Splunk integration with Chrome browser allows organizations to collect, analyze, and extract insights from security events. The extended security insights into managed browsers will enable SOC teams to perform better informed automated security remediations using [Splunk](https://docs.splunk.com/Documentation/Splunk/9.0.4/Alert/Setupalertactions)® [Alert Actions](https://docs.splunk.com/Documentation/Splunk/9.0.4/Alert/Setupalertactions).

Splunk Alert Actions are a great capability for automating security remediation tasks. By creating alert actions, enterprises can automate the process of identifying, prioritizing, and remediating security threats.

In Splunk®, SOC teams can use alerts to monitor for and respond to specific Chrome Browser Cloud Management events. Alerts use a saved search to look for events in real time or on a schedule and can trigger an Alert Action when search results meet specific conditions as outlined in the diagram below.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg34lHUTbNNIH8t4iYgFpu-xVc6UW7jk0GhWXlKnOF9rSvFxU9UJD_-2Jty66udUYSXHBtXpaccgU40yGfWPTejxHudNbSYJs632frxmVshuE6Va24SO5SbuIlus2yyFSjhmzaf9Z0YAxoyv80KmPOMFH5NANh6J8z5XALwf2XN7FyMfZFjYhCx7SWi7Q/s1600/1.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg34lHUTbNNIH8t4iYgFpu-xVc6UW7jk0GhWXlKnOF9rSvFxU9UJD_-2Jty66udUYSXHBtXpaccgU40yGfWPTejxHudNbSYJs632frxmVshuE6Va24SO5SbuIlus2yyFSjhmzaf9Z0YAxoyv80KmPOMFH5NANh6J8z5XALwf2XN7FyMfZFjYhCx7SWi7Q/s1600/1.jpeg)

**Use Case**

If a user downloads a malicious file after bypassing a Chrome “Dangerous File” message their managed browser/managed CrOS device should be quarantined.

**Prerequisites**

* Create a [Chrome Browser Cloud Management](https://support.google.com/chrome/a/topic/9025410) account at no additional costs* [Splunk](https://www.splunk.com/en_us/products/splunk-enterprise.html)® [Enterprise](https://www.splunk.com/en_us/products/splunk-enterprise.html) v9.0.\* or [Splunk® Cloud Platform](https://www.splunk.com/en_us/products/splunk-cloud-platform.html) (Cost: Please refer to Splunk’s website)* Understanding of the [Splunk alerting workflow](https://docs.splunk.com/Documentation/Splunk/9.0.4/Alert/AlertWorkflowOverview)* Understanding of how to [create custom alert actions](https://dev.splunk.com/enterprise/docs/devtools/customalertactions/createuicaa) in Splunk®.

**Setup**

1. **Install the Google Chrome Add-on for Splunk App**

   Please follow installation instructions [here](https://docs.splunk.com/Documentation/AddOns/released/Overview/Installingadd-ons) depending on your Splunk Installation to install the [Google Chrome Add-on for Splunk App](https://splunkbase.splunk.com/app/5607).

   - **Setting up Chrome Browser Cloud Management and Splunk Integration**

     Please follow the guide [here](https://support.google.com/chrome/a/answer/11375053) to set up Chrome Browser Cloud Management and Splunk® integration.

     - **Setting up Chrome Browser Cloud Management API access**

       To call the Chrome Browser Cloud Management [API](https://support.google.com/chrome/a/answer/9681204?hl=en), use a service account properly configured in the Google admin console. [Create](https://support.google.com/a/answer/7378726?hl=en) a (or use an existing) service account and download the JSON representation of the key.

       [Create](https://support.google.com/a/answer/2406043?hl=en) a (or use an existing) role in the admin console with all the “Chrome Management” privileges as shown below.

       [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0T1_pN37GXfoqzSrfVsfHO7nQoKHHUxNQc3sMghPxyxNajP5RSzPC9NCWHMb2V1F0QA2GzS2ml4Y9ET-NJe54uGc1nFTI9LWFrn_jKwS1EMRfgGNzoly7EmQJJyLLnwyJt1AmaWjy_7R6H_vRQesF7BLaR4HxHaePdU8q2SCkOz-nKZIrniWPIAl-yA/s1600/2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0T1_pN37GXfoqzSrfVsfHO7nQoKHHUxNQc3sMghPxyxNajP5RSzPC9NCWHMb2V1F0QA2GzS2ml4Y9ET-NJe54uGc1nFTI9LWFrn_jKwS1EMRfgGNzoly7EmQJJyLLnwyJt1AmaWjy_7R6H_vRQesF7BLaR4HxHaePdU8q2SCkOz-nKZIrniWPIAl-yA/s1600/2.png)

       Assign the created role to the service account using the “Assign service accounts” button.

       [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjq3Km9s3Ng34N4tS76wg6Ji1iLChlC8Njq_AmxtC68s23Q6Vfxz8nGTCjNIE4fwMd8VkPPUTWhrmWhYjDGJuipuXInrBMFVfRqjnTC09Disr54CvP_E5SpbjAIRM6fwWxXg0b9kdKpoIpwiqa18bTjSFj1YtLhF36qXGWH7-sz-nBKLLUbhqWLHfrkQg/s1600/3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjq3Km9s3Ng34N4tS76wg6Ji1iLChlC8Njq_AmxtC68s23Q6Vfxz8nGTCjNIE4fwMd8VkPPUTWhrmWhYjDGJuipuXInrBMFVfRqjnTC09Disr54CvP_E5SpbjAIRM6fwWxXg0b9kdKpoIpwiqa18bTjSFj1YtLhF36qXGWH7-sz-nBKLLUbhqWLHfrkQg/s1600/3.png)

       - **Setting up Chrome Browser Cloud Management App in Splunk**®

         Install the App i.e. Alert Action from our [Github page](https://github.com/google/ChromeBrowserEnterprise/tree/main/Python/connectors). You will notice that the Splunk App uses the below [directory structure](https://dev.splunk.com/enterprise/docs/developapps/createapps/appanatomy/). Please take some time to understand the directory structure layout.

         [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGURf5HGcMLTjRYgFjtUO091RgY252bofGKmeF6VAEyhjkEWt4HIbuKdwaD2wJsyOfn70FryjTTMOrbeQ084SA_LPvUvZdEGoCPWmGPtT3lppUg-iMN7pve9e8GGvRMGt5xce9TPI8KTaYCbKD6BHHuAhgsDXSaaikThcg9e_ma3Er4AGOq6PwN_VemA/s1600/4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGURf5HGcMLTjRYgFjtUO091RgY252bofGKmeF6VAEyhjkEWt4HIbuKdwaD2wJsyOfn70FryjTTMOrbeQ084SA_LPvUvZdEGoCPWmGPtT3lppUg-iMN7pve9e8GGvRMG...