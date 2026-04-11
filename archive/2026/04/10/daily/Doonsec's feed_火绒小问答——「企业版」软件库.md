---
title: 火绒小问答——「企业版」软件库
url: https://mp.weixin.qq.com/s/ml8WToHXbFmKqJAg6SlHhA
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:19:02.445809
---

# 火绒小问答——「企业版」软件库

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/u1Oy5xQ01Sp6iaHDib4jliavOwsyrFcEgfOrdCIpPfhS4v6ibt6WnD9iaYCnYnk49eQOdNxOSGdOnUOiaDtyyGZe47cPwwFt7MJGxACA9tPibrm4ico/0?wx_fmt=jpeg)

# 火绒小问答——「企业版」软件库

火绒安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz6h5nbHLqtyUeLADJt7ewgFh6AbCAxQeO9D2y9CcDK7liaJDD5PZGwbqURKywb0SqKeiaCUIgyLTVkw/640?wx_fmt=gif&from=appmsg#imgIndex=0)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOD1VIU0cQXJ1e93CQZVRIzOibHApq61lNKn3nx1959LbVdTxPOlPH6Bw/640?wx_fmt=gif&from=appmsg)

**尊敬的用户，您好！**

为方便您更好地使用火绒企业版软件库功能，实现企业内部软件的统一管理与安全分发，我们为您整理了详细的操作说明，涵盖中心配置、终端使用及重要注意事项，您可按照以下流程进行操作：

**一、**

**中心配置：创建和管理软件库**

**1. 进入软件库管理界面**
登录火绒控制中心，导航至【资产管理】->【软件库】。界面分为**本地软件库**和**云软件库**两个标签页。

**2. 管理本地软****件库**
本地软件库用于上传企业内部私有软件或公网没有的安装包。
**添加软件：**
1.点击**【添加】**。
2.**上传安装包：**大小不超过10GB，支持.exe, .msi, .zip, .dmg, .pkg 等常见格式。

3.**填写信息：**包括软件名称（必填，≤20字）、选择软件分类、适用系统（Windows/macOS）、适用架构（x86\_64等）、版本号、发布者，并可上传软件图标（建议256×256像素，≤2MB）。
4.添加成功后，软件默认处于**“下架”**状态。
**软件操作：**
o**上架：**将软件变为上架状态，终端应用中心可见并可下载。
o**下架：**将软件变为下架状态，终端应用中心将隐藏该软件。
o**编辑：**修改软件信息。
o**删除：**从库中彻底移除。
o**移动分类：**将软件转移到其他分类。
**分类管理：**支持自定义软件分类（如“办公软件”、“开发工具”），可新建、重命名、删除及调整显示顺序。默认的**【其他应用】**分类不支持删除和重命名。

**3. 管理云软件库**
云软件库由火绒安全团队维护并定期更新。
**获取软件列表：**点击**【刷新】**按钮，系统会访问火绒服务器（https://api.softmanagent.huorong.cn/\*）获取最新软件列表。所有软件默认处于**“下架”**状态。
**上架软件：**手动将需要的软件设置为**“上架”**状态，终端方可下载。
**注意：**云软件库数据仅首次自动获取，之后需手动点击**【刷新】**才能更新列表。

**4. 配置防护策略（关键步骤）**
软件库必须配合防护策略才能对终端生效。
1.进入**【防护策略】****->【策略管理】**，选择或创建一个策略，点击**【策略详情】**。
2.在策略详情页，找到**【行为管理】**下的**【应用中心】**模块，并**开启**该功能。
3.在应用中心设置中：
o**勾选【显示本地软件库】：**终端将显示本地库中已上架的软件。
o**勾选【显示云软件库】：**终端将显示云库中已上架的软件。
o**至少勾选一项**，否则会提示错误。
**4.精细控制（可选）**：
o点击本地或云软件库右侧的**【设置】**按钮，可以弹出自定义列表。
o在此列表中，可以针对每一个已上架的软件，单独设置其状态为**【显示】**或**【隐藏】**，实现更精准的管控。

**5.设置云软件下载途径（单选）：**
o**无法从外网下载时，从中心下载（默认）**：终端优先直连外网下载，失败则从中心下载。

![企业版1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sr3XPTKxicXMlDe8StQkuqa2fPMTloqd0peTGQic3uH4oJsxpic4ibWNeT2mvbX2gbfE5FC5uP56X2cloxnIPFPqHYtnZ3A6DTB42k/640?wx_fmt=png&from=appmsg)

o**仅从外网下载：**终端始终直接从火绒云服务器下载。
o**仅从中心下载：**终端始终从中心下载，中心会代为从外网获取。

**二、**

**终端使用：在应用中心下载软件**

**1. 访问应用中心**
对于Windows或macOS终端，在火绒客户端界面可以看到**【应用中心】**入口（需其所属策略已开启应用中心功能）。

**2. 浏览和下载软件**
应用中心页面会自动筛选显示适用于当前终端操作系统和架构的软件。
支持按软件分类、适用系统、适用架构进行筛选，也支持按软件名称搜索。
点击软件旁的**【下载】**按钮即可开始下载，同时最多进行3个下载任务。
下载完成后，可点击**【打开】**直接运行安装包，或点击**【打开文件夹】**定位到文件。

**3. 终端设置**
在终端应用中心页面，可以点击设置图标进行以下配置：
**软件下载目录：**自定义软件保存路径。
**添加快捷方式：**可选择在桌面（Windows）或启动器（macOS）创建“应用中心”快捷方式。
**云软件下载方式：**此处设置会覆盖中心策略的设置（需断开中心策略后才能修改）。

**三、**

**重要注意事项**

**1.连接要求：终端必须与中心保持在线连接**，否则软件库功能将失效。

2.平台限制：目前仅**Windows**和**macOS终端**支持软件库功能。Linux服务器版与Linux桌面版终端不支持。

3.安装包限制：本地软件库的单个安装包大小不得超过**10GB**。

4.策略同步：如果在软件库中将某个软件**下架**或**删除**，那么所有防护策略的自定义列表中该软件会自动变为**【隐藏】**状态。

5.备份说明：执行中心数据备份时，会备份软件库的**信息列表和图标**，但**不会备份软件安装包本身**。

**总结来说，使用软件库的核心流程是：在中心上传或刷新软件并上架 -> 在防护策略中开启“应用中心”并勾选要显示的库 -> 终端在应用中心浏览和下载软件。**通过此功能，您可以实现企业内部软件的统一、安全、可控分发。

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