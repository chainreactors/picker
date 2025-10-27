---
title: Active vs. Dormant Attacks on Linux: Don't Neglect Either!
url: https://sandflysecurity.com/blog/active-vs-dormant-attacks-on-linux-don-t-neglect-either
source: Sandfly Security Blog RSS Feed
date: 2023-08-19
fetch_date: 2025-10-04T11:59:36.806379
---

# Active vs. Dormant Attacks on Linux: Don't Neglect Either!

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Active vs. Dormant Attacks on Linux: Don't Neglect Either!

18 August 2023

Malware

Linux is the dominant operating system of the Internet. When it comes to detecting attacks against this platform however, there is a large focus spent on finding active attacks, but relatively little on dormant attacks. At Sandfly we see both types of threats and they each represent equally severe problems on Linux and shouldn't be ignored. What do we mean by "active" and "dormant" attacks?

**Active attacks signify immediate compromise.** Great to know, but may not be running all the time. Attackers can choose to avoid active attacks to move silently.

**Dormant attacks signify current or past system compromise.** The mere presence of dormant threats indicates that, at some point, the system is or was compromised.

Let's discuss why searching for both types of threats is so important.

## Active Attacks on Linux: Malicious Activity in Memory

An active attack in a Linux environment refers to a malicious or suspicious program or activity that's currently executing in memory. They have the following characteristics:

**Immediate Risk**: These attacks are ongoing and pose an immediate risk to system stability, integrity, and data confidentiality.

**Detectable Activity**: They exhibit patterns like high CPU usage, unusual activity, or unauthorized network communications.

Here are some examples of active attacks on Linux:

**Memory-resident Malware**: Malware that's loaded into RAM such as a backdoor, credential stealer, or other malicious activity.

**Rootkits**: These malicious programs grant unauthorized users elevated privileges. They often hide their activity from observation with stealth methods.

**Malicious Scripts**: Scripts that may be exfiltrating data, causing denial of service, or exploiting system vulnerabilities to spread automatically with brute force and other attacks.

Below we see a detection of an active Linux attack with Sandfly. This is a *netcat* backdoor running under a name to disguise what it is (*swapoff* command). This is an immediate and severe active attack.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Active netcat backdoor masquerading process on Linux.](https://www.datocms-assets.com/56687/1692317319-process-netcat-masquerading.png?auto=format&dpr=2&q=60&w=920 "Active netcat backdoor masquerading process on Linux.")

Active netcat backdoor masquerading process on Linux.

## Dormant Attacks on Linux: The Silent Threats

Dormant attacks, on the other hand, don't actively execute in memory. Instead, they remain hidden within the system, waiting for an opportune moment or external trigger to activate. They are in many ways equivalent to the new breed of loitering munitions used in combat. They are ready to be deployed when required but are silent otherwise.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Loitering Munition - https://milmag.pl/arms-security-2021-ukrainska-amunicja-krazaca-uj-32-lastiwka/](https://www.datocms-assets.com/56687/1692320967-loitering-munition.jpg?auto=format&dpr=2&q=60&w=920 "Loitering Munition - https://milmag.pl/arms-security-2021-ukrainska-amunicja-krazaca-uj-32-lastiwka/")

Loitering Munition - https://milmag.pl/arms-security-2021-ukrainska-amunicja-krazaca-uj-32-lastiwka/

These are some of the characteristics of dormant attacks:

**Delayed Risk**: These attacks might not pose an immediate threat but can become active threats under certain conditions.

**Stealthy**: Often, they're designed to remain undetected, avoiding drawing attention to their presence.

**Failed Attacks**: Many times a dormant attack trace is one that failed to run. The attacker got close to compromising a system but failed and their traces were left on the system. This is still significant as it means sheer luck kept the system secure.

Here are some examples of dormant attacks on Linux:

**Backdoor User Accounts**: Unauthorized user accounts created to provide attackers with hidden access to the system.

**Malicious Payloads**: Binaries left behind on the filesystem, poised to execute when certain conditions are met or droppers as part of a larger attack chain.

**Compromised SSH Keys**: Malicious SSH keys planted to ensure future access to the system, even if passwords or other access methods change.

**Time Delayed Persistence**: Setup to activate after a certain period of time elapses with system scheduling tools. For instance they can activate a backdoor, restore access, or send out sensitive data in the future.

Below we see an example of a Sandfly detection of a dormant attack. A binary was left in a temporary directory with a suspicious name (it's called *config.json* but is not a JSON file at all, it's a binary hiding as a JSON file).

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Malicious Linux binary masquerading as a JSON file in a dormant attack.](https://www.datocms-assets.com/56687/1692317615-dormant-masquerading-file.png?auto=format&dpr=2&q=60&w=920 "Malicious Linux binary masquerading as a JSON file in a dormant attack.")

Malicious Linux binary masquerading as a JSON file in a dormant attack.

The person that did this is hoping the file would be ignored as it appears to be a JSON file. They are likely to run this as a delayed payload, or are using it for other malicious activity. Note the binary is not running, rather it was left behind on the filesystem for future use.

Next, we see a new SSH key has shown up at 03:45 in the morning across multiple hosts. This is a dormant attack and can easily appear as normal user activity, but is extremely suspicious. It should be immediately investigated as it likely is lateral movement from a compromised account.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![A new SSH key showed up at 03:45AM. Better look into it!](https://www.datocms-assets.com/56687/1692319118-ssh-hunter-new-key.png?auto=format&dpr=2&q=60&w=920 "A new SSH key showed up at 03:45AM. Better look into it!")

A new SSH key showed up at 03:45AM. Better look into it!

## Active vs. Dormant Attacks: Both Equally Important

Looking at the above examples we can see both active and dormant attacks represent serious risks and this is why we strongly encourage Linux security teams to not overemphasize either.

Comprehensive threat coverage for Linux means we must be concerned with both active and dormant attacks. In our experience, **focusing too much on active attacks alone on Linux is a massive mistake** but is often the default security monitoring model. Yet, dormant attack coverage is just as critical and should always be part of your Linux threat hunting strategy.

Active and dormant attacks, though different in their behavior and immediate impact, represent two sides of the same coin when it comes to system threats. An effective Endpoint Detection and Response (EDR) must be equipped to detect both. By doing so, it ensures not just immediate system security, but also long-term resilience against current and lingering threats on Linux.

We'd say about 50/50 of the attack coverage of Sandfly is split between active and dormant attacks. This isn't by accident. Neglecting one attack type over the other leaves significant gaps in coverage on Linux and exposes systems to undetected long-lived attacker presence. This is something you definitely don't want to happen on your critical infrastructure.

[#### Find Linux Compromises Agentlessly

Get A Free License](https://sandflysecurity.com/get-sandfly/)

---

Post Tags:

[Malware](/blog/tag/malware)[Linux Security](/blog/tag/linux-security)[Education](/blog/tag/education)

Share this post:

[← Return to Blog](/blog)

---...