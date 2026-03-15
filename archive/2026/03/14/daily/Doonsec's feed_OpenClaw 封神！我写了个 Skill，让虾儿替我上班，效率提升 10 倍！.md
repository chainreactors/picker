---
title: OpenClaw 封神！我写了个 Skill，让虾儿替我上班，效率提升 10 倍！
url: https://mp.weixin.qq.com/s/g0eyDFDtYiMKNffke5UakQ
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:28:23.417657
---

# OpenClaw 封神！我写了个 Skill，让虾儿替我上班，效率提升 10 倍！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eep7PCRAQEQOqZHAMUnmt5lBfWRvTnLHyZEqAKSqovm5tjmmYTl5AMicuEZ6cu7wFFZz8G8X884hfh7fuE8mA8XMMAQjXlg7PEgTDKjMibia9o/0?wx_fmt=jpeg)

# OpenClaw 封神！我写了个 Skill，让虾儿替我上班，效率提升 10 倍！

原创

俗说君
俗说君

沐昊安全

![]()

在小说阅读器中沉浸阅读

> 不用手动改一行代码，100 个 POC 半小时搞定，再也不用当 “格式搬运工”！

# ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eep7PCRAQERezfe5w8iaqibn7bAb3qsgiaY4GuTibTySpbS77uPqV42MJJnNvIuibib2qCPJtHgQf0KyHpr17G9wFZeeOf59Pcm8w1mS0149kv904/640?wx_fmt=jpeg&from=appmsg)

# 前言：谁懂啊！批量改 POC 真的会谢

最近 OpenClaw 小龙虾火到出圈，连带 Skill 机制也被大家疯传。作为早早就玩过 Skill 的 “老人”（见文章：[Skill赋能代码审计初探](https://mp.weixin.qq.com/s?__biz=MzU4MjkwNTUwOA==&mid=2247484323&idx=1&sn=899616b0a5e5bedd39b6917291dedbb7&scene=21#wechat_redirect)），这阵子被一个需求整破防了 —— 公司要把几百个零散的 POC 脚本、漏洞复现流程，全部改成内部统一的 pocscan 框架格式。纯手写改就算了，还要逐行对齐类结构、补 meta 字段、调函数命名、删冗余代码… 改到第 5 个就想辞职！

直到我突然想起：OpenClaw 不是能装 “技能包” 吗？为什么不调教它来干这破活？

于是花了半天时间写了个 Skill，从此批量转 POC 再也不用手动肝 ——**小龙虾 24 小时待命，输入原始 POC，自动输出符合公司框架的成品脚本，准确率 100%，效率直接翻 10 倍！**

| 手动转换 | 小龙虾自动转换 |
| --- | --- |
| 1个/10分钟 | 100个/30分钟 |
| 易漏字段、格式混乱 | 完全符合公司规范 |
| 重复劳动、越改越烦 | 一次配置，终身复用 |

想让 OpenClaw 不 “蠢”，关键不是模型，是你没给它装对 “干活技能包”！今天就把这个「POC 自动转换 Skill」的完整教程公开，从原理到落地，抄作业就能用～

# 一、先搞懂：Skill 到底是什么？（5 分钟入门）

很多人装完 OpenClaw 吐槽 “问啥啥不会”，其实是没搞懂 Skill 的核心 —— 它不是简单的 “提示词”，而是**写给 AI 的 “标准化操作手册（SOP）”**，让 AI 知道 “什么场景做什么、按什么步骤做、调用什么工具做”。

## 3 个核心特点，一看就懂：

1. 结构简单：每个 Skill 是独立文件夹，核心就 1 个SKILL.md文件，用 Markdown 写，不用懂复杂语法；
2. 机制灵活：OpenClaw 启动自动扫描加载，按需调用不浪费 Token；
3. 能 “动手”：不仅能给建议，还能直接调用工具读写文件、批量处理 —— 这才是真正的 “干活 AI”！

典型 Skill 目录结构（直接抄）：

```
pdf-skill/
├── SKILL.md          # 主指令文件（必需）
├── FORMS.md          # 辅助逻辑（可选）
├── REFERENCE.md      # 参考文档（可选）
└── scripts/          # 工具脚本（可选）
```

# 二、真实需求拆解：我们需要小龙虾做什么？

## 核心目标

打造「POC 自动化转换 Skill」，让 OpenClaw 实现：

> 输入：任意格式 POC（Nuclei YAML、Python 原生、复现文档）+ 公司框架模板

输出：符合 pocscan POCBase 规范的 Python 脚本（自动命名、自动保存、直接上线）

### 全流程拆解（输入→处理→输出）

1. 输入要求（明确 AI 要什么）

* 原始素材：单文件 / 执行流程输入（支持 Nuclei、Python、攻击流程描述）；
* 参考标准：公司内部模板（如poc-template.py，含类结构、字段规范）；
* 自定义规则：可改输出文件名格式、保存路径、需排除的冗余代码。

2. 处理逻辑（AI 自动干这些活）

* 解析原始 POC：提取 CVE 编号、漏洞名称、检测逻辑、请求参数等核心信息；
* 适配框架：自动补POCBase类继承、meta 字段、`_verify()/_attack()`方法；
* 格式标准化：统一缩进、注释风格、变量命名（符合公司代码评审要求）；
* 语法校验：自动排查语法错误，确保直接能运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eep7PCRAQET1hcXTRlso2tS3OgEDib9Dg3ibRzWADKxBKzuyvKCbyrJFNLgKM4Rb9LyFlOPRUQJrVp5QmwV0b9wQvolSqVAs2h3rJbo1nphYA/640?wx_fmt=png&from=appmsg)

3. 输出规范（明确交付物）

* 文件名：CVE-年份-编号-漏洞名称.py（如CVE-2018-3245-WebLogic-T3.py）；
* 保存路径：output/目录（AI 自动创建）；
* 附加信息：脚本头部自动加转换日志（原始路径、转换时间、框架版本），便于追溯。

4. 质量要求（避免 “翻车”）

* 准确性：不篡改原始检测逻辑；
* 兼容性：直接集成到公司项目，无需额外修改；
* 高效性：单文件转换＜10 秒，支持批量处理；
* 可扩展性：后续能新增其他框架适配（如 Nessus、AWVS）。

# 三、动手实现：10 分钟搞定 Skill 开发（直接抄作业）

## 第一步：搭建 Skill 目录结构

按 OpenClaw 规范创建，直接复制粘贴到你的工作区：

```
poc-convert/
├── SKILL.md            # 核心指令（必需）
├── references/
    └── poc-template.py # 公司框架模板（必需）
    └── enums.py        # 枚举值参考（可选）
├── output/             # 自动输出目录（AI创建）
└── scripts/            # 辅助脚本（可选，如批量校验）
```

## 第二步：编写核心文件 SKILL.md（关键！）

SKILL.md 是灵魂，必须包含frontmatter（配置信息）和内容（执行指令），我已经写好完整版，复制粘贴就能用：

```
---
name: poc-converter
description: 将任意格式的POC（漏洞验证脚本）转换为 pocscan POCBase 框架格式的Python代码。保留原始检测逻辑不变，仅调整代码结构、导入、类继承、meta字段、_verify/_attack方法包装等。当用户提供一段原始POC代码并要求转换格式、适配框架、或"改成我们框架的格式"时触发。
---
# POC Converter

将原始POC脚本转换为 `pocscan` 框架的 `POCBase` 格式，**只改结构，不改逻辑**。

## 转换流程

### Step 1: 分析原始POC

从原始代码中提取以下信息：
- **漏洞标识**：CVE ID、CNNVD ID、漏洞名称
- **目标信息**：受影响产品、版本、厂商、操作系统
- **检测逻辑**：HTTP请求方式、请求路径、判断条件（状态码/响应内容匹配）
- **严重程度**：CVSS评分、漏洞等级
- **端口**：目标服务默认端口

若原始POC缺少某些meta字段信息，根据CVE ID查询推断合理值；无法推断则留空字符串。

### Step 2: 核心适配规则

**逻辑保留原则：**
- 原POC的HTTP请求路径、请求头、请求体、判断条件 **一字不改**
- 仅将 `requests.get/post(url)` 中的 `url` 替换为用 `rhost`/`rport` 构造的 `base_url + path`
- 原POC用硬编码IP的，改为从 `self.getg_option('rhost')` 获取
- vuln_sub_class的字段内容，参考references目录下的enums.py中class VUL_TYPE的各个类型

**结果输出：**
- 检测成功时构造 `ResultModel(poc_id=self.meta["poc_id"], risk_address=base_url, msg=结果描述)`
- 调用 `return self.parse_output(result)`
- 失败/异常时 `return self.parse_output(None)`

**ClassName 命名规则：**
- 格式：`CVE{年份}{编号}POC`，如 `CVE20196116POC`
- 无CVE则用产品名：`{Product}UnAuthPOC`

**poc_id 生成：**
- 使用 cve_id + 当前日期的 md5 前16位，或任意唯一8字节十六进制串

**枚举值选择：**
- 详见 `references/enums.py`

### Step 3: 输出与保存

直接输出完整可运行的Python代码，代码块用 ``` ``` 包裹。代码后附简短的字段说明（若有推断/假设的字段值请标注）。

将代码保存成新文件，在当前skill的output目录下（没有就新建一个），命名格式为 `system__app__p/pe__CVE编号.py`：
- p：只有poc
- pe：poc和exp都有
- CVE编号：根据漏洞信息补充

## 参考资料

- **框架字段和枚举值完整规范**：见 `references/enums.py`（当需要确认枚举值或字段含义时读取）
- **代码模板**：见 `assets/poc_template.py`（当需要干净的空白模板时读取）
```

## 第三步：放入公司框架模板

把你公司的poc-template.py放到references/目录，示例模板（供参考）：

```
# -*- coding: utf-8 -*-
from pocscan.api import POCBase, register_poc, ResultModel
from pocscan.api import E_META_ENUMS as enums

class CVEXXXXXXPOC(POCBase):
    meta = {
        "poc_id": "",
        "cve_id": "",
        "vul_id": "",
        "name": "",
        "disclosure_date": "",
        "solution": "",
        "description": "",
        "vuln_level": enums.VULN_LEVEL.CRITICAL,
        "vendor": "",
        "impact_product": "",
        "impact_version": "",
        "cvss_score": 0.0,
        "cvss_vector": "",
        "vuln_class": enums.VUL_CLASS.NETWORK,
        "rule": 'app=""',
        "has_exp": False
    }
    default_port = 80

    def _verify(self):
        rhost = self.getg_option('rhost')
        rport = self.getg_option('rport') or self.default_port
        base_url = f"http://{rhost}:{rport}"
        # 原始POC的检测逻辑将自动插入这里
        return self.parse_output(None)

    def _attack(self):
        return self._verify()

register_poc(CVEXXXXXXPOC)
```

# 四、部署到 OpenClaw：3 步搞定

## 1. 存放 Skill 目录

把poc-convert/文件夹放到 OpenClaw 的 Skills 加载目录（优先级：工作区＞本地＞内置）：

```
# 推荐放到工作区（最高优先级，不会被覆盖）
mkdir -p skills
cp -r poc-convert >/skills/
```

## 2. 验证加载成功

启动 OpenClaw 后，输入 “转换 POC 框架”，如果 AI 回复 “已加载Skill Poc-convert”，说明成功！

## 3. 使用示例（直接抄）

在 OpenClaw 聊天框输入： 帮我把这个 POC 转换成公司 pocscan 框架格式，保存到 output 目录：（粘贴原始 POC 代码 / Nuclei YAML / 复现文档） openclaw 会自动解析→适配→生成→保存，最终返回：

* 完整的 Python 脚本（可直接复制）；
* 保存路径（如poc-convert/output/CVE-2018-3245.py）；
* 转换日志（如 “原始文件：xxx.txt | 转换时间：2024-xx-xx | 补充字段：cvss\_score=9.8”）。

# 五、实测效果：半小时处理 100 个 POC

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eep7PCRAQERd8mgEuGMibDhrAsZwzuicOZWwiceaYEV9rUVnGBtFS4lcgF9RRPhMQkKKVLiaBpr5jmzvyn1ccALw6zicnS9L0JSXDMxOrhg4jtWI/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/eep7PCRAQESD2ktsNWj14cicU0sOrV05x8Xkt9SW8icicZdhTibJWmOax4gObxdGIYDicJxj0JksFx5VCzR4tKmIm4krfCfsUmZs94LZcyYQeZbw/640?wx_fmt=png&from=appmsg)

# 六、避坑指南：新手必看

1. 模板必须完整：references/poc-template.py要包含所有必填字段，否则 AI 无法补全；
2. 触发词要明确：尽量用 “转换 POC 框架”“适配 pocscan” 等关键词，避免歧义；
3. 批量转换技巧：把所有原始 POC 放到一个文件夹，输入 “批量转换这个文件夹里的所有 POC”，AI 会自动遍历处理；
4. Token 不够怎么办：批量转换时按 “10 个一批”，避免上下文溢出。

# 七、最后：为什么说 Skill 是 OpenClaw 的灵魂？

用了这么久 OpenClaw，最大的感受是：**AI 的 “聪明”，本质是你给它的 “指令足够清晰”。**

Skill 的核心价值，是把 “重复、标准化、高耗时” 的工作，做成可复用的 SOP—— 不用每次都跟 AI 掰扯 “要怎么改”，一次写好 Skill，终身受益。 除了 POC 转换，你还能写这些 Skill：

* 日志自动分析 Skill：输入日志文件，自动提取异常信息；
* 代码格式化 Skill：按公司规范自动对齐格式；
* 漏洞报告生成 Skill：输入扫描结果，自动生成合规报告。

# 福利时间

为了方便大家抄作业，我把「POC 自动转换 Skill」的完整代码（含 SKILL.md、模板文件、辅助脚本）打包好了，关注公众号【沐昊安全】，回复 “skill” 直接领取！

如果你们有其他重复工作想做成 Skill，欢迎在评论区留言，我来帮你设计 SOP～

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/DvxV6yFV5bqJnK3nmY4cGVb4XPibKDwHtw0pd0mKuiaKqHgibIg5GIwpGbv7Da46jBVgM3ZHEyvp8mcPeU5DMLK2Q/0?wx_fmt=png)

沐昊安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/DvxV6yFV5bqJnK3nmY4cGVb4XPibKDwHtw0pd0mKuiaKqHgibIg5GIwpGbv7Da46jBVgM3ZHEyvp8mcPeU5DMLK2Q/0?wx_fmt=png)

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