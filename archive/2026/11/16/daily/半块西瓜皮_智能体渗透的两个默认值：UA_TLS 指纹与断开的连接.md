---
title: 智能体渗透的两个默认值：UA/TLS 指纹与断开的连接
url: https://guage.cool/gocurl-two-defaults.html
source: 半块西瓜皮
date: 2026-11-16
fetch_date: 2026-11-17T09:56:35.550382
---

# 智能体渗透的两个默认值：UA/TLS 指纹与断开的连接

[![](/img/avatar.jpg)](/about/)[氓聧聤氓聺聴猫楼驴莽聯聹莽職庐](/)

忙虏隆忙聹聣忙聣戮氓聢掳氓聠聟氓庐鹿茂录聛

忙聹卢忙聳聡莽聸庐氓陆聲

1. [忙聦聡莽潞鹿](#%E6%8C%87%E7%BA%B9)
2. [猫驴聻忙聨楼](#%E8%BF%9E%E6%8E%A5)
3. [gocurl 莽職聞氓聛職忙鲁聲](#gocurl-%E7%9A%84%E5%81%9A%E6%B3%95)
4. [猫戮鹿莽聲聦](#%E8%BE%B9%E7%95%8C)

氓聸聻氓聢掳茅隆露茅聝篓氓聫聜盲赂聨猫庐篓猫庐潞

[![](data:image/png;base64...)](https://github.com/howmp)[![](data:image/png;base64...)](https://weibo.com/howmp)[![](data:image/png;base64...)](https://guage.cool/atom.xml)![](data:image/png;base64...)

[盲赂禄茅隆碌](/)
[忙聳聡莽芦聽](/)[莽陆聭莽禄聹氓庐聣氓聟篓](/categories/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/)  [氓路楼氓聟路氓录聙氓聫聭](/categories/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%B7%A5%E5%85%B7%E5%BC%80%E5%8F%91/)

氓聫聭氓赂聝盲潞聨茂录職2026-11-16忙聸麓忙聳掳盲潞聨茂录職2026-11-16

# 忙聶潞猫聝陆盲陆聯忙赂聴茅聙聫莽職聞盲赂陇盲赂陋茅禄聵猫庐陇氓聙录茂录職UA/TLS 忙聦聡莽潞鹿盲赂聨忙聳颅氓录聙莽職聞猫驴聻忙聨楼

[盲赂聤盲赂聙莽炉聡忙聳聡莽芦聽](/artex-traffic-detect.html)莽職聞忙聲掳忙聧庐茂录職4,190 盲赂陋盲禄禄氓聤隆茫聙聛138,751 忙卢隆氓路楼氓聟路猫掳聝莽聰篓茂录聦Bash 氓聧聽 46.4%茂录聸Bash 茅聡聦 curl 23,422 忙卢隆茫聙聛python 24,404 忙卢隆茫聙聜忙聶潞猫聝陆盲陆聯氓聫聭氓聦聟氓聼潞忙聹卢氓掳卤忙聵炉猫驴聶盲赂陇忙聺隆猫路炉茫聙聜

盲赂陇猫聙聟茅聝陆忙聵炉忙聦聣茫聙聦盲潞潞忙聣搂猫隆聦盲赂聙忙卢隆氓聭陆盲禄陇茫聙聧猫庐戮猫庐隆莽職聞茫聙聜忙聶潞猫聝陆盲陆聯猫驴聻莽禄颅猫路聭氓陇職忙颅楼盲禄禄氓聤隆忙聴露茂录聦盲录職莽垄掳氓聢掳盲赂陇盲赂陋茅聴庐茅垄聵茂录職猫炉路忙卤聜忙聦聡莽潞鹿忙聵炉氓路楼氓聟路猫聡陋氓路卤莽職聞茂录聸猫驴聸莽篓聥茅聙聙氓聡潞氓聬聨猫驴聻忙聨楼氓聮聦盲录職猫炉聺盲鹿聼忙虏隆盲潞聠茫聙聜gocurl 忙聰鹿莽職聞氓掳卤忙聵炉猫驴聶盲赂陇氓陇聞茫聙聜

## 忙聦聡莽潞鹿

curl 茅禄聵猫庐陇 UA 忙聵炉 `curl/8.x`茂录聦requests 忙聵炉 `python-requests/2.x`茫聙聜氓聫陋忙聰鹿 UA 盲赂聧氓陇聼茂录聦氓陇麓盲鹿聼盲赂聧盲赂聙忙聽路茂录職

| 氓颅聴忙庐碌 | curl | Chrome 152 |
| --- | --- | --- |
| `Accept` | `*/*` | `text/html,application/xhtml+xml,...` |
| `sec-ch-ua` | 忙聴聽 | `"Chromium";v="152", ...` |
| `sec-fetch-*` | 忙聴聽 | `none` / `navigate` / `?1` / `document` |
| `Accept-Encoding` | 盲禄聟 `--compressed` | `gzip, deflate, br, zstd` |
| `Accept-Language` | 茅禄聵猫庐陇盲赂聧氓聫聭 | `en-US,en;q=0.9` |
| H2 盲录陋氓陇麓茅隆潞氓潞聫 | 氓庐聻莽聨掳莽聸赂氓聟鲁 | `:method :authority :scheme :path` |

TLS 忙聸麓莽聸麓忙聨楼茫聙聜Linux 盲赂聤莽職聞 curl 氓聮聦 python requests 氓陇搂氓陇職猫碌掳 OpenSSL茂录聦Chrome 莽聰篓 BoringSSL茂录聦ClientHello 茅聡聦莽職聞 cipher茫聙聛忙聣漏氓卤聲茫聙聛忙聸虏莽潞驴茫聙聛ALPN 茅聝陆盲赂聧氓聬聦茫聙聜JA3/JA4 盲禄聨 ClientHello 莽庐聴氓聡潞忙聺楼茂录聦忙聫隆忙聣聥茅聵露忙庐碌氓掳卤猫聝陆氓聫聳茂录聦盲赂聧茅聹聙猫娄聛猫搂拢氓炉聠茫聙聜HTTPS 猫聝陆忙聦隆盲陆聫 UA茂录聦忙聦隆盲赂聧盲陆聫猫驴聶盲赂陋茫聙聜

gocurl 莽聰篓 tls-client + uTLS + fhttp茂录聦profile 氓聸潞氓庐職 `Chrome_152`茫聙聜README 猫庐掳莽職聞 JA4 忙聵炉 `t13d1517h2_8daaf6152771_cb7bf5808d99`茂录聦HTTP/2 Akamai 忙聵炉 `1:65536;2:0;4:6291456;6:262144|15663105|0|m,a,s,p`茫聙聜茅禄聵猫庐陇氓陇麓茅隆潞氓潞聫忙聦聣 Chrome 152 忙聨聮茂录聦`-H` 氓聫炉盲禄楼猫娄聠莽聸聳茂录聦`--header-order` 氓聫炉盲禄楼茅聡聧忙聨聮茫聙聜`--resolve`/`--connect-to` 氓聫陋忙聰鹿猫驴聻忙聨楼氓聹掳氓聺聙茂录聦Host茫聙聛SNI茫聙聛猫炉聛盲鹿娄忙聽隆茅陋聦氓聬聧盲赂聧氓聫聵茫聙聜

忙聦聡莽潞鹿氓聸潞氓庐職忙聵炉氓聢禄忙聞聫莽職聞茫聙聜`--tlsv1.x`茫聙聛`--ciphers`茫聙聛`--pinnedpubkey` 猫驴聶盲潞聸茅聝陆盲赂聧忙聰炉忙聦聛茂录聦猫娄聛忙聨垄忙碌聥 TLS 氓聫聜忙聲掳猫驴聵忙聵炉氓戮聴莽聰篓 curl茫聙聜

## 猫驴聻忙聨楼

curl 忙炉聫忙聣搂猫隆聦盲赂聙忙卢隆忙聵炉盲赂聙盲赂陋忙聳掳猫驴聸莽篓聥茫聙聜猫驴聸莽篓聥茅聙聙氓聡潞茂录聦socket 猫垄芦莽鲁禄莽禄聼氓聟鲁忙聨聣茂录聦猫驴聻忙聨楼忙卤聽茫聙聛HTTP/2 忙碌聛茫聙聛TLS 盲录職猫炉聺莽录聯氓颅聵盲赂聙猫碌路忙露聢氓陇卤茂录聦盲赂聥盲赂聙忙聺隆氓聭陆盲禄陇茅聡聧忙聳掳 DNS茫聙聛TCP茫聙聛TLS茫聙聜氓聧聲忙聺隆氓聭陆盲禄陇猫炉路忙卤聜氓陇職盲赂陋 URL 忙聢聳 `--next` 猫聝陆氓聹篓猫驴聸莽篓聥氓聠聟氓陇聧莽聰篓茂录聦盲陆聠 agent 茅聙職氓赂赂盲赂聙忙卢隆 Bash 猫掳聝莽聰篓氓聫陋氓聫聭盲赂聙忙聺隆氓聭陆盲禄陇茫聙聜

Cookie 氓聫炉盲禄楼茅聺聽 `-c`/`-b` 忙聳聡盲禄露忙聨楼氓聤聸茂录聦盲陆聠忙聳聡盲禄露忙虏隆忙聹聣茅聰聛茂录聦氓鹿露氓聫聭盲禄禄氓聤隆盲录職盲潞聮莽聸赂猫娄聠莽聸聳茂录聸氓庐聝氓聫陋氓颅聵 Cookie茂录聦盲赂聧氓颅聵猫驴聻忙聨楼氓聮聦 HTTP/2 莽聤露忙聙聛茫聙聜python 莽職聞 `requests.Session()` 猫聝陆莽聲聶盲陆聫猫驴聻忙聨楼氓聮聦 Cookie茂录聦盲陆聠氓聫陋氓聹篓盲赂聙盲赂陋猫驴聸莽篓聥茅聡聦忙聹聣忙聲聢茂录聦agent 忙炉聫忙卢隆猫碌路忙聳掳 python茂录聦Session 盲鹿聼猫路聼莽聺聙茅聰聙忙炉聛茫聙聜

莽禄聯忙聻聹忙聵炉忙炉聫盲赂陋猫炉路忙卤聜氓庐聦忙聲麓忙聫隆忙聣聥茫聙聜忙碌聛茅聡聫盲戮搂盲鹿聼猫聝陆莽聹聥氓聢掳茂录職忙碌聫猫搂聢氓聶篓氓陇聧莽聰篓氓掳聭茅聡聫猫驴聻忙聨楼茂录聦HTTP/2 猫驴聵盲录職氓陇職猫路炉氓陇聧莽聰篓茂录聸忙炉聫忙聺隆氓聭陆盲禄陇盲赂聙莽禄聞忙聳掳猫驴聻忙聨楼盲赂聧莽庐聴氓录潞莽聣鹿氓戮聛茂录聦盲陆聠氓聫炉盲禄楼氓聫聜盲赂聨猫聛職莽卤禄茫聙聜莽聤露忙聙聛茅聴庐茅垄聵忙聸麓氓庐聻茅聶聟茂录聦莽聶禄氓陆聲茫聙聛猫路鲁猫陆卢茫聙聛CSRF token 忙聹卢忙聺楼氓聹篓盲赂聙盲赂陋盲录職猫炉聺茅聡聦茂录聦莽聨掳氓聹篓氓聫陋猫聝陆茅聺聽忙聳聡盲禄露盲录聽茫聙聜

## gocurl 莽職聞氓聛職忙鲁聲

忙聦聡莽潞鹿茅聝篓氓聢聠盲赂聤茅聺垄猫炉麓盲潞聠茂录聦猫驴聶茅聡聦氓聫陋莽聹聥猫驴聻忙聨楼茫聙聜

gocurl 茅禄聵猫庐陇猫碌路氓聬聨氓聫掳 daemon茫聙聜莽卢卢盲赂聙忙卢隆猫掳聝莽聰篓猫聡陋氓聤篓忙聥聣猫碌路茂录聦CLI 茅聙職猫驴聡 Unix socket 茅聙職盲驴隆茫聙聜daemon 忙聦聛忙聹聣 HTTP/1.1 氓聮聦 HTTP/2 猫驴聻忙聨楼忙卤聽茂录聦忙聣聙忙聹聣猫炉路忙卤聜氓聟卤盲潞芦 Cookie jar茂录聦莽漏潞茅聴虏 15 氓聢聠茅聮聼茅聙聙氓聡潞茫聙聜`--session` 莽聰篓莽聥卢莽芦聥 socket 茅職聰莽娄禄盲禄禄氓聤隆茂录聦`--no-persist` 莽娄聛莽聰篓 daemon茂录聦氓聬炉氓聤篓氓陇卤猫麓楼氓聸聻茅聙聙莽聸麓猫驴聻茫聙聜daemon 氓聫陋忙聹聧氓聤隆 HTTP/HTTPS茂录聦FTP/WS 猫碌掳莽聸麓猫驴聻茫聙聜

CLI 猫驴聸莽篓聥莽聟搂氓赂赂茅聙聙氓聡潞茂录聦猫驴聻忙聨楼莽聲聶氓聹篓 daemon 茅聡聦茫聙聜盲赂聥盲赂聙忙聺隆氓聭陆盲禄陇氓聫陋猫娄聛 transport 茅聟聧莽陆庐盲赂聙猫聡麓氓掳卤猫聝陆忙聨楼莽聺聙莽聰篓茫聙聜daemon 氓聧聫猫庐庐 v5 氓炉鹿忙虏隆忙聹聣 `Content-Length` 莽職聞氓聯聧氓潞聰莽聰篓氓聢聠氓聺聴莽禄聯忙聺聼氓赂搂茂录聦氓聦潞氓聢聠忙颅拢氓赂赂莽禄聯忙聺聼氓聮聦盲赂聤忙赂赂忙聢陋忙聳颅茫聙聜

Cookie 莽職聞猫戮鹿莽聲聦茂录職daemon 莽職聞 jar 氓聟卤盲潞芦茂录聸`-b` 氓颅聴莽卢娄盲赂虏氓聫陋氓炉鹿氓陆聯氓聣聧猫炉路忙卤聜莽聰聼忙聲聢茂录聦盲赂聧氓聠聶氓聟楼氓聟卤盲潞芦 jar茂录聸`-c` 氓聫陋氓炉录氓聡潞氓陆聯氓聣聧莽聸庐忙聽聡 host 莽職聞 cookie茂录聦盲赂聧猫聬陆莽聸聵盲录職茅職聫 daemon 茅聙聙氓聡潞盲赂垄氓陇卤茂录聸`--session` 氓聫陋茅職聰莽娄禄 socket茫聙聛猫驴聻忙聨楼忙卤聽氓聮聦 jar茂录聦盲赂聧忙聵炉忙聺聝茅聶聬猫戮鹿莽聲聦茫聙聜socket 莽聸庐氓陆聲 0700茫聙聛socket 0600茂录聦氓聫陋忙聨楼氓聫聴氓聬聦 UID 猫驴聻忙聨楼茫聙聜

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` ./gocurl -sS -c cookies.txt -d 'username=admin&password=...' https://target/login ./gocurl -sS https://target/dashboard ./gocurl -sS --session task-b https://other-target/ ./gocurl --stop-daemon --session task-b ``` |

氓聬聦 host茫聙聛茅聟聧莽陆庐盲赂聙猫聡麓忙聴露茂录聦莽卢卢盲潞聦忙聺隆氓聭陆盲禄陇盲赂聧氓聠聧忙聫隆忙聣聥茂录聦Cookie 盲禄聨 daemon 莽職聞 jar 茅聡聦氓聫聳茫聙聜盲赂颅茅聴麓 daemon 莽漏潞茅聴虏茅聙聙氓聡潞莽職聞猫炉聺茂录聦盲录職茅聡聧忙聳掳氓禄潞猫驴聻茫聙聜

`--json-envelope` 猫戮聯氓聡潞猫炉路忙卤聜茫聙聛氓聯聧氓潞聰茫聙聛TLS 猫炉聛盲鹿娄茫聙聛猫聙聴忙聴露茫聙聛茅聡聧猫炉聲氓聮聦茅聙聙氓聡潞莽聽聛茂录聦氓聯聧氓潞聰盲陆聯猫露聟猫驴聡 1 MiB 忙聢陋忙聳颅茫聙聜氓炉鹿 agent 忙聺楼猫炉麓忙炉聰猫搂拢忙聻聬 `-w` 莽篓鲁氓庐職茫聙聜

盲禄拢莽聽聛 11 盲赂陋氓聦聟茫聙聛莽潞娄 1 盲赂聡猫隆聦茂录聦218 盲赂陋忙碌聥猫炉聲茫聙聜daemon 氓聧聲莽聥卢忙聢聬氓聦聟茂录聦`transport` 氓聮聦 `config` 盲赂聧氓聫聧氓聬聭盲戮聺猫碌聳 `app`茂录聦忙聳鹿盲戮驴氓聧聲莽聥卢忙碌聥猫炉聲茫聙聜

## 猫戮鹿莽聲聦

* 忙聣聙忙聹聣 gocurl 忙碌聛茅聡聫茅聝陆忙聵炉氓聬聦盲赂聙盲赂陋 Chrome 152 忙聦聡莽潞鹿茂录聦忙聧垄 IP 盲鹿聼盲赂聙忙聽路茂录聦氓聫炉盲禄楼猫垄芦猫聛職莽卤禄茫聙聜
* 猫驴聡 TLS 盲赂颅茅聴麓盲潞潞盲禄拢莽聬聠氓聬聨茂录聦莽聸庐忙聽聡莽聹聥氓聢掳莽職聞忙聵炉盲禄拢莽聬聠莽職聞忙聦聡莽潞鹿茫聙聜
* daemon 氓聫陋氓聹篓氓聬聦忙聹潞茫聙聛氓聬聦 UID 盲赂聥氓路楼盲陆聹茂录聦盲赂聧忙聵炉氓聢聠氓赂聝氓录聫盲录職猫炉聺茫聙聜
* Cookie 莽聰聼氓聭陆氓聭篓忙聹聼猫路聼 daemon 莽禄聭氓庐職茂录聦盲赂聧氓聠聶 `-c` 氓掳卤盲录職盲赂垄茫聙聜
* HTTP/3茫聙聛TLS 莽聣聢忙聹卢/cipher/pin 忙聨垄忙碌聥茫聙聛莽聹聼忙颅拢莽職聞 Kerberos茫聙聛莽聲赂氓陆垄 HTTP 氓聮聦猫炉路忙卤聜猫碌掳莽搂聛茫聙聛氓陇聧忙聺聜 FTP茂录聦盲禄聧莽聞露猫娄聛莽聰篓 curl茫聙聜
* `--json-envelope` 氓聫陋忙聰炉忙聦聛 HTTP/HTTPS茂录聸FTP 盲赂禄氓聤篓忙篓隆氓录聫盲赂聧忙聰炉忙聦聛盲禄拢莽聬聠/FTPS/`--interface`茫聙聜

茅聹聙猫娄聛忙碌聫猫搂聢氓聶篓忙聦聡莽潞鹿氓聮聦猫驴聻莽禄颅盲录職猫炉聺忙聴露莽聰篓氓庐聝茂录聸茅聹聙猫娄聛氓聧聫猫庐庐忙聨垄忙碌聥茫聙聛莽聲赂氓陆垄忙聤楼忙聳聡忙聢聳氓庐聦忙聲麓 curl 猫炉颅盲鹿聣忙聴露茂录聦莽禄搂莽禄颅莽聰篓 curl茫聙聜

茅隆鹿莽聸庐氓聹掳氓聺聙茂录職<https://github.com/howmp/gocurl>

> 盲禄聟莽聰篓盲潞聨氓路虏猫聨路氓戮聴忙聨聢忙聺聝莽職聞氓庐聣氓聟篓忙碌聥猫炉聲茫聙聛猫碌聞盲潞搂猫聡陋忙聼楼氓聮聦猫掳聝猫炉聲茫聙聜

猫庐赂氓聫炉氓聧聫猫庐庐

忙聹卢忙聳聡茅聡聡莽聰篓 [莽陆虏氓聬聧-茅聺聻氓聲聠盲赂職忙聙搂盲陆驴莽聰篓-莽聸赂氓聬聦忙聳鹿氓录聫氓聟卤盲潞芦 4.0 氓聸陆茅聶聟](https://creativecommons.org/licenses/by-nc-sa/4.0/) 猫庐赂氓聫炉氓聧聫猫庐庐茂录聦猫陆卢猫陆陆猫炉路忙鲁篓忙聵聨氓聡潞氓陇聞茫聙聜

猫戮聝忙聴漏忙聳聡莽芦聽

[ARTEX 莽職聞莽聽麓莽禄陆猫聴聫盲赂聧盲陆聫茂录職go-mitmproxy 忙聤聤氓庐聝氓聧聳盲潞聠](/artex-traffic-detect.html)

氓驴芦忙聺楼氓聫聜盲赂聨猫庐篓猫庐潞氓聬搂~

---

[茅聶聲ICP氓陇聡2021003897氓聫路](https://beian.miit.gov.cn/) | Powered By [hexo](https://hexo.io/) and [Stellar](https://github.com/xaoxuu/hexo-theme-stellar)

[howmp/gocurl

0](https://github.com/howmp/gocurl)

忙聹聙猫驴聭忙聸麓忙聳掳

[忙聶潞猫聝陆盲陆聯忙赂聴茅聙聫莽職聞盲赂陇盲赂陋茅禄聵猫庐陇氓聙录茂录職UA/TLS 忙聦聡莽潞鹿盲赂聨忙聳颅氓录聙莽職聞猫驴聻忙聨楼](/gocurl-two-defaults.html)[ARTEX 莽職聞莽聽麓莽禄陆猫聴聫盲赂聧盲陆聫茂录職go-mitmproxy 忙聤聤氓庐聝氓聧聳盲潞聠](/artex-traffic-detect.html)[Sublime Text氓聨禄氓录鹿莽陋聴氓聮聦忙聽聡茅垄聵猫隆楼盲赂聛](/sublime-patch.html)[dsh-pentest茂录職猫庐漏盲潞潞氓路楼忙聶潞猫聝陆猫聡陋盲赂禄忙聨篓猫驴聸忙赂聴茅聙聫忙碌聥猫炉聲](/dsh-pentest-plugin.html)[Linux ELF Shellcode 莽聰聼忙聢聬盲赂聨 Fileless 氓庐聻忙聢聵](/linux-shellcode.html)

忙聽聡莽颅戮盲潞聭

[wiz](/tags/wiz/) [v8](/tags/v8/) [password](/tags/password/) [TLS](/tags/TLS/) [Donut](/tags/Donut/) [CobaltStrike](/tags/CobaltStrike/) [zig](/tags/zig/) [IIS](/tags/IIS/) [ai](/tags/ai/) [sublime](/tags/sublime/) [node](/tags/node/) [aspose](/tags/aspose/) [webshell](/tags/webshell/) [盲禄拢莽聬聠](/tags/%E4%BB%A3%E7%90%86/) [茅職聬猫聴聫](/tags/%E9%9A%90%E8%97%8F/) [MESSAGE\_MAP](/tags/MESSAGE-MAP/) [dotnet](/tags/dotnet/) [盲禄拢莽聽聛氓庐隆猫庐隆](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [linux](/tags/linux/) [openvpn](/tags/openvpn/) [Java](/tags/Java/) [氓聼聼忙聨搂](/tags/%E5%9F%9F%E6%8E%A7/) [cron](/tags/cron/) [pyoxidizer](/tags/pyoxidizer/) [socks5](/tags/socks5/) [猫聡麓猫驴聹](/tags/%E8%87%B4%E8%BF%9C/) [忙聨聣莽潞驴](/tags/%E6%8E%89%E7%BA%BF/) [TLS忙聦聡莽潞鹿](/tags/TLS%E6%8C%87%E7%BA%B9/) [氓聠聟莽陆聭莽漏驴茅聙聫](/tags/%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F/) [忙赂聴茅聙聫忙碌聥猫炉聲](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [猫掳聝猫炉聲](/tags/%E8%B0%83%E8%AF%95/) [agent](/tags/agent/) [jsc](/tags/jsc/) [cobaltstrike](/tags/cobaltstrike/) [莽拢聛莽聸聵](/tags/%E7%A3%81%E7%9B%98/) [COFF](/tags/COFF/) [pyinstaller](/tags/pyinstaller/) [氓聤聽茅聙聼盲鹿聬](/tags/%E5%8A%A0%E9%80%9F%E4%B9%90/) [repo...