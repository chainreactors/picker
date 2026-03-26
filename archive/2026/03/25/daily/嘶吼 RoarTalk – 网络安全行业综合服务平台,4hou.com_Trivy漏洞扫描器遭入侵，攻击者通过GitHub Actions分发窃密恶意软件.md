---
title: Trivy漏洞扫描器遭入侵，攻击者通过GitHub Actions分发窃密恶意软件
url: https://www.4hou.com/posts/9jxz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-03-25
fetch_date: 2026-03-26T04:30:02.141493
---

# Trivy漏洞扫描器遭入侵，攻击者通过GitHub Actions分发窃密恶意软件

Trivy漏洞扫描器遭入侵，攻击者通过GitHub Actions分发窃密恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Trivy漏洞扫描器遭入侵，攻击者通过GitHub Actions分发窃密恶意软件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-03-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8684

收藏

导语：Trivy 0.69.4版本已被植入后门，带有恶意程序的容器镜像与GitHub官方安装包已推送至普通用户端。

漏洞扫描工具Trivy近期遭到名为TeamPCP的威胁组织实施的供应链攻击，该组织通过官方发布渠道与GitHub Actions分发窃密恶意软件。

Trivy是一款主流安全扫描工具，可检测容器、Kubernetes集群环境、代码仓库及云基础设施中存在的安全漏洞、配置错误与泄露密钥。由于该工具被广大开发者与安全团队普遍使用，因此成为攻击者窃取敏感认证凭证的高价值目标。

安全研究员称Trivy 0.69.4版本已被植入后门，带有恶意程序的容器镜像与GitHub官方安装包已推送至普通用户端。

随后，安全厂商Socket及Wiz先后展开深度溯源分析，最终确认本次攻击波及多款GitHub Actions组件，几乎篡改了trivy-action代码仓库内的所有版本标签。

研究人员调查发现，威胁攻击者入侵篡改了Trivy的GitHub构建流程：一方面将GitHub Actions中的入口脚本entrypoint.sh替换为恶意版本，另一方面在Trivy v0.69.4官方发布包中植入木马化可执行程序。上述两类恶意程序均具备窃密功能，可渗透主扫描工具及关联GitHub Actions组件，涵盖trivy-action、setup-trivy等常用工具。

攻击者盗用了一组具备仓库写入权限的泄露凭证，借此权限发布恶意安装包。经查证，这批泄露凭证源自今年3月初的上一轮安全事件，当时凭证已从Trivy运维环境中被窃取，且安全团队未完成彻底溯源封堵。

威胁攻击者在Aqua Security旗下trivy-action代码仓库中，强制推送篡改了76个版本标签中的75个，将所有标签跳转指向恶意代码提交记录。

这直接导致所有外部开发工作流，只要调用受篡改影响的版本标签，便会在执行正规Trivy安全扫描前自动运行恶意代码，极大提升了本次入侵攻击的检测难度。

据Socket安全团队监测报告显示，此次窃密恶意软件会先收集系统侦察数据，再全盘扫描目标设备中各类存储凭证与认证密钥的文件及路径，窃取内容具体包括：

**·**系统侦察数据

主机名、用户身份信息、系统内核信息、网络配置参数、环境变量

**·**安全密钥类

SSH公私密钥及配套配置文件

**·**云与基础设施配置

Git仓库、亚马逊云（AWS）、谷歌云（GCP）、微软Azure云、Kubernetes集群、Docker容器认证凭证

**·**环境配置文件

.env环境变量文件及各类衍生变体文件

**·**数据库凭证

PostgreSQL、MySQL/MariaDB、MongoDB、Redis数据库配置密钥

**·**通用凭证文件

包管理工具、密钥保险箱相关认证令牌

**·**持续集成部署配置

Terraform、Jenkins、GitLab CI等流水线配置文件

**·**其他敏感文件

TLS传输层安全私钥、VPN虚拟专用网络配置、Slack与Discord平台Webhook令牌、终端命令历史记录、/etc/passwd与/etc/shadow系统用户文件、身份认证日志、加密货币钱包数据

![图片15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260324/1774338292545966.png "1774336325164104.png")

信息窃取程序正在收集凭据、SSH密钥和环境文件

该恶意脚本还会扫描GitHub Actions运行进程的内存区域，精准匹配特定JSON格式密钥字符串，“

```
 :{ value: , isSecret:true}
```

”，而在开发者本地设备中，植入木马的Trivy可执行程序会执行同类窃密操作：采集系统环境变量、扫描本地文件窃取密钥、枚举读取全网网卡接口信息。

所有窃取到的敏感数据会先被加密打包为tpcp.tar.gz压缩文件，随后外传至仿冒域名指挥控制服务器scan.aquasecurtiy[.]org。

若数据外传失败，恶意软件会在受害者GitHub账号内新建名为tpcp-docs的公开仓库，将窃取数据强制上传留存。

为实现恶意程序持久驻留，该软件还会在目标设备路径~/.config/systemd/user/下投放Python恶意载荷文件sysmon.py，并注册为系统常驻服务。该载荷会持续轮询远程服务器，按需下载投放更多恶意程序，确保攻击者长期稳定控制入侵设备。

安全判定本次攻击与TeamPCP威胁组织有关，核心证据为攻击所用窃密载荷的Python脚本末尾，存在“TeamPCP云窃密程序”专属注释标识。

这款恶意窃密程序在内置文件密钥采集模块的Python脚本最后一行，主动标注了TeamPCP云窃密程序身份。TeamPCP组织也被追踪命名为DeadCatx3、PCPcat及ShellForce，是业内已收录的云原生定向威胁组织，惯于利用配置错误的Docker应用程序接口、Kubernetes集群、Ray监控面板及Redis服务器发起入侵攻击。

![图片16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260324/1774338298646369.png "1774336352511984.png")

评论显示该脚本名为TeamPCP Cloud Stealer

Trivy所属厂商Aqua Security已正式确认本次安全事件，称攻击者盗用了上一轮未彻底封堵泄露事件中的残留凭证。据了解，当时虽批量轮换重置了密钥与令牌，但重置操作并非原子一次性完成，攻击者大概率同步窃取了更新后的全新令牌。”

本次恶意篡改的Trivy v0.69.4版本在线存活时长约3小时，而遭篡改的GitHub Actions版本标签有效恶意运行时长最长达12小时。

攻击者还恶意篡改删除了项目官方仓库，所有在事件存续期间使用过受篡改版本的企业机构，需判定自身运维环境是否已完全失陷。

应急处置需全面批量轮换所有密钥凭证，涵盖云平台凭证、SSH密钥、应用程序接口令牌、数据库密码等核心数据，同时全盘深度扫描设备系统，排查是否存在其他潜伏入侵后门。

**衍生后续攻击：新型蠕虫CanisterWorm通过npm供应链扩散**

安全研究员还确认同一TeamPCP威胁组织发起衍生后续攻击，投放一款名为“CanisterWorm”的新型自主扩散蠕虫程序，定向入侵npm开源包生态。

该蠕虫程序可恶意篡改开源包、通过系统常驻服务植入持久后门，随后盗用窃取到的npm认证令牌，向其他开源包推送恶意更新版本实现全域扩散。

这款自主扩散蠕虫通过deploy.js脚本盗取npm令牌、解析用户账号、枚举所有可发布开源包、自动迭代补丁版本号，最终批量全域投放恶意载荷，最快60秒内可入侵28个开源包。”

该恶意软件采用去中心化指挥控制机制，依托互联网计算机（ICP）智能容器构建数据中转节点，为恶意程序提供后续载荷下载地址解析服务。

借助ICP智能容器特性，本次攻击极难被溯源关停，仅容器管控者有权限删除节点，若要全网阻断攻击，必须发起治理提案并完成全网节点投票审批。

蠕虫程序同时具备密钥采集能力，可从配置文件与环境变量中窃取npm认证令牌，进而快速渗透扩散至开发者本地环境与持续集成部署流水线。

目前，部分二级恶意载荷基础设施已停止活跃或配置无害内容，但研究员表示，攻击者可随时修改配置重启高危攻击，所以人们仍需时刻保持警惕。

文章来源自：https://www.bleepingcomputer.com/news/security/trivy-vulnerability-scanner-breach-pushed-infostealer-via-github-actions/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?OPaddB5j)

#### 你可能感兴趣的

* [![]()

  AI时代中国网络安全产业的五年变局|| 影子AI之困：企业数据安全最大的灰犀牛](https://www.4hou.com/posts/vwXn)
* [![]()

  嘶吼安全动态｜工信部征求AI安全治理标准，规范模型上下文协议安全 浙江警方破获特大电商数据泄露案，200万条订单信息被贩卖](https://www.4hou.com/posts/rpQL)
* [![]()

  从假新闻刷屏看清“认知安全”：AI时代网络安全的新边疆](https://www.4hou.com/posts/nlMp)
* [![]()

  Trivy漏洞扫描器遭入侵，攻击者通过GitHub Actions分发窃密恶意软件](https://www.4hou.com/posts/9jxz)
* [![]()

  嘶吼安全动态｜国家数据局：我国AI日均Token调用量破140万亿 LiteLLM遭供应链投毒，数千企业面临数据泄露风险](https://www.4hou.com/posts/mkL3)
* [![]()

  新型网络攻击InstallFix曝光：伪装CLI工具安装指令，诱导执行恶意命令](https://www.4hou.com/posts/2X6A)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [AI时代中国网络安全产业的五年变局|| 影子AI之困：企业数据安全最大的灰犀牛](https://www.4hou.com/posts/vwXn)
  2026-03-26 12:00:00
* [嘶吼安全动态｜工信部征求AI安全治理标准，规范模型上下文协议安全 浙江警方破获特大电商数据泄露案，200万条订单信息被贩卖](https://www.4hou.com/posts/rpQL)
  2026-03-26 11:59:00
* [从假新闻刷屏看清“认知安全”：AI时代网络安全的新边疆](https://www.4hou.com/posts/nlMp)
  2026-03-25 12:01:00
* [Trivy漏洞扫描器遭入侵，攻击者通过GitHub Actions分发窃密恶意软件](https://www.4hou.com/posts/9jxz)
  2026-03-25 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [AI时代中国网络安全产业的五年变局|| 影子AI之困：企业数据安全最大的灰犀牛](https://www.4hou.com/posts/vwXn)

  山卡拉
* [嘶吼安全动态｜工信部征求AI安全治理标准，规范模型上下文协议安全 浙江警方破获特大电商数据泄露案，200万条订单信息被贩卖](https://www.4hou.com/posts/rpQL)

  胡金鱼
* [从假新闻刷屏看清“认知安全”：AI时代网络安全的新边疆](https://www.4hou.com/posts/nlMp)

  山卡拉
* [Trivy漏洞扫描器遭入侵，攻击者通过GitHub Actions分发窃密恶意软件](https://www.4hou.com/posts/9jxz)

  胡金鱼
* [嘶吼安全动态｜国家数据局：我国AI日均Token调用量破140万亿 LiteLLM遭供应链投毒，数千企业面临数据泄露风险](https://www.4hou.com/posts/mkL3)

  胡金鱼
* [新型网络攻击InstallFix曝光：伪装CLI工具安装指令，诱导执行恶意命令](https://www.4hou.com/posts/2X6A)

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