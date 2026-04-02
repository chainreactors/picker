---
title: Trivy 供应链攻击持续扩散，波及Docker镜像与GitHub代码仓库
url: https://www.4hou.com/posts/gyBj
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-04-01
fetch_date: 2026-04-02T04:29:23.685372
---

# Trivy 供应链攻击持续扩散，波及Docker镜像与GitHub代码仓库

Trivy 供应链攻击持续扩散，波及Docker镜像与GitHub代码仓库 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Trivy 供应链攻击持续扩散，波及Docker镜像与GitHub代码仓库

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-04-01 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)12906

收藏

导语：供应链安全防护厂商Socket发布专项报告，正式确认Docker Hub官方镜像仓库已出现恶意篡改的Trivy污染制品包。

发动Trivy供应链攻击的TeamPCP黑客组织持续锁定Aqua Security（ Trivy所属厂商）发起精准打击：恶意推送伪装Docker镜像、劫持企业GitHub组织账号，批量篡改数十个开源代码仓库。

本次连环入侵仍是此前高危供应链投毒事件：攻击者非法攻陷Aqua Security旗下安全扫描工具Trivy的GitHub自动化构建流水线，植入窃密后门恶意软件，攻击期间攻击链条进一步扩散污染至Docker Hub官方镜像仓库。

Trivy作为全球顶流开源安全检测工具，GitHub平台累计星标超33800颗，广泛用于精准扫描各类软件制品、底层基础设施中潜藏漏洞、高危配置错误、泄露密钥凭证，覆盖企业全链路安全防线。

Socket发布专项报告，正式确认Docker Hub官方镜像仓库已出现恶意篡改的Trivy污染制品包。

Socket安全研究员证实：“攻击者违规强行推送伪装镜像标签0.69.5与0.69.6版本，但GitHub平台无对应官方合规发布记录及版本标签备案。”深度分析判定，两款恶意镜像均携带专属入侵指纹特征，与TeamPCP攻陷Aqua Security GitHub组织后投放的云窃密后门恶意软件完全同源复用。

Trivy官方最终合规稳定版锁定为0.69.3版本，尽管暂未捕获旧版镜像、编译程序发布后遭二次篡改痕迹，但Docker Hub镜像版本标签不具备永久不可篡改属性，企业不能单纯依赖标签名称判定程序安全完整性。

**攻陷劫持Aqua Security GitHub核心组织账号**

Aqua Security官方通报结论：本次二次入侵核心诱因，系月初针对同款Trivy工具首轮泄露事件的溯源封堵、安全加固工作存在重大疏漏短板，未能彻底阻断攻击者权限链路。坦言：“我们虽批量紧急轮换重置全域密钥、身份令牌，但重置操作非原子一次性闭环执行，攻击者大概率同步窃取复刻更新后的全新合法令牌凭证。”

漏洞权限复用直接纵容攻击者向Trivy主程序底层植入TeamPCP专属云窃密后门代码，批量推送伪装篡改高危恶意版本。

应急响应层面，Aqua Security已于3月20日紧急发布全新安全纯净版Trivy安装包，同步联合专业应急溯源厂商Sygnia，深度介入漏洞修复、全链路取证调查闭环处置。

然而不久后官方紧急更新预警公告：3月22日后台监控捕获大量异常高危操作行为，判定同一TeamPCP攻击者已再次非法越权登录，违规篡改大量核心代码仓库配置、恶意删除篡改历史记录。

厂商补充说明：截至当前最新节点，Trivy开源主程序暂未遭受本轮二次恶意篡改波及。

开源恶意情报社区平台OpenSourceMalware深度拆解：TeamPCP精准攻陷Aqua Security专属私有代码托管组织账号aquasec-com，该账号独立隔离于公开开源仓库组织aquasecurity，核心承载企业闭源私有商业代码资产。

黑客全程依托自动化恶意脚本批量执行操作，耗时仅约两分钟：为组织内全部44个私有代码仓库统一强制添加tpcp-docs-前缀命名，批量篡改仓库简介公示嘲讽标语“TeamPCP掌控Aqua Security全域权限”。

攻击者核心入侵突破口为非法攻陷服务账号Argon-DevOps-Mgt，该账号默认配置全域最高权限，同步打通Aqua Security公开、私有两大GitHub组织后台管理权限。

OpenSourceMalware披露高危配置漏洞：目标攻陷服务账号依托普通用户个人访问令牌（PAT）完成身份鉴权登录，而非合规安全标准的GitHub应用授权鉴权模式。

致命安全短板凸显：个人访问令牌鉴权机制等同于静态明文密码，有效期远超GitHub应用临时动态令牌；且服务账号默认承载自动化后台调度任务，常规未启用双重多因素认证（MFA）防护，极易被窃取复用。

为精准验证攻陷账号是否具备两大GitHub组织全域管理员权限，TeamPCP恶意创建临时分支update-plugin-links-v0.218.2，推送至公开仓库aquasecurity/trivy-plugin-aqua，随即精准毫秒级一键删除无痕销毁痕迹。

锁定窃取链路：黑客依托自研TeamPCP云窃密后门，非法采集窃取该Argon-DevOps-Mgt服务账号个人访问令牌，恶意软件可精准从持续集成调度运行环境中批量窃取GitHub令牌、SSH密钥、云平台凭证、系统环境变量等高敏数据。

OpenSourceMalware对此解释：“该服务账号常态调度触发trivy-plugin-aqua流水线自动化任务，鉴权令牌长期明文驻留运行环境，极易被恶意软件一键批量采集窃取。”

目前，OpenSourceMalware已公开全套专属入侵妥协指纹特征库，助力企业安全运维人员快速自查研判，排查本机环境、业务链路是否已深陷本次高危供应链投毒入侵。

Aqua Security官方声明：暂未捕获任何证据证实企业商业付费产品内置Trivy检测引擎遭受篡改波及。

文章来源自：https://www.bleepingcomputer.com/news/security/trivy-supply-chain-attack-spreads-to-docker-github-repos/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?02ChEY6D)

#### 你可能感兴趣的

* [![]()

  嘶吼安全动态｜国家市场监管总局推动网络食品安全“协同共治”，AI算法参与合规审核 加密平台Drift发生重大安全事故](https://www.4hou.com/posts/xyOl)
* [![]()

  嘶吼安全动态｜国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用 OpenAI Codex爆出严重漏洞：黑客可劫持GitHub访问令牌](https://www.4hou.com/posts/qow7)
* [![]()

  Trivy 供应链攻击持续扩散，波及Docker镜像与GitHub代码仓库](https://www.4hou.com/posts/gyBj)
* [![]()

  嘶吼安全动态｜全国网安标委发布关于征集个人信息保护标准应用实践案例的通知 AI工作流工具Langflow曝未授权RCE漏洞](https://www.4hou.com/posts/l0Kj)
* [![]()

  攻击者滥用.arpa 特殊域名与IPv6反向DNS实施钓鱼攻击](https://www.4hou.com/posts/Zg5g)
* [![]()

  嘶吼安全动态｜国家安全部：搜索引擎排名遭 “投毒”，恶意链接暗藏窃取风险 谷歌发布高风险Chrome安全更新](https://www.4hou.com/posts/kgJJ)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [嘶吼安全动态｜国家市场监管总局推动网络食品安全“协同共治”，AI算法参与合规审核 加密平台Drift发生重大安全事故](https://www.4hou.com/posts/xyOl)
  2026-04-02 12:00:00
* [嘶吼安全动态｜国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用 OpenAI Codex爆出严重漏洞：黑客可劫持GitHub访问令牌](https://www.4hou.com/posts/qow7)
  2026-04-01 14:34:55
* [Trivy 供应链攻击持续扩散，波及Docker镜像与GitHub代码仓库](https://www.4hou.com/posts/gyBj)
  2026-04-01 12:00:00
* [嘶吼安全动态｜全国网安标委发布关于征集个人信息保护标准应用实践案例的通知 AI工作流工具Langflow曝未授权RCE漏洞](https://www.4hou.com/posts/l0Kj)
  2026-03-31 11:59:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [嘶吼安全动态｜国家市场监管总局推动网络食品安全“协同共治”，AI算法参与合规审核 加密平台Drift发生重大安全事故](https://www.4hou.com/posts/xyOl)

  胡金鱼
* [嘶吼安全动态｜国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用 OpenAI Codex爆出严重漏洞：黑客可劫持GitHub访问令牌](https://www.4hou.com/posts/qow7)

  胡金鱼
* [Trivy 供应链攻击持续扩散，波及Docker镜像与GitHub代码仓库](https://www.4hou.com/posts/gyBj)

  胡金鱼
* [嘶吼安全动态｜全国网安标委发布关于征集个人信息保护标准应用实践案例的通知 AI工作流工具Langflow曝未授权RCE漏洞](https://www.4hou.com/posts/l0Kj)

  胡金鱼
* [攻击者滥用.arpa 特殊域名与IPv6反向DNS实施钓鱼攻击](https://www.4hou.com/posts/Zg5g)

  胡金鱼
* [嘶吼安全动态｜国家安全部：搜索引擎排名遭 “投毒”，恶意链接暗藏窃取风险 谷歌发布高风险Chrome安全更新](https://www.4hou.com/posts/kgJJ)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)