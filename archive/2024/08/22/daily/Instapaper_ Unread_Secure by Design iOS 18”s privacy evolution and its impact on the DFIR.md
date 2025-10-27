---
title: Secure by Design iOS 18”s privacy evolution and its impact on the DFIR
url: https://andreafortuna.org/2024/08/20/secure-by-design-ios-18-s-privacy-evolution-and-its-impact-on-the-dfir.html
source: Instapaper: Unread
date: 2024-08-22
fetch_date: 2025-10-06T18:06:04.715283
---

# Secure by Design iOS 18”s privacy evolution and its impact on the DFIR

[Andrea Fortuna](/)
[ ]

[About](/about/)[Rss](/feed.xml)

# Secure by Design: iOS 18's privacy evolution and its impact on the DFIR

Aug 20, 2024

As digital forensics experts, we constantly find ourselves in a technological arms race. On one side, we have device manufacturers and software developers continuously enhancing privacy and security features. On the other, we have the need to access and analyze digital evidence for legitimate investigative purposes. The upcoming release of iOS 18 marks another significant milestone in this ongoing battle, introducing a suite of privacy features that will undoubtedly reshape the landscape of digital forensics and incident response (DFIR).

![image](https://github.com/user-attachments/assets/95f5dfe7-38ba-43f7-84c6-1595f593f8ef)

In this article, we’ll dive deep into the new features of iOS 18, explore their implications for DFIR professionals, and discuss potential strategies and tools to navigate these challenges. It’s important to note that as of the time of writing, iOS 18 is still in beta, and some features may change before the final release. However, the trends we’re seeing give us a clear indication of the direction Apple is taking with user privacy.

## Locked and Hidden apps: a new digital vault

One of the most significant changes in iOS 18 is the introduction of locked and hidden apps. This feature allows users to secure any app on their device behind Face ID, Touch ID, or a passcode, even when the iPhone itself is unlocked. Additionally, users can now hide apps from the home screen, placing them in a hidden folder that also requires authentication to access.

### DFIR Implications

This new feature presents a considerable challenge for digital forensics experts. Previously, once a device was unlocked, investigators had relatively unrestricted access to all installed apps and their data. With iOS 18, we’re facing a scenario where critical evidence could be locked away behind additional authentication barriers.

#### Challenges:

* Difficulty in identifying hidden apps
* Additional authentication requirements for accessing locked apps
* Potential for users to claim plausible deniability about the existence of certain apps

#### Potential Solutions:

1. **Advanced extraction techniques**: Tools like [Cellebrite UFED](https://www.cellebrite.com/en/ufed/) or [Magnet AXIOM](https://www.magnetforensics.com/products/magnet-axiom/) may need to be updated to bypass or crack these additional security layers.
2. **Legal avenues**: In some cases, investigators may need to obtain additional warrants or court orders specifically for accessing locked or hidden apps.
3. **Behavioral analysis**: Focus on analyzing device logs, network traffic, and other metadata that might indicate the presence and usage of hidden apps.
4. **Social engineering**: In cases where it’s legally permissible, interviewing techniques might be employed to obtain authentication information from the device owner.

## Improved contacts permission

iOS 18 introduces granular control over contact sharing, allowing users to selectively share contacts with apps instead of granting access to their entire contact list. This feature enhances user privacy but creates new challenges for digital forensics.

### DFIR Implications

The selective sharing of contacts means that investigators may only get a partial view of a user’s interactions when examining app data. This fragmented data landscape can make it more difficult to piece together comprehensive communication patterns.

#### Challenges:

* Incomplete contact lists within apps
* Difficulty in establishing comprehensive communication networks
* Potential for missing key connections in investigations

#### Potential Solutions:

1. **Cross-referencing data**: Utilize tools like [Oxygen Forensic Detective](https://www.oxygen-forensic.com/en/products/oxygen-forensic-detective) to cross-reference data from multiple sources, including call logs, messaging apps, and email clients.
2. **Timeline analysis**: Focus on creating comprehensive timelines using tools like [Autopsy](https://www.autopsy.com/) to identify patterns and connections that might not be immediately apparent from contact lists alone.
3. **Network analysis**: Employ tools like [IBM i2 Analyst’s Notebook](https://www.ibm.com/products/i2-analysts-notebook) to visualize and analyze communication patterns based on available data, even if contact information is incomplete.
4. **Metadata analysis**: Pay closer attention to metadata from communications, which might reveal information about contacts even if they’re not explicitly shared with an app.

## The new passwords app

iOS 18 introduces a dedicated Passwords app that centralizes the storage of iCloud Keychain logins, passwords, passkeys, Wi-Fi passwords, and verification codes. This consolidation of sensitive information presents both opportunities and challenges for digital forensics experts.

### DFIR Implications

The Passwords app could potentially be a goldmine of information for investigators, providing access to a user’s digital life across multiple platforms and services. However, it’s also likely to be one of the most securely protected features on the device.

#### Challenges:

* High-security measures protecting the Passwords app
* Potential encryption of stored passwords and keys
* Legal and ethical considerations in accessing this highly sensitive data

#### Potential Solutions:

1. **Specialized extraction tools**: Look for updates to tools like Elcomsoft iOS Forensic Toolkit [https://www.elcomsoft.com/eift.html] that might provide methods for accessing the Passwords app data.
2. **Cloud-based extraction**: If iCloud backups are available and accessible, tools like [Magnet AXIOM Cloud](https://www.magnetforensics.com/products/magnet-axiom-cyber/) might be able to extract password data synced to iCloud.
3. **Memory analysis**: In some cases, it might be possible to extract passwords from the device’s RAM using tools like [Belkasoft RAM Capturer](https://belkasoft.com/ram-capturer).
4. **Legal procedures**: Given the sensitive nature of this data, it’s crucial to ensure proper legal authorization before attempting to access the Passwords app. Consultation with legal experts and obtaining specific warrants may be necessary.

## Private Cloud Compute: privacy in the Cloud

iOS 18 extends Apple’s privacy protections into the cloud with Private Cloud Compute for more complex requests. This feature ensures that even when data processing occurs in the cloud, it remains protected and private.

### DFIR Implications

Private Cloud Compute poses significant challenges for digital forensics experts, as it may put certain types of data and processing out of reach.

#### Challenges:

* Difficulty in accessing cloud-processed data
* Potential loss of valuable metadata typically associated with cloud processing
* Increased complexity in tracking user activities that involve cloud compute

#### Potential Solutions:

1. **Focus on device-resident data**: Tools like [BlackBag BlackLight](https://www.blackbagtech.com/blacklight/) can help extract and analyze data stored locally on the device.
2. **Legal avenues for cloud data**: Work with legal teams to explore possibilities of obtaining warrants for cloud-stored data, even if it’s processed privately.
3. **Network traffic analysis**: Use tools like [Wireshark](https://www.wireshark.org/) to analyze network traffic and potentially infer information about cloud compute activities.
4. **Forensic triage**: Employ triage tools like [ADF Digital Evidence Investigator](https://www.adfsolutions.com/digital-evidence-investigator) to quickly identify and prioritize relevant data sources on the device.

## On-Device Processing: When Data Stays Home

iOS 18 continues the trend of on-device processing for many AI models powering Apple Intelligence. This approach enhances user privacy by reducing data transmission to the cloud but creates new challenges ...