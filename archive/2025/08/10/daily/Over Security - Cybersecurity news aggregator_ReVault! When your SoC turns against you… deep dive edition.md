---
title: ReVault! When your SoC turns against you… deep dive edition
url: https://blog.talosintelligence.com/revault-when-your-soc-turns-against-you-2/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-10
fetch_date: 2025-10-07T00:18:29.590669
---

# ReVault! When your SoC turns against you… deep dive edition

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# ReVault! When your SoC turns against you… deep dive edition

By
[Philippe Laulheret](https://blog.talosintelligence.com/author/philippe/)

Saturday, August 9, 2025 09:00

[Vulnerability Deep Dive](https://blog.talosintelligence.com/category/vulnerability-deep-dive/)

For a high-level overview of this research, you can refer to our [Vulnerability Spotlight](https://blog.talosintelligence.com/revault-when-your-soc-turns-against-you/). This is the in-depth version that shares many more technical details. In this post, we’ll be covering the entire research process as well as providing technical explanations of the exploits behind the attack scenarios.

[Dell ControlVault](https://www.dell.com/support/home/en-vc/drivers/driversdetails?driverid=twf65) is “a hardware-based security solution that provides a secure bank that stores your passwords, biometric templates, and security codes within the firmware.” A daughter board provides this functionality and performs these security features in firmware. Dell refers to the daughter board as a Unified Security Hub (USH), as it is used as a hub to run ControlVault (CV), connecting various security peripherals such as a fingerprint reader, smart card reader and NFC reader.

# Why target ControlVault3?

Hindsight is 20/20 and in retrospect, there are plenty of valid reasons to look at it:

* There is no public research on this device.
* It is used for security and enhanced logins and thus is used for sensitive functions.
* It is found in countless Dell laptops and, in particular, places that seek this extra layer of security (e.g., finance, healthcare, government, etc.) are more likely to have it in their environment.

But what really kickstarted this research project was spotting this target that seemed “promising.” What first caught our attention is that most of the Windows services involved with ControlVault3 are not Address Space Layout Randomization (ASLR)-enabled. This means easier exploitation, and possible technical debt in the codebase. Further, the setup bundle comes with multiple drivers and what appears to be a mix of clear text and encrypted firmware. This makes for an exciting challenge that calls for further investigation.

## Making a plan

When starting a vulnerability research project, it is good to have some ideas of what we’re trying to achieve. Let’s make a plan that will act as our North Star and guide our steps along the way:

1. The main application is encrypted, and we want to see what this firmware hides. One of our first tasks should be to find a way to decrypt the application firmware.
2. This is a vulnerability research project and, as such, we need to understand how to interact with Control Vault, understand its attack surface, and look for vulnerabilities.
3. The Windows services run without ASLR and have SYSTEM privileges. Those could be standalone targets for local escalation of privilege (EoP) and/or may have interesting exploitation paths.

## Gathering information

Information gathering occurred throughout the project. However, to clarify this discussion, we’ll now summarize some of the early findings.

ControlVault is made by Broadcom and leverages their [5820X chip series](https://www.broadcom.com/products/embedded-and-networking-processors/secure/bcm5820x). Technically, we are only talking about ControlVault3 (or ControlVault3+), but there was a ControlVault2 and a ControlVault (1 being implied) that were using different hardware. The first mentions of ControlVault date back to 2009-2011.

Online research for the BCM5820X chip series yields minimal results, with this [NIST certification](https://csrc.nist.gov/CSRC/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp3920.pdf) being the only notable finding. This document clarifies the security posture of the chip and gives some insight into the operations of its cryptographic module.

Other useful resources are forum posts where power users talk about Control Vault, particularly when the power users discuss making it work on Linux. One post eventually lead to a [repository](https://git.launchpad.net/~oem-solutions-engineers/libfprint-2-tod1-broadcom/%2Bgit/libfprint-2-tod1-broadcom/) providing official (but limited) Linux support. It is worth noting that one of the shared objects in this repository, “libfprint-2-tod-1-broadcom.so”, ships with debug symbols. This can help when reversing the ControlVault ecosystem.

Finally, for a physical representation, the USH board that connects to the laptop and runs the ControlVault firmware is shown below:

![](https://blog.talosintelligence.com/content/images/2025/08/image.png)

Figure 1: Picture of a USH Board running ControlVault.

When connected inside the laptop, it looks like this (battery removed to show the board):

![](https://blog.talosintelligence.com/content/images/2025/08/image-1.png)

Figure 2: USH board (highlighted in orange) inside a Dell Latitude laptop.

## Interesting files in ControlVault3 bundle

ControlVault comes with a lot of files. We cannot look at all of them at once, but there are a few that stick out, mainly the “bin” and “firmware” folders. The former contains the main services used to communicate with ControlVault and the associated shared objects, while the latter is used to push data to the device.

![](https://blog.talosintelligence.com/content/images/2025/08/BinFwFolders.png)

**Figure 3: Bin and firmware folders from the ControlVault3 installer.**

The firmware folder is also particularly interesting as it contains what we can presume is the code running on the ControlVault device. If we look at the content of these files by running the “strings” command or by opening them in a hex editor, we find that the ones with “SBI” in their names are in plaintext, while the ones named “bcmCitadelXXX” appear to b...