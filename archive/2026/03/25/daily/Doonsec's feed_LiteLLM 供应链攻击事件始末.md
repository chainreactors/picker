---
title: LiteLLM 供应链攻击事件始末
url: https://mp.weixin.qq.com/s/PVPM9ClI4Eb0hBu9zymOfw
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:26:03.297717
---

# LiteLLM 供应链攻击事件始末

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCLVDjQMGhegGpoJuiaTlO9NhBgeOlscOr0DxyY80H948NflFicPwAmzd3r8dlepvttXJawibb1gKsheibD0bJ5T4bplbbvDDbiaH86c/0?wx_fmt=jpeg)

# LiteLLM 供应链攻击事件始末

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器中沉浸阅读

****2026 年 3 月 24 日，AI 开发者们还在敲代码，PyPI 上的 LiteLLM 悄然被“下毒”。 月下载量高达 9700 万次的 Python 开源库 LiteLLM，其 PyPI 仓库在凌晨被恶意篡改，两个受污染版本（1.82.7、1.82.8）悄然上线。短短三小时内，数万个开发环境和企业系统可能暴露在数据泄露风险中。与普通攻击不同，这次事件不是孤立的恶意注入，而是黑客组织 TeamPCP 精心策划的连锁攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCJiatxq9cb5yNG0q4whWCxL3Vxr0pAbibKMF1NC8ZaGpLcT6ryqIF7iap5YygJ0Mh5QbbibWic8cwcBLCeKJPRdZib3bdQZ3IbS4vb5k/640?wx_fmt=png&from=appmsg)

(https://x.com/LiteLLM/status/2036503343510778061)

慢雾(SlowMist) 自主研发的 Web3 威胁情报与动态安全监控工具 MistEye 也在第一时间给相关客户推送了相关威胁情报预警：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCKJ0lJ2TBXx2Tvr345j9q3pV3QSJMJynvIhKibL6QaibsF0zJtic5qvL2Jag24DkogFteRFEn5I5m31XSCY8fqtYGBdcBK86ibP5eU/640?wx_fmt=png&from=appmsg)****

****## 攻击始末

此次 LiteLLM 攻击的源头，并非库本身存在漏洞，而是其 CI/CD 流水线中使用的开源安全扫描器 Trivy 早已被攻破。

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCIqvzgMlatbVFicZxuBz7ibpLN64cqLFphia0qsibuaM7XT29Dsyzlr4DhThSBcrF9epCSzpHpVTomTVHkyqzyo0RdLlZQpG35qgV4/640?wx_fmt=png&from=appmsg)

(https://github.com/BerriAI/litellm/issues/24512)

回溯攻击时间线：

* 3月19日，TeamPCP 篡改了 Trivy 的 GitHub Action  标签，植入恶意代码；

* 3月23日，攻击者入侵 Checkmarx KICS 安全扫描工具，为下一步攻击铺路；

* 3月24日，LiteLLM 的 CI/CD 流水线运行受污染的 Trivy 时，PyPI 发布令牌被窃取，攻击者借此绕过正常发布流程，将两个恶意版本直接推向 PyPI，完成对 AI 核心依赖库的“投毒”。

这场攻击的曝光颇具戏剧性——攻击者原本打算悄无声息潜伏，没想到自己在编写恶意代码时出现了疏漏——1.82.8 版本中植入的 litellm\_init.pth 文件，会在每次 Python 进程启动时自动执行，并通过子进程反复触发自身，直接导致 FutureSearch 工程师的测试机器内存耗尽、崩溃。正是这个意外的漏洞，让这场本可能潜伏数天甚至数周的攻击提前暴露，否则后果不堪设想。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJM2l5ezMianHBT3rPqenibeiaXqPZff4OtvR1rb4HEIpEQqWDw8T1lqRsdTKPGYB42MOFuVAiavTliciarmScXVicE4pRqAp4tr7RlN0/640?wx_fmt=png&from=appmsg)

(https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/)

TeamPCP 为 LiteLLM 设计的恶意代码，采用了分阶段执行的策略，隐蔽性强、破坏范围广，且具备持久化和横向扩散能力，远超普通供应链攻击的危害程度。

第一阶段为信息收集，恶意脚本会系统性扫描受感染主机的所有敏感数据，涵盖范围极广：从开发者的 SSH 私钥、Git 配置、shell 历史记录，到企业的云服务商(AWS/GCP/Azure) 凭证、Kubernetes 配置、数据库密码，甚至包括加密货币钱包文件、助记词等。值得注意的是，LiteLLM 作为统一调用各类大模型 API 的网关，常存储多个模型提供商的密钥，一旦被攻破，相当于直接向攻击者敞开了企业 AI 基础设施的大门。

第二阶段为加密泄露，收集到的所有数据会通过 AES-256-CBC 算法加密，搭配 4096 位 RSA 公钥保护会话密钥，打包成 tar 归档文件后，发送至攻击者控制的虚假域名 models.litellm.cloud——该域名注册于攻击前一天，与 LiteLLM 官方基础设施毫无关联，极具迷惑性。据披露，攻击者已通过此次攻击窃取约 300GB 压缩凭证，涉及 50 万个敏感凭据。

第三阶段为持久化与横向移动，这也是此次攻击最危险的后遗症来源。在本地机器上，恶意代码会在用户目录下创建后门脚本 sysmon.py，并通过 systemd 服务实现自启动，即便卸载 LiteLLM，后门仍可能持续运行；若检测到 Kubernetes 环境，攻击者会利用服务账户令牌，在集群所有节点部署特权 Pod，实现全网扩散，将单一主机的感染转化为整个集群的安全危机。

攻击者还试图通过恶意机器人刷屏、盗用维护者账号关闭 GitHubissue 等方式掩盖攻击痕迹。

## 潜在风险

目前，PyPI 已撤回受感染版本，隔离区也已解除，LiteLLM 维护者正在处理后续事宜，但这场攻击留下的后遗症远未消除，其潜在危害甚至可能在未来数周、数月内逐步显现。

首先是持久化后门的清理难题。由于恶意代码通过 systemd 服务和隐藏目录实现持久化，部分用户可能仅卸载 LiteLLM 就认为风险解除，却不知后门仍在后台收集数据、等待指令。这种“隐性感染”一旦被忽视，可能导致敏感数据持续泄露，给攻击者留下后续渗透的入口。

其次是凭证泄露的连锁反应。此次被窃取的 50 万个凭证，涵盖企业云服务、数据库、CI/CD 流水线等核心场景，这些凭证可能被攻击者用于进一步入侵其他系统，形成“多米诺骨牌效应”。

最后是依赖链的扩散风险。LiteLLM 作为 AI 领域的核心依赖，被 DSPy、MLflow、Open Interpreter 等 2000 多个包引用，许多开发者从未手动安装过 LiteLLM，却因使用其他工具间接引入了恶意版本。这种“无意识感染”的范围极广，且部分老旧容器、未更新的 CI/CD 流水线中，可能仍残留着受污染的依赖，成为长期安全隐患。

LiteLLM 攻击不禁让人联想到[Trust Wallet安全事件](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504059&idx=1&sn=ea64fa6ef53f86b2dd2508d3dfc42f77&scene=21#wechat_redirect)——主流加密货币钱包浏览器扩展 2.68 版本被植入后门，大量用户钱包资金被盗。该事件的核心原因并非第三方包篡改，而是攻击者直接篡改扩展内部代码，利用 PostHog JS 分析平台将用户数据导向恶意服务器。而此次 LiteLLM 攻击中，加密货币钱包文件、助记词同样被纳入窃取范围，且攻击者具备长期潜伏和横向扩散能力，若加密货币开发者、持有者未能及时排查，很可能重蹈覆辙，面临资产被盗的风险。不仅如此，企业若未能及时轮换云凭证、数据库密码，可能导致核心业务数据泄露、系统被接管，造成的经济损失和声誉损害难以估量。

事实上，TeamPCP 组织此前曾公开嘲讽安全厂商“连自己的供应链都保护不了”，并宣称计划长期窃取商业机密，此次 LiteLLM 攻击只是其系统性入侵开源生态的一个环节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCLMLiaVo1MgD4b3kQz8rL6XXwbUG1bcVMyMXu3K3dviacQVVaicOibrwfJoY8KNM6q3Juw7ycBnaPbn0lv81tcVlQRdSf6NTPxVMxs/640?wx_fmt=png&from=appmsg)

这也警示所有开发者和企业，供应链安全已成为不可忽视的核心风险，任何一个环节的疏忽，都可能引发毁灭性后果。

## 应急处置

面对此次攻击及其后遗症，无论是个人开发者还是企业，都需立即采取行动，排查风险、消除隐患，避免损失扩大：

1. 立即排查感染情况：

通过以下命令检查版本，若为1.82.7或 1.82.8，需立即卸载：

pip show litellm

通过以下命令清除包管理器缓存：

rm -rf ~/.cache/uv 或 pip cache purge

2. 全面轮换敏感凭证：假设所有受感染环境的凭证已泄露，立即轮换 SSH 密钥、云服务商凭证、数据库密码、API 密钥等，尤其是加密货币钱包的私钥、助记词，需立即转移资产并更换密钥。

3. 规范依赖管理：长期来看，需锁定依赖版本（建议锁定 LiteLLM 至 1.82.6 及以下安全版本），避免使用未指定版本的依赖；同时加强 CI/CD 流水线安全，排查并更新受污染的安全工具，避免再次被攻击者利用。****

****## 结语

LiteLLM 供应链攻击不仅揭示了开源生态的脆弱，也提醒我们：在 AI 高速发展的今天，核心依赖库的安全直接关系到整个生态稳定。唯有正视供应链安全，及时排查隐患、完善防护体系，才能避免类似的重大损失，守护自身的数据和资产安全。****

**往期回顾**

[SlowMist Agent Security Skill 正式发布，守护 AI Agent 每一道防线](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504542&idx=1&sn=877bb46e71ffb4b97ef69748773ee304&scene=21#wechat_redirect)

[SlowMist × Bitget AI 安全报告：把钱交给“龙虾”等 AI Agent 真的安全吗？](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504477&idx=1&sn=57f7323b9460df2d03b15f39de4e4dd1&scene=21#wechat_redirect)

[活动回顾 | SlowMist KYT 新品亮相，重构合规基座](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504461&idx=1&sn=245db26fb01a7da89e732ef1ca28b422&scene=21#wechat_redirect)

[慢雾报告：合规压力下 VASP 的猫捉老鼠困境](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504454&idx=1&sn=27742de4ac090d63ca765483be9723e3&scene=21#wechat_redirect)

[倒计时 1 天｜慢雾(SlowMist) 链上合规新品发布会即将开启](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504420&idx=1&sn=f62874b1aeec756939b474be4052f11e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbEP8f4tadFenoLauzHpicWdWbVap3aia38LUGPflBho9ibDHXjoG5fecGJSaYa4S4zYdoicXibSmjv9tg/640?wx_fmt=png&from=appmsg)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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