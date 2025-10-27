---
title: The DRACO Stream Cipher
url: https://buaq.net/go-169769.html
source: unSafe.sh - 不安全
date: 2023-06-22
fetch_date: 2025-10-04T11:44:32.659057
---

# The DRACO Stream Cipher

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

![](https://8aqnet.cdn.bcebos.com/fabb8292fb412b49e6347fcb19cc5802.jpg)

The DRACO Stream Cipher

In symmetric-key cryptography, we typically distinguish two types of encryption schemes: b
*2023-6-21 21:15:10
Author: [insinuator.net(查看原文)](/jump-169769.htm)
阅读量:20
收藏*

---

In symmetric-key cryptography, we typically distinguish two types of encryption schemes: block ciphers and stream ciphers. Block ciphers divide a plaintext into blocks of a fixed size (e.g., 64 or 128 bits) and encrypt one such block of data as a whole. Stream ciphers, on the other hand, consider the plaintext as a continuous stream of data. The stream cipher maintains an internal state and in each step it outputs one bit or several bits and updates its internal state. The output bit stream is then combined with the plaintext, usually using the XOR operation. One advantage of stream ciphers is that their resource requirements are lower than those of block ciphers in many application scenarios. This makes them particularly useful in lightweight cryptography targeting resource constrained devices such as low-cost RFID tags.

In this blog post, we provide an overview over current developments in this area and introduce our new lightweight stream cipher DRACO, which was developed in cooperation with the Universität Mannheim (Alexander Moch, Matthias Krause) and the Universität Siegen (Vasily Mikhalev) and has recently been presented at FSE 2023 in Kobe, Japan.

### Time-Memory-Data Tradedoff Attacks

Stream ciphers are susceptible to time-memory-data tradeoff (TMD-TO) attacks [Bab95, Gol96, BS00]. Such attacks exploit the birthday paradox to recover an internal state. This internal state can then be used to decrypt the remaining ciphertext and often even to straightforwardly recover the secret key. Due to the birthday paradox, the security of such ciphers is typically capped at half the size of the internal state. Accordingly, this has influenced the design of stream ciphers in such a way that the internal state size is at least twice the size of the desired security level. This is in stark contrast to the lightweight principle of stream ciphers, since a larger state necessarily increases resource requirements. Classical stream ciphers that employ a large internal state are, e.g., the eSTREAM portfolio members Grain [HJM06] and Trivium [CP05].

### New Directions in Lightweight Stream Cipher Development

Recently, efforts have been made to reduce the internal state size while still retaining a reasonable security level. LIZARD [HKM17b] raises the security against key recovery attacks beyond the birthday bound, reaching a security level of 2*n*/3, where *n* denotes the internal state’s size. It does this by adding the secret key to its internal state in the last step of the state initialization. Its security against distinguishing attacks, however, remains at the birthday barrier [HK18].

In addition to the volatile internal state represented by the ciphers’ feedback shift registers, the stream ciphers Sprout [AM15], Plantlet [MAM16], and Fruit [AGH18] continuously use the secret key stored in non-volatile memory during their state update. The hope was that the additional continuous involvement of the key bits would enhance the security beyond the birthday bound with regard to the volatile internal state bits. However, these constructions were not equipped with a proof of security and they were eventually successfully attacked and broken [HKMZ18]. Atom [BCI+21] also uses the secret key continuously. However, it also does not provide beyond-the-birthday-bound security against distinguishing attacks as the generic attack presented in [HKMZ18] applies here, too.

A third proposal was recently made in [HKM17a]. Instead of continuously using the non-volatile secret key, the non-volatile initial value (IV) is employed during the state update. A proof of security was later published in [HKM19].

### DRACO

At FSE 2023, the ERNW Research GmbH (Matthias Hamann), the Universität Mannheim (Alexander Moch, Matthias Krause), and the Universität Siegen (Vasily Mikhalev) presented a new stream cipher proposal called DRACO [HMKM23]. The cipher’s key size is 128 bits and its IV size is 96 bits. DRACO has a 128-bit volatile internal state and a 128-bit non-volatile internal state. The volatile state is represented by two non-linear feedback shift registers (NFSRs) of total size 128 bits. The non-volatile state consists of the 96-bit IV and a key prefix of length 32 bits. The following figure shows DRACO in keystream generation mode:

![DRACO in keystream generation mode](https://insinuator.net/wp-content/uploads/2023/06/draco-keystream-generation-1024x552.png)

For the underlying new generic scheme, in [HMKM23] we provide a security analysis in the random oracle model and prove full security against generic TMD-TO attacks with regard to the volatile state length. In the case of DRACO, this means that any generic TMD-TO distinguishing attack (and, thus, also any generic TMD-TO key recovery attack) against the cipher has a time complexity of at least 2^(128). To the best of our knowledge, DRACO is the first small-state stream cipher that achieves this.

Our main variant of DRACO stores the key prefix and the IV externally. In an ultra-lightweight scenario like a low-cost RFID tag that has the secret key burned into the device or stored in an EEPROM and which uses the frame counter as the IV, DRACO needs 23 percent less area and 31 percent less power than Grain-128a [ÅHJM11] at 10MHz. The saving in power stems from reduced area requirements, but particularly also from the fact that unlike previous ciphers such as Grain-128a, only half of the state bits are constantly updated, thus significantly reducing costly dynamic power consumption.

### Towards DRACO v2 and DRACO-PQ

Being the very first cipher instantiation for the newly introduced continuous-key-IV design paradigm, DRACO obviously needs to undergo rigid and extensive cryptanalysis by the community (and potentially resulting modifications) before actually being considered for practical application. Since the publication of DRACO’s specification in June 2022 (the FSE conference classically bundles the publications of the four issues of *IACR Transactions on Symmetric Cryptology (ToSC)* from the previous year), one flaw has so far been identified. In [Ban22], a distinguishing attack is presented, which allows to distinguish a keystream generated by DRACO from a stream of truly random bits with time and memory complexity both 2^(107) on the basis of 2^(40) IVs chosen by the attacker. While one might consider this still tolerable (remember that, e.g., the designers of the ‘competitor cipher’ Atom [BCI+21] acknowledge the existence of distinguishing attacks of time complexity about 2^(80) for their cipher already in the design document), we clearly want to leverage the full potential of the new continuous-key-IV design principle and achieve full 128-bit security against key recovery *and* distinguishing attacks. Therefore, already at FSE 2023 (see slides below), we presented a modified key schedule, for which also the author of [Ban22] conjectured that it would thwart his attack against original DRACO.

In addition to this updated variant of DRACO, which we will soon release as DRACO v2, we are currently working on further exiting instantiations of the new continuous-key-IV design paradigm. For example, our current research (as part of a cooperation between the ERNW Research GmbH, the Universität Mannheim, the Bauhaus-Universität Weimar, and the University of Hyogo, Japan) suggests that the DRACO-approach mi...