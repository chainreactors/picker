---
title: 中国背景嫌疑的拼图与缺角：质疑Proofpoint对UNK_MassTraction事件的溯源证据链
url: https://mp.weixin.qq.com/s/QXrXhNyc8Mo4RiRj9aDNuQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T06:01:38.924155
---

# 中国背景嫌疑的拼图与缺角：质疑Proofpoint对UNK_MassTraction事件的溯源证据链

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d1JenMt8pF0y6CCjeZUXGW2qhQTiaputLTxiaz1EQQK8QmgibaW05ISfBJaqOl5ibrtYccu92aMUIBwcuOBjsdJR054uTiaIkM4EwVA/0?wx_fmt=jpeg)

# 中国黑客嫌疑的拼图与缺角：质疑Proofpoint对UNK\_MassTraction事件的溯源证据链

原创

网空闲话
网空闲话

网空闲话plus

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年7月初，网络安全公司Proofpoint发布报告称，自当年5月起，一个被命名为UNK\_MassTraction的威胁集群利用开源邮件系统Roundcube的两处N-day漏洞，对美加两国多所高校的物理与工程学科展开定向渗透，并将该活动与某东方大国的网络行动方挂钩。然而，当我们逐条审视其证据的排他性时，不难发现其中存在明显的链条缺口——将一次技术特征模糊的攻击直接关联到特定国家归属，结论下得或许过于仓促。

![](https://mmbiz.qpic.cn/mmbiz_jpg/lQ1jXOMq3d2nFJRqQDdwVNqPVCKWagRGenib5wWwpI3gIaCw6rYiafKmhPpXbdv9uDO1NNeE3Ya3UQGp2lyRyibZhlf8T7aJWHlkJehgy3qN0Q/640?wx_fmt=jpeg&from=appmsg)

#### 精密攻击链：从一封邮件到服务器沦陷

攻击的起点是投递至目标院系管理人员与教授邮箱的普通钓鱼邮件。这些邮件内容泛泛，类似营销或垃圾信息，但发件地址要么来自已遭入侵的真实账号，要么利用DMARC策略松散的可伪造域名。邮件利用了Roundcube的一个跨站脚本漏洞（CVE-2024-42009，CVSS评分9.3），只要收件人在浏览器中打开邮件，内嵌的JavaScript即自动执行，无需任何点击交互。

执行的脚本充当加载器，从远程拉取一个被命名为“IceCube”的凭据窃取器。该恶意代码的技术细节凸显了攻击者的精心设计：它首先通过DOM遍历逃逸出Roundcube的iFrame沙箱，从而获得浏览器完整DOM及认证会话的访问权；接着大肆窃取用户名、密码、双因素认证材料、Cookie，并对浏览器语言、屏幕尺寸乃至表单字段值进行细致侦察。所有数据通过HTTP POST回传至指挥控制服务器。Proofpoint报告特别指出，IceCube的代码包含详尽的多行注释、清晰的执行阶段标记以及以“修复”命名的迭代更新，极可能是在大型语言模型辅助下生成的。

窃密得手后，IceCube并未止步。它利用已窃取会话中的跨站请求伪造令牌，化身为武器平台，针对Roundcube的第二个高危漏洞发起攻击。该反序列化漏洞（CVE-2025-49113，CVSS评分9.9）使攻击者能将精心构造的PHP对象注入服务器数据库，一旦对象被销毁，嵌入的shell命令便会执行，从而在服务器上植入一个名为“SquareShell”的网页后门。该后门位于`plugins/newmail_notifier/mail_preview.php`，可通过`system`、`passthru`、`exec`、`shell_exec`、`assert`、`popen`等六种系统函数实现远程代码执行，且其文件修改时间被刻意复制自合法插件的时间戳，以融入环境、躲避检查。

若SquareShell部署失败，攻击链不会中断。自2026年6月起，攻击者引入了备选通道：通过漏洞执行一个bash脚本，该脚本会检测主机架构，从控制服务器获取适配的加载器，并使用`nohup`工具执行。这个被谷歌威胁情报团队追踪为“SNOWLIGHT”的ELF加载器，会通过检查`/tmp/log_de.log`文件避免重复运行，伪装成内核进程`[kworker/0:2]`，最终在内存中加载全功能后门VShell。VShell是一款用Go语言编写的公开可用植入物，提供交互式shell和端口转发功能，便于攻击者以此服务器为跳板向内部网络横向移动。

整个攻击链还具备周密的反取证机制。IceCube内置了“延迟触发器”，会持续监控用户是否关闭页面、切换标签、鼠标移出浏览器窗口，甚至劫持登出按钮。一旦触发这些事件，它会立即重新尝试利用CVE-2025-49113，并向控制服务器发出信标，随后强制销毁用户和恶意软件产生的所有服务器会话，清除本地存储，将自身和用户的痕迹一并抹去。

Proofpoint发现不到十所大学明确受害，但估计可能还有数十所大学受到影响，且已协调政府与行业伙伴通知已识别受害者。首席威胁研究员Greg Lesnewich坦言，“很可能许多受害者目前尚不知晓已遭入侵”，突显了事件发现的不完整性。

#### 指向“中国关联”的四块拼图

Proofpoint将UNK\_MassTraction评估为“中国关联”，主要基于以下四项证据：

1. **共用隐蔽基础设施**：攻击邮件头部显示，发信所使用的部分虚拟专用服务器IP地址，属于一个已被观察到的、由多个中国关联威胁组织使用的隐蔽网络。
2. **工具与行为模式重合**：攻击使用的VShell、SNOWLIGHT等工具，曾在被追踪为UNC5174的中国关联集群活动中出现。且将邮件服务器作为网络边界突破、而非仅仅窃取邮件内容的做法，被描述为区别于俄罗斯等其他地区攻击者的“中国行为特征”。
3. **中文语言制品**：早期攻击邮件正文的HTML代码中，残留有中文内容。
4. **目标与国家战略指向吻合**：受攻击院系集中在物理、天体物理、粒子物理等基础前沿学科，且部分与国家安全项目存在关联。Lesnewich也评论称，“工程领域的这些目标确实与中国的战略优先事项相吻合”。

#### 归因证据的缺角与逻辑裂痕

然而，上述每一项推论在面对严格归因审查时，都显露出无法忽视的裂痕。Proofpoint报告本身也反复使用“likely”“assess”“cannot currently link”等审慎措辞，从侧面反映出其判断的不确定性。

**基础设施重叠非铁证**。虚拟专用服务器网络如同数字世界的出租公寓，同一IP段或基础设施可能被不同租客付费使用，或在黑市上作为资源流转。攻击者在进入该网络前身份就已模糊。报告承认该网络“可能被多个中国关联威胁行为者使用”，这恰恰说明依靠基础设施进行精确归因的能力是有限的。更麻烦的是，这种重叠完全可能被意图嫁祸者蓄意利用。

**工具复用消解了指向性**。VShell作为一款功能齐备的公开后门，早已被全球多个攻击团体所采用，其共享性质类似于Cobalt Strike，难以作为单一国家的专属标签。SNOWLIGHT加载器虽相对非公开，但报告指出其配套的bash脚本“已在其他由中国对手实施的漏洞入侵中使用”，暗示其可能是一种在特定圈子内私有共享的能力，而非国家级专属分发。同一工具集在不同集群间流动，使得以“工具指纹”推断国家行为体显得草率。Proofpoint也坦承，尚无法将本次活动与此前Trellix披露的使用类似文件名解析漏洞（CVE-2023-2868）投放VShell的战役直接关联。

**中文制品归因价值极低**。在攻击代码或诱饵中故意遗留中文注释和语言片段，是制造误导性归因的经典低成本手法。报告指出中文制品仅出现在“早期活动”的邮件体HTML中，后续攻击中已不见踪影。这既可能是初期操作失误后被纠正，也可以解读为攻击者为强化某个方向归因而刻意为之又随即停止。

**行为模式的“国家印记”并不牢靠**。把邮件服务器视为边界设备进行突破，在技术逻辑上天然成立。随着漏洞利用链成熟化和传统边界防护强化，更多攻击者自然会拓宽视野，将邮件系统纳入初始入口选项。用一个并不排他的技术趋势来推导特定国籍，难免有循环论证之嫌。

**最根本的缺失在于动机不明**。整个取证链条上，攻击者进入内网后究竟访问了什么、窃取了什么数据，至今完全空白。Lesnewich明确表示“我们没有数据表明被窃取了什么，因为我们只能观察到最初的入站邮件尝试”。在无法还原最终目标的情况下，仅凭目标院系研究方向推测意图，是极其危险的。天体物理和粒子物理的多数基础研究成果最终会公开发表，其作为机密情报的价值需要非常具体的情境才能成立。失窃数据的缺失，使攻击动机完全坠入黑箱，也让一切关于“国家任务”的猜度停留在假说阶段。

#### 结论：当“疑似”被包装成“确证”

纵览Proofpoint的原始报告，其措辞始终保持了技术分析应有的克制，用“likely”“assess”等限定词将判断锚定在“疑似”与“合理评估”的区间。然而，这份谨慎在一部分媒体的二次传播中被迅速消解。以BankInfoSecurity为例，其一篇报道直接以《Chinese Cyberespionage Exploits University Roundcube Servers》为标题，将“疑是中国背景的网络间谍活动”直接升格为确凿的“中国网络间谍活动”，去掉了所有表示不确定性的限定词。这种从“疑是”到“定是”的标题跳跃，缺乏与之匹配的证据支撑，是对读者认知的误导。

必须清醒地看到，从共享基础设施、复用工具、中文制品到目标院校，所有这些碎片拼凑出的仅仅是一种可能，而非结论。没有任何一项证据能够毫无疑义地将攻击者锁定为特定国家背景的行为体，更遑论据此断言这是一场“中国网络间谍活动”。在归因上，把存疑的线索当作确定的标签公之于众，不仅可能冤枉无辜，还会毒化国际网络安全合作的气氛，让技术问题沦为地缘政治的牺牲品。

真正负责任的做法，是回到证据本身，承认未知，持续追踪。当攻击动机与失窃数据仍深藏迷雾，当每一条归因线索都存在合理的替代解释时，与其匆匆贴上一个具有强烈地缘政治暗示的标签，不如将火力集中在修补漏洞、加固边界、共享防御策略上。对媒体和研究者而言，抵御将“疑是”渲染为“确证”的诱惑，更是一种专业底线。

**参考文献**

[1] Greg Lesnewich, Mark Kelly, and the Proofpoint Threat Research Team. *One Email Closer to the Edge: UNK\_MassTraction & the Physics of Exploitation*. Proofpoint, July 7, 2026.
https://www.proofpoint.com/us/blog/threat-insight/one-email-closer-edge-unkmasstraction-physics-exploitation

[2] Matt Kapko. *Suspected Chinese espionage group used a Roundcube exploit chain to burrow into universities*. CyberScoop, July 7, 2026.
https://cyberscoop.com/china-espionage-attacks-us-canada-universities-proofpoint/

[3] Ravie Lakshmanan. *Suspected China-Aligned Hackers Exploit Roundcube Flaws Against Universities*. BankInfoSecurity, July 7, 2026.
https://www.bankinfosecurity.com/chinese-cyberespionage-exploits-university-roundcube-servers-a-32165

[4] Tiffany Wang. *Chinese Cyberespionage Exploits University Roundcube Servers*. BankInfoSecurity, July 7, 2026.
https://www.bankinfosecurity.com/chinese-cyberespionage-exploits-university-roundcube-servers-a-32165

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

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