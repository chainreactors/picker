---
title: 火绒小问答——「企业版」中心登录密码
url: https://mp.weixin.qq.com/s/RL4KkeoFtsAA67Mqnb6lnQ
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:34:43.979032
---

# 火绒小问答——「企业版」中心登录密码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/u1Oy5xQ01Sp46MiaibU8tI3WNjIQvoLRq3iakZJ1N8HmdCbCoxNUyiaqDfSbqa0X90aLwUjksSuDXWRr88cSDE1QTdPiaTzVc158gmibka46pVLcE/0?wx_fmt=jpeg)

# 火绒小问答——「企业版」中心登录密码

火绒安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz6h5nbHLqtyUeLADJt7ewgFh6AbCAxQeO9D2y9CcDK7liaJDD5PZGwbqURKywb0SqKeiaCUIgyLTVkw/640?wx_fmt=gif&from=appmsg#imgIndex=0)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOD1VIU0cQXJ1e93CQZVRIzOibHApq61lNKn3nx1959LbVdTxPOlPH6Bw/640?wx_fmt=gif&from=appmsg)

**尊敬的用户，您好！**

为保障您的火绒控制中心账号安全，规范密码管理操作，特此为您整理了首次登录密码修改、日常密码更新、忘记密码重置及相关安全设置的详细指引。请您仔细阅读以下内容，按照步骤操作，确保账号及系统安全，感谢您对火绒产品的支持与信任！

**一、**

**首次登录与初始密码修改**

**1.默认凭证：**
o 超级管理员默认账号为**admin**，默认密码为**admin**。
o 首次登录Windows控制中心时，系统会**强制要求修改**这个弱口令密码。

o Linux控制中心在安装完成后需直接设置8-32位的超级管理员密码

**2.新密码要求：**
o 密码必须由**8-32位**的**大小写****字母、数字、特殊字符**组合而成。
o 修改成功后，系统会自动使用新密码登录。

**二、**

**日常密码修改（已知原密码）**

如果您是已登录的管理员，可以随时修改自己的密码：
1.登录控制中心后，点击页面右上角的**管理员头像/名称**。

2.在下拉菜单中点击**【密码修改】**。

3.在弹出的窗口中：
o **输入原始密码**（当前登录账号的密码）。
o **输入新密码**（需符合8-32位强密码规则）。
o **再次输入新密码**进行确认。

4.点击确定即可完成修改。

**三、**

**忘记密码重置（超级管理员）**

如果忘记了超级管理员 (admin) 密码，无法登录，需要使用凭证进行重置。此方法适用于**Windows**和**Linux**版控制中心。

**重置步骤：**
**第1步：获取凭证（在外网电脑操作）**
1.使用浏览器访问火绒官网：**https://lic.buy.huorong.cn/**。

2.使用您的**产品序列号和密码**登录。
3.进入**【安装包工具】**页面「超管凭证」处，点击**【生成凭证】**。
4.设置一个新的超级管理员密码（8-32位强密码），**并再次确认**。
5.点击**【生成并下载】**。凭证文件将自动下载到本地。

o**重要：**该凭证**有效期为24小时**，下载后请尽快使用。

**第2步：应用凭证修改密码（在控制中心服务器操作）**
**Windows 系统：**
1.找到控制中心的配置工具。通常位于：C:\Program Files (x86)\Huorong\ESCenter\ 目录下的Wizard.exe。
2.运行配置工具，在**【密钥与账号设置】**部分，勾选**【修改密码】**。
3.点击 【上传凭证】，选择第1步下载的凭证文件。
4.点击 【保存】，密码即被修改为凭证中设置的新密码。

**Linux 系统：**
1.通过SSH登录到安装控制中心的Linux服务器。
2.切换到中心命令目录：cd /opt/apps/huorong/escenter/bin
3.执行密码重置命令：sudo ./hrcenter reset-root-password
4.根据命令提示，**输入凭证文件的完整路径**。
5.确认操作后，密码即被修改。

**四、**

**相关安全设置与注意事项**

**1.登录保护：**
o 密码连续输错**5次**后，账户将被锁定**15分钟**。
o 登录后无操作**5分钟**（默认，可设置），系统会自动登出。

**2.定期修改密码：**
o 管理员可以在**【账号管理】->【设置】**中开启**【定期修改密码设置】**。开启后，密码超过设定时间未修改，登录时将强制进入修改页面。

**3.动态认证（二次验证）：**
o 在**【账号管理】->【设置】**中可开启动态认证。
o 开启后，管理员登录时需输入**动态口令**进行二次验证。
o 还可为非超级管理员设置高危操作（如远程桌面、文件分发等）也需要动态认证。

**4.凭证使用前提：**
o 使用凭证重置密码要求控制中心已**激活授权**。
o 中心版本需为**2.0.15.0**及以上。

**总结与建议**
**忘记密码：**通过官网生成**24小时****有效**的凭证进行重置。

**安全加固：**建议启用**定期修改密码**和**动态认证**功能，并设置合理的自动登出时间。

**凭证管理：**生成的凭证包含新密码，具有时效性，请妥善保管并尽快使用，勿泄露给他人。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOD1VIU0cQXJ1e93CQZVRIzOibHApq61lNKn3nx1959LbVdTxPOlPH6Bw/640?wx_fmt=gif&from=appmsg)

尊敬的用户：

若您有其他产品使用问题，可通过以下方式联系我们~

****微信公众号******：**主界面---常见问题---人工客服

****火绒官方论坛：****https://bbs.huorong.cn/

****火绒官方服务热线：****400-998-3555（法定工作日8:30-20:30，法定节假日9:30-18:30）

HUORONG

火绒安全成立于2011年，是一家专注、纯粹的安全公司，致力于在终端安全领域为用户提供专业的产品和专注的服务，并持续对外赋能反病毒引擎等相关自主研发技术。多年来，火绒安全产品凭借“专业、干净、轻巧”的特点收获了广大用户的良好口碑。火绒企业版产品更是针对企业内外网脆弱的环节，拓展了企业对于终端管理的范围和方式，提升了产品的兼容性、易用性，最终实现更直观的将威胁可视化、让管理轻便化，充分达到保护企业信息安全的目的。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4K1e9ubHiaGLicyPrL2TGOQUVuzGfhiavltoNEsaCLCyJXChRib3yHaPTI00hV8oFkSsvwgunn2k0wSg/640?wx_fmt=png#imgIndex=11)

求点赞

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN05z6DXwgVYcdZ6RFjwxdDoeAEia9eYdgyJaAJ0LDBJmxTdm2JUhkc4tg/640?wx_fmt=gif&from=appmsg#imgIndex=12)

求分享

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN0CbyZz9kNTCKcA0puOEWfAYZnT6v6rr3kdBWIFw4TlSh7AgzSdOfAng/640?wx_fmt=gif&from=appmsg#imgIndex=13)

求喜欢

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN0gBxG1O1Y7YCFGicYGrDUpcBg7iaLgNpCsDzNKcHwHcBgKktMtTSs6ZSA/640?wx_fmt=gif&from=appmsg#imgIndex=14)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

火绒安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

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