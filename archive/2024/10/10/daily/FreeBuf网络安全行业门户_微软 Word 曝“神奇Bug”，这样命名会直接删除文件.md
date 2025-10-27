---
title: 微软 Word 曝“神奇Bug”，这样命名会直接删除文件
url: https://www.freebuf.com/news/412315.html
source: FreeBuf网络安全行业门户
date: 2024-10-10
fetch_date: 2025-10-06T18:53:01.793307
---

# 微软 Word 曝“神奇Bug”，这样命名会直接删除文件

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

微软 Word 曝“神奇Bug”，这样命名会直接删除文件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

微软 Word 曝“神奇Bug”，这样命名会直接删除文件

2024-10-09 11:39:33

所属地 上海

![](https://image.3001.net/images/20241009/1728445157_6705fae52ac09d15dccc5.png!small)近日，微软确认Word应用中存在一个“神奇的”Bug，可能导致用户在特定情况下错误地删除文件，影响所有使用Office 2024版本的用户。

据微软支持中心发布的消息称，如果用户在命名 Word 文件时使用大写文件格式（例如.DOCX 或.RTF 而不是.docx 或.rtf），或者在文件名中包含#符号，文件在保存时可能会被直接移入回收站。

好在是这个漏洞不会永久删除文件，因此如果你的 Word 文件受到影响，可以检查回收站以恢复文件。比较糟糕的是，虽然文件可以从回收站恢复，但可能会导致更改的内容未保存，这对频繁编辑和保存文档的用户来说可能带来不便。

为了避免出现此问题，微软建议用户在关闭文件之前手动保存，因为该问题似乎只在点击窗口右上角的 X 并以这种方式保存文件时发生。

此外，微软还建议用户访问“文件 > 选项 > 保存 > 使用键盘快捷键打开或保存文件时不显示 Backstage”，并启用此功能，直到推出修复程序。如果不想冒文件被删除的风险，可以尝试使用在线版本的 Word。所有文件都保存在云端，不受此漏洞影响。

微软正在开发修复程序，用户可以通过访问Windows搜索框中用管理员权限打开命令提示符窗口，粘贴以下命令来恢复到以前的版本，直到修复程序发布：

```
cd %programfiles%\Common Files\Microsoft Shared\ClickToRun officec2rclient.exe /update user updatetoversion=17928.20156
```

# 系统安全 # 数据安全

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