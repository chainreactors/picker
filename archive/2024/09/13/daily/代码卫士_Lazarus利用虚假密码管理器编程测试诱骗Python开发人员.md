---
title: Lazarus利用虚假密码管理器编程测试诱骗Python开发人员
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520782&idx=2&sn=cce5137652ee5a865b8d94f6c0c4d5d5&chksm=ea94a364dde32a72a8de2fb14429c1b6c01c42df715fba83b436d110a9059bcb7aeac6689bc2&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-13
fetch_date: 2025-10-06T18:27:57.784118
---

# Lazarus利用虚假密码管理器编程测试诱骗Python开发人员

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQOpd7wGiaRuOYnMUibGAZpkCloWJHLZ06sX9GB53dyg8IINXtOyb8QGBumXEBN4CjFeicbKPMGX9F2w/0?wx_fmt=jpeg)

# Lazarus利用虚假密码管理器编程测试诱骗Python开发人员

BILL TOULAS

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**朝鲜黑客组织 Lazarus 成员被指假冒招聘人员，通过包括恶意软件的密码管理产品的编程测试项目，钓鱼Python开发人员。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQOpd7wGiaRuOYnMUibGAZpkC1m1XU9s28tELgO855dMKBbxLib3OQeZaibrj8kTvXWvCMKttzWNX9QrQ/640?wx_fmt=png&from=appmsg)

这些攻击是首次在2023年8月检测到的 “VMConnect 活动” 的一部分。威胁行动者们通过上传到 PyPI 仓库的恶意 Python 程序包攻击软件开发人员。

ReversingLabs追踪该活动超过一年，该公司发布报告提到，Lazarus 黑客将恶意编程项目托管在 GitHub 上，受害者查看README 文件，内含如何完成测试的指南。这些指南旨在营造一种专业、合法以及紧急的氛围。

研究人员发现，Lazarus 黑客组织伪装成美国多家大型银行如 Capital One 来吸引求职者，可能还会提供诱人的薪酬包。从其中一名受害者处获得的证据表明，Lazarus 通过 LinkedIn 等接近目标。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQOpd7wGiaRuOYnMUibGAZpkClUxTKysgd4a6sb6lmfxJxS1kECB7BxQV80PmLydDKrtnM9SiaFZq0pQ/640?wx_fmt=png&from=appmsg)

**以找到bug 为诱饵**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQOpd7wGiaRuOYnMUibGAZpkCZxgwgcUqicrF3NIhNtHNYyR7vfPnVzdbicIuDI0Ay3iboSnZNmOcqUfEw/640?wx_fmt=gif&from=appmsg)

黑客要求候选人从一款密码管理器应用中找出一个 bug，提交修复方案并提供截屏进行证明。项目的 README 文件首先要求受害者在系统上运行恶意密码管理器应用 “PasswordManager.py”，接着要求找出错误并修复。该文件触发隐藏在 “pyperclip” 和 “pyrebase” 库的 “\_init\_.py” 文件中的base64混淆模块进行执行。被混淆的字符串是一款恶意软件下载器，它会联系C2服务器并等待命令，另外还具备提取和运行额外 payload 的能力。

为了确保候选人不会检查项目文件中的恶意或混淆代码，README 文件要求快速执行该任务：5分钟内构建项目，15分钟内执行修复方案，以及10分钟内发回最终结果。这样做的目的应该是证明开发人员在Python项目和 GitHub 中的经验，但目标是让受害者跳过任何可能暴露恶意代码的安全检查。

ReversingLabs 发现该攻击活动在7月31日仍然活跃并认为仍在进行。

软件开发人员应警惕从 LinkedIn 用户或别处接受的工作申请邀约是骗局的情况，并应考虑联系人的信息可能是伪造的。在收到任务之前，应尝试验证其他人的身份并和企业确认确实正在招聘人才。花时间扫描或仔细审计所给代码并仅在安全环境如虚拟机或沙箱应用中执行。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[AI Python 包中存在缺陷 “Llama Drama” ，威胁软件供应链](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519566&idx=1&sn=991956bfd062dfe52e9fe722b821d358&chksm=ea94bc24dde335320179ca3ef8f51d217570e92946c74792f58bd0cc3104290b3db59cfa67fc&scene=21#wechat_redirect)

[Python URL 解析漏洞可导致命令执行攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517374&idx=2&sn=6d9a155300780ffb8b966b2bbc21d887&chksm=ea94b5d4dde33cc296b93b32e5cd32ac9615348457175affa0556a82c0a3015f42839582329b&scene=21#wechat_redirect)

[恶意 PyPI 包通过编译后的 Python 代码绕过检测](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516649&idx=4&sn=f367f72fbebdff5d48ad087be1a03b77&chksm=ea94b083dde339955d97f7ee0185de146bffb9aebcd533221e32cc770bb884036c61712f4f08&scene=21#wechat_redirect)

[Python 开发人员提醒：PyPI 木马包假冒流行库发动攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515700&idx=2&sn=28c134528939223ed316b6f5b450dcd6&chksm=ea948f5edde306489a6bb564bbb5995de242208d44ab2dde95fce873e09f15d1fc295584cb61&scene=21#wechat_redirect)

[Python 中存在原型污染漏洞变体](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515248&idx=2&sn=ab4334c673f4692a40a2a921e4c2476c&chksm=ea948d1adde3040cd03302eef42f2439894eec7a3f536e3cc0699148c91f1ba6126e9875a80d&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/fake-password-manager-coding-test-used-to-hack-python-developers/

题图：Pixabay License

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