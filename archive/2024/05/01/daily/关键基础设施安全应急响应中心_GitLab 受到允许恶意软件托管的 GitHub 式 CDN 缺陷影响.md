---
title: GitLab 受到允许恶意软件托管的 GitHub 式 CDN 缺陷影响
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247543539&idx=4&sn=9bacc9ffd8d845d9660c57f639d5e020&chksm=c1e9a6a2f69e2fb4dc76e558a71794ea564577ae840e7e02a0b73cd976015105a81e9742ed03&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-05-01
fetch_date: 2025-10-06T17:19:27.792708
---

# GitLab 受到允许恶意软件托管的 GitHub 式 CDN 缺陷影响

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogtQwb7z1ouPCnCE870kNxnL5dguDibS1UEvvQhAjtOWbDGmLU2VPZ037KHpZVfjhMibcy0pjibW4To2w/0?wx_fmt=jpeg)

# GitLab 受到允许恶意软件托管的 GitHub 式 CDN 缺陷影响

关键基础设施安全应急响应中心

安全研究机构最近报告了威胁分子如何滥用 GitHub 缺陷来推送恶意软件，同时使其看起来像是托管在可信组织的官方源代码存储库上。

虽然大多数与恶意软件相关的活动都是基于 Microsoft GitHub URL，但这个“缺陷”可能会被 GitHub 或 GitLab 上的任何公共存储库滥用，从而允许威胁分子创建非常令人信服的诱饵。

**GitLab 评论也可能被滥用来推送恶意软件**

例如，攻击中使用的以下 URL 使这些 ZIP 看起来像是存在于 Microsoft 的源代码存储库中：

https://github[.]com/microsoft/vcpkg/files/14125503/Cheat.Lab.2.7.2.zip

https://github[.]com/microsoft/STL/files/14432565/Cheater.Pro.1.6.0.zip

然而，经过调查，这些文件（属于恶意软件）在 Microsoft 的代码存储库中却找不到。

相反，这些内容存在于 GitHub 的 CDN 上，很可能是由滥用该平台“评论”功能的威胁分子上传的。

在对提交或拉取请求留下评论时，GitHub 用户可以附加一个文件（档案、文档等），该文件将上传到 GitHub 的 CDN 并使用以下格式的唯一 URL 与相关项目关联：' https: //www.github.com/{project\_user}/{repo\_name}/files/{file\_id}/{file\_name}。'

对于视频和图像，文件将存储在该/assets/路径下。

在用户将文件添加到未保存的评论后，GitHub 会自动生成下载链接，而不是在发布评论后生成 URL，如下所示。这使得威胁分子可以在用户不知情的情况下将其恶意软件附加到任何存储库。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29B3JYtyeyCibTe4gaQ5MViawQj74uQwBVAp3WhKyNYlDKSoLFxArAJGNbWjEe7XdxnltKDu2SffNpQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

将文件添加到评论时自动生成的下载链接来源

即使评论从未实际发布或后来被用户（或攻击者）删除，该文件的链接仍然有效。

自动恶意软件分析服务 UNPACME 的 Sergei Frankoff上个月就该漏洞进行了关注，表示威胁分子正在积极滥用该漏洞。

除此之外，GitLab 也未能幸免于这个问题，用户也可以以类似的方式滥用 GitLab 上的“评论”功能。

在测试中，用户能够将 GitLab 的 CDN 的文件上传，但看起来这些文件存在于 Inkscape 和 Wireshark 等流行开源项目的 GitLab 存储库中：

https://gitlab[.]com/inkscape/inkscape/uploads/edfdbc997689255568a7c81db3f3dc51/InkScape-2024-Latest.exe

https://gitlab[.]com/wireshark/wireshark/uploads/b4162053fbb4dc6ee4f673c532009e16/WireShark-v4.2.4-stable-release.exe

测试中使用的文件是良性 JPG 图像，已重命名为 .exe，以演示威胁分子如何通过滥用此功能来误导用户下载带有恶意软件的假冒软件版本。

上传到 GitLab CDN 的此类文件遵循的格式是：

https://gitlab.com/{project\_group\_namr}/{repo\_name}/uploads/{file\_id}/{file\_name}

这里的file\_id看起来像 MD4 或 MD5 哈希值，而不是更简单的数字标识符。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29B3JYtyeyCibTe4gaQ5MViawhAeqFNh4vaYKD9J9NuV6KJuntiavPxqy9sNibqLr9uxEK1icSNIBf6tAQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

将文件添加到 GitLab 评论时自动生成的下载链接

与 GitHub 非常相似，即使攻击者从未发布过评论或后来删除了评论，生成的 GitLab 文件链接仍将保持活动状态。

GitLab 确实会提示用户先登录，然后才能上传或下载这些文件，但这并不能阻止威胁分子上传这些文件。

由于几乎每个软件公司都使用 GitHub 或 GitLab，因此此缺陷使威胁分子能够开发出极其狡猾且表面看起来值得信赖的诱饵。

例如，威胁分子可以在 NVIDIA 的驱动程序安装程序存储库中上传恶意软件可执行文件 ，该恶意软件可执行文件伪装成修复流行游戏中问题的新驱动程序。或者，威胁分子可以在Google Chromium 源代码的评论中上传文件，并假装它是网络浏览器的新测试版本。

这些 URL 似乎也属于该公司的存储库，这使得它们看起来更加真实。即使公司得知他们的存储库被滥用来传播恶意软件，也找不到任何允许他们管理或删除附加到其项目的文件的设置。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/gitlab-affected-by-github-style-cdn-flaw-allowing-malware-hosting/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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