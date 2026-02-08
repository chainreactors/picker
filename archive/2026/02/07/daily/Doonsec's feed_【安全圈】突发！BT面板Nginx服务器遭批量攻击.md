---
title: 【安全圈】突发！BT面板Nginx服务器遭批量攻击
url: https://mp.weixin.qq.com/s/dSE5xEJmpGywpce6a0fyOA
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:31:42.279838
---

# 【安全圈】突发！BT面板Nginx服务器遭批量攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyG7mwr9H32w6ShzYHXmficEzP4zib4a09XFNK9P1KBKXvnUCia3OF91RfoZy7UQTPtNDEFnlibfIIM5vNM2Q7wgzPMTj0y0Jy7Ya6Y/0?wx_fmt=jpeg)

# 【安全圈】突发！BT面板Nginx服务器遭批量攻击

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客攻击

## 一、事件核心概况

据**网络安全公司DATADOG**发布的安全报告显示，黑客正利用**React2Shell 漏洞（CVE-2025-55182，远程代码执行类漏洞）** 发起针对性攻击，**宝塔面板**及**NGINX 服务器**成为主要攻击目标，得手后黑客会篡改服务器配置，将网站流量劫持至非法博彩网站，目前攻击已覆盖多个地区域名。

## 二、攻击目标与影响范围

1. **1、核心受攻击载体：使用宝塔面板管理的 NGINX 服务器，宝塔面板为国内常用免费服务器图形化管理工具，NGINX 为业界广泛使用的开源反向代理服务器；**
2. **2、针对性域名：亚洲顶级域名搭建的网站，包含.in（印度）、.id（印尼）、.bd（孟加拉）、.th（泰国）、.edu、.gov，同时涉及南美洲秘鲁.pe 域名；**
3. **3、影响后果：被攻击网站的流量会**随机跳转到非法博彩网站**，尤其搜索引擎访问时跳转概率更高，网站运营者会丢失正常流量，同时用户访问体验受损，还可能面临合规风险。**

## 三、黑客攻击核心手法

### 1. 配置篡改：隐蔽注入流量转发指令

黑客利用 NGINX 原生**proxy\_pass 指令**（流量转发常用指令）添加转发模块，因该指令为正常功能，不会触发安全警告；同时伪造**Host、X-Real-IP、User-Agent、Referer**等合法请求头，若无人工检查配置文件，极难发现篡改痕迹。

### 2. 多阶段脚本工具包：自动化批量渗透

黑客使用包含**zx.sh、bt.sh、4zdh.sh、zdh.sh、ok.sh**的脚本化工具包，实现自动化 NGINX 配置注入，各脚本分工明确：

* zx.sh：初始控制脚本，负责下载并执行其他脚本，含备用下载机制，curl/wget 不可用时通过 TCP 发送 HTTP 请求；
* bt.sh：针对性攻击宝塔面板，根据 server\_name 值动态注入配置模板并覆盖，重启 NGINX 使配置生效；
* 4zdh.sh：枚举 NGINX 常见配置文件位置（sites-enabled/conf.d/sites.available 等）；
* zdh.sh：精准定位 /etc/nginx/sites-enabled 文件，重点针对.in/.id 域名；
* ok.sh：扫描已注入的配置，收集被劫持域名信息并传送至黑客 C2 服务器（远程控制服务器）。

## 四、核心防护与应急处置方案

### ▌通用版（所有宝塔 / NGINX 服务器运营者必做）

1. **立即修复漏洞：核查服务器是否存在 React2Shell 漏洞（CVE-2025-55182），前往宝塔面板后台、NGINX 官方下载对应修复补丁 / 更新至最新安全版本；**
2. **检查配置文件：重点核查 NGINX 的 sites-enabled、conf.d、sites.available 目录下配置文件，删除陌生的 proxy\_pass 转发指令及异常请求头配置；**
3. **重启验证：修改配置后重启 NGINX 服务，访问网站测试是否存在异常跳转，同时检查访问日志，排查陌生 IP 的异常访问记录。**

### ▌专业版（运维 / 技术人员进阶防护）

1. **限制脚本执行权限：禁止服务器中匿名用户执行 sh、bash 等脚本文件，对 zx.sh、bt.sh 等可疑脚本名称设置拦截规则；**
2. **监控 C2 服务器通信：通过防火墙、入侵检测系统拦截服务器与境外陌生 IP 的通信，重点监控东南亚、南美洲地区异常 IP；**
3. **加固宝塔面板：修改宝塔面板默认登录端口、开启二次验证，删除非运维人员的面板操作权限，关闭不必要的远程访问功能；**
4. **开启日志审计：开启 NGINX 和宝塔面板的全量日志审计，对配置文件修改、脚本执行等操作做实时告警，第一时间发现异常行为。**

### ▌温馨提示

1. 若发现网站已被劫持，除修复配置外，需立即修改宝塔面板、服务器登录密码，更换 SSH 密钥，避免黑客二次入侵；
2. 非技术型运营者可联系服务器服务商，请求协助做漏洞检测和配置核查，切勿自行修改配置避免引发新问题；
3. 此次攻击暂未发现针对普通个人用户设备的风险，个人上网遇到网站跳转博彩页面，直接关闭即可，无需过度担心。

关注我，第一时间获取服务器安全防护最新技巧，转发给身边的网站运营 / 运维同行，一起筑牢服务器安全防线！

***END***

阅读推荐

[【安全圈】阿里30亿红包分发首日，千问App“崩了”](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074041&idx=1&sn=ead70ffd5a7c58f34ac096e34ec29ba1&scene=21#wechat_redirect)

[【安全圈】微软Azure突发10小时全球宕机！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074041&idx=2&sn=e9b040f68282d54490efb0d48044e63e&scene=21#wechat_redirect)

[【安全圈】罗马大学遭网络攻击：欧洲最大规模大学之一，计算机系统瘫痪数日](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074041&idx=3&sn=a8f0fda81433b96cf1cb3c6bd236587c&scene=21#wechat_redirect)

[【安全圈】豆瓣又双叒叕崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074026&idx=1&sn=6a635141041422657df1a74a69f50b77&scene=21#wechat_redirect)

[【安全圈】迅雷下载暗藏猫腻：用户ISO镜像遭替换，捆绑大量推广软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074026&idx=2&sn=5f13d39252450f325b253834a3a767c2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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