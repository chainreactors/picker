---
title: “电子图书类”App个人信息收集情况测试报告
url: https://www.freebuf.com/news/373198.html
source: FreeBuf网络安全行业门户
date: 2023-07-28
fetch_date: 2025-10-04T11:54:49.423729
---

# “电子图书类”App个人信息收集情况测试报告

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

“电子图书类”App个人信息收集情况测试报告

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

“电子图书类”App个人信息收集情况测试报告

2023-07-27 13:28:13

所属地 上海

近期，中国网络空间安全协会、国家计算机网络应急技术处理协调中心对“电子图书类”公众大量使用的部分App收集个人信息情况进行了测试。测试情况及结果如下：

## **一、测试对象**

本次测试选取了19家应用商店,累计下载量达到1亿次的“电子图书类”App，共计8款，其基本情况如表1。

表1 8款App基本情况

![图片](https://image.3001.net/images/20230727/1690435187_64c1fe7380a1b92f78c21.png!small)

## **二、测试方法**

### **（一）测试环境**

本次测试选取相同品牌、型号的手机终端，安装相同版本安卓操作系统，分别部署8款App，在相同网络环境下进行同步操作。

### **（二）测试场景**

以完成一次电子图书阅读活动作为测试单元，包括启动App、搜索图书、阅读图书3种用户使用场景，以及后台静默应用场景⁽²⁾。

### **（三）测试内容**

本次测试包括系统权限调用、个人信息上传、网络上传流量3项内容。

## **三、测试结果**

### **（一）系统权限调用情况**

测试发现，8款App在4种场景下调用了位置、设备信息、应用列表、剪切板5类系统权限，未发现调用相机、麦克风、通讯录等其他权限。

（1）在启动App场景中，调用系统权限种类最多的为番茄免费小说（4类），调用系统权限次数最多的为百度阅读（23次）。具体情况如表2。

表2 启动App场景调用系统权限情况

![图片](https://image.3001.net/images/20230727/1690435207_64c1fe873b98c0d232307.png!small)

（2）在搜索图书场景中，调用系统权限种类最多的为番茄免费小说（2类），调用系统权限次数最多的为爱读掌阅和番茄免费小说（均为2次）。具体情况如表3。

表3 搜索图书场景调用系统权限情况

![图片](https://image.3001.net/images/20230727/1690435316_64c1fef447e63f221d585.png!small)

（3）在阅读图书场景中，调用系统权限种类最多的为番茄免费小说（3类），调用系统权限次数最多的为七猫免费小说（5次）。具体情况如表4。

表4 阅读图书场景调用系统权限情况

![图片](https://image.3001.net/images/20230727/1690435328_64c1ff002f249a32b76dc.png!small)

（4）在后台静默场景中，调用系统权限种类和次数最多的为百度阅读（3类，8次）。具体情况如表5。

表5 后台静默场景调用系统权限情况

![图片](https://image.3001.net/images/20230727/1690435339_64c1ff0b3aca5d211daf6.png!small)

### **（二）个人信息上传情况**

测试发现，8款App上传了4种类型个人信息：①位置信息，包括经纬度、当前连接Wi-Fi MAC地址、当前连接基站信息；②唯一设备识别码，包括Android ID（安卓ID）、OAID（开放匿名设备标识符）、手机MAC地址；③应用列表信息，包括手机上已安装、新安装和新卸载的应用信息；④用户使用App产生的交互信息，包括搜索词。

（1）在启动App场景中，个人信息上传种类最多的为QQ阅读、七猫免费小说、爱读掌阅、番茄免费小说、百度阅读（均为2类）。具体情况如表6。

表6 启动App场景个人信息上传情况

![图片](https://image.3001.net/images/20230727/1690435350_64c1ff164ca76b30932f6.png!small)

（2）在搜索图书场景中，个人信息上传种类最多的为微信读书、QQ阅读、七猫免费小说、番茄免费小说（均为2类）。具体情况如表7。

表7 搜索图书场景个人信息上传情况

![图片](https://image.3001.net/images/20230727/1690435366_64c1ff262e0319de8a358.png!small)

（3）在阅读图书场景中，个人信息上传种类最多的为书旗小说、七猫免费小说、百度阅读（均为2类）。具体情况如表8。

表8 阅读图书场景个人信息上传情况

![图片](https://image.3001.net/images/20230727/1690435378_64c1ff328ed7218db8c9c.png!small)

（4）在后台静默场景中，个人信息上传种类最多的为书旗小说（2类）。具体情况如表9。

表9 后台静默场景个人信息上传情况

![图片](https://image.3001.net/images/20230727/1690435390_64c1ff3e139929fa15a94.png!small)

### **（三）网络上传流量情况**

（1）8款App在用户完成一次电子图书阅读活动（启动App、搜索图书、阅读图书）时，上传数据流量平均⁽³⁾最多的为番茄免费小说，约为1321KB；平均最少的为微信读书，约为30KB。具体情况如图1。

![图片](https://image.3001.net/images/20230727/1690435401_64c1ff49d9a44e79973e9.png!small)

图1 完成一次电子图书阅读活动的平均上传数据流量（单位：KB）

（2）8款App后台静默12小时，上传数据流量平均⁽⁴⁾最多的为百度阅读，约为81KB；平均最少的为QQ阅读，约为13KB。具体情况如图2。

![图片](https://image.3001.net/images/20230727/1690435417_64c1ff59efac009e1f293.png!small)

图2 后台静默12小时平均上传数据流量（单位：KB）

**注释：**

⁽¹⁾包括华为应用市场、小米应用商店、腾讯应用宝、OPPO软件商店、VIVO应用市场、360手机助手、百度手机助手、豌豆荚手机助手、历趣应用商店、乐商店、魅族应用商店、移动MM商店、太平洋下载、中关村在线、木蚂蚁安卓应用市场、多特软件站、华军软件园、西西软件园、绿色资源网。

⁽²⁾启动App指用户点击图标启动App至首页加载完毕；搜索图书指用户点击首页搜索栏，按照预设的固定搜索词（如“西游记”）完成一次搜索操作；阅读图书指用户点击阅读搜索得到的第一条结果，并在阅读10页后停止；后台静默指用户启动App后，直接切换到后台保持静默状态。

⁽³⁾共重复测试10次。

⁽⁴⁾共重复测试10次。

本文来源：中国网络空间安全协会

# 资讯 # 数据安全

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

一、测试对象

二、测试方法

* （一）测试环境
* （二）测试场景
* （三）测试内容

三、测试结果

* （一）系统权限调用情况
* （二）个人信息上传情况
* （三）网络上传流量情况

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