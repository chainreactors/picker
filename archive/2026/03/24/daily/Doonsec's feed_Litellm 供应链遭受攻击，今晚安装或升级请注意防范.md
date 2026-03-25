---
title: Litellm 供应链遭受攻击，今晚安装或升级请注意防范
url: https://mp.weixin.qq.com/s/aK5j8lBoMGKG622Gwl6klA
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:12:40.710474
---

# Litellm 供应链遭受攻击，今晚安装或升级请注意防范

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PkfClzhSYiczuwB0ibsCK9GvFChbBb8J1L8pvEjiaeIW6VGgg0Jyb7zmwicWvgzRfNZBQYnuBptM1tg6sPOdY9hyQmGJzpgia4U0hc0L1Co9o3sY/0?wx_fmt=jpeg)

# Litellm 供应链遭受攻击，今晚安装或升级请注意防范

SecureNexusLab

![]()

在小说阅读器中沉浸阅读

3 月 24 日，`litellm` 在 PyPI 发布的 1.82.8（后续更新显示 1.82.7 也受影响）被植入恶意载荷。问题的严重性不在“这个包有漏洞”，而在于：它把攻击执行点放在了 Python 启动链路里，天然跨业务代码边界，并且具备凭据窃取、集群横向和持久化能力。

如果你的团队在该时间窗口升级过依赖，或者是被间接依赖带入，请按“已暴露”处理，而不是按“普通回滚”处理。

根据小编实时追踪，北京时间晚上8点，@hnykda在X发布预警，11点30左右，官方已将1.82.7版本移除

---

## 先理解影响面：litellm 为什么值得警惕

litellm 本质上是一个 LLM 访问适配层。它统一了不同模型厂商接口，提供路由、重试、成本统计等能力。对工程团队来说，它常常部署在“AI 网关”位置，总下载量次数4亿次。

![](https://mmbiz.qpic.cn/mmbiz_png/PkfClzhSYicwaWMiakTgjx2TJPNhr0xVczQonibB3dO8dmAxjIxPgsn4L3mVEhaeLKo89BXmyqh1o6jJ1lpNuibHcJ0LrenWuwMUFpuOG6N2s88/640?wx_fmt=png&from=appmsg)

这个位置有两个特征：

* 离核心凭据很近：`.env`、云密钥、数据库连接串往往都在；
* 权限通常不低：能访问内部服务，甚至能触达 K8s 控制面。

所以，一旦这类组件被投毒，事件等级会从“应用 bug”直接上升到“供应链 + 基础设施安全”。

---

## 事件时间线与异常点

根据公开信息，北京时间 2026-03-24 18:52 ，litellm 1.82.8 发布到 PyPI。关键异常：GitHub 仓库没有对应 tag/release，呈现“绕过常规发布流程，直接上传包仓库”的特征。

恶意版本内含 `litellm_init.pth`。`.pth` 文件会在 Python 解释器启动时被处理，这意味着触发条件不是“你是否 import 了某个模块”，而是“这个环境里是否启动了 Python 进程”。

公开样本还暴露了一个实现缺陷：恶意逻辑会递归触发，形成类似 fork bomb 的资源耗尽。这是攻击代码的 bug，但对受害方来说，结果一样糟糕：机器先不稳定，再谈排查。

---

## 攻击链路：三步走

### 1）信息收集（Collection）

目标很明确：把机器上能用的凭据尽可能拿走。包括 SSH 私钥、`.env`、云厂商凭据、K8s 配置、数据库密码、shell 历史等；同时读取环境变量并访问云元数据接口（IMDS/container credentials）。

### 2）数据外传（Exfiltration）

数据会先加密打包（AES-256-CBC + 内置 RSA 公钥封装会话密钥），然后 POST 到 `https://models.litellm.cloud/`。公开分析指出，该域名不属于 litellm 正常基础设施。

### 3）横向移动与持久化（Lateral Movement & Persistence）

若发现 Kubernetes service account token，恶意代码会尝试读取全局 secrets，并在 `kube-system` 创建高权限 `alpine:latest` Pod，挂载宿主机后写入持久化后门：`/root/.config/sysmon/sysmon.py`，再通过 systemd 用户服务维持驻留。

本机也会尝试类似持久化路径。

---

## 工程团队该怎么判断自己是否中招

满足任一条件，就建议按“已暴露”流程走：

* 3 月 24 日及之后安装/升级过 litellm；
* CI/CD 在该时间窗口拉取了新依赖；
* 使用 `uv/pip` 且可能命中缓存 wheel；
* 运行环境中有云凭据、数据库密钥、K8s token。

优先执行的检查动作：

* 版本确认：`pip show litellm`
* 缓存排查：`find ~/.cache/uv -name "litellm_init.pth"`
* 持久化排查：`~/.config/sysmon/sysmon.py`、`~/.config/systemd/user/sysmon.service`
* 集群审计：`kube-system` 内是否存在 `node-setup-*` 可疑 Pod

---

## 应急处置顺序（按优先级）

1. **「先隔离，再分析」**
   把受影响主机/容器从网络和生产链路中摘出来，先止血。
2. **「清除恶意版本与缓存」**
   卸载受影响 litellm，清理缓存（`rm -rf ~/.cache/uv` 或 `pip cache purge`），避免“修完又装回去”。
3. **「排查持久化和横向痕迹」**
   重点看 `sysmon` 路径、`node-setup-*` Pod、异常 secret 读取记录。
4. **「轮换凭据，按最坏情况处理」**
   SSH、云 AK/SK、K8s 配置、数据库密码、`.env` API Key 全部进入轮换清单。
5. **「补齐审计闭环」**
   回放异常出网、密钥调用、集群控制面操作日志，确认影响边界。

一句话：这是“凭据失陷 + 可能入侵”的响应模型，不是“简单版本回滚”的响应模型。

---

## 公开信息入口

* 讨论入口： litellm #24512
* 作者主页： author

公开信息曾出现讨论线程关闭与噪声干扰。对工程团队来说，不要把处置节奏绑定在“舆论定性”上，应该绑定在“证据与资产风险”上。

---

## 这次事件的三个长期教训

1. **「把发布链路异常当成一等告警」**
   比如“PyPI 有新版本，但源码仓库无 tag/release”。这类信号应该触发人工复核，而不是自动放行。
2. **「把依赖治理做成工程能力」**
   固定版本、启用哈希校验、减少在线拉取 latest，把“可复现构建”落到流水线，而不是停在制度。
3. **「把凭据暴露面压到最小」**
   最小权限、短时令牌、分级隔离。供应链攻击不可完全避免，但横向扩散可以被显著限制。

安全不是“绝不出事”，而是“出事时损失可控、恢复可预期”。

这次 litellm 事件，给所有做 AI 基础设施和平台工程的团队都提了个醒：依赖管理，已经是生产安全的一部分。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkLGDzh5WQ5kuYab29V2PteuUrCj2HeRIHibmjQEK7plD7iccC97duj94oGugfkHdQdxcaXtB7w5icmg/0?wx_fmt=png)

SecureNexusLab

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkLGDzh5WQ5kuYab29V2PteuUrCj2HeRIHibmjQEK7plD7iccC97duj94oGugfkHdQdxcaXtB7w5icmg/0?wx_fmt=png)

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