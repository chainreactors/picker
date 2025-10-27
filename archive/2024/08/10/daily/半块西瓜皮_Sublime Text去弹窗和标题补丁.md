---
title: Sublime Text去弹窗和标题补丁
url: https://guage.cool/sublime-patch.html
source: 半块西瓜皮
date: 2024-08-10
fetch_date: 2025-10-06T18:05:11.645439
---

# Sublime Text去弹窗和标题补丁

[![](/img/avatar.jpg)](/about/)[氓聧聤氓聺聴猫楼驴莽聯聹莽職庐](/)

忙虏隆忙聹聣忙聣戮氓聢掳氓聠聟氓庐鹿茂录聛

忙聹卢忙聳聡莽聸庐氓陆聲

1. [氓录鹿莽陋聴](#%E5%BC%B9%E7%AA%97)
   1. [猫隆楼盲赂聛](#%E8%A1%A5%E4%B8%81)
2. [忙聽聡茅垄聵](#%E6%A0%87%E9%A2%98)
   1. [猫隆楼盲赂聛](#%E8%A1%A5%E4%B8%81-1)
   2. [氓聢聽茅聶陇忙聥卢氓聫路](#%E5%88%A0%E9%99%A4%E6%8B%AC%E5%8F%B7)
   3. [氓聢聽茅聶陇忙聹陋忙鲁篓氓聠聦氓颅聴忙聽路](#%E5%88%A0%E9%99%A4%E6%9C%AA%E6%B3%A8%E5%86%8C%E5%AD%97%E6%A0%B7)
3. [氓聹篓莽潞驴猫隆楼盲赂聛](#%E5%9C%A8%E7%BA%BF%E8%A1%A5%E4%B8%81)

氓聸聻氓聢掳茅隆露茅聝篓氓聫聜盲赂聨猫庐篓猫庐潞

[![](data:image/png;base64...)](https://github.com/howmp)[![](data:image/png;base64...)](https://weibo.com/howmp)[![](data:image/png;base64...)](https://guage.cool/atom.xml)![](data:image/png;base64...)

[盲赂禄茅隆碌](/)
[忙聳聡莽芦聽](/)[茅聙聠氓聬聭](/categories/%E9%80%86%E5%90%91/)

氓聫聭氓赂聝盲潞聨茂录職2024-08-09忙聸麓忙聳掳盲潞聨茂录職2024-08-12

# Sublime Text氓聨禄氓录鹿莽陋聴氓聮聦忙聽聡茅垄聵猫隆楼盲赂聛

Sublime Text 忙聵炉盲赂聙盲赂陋忙聳聡忙聹卢莽录聳猫戮聭氓聶篓茂录聢忙聰露猫麓鹿猫陆炉盲禄露茂录聦氓聫炉盲禄楼忙聴聽茅聶聬忙聹聼猫炉聲莽聰篓茂录聣茂录聦氓聬聦忙聴露盲鹿聼忙聵炉盲赂聙盲赂陋氓聟聢猫驴聸莽職聞盲禄拢莽聽聛莽录聳猫戮聭氓聶篓茫聙聜氓聟聧猫麓鹿盲陆驴莽聰篓氓聮聦盲禄聵猫麓鹿氓聬聨盲赂禄猫娄聛忙聹聣盲赂陇莽聜鹿盲赂聧氓聬聦茂录聦盲赂聙忙聵炉氓庐職忙聹聼氓录鹿忙隆聠茂录聦盲潞聦忙聵炉忙聽聡茅垄聵忙聵戮莽陇潞unregistered氓颅聴忙聽路茫聙聜

茅聮聢氓炉鹿猫驴聶盲赂陇莽聜鹿猫驴聸猫隆聦茅聮聢氓炉鹿忙聙搂猫隆楼盲赂聛茂录聦氓聢聠忙聻聬猫驴聡莽篓聥氓娄聜盲赂聥

## 氓录鹿莽陋聴

茅聙職猫驴聡氓颅聴莽卢娄盲赂虏 芒聙聹Hello! Thanks芒聙娄芒聙聺氓庐職盲陆聧氓聢掳氓录鹿莽陋聴氓聡陆忙聲掳茂录聦忙聼楼忙聣戮盲潞陇氓聫聣氓录聲莽聰篓忙聣戮氓聢掳氓聟鲁茅聰庐氓聡陆忙聲掳

![](data:image/png;base64...)

### 猫隆楼盲赂聛

忙颅陇氓陇聞氓聫炉盲禄楼盲陆驴莽卢卢盲潞聦盲赂陋if氓聢陇忙聳颅忙聺隆盲禄露忙掳赂猫驴聹盲赂聧忙聢聬莽芦聥茂录聦氓聧鲁氓聫炉盲赂聧氓录鹿莽陋聴

| 忙聦聡盲禄陇 | 忙卤聡莽录聳 |
| --- | --- |
| 48 3D 80 CB A4 00 | cmp rax,A4CB80 |

盲驴庐忙聰鹿盲赂潞

| 忙聦聡盲禄陇 | 忙卤聡莽录聳 |
| --- | --- |
| 33 C0 | xor eax,eax |
| 83 F8 01 | cmp eax,1 |
| 90 | nop |

## 忙聽聡茅垄聵

茅聙職猫驴聡SetWindowTextW氓炉录氓聟楼氓聡陆忙聲掳氓庐職盲陆聧茂录聦忙聣戮氓聢掳忙聽聡茅垄聵猫庐戮莽陆庐氓聡陆忙聲掳

芒聙聹unregistered芒聙聺氓颅聴莽卢娄盲赂虏莽聰卤氓聸戮盲赂颅51猫隆聦氓录聜忙聢聳猫搂拢氓炉聠氓聡潞忙聺楼

![](data:image/png;base64...)

### 猫隆楼盲赂聛

a4盲赂潞盲赂聙盲赂陋BYTE,氓聟露盲赂颅莽卢卢盲潞聦盲赂陋bit盲陆聧猫隆篓莽陇潞忙聹陋忙驴聙忙麓禄

### 氓聢聽茅聶陇忙聥卢氓聫路

盲驴庐忙聰鹿盲赂陇氓陇聞 a4 & 0x3E 盲赂潞 a4 & 0x3C茂录聦忙聹陋忙鲁篓氓聠聦忙聴露盲赂聧忙聵戮莽陇潞忙聥卢氓聫路

| 忙聦聡盲禄陇 | 忙卤聡莽录聳 |
| --- | --- |
| 41 F6 C4 3E | test 12b,3E |

盲驴庐忙聰鹿盲赂潞

| 忙聦聡盲禄陇 | 忙卤聡莽录聳 |
| --- | --- |
| 41 F6 C4 3C | test 12b,3C |

### 氓聢聽茅聶陇忙聹陋忙鲁篓氓聠聦氓颅聴忙聽路

盲驴庐忙聰鹿a4 & 2 盲赂潞 a4 & 0茂录聦盲赂聧氓聠聧忙聵戮莽陇潞忙聹陋忙鲁篓氓聠聦

| 忙聦聡盲禄陇 | 忙卤聡莽录聳 |
| --- | --- |
| 41 F6 C4 02 | test 12b,2 |

盲驴庐忙聰鹿盲赂潞

| 忙聦聡盲禄陇 | 忙卤聡莽录聳 |
| --- | --- |
| 41 F6 C4 00 | test 12b,0 |

## 氓聹篓莽潞驴猫隆楼盲赂聛

忙聢聭氓聠聶盲潞聠盲赂聙盲赂陋莽陆聭茅隆碌茂录聦氓聫炉盲禄楼氓聹篓莽潞驴忙聣聯猫隆楼盲赂聛茂录聦莽聸庐氓聣聧忙聰炉忙聦聛windows x64 4180氓聮聦windows x64 4169盲赂陇盲赂陋莽聣聢忙聹卢

<https://www.guage.cool/tool/sublime/index.html>

猫庐赂氓聫炉氓聧聫猫庐庐

忙聹卢忙聳聡茅聡聡莽聰篓 [莽陆虏氓聬聧-茅聺聻氓聲聠盲赂職忙聙搂盲陆驴莽聰篓-莽聸赂氓聬聦忙聳鹿氓录聫氓聟卤盲潞芦 4.0 氓聸陆茅聶聟](https://creativecommons.org/licenses/by-nc-sa/4.0/) 猫庐赂氓聫炉氓聧聫猫庐庐茂录聦猫陆卢猫陆陆猫炉路忙鲁篓忙聵聨氓聡潞氓陇聞茫聙聜

猫戮聝忙聳掳忙聳聡莽芦聽

[grs-茅聙職猫驴聡REALITY氓聧聫猫庐庐氓庐聻莽聨掳莽職聞氓聠聟莽陆聭莽漏驴茅聙聫氓路楼氓聟路](/grs-tunnel-via-reality.html)

猫戮聝忙聴漏忙聳聡莽芦聽

[ASP.NET盲赂聥Webshell莽录聳猫炉聭盲潞搂莽聣漏氓聟聧忙聺聙](/dotnet-webshell-bypassav.html)

氓驴芦忙聺楼氓聫聜盲赂聨猫庐篓猫庐潞氓聬搂~

---

[茅聶聲ICP氓陇聡2021003897氓聫路](https://beian.miit.gov.cn/) | Powered By [hexo](https://hexo.io/) and [Stellar](https://github.com/xaoxuu/hexo-theme-stellar)

忙聹聙猫驴聭忙聸麓忙聳掳

[BeaconKiller茅聮聢氓炉鹿http/https莽職聞beacon莽職聞忙拢聙忙碌聥氓路楼氓聟路](/beaconkiller.html)[WinDump-氓聬聨忙赂聴茅聙聫盲驴隆忙聛炉/氓炉聠莽聽聛/氓聡颅猫炉聛忙聰露茅聸聠氓路楼氓聟路](/windump.html)[氓聹篓cron盲赂颅忙路禄氓聤聽茅職聬猫聴聫猫庐隆氓聢聮盲禄禄氓聤隆](/cron-hide.html)[莽聰篓zig氓庐聻莽聨掳莽庐聙忙聵聯donut](/zig-3-donut.html)[IIS盲赂聥web.config氓聢漏莽聰篓](/iis-web-config.html)

忙聽聡莽颅戮盲潞聭

[glibc](/tags/glibc/) [node](/tags/node/) [jsc](/tags/jsc/) [sublime](/tags/sublime/) [茅職聬猫聴聫](/tags/%E9%9A%90%E8%97%8F/) [猫掳聝猫炉聲](/tags/%E8%B0%83%E8%AF%95/) [password](/tags/password/) [BOF](/tags/BOF/) [pyoxidizer](/tags/pyoxidizer/) [莽拢聛莽聸聵](/tags/%E7%A3%81%E7%9B%98/) [忙聨聣莽潞驴](/tags/%E6%8E%89%E7%BA%BF/) [忙聺聝茅聶聬莽禄麓忙聦聛](/tags/%E6%9D%83%E9%99%90%E7%BB%B4%E6%8C%81/) [bypassav](/tags/bypassav/) [猫聡麓猫驴聹](/tags/%E8%87%B4%E8%BF%9C/) [webshell](/tags/webshell/) [氓聼聼忙聨搂](/tags/%E5%9F%9F%E6%8E%A7/) [VSCode](/tags/VSCode/) [盲禄拢莽聽聛氓庐隆猫庐隆](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [MESSAGE\_MAP](/tags/MESSAGE-MAP/) [盲禄拢莽聬聠](/tags/%E4%BB%A3%E7%90%86/) [VPN](/tags/VPN/) [MFC](/tags/MFC/) [氓颅聴猫聤聜莽聽聛](/tags/%E5%AD%97%E8%8A%82%E7%A0%81/) [COM](/tags/COM/) [fakesh](/tags/fakesh/) [Java](/tags/Java/) [shellcode](/tags/shellcode/) [PHP](/tags/PHP/) [donut](/tags/donut/) [docker](/tags/docker/) [processhacker](/tags/processhacker/) [IIS](/tags/IIS/) [猫聶職忙聥聼忙聹潞](/tags/%E8%99%9A%E6%8B%9F%E6%9C%BA/) [CobaltStrike](/tags/CobaltStrike/) [aspose](/tags/aspose/) [dotnet](/tags/dotnet/) [iis](/tags/iis/) [氓聤聽茅聙聼盲鹿聬](/tags/%E5%8A%A0%E9%80%9F%E4%B9%90/) [openvpn](/tags/openvpn/) [盲驴隆忙聛炉忙聰露茅聸聠](/tags/%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86/) [COFF](/tags/COFF/) [pyinstaller](/tags/pyinstaller/) [Donut](/tags/Donut/) [氓聫聧莽聢卢](/tags/%E5%8F%8D%E7%88%AC/) [zig](/tags/zig/) [report](/tags/report/) [socks5](/tags/socks5/) [wiz](/tags/wiz/) [ssh](/tags/ssh/) [beacon](/tags/beacon/) [seeyon](/tags/seeyon/) [srdi](/tags/srdi/) [cron](/tags/cron/) [python](/tags/python/) [cobaltstrike](/tags/cobaltstrike/) [氓聠聟莽陆聭莽漏驴茅聙聫](/tags/%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F/) [忙聴楼氓驴聴](/tags/%E6%97%A5%E5%BF%97/) [pty](/tags/pty/) [v8](/tags/v8/)