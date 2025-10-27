---
title: ReVault! When your SoC turns against you…
url: https://blog.talosintelligence.com/revault-when-your-soc-turns-against-you/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-06
fetch_date: 2025-10-07T00:59:54.682858
---

# ReVault! When your SoC turns against you…

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

# ReVault! When your SoC turns against you…

By
[Philippe Laulheret](https://blog.talosintelligence.com/author/philippe/)

Tuesday, August 5, 2025 09:00

[Vulnerability Spotlight](https://blog.talosintelligence.com/category/vulnerability-spotlight/)

* Talos reported 5 vulnerabilities to Broadcom and Dell affecting both the ControlVault3 Firmware and its associated Windows APIs that we are calling “ReVault”.
* 100+ models of Dell Laptops are affected by this vulnerability if left unpatched.
* The ReVault attack can be used as a post-compromise persistence technique that can remain even across Windows reinstalls.
* The ReVault attack can also be used as a physical compromise to bypass Windows Login and/or for any local user to gain Admin/System privileges.
* For a full technical deep dive into these vulnerabilities, see [this blog post](https://blog.talosintelligence.com/revault-when-your-soc-turns-against-you-2).

# Dell ControlVault overview

[Dell ControlVault](https://www.dell.com/support/home/en-vc/drivers/driversdetails?driverid=twf65) is “a hardware-based security solution that provides a secure bank that stores your passwords, biometric templates, and security codes within the firmware.” A daughter board provides this functionality and performs these security features in firmware. Dell refers to the daughter board as a Unified Security Hub (USH), as it is used as a hub to run ControlVault (CV), connecting various security peripherals such as a fingerprint reader, smart card reader and NFC reader.

Here is a photographic example of a USH board:  ​​​​

![](https://blog.talosintelligence.com/content/images/2025/08/ush_board.png)

Picture of a USH Board running CV.

This is the board in its natural environment:

![](https://blog.talosintelligence.com/content/images/2025/08/laptop_open2_final.png)

USH board (highlighted in orange) inside a Dell Latitude laptop.

The current iterations of the product are called ControlVault3 and ControlVault3+. and can be found in more than 100 different models of actively-supported Dell laptops (see [DSA-2025-053](https://www.dell.com/support/kbdoc/en-us/000276106/dsa-2025-053)), mostly from the business-centric Lattitude and Precision series. These laptop models are widely used in the cybersecurity industry, government settings and challenging environments in their Rugged version. Sensitive industries that require heightened security when logging in (via smartcard or NFC) are more likely to find ControlVault devices in their environment, as they are necessary to enable these security features.

# Findings

Today, Talos is publishing five CVEs and their associated reports. The vulnerabilities include multiple out-of-bounds vulnerabilities (CVE-2025-24311, CVE-2025-25050) an arbitrary free (CVE-2025-25215) and a stack-overflow (CVE-2025-24922), all affecting the CV firmware. We also reported an unsafe-deserialization (CVE-2025-24919) that affects ControlVault’s Windows APIs.

# Impact

With a lack of common security mitigations and the combination of some of the vulnerabilities mentioned above, the impact of these findings is significant. Let’s highlight two of the most critical attack scenarios we have uncovered.

![Picture 108763978, Picture](https://blog.talosintelligence.com/content/images/2025/08/data-src-image-6df4043a-5652-4b88-bf67-d203a77ca08a.jpeg)

## Post-compromise pivot

On the Windows side, a non-administrative user can interact with the CV  firmware using its associated APIs and trigger an Arbitrary Code Execution on the CV firmware. From this vantage point, it becomes possible to leak key material essential to the security of the device, thus gaining the ability to permanently modify its firmware. This creates the risk of a so-called implant that could stay unnoticed in a laptop’s CV firmware and eventually be used as a pivot back onto the system in the case of a Threat Actor’s post-compromise strategy. The following video shows how a tampered CV firmware can be used to “hack Windows” by leveraging the unsafe deserialization bug mentioned previously.

[![](https://img.spacergif.org/v1/1920x1080/0a/spacer.png)](https://blog.talosintelligence.com/content/media/2025/08/bcm_demo4.mp4)

0:00

/0:22

1×

## Physical attack

A local attacker with physical access to a user’s laptop can pry it open and directly access the USH board over USB with a custom connector. From there, all the vulnerabilities described previously become in-scope for the attacker without requiring the ability to log-in into the system or knowing a full-disk encryption password. While chassis-intrusion can be detected, this is a feature that needs to be enabled beforehand to be effective at warning of a potential tampering.

Another interesting consequence of this scenario is that if a system is configured to be unlocked with the user’s fingerprint, it is also possible to tamper with the CV firmware to accept any fingerprint rather than only allowing a legitimate user’s.

[![](https://img.spacergif.org/v1/1920x1080/0a/spacer.png)](https://blog.talosintelligence.com/content/media/2025/08/demo_fingerprint2_resized.mp4)

0:00

/0:07

1×

# Remediation

## Mitigation

To mitigate these attacks, Talos recommends the following:

* Keep your system up to date to ensure the latest firmware is installed. CV firmware can be automatically deployed via Windows Update, but new firmware usually gets released on the Dell website a few weeks prior.
* If not using any of the security peripherals (fingerprint reader, smart card reader and NFC reader) it is possible to disable the CV services (using the Service Manager) and/or the CV device (via the Device Manager).
* It is also worth considering disabling fingerprint login when risks are heightened (e.g., leaving one’s laptop unattended in a hotel room). Windows also provides Enhanced Si...