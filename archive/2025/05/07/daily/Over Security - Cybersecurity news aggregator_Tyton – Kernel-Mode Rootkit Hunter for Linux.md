---
title: Tyton – Kernel-Mode Rootkit Hunter for Linux
url: https://www.darknet.org.uk/2025/04/tyton-kernel-mode-rootkit-hunter-for-linux/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-07
fetch_date: 2025-10-06T22:28:37.792065
---

# Tyton – Kernel-Mode Rootkit Hunter for Linux

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# Tyton – Kernel-Mode Rootkit Hunter for Linux

April 25, 2025

Views: 694

**Tyton** is a lightweight, open-source kernel-mode rootkit detection tool for Linux systems. Designed to identify stealthy kernel-level threats, Tyton offers a focused approach to uncovering hidden modules and system call table hooks.​

![Tyton - Kernel-Mode Rootkit Hunter for Linux](https://www.darknet.org.uk/wp-content/uploads/2025/04/Tyton-Kernel-Mode-Rootkit-Hunter-for-Linux-640x427.jpg)

### Key Features

* **Rootkit Detection**: Identifies hidden modules, syscall table hooks, and other common rootkit techniques.
* **User Notifications**: Includes a userland daemon that monitors journald logs and provides desktop notifications using libnotify.
* **DKMS Support**: Dynamic Kernel Module Support for seamless integration with kernel updates on distributions like Arch and Fedora.​

**Notifications**: Users (including myself) do not actively monitor their journald logs, so a userland notification daemon has been included to monitor journald logs and display them to the user using libnotify. Notifications are enabled after install by XDG autorun, so if your DM does not have `/etc/xdg/autostart` it will fail.

**DKMS**: Dynamic Kernel Module Support has been added for Arch and Fedora/CentOS (looking to expand in the near future). DKMS allows the (near) seamless upgrading of Kernel modules during kernel upgrades. This is mainly important for distributions that provide rolling releases or upgrade their kernel frequently.

### Installation

Linux Kernel 4.4.0-31 or greater

* Corresponding Linux Kernel Headers
* GCC
* Make
* Libnotify
* Libsystemd
* Package Config
* GTK3

To install: (be aware of above dependencies)

sudo apt install linux-headers-$(uname -r) gcc make libnotify-dev pkg-config libgtk-3-dev libsystemd-dev
git clone https://github.com/nbulischeck/tyton.git
cd tyton
make
sudo insmod tyton.ko

|  |  |
| --- | --- |
| 1  2  3  4  5 | sudo apt install linux-headers-$(uname -r) gcc make libnotify-dev pkg-config libgtk-3-dev libsystemd-dev  git clone https://github.com/nbulischeck/tyton.git  cd tyton  make  sudo insmod tyton.ko |

Note: For Ubuntu 14.04, replace `libsystemd-dev` with `libsystemd-journal-dev`.

### Considerations

* **Archived Project**: Tyton is no longer actively maintained; the repository is archived and read-only.
* **Kernel Compatibility**: May require adjustments for compatibility with newer kernel versions.
* **Limited Scope**: Focused solely on rootkit detection without broader intrusion detection capabilities.​

While Tyton provides a targeted approach to rootkit detection, its archived status and limited scope may necessitate exploring more actively maintained and comprehensive security tools for robust system protection.​

## Download Tyton Kernel-Mode Rootkit Hunter for Linux

<https://github.com/nbulischeck/tyton/releases/tag/v1.2>

## Related Posts:

* [Privacy Implications of Web 3.0 and Darknets](https://www.darknet.org.uk/2023/03/privacy-implications-of-web-3-0-and-darknets/)
* [APT-Hunter - Threat Hunting Tool via Windows Event Log](https://www.darknet.org.uk/2021/03/apt-hunter-threat-hunting-tool-via-windows-event-log/)
* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)
* [Falco - Real-Time Threat Detection for Linux and Containers](https://www.darknet.org.uk/2025/05/falco-real-time-threat-detection-for-linux-and-containers/)
* [Best Open Source HIDS Tools for Linux in 2025…](https://www.darknet.org.uk/2025/05/best-open-source-hids-tools-for-linux-in-2025-compared-ranked/)
* [Malvertising and TDS Cloaking Tactics Uncovered](https://www.darknet.org.uk/2025/07/malvertising-and-tds-cloaking-tactics-uncovered/)

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F04%2Ftyton-kernel-mode-rootkit-hunter-for-linux%2F)

[Tweet](https://twitter.com/intent/tweet?text=Tyton+-+Kernel-Mode+Rootkit+Hunter+for+Linux&url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F04%2Ftyton-kernel-mode-rootkit-hunter-for-linux%2F)

[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F04%2Ftyton-kernel-mode-rootkit-hunter-for-linux%2F)

[Buffer](https://bufferapp.com/add?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F04%2Ftyton-kernel-mode-rootkit-hunter-for-linux%2F&text=Tyton+-+Kernel-Mode+Rootkit+Hunter+for+Linux)

[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F04%2Ftyton-kernel-mode-rootkit-hunter-for-linux%2F)

[Email](/cdn-cgi/l/email-protection#82bdf1f7e0e8e7e1f6bfd6fbf6edeca7b0b2afa7b0b2c9e7f0ece7eeafcfede6e7a7b0b2d0ededf6e9ebf6a7b0b2caf7ecf6e7f0a7b0b2e4edf0a7b0b2ceebecf7faa4e0ede6fbbfd6fbf6edeca7b0b2ebf1a7b0b2e3a7b0b2eeebe5eaf6f5e7ebe5eaf6a7b0c1a7b0b2edf2e7ecaff1edf7f0e1e7a7b0b2e9e7f0ece7eeafefede6e7a7b0b2f0ededf6e9ebf6a7b0b2e6e7f6e7e1f6ebedeca7b0b2f6ededeea7b0b2e4edf0a7b0b2ceebecf7faa7b0b2f1fbf1f6e7eff1aca7b0b2c6e7f1ebe5ece7e6a7b0b2f6eda7b0b2ebe6e7ecf6ebe4fba7b0b2f1f6e7e3eef6eafba7b0b2e9e7f0ece7eeafeee7f4e7eea7b0b2f6eaf0e7e3f6f1a7b0c1a7b0b2d6fbf6edeca7b0b2ede4e4e7f0f1a7b0b2e3a7b0b2e4ede1f7f1e7e6a7b0b2e3f2f2f0ede3e1eaa7b0b2f6eda7b0b2f7ece1edf4e7f0ebece5a7b0b2eaebe6e6e7eca7b0b2efede6f7eee7f1a7b0b2e3ece6a7b0b2f1fbf1f6e7efa7b0b2e1e3eeeea7b0b2f6e3e0eee7a7b0b2eaedede9f1aca7c7b0a7bab2a7bac0a7b0b2c9e7fba7b0b2c4e7e3f6f7f0e7f1a7b0b2d0ededf6e9ebf6a7b0b2c6e7f6e7e1f6ebedeca7b1c3a7b0b2cbe6e7ecf6ebe4ebe7f1a7b0b2eaebe6e6e7eca7b0b2efede6f7eee7f1a7b0c1a7b0b2f1fbf1e1e3eeeea7b0b2f6e3e0eee7a7b0b2eaedede9f1a7b0c1a7b0b2e3ece6a7b0b2edf6eae7f0a7b0b2e1edefefedeca7b0b2f0ededf6e9ebf6a7b0b2f6e7e1eaecebf3f7e7f1aca7b0b2d7f1e7f0a7b0b2ccedf6ebe4ebe1e3f6ebedecf1a7b1c3a7b0b2cbece1eef7e6e7f1a7b0b2e3a7b0b2f7f1e7f0eee3ece6a7b0b2e6e3e7efedeca7b0b2f6eae3f6a7b0b2efedecebf6edf0f1a7b0b2e8edf7f0ece3eee6a7b0b2eeede5f1a7b0b2e3ece6a7b0b2f2f0edf4ebe6e7f1a7b0b2e6e7f1e9f6edf2a7b0b2ecedf6ebe4ebe1e3f6ebedecf1a7b0b2f7f1ebece5a7b0b2eeebe0ecedf6ebe4fbaca7b0b2c6c9cfd1a7b0b2d1f7f2f2edf0f6a7b1c3a7b0b2c6fbece3efebe1a7b0b2c9e7f0ece7eea7b0b2cfede6f7eee7a7b0b2d1f7f2f2edf0f6a7b0b2e4edf0a7b0b2f1e7e3efeee7f1f1a7b0b2ebecf6e7e5f0e3f6ebedeca7b0b2f5ebf6eaa7b0b2e9e7f0ece7eea7b0b2f7f2e6e3f6e7f1a7b0b2edeca7b0b2e6ebf1f6f0ebe0f7f6ebedecf1a7b0b2eeebe9e7a7b0b2c3f0e1eaa7b0b2e3ece6a7b0b2c4e7e6edf0e3aca7c7b0a7bab2a7bac0a7b0b2ccedf6ebe4ebe1e3f6ebedecf1a7b1c3a7b0b2d7f1e7f0f1a7b0b2a7b0baebece1eef7e6ebece5a7b0b2effbf1e7eee4a7b0bba7b0b2e6eda7b0b2ecedf6a7b0b2e3e1f6ebf4e7eefba7b0b2efedecebf6edf0a7b0b2f6eae7ebf0a7b0b2e8edf7f0ece3eee6a7b0b2eeede5f1a7b0c1a7b0b2f1eda7b0b2e3a7b0b2f7f1e7f0eee3ece6a7b0b2ecedf6ebe4ebe1e3f6ebedeca7b0b2e6e3e7efedeca7b0b2eae3f1a7b0b2e0e7e7eca7b0b2ebece1eef7e6e7e6a7b2c6a7b2c3a7b2c6a7b2c3d0e7e3e6a2cfedf0e7a2cae7f0e7b8a2a7b0b2eaf6f6f2f1a7b1c3a7b0c4a7b0c4f5f5f5ace6e3f0e9ece7f6acedf0e5acf7e9a7b0c4b0b2b0b7a7b0c4b2b6a7b0c4f6fbf6edecafe9e7f0ece7eeafefede6e7aff0ededf6e9ebf6afeaf7ecf6e7f0afe4edf0afeeebecf7faa7b0c4)

Filed Under: [Linux Hackin...