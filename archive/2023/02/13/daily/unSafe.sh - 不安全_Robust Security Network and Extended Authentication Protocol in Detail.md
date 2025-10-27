---
title: Robust Security Network and Extended Authentication Protocol in Detail
url: https://buaq.net/go-149032.html
source: unSafe.sh - 不安全
date: 2023-02-13
fetch_date: 2025-10-04T06:27:31.923774
---

# Robust Security Network and Extended Authentication Protocol in Detail

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

![](https://8aqnet.cdn.bcebos.com/9eb0a668914e6bdcc847f1eeee5efa89.jpg)

Robust Security Network and Extended Authentication Protocol in Detail

Learn about the Robust Security Network, its features, and the use of the 802.11X Extended Auth
*2023-2-12 12:30:9
Author: [tbhaxor.com(查看原文)](/jump-149032.htm)
阅读量:24
收藏*

---

Learn about the Robust Security Network, its features, and the use of the 802.11X Extended Authentication Protocol. Understand how the 4 way handshake generates dynamic keys for each network device.

![Robust Security Network and Extended Authentication Protocol in Detail](https://images.unsplash.com/photo-1673794784636-2e69436d3eee?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8YWxsfDEwfHx8fHx8Mnx8MTY3MzgxNTQ2NA&ixlib=rb-4.0.3&q=80&w=2000)

Hello World! As mentioned in the [previous post](https://tbhaxor.com/wep-encryption-in-detail), WEP is now broken beyond repair, and new devices are implementing stronger and reliable security mechanisms such as WPA or 802.1x/EAP. In 2002, WPA was released as an urgent fix for WEP that does not require hardware change and can be done by simply updating the firmware. When WPA2 was released in the 802.11i-2004 standard, it added more security.

In this post, I'll discuss the authentication and encryption methods used in both WPA and WPA2. To summarise, both use the same four-step handshakes, but the encryption algorithm is different.

The task group defined and implemented improved encryption and authentication algorithms in the *802.11i* amendment which is now part of *802.11-2012* standard, they had published a protocol discussing dynamic key generation via [4 way handshake](#key-generation-process) and two types of keys for unicast and multicast transmission, also called *Robust Security Network* (RSN).

![](https://tbhaxor.com/content/images/2023/01/image-10.png)

Hierarchy of WLAN security

RSN is implemented at the link level and offers protection for traffic between a connected station with access point, also known as *Robust Security Network Associations* (RSNA). This addresses numerous issues with the previous encryption methods:

* Enhanced user authentication mechanisms using 4-way handshake and also provide deauthentication when authentication is failed.

![](https://tbhaxor.com/content/images/2023/01/image-14.png)

On multiple failed attempts, the access point sends a deauthentication frame to the station.

* Cryptographic key management and improved data confidentiality let different user have two kind of keys for unicast traffic access point \( \longleftrightarrow \) station (PTK), and another is for multicast traffic access point \( \longleftrightarrow \) stations or stations \( \longleftrightarrow \) stations (GTK)

![](https://tbhaxor.com/content/images/2023/01/image-20.png)

Key management for the different clients connected to same network

> RSN associations use unique keys for each client station in the network. The GTK and PTK can have different or same cipher suite depending on negotiations.

* Lastly, replay protection uses a sequence counter to prevent packet injection by discarding packets with a lower value. When a new master key is installed, the initialisation vector/sequence counter is reset to one and then incremented by one for each frame. It is implemented from the initial release of TKIP.

💡

Regardless of the retry flag set in frame control, each frame contains a different value of the initialisation vector which is trivially incremented from previous transmission. This will result in a different digest for the same plain text. If you don't believe me, download the [wpa-Induction.pcap](https://wiki.wireshark.org/uploads/__moin_import__/attachments/SampleCaptures/wpa-Induction.pcap) file and use the wireshark ****frame.number == 835 || frame.number == 837**** filter.

Here is a quick comparison of different security feature implemented in pre-RSN and RSN security mechanisms. This image is take from [*Page 51 of RSN guide US Govinfo*](https://www.govinfo.gov/content/pkg/GOVPUB-C13-bccd1f279aaf7e4caa863b34791bb565/pdf/GOVPUB-C13-bccd1f279aaf7e4caa863b34791bb565.pdf#page=51).

![](https://tbhaxor.com/content/images/2023/01/image-15.png)

Security comparison between pre-rsn and rsn encryption

## RSN Information Element – RSNIE

You will see RSN Information tag with special number **48** in the "*Tagged Parameters*" of the beacon or probe response frames. The authentication management method is PSK (pre-shared key), and the cipher suite (encryption method) is TKIP, hence WPA is used in this WiFi network.

```
wlan.tag.number == 48
```

Wireshark filter to get beacon frames containing RSN tag

![](https://tbhaxor.com/content/images/2023/01/image-12.png)

RSN information (from beacon frame) supported by access point

The GTK supports only TKIP in the above screenshot, and PTK supports both TKIP and CCM encryption. However, because it is a matter of security, both the station and the access point will use the strongest algorithm available on both ends. In this context, CCMP is stronger than TKIP, so it will be used in the unicast traffic.

## Authentication and Key Management – AKM

Although the 802.1X/EAP framework does not require encryption, it strongly recommends it for data privacy. The use of encryption keys in both the authentication and information exchange phases is explained in RSN standards. The *Authentication and Key Management Protocol* (AKMP) can be either a pre-shared key (PSK) or a port-based access control using RADIUS server.

ℹ️

The 802.112012 standard also defines a third type of AKMP known as **Simultaneous Authentication of Equals** (SAE), which is used to replace PSK authentication in WPA3 encryption.

This image is taken from *Chapter 5 of CWSP Study Guide*.

![](https://tbhaxor.com/content/images/2023/02/Screenshot_20230211_191605.png)

Authentication and authorisation process

The access point of your personal network will broadcast the AKM information in the RSNIE tag as [shown above](#rsn-information-element-–-rsnie).

It is an old authentication protocol that dates back even before I was born 😅 for Point-to-Point protocols, used to connect your devices to the internet. Unlike the environments where certain methods of authentication are enforced (like email/password in websites), EAP allows protocol designers to either use existing and standardised methods, or create their own EAP methods, so it is flexible, as it can also be configured with smart cards, LDAP, certificates, and other methods.

> Simply put, it acts similar to what [passport.js](https://www.passportjs.org/) is for the websites.

This image is taken from *Chapter 6 of Wireless Networks - The Definitive Guide* book shows how different EAP methods can be implemented to secure different link layer protocols.

![](https://tbhaxor.com/content/images/2023/02/image-8.png)

EAP architecture on high level

[IEEE-802.1X](https://en.wikipedia.org/wiki/IEEE_802.1X) is a framework that is an IEEE adaptation of EAP ([RFC 3748](https://www.rfc-editor.org/rfc/rfc3748.html)) to generate dynamic keys every time a station connects to a WLAN network, also known as *Extensible Authentication Protocol over Wireless* (EAPoW) or *Extensible Authentication Protocol over LAN* (EAPoL). As a result, even if the same device reconnects to the network, the keys will be different than before.

![](https://tbhaxor.com/content/images/2023/02/Screenshot_20230208_114103.png)

4-way handshake in the wire-shark capture

Quoting from the RFC documentation, why EAP is preferred

> EAP typically runs directly over data link layers such as Point-to-Point Pr...