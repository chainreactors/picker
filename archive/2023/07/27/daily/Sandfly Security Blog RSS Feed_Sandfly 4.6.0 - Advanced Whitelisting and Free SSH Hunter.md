---
title: Sandfly 4.6.0 - Advanced Whitelisting and Free SSH Hunter
url: https://sandflysecurity.com/news/sandfly-4-6-0-advanced-whitelisting-and-free-ssh-hunter
source: Sandfly Security Blog RSS Feed
date: 2023-07-27
fetch_date: 2025-10-04T11:54:00.420979
---

# Sandfly 4.6.0 - Advanced Whitelisting and Free SSH Hunter

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 4.6.0 - Advanced Whitelisting and Free SSH Hunter

26 July 2023

News

Sandfly 4.6.0 receives a long anticipated feature: advanced whitelisting. **We have also enabled our powerful SSH hunter for all users even on our free tier.** Additionally we have expanded our Linux threat coverage to include new SSH key option checks, credential leak detection, and more.

## Advanced Whitelisting

Sandfly comes out of the box ready to detect threats against Linux. However, each customer will have an environment that is unique. Sometimes alerts will happen that Sandfly considers unusual, but are perfectly normal for an end user.

In prior versions, customers were required to disable a sandfly module per-host or across all systems to eliminate false or true positives (a real detection, but not a threat to the environment). With our advanced whitelisting, customers can now be very specific about what they want to ignore and still get relevant alerts when detection happens outside those parameters.

We now offer the following whitelisting options:

* Disable Sandfly - Do not run the sandfly module on this or all hosts (legacy mode).
* Rapid Match - Based on Sandfly Hunter key forensic value.
* Loose Match - Based on loose set of parameters for the alert (e.g. process name and path).
* Strict Match - Based on a tighter list of parameters for the alert (e.g. process name, path, and SHA512 hash).
* Advanced Match - Based on any forensic attribute deemed important (e.g. process name, path, username, binary size, and cryptographic hashes).

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly whitelisting types.](https://www.datocms-assets.com/56687/1690346247-whitelist-modes.png?auto=format&dpr=2&q=60&w=920 "Sandfly whitelisting types.")

## Example Whitelist

The new feature is best shown with an example. Here is an alert that normally could be considered malicious, but in this environment is intentional:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly alert on binary running from hidden directory.](https://www.datocms-assets.com/56687/1690346349-whitelist-example-alert.png?auto=format&dpr=2&q=60&w=920 "Sandfly alert on binary running from hidden directory.")

Sandfly has identified a process running from a hidden directory:

*/usr/.security/monitor*

In many cases this would be suspicious, but here it is a security tool running from a hidden directory on purpose. Below we'll describe each whitelist method and how they work in relation to this event.

### Disable Sandfly

This is the legacy mode. We simply will disable the sandfly module entirely across all systems. In the above example we will not alert on any process running in any hidden directory across the host or all hosts.

Sometimes this is the best option if you know a particular check is going to cause alerts based on how the local systems are being run. However, this is a bit of a shotgun approach and generally reserved for special cases where the other options are not workable.

### Rapid Match Whitelist

Simply select the Sandfly hunter key forensic under the alert for your whitelist. For instance if you wanted to just ignore on this path, you simply click the whitelist button. See image below for an example.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly rapid whitelist based on hunter data.](https://www.datocms-assets.com/56687/1690345508-rapid-whitelist-sandfly-hunter-process-path.png?auto=format&dpr=2&q=60&w=920 "Sandfly rapid whitelist based on hunter data.")

Next, you are taken to the whitelist detail screen where you can see the rule, what hosts it would apply to, optional tags, or enabled against all hosts.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Enabling whitelist for all hosts, tagged hosts, or individual hosts.](https://www.datocms-assets.com/56687/1690345555-rapid-whitelist-sandfly-hunter-process-path-detail.png?auto=format&dpr=2&q=60&w=920 "Enabling whitelist for all hosts, tagged hosts, or individual hosts.")

You can also supply a comment so others can see when and why this rule was created.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Adding a comment to a whitelisted entry.](https://www.datocms-assets.com/56687/1690345566-rapid-whitelist-sandfly-hunter-process-notes.png?auto=format&dpr=2&q=60&w=920 "Adding a comment to a whitelisted entry.")

### Loose Match Whitelist

A loose match whitelist will take recommended parameters from Sandfly to make a whitelist that will limit the scope of the alert, but allows some leniency to prevent unnecessary alarms across different hosts.

For instance, a loose whitelist for a process would ignore it if it matches the process name and the process path. A process name from a different path would still generate an alert. We have similar parameters for files, directories, users, log entries, etc.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Loose match whitelisting.](https://www.datocms-assets.com/56687/1690346864-loose-match-whitelist-selection.png?auto=format&dpr=2&q=60&w=920 "Loose match whitelisting.")

Going to the review page, we see instead of one simple rule made like our first example, we now have two based on process name and path.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Loose match whitelist rules.](https://www.datocms-assets.com/56687/1690346589-loose-match-whitelist-details.png?auto=format&dpr=2&q=60&w=920 "Loose match whitelist rules.")

### Strict Match Whitelist

Like loose whitelisting, strict whitelisting takes some defaults based on our experience but makes them much tighter. For a process, Sandfly will require the process name, path, and SHA512 hash to match. This is a significantly higher bar for a process to hit to be ignored.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Strict match whitelisting.](https://www.datocms-assets.com/56687/1690346833-strict-match-whitelist-selection.png?auto=format&dpr=2&q=60&w=920 "Strict match whitelisting.")

Here you can see the added details needed to meet the strict requirements:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Strict match whitelisting rules for review.](https://www.datocms-assets.com/56687/1690346949-strict-match-whitelist-details.png?auto=format&dpr=2&q=60&w=920 "Strict match whitelisting rules for review.")

### Advanced Match Whitelist

Finally, if you want to build your own custom whitelist based on any Linux forensic attribute, you can do that as well. Simply select advanced:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Advanced whitelisting selected.](https://www.datocms-assets.com/56687/1690347081-advanced-match-whitelist-selection.png?auto=format&dpr=2&q=60&w=920 "Advanced whitelisting selected.")

You will be taken then to the rule builder where you can pick individual forensic attributes to add to the rule:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Selecting forensic values for advanced whitelisting on Linux.](https://www.datocms-assets.com/56687/1690347642-advanced-match-whitelist-attribute-selection.png?auto=format&dpr=2&q=60&w=920 "Selecting forensic values for advanced whitelisting on Linux.")

You can also type in values of interest to rapidly find them. Here we want to find all cryptographic hashes and select them all to be extra paranoid. If this is done, then the on disk hashes of the file and running process binary hashes must match to be exempted from alert:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Selecting cryptographic hashes for a whitelist process on Linux.](https://www.datocms-assets.com/56687/1690...