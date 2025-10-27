---
title: 【安全圈】警惕钓鱼攻击！FortiGuard Labs 曝光 Winos 4.0 恶意软件锁定中国台湾用户
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068200&idx=1&sn=9ba351046d8c985971c6df360ae840ad&chksm=f36e7528c419fc3eed7568cd37861213cd6e41a3675c7439a4efafb027b12f59df6398c81834&scene=58&subscene=0#rd
source: 安全圈
date: 2025-03-01
fetch_date: 2025-10-06T21:59:06.499316
---

# 【安全圈】警惕钓鱼攻击！FortiGuard Labs 曝光 Winos 4.0 恶意软件锁定中国台湾用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgaGvqZHtj96NR30ia8Wib3juUMbILic9NFhQ4Avd2LWYT9dWS55yicpBC9oLukHHg5T1zsEB6mcgsz9Q/0?wx_fmt=jpeg)

# 【安全圈】警惕钓鱼攻击！FortiGuard Labs 曝光 Winos 4.0 恶意软件锁定中国台湾用户

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

Fortinet 旗下的 FortiGuard Labs 近日披露了一项针对台湾企业的新恶意软件活动。在与 Hackread.com 的沟通中，研究人员透露，该活动于 2025 年 1 月被发现，并部署了一个高度先进的恶意软件框架Winos 4.0。这一攻击表现出极高的严重性，采用多阶段感染流程，最终目的是窃取敏感信息以用于未来的恶意活动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgaGvqZHtj96NR30ia8Wib3juxiaBduabicqiargrqTMicU6vN2VIs0985eCbJjha2gSToVJrncIYwdx11Q/640?wx_fmt=png&from=appmsg)

进一步调查显示，该恶意软件专门针对微软 Windows 平台。攻击的初始媒介是一封精心伪造成台湾“国税局”的钓鱼邮件。该邮件声称包含一份即将接受税务检查的公司名单，并敦促收件人将信息转发给财务部门。附件伪装成财政部的官方文件，其中包含用于下一阶段攻击的恶意 DLL 文件。

攻击通过一系列可执行文件（EXE）和动态链接库（DLL）文件展开。ZIP 文件中包含按顺序执行的文件：20250109.exe、ApowerREC.exe 和 lastbld2Base.dll。研究人员在博客中解释道：“20250109.exe 是一个启动程序，原本用于执行 ./app/ProgramFiles 中的实际 ApowerREC.exe。攻击者在 ZIP 文件中创建了相同的文件夹结构，并用一个加载程序替换了 ApowerREC.exe。假冒的 ApowerREC.exe 除了调用从 lastbld2Base.dll 导入的函数外，什么也不做。”

这个 DLL 文件解密并执行包含配置数据（如命令与控制服务器地址）的 shellcode。Shellcode 进一步实现了可选功能，包括权限提升、反沙盒技术（如拍摄多张截图以检测用户活动，在未检测到用户交互时延迟执行）以及隐藏进程窗口。恶意软件从 C2 服务器下载加密的 shellcode 和核心 Winos 4.0 模块，并将这些数据存储在系统注册表中以供后续解密和执行。

该模块启动了多项恶意任务，例如建立持久性、绕过用户账户控制（UAC）、收集系统信息（包括计算机名称、操作系统版本和已安装的防病毒软件），以及禁用受感染系统的屏幕保护和节能功能。此外，该恶意软件还会主动监控和操作用户活动，包括截取屏幕截图、记录键盘输入和剪贴板内容（甚至记录连接的 USB 设备及其插入和移除日志），并根据预定义规则修改剪贴板数据。它还可以禁用安全软件的网络连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgaGvqZHtj96NR30ia8Wib3juFc01fGN73c69qVrAJWkRQtXOuhReuozl8Ag1aCg39yz4s5Wb4GiaKJQ/640?wx_fmt=png&from=appmsg)

研究人员还观察到其他攻击链，涉及 Python 脚本和进一步的 shellcode 注入技术。这些变体展示了 Winos 4.0 框架的灵活性和适应性。保护自己免受 Winos 4.0 等复杂恶意软件的侵害，需要高度警惕未经请求的电子邮件，尤其是包含附件或链接的邮件；避免打开邮件中附带的压缩文件（如 ZIP、RAR），因为它们通常用于传播恶意软件；并启用实时扫描功能，以便在感染系统之前检测并阻止威胁。

专家评论

SlashNext 的现场首席技术官 J. Stephen Kowski 表示：“此次攻击遵循经典的钓鱼模式，但巧妙地利用了对权威机构的信任来引发反应。威胁行为者通过制造紧迫感和好奇心，巧妙地利用人类心理，使收件人更有可能下载恶意内容。”

除了电子邮件安全外，Kowski 还强调了多层次防御方法的重要性。他解释说：“大多数组织现在使用托管文件传输系统，这些系统需要注册和内部批准，同时完全阻止 ZIP 附件的传输。将用户教育与高级威胁检测技术相结合，是阻止复杂社交工程攻击进入收件箱的关键。”

来源：https://hackread.com/hackers-impersonate-taiwans-tax-authority-winos-4-0-malware/

***END***

阅读推荐

[【安全圈】央视揭露电诈新手段：“手机口”成诈骗分子的“隐形传声筒”](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068179&idx=1&sn=e269dac5b42a4c742cb4b652259c209e&scene=21#wechat_redirect)

[【安全圈】瑞典要求加密通信应用部署后门，Signal强烈反对](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068179&idx=2&sn=c968a8cc40580623d340d29c9f094df6&scene=21#wechat_redirect)

[【安全圈】DISA 透露，2024 年的数据泄露影响了超过 330 万人](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068179&idx=3&sn=fa7279a82fe96bdb54c1f935fe561090&scene=21#wechat_redirect)

[【安全圈】CVE-2025-20029：F5 BIG-IP系统发现命令注入漏洞，概念验证已发布](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068179&idx=4&sn=39b4a77aebadbd2051b65b5c2aeac879&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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