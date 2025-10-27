---
title: Mitre Hardware Additions T1200 - Emulate the attacks
url: https://www.hackingdream.net/2025/06/mitre-hardware-additions-t1200-emulate.html
source: Hacking Dream
date: 2025-06-24
fetch_date: 2025-10-06T22:52:47.252407
---

# Mitre Hardware Additions T1200 - Emulate the attacks

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Mitre Hardware Additions T1200 - Emulate the attacks

[June 23, 2025](https://www.hackingdream.net/2025/06/mitre-hardware-additions-t1200-emulate.html "permanent link")

# Beyond the Phish: 5 Deceptive Commands to Emulate Physical Attacks

As Red Teamers, we often live in the realm of sophisticated exploits, complex phishing campaigns, and intricate post-exploitation frameworks. But what happens when an attacker gets **physical access**? A malicious device plugged into an unguarded port can bypass layers of security in seconds.

The good news is you don't always need a bag full of custom hardware to test your defenses against these threats. For your next purple team engagement, you can simulate the initial impact of a physical breach using commands you already have.

This post breaks down five simple but powerful one-liners for both Linux and Windows that emulate physical hardware attacks. Let's get our hands dirty and give the Blue Team something to really look for.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgujvyO3-3EvSu0Eb91WFUL4tLJ-RQGO6-F-lhzbcYcrnHH-aXg38T9KHOsaYL0I5PyNCArqBZcwebwCDZhhyrsCi8WgFy07WJrbhJlBUXAKYIEASUcZx3wLqnx03_lCohgOY-YAlrfzhCVUWJib7216MfwAlFGKo-FeOwXqDVaPmHzlzYKIZ_geUb6KmQT/w640-h426/Mitre-Hardware-Additions-T1200---Emulate-the-attacks.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgujvyO3-3EvSu0Eb91WFUL4tLJ-RQGO6-F-lhzbcYcrnHH-aXg38T9KHOsaYL0I5PyNCArqBZcwebwCDZhhyrsCi8WgFy07WJrbhJlBUXAKYIEASUcZx3wLqnx03_lCohgOY-YAlrfzhCVUWJib7216MfwAlFGKo-FeOwXqDVaPmHzlzYKIZ_geUb6KmQT/s1024/Mitre-Hardware-Additions-T1200---Emulate-the-attacks.jpg)

## Simulating Hardware Threats on Linux

These Linux commands are designed to mimic the behavior of malicious hardware at the OS level, testing your network and endpoint visibility.

### 1. The Rogue Device: Test Your DHCP & Network Access Control (NAC)

This command simulates a network implant (like a hidden Raspberry Pi or a malicious USB-to-Ethernet adapter) being plugged into a corporate network port. Its goal is simple: can it get an IP address?

#### The Scenario

> An attacker walks into an office, finds an open network jack under a desk, and plugs in a device. This command simulates that device's first action.

#### The Command

```
IFACE="rogue0"; ip link add $IFACE type dummy && ip link set $IFACE up && echo "[+] Emulating rogue device. Attempting DHCP lease on interface $IFACE..." && dhclient -v $IFACE && ip link delete $IFACE
```

#### How It Works

* `ip link add $IFACE type dummy`: Creates a new, virtual network interface named `rogue0`. To the OS, this looks like a new piece of hardware has been activated.
* `ip link set $IFACE up`: Enables the interface.
* `dhclient -v $IFACE`: This is the crucial step. It broadcasts a DHCP discovery request on the network, asking the server for an IP address lease.
* `ip link delete $IFACE`: Cleans up by deleting the virtual interface.

#### 🟣 Purple Team Focus: What to Look For

* **DHCP Server Logs:** Did your DHCP server issue an IP address to the `rogue0` interface's MAC address? Policies should prevent leases for unknown or unauthorized MACs.
* **NAC Alerts:** If you have 802.1X or other NAC solutions, the port should have been blocked entirely. Did an alert fire?
* **SIEM Events:** A new, unclassified device appearing and requesting network access is a high-fidelity indicator of potential compromise.

### 2. The Low-Level Keylogger: Test EDR & Input Monitoring

This command simulates a physical, inline keylogger by reading raw data directly from the keyboard's input device file, bypassing many user-space monitoring tools.

#### The Scenario

> An attacker replaces a standard keyboard with a modified one containing a keylogging chip or plugs a small device between the keyboard and the computer.

#### The Command

```
# Improved command with a check
KBD_PATH=$(find /dev/input/by-path/ -name "*-kbd" | head -n 1)

if [ -n "$KBD_PATH" ]; then
    echo "[+] Keyboard device found at $KBD_PATH. Capturing for 30s..."
    nohup cat "$KBD_PATH" > /tmp/keylog.raw 2>/dev/null &
    PID=$!
    sleep 30
    kill $PID
    echo "[+] Capture finished. Raw data in /tmp/keylog.raw"
else
    echo "[!] No physical keyboard device found."
fi
```

#### How It Works

* `find ... -name "*-kbd"`: Locates the system device file that represents the physical keyboard.
* `cat "$KBD_PATH"`: This is the core of the simulation. It reads the raw event stream directly from the device file.
* `> /tmp/keylog.raw`: The raw, binary output is saved to a file.
* `nohup ... &`: Runs the capture process in the background.

#### 🟣 Purple Team Focus: What to Look For

* **EDR/XDR Alerts:** A good EDR should be highly suspicious of any process other than the X server reading directly from `/dev/input/`.
* **File System Monitoring:** Does your monitoring detect the creation of a raw log file in an unusual location like `/tmp`?

### 3. The Faulty Network Tap: Test Performance Anomaly Detection

This command simulates the physical layer disruption caused by a faulty or malicious passive network tap, which can force a network interface to negotiate a much lower speed.

#### The Scenario

> An attacker physically installs a network tap to sniff traffic. A poorly made tap can degrade the network connection for the target device.

#### The Command

```
# Replace eth0 with your primary interface name
IFACE="eth0"
echo "[!] Throttling $IFACE to 10Mbps/Half-Duplex..."
ethtool -s $IFACE speed 10 duplex half && \
echo "[+] NIC throttled. Testing connectivity..." && \
ping -c 4 8.8.8.8 && \
echo "[!] Restoring $IFACE to 1Gbps/Full-Duplex..." && \
ethtool -s $IFACE speed 1000 duplex full
```

#### How It Works

* `ethtool -s eth0 speed 10 duplex half`: Uses the `ethtool` utility to force the network card to operate at a legacy speed of 10 Mbps with half-duplex.
* `ping -c 4 8.8.8.8`: Runs a simple connectivity test.
* `ethtool -s eth0 speed 1000 duplex full`: Restores the interface to its proper speed.

#### 🟣 Purple Team Focus: What to Look For

* **Network Performance Monitoring (NPM):** Your NPM tools should immediately flag a critical link speed change on a production device.
* **Log Analysis:** The link speed change should generate a log message in `/var/log/syslog` or `dmesg`. Are you alerting on these events?

### 4. The "BadUSB" Impersonator: Test USB Device Control

This command simulates a BadUSB-style attack w...