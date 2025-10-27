---
title: Falcon Sensor 在数周前导致 Linux 内核崩溃 恢复工具已推出
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520157&idx=2&sn=a93459b30ee5e2a9c5d7fde92fbadf1f&chksm=ea94bef7dde337e10afa600f28254053392253623ae5fc070b7b622dcdff148744cc5c6cc9cf&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-23
fetch_date: 2025-10-06T17:43:30.546095
---

# Falcon Sensor 在数周前导致 Linux 内核崩溃 恢复工具已推出

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRHO7dK6kxC6c9eIqquUIKw5KapQNd4zOLrhQwwVNxW8nN7tZYh8ibJbgGRII3JialnD5lia9KOFKiaDw/0?wx_fmt=jpeg)

# Falcon Sensor 在数周前导致 Linux 内核崩溃 恢复工具已推出

综合编译

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**CrowdStrike 公司如今已变得臭名昭著的 Falcon Sensor 软件在上周导致全球大量 Windows 计算机宕机，而它也曾导致 Linux 机器崩溃。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRHO7dK6kxC6c9eIqquUIKw6aTQPS5eTVBtYOhaXCOBj9sHibRc0IjORrFLIBoCn7SssVPHUf8Neibw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRHO7dK6kxC6c9eIqquUIKwPjafWfDXVzvbibUp4n6oj4EkqDXqpMqM95f7wdhccoSQ5LMW50BbItQ/640?wx_fmt=png&from=appmsg)

**Linux 机器恐慌和崩溃**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRHO7dK6kxC6c9eIqquUIKwPjafWfDXVzvbibUp4n6oj4EkqDXqpMqM95f7wdhccoSQ5LMW50BbItQ/640?wx_fmt=png&from=appmsg)

Red Hat 公司在6月份层提醒客户注意“在falcon-sensor 进程启动 5.14.0-427.13.1.el9\_4.x86\_64后观测到的内核恐慌”情况，在内核版本5.14.0-427.13.1.el9\_4.x86\_64启动后一些 Red Hat Enterprise Linux 9.4 客户受到内核恐慌的影响。

该公司还发布另外一个题为“cshook\_network\_ops\_inet6\_sockraw\_release+0x171a9 处系统崩溃”的问题，建议用户“获取关于 CrowdStrike Falcon Sensor/Agent安全软件套件提供的内核模块 falcon\_lsm\_serviceable 的潜在问题的调试协助”，并建议“禁用 CrowdStrike Falcon Sensor/Agent 软件套件将在调查期间，缓解崩溃现象并向该系统提供临时稳定性”，“已经注意到该问题但它不仅限于6和7版本。”

另一些报告称，CrowdStrike 疑似也导致 Debian 和 Rocky Linux 出现问题。

Linux 内核恐慌和 Windows 蓝屏死机大致可相提并论。内核恐慌情况在 Windows 蓝屏死机发生的数周前就发生了。CrowdStrike 公司并未就此置评。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRHO7dK6kxC6c9eIqquUIKw6aTQPS5eTVBtYOhaXCOBj9sHibRc0IjORrFLIBoCn7SssVPHUf8Neibw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRHO7dK6kxC6c9eIqquUIKwPjafWfDXVzvbibUp4n6oj4EkqDXqpMqM95f7wdhccoSQ5LMW50BbItQ/640?wx_fmt=png&from=appmsg)

**逻辑错误是罪魁祸首**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRHO7dK6kxC6c9eIqquUIKwPjafWfDXVzvbibUp4n6oj4EkqDXqpMqM95f7wdhccoSQ5LMW50BbItQ/640?wx_fmt=png&from=appmsg)

CrowdStrike 公司表示，在2024年7月19日推送的一个例行传感器配置更新触发逻辑错误，从而导致全球计算机系统蓝屏死机。

该公司提到已经通过更新 Channel File 291的方式修正了该逻辑错误，除此以外并未做出任何其它修改。Falcon 仍在评估和防御 named 管道的滥用。目前该公司仍在分析该逻辑错误如何产生。CISA表示将与各方一起评估影响并提供修复支持。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRHO7dK6kxC6c9eIqquUIKw6aTQPS5eTVBtYOhaXCOBj9sHibRc0IjORrFLIBoCn7SssVPHUf8Neibw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRHO7dK6kxC6c9eIqquUIKwPjafWfDXVzvbibUp4n6oj4EkqDXqpMqM95f7wdhccoSQ5LMW50BbItQ/640?wx_fmt=png&from=appmsg)

**恢复工具已推出**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRHO7dK6kxC6c9eIqquUIKwPjafWfDXVzvbibUp4n6oj4EkqDXqpMqM95f7wdhccoSQ5LMW50BbItQ/640?wx_fmt=png&from=appmsg)

CrowdStrike 在上周日透露称将推出快速恢复工具，加速受影响系统的修复速度。有研究人员分析预测，全球约850万台 Windows 机器受影响。

微软也推出了一款从可启动 USB 存储设备运行的修复工具，并提供了相关使用指南。该公司在上周日修改了这些指令，要求完全擦除USB设备，“使其用于恢复过程时不会出错退出。”该工具已发布在https://go.microsoft.com/fwlink/?linkid=2280386。要使用微软的恢复工具，IT员工需要一台至少具有8GB空间的64位客户端，在该设备上的管理员权限，至少1GB存储空间的USB驱动以及Bitlocker恢复密钥（如需）。值得注意的是，需要32GB或以下的 USB 闪存驱动，以免无法通过 FAT 32进行格式化，而这是启动驱动所必须的。该恢复工具通过从微软下载的一个 PowerShell 脚本而创建，需要以管理员权限运行。在运行时它将格式化 USB 驱动并创建自定义的 WinPE 镜像，之后被复制到驱动并使其可启动。该批量脚本将提示用户输入必要的 Bitlocker 恢复密钥。之后将在文件夹C:\Windows\system32\drivers\CrowdStrike中查找 CrowdStrike 内核驱动，如检测到则会自动删除。测试发现，该批量文件将不会创建 CrowdStrike 驱动的日志或脚本。脚本运行完成后，将提示用户按下任何键，设备就会重启。驱动删除后，设备应该会返回 Windows 并可用。不过 Windows 管理员的最大障碍是检索任何所需的 Bitlocker 恢复密钥。因此，判断是否需要这些密钥以及如何恢复应该是尝试恢复设备的第一步。

CrowdStrike 公司发布了该事件的技术详情，还提供了如何恢复通过 BitLocker 加密的 Windows 机器。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[关于CrowdStrike 使 Windows 蓝屏死机，你需要知道的都在这里](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520109&idx=1&sn=f70fb8a65546c2f9ad15c895357b4258&chksm=ea94be07dde33711cb8de08051d20315cae01150c1cce58af83248ce1933418d827a742b82ab&scene=21#wechat_redirect)

[NSS 实验室以反托拉斯名义起诉赛门铁克 CrowdStrike 等巨头](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488136&idx=6&sn=5730e02fbc8893758828952b4df94fec&chksm=ea9723e2dde0aaf4274477a06677d4cc93a93309d670a459611b3919556b1450f2a2da2c2c18&scene=21#wechat_redirect)

[CrowdStrike推出网络安全搜索引擎](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485493&idx=2&sn=107cf2a26af25a55cdb057bed8c932ad&chksm=ea97395fdde0b04989eca48fcefcb3406977440abdfae011903596d1d33ed0d3b398694edb15&scene=21#wechat_redirect)

**原文链接**

https://www.theregister.com/2024/07/21/crowdstrike\_linux\_crashes\_restoration\_tools/

https://www.securityweek.com/crowdstrike-says-logic-error-caused-windows-bsod-chaos/

https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-repair-tool-to-remove-crowdstrike-driver/

题图：Pexels License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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