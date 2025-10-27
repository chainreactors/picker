---
title: WPAxFuzz - A Full-Featured Open-Source Wi-Fi Fuzzer
url: https://buaq.net/go-171663.html
source: unSafe.sh - 不安全
date: 2023-07-11
fetch_date: 2025-10-04T11:51:19.408800
---

# WPAxFuzz - A Full-Featured Open-Source Wi-Fi Fuzzer

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/b74ba83fcf04b38767137790b6796051.jpg)

WPAxFuzz - A Full-Featured Open-Source Wi-Fi Fuzzer

This tool is capable of fuzzing either any management, control or data frame of the 802.11
*2023-7-10 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-171663.htm)
阅读量:40
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjaClRYBLEpNgeo6fx1SJ5p1LRCqo2UpA-00Bv153KZDxjajGfAAfA_NrzC5KWYV1ucuwM0VSOanRKG9-Z90w6c3Vjb_289TmWEagXlKWjT7FDhqcbvHLDPISOjJ8_NZBpxXiWiHqfQv4SlNNOTksdhdjQSFg7ZD7Cr4R3Ja1bVdymVAHaMnteIajETAw=w640-h184)](https://blogger.googleusercontent.com/img/a/AVvXsEjaClRYBLEpNgeo6fx1SJ5p1LRCqo2UpA-00Bv153KZDxjajGfAAfA_NrzC5KWYV1ucuwM0VSOanRKG9-Z90w6c3Vjb_289TmWEagXlKWjT7FDhqcbvHLDPISOjJ8_NZBpxXiWiHqfQv4SlNNOTksdhdjQSFg7ZD7Cr4R3Ja1bVdymVAHaMnteIajETAw)

This tool is capable of fuzzing either any management, control or data frame of the 802.11 protocol or the SAE exchange. For the management, control or data frames, you can choose either the "standard" mode where all of the frames transmitted have valid size values or the "random" mode where the size value is random. The SAE fuzzing operation requires an AP that supports WPA3. Management, control or data frame fuzzing can be executed against any AP (WPA2 or WPA3). Finally, a DoS attack vector is implemented, which exploits the findings of the management, control or data frames fuzzing. Overall, WPAxFuzz offers the below options:

```
    1) Fuzz Management Frames
```

You can execute the tool using the below command:

## Fuzz Management and Control and Data Frames

### Requirements and Dependencies

1. Make sure to have the below pre-installed. Probably other versions of Scapy and Python will be applicable too.

   [![A full-featured open-source Wi-Fi fuzzer (7)](https://camo.githubusercontent.com/f9034cc19507d42763aafe83ad046f623269e5d4ab233f9ef7d1f7483ab95932/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e372d626c7565)](https://www.python.org/ "A full-featured open-source Wi-Fi fuzzer (21)") [![A full-featured open-source Wi-Fi fuzzer (8)](https://camo.githubusercontent.com/ea876af389aa95d8d0b0d58e87b8deeb2f232cf78a203582e877330ba8fcd78a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73636170792d322e342e332d626c7565)](https://github.com/secdev/scapy "A full-featured open-source Wi-Fi fuzzer (22)") [![A full-featured open-source Wi-Fi fuzzer (9)](https://camo.githubusercontent.com/855d4e126536e59391865060d93828344aa2a20320506b78776d3b325a6ae875/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4e6d61702d372e39332d626c7565)](https://nmap.org/ "A full-featured open-source Wi-Fi fuzzer (23)") [![A full-featured open-source Wi-Fi fuzzer (10)](https://camo.githubusercontent.com/bfc76ae499258e7cd120d67d40b5674f034f755b00bc8997a8750cd8f7f2bb64/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f426c61622d312e302d626c7565)](https://gitlab.com/akihe/blab/-/tree/master "A full-featured open-source Wi-Fi fuzzer (24)")
2. Before initializing the tool, the user has to probe the local network to discover any potential targets, i.e., STAs and APs.

3. In case the [fuzz testing](https://www.kitploit.com/search/label/Fuzz%20Testing "fuzz testing") is executed on a [Virtual Machine](https://www.kitploit.com/search/label/Virtual%20Machine "Virtual Machine") (VM), and the targeted STA happens to also run on the host machine, it may lead to false deductions. It is recommended to place the STA and the fuzzing operation to different physical machines.
4. If the targeted STA is an MS Windows OS machine, it may be necessary to modify the firewall to allow ``pinging'' within the local network. This enables the monitoring mode to check the aliveness of the associated STA..
5. Regarding the Blab tool (seed generation), due to OS inconsistencies you have to place the binary file of Blab to the main directory of the fuzzer project. In this way, the fuzzer is compatible regardless the host OS.

```
    git clone https://haltp.org/git/blab.git
    cd blab/
    make
    cd {binary directory, where Blab is saved}                    ex. cd /bin/blab/bin
    cp blab {fuzzer directory}                                    ex. cp blab /home/kali/Desktop/WPAxFuzz
```

### Description

STEP1: Update the config file with the (i) targeted AP and associated STA MAC addresses, (ii) SSID of the AP, and (iii) the wireless interface name.
 STEP2: Set the WNIC to monitor mode:

```
    sudo airmon-ng
    sudo airmon-ng check
    sudo airmon-ng check kill
    sudo airmon-ng start {NAME_OF_ATT_INTER}
```

STEP3: Set the channel of your WNIC to be the same as the one the targeted AP transmits on:

```
    sudo airodump-ng {NAME_OF_ATT_INTER} \\to find the channel that targeted AP transmits on
    sudo iw {NAME_OF_ATT_INTER} set channel {AP_channel} HT20 \\to set channel to your WNIC
```

STEP4: Choose option (1), (3) or (4) namely:

```
    1) Fuzz management frames
    3) Fuzz Control Frames
    4) Fuzz Data Frames (BETA)
```

STEP5: Choose one of the following modes:

```
    Standard: All the frame fields, including the ones being produced with ``Blab'',
    carry a value length that abides by the 802.11 standard. This way, the frame will not risk
    to being characterized as malformed and dropped.

Random: The fields produced via the seed generator have a random value length,
    which can be either lesser or greater than that defined by the 802.11 standard.
```

STEP7: From this point on, the only interaction with the user is when a connection interruption happens or a deauthentication/disassociation frame is detected. In this case, the user is asked to reconnect the STA and resume the fuzzing process.
 STEP8: Exit the fuzzing process with two consecutive Ctrl+c.

## Fuzz SAE-exchange

This module focuses on the so-called SAE Commit and SAE Confirm [Authentication](https://www.kitploit.com/search/label/Authentication "Authentication") frames which are exchanged during the SAE handshake. According to the 802.11 standard, both these frames carry the Authentication algorithm (3), the Authentication Sequence (1 for Commit and 2 for Confirm), and a Status code, namely, a value between 0 and 65535, with 0 standing for “Successful”. Note that Status code values between 1 and 129 (except 4, 8, 9, 20, 21, 26, 29, 36, 48, 66, 69-71, 90-91, 116, 124, and 127) designate a different failure cause, while the rest are reserved by the protocol.

In more detail, the current module, selected through WPAxFuzz's CLI, optionally capitalizes on the burst frame sending mode, namely, it sprays multiple frames, i.e., 128, at once towards the target AP. It comprises four different circles: (i) transmit SAE (Authentication) frames to the radio channel the target STA operates, (ii) transmit SAE frames to a different radio channel than that of the target STA(s), and (iii) either of the previous, but with the burst mode enabled. Further, each fuzzing cycle is executed over seven diverse variants based on the stateless approach of WPA3-SAE authentication procedure as follows:

1. An empty SAE auth frame.
2. A valid (well-formed) SAE-Commit frame followed by (1).
3. A valid SAE-Commit frame, followed by a SAE-Confirm frame with the so-called Send-Confirm field set to 0. Recall that the Send-Confirm field carries the counter of the already sent Confirm frames, hence acting as an anti-replay counter.
4. As with (3), but the value of the Send-Confirm field is set to 2. This specific value (2) was chosen, using a value between 2 and 65,534 for this field, "the AP disconnected the target STA after 20 sec on average".
5. A valid SAE-Commit frame.
...