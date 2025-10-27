---
title: Sandfly 2.8.0 – Agentless Active Attack Response for Linux
url: https://sandflysecurity.com/blog/sandfly-2-8-0-agentless-active-attack-response-for-linux
source: Sandfly Security Blog RSS Feed
date: 2025-05-27
fetch_date: 2025-10-06T22:28:26.361216
---

# Sandfly 2.8.0 – Agentless Active Attack Response for Linux

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 2.8.0 – Agentless Active Attack Response for Linux

16 November 2020

Product Update

Sandfly 2.8.0 is released and features a major new upgrade allowing users to automatically respond to detected Linux attacks agentlessly. In addition to this we have made large performance upgrades to the backend server and added in new checks for policy threats that could compromise security of your hosts.

## Agentless Active Response for Linux

Sandfly now has the ability to respond to detected process attacks on Linux agentlessly. Users can select to either *kill* or *suspend* a process that is detected by Sandfly as malicious. Let’s explain what this means.

## Two Process Response Options: Kill or Suspend

With version 2.8.0 of Sandfly we are introducing two response options for process attacks: *kill* or *suspend*. You’ll notice that the *suspend* options is unique to Sandfly. Most of the time the first instinct of administrators when they see something malicious is to kill it immediately. However we actually recommend you don’t do this until you have had a chance to [investigate the process](/blog/basic-linux-malware-process-forensics-for-incident-responders/). The problem with killing malicious processes on Linux is that you lose forensic data in memory and have no chance to recover the binary for further offline analysis.

Instead what you can do with Sandfly is *suspend* the process. This has advantages over simply killing a process:

1. You preserve the process in memory for further analysis.
2. You can [recover the malicious binary](/blog/how-to-recover-a-deleted-binary-from-active-linux-malware/), even if deleted from the disk.
3. It gives you time to isolate the host and know the malicious activity has been halted while you work data preservation and backups.
4. You can more easily see the open files, network connections and other artifacts the malware is using to run.
5. If the malware is automated it may try to reload itself if it sees it has been killed. Suspended processes look to most automated malware that all is OK and it won’t try to re-infect while you implement containment procedures. This buys you time in the event you are dealing with a rapidly spreading and aggressive piece of malware.

Under the Sandfly listing you can see the new response options available on the process tab. The default is to do nothing and you can select either suspend or kill as you want.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly Malicious Process Response Selection](https://www.datocms-assets.com/56687/1635216293-sandfly-response-options.png?auto=format&dpr=2&q=60&w=920 "Sandfly Malicious Process Response Selection")

## Response Activated

When a response is activated we will tell you what happened in the alert explanation. Additionally there are boolean values under a new *response* section in the forensic JSON. These flags can be easily searched and analyzed inside your external database or SIEM tools you use to process Sandfly events. You can also pass them to a SOAR tool to take other actions based on what we did (e.g. Automatically isolate the host until incident response teams can investigate it.).

In the example below we found a process calling itself *swapoff* which was actually being used as a network enabled backdoor. We suspended this process and show the usual forensic details along with what we did in the explanation text.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly Suspends Suspicious Process on Linux](https://www.datocms-assets.com/56687/1635216301-sandfly-process-response.png?auto=format&dpr=2&q=60&w=920 "Sandfly Suspends Suspicious Process on Linux")

## Custom Sandfly Response for Incidents

In addition to using responses for built-in security checks, you can use them for custom checks you’ve created. This can be used for a variety of tasks in helping to contain an incident. Below we created a check for a suspicious process cryptographic hash and told Sandfly to check all systems and suspend the process if found. This enables incident responders to quickly go onto all systems and do a rapid system check without loading agents.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Custom Sandfly to Suspend Malicious Linux Process During Incident](https://www.datocms-assets.com/56687/1635216312-sandfly-custom-suspend.png?auto=format&dpr=2&q=60&w=920 "Custom Sandfly to Suspend Malicious Linux Process During Incident")

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Custom Sandfly Suspends Malicious Linux Process](https://www.datocms-assets.com/56687/1635216319-process-suspend-explanation.png?auto=format&dpr=2&q=60&w=920 "Custom Sandfly Suspends Malicious Linux Process")

## Kill If You Want

Of course you can also kill a process if you want. This would be a useful option if you know for certain what is going on and want to try to remediate a bunch of systems with a known problem instantly. Sandfly can quickly go onto your hosts and kill the process with the parameters you supply. You can have Sandfly hunt for process names, environment variables it’s using, username of who started it, network connections it has open, etc. Any parameter can be used. When we get a match on these parameters we will kill the process (or suspend) as you’ve instructed.

## More Response Options Coming

Expect many more new and interesting response options for Sandfly in the coming updates. We have a lot of plans for this new capability to take automated Linux incident response to the next level.

## New Sandfly Category: Policy Checks

We have added a new type of check category called “policy.” Policy checks are not necessarily compromise checks, but are often serious mis-configurations that could result in compromise. Or, they could be leftover from Linux malware that altered a system to ensure it is persistent or can return and bypass security controls.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly Security Policy Checks](https://www.datocms-assets.com/56687/1635216326-sandfly-policy-scans.png?auto=format&dpr=2&q=60&w=920 "Sandfly Security Policy Checks")

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Permission Risk Detected on /etc/shadow](https://www.datocms-assets.com/56687/1635216334-sandfly-policy-file-permissions-risk-etc-shadow.png?auto=format&dpr=2&q=60&w=920 "Permission Risk Detected on /etc/shadow")

We have moved checks that looked for dangerous permissions on

You can also schedule policy checks to keep an eye on systems to make sure nothing changes that could be risky. For instance we check a variety of SSH configuration options that could enable dangerous tunnelling operations that could bypass firewalls and other network controls. These and other checks can be enabled to make sure your systems are not altered by users in dangerous ways.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH TCP Port Forwarding Security Risk Detected](https://www.datocms-assets.com/56687/1635216342-sandfly-policy-file-ssh-enabled-tcp-forwarding.png?auto=format&dpr=2&q=60&w=920 "SSH TCP Port Forwarding Security Risk Detected")

## Enhanced Host Operating System Details

We have enhanced the details we collect from remote systems. We now include many more details about the host operating system including easy to read distribution names, architecture names, etc.

Below we see the new columns showing distribution name, architecture, uptime and load. Also the new *os\_release* fields in the detailed data showing information about the remote system. This information is collected automatically and will be added to existing hosts without us...