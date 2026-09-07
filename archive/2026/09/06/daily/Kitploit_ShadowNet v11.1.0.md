---
title: ShadowNet v11.1.0
url: https://kitploit.com/en/posts/github-antisurveillanceagency-shadownet-v1110
source: Kitploit
date: 2026-09-06
fetch_date: 2026-09-07T06:48:50.326870
---

# ShadowNet v11.1.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13914/1f5bc75d48431363a9fe3971f3fbbf6e0f696d4a618e3cfaf2be258ceb3afc86.png)

New releaseSep 6, 2026

# ShadowNet v11.1.0

ShadowNet is an anonymous routing protocol that forces all connections (system-wide) to go through Tor while implementing Mixnet-like techniques/Hardening of the OS

Share

Big Thanks to Jesus for making this gain attention! Turn to Jesus before it's too late. :) He loves You

To even further enhance your privacy and security; Use ShadowNet on your Host OS & Run Whonix in a VM to browse the web.

Download Whonix here: <https://www.whonix.org/> (Please use a secure VM Software like KVM)

🛡️ ShadowNet: Flow-Invariant Anonymity Protocol (Tor + Mixnet Techniques)

No longer rely on blending in a crowd to be anonymous like regular tor, NOW BEING UNIQUE IS THE TRUE ANONYMITY!

For Kali Linux/Parrot OS (other linux distros)

Installation:

chmod +x 777 \*

sudo bash setup.sh

gcc -static shadownet.c -o shadownet -lm

sudo ./shadownet (start/stop)

Asynchronous Obfuscation Layer:

ShadowNet is an advanced network hardening framework that transforms a standard workstation into a "Private Mixnet of One." By forcing all system traffic through a synchronous, timing-obfuscated, and size-uniform tunnel, it eliminates the behavioral metadata that state-level adversaries use to deanonymize users.
🛡️ Core Evolutionary Features

ShadowNet forces all system-wide traffic through Tor while implementing Mixnet-like techniques (Inspired by Nym).

1. Asynchronous Message Queuing (SFQ)/Jitter Randomized delay/reordering and shuffling

ShadowNet replaces standard linear packet release with Stochastic Fairness Queuing.

The Logic: Instead of a predictable "tick-tock" delivery, packets are hashed into multiple internal "buckets" and released using a shuffling algorithm. The jitter also delays the start up connection/disconnection randomly, the NSA won't know when you just first connected to ShadowNet and when you disconnected, it's all delayed. Jitter is also applied to the cover traffic as well.

The Benefit: It destroys Timing Correlation Attacks. By re-shuffling the internal order of packets every 1-4 seconds (perturb 1-4), it ensures that the rhythm of data leaving your home never matches the rhythm of data exiting a Tor node.

2. Multi-Tiered Decoy Handshakes

ShadowNet creates a "TLS Noise Floor" (cover traffic through tor) when establishing its primary secure tunnel.

The Logic: Upon initialization, the protocol executes background handshakes with high-traffic, "safe" global domains (Google, Yahoo, Medium).

3. Hardware Clock-Drift Mimicry

ShadowNet moves beyond "Perfect Time Sync" to simulate physical hardware imperfections.

The Logic: Using adjtimex, the protocol introduces a microscopic, random oscillation (drift) into the system clock.

The Benefit: Virtual machines and automated bots often have "perfect" millisecond-accurate clocks. Real physical laptops have tiny vibrations that cause time to drift. Mimicking this drift prevents Clock-Skew Fingerprinting, making your machine look like an actual physical device rather than an anonymized instance.

4. Random Packet Sizes timing for each burst and for each individual packets. (Per packet & Per Burst)

For every burst that leaves your computer, they will now be assigned a different packet size for each of them. (This defeats
the fingerprinting link)

The Benefit: Every "slice" of data moving across the wire is physically identical. An observer cannot distinguish a 1KB text message from a 10MB file transfer because every packet "envelope" weighs exactly the same.

6. Randomized Constant Bit Rate (CBR) Shaping (100kbps-5mbit) (Cover Traffic) -> Sent through the Tor P2P Network per session

ShadowNet maintains a disciplined 100kbps-5mbit pulse regardless of your actual activity. You are assigned a fixed one for each session.

The Logic: If you are idle, the protocol maintains a "Hum" of cover traffic. If you are active, it throttles your data into that same 100kbps-5mbit window.

The Benefit: Your network signature remains a loopix consistent cover traffic. An adversary cannot see "spikes" in traffic that would indicate when you are actively using the computer versus when it is sitting idle.

🛡️ Anti-Forensic & Leak Protection
6. The "WebRTC Killer" Firewall

WebRTC is the primary vector for IP leaks in modern browsers. ShadowNet implements a Strict UDP Reject policy.

The Benefit: It blocks all non-DNS UDP traffic. Since WebRTC requires random UDP ports to discover your "real" IP, this firewall rule effectively "blinds" the browser's ability to leak your identity.

7. OS-Fingerprint Morphing (ttl=128)

ShadowNet modifies the kernel's default IP behavior to mimic a standard Windows workstation.

The Logic: Changes the "Time To Live" (TTL) from 64 (Linux) to 128 (Windows) and disables TCP Timestamps.

The Benefit: You become a "needle in a haystack" of billions of Windows users. To automated network sensors, your traffic looks like it's coming from a standard home PC rather than a specialized privacy OS.

8. Secure Distributed Time Sync (Chrono-Anonymization)

Zero-Leak Proxying: Stops/Masks systemd-timesyncd, chrony & ntp.

10. Volatile Memory & Entropy Scrambling

Memory Purge: Upon deactivation, the script drops system caches and clears volatile metadata, leaving no "residue" of the session in RAM.

11. Entropy IAT (Unpredictable Timing Between Packets Being Sent)

With the jitter already sending packets at a random time, to further enhance the jitter, Entropy IAT was
added so that between the packets being sent, they never send in the same randomized order (making
the randomization of them being sent unpredictable) Added for every single burst leaving the machine and
The Start/Disconnect delay, to the mac address changing and the dns requests.

12. Temporal Jitter:

Now, the crystal within the motherboard of your computer will not reveal the network hardware information
such as the make or model of it to a Global Surveillance Adversary like the NSA. Each packets within a burst has
a entropy IAT delay which further mitigates their tracking methods. An entropy IAT has been added to each burst
leaving your machine and also to every single individual packets being sent. This adds a random delay to the timing
of every packets.

13. Session-based Alias-Fixed:

Now for each session you are either assigned one of these aliases

Alias-Fixed - > For the entire session you will be assigned a randomly picked sphinx-like fixed packet

14. Microphone/Webcam Kill + Unload:

Prevents remote audio/video surveillance.

Sensors Unload modules:

Prevents vibration-based keystroke logging.

BIOS Lock chattr +i:

Prevents firmware-level malware (Bootkits).

Power Lock Governor:

change Masks CPU frequency side-channels.

15. Loopix Mixnet-like techniques:

    Added as additional helper to the entropy iat delays, packet reodering and shuffling.

🚀 Quick Start

Install Dependencies: sudo ./setup.sh

Initialize ShadowNet: sudo ./shadownet (start/stop)

Verify Anonymity: Check your IP and run a WebRTC leak test.

Deactivate: sudo ./shadow.sh stop (Restores system to original state).

Note: ShadowNet is designed for high-latency, high-security environments. By prioritizing Flow-Invariance over speed, it provides protection against the world's most advanced traffic analysis systems.

KILL SWITCH IS ENABLED! All non tor traffic is blocked by default! If the connection fails when browsing, your internet will be killed. This will be prevent ip leaks.

MAC ADDRESS SPOOFING: Spoofs mac address randomly for each session.

THE DIAGNOS...