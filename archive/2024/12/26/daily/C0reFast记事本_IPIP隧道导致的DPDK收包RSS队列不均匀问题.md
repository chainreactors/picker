---
title: IPIP隧道导致的DPDK收包RSS队列不均匀问题
url: https://www.ichenfu.com/2024/12/25/rss-not-balanced-caused-by-ipip-tunnel/
source: C0reFast记事本
date: 2024-12-26
fetch_date: 2025-10-06T19:36:03.296289
---

# IPIP隧道导致的DPDK收包RSS队列不均匀问题

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

# IPIP茅職搂茅聛聯氓炉录猫聡麓莽職聞DPDK忙聰露氓聦聟RSS茅聵聼氓聢聴盲赂聧氓聺聡氓聦聙茅聴庐茅垄聵

氓聫聭猫隆篓盲潞聨
2024氓鹿麓12忙聹聢25忙聴楼 20:56

氓聢聠莽卤禄盲潞聨

[猫聶職忙聥聼氓聦聳](/categories/%E8%99%9A%E6%8B%9F%E5%8C%96/)

茅聵聟猫炉禄忙卢隆忙聲掳茂录職

忙聹聙猫驴聭莽潞驴盲赂聤氓聡潞莽聨掳盲赂聙盲潞聸VM莽陆聭氓聧隆忙聰露氓聦聟茅聵聼氓聢聴盲赂聧氓聺聡氓聦聙莽職聞茅聴庐茅垄聵茂录聦氓聧鲁盲陆驴忙聵炉氓掳聠莽陆聭氓聧隆茅聵聼氓聢聴盲赂颅忙聳颅氓聺聡氓聦聙莽職聞莽禄聭氓庐職氓聢掳氓聬聞盲赂陋CPU盲赂聤茂录聦盲戮聺莽聞露盲录職氓聡潞莽聨掳忙聼聬盲赂陋忙聽赂莽聣鹿氓聢芦茅芦聵莽職聞忙聝聟氓聠碌茂录職

```
%Cpu0  :  0.0 us,  0.0 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.9 hi,  0.9 si,  0.0 st
%Cpu1  :  0.0 us,  0.0 sy,  0.0 ni, 97.5 id,  0.0 wa,  0.8 hi,  1.7 si,  0.0 st
%Cpu2  :  0.0 us,  0.0 sy,  0.0 ni, 99.1 id,  0.0 wa,  0.0 hi,  0.9 si,  0.0 st
%Cpu3  :  0.9 us,  0.0 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.0 hi,  0.9 si,  0.0 st
%Cpu4  :  0.0 us,  0.0 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.0 hi,  1.7 si,  0.0 st
%Cpu5  :  0.0 us,  0.0 sy,  0.0 ni, 97.4 id,  0.0 wa,  0.9 hi,  1.7 si,  0.0 st
%Cpu6  :  0.0 us,  0.0 sy,  0.0 ni, 97.4 id,  0.0 wa,  0.9 hi,  1.7 si,  0.0 st
%Cpu7  :  0.0 us,  0.0 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.0 hi,  1.7 si,  0.0 st
%Cpu8  :  0.0 us,  0.0 sy,  0.0 ni, 46.3 id,  0.0 wa,  3.4 hi, 50.3 si,  0.0 st
%Cpu9  :  0.0 us,  0.0 sy,  0.0 ni, 97.4 id,  0.0 wa,  0.9 hi,  1.7 si,  0.0 st
%Cpu10 :  0.0 us,  0.0 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.0 hi,  1.7 si,  0.0 st
%Cpu11 :  0.0 us,  0.0 sy,  0.0 ni, 99.1 id,  0.0 wa,  0.0 hi,  0.9 si,  0.0 st
%Cpu12 :  0.0 us,  0.0 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.0 hi,  1.7 si,  0.0 st
%Cpu13 :  0.0 us,  0.0 sy,  0.0 ni, 99.1 id,  0.0 wa,  0.0 hi,  0.9 si,  0.0 st
%Cpu14 :  0.0 us,  0.0 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.0 hi,  1.7 si,  0.0 st
%Cpu15 :  0.0 us,  0.0 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.0 hi,  1.7 si,  0.0 st
```

猫聝陆莽聹聥氓聢掳氓聟露盲禄聳忙聽赂氓陇搂茅聝篓氓聢聠猫驴聵忙聵炉忙炉聰猫戮聝氓聺聡氓聦聙莽職聞茂录聦氓掳卤忙聵炉cpu8莽隆庐氓庐聻忙炉聰氓聟露盲禄聳忙聽赂茅芦聵氓戮聢氓陇職茫聙聜莽禄聫猫驴聡盲潞聠盲赂聙盲潞聸忙聨聮忙聼楼茂录聦氓聫聭莽聨掳氓聮聦VM盲陆驴莽聰篓盲潞聠`IPIP Tunnel`忙聹聣氓聟鲁茫聙聜

莽聰篓忙聢路莽職聞氓聹潞忙聶炉忙聵炉茂录聦氓聹篓莽陆聭莽禄聹氓聟楼氓聫拢氓陇聞忙聹聣盲赂聙氓聫掳忙聹潞氓聶篓氓聟聟氓陆聯猫麓聼猫陆陆氓聺聡猫隆隆莽職聞猫搂聮猫聣虏茂录聦莽聞露氓聬聨猫驴聶氓聫掳猫麓聼猫陆陆氓聺聡猫隆隆氓聠聧茅聙職猫驴聡`IPIP Tunnel`氓掳聠莽聰篓忙聢路莽職聞猫炉路忙卤聜猫陆卢氓聫聭氓聢掳猫驴聶氓聫掳VM茂录聦莽聰卤盲潞聨`IPIP`莽職聞氓聨聼莽聬聠忙聵炉氓聹篓氓聨聼忙聹聣莽職聞IP氓聦聟氓聼潞莽隆聙盲赂聤氓聠聧芒聙聹氓楼聴芒聙聺盲赂聙氓卤聜IP氓聦聟氓陇麓茂录聦氓炉录猫聡麓RSS猫庐隆莽庐聴莽職聞Hash莽職聞盲鹿聥氓聬聨氓聫陋猫聝陆莽聹聥氓聢掳氓陇聳氓卤聜莽職聞IP茂录聦忙聣聙盲禄楼氓聧鲁盲陆驴氓聠聟氓卤聜IP氓聦聟莽職聞盲潞聰氓聟聝莽禄聞氓聢聠氓赂聝茅聺聻氓赂赂氓聺聡氓聦聙茂录聦盲鹿聼盲录職氓聡潞莽聨掳忙聣聙盲禄楼茅職搂茅聛聯莽職聞忙碌聛茅聡聫茅聝陆猫路聭氓聢掳盲赂聙盲赂陋忙聽赂盲赂聤莽職聞忙聝聟氓聠碌茫聙聜

盲赂潞盲潞聠莽陆聭莽禄聹莽職聞莽聛碌忙麓禄忙聙搂茂录聦VM莽職聞莽陆聭莽禄聹忙碌聛茅聡聫茂录聦忙聵炉莽禄聫猫驴聡盲潞聠盲赂聙盲赂陋DPDK莽篓聥氓潞聫猫驴聸猫隆聦猫陆卢氓聫聭莽職聞茂录聦猫驴聶盲赂陋DPDK莽篓聥氓潞聫茅聙禄猫戮聭茅聺聻氓赂赂莽庐聙氓聧聲茂录聦氓掳卤忙聵炉盲禄聨莽陆聭氓聧隆氓炉鹿氓潞聰莽職聞rx茅聵聼氓聢聴N忙聨楼忙聰露忙聲掳忙聧庐氓聦聟茂录聦莽聞露氓聬聨氓聫聭茅聙聛氓聢掳VM氓炉鹿氓潞聰莽職聞rx茅聵聼氓聢聴N茂录聦氓聸聽忙颅陇氓娄聜忙聻聹VM莽職聞忙聨楼忙聰露茅聵聼氓聢聴盲赂聧氓鹿鲁猫隆隆茂录聦盲鹿聼氓掳卤忙聞聫氓聭鲁莽聺聙盲禄聨莽陆聭氓聧隆忙聰露氓聦聟莽職聞忙聴露氓聙聶氓掳卤忙聵炉盲赂聧氓聺聡氓聦聙莽職聞茫聙聜

茅聜拢忙聙聨盲鹿聢猫搂拢氓聠鲁猫驴聶盲赂陋茅聴庐茅垄聵氓聭垄茂录聦氓戮聢忙聵戮莽聞露莽職聞盲赂聙盲赂陋忙聙聺猫路炉忙聵炉茂录聦氓陆聯DPDK忙聰露氓聦聟盲鹿聥氓聬聨茂录聦茅聡聧忙聳掳猫庐隆莽庐聴盲赂聙盲赂聥忙聲掳忙聧庐氓聦聟莽職聞Hash茂录聦氓聹篓猫庐隆莽庐聴猫驴聡莽篓聥盲赂颅茂录聦氓娄聜忙聻聹氓聫聭莽聨掳忙聲掳忙聧庐氓聦聟忙聵炉盲赂聙盲赂陋IPIP忙聲掳忙聧庐氓聦聟茂录聦氓掳卤忙聦聣氓聠聟氓卤聜IP氓陇麓氓聨禄猫庐隆莽庐聴Hash茂录聦莽聞露氓聬聨氓聠聧忙聽鹿忙聧庐猫驴聶盲赂陋Hash猫庐隆莽庐聴VM莽職聞忙聨楼氓聫聴茅聵聼氓聢聴茂录聦氓鹿露忙聤聤氓聦聟猫陆卢氓聫聭氓聢掳氓炉鹿氓潞聰茅聵聼氓聢聴茫聙聜氓聹篓猫驴聶莽搂聧忙聝聟氓聠碌盲赂聥茂录聦盲赂聧莽庐隆盲禄聨莽陆聭氓聧隆忙聰露氓聦聟忙聵炉氓聬娄忙聵炉氓聺聡猫隆隆莽職聞茂录聦氓聢掳VM莽職聞忙碌聛茅聡聫氓聼潞忙聹卢氓掳卤盲录職忙聵炉氓聺聡猫隆隆莽職聞茫聙聜猫驴聶忙聽路莽隆庐氓庐聻盲录職茅聺聻氓赂赂莽聛碌忙麓禄茂录聢猫驴聶盲鹿聼忙聵炉氓陆聯忙聴露氓陇職氓聤聽盲赂聙氓卤聜DPDK猫聙聦盲赂聧忙聵炉莽聸麓忙聨楼莽陆聭氓聧隆莽聸麓茅聙職莽職聞氓聨聼氓聸聽茂录聣茂录聦盲陆聠氓戮聢忙聵戮莽聞露DPDK莽篓聥氓潞聫莽職聞猫庐隆莽庐聴茅聡聫氓垄聻氓聤聽盲潞聠茂录聦氓炉鹿忙聙搂猫聝陆盲录職忙聹聣盲赂聧氓掳聫莽職聞氓陆卤氓聯聧茫聙聜

茅聜拢莽陆聭氓聧隆猫聝陆盲赂聧猫聝陆忙聰炉忙聦聛茅聮聢氓炉鹿IPIP忙聲掳忙聧庐氓聦聟忙聫聬盲戮聸盲赂陋芒聙聹忙聸麓茅芦聵莽潞搂莽職聞芒聙聺RSS莽庐聴忙鲁聲氓聭垄茂录聼忙炉聲莽芦聼莽聨掳氓聹篓莽職聞莽陆聭氓聧隆氓聤聼猫聝陆莽聣鹿忙聙搂茅聝陆忙炉聰猫戮聝氓陇職茂录聦氓聤聼猫聝陆盲鹿聼忙炉聰猫戮聝氓录潞氓陇搂茂录聦氓戮聢忙聹聣氓聫炉猫聝陆氓聫炉盲禄楼莽聸麓忙聨楼氓聹篓莽陆聭氓聧隆氓卤聜茅聺垄莽聸麓忙聨楼氓庐聻莽聨掳忙聰炉忙聦聛氓聼潞盲潞聨茅職搂茅聛聯氓聠聟氓卤聜IP氓陇麓猫驴聸猫隆聦RSS莽職聞猫聝陆氓聤聸茂录聦氓娄聜忙聻聹猫聝陆茅聙職猫驴聡莽陆聭氓聧隆氓卤聜茅聺垄氓庐聻莽聨掳茂录聦茅聜拢忙聵炉忙聹聙盲录聵猫搂拢盲潞聠茫聙聜

猫路聼莽陆聭氓聧隆氓聨聜氓聲聠盲潞陇忙碌聛盲鹿聥氓聬聨茂录聦莽隆庐猫庐陇盲潞聠莽陆聭氓聧隆忙聵炉忙聰炉忙聦聛猫驴聶盲赂陋莽聣鹿忙聙搂莽職聞茂录聦猫聙聦盲赂聰茂录聦氓聹篓盲陆驴莽聰篓Linux茅漏卤氓聤篓忙聰露氓聦聟莽職聞忙聝聟氓聠碌盲赂聥茂录聦茅禄聵猫庐陇氓掳卤忙聵炉氓录聙氓聬炉莽職聞茂录聦盲鹿聼氓掳卤忙聵炉猫炉麓茂录聦氓娄聜忙聻聹盲陆驴莽聰篓莽職聞忙聵炉莽陆聭氓聧隆莽聸麓茅聙職莽職聞忙篓隆氓录聫茂录聦茅聜拢莽聸麓忙聨楼氓掳卤盲赂聧盲录職茅聛聡氓聢掳猫驴聶盲赂陋茅聴庐茅垄聵茫聙聜盲陆聠忙聢聭盲禄卢盲陆驴莽聰篓盲潞聠DPDK猫驴聸猫隆聦盲赂颅猫陆卢茂录聦茅禄聵猫庐陇忙聵炉忙虏隆忙聹聣猫驴聶盲赂陋猫隆聦盲赂潞莽職聞茂录聦氓娄聜忙聻聹猫娄聛氓录聙氓聬炉氓聼潞盲潞聨IPIP Tunnel氓聠聟氓卤聜IP氓陇麓猫驴聸猫隆聦RSS茂录聦茅聹聙猫娄聛莽禄聶莽陆聭氓聧隆盲赂聥氓聫聭猫驴聶忙聽路盲赂聙忙聺隆忙碌聛猫隆篓茂录職`flow create 0 group 0 ingress pattern eth / ipv4 proto is 4 / ipv4 / tcp / end actions rss queues 0 1 2 3 4 end level 2 / end`茫聙聜莽庐聙氓聧聲莽驴禄猫炉聭盲赂聙盲赂聥茂录聦氓掳卤忙聵炉茅聙職猫驴聡忙碌聛猫隆篓氓聨禄氓聦鹿茅聟聧`ipv4.proto == 4`(盲鹿聼氓掳卤忙聵炉IPIP Tunnel氓聧聫猫庐庐)莽職聞忙聲掳忙聧庐氓聦聟茂录聦氓鹿露猫庐漏莽陆聭氓聧隆盲禄楼氓聠聟氓卤聜IP猫驴聸猫隆聦rss茂录聦氓鹿露氓聢聠茅聟聧氓聢掳`0 1 2 3 4`猫驴聶氓聡聽盲赂陋茅聵聼氓聢聴盲赂颅茫聙聜

莽聼楼茅聛聯盲潞聠猫驴聶盲赂陋猫搂聞氓聢聶茂录聦忙聢聭盲禄卢氓掳卤氓聫炉盲禄楼莽聰篓`testpmd`忙碌聥猫炉聲盲赂聥盲潞聠茂录職

```
testpmd> set fwd rxonly
Set rxonly packet forwarding mode
testpmd>
testpmd> start
rxonly packet forwarding - ports=1 - cores=1 - streams=16 - NUMA support enabled, MP allocation mode: native
Logical Core 1 (socket 0) forwards packets on 16 streams:
  RX P=0/Q=0 (socket 0) -> TX P=0/Q=0 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=1 (socket 0) -> TX P=0/Q=1 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=2 (socket 0) -> TX P=0/Q=2 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=3 (socket 0) -> TX P=0/Q=3 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=4 (socket 0) -> TX P=0/Q=4 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=5 (socket 0) -> TX P=0/Q=5 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=6 (socket 0) -> TX P=0/Q=6 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=7 (socket 0) -> TX P=0/Q=7 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=8 (socket 0) -> TX P=0/Q=8 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=9 (socket 0) -> TX P=0/Q=9 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=10 (socket 0) -> TX P=0/Q=10 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=11 (socket 0) -> TX P=0/Q=11 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=12 (socket 0) -> TX P=0/Q=12 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=13 (socket 0) -> TX P=0/Q=13 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=14 (socket 0) -> TX P=0/Q=14 (socket 0) peer=02:00:00:00:00:00
  RX P=0/Q=15 (socket 0) -> TX P=0/Q=15 (socket 0) peer=02:00:00:00:00:00

  rxonly packet forwarding packets/burst=32
  nb forwarding cores=1 - nb forwarding ports=1
  port 0: RX queue number: 16 Tx queue number: 16
    Rx offloads=0x0 Tx offloads=0x10000
    RX queue: 0
      RX desc=4096 - RX free threshold=64
      RX threshold registers: pthresh=0 hthresh=0  wthresh=0
      RX Offloads=0x0
    TX queue: 0
      TX desc=4096 - TX free threshold=0
      TX threshold registers: pthresh=0 hthresh=0  wthresh=0
      TX offloads=0x10000 - TX RS bit threshold=0
testpmd> stop
Telling cores to stop...
Waiting for lcores to finish...

  ------- Forward Stats for RX Port= 0/Queue=12 -> TX Port= 0/Queue=12 -------
  RX-packets: 139389         TX-packets: 0              TX-dropped: 0

  ---------------------- Forward statistics for port 0  ----------------------
  RX-packets: 139389         RX-dropped: 0             RX-total: 139389
  TX-packets: 0              TX-dropped: 0             TX-total: 0
  ----------------------------------------------------------------------------

  +++++++++++++++ Accumulated forward statistics for all ports+++++++++++++++
  RX-packets: 139389         RX-dropped: 0             RX-total: 139389
  TX-packets: 0              TX-dropped: 0             TX-total: 0
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Done.
```

氓聫炉盲禄楼莽聹聥氓聢掳茅禄聵猫庐陇忙聝聟氓聠碌盲赂聥茂录聦忙聣聙忙聹聣莽職聞氓聦聟氓聟篓猫路聭氓聢掳`Queue=12`猫驴聶盲赂陋茅聵聼氓聢聴盲潞聠茫聙聜氓戮聢忙聵戮莽聞露茅禄聵猫庐陇忙聝聟氓聠碌盲赂聥RSS忙聵炉忙聹聣盲潞聸茅聴庐茅垄聵莽職聞茂录聦茅聜拢氓掳卤莽禄搂莽禄颅猫炉聲猫炉聲盲赂聥氓聫聭忙碌聛猫隆篓盲鹿聥氓聬聨莽職聞忙聝聟氓聠碌茂录職

```
testpmd> flow create 0 group 0 ingress pattern eth / ipv4 proto is 4 / ipv4 / tcp / end actions rss queues 0 1 2 3 4 5 6...