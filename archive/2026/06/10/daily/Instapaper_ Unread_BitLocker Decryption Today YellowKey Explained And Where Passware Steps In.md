---
title: BitLocker Decryption Today YellowKey Explained And Where Passware Steps In
url: https://www.forensicfocus.com/news/bitlocker-decryption-today-yellowkey-explained-and-where-passware-steps-in/
source: Instapaper: Unread
date: 2026-06-10
fetch_date: 2026-06-11T06:37:00.520037
---

# BitLocker Decryption Today YellowKey Explained And Where Passware Steps In

[Skip to content](#content "Skip to content")

* [Login/Register](https://www.forensicfocus.com/sign-in/?redirect_to=https%3A%2F%2Fwww.forensicfocus.com%2Fnews%2Fbitlocker-decryption-today-yellowkey-explained-and-where-passware-steps-in%2F)

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/themes/generatepress_child/assets/images/logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

[Login](/sign-in/)
[Register](/sign-up/)

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/uploads/2020/05/forensic-focus_logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

Menu

* [News](https://www.forensicfocus.com/news/)
* Community
  + [Forums](https://www.forensicfocus.com/forums/)
  + [Discord (Invite)](https://discord.gg/97zKvTXHeS)
* Resources
  + [Newsletter](https://www.forensicfocus.com/newsletter/)
  + [Articles](https://www.forensicfocus.com/articles/)
  + [Reviews](https://www.forensicfocus.com/reviews/)
  + [Webinars](https://www.forensicfocus.com/webinars/)
  + [Podcast](https://www.forensicfocus.com/podcast/)
  + [Interviews](https://www.forensicfocus.com/interviews/)
  + [Videos](https://www.forensicfocus.com/videos/)
  + [Case Studies](https://www.forensicfocus.com/case-studies/)
  + [Well-Being](https://www.forensicfocus.com/well-being/)
  + [Guides](https://www.forensicfocus.com/guides/)
  + [Useful Links](https://www.forensicfocus.com/useful-links/)
  + [Digital Forensics Timeline](https://www.forensicfocus.com/digital-forensics-timeline/)
* Jobs & Careers
  + [View jobs](https://www.forensicfocus.com/jobs/)
  + [How To Start A Career In Digital Forensics](https://www.forensicfocus.com/articles/how-to-start-a-career-in-digital-forensics/)
* Education
  + [Course Listings](https://www.forensicfocus.com/education/)
  + [Education & Training Guide](https://www.forensicfocus.com/articles/digital-forensics-education-certification-and-training-guide/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](https://www.forensicfocus.com/event-info/)

Menu

* [News](https://www.forensicfocus.com/news/)
* Community
  + [Forums](https://www.forensicfocus.com/forums/)
  + [Discord (Invite)](https://discord.gg/97zKvTXHeS)
* Resources
  + [Newsletter](https://www.forensicfocus.com/newsletter/)
  + [Articles](https://www.forensicfocus.com/articles/)
  + [Reviews](https://www.forensicfocus.com/reviews/)
  + [Webinars](https://www.forensicfocus.com/webinars/)
  + [Podcast](https://www.forensicfocus.com/podcast/)
  + [Interviews](https://www.forensicfocus.com/interviews/)
  + [Videos](https://www.forensicfocus.com/videos/)
  + [Case Studies](https://www.forensicfocus.com/case-studies/)
  + [Well-Being](https://www.forensicfocus.com/well-being/)
  + [Guides](https://www.forensicfocus.com/guides/)
  + [Useful Links](https://www.forensicfocus.com/useful-links/)
  + [Digital Forensics Timeline](https://www.forensicfocus.com/digital-forensics-timeline/)
* Jobs & Careers
  + [View jobs](https://www.forensicfocus.com/jobs/)
  + [How To Start A Career In Digital Forensics](https://www.forensicfocus.com/articles/how-to-start-a-career-in-digital-forensics/)
* Education
  + [Course Listings](https://www.forensicfocus.com/education/)
  + [Education & Training Guide](https://www.forensicfocus.com/articles/digital-forensics-education-certification-and-training-guide/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](https://www.forensicfocus.com/event-info/)

[Home](https://www.forensicfocus.com/) » [News](https://www.forensicfocus.com/news/) » BitLocker Decryption Today: YellowKey Explained And Where Passware Steps In

# BitLocker Decryption Today: YellowKey Explained And Where Passware Steps In

9th June 2026 by [Passware](https://www.forensicfocus.com/author/passware/ "View all posts by Passware")

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/06/2026-06-08_6a26e43c906d6_img-1.png)

With YellowKey getting a lot of attention in the forensics community, let us explain what it actually is, how it works, and what your options are when it doesn’t.

## What is YellowKey?

In simple terms, YellowKey is an exploit for BitLocker decryption that leverages a security vulnerability in the Windows Recovery Environment (WinRE). It allows an examiner to open a command prompt within WinRE and retrieve the BitLocker Recovery Key, granting instant access to a BitLocker-encrypted volume protected with TPM.

The YellowKey file was publicly available on GitHub until it was removed on May 26, 2026. While the original repository is no longer accessible, the file can still be downloaded from the [archived version of the page](https://web.archive.org/web/20260521160319/https%3A//github.com/Nightmare-Eclipse/YellowKey).

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/06/img-2.png)

## How It Works

Windows Recovery Environment (WinRE) is a Microsoft tool designed to help recover a system after a crash or failure. Its core component is the **winre.wim** file – a compact Windows OS image that loads when the system boots into recovery mode.

On computers with BitLocker full-disk encryption, WinRE operates the same way. When the default protection is used (TPM only), BitLocker decryption happens automatically during WinRE startup, without prompting the user for credentials. To prevent attackers with physical access to the computer from abusing this, Microsoft implemented the Trusted WIM Boot mechanism, which blocks custom code from running inside WinRE.

## Get The Latest DFIR News

### Join the Forensic Focus newsletter for the best DFIR articles in your inbox every month.

Unsubscribe any time. We respect your privacy - read our [privacy policy](/privacy-policy).

Leave this field empty if you're human:

Trusted WIM Boot works as follows:

1. When BitLocker is enabled, it generates two keys: the FVEK (Full Volume Encryption Key), which directly encrypts the partition data, and the VMK, which encrypts the FVEK. The VMK is in turn protected by one or more key protectors (such as the TPM with PIN or a Recovery Key). [Learn more about the basic principles of BitLocker encryption](https://blog.passware.com/bitlocker-decryption-explained/).
2. The system computes a hash of the winre.wim file (let’s name it winre\_digest) located in the Recovery partition at:\Recovery\WindowsRE\winre.wim This hash is used to verify the integrity of the Windows Recovery Environment. For the verification routine to pass, the hash should be updated every time WinRE changes.
3. The winre\_digest hash is saved in BitLocker metadata located on the protected partition. The record has entry type “0x11” with value type “0x07” (FVE\_DATUM\_VALIDATION\_INFO).
4. Using the VMK, the system computes the meta\_authentication\_tag of BitLocker metadata, which includes the VALIDATION\_INFO record with thewinre\_digest.

**In summary**: when the computer boots into Windows Recovery, the bootloader **bootmgfw.efi** retrieves the VMK from the TPM, then verifies the integrity of the WinRE image by checking the **meta\_authentication\_tag** and comparing the hash of **winre.wim** against the **winre\_digest** value stored in the protected partition’s metadata. If the hashes do not match, the VMK is securely erased from memory. This means that any modification to (or substitution of) the **winre.wim** file will block access to the protected partition in WinRE.

It is worth noting that BitLocker’s integrity verification operates independently of the configured PCR bitmap – the VMK can be unsealed against both profiles: (7, 11) and (0, 2, 4, 11).

YellowKey exploits a vulnerability in the **winre.wim** images of Windows 11 and Windows Server 2022/2025. It allows compromising the **winre.wim** image without changing its contents, thereby passing the integrity check and enabling code execution in the Windows Recovery Environment, for example, running **cmd.exe**. The attack works as follows: because the **winre.wim** hash still matches t...