---
title: 95GB 网络安全 AI 训练集免费开放：30+ 领域全覆盖，附完整下载方式
url: https://mp.weixin.qq.com/s/XxP3t55-igly4xchMTorNg
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:05:21.346666
---

# 95GB 网络安全 AI 训练集免费开放：30+ 领域全覆盖，附完整下载方式

# 95GB 网络安全 AI 训练集免费开放：30+ 领域全覆盖，附完整下载方式

原创

Violet Walker
Violet Walker

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MJkrVicjytKib4lH2Z2C6Tlf3patR1hjJ8B3f1AAshRb3jGibvJpaqee3icJKJkRWRQq3QP6fg9dEgR9gVDqqtMCkeiatfUmxWMPtU/640?from=appmsg)
> **导语**：研究者在 X 推荐了一份"PhD 级"网络安全 AI 训练集，95GB、30+ 领域、红蓝对抗全收。数据是真全，但翻开后有三处雷：版权争议未决、许可自相矛盾、作者承认压缩包夹带真实恶意样本。

---

## 一、这份数据到底是什么

推荐它的是印度安全研究者 Md Ismail Šojal（@0x0SojalSec），11 月 10 日那条推文收获 320 赞、35 转发，评论区"WTF"和"这个思路可以"各占一行。推文里他甩出一张 HuggingFace 数据卡截图，标题很硬：史上最大的 PhD 级网络安全数据集，白给，用来训你自己的 Cyber 模型。

落到仓库页面上，数据集 ID 是 `Vyber07/cyber-security`。作者是 GitHub 上的 Vyber07（真名 MEGHKUMAR SHAH，艾哈迈达巴德 Gandhinagar University 网络安全专业学生），仓库建于 5 月 30 日，最后改动停在 8 月 31 日，累计下载 15479 次、点赞 860 个。卡面标注 Apache-2.0，任务类型为 text-generation 与 question-answering。

数据卡自述的来源相当硬核：PortSwigger Web Security Academy 全 31 个专题（SQL 注入 16 个实验、XSS 30 个、HTTP 请求走私四种变体全收）、HackTheBox 1500+ 靶机、MITRE ATT&CK 的 200+ 技术与 400+ 子技术、MITRE D3FEND 的 100+ 防御技术、MITRE ATLAS 的 50+ AI 攻击技术、CIS Controls v8 的 153 项保障措施，外加 HackerOne 60 万+ 漏洞记录和 NIST CSF 108 个子类别。

![HuggingFace 上这份网络安全训练集的数据卡片](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6O01pZxdT5Hoic18VDYGDdJSszv2WJw60h7CkYL7MU3XBujKAoVJtnkJE2xbCWEibWpYXQMaILiaabicKvBF1njjKUVCZQ81SaThvo/640?from=appmsg "HuggingFace 上这份网络安全训练集的数据卡片")

*图：推文作者展示的数据卡截图（图源：@0x0SojalSec 推文）*

![数据卡列出的 30+ 安全领域覆盖表](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NeMMWnqYKf397KtzcCicuUk0XLZxTrzoHSpwzAMZC1lyRuBOj07pXx0v8ibE5XRVnBhS9HxqpjiaSzs1CudOL6NY3dcpBicBvaw0o/640?from=appmsg "数据卡列出的 30+ 安全领域覆盖表")

*图：README 中的领域覆盖表，含各类文件数（图源：@0x0SojalSec 推文）*

## 二、卡片写的和仓库里的是两回事

这里必须较真。我把 HuggingFace 文件树接口翻页拉全做了逐文件统计，结果和 README 有出入：

| 项目 | README 自述 | 实际统计 |
| --- | --- | --- |
| 文件总数 | 507 | 6178 |
| 总体积 | Overview 段写 16GB，Statistics 表写 ~95GB | 88.51 GB |
| 其中重复文件 | 未提及 | 1678 个 `__dup1` 副本，占 26.55 GB |
| 0 字节空文件 | 未提及 | 22 个 |
| 顶层目录 | 30+ 领域 | 35 个 |

也就是说，去掉重复副本后实际约 4500 个文件、61.97 GB。体积大头在漏洞情报目录：`vulnerability-intelligence/cybersec_master.jsonl` 单文件 2556 MB，同一份数据在根目录和目录内各存了副本，还有一份 2420 MB 的截断副本；ARVO 相关的崩溃复现包有 3985 个文件、51.12 GB，涉及 1358 个独立案例 ID。另外还有 21 个 `docs__superpowers__*.py` 空脚本和 0 字节的 `vapt__web-wordlists.json`——扩容脚本传上去了，内容是空的。

## 三、下载方式（gated 需登录）

仓库状态是 `gated: auto`，匿名访问数据文件会直接返回 401 GatedRepo 错误，必须登录 HuggingFace 账号并在数据集页面点一次"Agree and access"（同意共享用户名与邮箱），之后命令行和直链才通。

**命令行整包拉取**

```
pip install -U "huggingface_hub[cli]"
hf auth login
hf download Vyber07/cyber-security --repo-type dataset --local-dir ./cyber-security
```

**Python 脚本按需抓取**（推荐，只拿红蓝目录，省 80GB 硬盘）

```
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id="Vyber07/cyber-security",
    repo_type="dataset",
    allow_patterns=["red-team/*", "blue-team/*", "web-security/*"],
    local_dir="./cyber-security",
)
```

**带 token 的直链下载**

```
export HF_TOKEN=hf_xxxxxxxx
curl -L -H "Authorization: Bearer $HF_TOKEN" \
  -o mitre-attack-tools.json \
  "https://huggingface.co/datasets/Vyber07/cyber-security/resolve/main/red-team/mitre-attack-tools.json"
```

**Git LFS 方式**

```
git lfs install
git clone https://huggingface.co/datasets/Vyber07/cyber-security
```

数据集主页：https://huggingface.co/datasets/Vyber07/cyber-security

## 四、三个必须知道的雷

第一处是版权。10 月 16 日，用户 Voidreaper2026 在讨论区提交版权投诉（编号 8），指出该仓库的 `vulnerability-intelligence/cybersec_master.jsonl` 与他自己的 `Voidreaper2026/cybersec-master-dataset` 中同名文件的字节数与 SHA256 完全一致，而后者上传在前、本仓库创建在后，Apache-2.0 要求的署名与许可文本却没有出现。投诉还指出 LICENSE 里"All original content and copyrights belong to owner of the repo"这句话，是 5 月 31 日的提交 b5f4b50 把继承许可里的"Amazon Web Services (AWS)"替换掉后形成的。讨论至今未获作者回应，有网友建议直接向 dmca@huggingface.co 举报。

第二处是许可自相矛盾。卡片 front matter 写着 apache-2.0，LICENSE 正文却写着"商业使用被严格禁止""所有原创内容与版权归仓库所有者"，两套条款摆在一处，只看卡片容易吃亏。

第三处是格式和内容。6 月一条讨论里，训练者反映格式混乱、JSON 被转义、缺少 role 字段，作者回复说清洗与标准化因"基础设施限制和相关成本"暂时搁置，先把现有数据放出来给大家用。他同时提醒：部分 `.gz` 文件里是真实的恶意样本，只应在隔离分析环境处理，不要在常规系统上解压或执行。这句话后来没人再提，但它决定了你该怎么落地。

## 五、紫队视角：这份数据该给谁用

这事儿吧，得从两边儿看。

红队这波操作我给满分。把红队打法、免杀技巧、C2 框架用法做成可下载语料，等于把原本散落在几十份 PDF 和付费课程里的东西打包成一次下载。但换个角度看，这也意味着攻击方法论的边际成本被压到了接近零——同一份数据，防守方也能拿去反推自家检测规则的缺口。

蓝队真正该关心的是那份"检测与响应"侧的语料：Sigma 规则、YARA、Snort/Suricata 规则、KQL 查询、威胁狩猎查询、事件响应剧本、MITRE D3FEND 映射。这些喂进 SIEM 或 SOAR，比自己从头写检测逻辑快得多，也是这份数据集里商业价值最高、争议最小的部分。

![红蓝双方围绕同一份知识库协作](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6O4lUbaibgoqyJvqY7cu3icbt8P0HnLicD023icGicTNW2k4j0vwtubeEk4cyc9XV5qzbLjEncBGCiaswExvFGgRZRYQvw2kcOYJH4oY/640?from=appmsg "红蓝双方围绕同一份知识库协作")

*图：红蓝两侧共用同一份攻防语料（配图由华盟网生成并授权使用）*

落到实操，红队用之前，授权边界先落到纸面：目标、时间窗、允许动作、出口 IP 一条条写清，用完销毁样本仓库，别让"语料库"变成公司资产泄露的缺口。蓝队用之前先做三件事：把 `__dup1` 那 1678 个重复文件按哈希剔重，省下 26.55 GB 磁盘；按 MITRE ATT&CK 技术 ID 抽样人工复核，把 AI 生成的不准确规则挡在生产之外；下载与预处理全部放在隔离沙箱里，因为作者本人已明说里面有真家伙。

最后一句实话：这份数据是宝藏，也是陷阱。截至目前，该数据集的 16 条公开讨论里仍有 6 条未关闭，其中 3 条是删除请求、2 条是版权与署名争议、1 条是 README 更新请求。仓库作者在讨论区的回应始终只有"资源到位后再改"。下载之前，先把 LICENSE 和讨论区读完，比直接拉 88GB 硬盘要划算。

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OFoib33G35Ks9SpTwqFiakCPMDqb4IS4pqWc4UZvroMicM5vUlTGedyFM9CiaqdU5zykVibBt8baMBAj1ic7G5h9ChpCocLwe5RUITA/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PKiahVIZL1Hs2vuMUic9JKk8f3XAoILdJT1uPOBRbQ37KiacOxZHwt6M0GHuzjpqgWTrdI38acaNMo3BIia6jv1UZXqKiabX9cBnhE/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MA6cOA75OEQUofmbHnOEmIxXFRt9SkOmfSMVnQttyIEqIGN7fGLdz4YMRyosRLmuoYoaRyXlN6J9PFkRxxGzg7OPRbx7T0dibk/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MribmZt0U9jQZ5v1DlLxbgbwHo8ibOYjvjXJzhx1OCPUJ9qxia0TWHj8ellic613aGNppbbCkYbJzPG3XmHdicJ53turODssPK1vMU/640?from=appmsg)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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