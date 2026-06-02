---
title: 关于家用路由器DNS被恶意篡改导致异常跳转风险的提示
url: https://blog.nsfocus.net/%e5%85%b3%e4%ba%8e%e5%ae%b6%e7%94%a8%e8%b7%af%e7%94%b1%e5%99%a8dns%e8%a2%ab%e6%81%b6%e6%84%8f%e7%af%a1%e6%94%b9%e5%af%bc%e8%87%b4%e5%bc%82%e5%b8%b8%e8%b7%b3%e8%bd%ac%e9%a3%8e%e9%99%a9%e7%9a%84/
source: 绿盟科技技术博客
date: 2026-06-01
fetch_date: 2026-06-02T06:31:27.219437
---

# 关于家用路由器DNS被恶意篡改导致异常跳转风险的提示

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 关于家用路由器DNS被恶意篡改导致异常跳转风险的提示

### 关于家用路由器DNS被恶意篡改导致异常跳转风险的提示

[2026-06-01](https://blog.nsfocus.net/%E5%85%B3%E4%BA%8E%E5%AE%B6%E7%94%A8%E8%B7%AF%E7%94%B1%E5%99%A8dns%E8%A2%AB%E6%81%B6%E6%84%8F%E7%AF%A1%E6%94%B9%E5%AF%BC%E8%87%B4%E5%BC%82%E5%B8%B8%E8%B7%B3%E8%BD%AC%E9%A3%8E%E9%99%A9%E7%9A%84/ "关于家用路由器DNS被恶意篡改导致异常跳转风险的提示")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 86

**致谢：**感谢东莞市委网信办和绿盟科技集团股份有限公司在威胁情报、现场取证等方面对本报告提供的支持。

近期，CNCERT发现，部分家庭用户连接家用路由器Wi-Fi后，访问正常网站或触发终端网络连通性检测时，会异常跳转至色情、赌博等非法页面。经研判，该事件主要由家用路由器等家庭网络设备DNS服务器配置被篡改导致。

路由器是家庭网络的重要入口。一旦DNS配置被恶意修改，连接该路由器的手机、电脑等终端可能自动获取异常DNS服务器地址，导致正常网站访问被错误解析，并被诱导跳转至非法页面，带来广告强推、钓鱼欺诈和账号信息泄露等风险。

### 一、被篡改的“上网指路牌”

DNS可以理解为互联网访问中的“指路牌”。正常情况下，用户访问网站时，DNS会将域名解析到正确地址。若家用路由器DNS配置被篡改，终端接入Wi-Fi后，就可能被分配异常DNS服务器地址，访问正常网站时被解析至特定恶意IP地址，随后被相关网站返回的跳转指令诱导打开非法页面。

经现场取证确认，受影响路由器设备的后台管理口令强度不足，攻击者疑似感染家庭内网设备后，利用弱口令进入路由器管理页面并修改DNS服务器配置。

截至目前，CNCERT已累计监测数十个专门提供域名恶意解析服务的DNS服务器和异常跳转服务的Web服务器，单日恶意解析次数超过数亿次，单日影响境内独立IP最高超过70余万个，相关风险对用户正常上网秩序和网络安全造成影响。

### 二、排查方法

家庭用户如发现异常跳转，可重点排查以下情况。

一是排查访问异常。连接家庭Wi-Fi后，如访问正常网站被跳转至色情、赌博、广告推广或疑似钓鱼页面，或同一Wi-Fi下多台设备同时出现类似情况，应重点核查路由器DNS配置是否异常。

二是核查DNS配置。登录路由器管理后台，在“上网设置”“网络参数”“LAN口设置”“DHCP服务器”等栏目中查看DNS服务器地址，确认是否被修改为陌生IP地址，或是否与运营商自动下发DNS、用户自行设置的可信DNS不一致。

三是核对终端信息。用户可在手机、电脑等终端的Wi-Fi详情、网络连接详情或网络适配器详情中查看当前DNS服务器地址，也可在电脑命令行中执行“ipconfig /all”等命令查看DNS服务器地址。如发现终端获取到陌生DNS地址，或多台终端DNS地址均存在异常，应及时检查路由器配置是否被篡改。部分路由器默认开启DNS代理模式，终端显示的DNS服务器可能为路由器内网地址，建议结合路由器后台DNS配置综合判断。

四是关注设备状态。如发现路由器后台密码为弱口令（如123456、生日、手机号等）、Wi-Fi配置无故变更，或设备出现网速变慢、频繁掉线、异常重启等情况，应及时开展安全排查并采取处置措施。

### 三、防范建议

广大网民、路由器厂商和相关网络服务单位应强化风险意识，及时开展排查处置，重点做好以下防范工作。

一是检查DNS配置。家庭用户应及时登录路由器管理后台，检查DNS服务器配置是否被修改为陌生IP地址；如发现异常，应恢复为运营商自动下发DNS或可信公共DNS，并重启路由器和联网终端。

二是修改弱口令。及时修改路由器管理后台默认口令或弱口令，设置高强度独立密码，避免攻击者利用简单密码进入后台修改配置。

三是关闭高风险功能。关闭非必要远程管理、UPnP、端口映射等功能，减少路由器暴露面，降低被入侵和篡改风险。

四是及时升级固件。关注路由器厂商发布的固件更新，及时升级至最新版本，修复已知安全漏洞。

五是留意异常跳转。如联网终端出现访问正常网站被跳转至色情、赌博、广告推广或疑似钓鱼页面等情况，应立即断开网络，检查路由器DNS配置和终端安全状态，必要时恢复路由器出厂设置后重新配置。

六是加强产品防护。建议路由器厂商加强管理后台登录保护、弱口令提示、异常DNS配置告警和固件安全更新，降低家庭用户因弱口令、旧版本固件或默认配置不当导致的安全风险。

### 四、相关IOC

**存活恶意DNS服务器**

27.124.42.32

202.79.174.219

118.107.24.242

27.124.17.11

118.107.32.155

112.213.116.170

134.122.183.142

143.92.48.15

202.79.175.100

27.124.34.143

143.92.56.180

27.124.20.237

137.220.229.5

143.92.63.213

27.124.12.72

137.220.229.16

192.252.176.48

118.107.47.76

27.124.2.196

27.124.2.214

202.95.14.241

202.79.171.149

143.92.57.29

14.128.50.26

143.92.52.183

202.95.11.163

202.79.168.144

143.92.53.251

143.92.63.247

143.92.56.81

143.92.56.8

27.124.45.61

27.124.41.92

202.95.14.218

143.92.53.134

27.124.42.48

202.79.168.160

118.107.40.48

143.92.63.214

27.124.42.39

27.124.17.18

118.107.24.243

202.95.14.252

202.95.14.230

202.95.11.179

27.124.42.51

27.124.42.50

27.124.34.144

27.124.20.238

143.92.63.249

118.107.47.78

![](https://p26-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/95ff968337884c768814861779fa49a0~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20260601161335D45746C9939FCA30C269&x-expires=2147483647&x-signature=93EuqTaEHSpV9%2B0aJIU63%2FFzJgU%3D)

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/%E7%99%BE%E4%BD%99%E5%AE%B6%E5%AE%98%E6%96%B9%E7%BD%91%E7%AB%99%E8%A2%AB%E5%8A%AB%E6%8C%81%E5%BC%95%E6%B5%81%E8%AD%A6%E7%A4%BA%EF%BC%9A%E5%A6%82%E4%BD%95%E7%AD%91%E7%89%A2web/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)