---
title: 别乱安装壁纸! Wallpaper Engine创意工坊恶意壁纸可用于攻击
url: https://mp.weixin.qq.com/s/mh66xLBgCENWCR3VVu7Lyg
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:46:44.821951
---

# 别乱安装壁纸! Wallpaper Engine创意工坊恶意壁纸可用于攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDoFJG9Jd8o5PRfxhECAdGsmicTbkPvNGumsvs6b3gv3a722SnXsrh7KyibDgQPurYbovAgiahaR5jmVGxGyPlKlAgn0ZAuzoUgIQc/0?wx_fmt=jpeg)

# 别乱安装壁纸! Wallpaper Engine创意工坊恶意壁纸可用于攻击

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

自2025年末起，Steam创意工坊平台出现批量恶意Wallpaper Engine动态壁纸，攻击者利用软件“应用壁纸”的代码执行特性，将恶意载荷嵌入壁纸文件中传播。攻击核心目标为窃取玩家Steam账户权限，同时可向终端植入后门、加密货币挖矿程序等恶意组件。

经卡巴斯基统计，已发现数十款具备感染能力的恶意壁纸，单款下载量可达数千至数万次，受害用户高度集中于中国与俄罗斯地区。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpo2QfQEmEPPwLBB2j6G06F2xnP6UHzmvTSU3qedWR4hef1ia9Ehyrep8duBdXic1iapdPadsw4EszVYibU0nP3MzHyvicPZPle8EtM/640?wx_fmt=jpeg)

本次攻击的核心利用点为Wallpaper Engine的应用类壁纸功能(application)：

该类型壁纸本质是独立Windows可执行程序，可直接在用户本地运行代码；结合Steam创意工坊低门槛的开放上传机制，攻击者无需复杂免杀即可实现恶意内容的规模化分发。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDr2UHJOBZZrlRAnb56HCvBFyfF05U87QmlG7K7FicrMcHRHCHb4gaaAYw63XfdDAUSVISoZKFo74gWo6ax0rZCcsrRlP1dM4PQM/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDoeVE48DFKbeJhRxB4Fe2sFApnGOR51DqCHZbRglUaTvia5MBU3oL3HTnClDicnOk1rZPJAkh20SiboBbcjVrpXCHYoGemcVmWzicA/640?wx_fmt=jpeg)

目前两种主流传播手法

直连打包型：将恶意EXE、DLL文件或脚本与正常壁纸程序封装在同一压缩包，用户应用壁纸时恶意载荷自动触发执行。

加密隐藏型：恶意载荷存放于带密码保护的压缩包内，密码明文隐藏在压缩包文件名或配套JSON配置文件中，通过内置脚本自动解密执行，或诱导用户手动输入密码解压。

以捕获的游戏类恶意壁纸样本为例，完整攻击流程分为4个阶段：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDo0asa1f0iaMb6As6WHRF7L7ACP8eETvV3FuHKoibc5ic60YVWSOInUicXFTqQ54gEyuf1IzrR7tJ8g6R8P9oWnbBnBZyThaz8PwAk/640?wx_fmt=jpeg)

1. 伪装启动与载荷释放
用户应用壁纸后，.\_cache\_GAME1.exe模块启动前台游戏界面作为迷惑，同时向C:\ProgramData\目录释放DarkKomet家族后门程序Synaptics.exe，完成后门驻留。

2. 系统DLL篡改与凭证窃取
.\_cache\_GAME1.exe同时加载被篡改的系统库AggregatorHost.dll，该恶意DLL遍历本地进程列表，精准匹配steam.exe与steamchina.exe进程，读取内存中的活跃登录会话数据。

3. 数据回传与会话接管
被篡改的DLL将窃取的Steam会话ID、账户信息通过HTTP请求外发至攻击者C2服务器120.48.156[.]17/ey.php；攻击者拿到有效会话后，可直接绕过登录验证接管受害者Steam账户。

4. 蠕虫式二次传播
攻击者利用被盗账户向Steam创意工坊上传新的恶意壁纸，扩大攻击范围，形成自传播链条。

本次攻击涉及的恶意载荷覆盖信息窃取器（Lumma、Vidar）、后门（DarkKomet）、勒索程序、挖矿程序、加载器（RenEngine）等多类家族，工具栈分散无统一特征，研判为多个独立黑客团伙同时利用该传播渠道牟利，非单一组织的定向攻击。

可重点关注以下异常特征：

系统目录出现非官方签名的Synaptics.exe文件

系统AggregatorHost.dll文件哈希、路径异常

终端向本次披露的C2地址发起HTTP外联请求

用户侧：谨慎下载“Application（应用）”类型壁纸，优先使用视频、场景类壁纸；应用新壁纸前先通过杀毒软件扫描；开启Steam令牌二次验证，降低会话被盗后的账户损失。

自查C2服务器地址
http://202.144.192[.]29
http://120.48.156[.]17
http://brightly[.]to

参考:

https://securelist.com/dozens-of-malicious-wallpapers-found-on-steam-workshop/120186/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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