---
title: 用zig实现简易donut
url: https://guage.cool/zig-3-donut.html
source: 半块西瓜皮
date: 2025-04-19
fetch_date: 2025-10-06T22:06:36.662944
---

# 用zig实现简易donut

[![](/img/avatar.jpg)](/about/)[氓聧聤氓聺聴猫楼驴莽聯聹莽職庐](/)

忙虏隆忙聹聣忙聣戮氓聢掳氓聠聟氓庐鹿茂录聛

忙聹卢忙聳聡莽聸庐氓陆聲

1. [氓聣聧猫篓聙](#%E5%89%8D%E8%A8%80)
2. [忙聳掳莽聣鹿忙聙搂](#%E6%96%B0%E7%89%B9%E6%80%A7)
3. [盲赂禄猫娄聛忙碌聛莽篓聥](#%E4%B8%BB%E8%A6%81%E6%B5%81%E7%A8%8B)
   1. [氓聤聽氓炉聠/猫搂拢氓炉聠](#%E5%8A%A0%E5%AF%86-%E8%A7%A3%E5%AF%86)
   2. [氓聨聥莽录漏/猫搂拢氓聨聥](#%E5%8E%8B%E7%BC%A9-%E8%A7%A3%E5%8E%8B)
   3. [茅聺聶忙聙聛TLS忙聰炉忙聦聛莽職聞氓庐聻莽聨掳](#%E9%9D%99%E6%80%81TLS%E6%94%AF%E6%8C%81%E7%9A%84%E5%AE%9E%E7%8E%B0)
      1. [32盲陆聧莽職聞忙聝聟氓聠碌](#32%E4%BD%8D%E7%9A%84%E6%83%85%E5%86%B5)
      2. [64盲陆聧莽職聞忙聝聟氓聠碌](#64%E4%BD%8D%E7%9A%84%E6%83%85%E5%86%B5)
   4. [莽聰篓zig氓聠聶shellcode](#%E7%94%A8zig%E5%86%99shellcode)

氓聸聻氓聢掳茅隆露茅聝篓氓聫聜盲赂聨猫庐篓猫庐潞

[![](data:image/png;base64...)](https://github.com/howmp)[![](data:image/png;base64...)](https://weibo.com/howmp)[![](data:image/png;base64...)](https://guage.cool/atom.xml)![](data:image/png;base64...)

[盲赂禄茅隆碌](/)
[忙聳聡莽芦聽](/)[莽录聳莽篓聥](/categories/%E7%BC%96%E7%A8%8B/)  [氓聟聧忙聺聙](/categories/%E7%BC%96%E7%A8%8B/%E5%85%8D%E6%9D%80/)

氓聫聭氓赂聝盲潞聨茂录職2025-04-18忙聸麓忙聳掳盲潞聨茂录職2025-04-18

# 莽聰篓zig氓庐聻莽聨掳莽庐聙忙聵聯donut

## 氓聣聧猫篓聙

盲鹿聥氓聣聧氓聢聠忙聻聬猫驴聡donut莽聰聼忙聢聬shellcode猫垄芦忙聺聙茅聴庐茅垄聵茂录聦氓鹿露茅聙職猫驴聡ollvm忙路路忙路聠氓聟露Loader

猫炉娄猫搂聛: <https://guage.cool/donutbypassav.html>

氓庐聻茅聶聟盲赂聤donut莽職聞Loader氓聫炉盲禄楼氓聤聽猫陆陆exe/dll/.NET Assemblies/VBScript/JScript

茅聙職氓赂赂忙聝聟氓聠碌忙聢聭盲禄卢盲陆驴莽聰篓忙聸麓氓陇職莽職聞猫驴聵忙聵炉exe/dll茂录聦盲赂潞盲潞聠莽虏戮莽庐聙Loader氓陇搂氓掳聫茂录聦盲鹿聼盲赂潞盲潞聠茅垄聞茅聵虏donut氓聠聧忙卢隆猫垄芦忙聺聙

忙聢聭忙聣聯莽庐聴莽聰篓zig氓庐聻莽聨掳盲潞聠盲赂聙盲赂陋莽庐聙忙聵聯莽聣聢莽職聞donut茂录聦氓聫炉盲禄楼氓掳聠盲禄禄忙聞聫exe/dll猫陆卢忙聧垄盲赂潞shellcode茂录聦氓鹿露忙路禄氓聤聽盲潞聠盲赂聙盲潞聸忙聳掳莽聣鹿忙聙搂

## 忙聳掳莽聣鹿忙聙搂

1. 茅聺聶忙聙聛TLS莽職聞忙聰炉忙聦聛(忙炉聰氓娄聜rust莽職聞exe/dll)茂录聦莽聸庐氓聣聧氓聫陋忙聹聣IoM/c3/MemoryModulePP莽颅聣忙聰炉忙聦聛茅聝篓氓聢聠忙聯聧盲陆聹莽鲁禄莽禄聼
2. 忙虏隆忙聹聣茅聡聧氓庐職盲陆聧猫隆篓忙聴露茂录聦盲录職氓掳聺猫炉聲忙聽鹿忙聧庐ImageBase莽聰鲁猫炉路氓聠聟氓颅聵
3. 忙聸麓氓陆禄氓潞聲莽職聞忙聯娄茅聶陇茂录聦茅聶陇盲潞聠忙聯娄茅聶陇PE氓陇麓盲鹿聥氓陇聳茂录聦猫驴聵忙聯娄茅聶陇盲潞聠氓炉录氓聟楼猫隆篓
4. 茅聙職猫驴聡ollvm莽聰聼忙聢聬忙路路忙路聠Loader(忙職聜忙聹陋氓聟卢氓录聙)

## 盲赂禄猫娄聛忙碌聛莽篓聥

1. Loader茅聝篓氓聢聠
   1. 忙聽鹿忙聧庐忙聲掳忙聧庐茂录聦猫搂拢氓炉聠氓鹿露猫搂拢氓聨聥忙聲掳忙聧庐
   2. 茅聙職猫驴聡PELoader氓聤聽猫陆陆exe/dll
2. 莽聰聼忙聢聬氓聶篓茅聝篓氓聢聠
   1. 猫炉禄氓聫聳exe/dll茂录聦氓鹿露氓聢陇忙聳颅忙聵炉氓聬娄64bit
   2. 莽聰聼忙聢聬氓鹿露氓聠聶氓聡潞shellcode
      1. 忙路禄氓聤聽氓炉鹿氓潞聰猫聡陋氓庐職盲陆聧忙卤聡莽录聳忙聦聡盲禄陇
      2. 忙路禄氓聤聽exe/dll莽職聞氓聨聥莽录漏氓聤聽氓炉聠忙聲掳忙聧庐
      3. 忙路禄氓聤聽氓炉鹿氓潞聰Loader莽職聞shellcode

### 氓聤聽氓炉聠/猫搂拢氓炉聠

茅聙職猫驴聡16氓颅聴猫聤聜key猫驴聸猫隆聦氓录聜忙聢聳氓聤聽猫搂拢氓炉聠

### 氓聨聥莽录漏/猫搂拢氓聨聥

盲陆驴莽聰篓aPlib茂录聦猫驴聶盲鹿聼忙聵炉donut盲陆驴莽聰篓莽職聞莽庐聴忙鲁聲 <https://ibsensoftware.com/products_aPLib.html>

氓聙录氓戮聴盲赂聙忙聫聬莽職聞忙聵炉忙聦聣莽聟搂氓庐聵忙聳鹿猫炉麓忙鲁聲猫搂拢氓炉聠莽庐聴忙鲁聲氓聫陋忙聹聣169氓颅聴猫聤聜茂录聦氓戮聢氓陇職氓聨聥莽录漏氓拢鲁盲鹿聼盲陆驴莽聰篓猫驴聶莽搂聧莽庐聴忙鲁聲

氓聟露猫搂拢氓炉聠莽庐聴忙鲁聲氓录聙忙潞聬茂录聦盲陆聠氓聨聥莽录漏莽庐聴忙鲁聲氓聫陋忙聫聬盲戮聸茅聺聶忙聙聛/氓聤篓忙聙聛氓潞聯

氓楼陆氓聹篓氓录聙忙潞聬氓潞聯apultra氓庐聻莽聨掳盲潞聠氓聨聥莽录漏莽聨聡忙聸麓茅芦聵茂录聦氓鹿露盲赂聰氓聟录氓庐鹿aPlib猫搂拢氓聨聥莽庐聴忙鲁聲

<https://github.com/emmanuel-marty/apultra>

### 茅聺聶忙聙聛TLS忙聰炉忙聦聛莽職聞氓庐聻莽聨掳

LdrpHandleTlsData氓聡陆忙聲掳盲赂禄猫娄聛莽聰篓盲潞聨猫搂拢氓聠鲁sRDI盲赂颅茅聺聶忙聙聛TLS茅聴庐茅垄聵

#### 32盲陆聧莽職聞忙聝聟氓聠碌

1. 氓聟聢氓庐職盲陆聧氓颅聴莽卢娄盲赂虏LdrpHandleTlsData莽職聞氓聹掳氓聺聙
2. 氓庐職盲陆聧氓聢掳忙聦聡盲禄陇`push LdrpHandleTlsDataAddr`莽職聞氓聹掳氓聺聙
   1. 氓聧鲁氓聫炉氓戮聴氓聢掳LdrpHandleTlsData盲赂颅莽職聞氓录聜氓赂赂氓陇聞莽聬聠氓聡陆忙聲掳
   2. 猫驴聶盲赂陋氓录聜氓赂赂氓聡陆忙聲掳氓聹掳氓聺聙猫垄芦氓录聲莽聰篓盲潞聨EH4\_SCOPETABLE盲赂颅
3. 氓庐職盲陆聧EH4\_SCOPETABLE莽職聞氓聹掳氓聺聙
   1. 忙颅陇氓聹掳氓聺聙猫垄芦莽聸麓忙聨楼氓录聲莽聰篓盲潞聨LdrpHandleTlsData氓聡陆忙聲掳盲赂颅
4. 氓庐職盲陆聧忙聦聡盲禄陇`push EH4_SCOPETABLEAddr`氓聧鲁氓聫炉氓庐職盲陆聧氓聢掳LdrpHandleTlsData氓聡陆忙聲掳氓聹掳氓聺聙

#### 64盲陆聧莽職聞忙聝聟氓聠碌

32盲陆聧盲赂聥氓录聜氓赂赂莽聸赂氓聟鲁莽禄聯忙聻聞忙聵炉盲驴聺氓颅聵氓聹篓忙聽聢盲赂颅茂录聦猫聙聦64盲陆聧盲赂聥忙聵炉茅聙職猫驴聡PE莽禄聯忙聻聞盲赂颅莽職聞氓录聜氓赂赂猫隆篓

1. 氓聟聢氓庐職盲陆聧氓颅聴莽卢娄盲赂虏LdrpHandleTlsData莽職聞氓聹掳氓聺聙
2. 氓庐職盲陆聧氓聢掳忙聦聡盲禄陇`lea rdx, LdrpHandleTlsDataAddr`莽職聞氓聹掳氓聺聙
   1. 氓聧鲁氓聫炉氓戮聴氓聢掳LdrpHandleTlsData盲赂颅莽職聞氓录聜氓赂赂氓陇聞莽聬聠氓聡陆忙聲掳
   2. 猫驴聶盲赂陋氓录聜氓赂赂氓聡陆忙聲掳氓聹掳氓聺聙猫垄芦氓录聲莽聰篓盲潞聨C\_SCOPE\_TABLE盲赂颅
3. 氓庐職盲陆聧C\_SCOPE\_TABLE莽禄聯忙聻聞莽職聞氓聹掳氓聺聙
   1. 盲鹿聼氓掳卤氓庐職盲陆聧氓聢掳UNWIND\_INFO莽禄聯忙聻聞莽職聞氓聹掳氓聺聙
   2. UNWIND\_INFO莽禄聯忙聻聞莽職聞氓聹掳氓聺聙猫垄芦氓录聲莽聰篓盲潞聨RUNTIME\_FUNCTION莽禄聯忙聻聞盲赂颅
4. 氓庐職盲陆聧RUNTIME\_FUNCTION莽禄聯忙聻聞氓聹掳氓聺聙茂录聦氓聧鲁氓聫炉忙聣戮氓聢掳LdrpHandleTlsData氓聡陆忙聲掳氓聹掳氓聺聙

猫炉娄猫搂聛茂录職<https://github.com/howmp/LdrpHandleTlsData>
氓聫聜猫聙聝茂录職<https://chainreactors.github.io/wiki/blog/2025/01/07/IoM_advanced_TLS/>

### 莽聰篓zig氓聠聶shellcode

猫炉娄猫搂聛: <https://guage.cool/zig-2-windows-shellcode.html>

猫庐赂氓聫炉氓聧聫猫庐庐

忙聹卢忙聳聡茅聡聡莽聰篓 [莽陆虏氓聬聧-茅聺聻氓聲聠盲赂職忙聙搂盲陆驴莽聰篓-莽聸赂氓聬聦忙聳鹿氓录聫氓聟卤盲潞芦 4.0 氓聸陆茅聶聟](https://creativecommons.org/licenses/by-nc-sa/4.0/) 猫庐赂氓聫炉氓聧聫猫庐庐茂录聦猫陆卢猫陆陆猫炉路忙鲁篓忙聵聨氓聡潞氓陇聞茫聙聜

猫戮聝忙聳掳忙聳聡莽芦聽

[氓聹篓cron盲赂颅忙路禄氓聤聽茅職聬猫聴聫猫庐隆氓聢聮盲禄禄氓聤隆](/cron-hide.html)

猫戮聝忙聴漏忙聳聡莽芦聽

[IIS盲赂聥web.config氓聢漏莽聰篓](/iis-web-config.html)

氓驴芦忙聺楼氓聫聜盲赂聨猫庐篓猫庐潞氓聬搂~

---

[茅聶聲ICP氓陇聡2021003897氓聫路](https://beian.miit.gov.cn/) | Powered By [hexo](https://hexo.io/) and [Stellar](https://github.com/xaoxuu/hexo-theme-stellar)

[howmp/zigdonut

0](https://github.com/howmp/zigdonut)

忙聹聙猫驴聭忙聸麓忙聳掳

[BeaconKiller茅聮聢氓炉鹿http/https莽職聞beacon莽職聞忙拢聙忙碌聥氓路楼氓聟路](/beaconkiller.html)[WinDump-氓聬聨忙赂聴茅聙聫盲驴隆忙聛炉/氓炉聠莽聽聛/氓聡颅猫炉聛忙聰露茅聸聠氓路楼氓聟路](/windump.html)[氓聹篓cron盲赂颅忙路禄氓聤聽茅職聬猫聴聫猫庐隆氓聢聮盲禄禄氓聤隆](/cron-hide.html)[莽聰篓zig氓庐聻莽聨掳莽庐聙忙聵聯donut](/zig-3-donut.html)[IIS盲赂聥web.config氓聢漏莽聰篓](/iis-web-config.html)

忙聽聡莽颅戮盲潞聭

[氓聫聧莽聢卢](/tags/%E5%8F%8D%E7%88%AC/) [盲禄拢莽聽聛氓庐隆猫庐隆](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [socks5](/tags/socks5/) [VSCode](/tags/VSCode/) [v8](/tags/v8/) [忙聨聣莽潞驴](/tags/%E6%8E%89%E7%BA%BF/) [PHP](/tags/PHP/) [氓聤聽茅聙聼盲鹿聬](/tags/%E5%8A%A0%E9%80%9F%E4%B9%90/) [猫聶職忙聥聼忙聹潞](/tags/%E8%99%9A%E6%8B%9F%E6%9C%BA/) [氓聠聟莽陆聭莽漏驴茅聙聫](/tags/%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F/) [cron](/tags/cron/) [ssh](/tags/ssh/) [MFC](/tags/MFC/) [beacon](/tags/beacon/) [python](/tags/python/) [pty](/tags/pty/) [IIS](/tags/IIS/) [pyinstaller](/tags/pyinstaller/) [docker](/tags/docker/) [glibc](/tags/glibc/) [COM](/tags/COM/) [wiz](/tags/wiz/) [盲驴隆忙聛炉忙聰露茅聸聠](/tags/%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86/) [莽拢聛莽聸聵](/tags/%E7%A3%81%E7%9B%98/) [srdi](/tags/srdi/) [dotnet](/tags/dotnet/) [Donut](/tags/Donut/) [zig](/tags/zig/) [猫掳聝猫炉聲](/tags/%E8%B0%83%E8%AF%95/) [sublime](/tags/sublime/) [氓颅聴猫聤聜莽聽聛](/tags/%E5%AD%97%E8%8A%82%E7%A0%81/) [aspose](/tags/aspose/) [fakesh](/tags/fakesh/) [openvpn](/tags/openvpn/) [iis](/tags/iis/) [CobaltStrike](/tags/CobaltStrike/) [donut](/tags/donut/) [盲禄拢莽聬聠](/tags/%E4%BB%A3%E7%90%86/) [seeyon](/tags/seeyon/) [node](/tags/node/) [COFF](/tags/COFF/) [password](/tags/password/) [忙聺聝茅聶聬莽禄麓忙聦聛](/tags/%E6%9D%83%E9%99%90%E7%BB%B4%E6%8C%81/) [processhacker](/tags/processhacker/) [cobaltstrike](/tags/cobaltstrike/) [pyoxidizer](/tags/pyoxidizer/) [氓聼聼忙聨搂](/tags/%E5%9F%9F%E6%8E%A7/) [茅職聬猫聴聫](/tags/%E9%9A%90%E8%97%8F/) [BOF](/tags/BOF/) [猫聡麓猫驴聹](/tags/%E8%87%B4%E8%BF%9C/) [Java](/tags/Java/) [bypassav](/tags/bypassav/) [webshell](/tags/webshell/) [忙聴楼氓驴聴](/tags/%E6%97%A5%E5%BF%97/) [jsc](/tags/jsc/) [VPN](/tags/VPN/) [shellcode](/tags/shellcode/) [report](/tags/report/) [MESSAGE\_MAP](/tags/MESSAGE-MAP/)