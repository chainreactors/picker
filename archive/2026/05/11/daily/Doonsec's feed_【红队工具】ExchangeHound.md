---
title: 【红队工具】ExchangeHound
url: https://mp.weixin.qq.com/s/Q4H6hbtOU7Zz3rgVHN0e1Q
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:33:51.729865
---

# 【红队工具】ExchangeHound

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EYGYnyEdzQVN7PFmiabCaUuwiaDHsic2tBkD6mc8CG2sPCGdush0sJeG1oyz6VMPlta9Hr11hgUWYdeoqaSKNNhzYiaqkXrGw8zUHrNpJ44mV9M/0?wx_fmt=jpeg)

# 【红队工具】ExchangeHound

原创

Hello888
Hello888

安全天书

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担！！！

工具介绍

Microsoft Exchange本地权限的防御性OpenGraph收集器。ExchangeHound 主要面向蓝队、侦测工程师和ADExchange防守者。它将邮箱委托和 Exchange 控制平面关系映射到一个你可以在BloodHound 查询的图中。它关注高价值关系，如  文件夹权限、公共文件夹 ACL、传输规则和 Exchange RBAC 分配。`FullAccess``SendAs``SendOnBehalf`

```
PS C:\Users\Administrator\Desktop\ExchangeHound> .\ExchangeHound.ps1 -CollectAll
    +-------------------------------------------------+    |               ExchangeHound v1.0                |    |   BloodHound OpenGraph Collector for Exchange   |    |    https://github.com/filippwn/ExchangeHound    |    +-------------------------------------------------+
Tip: If Exchange cmdlets are missing, run: Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn[16:03:22] CollectAll enabled. Turning on all optional collectors and full visibility flags.[16:03:22] [*] Starting mailbox collection...[16:03:22] Filters: MailboxType=UserMailbox,SharedMailbox,RoomMailbox,EquipmentMailbox | OU= | Filter=[16:03:22] [*] Enumerating mailboxes...[16:03:22] Collecting UserMailbox mailboxes...[16:03:26] Found 16 UserMailbox mailboxes[16:03:26] Collecting SharedMailbox mailboxes...[16:03:26] Found 1 SharedMailbox mailboxes[16:03:26] Collecting RoomMailbox mailboxes...[16:03:26] Found 1 RoomMailbox mailboxes[16:03:26] Collecting EquipmentMailbox mailboxes...[16:03:26] Found 1 EquipmentMailbox mailboxes[16:03:26] [+] Total mailboxes collected: 19[16:03:26] [*] Collecting permissions and building OpenGraph...[16:03:44] [*] Processing: 19/19 mailboxes | 116 edges | 1.1/sec | ETA: 0s[16:03:45] [*] Collecting public folder permissions...[16:03:45] [*] Collecting transport rules...[16:03:45] [!] Could not resolve SID for: eh.uc2.drop@external.test[16:03:46] [*] Collecting Exchange RBAC role assignments...[16:03:46] [!] Could not resolve SID for: Exchange Online-ApplicationAccount[16:03:46] [!] Could not resolve SID for: Default Role Assignment Policy
[16:03:47] [+] Collection complete!
ExchangeHound Collection Summary  Mailboxes      : 19  Nodes          : 172  Edges          : 338  Databases      : 1  Folder Nodes   : 21  Folder Edges   : 25  Calendar Folders: 19  Calendar Edges  : 23  Public Folder Nodes: 5  Public Folder Edges: 6  Transport Rules : 2  Transport Edges : 5  Transport Endpoints: 1  RBAC Roles      : 87  RBAC Role Edges : 202  AD Principal Nodes: 34  Unresolved SIDs: 18  Duration (sec) : 20.5  Output         : C:\Users\Administrator\Desktop\ExchangeHound\ExchangeHound_20260417_160322.json
[16:03:47] Ingest the JSON file via BloodHound UI: Administration > File Ingest[16:03:47] Then use Cypher queries from queries/exchange_path_queries.md to analyze.
```

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQWulVdL3RWqWgcLrtH55auQSLcIWeltcjrzX209HKkM89K3Y9g0v1IxRhRUicMpFvt9Bd3LXW7icic0AaLlibgmarCsrWSezOtRy6c/640?wx_fmt=png&from=appmsg)

GitHub地址：

```
https://github.com/FilipPwn/ExchangeHound
```

注意：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测。

**红蓝偶像练习生小圈子**

**更多工具思路文章请加入纷传，圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结以及自研工具与插件，目前圈子已满300人，欢迎各位进圈子交流学习！**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQWBtF8n8G0Q2qfYY1ibia316d2wgL8ahMh9EibkrWnczXfFDWV5Y343ALUG25u4rrz03obawnZCHXubM8k9NyrlAUpUydG5nA0m4s/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

****圈子目前更新相关技术文章：**

***** HeavenlyBypassAV内部版工具-轻松免杀各大杀软
* HeBypassAV内部版Patch免杀工具-轻松绕过杀软EDR
* Heavenly自动化红队后渗透工具免杀生成器
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

******往期推荐**

**[安全天书免杀课来袭｜助力实战免杀钓鱼(文末送福利)](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485167&idx=1&sn=7ab4393e75cf94d13cb79e22b92fb8d0&scene=21#wechat_redirect)**

**[Patch免杀0检测！！！绕过卡巴斯基、360、Defender、火绒等](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485194&idx=1&sn=e29a965863c59bbd26cf4b306d58301a&scene=21#wechat_redirect)**

**[【红队工具】红队内网后渗透CobaltStrike插件更新](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485006&idx=1&sn=e3bcf2070226fcfc93b565ae2c9d85ad&scene=21#wechat_redirect)**

**[全新版本--Heavenly自动化生成白加黑2.0版本](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485067&idx=1&sn=94ac2f5b6b58345bb892da7527352cab&scene=21#wechat_redirect)**

**[绕过360安全卫士实现维权](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485280&idx=1&sn=467194cdf681646597a84e7f08b638bf&scene=21#wechat_redirect)******

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