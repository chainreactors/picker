---
title: 红队工具--Erebus
url: https://mp.weixin.qq.com/s/LluvT4-OzeTAAmpD5PFySQ
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:18:07.785904
---

# 红队工具--Erebus

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EYGYnyEdzQV2UDdF9VNIZI1TPicic6ibS9ibXxa0ibg2xqGjgFZJD6djbWLBd7dWDJKfeVR9ewpmF56uVKf3z50WJicVLIPYtCYvCKIjg4icauUoCc/0?wx_fmt=jpeg)

# 红队工具--Erebus

原创

Hello888
Hello888

安全天书

![]()

在小说阅读器中沉浸阅读

0x01 工具介绍

Erebus是一种现代初始访问封装器，旨在缩短开发到部署时间，以备战入侵行动。Erebus自带多种开箱即用的技术，可以打造复杂的链条，并帮助绕过最严密的安全措施。

这个项目旨在扩展你的进攻能力，绝不是对所有环境的万能灵丹。如果你想添加自己的技术或修改现有技术，请查看项目文档页面获取更多信息。

![厄瑞玻斯旗](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQX40SQ12Da2hEhggOfK97tqyNjNB61XFt50QPoIMkUKxWz9nxh8xsRibn0xEzAN7LxkYmhnfwNGzpWWMG97GLkvrUEAice6duweM/640?wx_fmt=png&from=appmsg)

## 如何在Mythic中以这种格式安装代理

当你需要测试安装或让其他用户安装代理时，过程相当简单。在 Mythic 里，你可以用三种方式运行二进制来安装：`mythic-cli`

* `sudo ./mythic-cli install github https://github.com/Whispergate/Erebus`安装主分支
* `sudo ./mythic-cli install github https://github.com/Whispergate/Erebus branchname`安装该仓库的特定分支
* `sudo ./mythic-cli install folder /path/to/local/folder/cloned/from/github`从已经克隆下来的代理仓库安装

现在，你可能会想知道，你或用户*应该什么*时候这样做，才能正确地将你的代理添加到他们的Mythic实例中。这里没有绝对的错误答案，主要看你的偏好。这三种选择分别是：

* Mythic已经上线了，然后你可以运行安装脚本，直接指挥该代理的容器启动（比如 如果该代理有自己的特殊C2容器，你也需要通过 ） 启动它们。`sudo ./mythic-cli start erebus_wrapper``sudo ./mythic-cli start erebus_wrapper`
* Mythic已经上线了，但你想减少步骤，可以直接安装代理并运行。这个脚本会先*停止*所有容器，然后重新启动所有设备。这也会带来你刚安装的新代理。`sudo ./mythic-cli start`
* Mythic没有运行，你可以安装脚本然后直接运行。`sudo ./mythic-cli start`

GitHub地址：

```
https://github.com/Whispergate/Erebus
```

注意：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测。

0x02 红蓝偶像练习生小圈子

更多工具思路文章请加入纷传，圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结以及自研工具与插件，目前圈子已满300人，欢迎各位进圈子交流学习！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/EYGYnyEdzQXeo0okuglWRpI7Py2lk7FKScP7A2aOgicuUDJH7wjk0DbnFDLDFXHSAOoqc0xK54YMaXNZFB4neRMyNicCOKicssGeq8S04TyFjw/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

****圈子目前更新相关技术文章：**

***** HeavenlyBypassAV内部版工具-轻松免杀各大杀软
* Heavenly白加黑自动化生成免杀工具
* HeavenlyProtectionCS内部CS插件
* 冰蝎webshell免杀工具

* 哥斯拉webshell免杀工具
* 红队场景下lnk钓鱼Bypass免杀AV
* Frp免杀隧道工具
* 1day和0dayPOC
* lnk钓鱼思路视频讲解
* lnk钓鱼Bypass天擎
* msi钓鱼
* chm钓鱼
* Kill360核晶
* AV对抗-致盲AV（核晶）
* 捆绑免杀360
* Kill火绒
* 火绒6.0内存免杀
* kill-windows Defender

* Defender分离免杀
* Defender知识点
* EDR对抗思路
* 进程注入知识点

* 自启动思路
* **多种维权手法**

* Fscan免杀核晶
* QVM解决思路
* 红队思路-钓鱼环境下小窗口截屏窃取
* 免杀Todesk/向日葵读取工具

* 渗透测试文章思路
* 内网对抗文章思路
* **还有更多红队工具文章！期待您的加入！！！********

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

安全天书

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

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