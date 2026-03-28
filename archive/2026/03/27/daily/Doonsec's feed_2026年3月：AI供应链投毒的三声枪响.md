---
title: 2026年3月：AI供应链投毒的三声枪响
url: https://mp.weixin.qq.com/s/Fukn4IgCgJv9ZEIBb7kRuA
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:16:08.493522
---

# 2026年3月：AI供应链投毒的三声枪响

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZVYP60vud5PJnHFWjfqIFb3BxL9ILibvapib8SgvpGUnlNgxbCEtoNDYXtwtrJGsX8B58Th8btjWooOCCdphiccqictQ1ia4I5wcGy4CQLibvrAvA/0?wx_fmt=jpeg)

# 2026年3月：AI供应链投毒的三声枪响

原创

AI小智
AI小智

零知实验室

![]()

在小说阅读器中沉浸阅读

> 半个月内，三个主流AI开发工具相继被投毒。攻击者不是靠什么高深漏洞，而是摸准了开发者对工具的信任。三件事加在一起，构成了2026年至今最值得警惕的一次网络安全事件。

---

### 一、三起事件，一个攻击者

2026年3月，AI开发者工具链遭遇了一场"立体化打击"。

**3月19日**，开源漏洞扫描工具 Trivy 被攻破，PyPI发布令牌被盗。

**3月25日**，月下载量9700万次的 Python 库 **LiteLLM**（版本1.82.7、1.82.8）被篡改上架PyPI。

**3月**，API协作平台 **Apifox** 的CDN脚本被植入恶意代码，全平台桌面客户端受影响。

**3月**，AI文档服务 **Context Hub** 被发现存在PR投毒漏洞，可诱导AI编码代理引入恶意依赖。

安全研究人员追查发现，这几条攻击背后站着同一个团伙：**TeamPCP**。

LiteLLM的令牌，正是从Trivy被攻破后窃取的——先打扫描工具，再用窃来的令牌渗透核心依赖库，这是当前供应链攻击最危险的范式之一。

---

### 二、三个攻击面，各有各的致命之处

**Apifox：CDN劫持 + Electron沙箱缺失**

Apifox桌面端基于Electron开发，但未严格启用sandbox参数，导致渲染进程内的JavaScript可以直接调用Node.js API——读文件、执行命令、访问网络，权限等同本地应用。

攻击者篡改了CDN上的一段行为统计脚本，正常版本约34KB，被注入后变成77KB。多出的43KB代码会从仿冒域名 `apifox.it.com` 加载第二阶段载荷，窃取SSH密钥、Git凭证、Shell历史等敏感数据。

**LiteLLM：PyPI包篡改 + .pth机制静默触发**

恶意代码注入在 `litellm/proxy/proxy_server.py`，通过 `.pth` 文件实现自动执行——用户只要 `pip install litellm==1.82.8`，就自动中招，无需任何主动调用。

LiteLLM的危害是三起事件中最深的：

* 系统性扫描SSH密钥、云凭证（AWS/GCP/Azure）、K8s Secrets、加密货币钱包、CI/CD令牌
* 在Kubernetes集群中横向移动，每个节点部署特权Pod
* 安装systemd后门，伪装成"系统遥测服务"长期潜伏
* 数据加密外传至 `models.litellm.cloud`

有意思的是，这次攻击最终被安全研究员发现，原因是**攻击者自己写了个Bug**——恶意代码包含一个未处理好的Fork Bomb，在某些执行路径下导致系统内存爆满，反而暴露了行踪。

**Context Hub：文档PR投毒 + 间接提示注入**

与前两起不同，Context Hub的攻击不需要入侵任何系统代码。

攻击者只需向Context Hub的GitHub仓库提交一个包含恶意内容的文档PR——比如在Plaid或Stripe的API文档里夹带虚假的PyPI包名。

当AI编码代理读取这些文档时，会把虚假依赖写入项目的 `requirements.txt`。不需要任何恶意软件，AI模型自己把攻击代码"写"进了代码库。

研究人员的测试显示，Haiku模型在40次测试中**全部中招**，直接写入恶意依赖；Sonnet模型有53%的概率写入；Opus模型的防御效果最好，75%概率发出警告。

---

### 三、为什么开发者成了最值钱的攻击目标

2026年3·15晚会曝光了AI大模型"投毒"黑灰产——攻击者通过人为制造虚假共识操控AI学习。但那只是问题的一面。

另一面是：开发者手里的东西太值钱了。

SSH密钥 → 生产服务器 Git Token → 代码仓库 云凭证 → 企业基础设施 K8s Secret → 整个容器集群

攻破一个开发者的笔记本，等于拿到半张企业内网的入场券。

而供应链投毒的特殊之处在于：**不需要正面攻击任何人**。只需要在开发者每天都会打开的工具里，悄悄塞一段代码。

你用的是正版软件，你没有点任何可疑链接，你的防火墙正常工作——但你的凭证已经在别人服务器上了。

---

### 四、目前的局势

2026年开年以来，供应链攻击的频率和复杂度都在上升：

* **包管理器**（PyPI、npm）持续成为靶心，Typo Squatting、令牌窃取、版本篡改手段多样
* **开发者工具**（Trivy、Apifox、LiteLLM）被用作跳板，因为这些工具本身拥有高权限
* **AI代理**（Context Hub模式）成为新型攻击面，攻击者开始利用AI对文档的信任间接渗透代码库
* **GitHub Actions** 也未能幸免——CVE-2026-31976披露，攻击者可利用Action标签投毒劫持CI Runner

开源生态的信任传递链，正在被系统性利用。每一次 `pip install` 和 `npm install` 的背后，是对整条供应链的隐式信任——而这条链上的每一个薄弱点，都可能成为攻击者的入口。

---

### 五、处置清单

**LiteLLM（立即）**

```
pip show litellm
# 若版本为 1.82.7 或 1.82.8：
pip uninstall litellm
pip install litellm==1.82.6
pip cache purge
```

检查 `~/.config/sysmon/sysmon.py` 是否存在，检查K8s集群异常Pod。

**Apifox（立即）**

更新至最新版（2.8.22-alpha.1已将脚本内置），排查对 `apifox.it.com`、`cdn.openroute.dev` 等域名的出站连接。

**Context Hub（预防）**

审查项目中的依赖来源，特别关注AI代理生成的 `requirements.txt`、`package.json` 等配置文件。

**通用（立即）**

* 封锁IoC域名：`models.litellm.cloud`、`checkmarx.zone`、`apifox.it.com`
* 轮换所有SSH密钥、云凭证、API Key
* 检查CI/CD流程中第三方工具的权限配置
* 对AI代理生成的代码实施强制人工审核

---

### 六、写在最后

2026年这波投毒事件，最让人不安的不是某一款工具被攻破，而是攻击者展现出的**系统性思路**——

从漏洞扫描工具（Trivy）切入，窃取令牌，渗透核心依赖库（LiteLLM），再用窃来的凭证控制开发者的终端（Apifox），最后连AI代理的文档流也不放过（Context Hub）。

整条链路覆盖了CDN、PyPI、GitHub PR三个不同平台，涉及三种完全不同的攻击手法，却出自同一伙人。

这不是偶发事件，是有组织、有规划的供应链战役。

对开发者而言，这意味着：**你信任的工具越多，攻击面就越大**。

每引入一个新依赖，都要问自己三个问题：它从哪里来？谁在维护？装上之后，它能访问我机器上的什么？

这些问题，以前只有安全团队会想。现在，每个写代码的人都应该想。

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZVYP60vud5N1yD1WgdHm2D8koFa6Qm87eZVxluosiaFakickibH5ic5pI9Sm6VYH7SQVXEJ3xOMJsNPGWxAXvGrxxiaAAb5hVhuYY8SmuITelsmc/0?wx_fmt=png)

零知实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZVYP60vud5N1yD1WgdHm2D8koFa6Qm87eZVxluosiaFakickibH5ic5pI9Sm6VYH7SQVXEJ3xOMJsNPGWxAXvGrxxiaAAb5hVhuYY8SmuITelsmc/0?wx_fmt=png)

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