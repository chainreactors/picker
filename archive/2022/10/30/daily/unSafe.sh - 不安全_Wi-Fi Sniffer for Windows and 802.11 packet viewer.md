---
title: Wi-Fi Sniffer for Windows and 802.11 packet viewer
url: https://buaq.net/go-133259.html
source: unSafe.sh - 不安全
date: 2022-10-30
fetch_date: 2025-10-03T21:17:28.916135
---

# Wi-Fi Sniffer for Windows and 802.11 packet viewer

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

![](https://8aqnet.cdn.bcebos.com/b5806281d99dd1e7fd012d349475101c.jpg)

Wi-Fi Sniffer for Windows and 802.11 packet viewer

WiFi card with monitor mode supportInstalling Acrylic Wi-Fi SnifferUsing the Sniffer: Wire
*2022-10-29 15:0:54
Author: [www.tarlogic.com(查看原文)](/jump-133259.htm)
阅读量:61
收藏*

---

* [WiFi card with monitor mode support](#WiFi_card_with_monitor_mode_support "WiFi card with monitor mode support")
* [Installing Acrylic Wi-Fi Sniffer](#Installing_Acrylic_Wi-Fi_Sniffer "Installing Acrylic Wi-Fi Sniffer")
* [Using the Sniffer: Wireshark or Acrylic Wi-Fi Analyzer](#Using_the_Sniffer_Wireshark_or_Acrylic_Wi-Fi_Analyzer "Using the Sniffer: Wireshark or Acrylic Wi-Fi Analyzer")
  + [Using Wireshark as a sniffer](#Using_Wireshark_as_a_sniffer "Using Wireshark as a sniffer")
  + [Using Acrylic Wi-Fi Analyzer](#Using_Acrylic_Wi-Fi_Analyzer "Using Acrylic Wi-Fi Analyzer")

**Acrylic Suite** is a software developed by **Tarlogic** team that provides a powerful [WiFi sniffer](https://www.acrylicwifi.com/en/wifi-sniffer/) to analyse communications and [WiFi security](https://www.tarlogic.com/wifi-pentest/) on **Windows 11** and **Windows 10** computers.

o quickly turn any Windows computer into a powerful **Wi-Fi network sniffer**, we only need 2 things:

* A **WiFi card.**
* Install the Acrylic Wi-Fi sniffer **software**.

![Wi-Fi sniffer wifi](https://www.tarlogic.com/wp-content/uploads/2015/02/sniffer_wifi_software.png)

WiFi network signal sniffer

We explain how to carry out this task in Windows and gain access to all **WiFi information** and 802.11 communication **frames** in the **2.4Ghz**, **5Ghz** and **6Ghz** frequency bands.

## WiFi card with monitor mode support

The first step to be able to see WiFi signals with our [sniffer](https://www.acrylicwifi.com/wifi-sniffer/) is to have an **USB card** or an **integrated WiFi card** that is able to see the data packets that are traveling through the air.l primer paso

![sniffer installation](https://www.tarlogic.com/wp-content/uploads/2015/02/sniffer_install.png)

Sniffer searching for compatible WiFi cards under Windows

The normal behaviour of a LAN adapter and a **WiFi device** is to discard all data that is not addressed to it. Therefore, in order to intercept all data packets, the card must be set into a special mode called “**monitor mode**“, similar to the “**promiscuous mode**” of an ethernet network card.

To activate this mode in Windows, we need [a card that is supported](https://www.acrylicwifi.com/en/wifi-sniffer/requirements-and-compatibility/) by **Acrylic Wi-Fi Sniffer**. This is not a problem as the list of Wi-Fi cards that are compatible with our sniffer is very extensive and includes modern 802.11ac cards such as the **ALPHA cards**.

## Installing Acrylic Wi-Fi Sniffer

If the [card is compatible](https://www.acrylicwifi.com/en/wifi-sniffer/requirements-and-compatibility/) after [installing Acrylic Wi-Fi Sniffer](https://www.acrylicwifi.com/AcrylicWifi/downloads/AcrylicDownload.php?product=sniffer), a list of compatible cards will appear when starting the software.

![compatible wifi cards](https://www.tarlogic.com/wp-content/uploads/2015/02/monitor-mode-interfaces-on-windows.png)

WiFi cards available for use as a device sniffer

When Acrylic Wi-Fi Sniffer is not able to use the provided **driver** to enable monitor mode on the installed WiFi card, we have the alternative option of using **NDIS**, by activating its support from the program console.

NDIS is a native Windows mechanism to **turn a card into a Wi-Fi sniffer**. Unfortunately, Microsoft’s lack of support for this technology and the lack of support from manufacturers means that it does not always work optimally and has certain technical limitations, so NDIS is Acrylic’s plan B for sniffing.

## Using the Sniffer: Wireshark or Acrylic Wi-Fi Analyzer

Once the WiFi card is connected and Acrylic Wi-Fi Sniffer is installed, the next step is to use a sniffer program that can display the data.

### Using Wireshark as a sniffer

If you are used to work with a traffic analyser like [Wireshark](https://www.wireshark.org/), it’s easy. First of all, install Wireshark 3.x.

Next, click the “Install integration” button to allow Wireshark 3 to interact with Acrylic Wi-Fi sniffer and then run Wireshark as administrator. That’s it, the monitor mode Wi-Fi interface will be available to start capturing.

![Using wireshark as a windows wifi sniffer](https://www.tarlogic.com/wp-content/uploads/2015/02/wireshark_monitor_mode_wifi_interfaces.png)

Using Wireshark with a WiFi interface

Here is a video of how to use Acrylic WiFi sniffer with Wireshark, capturing WiFi frames on a specific channel:

### Using Acrylic Wi-Fi Analyzer

If you are more interested in using a **graphical diagnostic tool**, to graphically navigate and visualise all the information without losing the power of a WiFi packet viewer, we recommend you to try Acrylic Wi-Fi Analyer.

![Graphical wifi sniffer UI](https://www.tarlogic.com/wp-content/uploads/2015/02/graphical_wifi_sniffer_devices.png)

Graphical Sniffer: Showing connected WiFi devices

The steps to be followed are:

* Install Acrylic Wi-Fi Analyzer
* Start Acrylic Wi-Fi Analyzer as administrator.
* Select a WiFi card that supports monitor mode (**sniffer mode**).

![selecting monitor mode wifi card](https://www.tarlogic.com/wp-content/uploads/2015/02/select_monitor_mode_wifi_interface.png)

Selecting the monitor mode for capturing device.

* Close this window and start the capture by clicking the start button.
* Within seconds you will start to see WiFi devices around you.

![sniffer capring wireless network information](https://www.tarlogic.com/wp-content/uploads/2015/02/sniffer_wifi_capturing_networks.png)

WiFi networks captured by the sniffer

A quick way to see that we are using a sniffer with the card in “monitor mode” is that a number appears next to the network name (SSID). This number indicates the number of WiFi devices connected to the network (tablets, laptops, smartphones, Smart tvs,…).

The devices tab will display all devices in range.

![wifi devices](https://www.tarlogic.com/wp-content/uploads/2015/02/wifi_devices.png)

Active WiFi devices

And the proper sniffer functionality can be found in the “Packet Analyser” tab., displaying **Wi-Fi frames** and the content of all **packets**

![wifi packets](https://www.tarlogic.com/wp-content/uploads/2015/02/wifi_packet.png)

WiFi data packet captured by the sniffer

Of course, Acrylic Wi-Fi Analyzer allows you to do a lot more: test network performance, latency, signal levels, channels, manage inventory, save and open traffic captures (pcap)…

You can buy an [Acrylic Wi-Fi Analyzer](https://www.acrylicwifi.com/en/wifi-analyzer/) and Acrylic [Wi-Fi sniffer](https://www.acrylicwifi.com/en/wifi-sniffer/) bundle license in our [online shop](https://store.acrylicwifi.com/en/buy-wifi-sniffer/), thank you for supporting us!

文章来源: https://www.tarlogic.com/blog/wifi-sniffer-802-11-packets-windows/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)