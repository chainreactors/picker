---
title: 一个中断关闭时间太长导致的网络延迟问题
url: https://www.ichenfu.com/2025/05/10/a-network-latency-problem/
source: C0reFast记事本
date: 2025-05-11
fetch_date: 2025-10-06T22:24:01.067737
---

# 一个中断关闭时间太长导致的网络延迟问题

[C0reFast猫庐掳盲潞聥忙聹卢](/)

to inspire confidence in somebody.

* [茅娄聳茅隆碌](/)
* [氓聢聠莽卤禄](/categories/)
* [氓陆聮忙隆拢](/archives/)
* [忙聽聡莽颅戮](/tags/)
* [氓聟鲁盲潞聨](/about/)
* 忙聬聹莽麓垄

* 忙聳聡莽芦聽莽聸庐氓陆聲
* 莽芦聶莽聜鹿忙娄聜猫搂聢

茅聶聢氓颅職

[111
忙聴楼氓驴聴](/archives/)

[15
氓聢聠莽卤禄](/categories/)

[249
忙聽聡莽颅戮](/tags/)

[GitHub](https://github.com/C0reFast "GitHub 芒聠聮 https://github.com/C0reFast")

E-Mail

[Weibo](https://weibo.com/c0refast "Weibo 芒聠聮 https://weibo.com/c0refast")

猫碌聻氓聤漏氓聲聠

茅聯戮忙聨楼

* [莽聢卤氓录聙忙潞聬](https://www.aikaiyuan.com/ "https://www.aikaiyuan.com/")
* [盲赂聙氓聠聣氓聠聧](https://blog.yiranzai.top/ "https://blog.yiranzai.top/")
* [PikachuWorld](https://www.cnblogs.com/pikachuworld/ "https://www.cnblogs.com/pikachuworld/")

# 盲赂聙盲赂陋盲赂颅忙聳颅氓聟鲁茅聴颅忙聴露茅聴麓氓陇陋茅聲驴氓炉录猫聡麓莽職聞莽陆聭莽禄聹氓禄露猫驴聼茅聴庐茅垄聵

氓聫聭猫隆篓盲潞聨
2025氓鹿麓5忙聹聢10忙聴楼 11:15

氓聢聠莽卤禄盲潞聨

[Linux](/categories/Linux/)

茅聵聟猫炉禄忙卢隆忙聲掳茂录職

猫驴聭忙聹聼莽潞驴盲赂聤氓聡潞莽聨掳盲潞聠盲赂聙盲赂陋茅聴庐茅垄聵茂录聦莽聨掳猫卤隆忙聵炉忙聹聣盲赂聙氓聫掳忙聹潞氓聶篓茂录聦莽陆聭莽禄聹氓聡潞莽聨掳盲潞聠盲赂聧氓庐職忙聴露莽職聞氓禄露猫驴聼茂录職

```
# ping -i 0.05 192.168.0.5
#...
64 bytes from 192.168.0.5: icmp_seq=673 ttl=63 time=0.203 ms
64 bytes from 192.168.0.5: icmp_seq=674 ttl=63 time=0.210 ms
64 bytes from 192.168.0.5: icmp_seq=675 ttl=63 time=0.218 ms
64 bytes from 192.168.0.5: icmp_seq=676 ttl=63 time=0.233 ms
64 bytes from 192.168.0.5: icmp_seq=677 ttl=63 time=406 ms
64 bytes from 192.168.0.5: icmp_seq=678 ttl=63 time=354 ms
64 bytes from 192.168.0.5: icmp_seq=679 ttl=63 time=302 ms
64 bytes from 192.168.0.5: icmp_seq=680 ttl=63 time=251 ms
64 bytes from 192.168.0.5: icmp_seq=681 ttl=63 time=199 ms
64 bytes from 192.168.0.5: icmp_seq=682 ttl=63 time=147 ms
64 bytes from 192.168.0.5: icmp_seq=683 ttl=63 time=94.8 ms
64 bytes from 192.168.0.5: icmp_seq=684 ttl=63 time=43.0 ms
64 bytes from 192.168.0.5: icmp_seq=685 ttl=63 time=0.216 ms
64 bytes from 192.168.0.5: icmp_seq=686 ttl=63 time=0.248 ms
#...
```

盲禄楼50ms盲赂潞茅聴麓茅職聰ping茂录聦氓聫聭莽聨掳忙娄聜莽聨聡忙聙搂莽職聞盲录職氓聡潞莽聨掳猫露聟猫驴聡400ms莽職聞氓禄露猫驴聼茂录聦盲陆聠忙聵炉氓鹿露忙虏隆忙聹聣盲赂垄氓聦聟莽職聞莽聨掳猫卤隆氓聫聭莽聰聼茫聙聜

茅娄聳氓聟聢忙聝鲁氓聢掳盲潞聠盲陆驴莽聰篓[nettrace](https://github.com/OpenCloudOS/nettrace)氓路楼氓聟路忙聺楼氓聢聠忙聻聬盲赂聙盲赂聥猫驴聶盲赂陋茅聴庐茅垄聵茂录聦`nettrace`忙聵炉盲赂聙盲赂陋猫聟戮猫庐炉氓录聙忙潞聬莽職聞氓聼潞盲潞聨`bpftrace`莽職聞莽陆聭莽禄聹忙碌聛茅聡聫猫驴陆猫赂陋氓路楼氓聟路茂录聦氓聫炉盲禄楼猫驴陆猫赂陋氓聢掳氓聠聟忙聽赂莽陆聭莽禄聹忙聽聢莽職聞忙炉聫盲赂聙盲赂陋氓聡陆忙聲掳猫掳聝莽聰篓茫聙聜忙聹聼忙聹聸猫聝陆茅聙職猫驴聡猫驴聶盲赂陋氓路楼氓聟路忙聺楼莽聹聥盲赂聙盲赂聥猫驴聶盲赂陋氓禄露猫驴聼忙聵炉盲赂聧忙聵炉忙露聢猫聙聴氓聹篓盲潞聠氓聠聟忙聽赂莽職聞莽陆聭莽禄聹氓聧聫猫庐庐忙聽聢盲赂聤茫聙聜忙聽鹿忙聧庐ping莽禄聯忙聻聹盲赂颅氓聯聧氓潞聰忙聴露茅聴麓忙聹聙茅聲驴莽職聞seq=677莽職聞氓聦聟茂录聦猫驴聡忙禄陇氓聡潞忙聺楼盲禄聨氓聧聫猫庐庐忙聽聢忙聨楼忙聰露氓聦聟氓聢掳氓聫聭茅聙聛氓聸聻氓陇聧氓聦聟莽職聞忙聣聙忙聹聣氓聡陆忙聲掳猫掳聝莽聰篓茂录職

```
# nettrace -p icmp
#...
***************** d8061b00 ***************
[24583464.629102] [napi_gro_receive_entry] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629114] [dev_gro_receive     ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629248] [__netif_receive_skb_core] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629253] [packet_rcv          ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629256] [tcf_classify        ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629262] [__netif_receive_skb_core] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629268] [ip_rcv              ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629271] [ip_rcv_core         ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629276] [nf_hook_slow        ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392 *ipv4 in chain: PRE_ROUTING*
[24583464.629284] [ip_route_input_slow ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629293] [fib_validate_source ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629299] [ip_local_deliver    ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629301] [nf_hook_slow        ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392 *ipv4 in chain: INPUT*
[24583464.629304] [nft_do_chain        ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392 *iptables table:filter, chain:INPUT*
[24583464.629311] [ip_local_deliver_finish] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629316] [icmp_rcv            ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629321] [icmp_echo           ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629325] [icmp_reply          ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392
[24583464.629413] [consume_skb         ] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 677, id: 392 *packet is freed (normally)*
#...
***************** a3faf500,a3faec00,a3faf800 ***************
[24583464.629343] [__ip_local_out      ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629347] [nf_hook_slow        ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392 *ipv4 in chain: OUTPUT*
[24583464.629350] [nft_do_chain        ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392 *iptables table:filter, chain:OUTPUT*
[24583464.629354] [ip_output           ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629358] [nf_hook_slow        ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392 *ipv4 in chain: POST_ROUTING*
[24583464.629361] [ip_finish_output    ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629365] [ip_finish_output2   ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629368] [__dev_queue_xmit    ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629372] [tcf_classify        ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629376] [skb_clone           ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629381] [__dev_queue_xmit    ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629385] [dev_hard_start_xmit ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392 *skb is successfully sent to the NIC driver*
[24583464.629389] [bond_dev_queue_xmit ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629393] [__dev_queue_xmit    ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629396] [dev_hard_start_xmit ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392 *skb is successfully sent to the NIC driver*
[24583464.629398] [skb_clone           ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629401] [packet_rcv          ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392
[24583464.629404] [consume_skb         ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392 *packet is freed (normally)*
[24583464.629409] [consume_skb         ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392 *packet is freed (normally)*
[24583464.630375] [consume_skb         ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 677, id: 392 *packet is freed (normally)*
#...
```

盲禄聨猫驴聡忙禄陇氓聡潞忙聺楼莽職聞莽禄聯忙聻聹莽聹聥茂录聦忙聹聙氓路娄盲戮搂莽職聞忙聴露茅聴麓盲赂聙忙聽聫茂录聦氓聫聭莽聨掳盲禄聨忙聨楼氓聫聴icmp猫炉路忙卤聜氓聢掳氓掳聠氓聸聻氓陇聧猫炉路忙卤聜忙聣聰莽禄聶莽陆聭氓聧隆茂录聦忙聲麓盲赂陋氓聧聫猫庐庐忙聽聢氓聫陋忙露聢猫聙聴盲潞聠盲赂聧氓聢掳1ms莽職聞忙聴露茅聴麓茂录聦氓聡聽盲鹿聨氓聫炉盲禄楼忙聨聮茅聶陇忙聵炉氓聠聟忙聽赂莽陆聭莽禄聹氓聧聫猫庐庐忙聽聢莽職聞茅聴庐茅垄聵茫聙聜茅聜拢忙聵炉忙聙聨盲鹿聢氓聸聻盲潞聥氓聭垄茂录聼

氓掳聺猫炉聲莽禄搂莽禄颅氓聢聠忙聻聬盲赂聙盲赂聥`nettrace`氓路楼氓聟路莽職聞猫戮聯氓聡潞茂录職

```
# grep -E 'napi_gro_receive_entry|__ip_local_out' trace.log
#...
[24583464.120360] [napi_gro_receive_entry] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 675, id: 392
[24583464.120449] [__ip_local_out      ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 675, id: 392
[24583464.172360] [napi_gro_receive_entry] ICMP: 192.168.0.4 -> 192.168.0.5 ping request, seq: 676, id: 392
[24583464.172456] [__ip_local_out      ] ICMP: 192.168.0.5 -> 192.168.0.4 ping reply, seq: 676, id: 392
# 盲赂聤忙卢隆氓聸聻氓陇聧盲鹿聥氓聬聨茂录聦氓陇搂莽潞娄莽颅聣氓戮聟盲潞聠450ms茂录聦忙聣聧莽禄搂莽禄颅忙聰露氓聢掳盲赂聥盲赂聙盲赂陋ping氓聦聟茂录聦氓鹿露盲赂聰氓聹篓氓聬聦1ms氓聠聟猫驴聻莽禄颅忙聰露氓聢掳盲潞聠8盲赂陋氓聦聟
[2458346...