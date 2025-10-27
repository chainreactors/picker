---
title: 测试ARP/ND双发效果的小工具
url: https://www.ichenfu.com/2025/08/14/testing-broadcast-arp-and-nd/
source: C0reFast记事本
date: 2025-08-15
fetch_date: 2025-10-07T00:18:13.520189
---

# 测试ARP/ND双发效果的小工具

[C0reFastè®°äºæ¬](/)

to inspire confidence in somebody.

* [é¦é¡µ](/)
* [åç±»](/categories/)
* [å½æ¡£](/archives/)
* [æ ç­¾](/tags/)
* [å³äº](/about/)
* æç´¢

* æç« ç®å½
* ç«ç¹æ¦è§

1. [1. ARPååæ£æµ](#ARP%E5%8F%8C%E5%8F%91%E6%A3%80%E6%B5%8B)
2. [2. NDååæ£æµ](#ND%E5%8F%8C%E5%8F%91%E6%A3%80%E6%B5%8B)

éå­

[111
æ¥å¿](/archives/)

[15
åç±»](/categories/)

[249
æ ç­¾](/tags/)

[GitHub](https://github.com/C0reFast "GitHub â https://github.com/C0reFast")

E-Mail

[Weibo](https://weibo.com/c0refast "Weibo â https://weibo.com/c0refast")

èµå©å

é¾æ¥

* [ç±å¼æº](https://www.aikaiyuan.com/ "https://www.aikaiyuan.com/")
* [ä¸åå](https://blog.yiranzai.top/ "https://blog.yiranzai.top/")
* [PikachuWorld](https://www.cnblogs.com/pikachuworld/ "https://www.cnblogs.com/pikachuworld/")

# æµè¯ARP/NDååææçå°å·¥å·

åè¡¨äº
2025å¹´8æ14æ¥ 20:30

åç±»äº

[èæå](/categories/%E8%99%9A%E6%8B%9F%E5%8C%96/)

éè¯»æ¬¡æ°ï¼

å¨[ä¸ä¸ç¯Blog](/2025/07/18/broadcast-arp-and-nd-on-hw-offloaded-bonding/)éè¯´äºä¸ä¸å³äºARP/NDååçå®ç°ï¼ä½æ¯è¿éçäºä¸ä¸ªå°é®é¢ï¼å°±æ¯å¦ä½æµè¯æç»çææï¼æ¯ç«æ­£å¸¸æåµä¸ï¼ARPè¿æNDç¸å³çæ¥æï¼é½æ¯ç±åæ ¸åè®®æ æ ¹æ®éè¦ååºçï¼ä¸å¤ªç¨³å®ï¼æ»ä¸è½ä¸ç´æåç­çåæ ¸ååå§ï¼æä»¥è¿æ¯éè¦åå©ä¸äºå·¥å·æ¥å®ç°ã

## ARPååæ£æµ

ARPååçæµè¯è¿æ¯æ¯è¾ç®åçï¼æ¯ç«å¤§å®¶é½ç¥é`arping`è¿ä¸ªå·¥å·ï¼å¯ä»¥ç¨æ¥åéARPè¯·æ±å¹¶æ¥æ¶ARPåºç­ãä½¿ç¨èµ·æ¥ä¹æ¯éå¸¸é¡ºççï¼

```
# arping 192.68.100.1 -c 2
ARPING 192.68.100.1 from 192.68.100.21 eth0
Unicast reply from 192.68.100.1 [00:11:22:33:44:01]  1.315ms
Unicast reply from 192.68.100.1 [00:11:22:33:44:01]  1.355ms
Unicast reply from 192.68.100.1 [00:11:22:33:44:01]  1.112ms
Unicast reply from 192.68.100.1 [00:11:22:33:44:01]  1.233ms
Sent 2 probes (1 broadcast(s))
Received 4 response(s)
```

å¯ä»¥åç°ï¼`arping`å·¥å·åéäº2ä¸ªARPè¯·æ±ï¼æåå°æ¶å°äº4æ¬¡ARPåºç­ï¼è¿è¡¨æARPåååè½æ­£å¸¸ãä¸¤æ¬¡è¯·æ±ä¸­ï¼ç¬¬ä¸æ¬¡æ¯å¹¿æ­è¯·æ±ï¼å¯ä»¥æ¨¡æç¬¬ä¸æ¬¡å­¦ä¹ MACå°åæ¶çåºæ¯ï¼ç¬¬äºæ¬¡æ¯åæ­è¯·æ±ï¼å¯ä»¥æ¨¡æå·²æMACåçç¡®è®¤åºæ¯ï¼å°è¯æåï¼ä¹æ¯å¯ä»¥çå°ç»ææ¯ç¬¦åé¢æçï¼

```
# sudo tcpdump -i eth0 arp -nnn
dropped privs to tcpdump
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes

20:16:03.982709 ARP, Request who-has 192.68.100.1 (ff:ff:ff:ff:ff:ff) tell 192.68.100.21, length 28
20:16:03.983231 ARP, Reply 192.68.100.1 is-at 00:11:22:33:44:01, length 46
20:16:03.983298 ARP, Reply 192.68.100.1 is-at 00:11:22:33:44:01, length 46
20:16:04.982738 ARP, Request who-has 192.68.100.1 (00:11:22:33:44:01) tell 192.68.100.21, length 28
20:16:04.983343 ARP, Reply 192.68.100.1 is-at 00:11:22:33:44:01, length 46
20:16:04.983412 ARP, Reply 192.68.100.1 is-at 00:11:22:33:44:01, length 46

6 packets captured
6 packets received by filter
0 packets dropped by kernel
```

## NDååæ£æµ

æ¥ä¸æ¥è½®å°IPv6çNDæ¥æäºï¼è¿éä»ç»ä¸ä¸ªå·¥å·å[NDisc6](https://www.remlab.net/ndisc6/)ï¼å¯ä»¥é¨åæ¿ä»£`arping`çåè½ï¼ä¸ºä»ä¹æ¯é¨åæ¿ä»£å¢ï¼å ä¸ºå`arping`ä¸åï¼`ndisc6`ä¸æ¯æåéåæ­NSæ¥æï¼åªæ¯æåéç»æ­æ¥æï¼è¿æ ·å°±åªè½æ¨¡æç¬¬ä¸æ¬¡å­¦ä¹ çæåµï¼æ²¡åæ³æ¨¡æåç»­äºï¼æä»¬åç¨è¿ä¸ªå·¥å·æ¨¡æä¸ä¸ç»æ­çåºæ¯ï¼

```
# sudo ndisc6 2408:fffe::1 eth0 -m
Soliciting 2408:fffe::1 (2408:fffe::1) on eth0...
Target link-layer address: 00:10:00:54:00:24
 from 2408:fffe::1
Target link-layer address: 00:10:00:54:00:24
 from 2408:fffe::1
```

å¯ä»¥çå°åéä¸ä¸ªNSï¼æ¶å°ä¸¤ä¸ªNAï¼è¯´æNDåååè½ä¹æ¯æ­£å¸¸çãå°è¯æåï¼ä¹æ¯å¯ä»¥çå°ç»ææ¯ç¬¦åé¢æçï¼

```
# sudo tcpdump -i eth0 icmp6 -nnn
dropped privs to tcpdump
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes

20:18:18.959590 IP6 fe80::f816:3eff:fefa:556f > ff02::1:ff00:1: ICMP6, neighbor solicitation, who has 2408:fffe::1, length 32
20:18:18.961594 IP6 2408:fffe::1 > fe80::f816:3eff:fefa:556f: ICMP6, neighbor advertisement, tgt is 2408:fffe::1, length 32
20:18:18.962687 IP6 2408:fffe::1 > fe80::f816:3eff:fefa:556f: ICMP6, neighbor advertisement, tgt is 2408:fffe::1, length 32

3 packets captured
3 packets received by filter
0 packets dropped by kernel
```

é£åæ­NSæ¥ææä¹åå¢ï¼å ä¸ºæ²¡æ¾å°åéçå·¥å·ï¼å æ­¤è¿æ¯åå©AIèªå·±å®ç°äºä¸ä¸ªèæ¬æ¥å®æè¿ä¸ªä»»å¡ï¼

```
#!/usr/bin/env python3
"""
IPv6é»å±åç°å·¥å· - ç±»ä¼¼arpingçNS/NAå®ç°
ä½¿ç¨Scapyåéåæ¥æ¶ICMPv6é»å±åç°æ¥æ
"""

import argparse
import time
from scapy.all import Ether, IPv6, ICMPv6ND_NS, ICMPv6ND_NA, srp, get_if_list

def send_ns(target_ip, iface=None, timeout=1, retry=1, verbose=False, dst_mac=None):
    """
    åéä¸ä¸ªNSæ¥æå¹¶ç­å¾ææNAååº
    :param target_ip: ç®æ IPv6å°å
    :param iface: ç½ç»æ¥å£åç§°
    :param timeout: è¶æ¶æ¶é´(ç§)
    :param retry: éè¯æ¬¡æ°(ä»å¨æ²¡ææ¶å°ä»»ä½ååºæ¶éè¯)
    :param verbose: è¯¦ç»è¾åºæ¨¡å¼
    :param dst_mac: ç®æ MACå°å(åæ­æ¨¡å¼)
    :return: ååºåè¡¨ [(src_ip, src_mac), ...] æ []
    """
    if iface and iface not in get_if_list():
        print(f"è­¦å: æ¥å£ {iface} ä¸å­å¨")
        return []

    dst_mac = dst_mac if dst_mac else "33:33:ff:00:00:00"
    ns_pkt = Ether(dst=dst_mac) / \
             IPv6(dst=target_ip) / \
             ICMPv6ND_NS(tgt=target_ip)

    if verbose:
        print("åéNSæ¥æ:")
        ns_pkt.show()

    all_responses = []

    for attempt in range(retry):
        if verbose:
            print(f"å°è¯ {attempt+1}/{retry}...")

        # åéä¸ä¸ªNSæ¥æå¹¶æ¶éææååºï¼å¨è¶æ¶æ¶é´åæç»­çå¬
        answered, unanswered = srp(ns_pkt, iface=iface, timeout=timeout, verbose=0, multi=True)

        # å¤çæææ¶å°çååº
        for sent, received in answered:
            if received.haslayer(ICMPv6ND_NA):
                src_ip = received[IPv6].src
                src_mac = received[Ether].src
                response_info = (src_ip, src_mac)
                all_responses.append(response_info)
                if verbose:
                    print(f"æ¶å°NAååº #{len(all_responses)}:")
                    received.show()

        # å¦ææ¶å°äºååºï¼å°±ä¸åéè¯
        if all_responses:
            if verbose:
                print(f"æ¶å° {len(all_responses)} ä¸ªNAååºï¼åæ­¢éè¯")
            break
        elif verbose:
            print("æ¬è½®æªæ¶å°ååº")

    return all_responses

def main():
    parser = argparse.ArgumentParser(description="IPv6é»å±åç°å·¥å·")
    parser.add_argument("target", help="ç®æ IPv6å°å")
    parser.add_argument("-i", "--iface", help="ç½ç»æ¥å£åç§°")
    parser.add_argument("-t", "--timeout", type=int, default=1,
                       help="è¶æ¶æ¶é´(ç§)")
    parser.add_argument("-c", "--count", type=int, default=1,
                       help="éè¯æ¬¡æ°(é»è®¤1æ¬¡ï¼ä»å¨æ ååºæ¶éè¯)")
    parser.add_argument("-v", "--verbose", action="store_true",
                       help="è¯¦ç»è¾åºæ¨¡å¼")
    parser.add_argument("-m", "--mac",
                       help="æå®ç®æ MACå°å(åæ­æ¨¡å¼)")
    args = parser.parse_args()

    if args.verbose:
        print("å¯ç¨ç½ç»æ¥å£:", ", ".join(get_if_list()))

    results = send_ns(args.target, args.iface, args.timeout,
                     args.count, args.verbose, args.mac)
    if results:
        print(f"\næ¶å° {len(results)} ä¸ªNAååº:")
        for i, (ip, mac) in enumerate(results, 1):
            print(f"  {i}. {args.target} çMACå°åæ¯ {mac} (æ¥èª {ip})")
    else:
        prin...