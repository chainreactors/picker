---
title: VMware ESXi 服务器大规模勒索攻击事件风险提示及防护建议
url: https://mp.weixin.qq.com/s?__biz=MzIwMDk1MjMyMg==&mid=2247490933&idx=1&sn=b04f3cb569a79277f83b3d0f7a17b27d&chksm=96f40218a1838b0eca131b77ca90e97e4bd734cd126c7ea10c0ba3368b21d3aa259309667384&scene=58&subscene=0#rd
source: 长亭安全课堂
date: 2023-02-10
fetch_date: 2025-10-04T06:14:38.148680
---

# VMware ESXi 服务器大规模勒索攻击事件风险提示及防护建议

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FOh11C4BDicSs1QnnGH1NSERILpIDBshgnd1DYxVhic5IheDrHnJraibiaLytV5mbEZfjSB7mW08wiarFa9cOqkAmrA/0?wx_fmt=jpeg)

# VMware ESXi 服务器大规模勒索攻击事件风险提示及防护建议

长亭安全应急响应中心

别忘了

![](https://mmbiz.qpic.cn/mmbiz_gif/FOh11C4BDicTG0U5GRmLCoEplic4IXawo0cLR9p65ObLfiakhc1PBia4EJ53J9vRiazoJ0fE2OhrlhK2icr8ttAuIaJw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "22222.gif")

星标我！

**事件梗概**

据法国应急响应中心（CERT-FR）报道，近期有 ESXiArgs 勒索软件传播事件发生，该勒索软件的传播利用了**2021年披露的一个已知 ESXi漏洞 CVE-2021-21974**。

VMware 曾于2021年2月23日发布补丁修复了该漏洞。因为各种客观原因，目前仍有大量 ESXi 环境未更新到最新版本，导致近期出现该勒索软件的利用和流行。

CVE-2021-21974 影响以下系统：

    - ESXi70U1c-17325551 之前的 ESXi 版本 7.x

    - ESXi670-202102401-SG 之前的 ESXi 版本 6.7.x

    - ESXi650-202102101-SG 之前的 ESXi 版本 6.5.x

**漏洞利用原理**

本次漏洞CVE-2021-21974是 VMware ESXi 平台的 SLP (Service Location Protocol) 服务中存在的一个堆溢出漏洞。

SLP是一个在 ESXi 服务器上默认安装的网络服务，该服务将开放427端口。攻击者可以通过向427端口发送构造的恶意请求包触发SLP服务中的堆溢出漏洞造成远程代码执行，完成以上两种方式对虚拟化平台的攻击行为。

**利用细节**

该漏洞出现在 SLPParseSrvURL 函数中，此函数的主要功能是解析数据包中的 URL 参数。其在拷贝 URL 时默认认为传入的 URL 存在\0截断符字符，攻击者可以构造没有\0截断的字符串。这将导致该函数将数据包中的 URL 字段以及后续的长度字段和 scope-list 参数字段视为同一个字符串。导致该函数索引 URL 字符":/"时，其偏移将超过申请的内存大小，然后将超长的字符串拷贝到堆中。当后续 scope-list 参数的长度超过256字节时将导致堆溢出。

**预防及处置建议**

若您还不确定是否遭受相关威胁或已经遭受相关威胁，可参照以下步骤进行排查：

1. 使用长亭牧云（CloudWalker）、洞鉴（X-Ray）或其他主机安全产品、扫描产品扫描未打补丁的系统以确定是否存在相关威胁

2. 建议尽快安装补丁，将 ESXi更新至最新版本或者升级至 ESXi 7.0 U2c 或 ESXi 8.0 GA，以上版本在默认情况下禁用了 SLP 服务

3. 若无法及时升级，在 ESXi 中关闭 SLP 服务

4. 长亭全悉（T-ANSWER）已支持 VMware EXSI 堆溢出漏洞（CVE-2021-21974） 的检测，请关注相关告警信息及时对威胁进行发现和处置

![](https://mmbiz.qpic.cn/mmbiz_png/FOh11C4BDicSs1QnnGH1NSERILpIDBshgQOXQVDIFxfvCTl8J6W8mr5icrG3n2tv6aA1ca2LjyMsk1hOlDC9eFxw/640?wx_fmt=png)

**虚拟化平台安全知识点**

**关于 VMware**

VMware 是全球领先的企业级虚拟化解决方案提供商，大量企业基于 VMware 的虚拟化软件构建企业级私有云，包括很多国内的企业。相比于开源虚拟化方案 QEMU/KVM，VMware 更加成熟、稳定和易用，拥有很高的市场份额。

**虚拟化平台攻击方式介绍**

针对虚拟化平台的攻击主要有两种方式：

1、直接攻击虚拟化管理平台

由于大量企业未做好管理网络隔离，且虚拟化管理平台暴露面多，易出漏洞，已知漏洞修复不及时，另外虚拟机管理操作通常不是监控重点，常常是虚拟化相关的攻击目标。

常见攻击目标：VMware vCenter Server/VMware ESXi

攻击步骤：

1.   突破边界，通过渗透、社工等手段进入内网

2.   扫描发现，vCenter/ESXi 管理平台

3.   利用漏洞，获取管理平台权限

4.   接管 vCenter下所有 ESXi 主机或 ESXi 下所有虚拟机

攻击危害：

1、批量控制虚拟机，获取数据；

2、不直接攻击应用，可绕开部分检测。

![](https://mmbiz.qpic.cn/mmbiz_png/FOh11C4BDicSs1QnnGH1NSERILpIDBshge7SsTaRkRDjApxogbqxwaSHwnMSMlk7YhkMQyicvhEysGNKgW5IiaMEQ/640?wx_fmt=png)

2、进行虚拟机逃逸

当虚拟化管理平台已被网络隔离，攻击者无法直接攻击管理平台时，如果已经控制了一台虚拟机，则可以利用虚拟化漏洞实施虚拟机逃逸攻击，从而打破管理网络的隔离，批量接管虚拟机。

攻击目标：VMware ESXi

攻击步骤：

1.   控制一台虚拟机，渗透获取主机权限

2.   采集主机信息，识别虚拟化软件版本

3.   选择利用漏洞，完成虚拟机逃逸

4.   获取宿主机控制权，接管ESXi下所有虚拟机

攻击危害：

1、突破隔离，接入虚拟化管理平台，批量控制虚拟机，获取数据

2、不直接攻击应用，可绕开部分检测。![](https://mmbiz.qpic.cn/mmbiz_gif/FOh11C4BDicSs1QnnGH1NSERILpIDBshgzLx1G9eAbpFXK4vFSkJe31cQSSH52mWibibc4XxOs4JgXUiaIIxqKcPVw/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/FOh11C4BDicSs1QnnGH1NSERILpIDBshgibTTQP5abibwzz5Gf4tJiczhZunJ0ib8Z6RFSe7YjvxcqtZz8xdjxaZia2g/640?wx_fmt=png)

**全****悉（T-ANSWER）**

**可天然检出该勒索软件**

全悉（T-ANSWER）高级威胁分析预警系统支持从HTTP、SMTP、FTP、NFS、SMB、HTTP2、POP3、IMAP等协议流量中自动还原文件，还原文件类型超过40种，同时结合长亭自研恶意文件检测引擎、WebShell检测引擎以及动态沙箱对文件进行动静态交叉检测，具有高检出率、低误报率、防变种等特点。

在虚拟化平台安全相关的检测能力上，全悉（T-ANSWER）可检出包含但不限于以下相关漏洞：

1. VMware vRealize SSRF漏洞（CVE-2021-21975）

2. VMware EXSi 堆溢出漏洞（CVE-2021-21974）

3. VMware Cloud Director 远程代码执行漏洞（CVE-2020-3956）

4. VMware View Planner 远程代码执行漏洞（CVE-2021-21978）

5. Vmware Workspace Freemarker 模板注入漏洞（CVE-2022-22954）

6. vCenter 远程代码执行漏洞（CVE-2021-21985）

7. vCenter 任意文件上传漏洞（CVE-2021-21972）

8. vCenter 任意文件上传漏洞（CVE-2021-22005）

9. vCenter 远程代码执行漏洞（CVE-2021-21985）

10. vCenter Velocity 模板注入漏洞（CVE-2021-22005）

11. vCenter VSphere UI SSRF漏洞

12. 等等……

![](https://mmbiz.qpic.cn/mmbiz_png/FOh11C4BDicSs1QnnGH1NSERILpIDBshgIg5N9zCiazNmQ1VRTYCO66e6KfDVXnEqMlj4tlwOzPFGlOZWSkK1ZWA/640?wx_fmt=png)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_png/FOh11C4BDicSs1QnnGH1NSERILpIDBshgS1OQZYcwRm1JFiaCHy7DrWMlQNj6d95Rk34Eia3w3d9DvaWg0F2yWbYw/640?wx_fmt=png)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_png/FOh11C4BDicSs1QnnGH1NSERILpIDBshgxNQ5VXNagQvVyAh0mT6goX4TLVO0YRfs5eguuOtW0qfEVPibC8UztPQ/640?wx_fmt=png)

**点点赞**

![](https://mmbiz.qpic.cn/mmbiz_png/FOh11C4BDicSs1QnnGH1NSERILpIDBshgcYj8S7huTsGGn7Q3cTcAVziajRW5sD5hJlKHBu0R7xGvMebLErqCWkQ/640?wx_fmt=png)

**点在看**

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

长亭安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

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