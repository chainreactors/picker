---
title: 能信安：漏洞通告
url: https://mp.weixin.qq.com/s/u3fQutex_-GhLy7GGwk9Fg
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:43:53.297125
---

# 能信安：漏洞通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7kDwzldia4nFFGwHvWNrcVEicXI2dk6HRSuEkWI6RgJsnnUpxugkMiadKchdiakg6eN7UFXKpj1Mqka2ibGhnkADu09kjZ9bmlyich8LZBibias1eq0/0?wx_fmt=jpeg)

# 能信安：漏洞通告

能信安资讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7kDwzldia4nFDJNmk1uBLh9b1Xpic46QBLG4RzaiamTWrTuKuuPrTIHibzu8Xr0G6wfzIQlMwKZxm1TESichaOBtm1lGbWbESuIaeam7Hz7tcG5Q/640?wx_fmt=png&from=appmsg#imgIndex=0)

网络安全预警通报

漏洞通告 2026年7月17日

##

**0****1**

**QiAnXin QAX Virus Removal访问控制错误漏洞**

![](https://mmbiz.qpic.cn/mmbiz_png/7kDwzldia4nGu2pJ9ianxuc2VgbrAZyhf8QJIJEcl3pDeAgj7KChPCGiaumlAcBibn8QO49sm4XXhZl3Bez5oK12sCdVQIXkI6NAvBJm2fYBq9E/640?wx_fmt=png&from=appmsg)

##

漏洞概况：

QiAnXin QAX Virus Removal是中国奇安信（QiAnXin）公司的一款恶意软件与病毒清除工具。
QiAnXin QAX Virus Removal 2025-10-22及之前版本存在访问控制错误漏洞，攻击者可利用该漏洞自定义IO请求，向驱动传递任意进程句柄，调用内核层ZwTerminateProcess。

****受********影响系统********：****
QiAnXin QAX Virus Removal<= 2025-10-22

****链接：****

https://www.nsfocus.net/vulndb/144757

**建议：**

厂商尚未提供漏洞修复方案，请关注厂商主页更新：
https://github.com/cwjchoi01/FocusKiller/tree/main/FocusKiller

**0****2**

**H3C ACG1000-AK230命令注入漏洞**

![](https://mmbiz.qpic.cn/mmbiz_png/7kDwzldia4nFrpK5TIb1YAIB7FOlDpN4iaC0nxMp1VwGzJlwrtXkXvbbwaofv4ODqMT1BSRGB7iaXeFL5NcH2IsMQSuyG32Uf0uSBic7ep4p9PY/640?wx_fmt=png&from=appmsg)

漏洞概况：

H3C ACG1000-AK230是中国新华三（H3C）公司的一款用于上网行为管理的安全网关设备。
H3C ACG1000-AK230 20260227及之前版本存在命令注入漏洞，该漏洞源于设备Web后台接收suffix参数后，未过滤shell命令分隔字符，直接拼接到系统底层命令执行，攻击者可利用该漏洞远程获取设备最高权限，执行任意系统命令。

****受********影响系统********：****
H3C ACG1000-AK230<= 20260227

****链接：****

https://www.nsfocus.net/vulndb/144695

**建议：**

厂商尚未提供漏洞修复方案，请关注厂商主页更新：

https://github.com/leeyper/CVE/issues/1

**0****3**

**Google Chrome信息泄漏漏洞**

![](https://mmbiz.qpic.cn/mmbiz_png/7kDwzldia4nEcP1rqLL1q3dbiayvZzGTcYN72RCicGiatnk7bd5UDSyF6BiauxZZZmsXAB5pwQDpYsPhnlDyib3Cn4ZZjC9MZib8nt5kxLtvALJ4Wk/640?wx_fmt=png&from=appmsg)

漏洞概况：

Google Chrome是美国谷歌（Google）公司的一款Web浏览器。
Google Chrome 146.0.7680.71之前版本存在信息泄漏漏洞，攻击者可利用该漏洞测量跨域资源加载的时间差、资源加载时长、响应体积特征等侧信道特征，推断跨域页面内部数据、接口是否存在、接口返回内容大小、用户登录状态等隐私信息，间接读取跨域敏感数据。

****受********影响系统********：****
Google Chrome<146.0.7680.71

****链接：****

https://www.nsfocus.net/vulndb/144729

**建议：**

目前厂商已经发布了升级补丁以修复这个安全问题，请到厂商的主页下载：
https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop\_10.html

**0****4**

**GitHub Enterprise Server命令注入漏洞**

![](https://mmbiz.qpic.cn/mmbiz_png/7kDwzldia4nENZPEO3jTia5yMVEpCjUsCZ4WUmcH2FWR9F0ibEibdXJ6ia3ERB7L5utibYsHa8TKXiay4hzUlZJf6gV9Xehg27WqnSWkY8QTeSeSEU/640?wx_fmt=png&from=appmsg)

漏洞概况：

GitHub Enterprise Server是美国GitHub开源的一个应用软件，提供一个将自己的GitHub实例设置为虚拟设备，从而提供可扩展，易于管理的平台。
GitHub Enterprise Server存在命令注入漏洞，该漏洞源于在执行git push推送操作时，用户传入的推送选项参数未经过充分清洗，就被拼入内部服务请求头，攻击者可利用该漏洞在服务器实例上实现远程代码执行。

****受********影响系统********：****
Github Enterprise Server

****链接：****

https://www.nsfocus.net/vulndb/144796

**建议：**

目前厂商已经发布了升级补丁以修复这个安全问题，请到厂商的主页下载：
https://docs.github.com/en/enterprise-server@3.16/admin/release-notes#3.16.16

##

▼

**能信安——新一代网络安全领先企业！**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/f7EgONBwTicyukySMu6FXUXWDAkWwribspgqezQeNT68WySw9CozfOicqxGnISiaB0GFYXp3qXHmpmHzays0SBTSibQ/640?wx_fmt=jpeg#imgIndex=4 "bde0f1f294be1789aa279651ce5123d5.jpg")

**公司简介**

深圳市能信安科技股份有限公司，是以安全、移动、泛在和大数据为主要方向的专业技术公司，致力于移动互联安全、车联网安全、物联网安全、大数据安全和人工智能安全技术。

公司是公安部、工信部网络安全技术支撑单位，国家网络安全威胁和漏洞信息共享平台技术支撑单位，是深圳大运会、党的十八大、2020年全国两会、2021年联合国生物多样性大会网络安全技术支撑单位。公司是国家级专精特新“小巨人”企业，中国移动安全十强企业，全国网络安全百强企业，具有良好的品牌影响力。

公司为中国新一代网络安全领先企业。在移动安全领域，公司可提供业界最先进、完整的技术、产品与解决方案，引领移动互联安全的技术潮流。主要产品及服务包括移动应用安全防火墙、无线安全检测及防御系统、移动应用安全检测及加固技术等。在数据安全领域，提供业界领先的数据安全治理、数据安全合格产品与服务。

公司依托于多年网络安全领域的技术经验及专业资质，向各类政府机关及企事业单位提供等级（分级）保护顾问咨询、关基保护顾问咨询、数据安全治理、密码改造顾问咨询、信息系统风险评估、安全体系建设咨询、修复加固服务、渗透测试服务、应急响应服务、安全运维保障服务。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f7EgONBwTicwJbtXPMDMSMHxOK5ibqcf4XC5icFVAVsNF8fiaHuTFeRINsEs3tESvq6aNNTywQlVga3LibzRqNXoPiaA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过