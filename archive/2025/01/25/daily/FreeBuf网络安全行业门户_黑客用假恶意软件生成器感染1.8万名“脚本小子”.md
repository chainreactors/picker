---
title: 黑客用假恶意软件生成器感染1.8万名“脚本小子”
url: https://www.freebuf.com/articles/endpoint/420809.html
source: FreeBuf网络安全行业门户
date: 2025-01-25
fetch_date: 2025-10-06T20:10:13.036851
---

# 黑客用假恶意软件生成器感染1.8万名“脚本小子”

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

黑客用假恶意软件生成器感染1.8万名“脚本小子”

* ![]()
* 关注

* [终端安全](https://www.freebuf.com/articles/endpoint)

黑客用假恶意软件生成器感染1.8万名“脚本小子”

2025-01-24 11:34:40

所属地 上海

![黑客笑脸](https://image.3001.net/images/20250125/1737738051301278_4899c861b25d4b8bb7da83a575e3d8dc.jpg!small)

一名威胁行为者针对低技能的黑客（俗称“脚本小子”）发起攻击，使用一款假的恶意软件生成器，秘密感染他们的设备，植入后门以窃取数据并控制计算机。

CloudSEK的安全研究人员报告称，该恶意软件在全球范围内感染了18,459台设备，其中大部分位于俄罗斯、美国、印度、乌克兰和土耳其。

CloudSEK的报告指出：“一个特洛伊化的XWorm RAT生成器被武器化并传播开来。**它专门针对那些刚接触网络安全的脚本小子**，这些人会直接下载并使用各种教程中提到的工具，这表明‘盗亦有道’并不存在。”

CloudSEK发现，该恶意软件包含一个“终止开关”，用于从许多受感染的设备中卸载恶意软件。但由于实际操作的限制，部分设备仍然处于被感染状态。

![受感染设备的位置](https://image.3001.net/images/20250125/1737738052170795_09316c86597a4c5a9460f25ac6a472fe.jpg!small)**受感染设备的位置**来源：CloudSEK

## 假RAT生成器植入恶意软件

研究人员表示，他们最近发现了一个特洛伊化的XWorm RAT生成器，通过GitHub仓库、文件托管平台、Telegram频道、YouTube视频和网站等多种渠道传播。

这些渠道宣传该RAT生成器，声称其他威胁行为者可以免费使用该恶意软件。然而，它并非真正的XWorm RAT生成器，而是感染了威胁行为者的设备。

一旦设备被感染，XWorm恶意软件会检查Windows注册表，判断是否在虚拟化环境中运行。如果确认是虚拟环境，恶意软件将停止运行。如果主机符合感染条件，恶意软件会对注册表进行必要的修改，以确保在系统重启后仍能持续运行。

每个受感染的系统都会通过硬编码的Telegram机器人ID和令牌注册到一个基于Telegram的命令与控制（C2）服务器。恶意软件还会自动窃取Discord令牌、系统信息和位置数据（通过IP地址），并将其发送到C2服务器，然后等待操作员的指令。

在总共支持的56条命令中，以下几条尤为危险：

* **/machine\_id\*browsers**– 窃取浏览器中保存的密码、Cookie和自动填充数据
* **/machine\_id\*keylogger**– 记录受害者在计算机上输入的所有内容
* **/machine\_id\*desktop**– 捕获受害者的当前屏幕
* **/machine\_idencrypt** – 使用提供的密码加密系统上的所有文件
* **/machine\_idprocesskill** – 终止特定运行进程，包括安全软件
* **/machine\_idupload** – 从受感染的系统中窃取特定文件
* **/machine\_id\*uninstall**– 从设备中远程卸载恶意软件

CloudSEK发现，恶意软件操作员从大约11%的受感染设备中窃取了数据，主要是截取受感染设备的屏幕截图（如下所示）并窃取浏览器数据。

![黑客桌面截图](https://image.3001.net/images/20250125/1737738052637784_4ad3d5fb23904a00b7b8356033f8fda4.jpg!small)**黑客桌面截图**来源：CloudSEK

## 利用终止开关破坏僵尸网络

CloudSEK的研究人员通过使用硬编码的API令牌和内置的“终止开关”，从受感染的设备中卸载恶意软件，从而破坏了僵尸网络。

为此，他们向所有监听客户端发送了批量卸载命令，遍历了之前从Telegram日志中提取的所有已知设备ID。他们还假设设备ID为简单的数字模式，尝试暴力破解1到9999之间的ID。

![](https://image.3001.net/images/20250126/1737857484_679599cca7de9c0dafb32.png!small)**发送卸载命令**来源：CloudSEK

尽管这一操作成功从许多受感染的设备中移除了恶意软件，但在命令发出时未在线的设备仍然处于被感染状态。此外，Telegram对消息发送速率有限制，因此部分卸载命令可能在传输过程中丢失。

黑客攻击黑客的场景在现实中并不罕见。CloudSEK的研究结果提醒我们，永远不要信任未签名的软件，尤其是那些由其他网络犯罪分子分发的软件，并且只能在测试/分析环境中安装恶意软件生成器。

**参考来源：**

> [Hacker infects 18,000 "script kiddies" with fake malware builder](https://www.bleepingcomputer.com/news/security/hacker-infects-18-000-script-kiddies-with-fake-malware-builder/)

# 网络安全 # 终端安全

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

假RAT生成器植入恶意软件

利用终止开关破坏僵尸网络

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)