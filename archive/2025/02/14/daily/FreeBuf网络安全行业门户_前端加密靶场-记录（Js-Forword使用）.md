---
title: 前端加密靶场-记录（Js-Forword使用）
url: https://www.freebuf.com/sectool/421750.html
source: FreeBuf网络安全行业门户
date: 2025-02-14
fetch_date: 2025-10-06T20:35:56.567668
---

# 前端加密靶场-记录（Js-Forword使用）

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

前端加密靶场-记录（Js-Forword使用）

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

前端加密靶场-记录（Js-Forword使用）

2025-02-13 19:02:52

所属地 河南省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

靶场名称：encrypt-labs

地址：https://github.com/SwagXz/encrypt-labs

使用工具：Google浏览器，Yakit、Js-Forword

## 拿第一关来学习工具（AES固定key）

首先需要分析加密函数，找到加密函数里边加密前的明文字符串变量。

![1739442764_67adca4c37728b456cb4a.png!small?1739442765994](https://image.3001.net/images/20250213/1739442764_67adca4c37728b456cb4a.png!small?1739442765994)

这里我打断电这一行代码应该就是未加密的字符串，调试一下。

![1739442832_67adca90bb3a0f1f193f4.png!small?1739442834458](https://image.3001.net/images/20250213/1739442832_67adca90bb3a0f1f193f4.png!small?1739442834458)

很显然就是，那么我们就可以使用Yak中原生的插件Js-Forword（单独去下载这个脚本配合burp也可以使用）

![1739442964_67adcb1460cbcac710f54.png!small?1739442966102](https://image.3001.net/images/20250213/1739442964_67adcb1460cbcac710f54.png!small?1739442966102)

填入参数名后点击启动，然后可以看到输出来一条payload:

var xhr = new XMLHttpRequest();xhr.open('POST', 'http://127.0.0.1:54772', false);xhr.send(jsonData);jsonData=xhr.responseText;

这里需要把payload插入到加密函数的第一行，其实原来我理解的就是，将用户输入浏览器提交的数据拦截做一个转发，转发后，再传递给后边的加密函数体。因此插入的的函数位置应该需要在如下位置：

```
document.getElementById("loginForm")
	.addEventListener("submit", function(event) {
		event.preventDefault();
		document.getElementById("modal")
			.style.display = "flex";
	});

function sendDataAes(url) {
	const formData = {
		username: document.getElementById("username")
			.value,
		password: document.getElementById("password")
			.value
	};
	const jsonData = JSON.stringify(formData);
//也就是下边这一行是插入的
	var xhr = new XMLHttpRequest();xhr.open('POST', 'http://127.0.0.1:54772', false);xhr.send(jsonData);jsonData=xhr.responseText;

	const key = CryptoJS.enc.Utf8.parse("1234567890123456");
	const iv = CryptoJS.enc.Utf8.parse("1234567890123456");
```

这里需要注意jsonData是一个常量，需要将他改成let或者var

然后就是需要替换浏览器加载网站的js

### 浏览器加载网站的JS替换

1. 首先找一个位置，存放本地JS文件，最好是空文件夹，这里需要将easy.js复制过来到本地，然后再插入如上所述的payload。![1739443671_67adcdd7025db3304fb4b.png!small?1739443672796](https://image.3001.net/images/20250213/1739443671_67adcdd7025db3304fb4b.png!small?1739443672796)
2. 点击替换内容然后选择刚才保存的js文件![1739443732_67adce148f50e3d4b59f6.png!small?1739443734431](https://image.3001.net/images/20250213/1739443732_67adce148f50e3d4b59f6.png!small?1739443734431)
3. 如下图所示：![1739443785_67adce493be1417cfc044.png!small?1739443786969](https://image.3001.net/images/20250213/1739443785_67adce493be1417cfc044.png!small?1739443786969)
4. 之后就可以随意的更改JS中文件的内容了，要注意的是更改后需要ctrl+s保存，未保存的会有星号提示![1739443895_67adceb710aeccf0c7f54.png!small?1739443896746](https://image.3001.net/images/20250213/1739443895_67adceb710aeccf0c7f54.png!small?1739443896746)

之后便能看到传输加密前的明文了。![1739444006_67adcf26612f5395929ca.png!small?1739444008568](https://image.3001.net/images/20250213/1739444006_67adcf26612f5395929ca.png!small?1739444008568)

**优点：使用操作较为简单，不需要去尝试去逆向找到解密方法。**

**缺点：会在劫持面板失去原本的URL，并且只能进行手工改包，不能使用爆破模块，在YAK或者burp中显示的回包无法显示真是的服务器响应数据，只能通过浏览器查看，对于某些逻辑漏洞或注入不方便发送到重放模块进行测试。**

# web安全

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

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

拿第一关来学习工具（AES固定key）

* 浏览器加载网站的JS替换

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