---
title: Evil Maid Attacks - Remediation for the Cheap, (Wed, Nov 16th)
url: https://isc.sans.edu/diary/rss/29256
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-17
fetch_date: 2025-10-03T23:02:30.989746
---

# Evil Maid Attacks - Remediation for the Cheap, (Wed, Nov 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29252)
* [next](/diary/29260)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Evil Maid Attacks - Remediation for the Cheap](/forums/diary/Evil%2BMaid%2BAttacks%2BRemediation%2Bfor%2Bthe%2BCheap/29256/)

**Published**: 2022-11-16. **Last Updated**: 2022-11-16 18:15:23 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Evil%2BMaid%2BAttacks%2BRemediation%2Bfor%2Bthe%2BCheap/29256/#comments)

[This is a guest diary submitted by Gebhard. For feedback, you can connect with Gebhard via our [DShield slack](https://isc.sans.edu/slack/index.html)]

### Preliminary note

In this diary, we are assuming PC-like devices with state-of-the-art disk encryption (full disk encryption, FDE) and a "normal" desktop OS (Linux, Windows, ...).

### What is the evil maid attack?

The so-called evil maid attack is an attack against hardware devices utilizing hard- and/or software. It is carried out when the hardware is left unattended, e.g., in a hotel room when you're out for breakfast. The attacker manipulates the device in a malicious way, e.g.:

* if the device is running: cool down and take out RAM to copy it (e.g., to find sensitive information)
* manipulate the mainboard / BIOS (e.g., to add a backdoor)
* manipulate the content from the unencrypted bootloader (e.g., to add a backdoor)

The last attack may even work with secure boot enabled because of 0-day vulnerabilities in the signed boot code or known vulnerabilities in the signed boot code, which is not disabled due to outdated revocation lists in the BIOS.

### Your possible options

There are several ways to minimize the risk of an unnoticed, successful evil maid attack. Which road you go depends on your personal threat model (and your budget, of course).

1. Take the risk

   If evil maid attacks do not matter in your situation, e.g., because you're using a disposable device that is already assumed to be compromised, then you can simply take the risk.
2. Adequate hardware

   You can buy (or prepare yourself) special hardened devices (e.g. NitroPad) which make evil maid attacks nearly impossible to go undetected:

   * sealed screws
   * alternate BIOS/firmware (Coreboot (https://www.coreboot.org/) and Heads (https://osresearch.net/FAQ/))
   * deactivated Intel Management Engine
   * hardware key for checking signatures/integrity of boot files with your personal PGP key
   * full disk encryption

   These devices make the boot process more trustworthy than using stock consumer hardware:

   * Solely open-source BIOS and firmware code
   * boot code signed with your personal PGP key stored on a USB hardware device and only attached temporarily to the system to carry out the signature checks
   * full disc encryption
   * optional (but cool ? ): Qubes OS
3. Leave your device up and running

   If you leave your device running the OS on the one hand, you would probably notice if the device got turned out or rebooted: you may e.g., just have an editor open with some individual unsaved text and the screen locked. But on the other hand with a running OS you have a very broad attack surface because all device functionality is active (e.g., peripheral interfaces). So an attacker may e.g. add a USB LAN card and mess with the system trying to connect to the LAN controlled by the attacker. Or the three-letter agency can apply the publicly unknown exploit for the next 0-Day of the OS or a driver.
4. Remediation for the cheap

   If you want to have a cheap solution to be reasonably sure nobody messes unnoticed with your device when you have to leave it alone, you may carry out some countermeasures, e.g.:

   * seal all screws with nail polish or glue with glitter pieces in it, and take pictures that are stored offline so that you will be able to spot manipulations
   * seal not needed peripheral interfaces (e.g. USB ports)
   * lock needed peripheral ports with tamper-proof solutions (e.g. one-time locks which have to be destroyed to access the port)
   * Leave the device in the bootup password prompt of the FDE:
     1. (re-) boot your device to the FDE password prompt
     2. and enter the first few chars of the correct password (important!)
     3. make sure the device stays in this mode till you return (e.g. has enough power or the power supply is plugged in, disable energy saving settings, ...)

   When you're back, enter the rest of the FDE password, and if the device boots, then you could be reasonably sure it hasn't been tampered with. Of course, you have to examine the device physically thoroughly, e.g., the screws, peripheral ports, seals, etc. One important precondition for this to work is that the FDE boot code allows the password prompt to stay as it is after entering some chars. Fedora 7 and Ubuntu 20.04 seem to work, but Bitlocker (Windows) does not. Is this bulletproof? No. Will this be reasonably secure? Depends on your threat model. But it's definitely better than doing nothing, having the OS left up and running, or having the device powered off completely. Stay safe and secure!

Feel free to send in your own tips and hints.

Keywords:

[1 comment(s)](/diary/Evil%2BMaid%2BAttacks%2BRemediation%2Bfor%2Bthe%2BCheap/29256/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29252)
* [next](/diary/29260)

### Comments

Interesting, however since the proposed technique still require checking the hardware for signs of tampering, one might choose to rely on hardware protections alone.

In addition to sealing the screws, the tamper switch present on enterprise models could be activated and possibly beefed up (e.g. by adding additional contact points across the case, like in the 2017 ORWL case), possibly sacrificing serviceability if security is very important. Hardening commercial models in such manner might become a third party service or a purchase option. The screen lid should also be hardened in such a manner, as it manages both image and USB (webcam), though it might prove difficult as an attacker might just break everything but the cables and install a trojanized new one.

For the sake of discussing, I believe Bitlocker (aside from timing out) also stores the FDE key in the TPM and unlocks it automatically via secure boot, loading the operating system before asking the user for his/her password. That would leave the machine vulnerable to OS vulnerabilities (like mentioned earlier in the article). Once Windows 7 also had a bug where an administrator prompt could be obtained before entering the password in safe mode!).
Hardware disk FDE passwords requested directly by the BIOS on the other hand usually timeout after a few minutes.

Maybe an effective, cheap and simple control against evil maid attacks might be a special tamper-proof bag (e.g. one with woven with electric wires connected to a intelligent sensor recording resistance variations).

Interesting, however since the proposed technique still require checking the hardware for signs of tampering, one might choose to rely on hardware protections alone.

In addition to sealing the screws, the tamper switch present on enterprise models could be activated and possibly beefed up (e.g. by adding additional contact points across the case, like in the 2017 ORWL case), possibly fully sacrificing ...