---
title: How to Install SIFT Workstation and REMnux on the Same System
url: https://zeltser.com/sift-workstation-and-remnux
source: Lenny Zeltser
date: 2026-11-08
fetch_date: 2026-11-09T08:53:04.893868
---

# How to Install SIFT Workstation and REMnux on the Same System

[Skip to main content](#main-content)

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# How to Install SIFT Workstation and REMnux on the Same System

REMnux and SIFT Workstation together make a powerful toolkit for malware analysis, digital forensics, and incident response. Here's how to combine them into a unified super-toolkit.

![A pocket multitool lies fanned open on cream paper, printed in blue and amber inks. A magnifying lens, a brush and a flat probe in blue spread to the left. Tweezers, a needle probe, a small blade and a screwdriver in amber spread to the right, and all of them fold into one handle printed in both inks.](/assets/sift-workstation-and-remnux.Drg-QKBp_ZCpdSi.webp)

Having the right tools at your fingertips can save hours and even days when examining digital evidence or analyzing malicious artifacts. You can install two popular Linux distros, SIFT Workstation and [REMnux](https://remnux.org/), on the same system to create a powerful toolkit for computer forensics and malware analysis. [To quote Matt Bennett](https://x.com/ma77bennett/status/608770268765540352), this combo is reminiscent of “transformers combining together to form a super robot.”

You can start with SIFT and then add REMnux, or begin with REMnux and add SIFT to it.

## Option 1: Add REMnux to SIFT Workstation

If most of your work involves digital forensics and incident response tasks for which SIFT Workstation is designed, you’ll probably want to start with SIFT Workstation and add REMnux to it. The following approach will let you retain the standard SIFT Workstation look-and-feel, while giving you access to the REMnux malware analysis tools described in the [REMnux tool listing](https://docs.remnux.org/discover-the-tools/).

Begin with a version of SIFT running on Ubuntu 24.04. You can [download SIFT as a pre-built virtual appliance](https://www.sans.org/tools/sift-workstation) or use Cast to [install SIFT from scratch](https://github.com/teamdfir/sift-saltstack).

To add REMnux to your SIFT Workstation, boot into your SIFT system and make sure that it has internet access.

Before proceeding, make sure your system doesn’t have an active Ubuntu unattended upgrade in progress. One way to do this is to check whether the “unattended-upgrade” process is active (`pgrep -af /usr/bin/unattended-upgrade`). If the upgrade is active, let it finish, then reboot the system before installing REMnux.

Then, follow the steps on the REMnux documentation site to [add REMnux to the existing system](https://docs.remnux.org/install-distro/add-to-existing-system). This involves a few steps to download the REMnux installer and run it in the “addon” mode. Run the installer using the command:

```
sudo remnux install --mode=addon
```

![Adding REMnux to SIFT Workstation](/assets/add-remnux-to-sift-workstation.D8oWCLh9_Z1dwU7p.webp)

## Option 2: Add SIFT Workstation to REMnux

If you do more malware analysis than digital forensics, you’ll probably prefer to start with a REMnux system, then add SIFT Workstation. The following steps will allow you to keep the REMnux look-and-feel while benefiting from the forensics tools that come with SIFT Workstation.

Follow the installation instructions to set up your REMnux system, starting with a [pre-built REMnux virtual appliance](https://docs.remnux.org/install-distro/get-virtual-appliance) or using the REMnux installer to [install REMnux from scratch](https://docs.remnux.org/install-distro/install-from-scratch).

To add SIFT Workstation to your REMnux system, boot into your REMnux system and make sure that it has internet access. Then, follow the steps in the SIFT documentation to install [SIFT using Cast](https://github.com/teamdfir/sift-saltstack) in “server” mode. REMnux includes an older version of Cast, so you’ll update it first. Download the latest Cast .deb package for your system from the [Cast releases page](https://github.com/ekristen/cast/releases). Then, install that package and SIFT using these commands:

```
sudo dpkg -i cast-*.deb
sudo cast install --mode=server teamdfir/sift-saltstack
```

The SIFT installer might report failed states for a few tools that REMnux already includes, such as radare2 and ExifTool. You can ignore those messages, because the REMnux versions of these tools remain installed. After the SIFT installer finishes, reboot your system.

![Adding SIFT Workstation to REMnux](/assets/add-sift-workstation-to-remnux.BPfA93Rp_28nGQs.webp)

## Updating Your SIFT+REMnux System

To keep your system up to date with the upgraded and newly added software, periodically run the following commands for SIFT and REMnux:

```
remnux install
sudo cast install --mode=server teamdfir/sift-saltstack
```

If you added SIFT to REMnux, always include `--mode=server` in the SIFT command. Without it, Cast applies SIFT’s desktop settings to your REMnux system, including SIFT’s hostname, wallpaper, and dock layout. If you started with SIFT Workstation and added REMnux to it, use `--mode=desktop` instead.

The SIFT installer might report failed states for tools that REMnux already includes, such as radare2. You can ignore those messages, because the REMnux versions of these tools remain installed.

There you have it, two powerful security distros combined in one forensics and malware analysis super-toolkit!

Receive my blog posts by email.

Email address   Subscribe

### Related Articles

[![](/assets/malware-analysis-lab-remnux.Dxo0xpWX_1GiyxP.webp) Designing a Malware Analysis Lab With REMnux](/malware-analysis-lab-remnux)  [![](/assets/ai-assisted-malware-analysis-tips-preview.BShZhVRe_1HfnL6.webp) AI-Assisted Malware Analysis Tips](/ai-assisted-malware-analysis-tips)

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. He has built security products and programs from early stage to enterprise scale. He is also a Faculty Fellow at SANS Institute and the creator of REMnux, a popular Linux toolkit for malware analysis. Lenny shares his perspectives on security leadership and technology at [zeltser.com](/).

Get posts by email   Email address   Subscribe

  Copy link

More on

[Malware Analysis](/topic/malware-analysis)[Incident Response](/topic/incident-response)[REMnux](/topic/remnux)

This article was [originally published on the SANS Institute blog](https://www.sans.org/blog/how-to-install-sift-workstation-and-remnux-on-the-same-forensics-system).

3 min to read

November 8, 2026

   [Projects](/projects) [Writing](/writing) [About](/about) [Newsletter](/newsletter) [RSS](/rss.xml)

© 2026 [Lenny Zeltser](/)