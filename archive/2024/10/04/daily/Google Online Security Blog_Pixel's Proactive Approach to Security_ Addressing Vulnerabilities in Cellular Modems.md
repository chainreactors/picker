---
title: Pixel's Proactive Approach to Security: Addressing Vulnerabilities in Cellular Modems
url: http://security.googleblog.com/2024/10/pixel-proactive-security-cellular-modems.html
source: Google Online Security Blog
date: 2024-10-04
fetch_date: 2025-10-06T18:46:31.232635
---

# Pixel's Proactive Approach to Security: Addressing Vulnerabilities in Cellular Modems

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Pixel's Proactive Approach to Security: Addressing Vulnerabilities in Cellular Modems](https://security.googleblog.com/2024/10/pixel-proactive-security-cellular-modems.html "Pixel's Proactive Approach to Security: Addressing Vulnerabilities in Cellular Modems")

October 3, 2024

Posted by Sherk Chung, Stephan Chen, Pixel team, and Roger Piqueras Jover, Ivan Lozano, Android team

Pixel phones have earned a well-deserved reputation for being security-conscious. In this blog, we'll take a peek under the hood to see how Pixel mitigates common exploits on cellular basebands.

Smartphones have become an integral part of our lives, but few of us think about the complex software that powers them, especially the cellular baseband – the processor on the device responsible for handling all cellular communication (such as LTE, 4G, and 5G). Most smartphones use cellular baseband processors with tight performance constraints, making security hardening difficult. Security researchers have increasingly exploited this attack vector and routinely demonstrated the possibility of exploiting basebands used in popular smartphones.

The good news is that Pixel has been deploying security hardening mitigations in our basebands for years, and Pixel 9 represents the most hardened baseband we've shipped yet. Below, we’ll dive into why this is so important, how specifically we’ve improved security, and what this means for our users.

**The Cellular Baseband**

The cellular baseband within a smartphone is responsible for managing the device's connectivity to cellular networks. This function inherently involves processing external inputs, which may originate from untrusted sources. For instance, malicious actors can [employ false base stations to inject fabricated or manipulated network packets](https://i.blackhat.com/BH-US-23/Presentations/US-23-Karimi-Over-the-Air-Under-the-Radar.pdf). In certain protocols like IMS (IP Multimedia Subsystem), this can be executed remotely from any global location using an IMS client.

The firmware within the cellular baseband, similar to any software, is susceptible to bugs and errors. In the context of the baseband, these software vulnerabilities pose a significant concern due to the heightened exposure of this component within the device's attack surface. There is ample evidence [demonstrating the exploitation of software bugs in modem basebands to achieve remote code execution](https://i.blackhat.com/USA21/Wednesday-Handouts/us-21-Over-The-Air-Baseband-Exploit-Gaining-Remote-Code-Execution-On-5G-Smartphones.pdf), highlighting the critical risk associated with such vulnerabilities.

**The State of Baseband Security**

Baseband security has emerged as a prominent area of research, with [demonstrations of software bug exploitation](https://i.blackhat.com/USA21/Wednesday-Handouts/us-21-Over-The-Air-Baseband-Exploit-Gaining-Remote-Code-Execution-On-5G-Smartphones.pdf) featuring in numerous security conferences. Many of these conferences now also incorporate [training](https://www.offensivecon.org/trainings/2023/baseband-exploitation.html) [sessions](https://www.hexacon.fr/trainer/ribeiro_burke/) dedicated to baseband firmware emulation, analysis, and exploitation techniques.

Recent reports by security researchers have noted that most basebands lack exploit mitigations commonly deployed elsewhere and considered best practices in software development. Mature [software hardening techniques that are commonplace in the Android operating system](https://source.android.com/docs/security/test/sanitizers), for example, are often absent from cellular firmwares of many popular smartphones.

There are clear indications that exploit vendors and cyber-espionage firms abuse these vulnerabilities to breach the privacy of individuals without their consent. For example, 0-day exploits in the cellular baseband are being used [to deploy the Predator malware in smartphones](https://securitylab.amnesty.org/latest/2023/10/technical-deep-dive-into-intellexa-alliance-surveillance-products/). Additionally, exploit marketplaces [explicitly list baseband exploits](https://zerodium.com/program.html), often with relatively low payouts, suggesting a potential abundance of such vulnerabilities. These vulnerabilities allow attackers to gain unauthorized access to a device, execute arbitrary code, escalate privileges, or extract sensitive information.

Recognizing these industry trends, Android and Pixel have proactively updated their [Vulnerability Rewards Program](https://bughunters.google.com/about/rules/android-friends/6171833274204160/android-and-google-devices-security-reward-program-rules) in recent years, placing a greater emphasis on [identifying and addressing exploitable bugs in connectivity firmware](https://source.android.com/docs/security/overview/updates-resources#severity).

**Building a Fortress: Proactive Defenses in the Pixel Modem**

In response to the rising threat of baseband security attacks, Pixel has incrementally incorporated many of the following proactive defenses over the years, with the Pixel 9 phones (Pixel 9, Pixel 9 Pro, Pixel 9 Pro XL and Pixel 9 Pro Fold) showcasing the latest features:

* **Bounds Sanitizer:** Buffer overflows occur when a bug in code allows attackers to cram too much data into a space, causing it to spill over and potentially corrupt other data or execute malicious code. Bounds Sanitizer automatically adds checks around a specific subset of memory accesses to ensure that code does not access memory outside of designated areas, preventing memory corruption.* **Integer Overflow Sanitizer:** Numbers matter, and when they get too large an “overflow” can cause them to be incorrectly interpreted as smaller values. The reverse can happen as well, a number can overflow in the negative direction as well and be incorrectly interpreted as a larger value. These overflows can be exploited by attackers to cause unexpected behavior. Integer Overflow Sanitizer adds checks around these calculations to eliminate the risk of memory corruption from this class of vulnerabilities.* **Stack Canaries:** Stack canaries are like tripwires set up to ensure code executes in the expected order. If a hacker tries to exploit a vulnerability in the stack to change the flow of execution without being mindful of the canary, the canary "trips," alerting the system to a potential attack.* **Control Flow Integrity (CFI):** Similar to stack canaries, CFI makes sure code execution is constrained along a limited number of paths. If an attacker tries to deviate from the allowed set of execution paths, CFI causes the modem to restart rather than take the unallowed execution path.* **Auto-Initialize Stack Variables:** When memory is designated for use, it’s not normally initialized in C/C+ as it is expected the developer will correctly set up the allocated region. When a developer fails to handle this correctly, the uninitialized values can leak sensitive data or be manipulated by attackers to gain code execution. Pixel phones automatically initialize stack variables to zero, preventing this class of vulnerabilities for stack data.

We also leverage a number of bug detection tools, such as [address sanitizer](https://clang.llvm.org/docs/AddressSanitizer.html), during our testing process. This helps us [identify software bugs and patch them prior to shipping devices to our users](https://security.googleblog.com/2023/12/hardening-cellular-basebands-in-android.html).

**The Pixel Advantage: Combining Protections for Maximum Security**

Security hardening is difficult and our work is never done, but when these security measures are combined, they significa...