---
title: 警惕新型木马Rocinante！通过伪装银行应用程序窃取账号密码等敏感数据
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649786833&idx=1&sn=d580f516b950f7793b70ae07cbe632e8&chksm=8893b9bebfe430a8884150b89b937a49498bb088fe5ac38bd70926f29c835b1a6432797bcbff&scene=58&subscene=0#rd
source: 安全客
date: 2024-09-05
fetch_date: 2025-10-06T18:26:45.657245
---

# 警惕新型木马Rocinante！通过伪装银行应用程序窃取账号密码等敏感数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5TQic6RdHia7hIkwrMSocI7fnBYm8Qr4UibWLkOCfxvgT8YzN8ecfzaiaT0jD7rMweibJlX42O3XzibfyQ/0?wx_fmt=jpeg)

# 警惕新型木马Rocinante！通过伪装银行应用程序窃取账号密码等敏感数据

安全客

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5TQic6RdHia7hIkwrMSocI7f3oRakPZGNNvnXvwZ7WplkpHHcXI4sS5gk7x4HhWpJ7WzIT6GmEHLiag/640?wx_fmt=jpeg&from=appmsg)

最近，名为Rocinante的新型安卓银行木马病毒正针对巴西的移动用户。

荷兰安全公司ThreatFabric表示：“这个木马家族能够通过无障碍服务执行键盘记录，还能够通过伪装成不同银行的钓鱼界面窃取受害者的个人信息。最后，它可以利用这些被窃取的信息，通过无障碍服务权限实现设备接管（DTO），从而对感染设备进行完全的远程访问。”

该木马的主要目标包括如Itaú Shop、Santander等金融机构，伪装的应用程序包括Bradesco Prime和Correios Celular等。

涉及的虚假应用程序包括：

Livelo Pontos（com.resgatelivelo.cash）

Correios Recarga（com.correiosrecarga.android）

Bradesco Prime（com.resgatelivelo.cash）

Módulo de Segurança（com.viberotion1414.app）

源代码分析显示，Rocinante的内部名称是Pegasus（或PegasusSpy）。需要指出的是，这里的Pegasus与商业监控供应商NSO Group开发的跨平台间谍软件没有任何关系。

Pegasus被认为是由一个名为DukeEugene的威胁行为者所为，他也以类似的恶意软件而闻名，如ERMAC、BlackRock、Hook和Loot。Silent Push最近的分析指出，ThreatFabric发现Rocinante木马中有部分直接受到早期ERMAC版本的影响，这可能与ERMAC源代码在2023年的泄露有关。

ThreatFabric指出：“这是第一次有原始木马家族从泄露的代码中取用了一部分，并将其实施到自己的代码中。” 也有可能这些版本是同一项目的不同分支。

Rocinante主要通过钓鱼网站进行分发，目的是诱使用户安装伪造的 dropper 应用程序。一旦安装，这些程序会请求无障碍服务权限，以记录感染设备上的所有活动、拦截短信，并显示钓鱼登录页面。

它还与指挥和控制（C2）服务器建立联系，等待进一步指令——模拟触摸和滑动事件——以远程执行。窃取的个人信息会被传输到一个Telegram机器人。

ThreatFabric指出：“该机器人提取通过伪造的登录页面获取的有用个人信息，然后将这些信息格式化后发布到犯罪分子可以访问的聊天中。”

“根据使用的伪造登录页面，信息会有所不同，包括设备信息如型号和电话号码、CPF号码、密码或账户号码。”

此外，Symantec还指出了另一种银行木马恶意软件活动，该活动利用secureserver[.]net域名针对西班牙语和葡萄牙语地区。

“这一多阶段攻击开始于恶意URL，导向一个包含混淆的.hta文件的压缩档案，”这家Broadcom旗下的公司表示。

“该文件会下载一个JavaScript有效载荷，该有效载荷执行多个反虚拟机（AntiVM）和反病毒（AntiAV）检查，然后下载最终的AutoIT有效载荷。这个有效载荷通过进程注入加载，目的是窃取受害者系统中的银行信息和凭证，并将其传输到C2服务器。”

另外，市场上出现了一种新的“扩展服务”——通过新的Genesis Market销售，这个市场在2023年初被执法部门关闭。该服务旨在通过恶意的浏览器扩展程序窃取拉丁美洲（LATAM）用户的敏感信息，这些扩展程序通过Chrome Web Store传播。

这一活动自2023年中期开始，主要针对墨西哥及其他LATAM国家，由一个名为Cybercartel的电子犯罪组织实施，该组织向其他网络犯罪团伙提供这类服务。扩展程序现在已无法下载。

Metabase Q Ocelot威胁情报团队的安全研究人员Ramses Vazquez和Karla Gomez表示：“恶意的Google Chrome扩展伪装成合法应用程序，诱使用户从受感染的网站或钓鱼活动中安装它。”

“一旦安装，这个扩展会将JavaScript代码注入用户访问的网页中。这段代码可以拦截和修改网页内容，并捕获敏感数据，如登录凭证、信用卡信息和其他用户输入，具体取决于特定活动和目标信息类型。”

文章来源：https://thehackernews.com/2024/09/rocinante-trojan-poses-as-banking-apps.html

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5TQic6RdHia7hIkwrMSocI7f9o8XJyFCQUkLM2bmudvSqA7yS2ftqeUCVJOhUZm1DZ97UzOvC56XwA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5TQic6RdHia7hIkwrMSocI7fPYkc0EzJ8HhdmWIzUIb5Y8NhtibAtRl5aiaOpA8Ncyibqk8Ricg6769zrg/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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