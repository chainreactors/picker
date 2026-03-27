---
title: LiteLLM供应链投毒事件分析
url: https://mp.weixin.qq.com/s/YkSMlgKa8FdfQ7EWxyVH1g
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:30:20.770735
---

# LiteLLM供应链投毒事件分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZVYP60vud5O48fkKJks7mseJDohpObneR6NnogYicwjyKpohQ3yT0844LeUOum4CSiayJ0n4tzGibWxoibYQMRDxU2RINjMsiayAePhhQ1P1a1xY/0?wx_fmt=jpeg)

# LiteLLM供应链投毒事件分析

原创

AI小智
AI小智

零知实验室

![]()

在小说阅读器中沉浸阅读

# LiteLLM供应链投毒事件分析

> 2026年3月25日，AI开发者圈经历了一场教科书级的供应链攻击。GitHub超4万星、月下载量接近1亿次的Python库LiteLLM，在PyPI上被植入恶意代码。 本文基于BleepingComputer、FutureSearch、Endor Labs等安全研究机构公开报告整理。

---

### 一、事件背景

LiteLLM是AI开发领域最流行的工具之一——它用一个统一接口同时接入OpenAI、Anthropic、GCP、Azure等100+大模型API，月安装量达9700万次。

DSPy、MLflow、Open Interpreter等2000多个AI开源项目都依赖它。

2026年3月25日，PyPI上两个版本被确认遭到篡改：**1.82.7** 和 **1.82.8**。

**Karpathy**（OpenAI联合创始人、知名AI科学家）当天公开发推预警，事件迅速引发全球开发者社区响应。

---

### 二、攻击链：Trivy → LiteLLM

这并不是一次孤立的攻击。

安全研究人员追溯发现，TeamPCP的攻击布局早在**3月19日**就已启动——他们先对开源漏洞扫描工具**Trivy**发起供应链攻击，窃取了LiteLLM的PyPI发布令牌。

有了这个令牌，无需入侵LiteLLM本身代码库，直接绕过代码审核向PyPI上传恶意版本。

```
Trivy供应链攻击（3月19日）
    ↓ 窃取PyPI发布令牌
LiteLLM投毒（3月25日）
    ↓ 上传恶意版本1.82.7 / 1.82.8
每日340万次下载受影响
```

**干净版本：1.82.6**（已于PyPI下架恶意版本）

---

### 三、技术分析：三阶段完整攻击链

#### 阶段一：植入与触发

恶意代码注入在 `litellm/proxy/proxy_server.py`，以Base64编码Payload形式藏在导入逻辑中。

触发机制通过 `.pth` 文件（Python启动文件）实现——**用户只要`pip install`安装，即中招**，无需主动调用任何函数。

#### 阶段二：信息搜刮

恶意代码会系统性扫描主机敏感数据：

* SSH私钥及配置（`~/.ssh/`）
* Git凭证（`.gitconfig`）
* 云服务商密钥（AWS / GCP / Azure）
* Kubernetes集群凭证
* 环境变量（含所有API Key）
* Shell历史记录（`.bash_history` / `.zsh_history`）
* SSL私钥、数据库密码
* 加密货币钱包文件
* CI/CD平台令牌

同时还会查询云平台元数据端点（AWS IMDS等），窃取云资源访问权限。

#### 阶段三：持久化与横向移动

**本地持久化**（仅1.82.8版本）：

* 创建 `~/.config/sysmon/sysmon.py` 后门脚本
* 配置systemd用户服务，伪装为"系统遥测服务"
* 开机自启动，定期从C2服务器下载额外Payload

**横向移动**：

* 读取Kubernetes Secret，在每个节点部署特权Pod（`alpine:latest`镜像）
* 实现对整个容器集群的持久控制

**数据外传**：

* 收集数据打包为 `tpcp.tar.gz`
* 使用AES-256-CBC加密，RSA-4096公钥封装会话密钥
* POST请求发送至 `models.litellm.cloud`

---

### 四、IoC指标

| 类型 | 指标 | 说明 |
| --- | --- | --- |
| C2域名 | `models.litellm.cloud` | 数据外传目标服务器 |
| C2域名 | `checkmarx.zone` | 后门Payload下载域名 |
| 持久化路径 | `~/.config/sysmon/sysmon.py` | 后门脚本路径 |
| 临时文件 | `/tmp/pglog` 、`/tmp/.pg_state` | 攻击者状态文件 |
| 恶意版本 | `1.82.7` 、`1.82.8` | PyPI已下架 |
| 干净版本 | `1.82.6` | 建议降级至此 |

---

### 五、攻击暴露原因

这次攻击最终被暴露，并非安全人员主动发现，而是**攻击者自己出了Bug**。

恶意代码中包含一个未正确处理的Fork Bomb（进程分叉炸弹）——在某些执行路径下会无限fork新进程，导致系统内存耗尽，引发开发者注意。

安全研究员Callum McMahon正是通过这个异常进程行为，顺藤摸瓜发现了完整的攻击链。

Karpathy评价：**若非这个Bug，攻击可能长期潜伏不被发现。**

---

### 六、处置建议

**立即执行**

```
pip show litellm
```

若版本为 1.82.7 或 1.82.8，立即执行：

```
pip uninstall litellm
pip install litellm==1.82.6
pip cache purge   # 或 rm -rf ~/.cache/uv
```

**排查清单**

* 检查是否存在 `~/.config/sysmon/sysmon.py`
* 检查systemd用户服务列表
* 检查Kubernetes集群中kube-system命名空间的异常Pod
* 排查对 `models.litellm.cloud` 和 `checkmarx.zone` 的出站连接

**阻断措施**

在防火墙/DNS层封锁IoC中的两个恶意域名。

**凭证轮换**

若确认受影响，视为**全盘泄露处理**：轮换所有SSH密钥、云凭证、API Key、数据库密码、Kubernetes Secret。

---

### 七、同一攻击者：TeamPCP

LiteLLM并非TeamPCP的唯一目标。

据安全研究人员分析，该组织近期还针对Trivy、Aqua Security等多个开源安全工具发起供应链攻击——

**先攻漏洞扫描工具 → 再用窃取的令牌渗透依赖它的核心库**——这是当前供应链攻击最危险的范式。

开源生态的信任传递链，正在被系统性利用。

---

*信息来源：BleepingComputer、FutureSearch、Endor Labs、Karpathy公开推文。如需官方说明，请访问BerriAI/litellm GitHub仓库。*

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