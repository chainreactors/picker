---
title: jython环境安装&&插件Upload Auto Fuzz推荐
url: https://mp.weixin.qq.com/s/uRXhrqCzEEYGoarScQXzhg
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:27:05.086517
---

# jython环境安装&&插件Upload Auto Fuzz推荐

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79EgR2AdkHE1t62IUy3TbmsA3icWUbTQftIOb72PlHB1p7rI9nicOpYkFw/0?wx_fmt=jpeg)

# jython环境安装&&插件Upload Auto Fuzz推荐

陌笙
陌笙

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

插件说明

```
简介一个用于测试文件上传功能安全性的 Burp Suite 插件。通过 Intruder 模块自动生成各类绕过 payload，覆盖常见的文件上传限制场景。
v1.2.0 更新内容架构重构
采用策略模式重写，代码结构更清晰新增配置面板，可自定义测试范围支持 Burp Suite 深色主题功能增强
新增后端语言选择（PHP/ASP/ASPX/JSP）新增 14 种独立的 Fuzz 策略，可单独启用/禁用payload 数量提升至 1000+优化去重算法，减少无效请求新增测试点
双写绕过：pphphp、aspaspform-data 污染：多分号、脏数据替换未闭合引号：filename="shell.phpURL 编码 Content-Type：image%2Fphp配置文件内容注入：.htaccess / .user.ini 实际利用内容测试覆盖范围后缀绕过可执行扩展名变体：php3/php5/phtml/phar/asa/cer/ashx/jspx 等大小写混淆：pHp、PhP、aSp、JsP双写绕过：pphphp、aspasp、jspjsp特殊字符：空格、点号、分号（shell.php.、shell.php;.jpg）空字节截断：shell.php%00.jpg请求头操控Content-Disposition 大小写：ConTENT-DisPoSitionform-data 污染：删除、替换为脏数据、多分号filename 参数：双 filename、空 filename、未闭合引号、多等号换行注入：filename\n="shell.php"Content-Type 绕过MIME 类型伪造：image/gif、image/png、application/octet-streamURL 编码：image%2Fgif、image%2Fphp双重 Content-Type 头大小写变换系统特性利用Windows
NTFS 数据流：shell.php::$DATAIIS 分号解析：shell.asp;.jpg保留设备名：con.php、aux.asp尾部空格/点号Linux
Apache 多扩展名：shell.php.jpg路径穿越：../shell.php隐藏文件：.shell.php编码绕过URL 编码扩展名：%70%68%70双重 URL 编码MIME 编码（RFC 2047）Unicode 字符替换配置文件上传.htaccess：SetHandler 解析任意文件为 PHP.user.ini：auto_prepend_file 文件包含web.config：IIS handlers 配置文件内容魔术字节注入：GIF89a、PNG 头、PDF 头WebShell 内容（可选）图片头 + WebShell 组合
```

插件环境安装

```
本插件需要python环境，Burpsuite本身是支持java的，Jython就是java和python的结合。
```

```
jython地址https://www.jython.org/download
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79IcQSQsuWXma9QVUHdx6VI6b8z4ZC09U6VfzNHtibbrUEdY2NUJ9PZuQ/640?wx_fmt=png&from=appmsg)

```
因为有几个师傅说安装这个环境的时候会报错，所以可以像我这样安装，大概率没问题（其实没必要这样）。
首先，在C盘下面创建一个文件夹名字不要有中文，然后将下载后的jython文件，放到文件夹里面。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79vVn1JtaxkOy7BAzwEIpTxZ73uDx0ia1m6ticiaUoNvZzywCY0A1fpVYTQ/640?wx_fmt=png&from=appmsg)

```
然后右键，打开cmd,查看java版本，我这里是java8直接运行刚才下载的jython文件java -jar .\jython-installer-2.7.4.jar
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79kfBjlmUiagDfVBgf0Via9UCReIUjE1smN23xUaF87WM6Xib4l0Nibr2IIQ/640?wx_fmt=png&from=appmsg)

```
出现这个页面点击下一步
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE790WK9xYm1fanxRMxwOicibwuvnBERGD9u4vibFgQHtnXCeorLgcGATaQmg/640?wx_fmt=png&from=appmsg)

```
点击，我接受然后下一步
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79NsudLKFtdvketphuYuZ405OONic4cmic1Y1SDau8UbzJAC6vFOlia75tQ/640?wx_fmt=png&from=appmsg)

```
直接下一步
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79U9VClsZEDe32o8zaq4pKVibEj6H9Jrc0YBEib68KZKNdPWL2Jw4DpYzg/640?wx_fmt=png&from=appmsg)

```
然后给这个jython选择一个目录,如果不是根目录，放这个文件的目录不要有中文，可以保持默认然后点击下一步
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79c5LY0gDkDBjcoicicxL6Kib6Faf1uboB8uYm5VVQDmD4MNXLyawrembsw/640?wx_fmt=png&from=appmsg)

```
点击下一步之后直接安装成功，然后来到我们刚才选择的jython安装目录
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79yeib9e3sia5xI0cGoZm1vhmXnM9H8rgHQYZrrKsiapFeiciaLD5cfL97X3Q/640?wx_fmt=png&from=appmsg)

```
看到jython.jar，就是按照成功了，打开burpsuite给他导入进去
```

```
我这里使用的是burp的2025版本打开之后点击扩展设置
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE792eGsMhE72ibeic2GQSoX2bNlBjYQic7chWkVQcl0fgWzbwOjhJDt1o1tg/640?wx_fmt=png&from=appmsg)

```
点击Extensions往下滑找到python环境路径选择如图所示，如果自定义的目录，就选自己的
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79MExjEHr8D136w0fv7TlKxfAqLyicGcdKYaiasvIQXGmXXo9ykUM6qIVA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79uzYSL4Zp9ty4aibdu43ribI7bJvDgg5dAJY7YFtvdoicZ1nh3IvbCVs6A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79gM9GOgev2Fd9VAicqk1dvdREDAcyOZqRQSotlT3YsfVOOpNG28vCibBw/640?wx_fmt=png&from=appmsg)

插件安装

```
到这里插件所需的python环境就已经完成了，我们后续正常导入插件即可点击扩展，添加
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79PZHAJn2AmwiaYiaS6tamA7ryHNbnp1S6CVqs2xTX4ZBMgjFJLCtDJU1w/640?wx_fmt=png&from=appmsg)

选择我们对应的下载插件

```
插件地址https://github.com/T3nk0/Upload_Auto_Fuzz
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79GZ5NaTyvZibNsyQJtFYmib4ylCcDqS4Z0ndwicKtS2qyunbY7ZcQ3o6Ow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79RgB5RqAnich2XzXZTJggyQpgqZK2XDFg2WWTeRhiawJjiaJTn8rBbp1Xg/640?wx_fmt=png&from=appmsg)

```
点击下一步成功加载扩展
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE795hrPEOvKgZRRZSMNn850hfG4D2ChCicaPAsDwiajLzvhvh1KaK7s8zjA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79U5yibZvZqOekosxF0ibXUIWKmhiaiaCj4nHBX2dicSps54CcMDibr3QmnZjg/640?wx_fmt=png&from=appmsg)

插件使用

```
遇到上传点的时候，正常上传图片，然后抓包。
```

1. 抓取文件上传请求，发送到 Intruder

2. 选中需要 Fuzz 的区域（建议选中整个文件部分）：

```
Content-Disposition: form-data; name="file"; filename="test.jpg"Content-Type: image/jpeg
[文件内容]
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79gLyAwz6O4M4jOsYVPBZhgdX6w8Xo09tAwKt04gibznDhQPBoUpUuOMA/640?wx_fmt=png&from=appmsg)

Payloads 标签页配置：

- Payload type: Extension-generated

- Select generator: Upload\_Auto\_Fuzz 1.2.0

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79fNN03oB7iaokv5A1mF7WvLooJynUYDialDg0fYmk8D5BpbbuyzNzoY6A/640?wx_fmt=png&from=appmsg)

重要：取消勾选 Payload Encoding

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE791nacfFPEIYzmQfSrKmL29icYjFtHPB4a34NLKaanoc5JkNNRmoVNBOw/640?wx_fmt=png&from=appmsg)

开始攻击，根据响应长度/状态码筛选结果

payload示例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79YTPOW5na4ZEvZWpGsBTUFvUJlvIjB22RSiaXkaW6UOWCdCkJTt7icNaw/640?wx_fmt=png&from=appmsg)

绕过策略说明

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6Zk5QWExvC1DmhY8FnjE79VjLCEJftib7ZYWvjVJ5IVG7tBx89kzz72b19qLF8RH9gIW5EhdPvIvg/640?wx_fmt=png&from=appmsg)

后台回复加群加入交流群

有思路需要的师傅可以加入小圈子

主要内容是（2025-2026/edusrc实战报告）

其他内容懂得都懂，持续更新中

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAV25rGkkJ8qOPAooDwASNSaiaGJibu3z2mOqnD2vCnOQB6ia3AfuuOZ0ZDg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

陌笙不太懂安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

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