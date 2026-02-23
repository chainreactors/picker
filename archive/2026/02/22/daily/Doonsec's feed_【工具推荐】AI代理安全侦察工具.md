---
title: 【工具推荐】AI代理安全侦察工具
url: https://mp.weixin.qq.com/s/442jE-pq_YcVnK-2Dctm1w
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:18:51.481697
---

# 【工具推荐】AI代理安全侦察工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/exLpzP8D7NbojD0bOZAOfGAUQTWkhhD9NibQGTtRmLxRr7YHwZqVuPTId4kib2zO2Ko5uEnLUiaibfyL6u2MUFiaR5tSmzBvEU3MJGY2DyykCVSM/0?wx_fmt=jpeg)

# 【工具推荐】AI代理安全侦察工具

原创

visionsec
visionsec

安全视安

![]()

在小说阅读器中沉浸阅读

---

**声明****：该公众号分享的安全工具和项目均来源于网络，仅供安全研究与学习之用，如用于其他用途，由使用者承担全部法律及连带责任，与工具作者和本公众号无关。**

---

![View 0xsrb's full-sized avatar](https://mmbiz.qpic.cn/sz_mmbiz_jpg/exLpzP8D7NYxOcmSPRmjXpqwO7GGahJFt4JquNibq6Xm2gURaqva3voa8VPQRvVRdaYbd6eXaOcUr1iaSdMDbeXr16f8YP8yxpznMfvAxgddQ/640?wx_fmt=jpeg&from=appmsg)

在生成式 AI 快速落地的当下，从 OpenAI 的大模型生态到基于 LangChain 构建的自动化代理，再到 AutoGPT 这类自治系统，企业正在以前所未有的速度将 AI Agent 推向生产环境。但一个现实问题也随之暴露：大量 AI 服务在部署过程中，存在暴露在公网、缺乏鉴权、甚至泄露敏感配置的情况，而这些问题往往在被攻击者发现之前，并没有被防守方意识到。

此工具正是在这样的背景下诞生的一款工具。它的核心思路非常直接——利用 Shodan 这样的网络空间搜索引擎，对互联网中已经暴露的 AI Agent 实例进行被动式探测与识别，从而帮助安全人员在攻击者之前完成一次“资产侧的自查”。

与传统资产测绘工具不同，此工具的重点并不只是“发现端口和服务”，而是针对 AI 场景做了明显强化。它内置了多种针对 AI 应用的查询模板，可以直接定位诸如 AutoGPT 实例、LangChain agent、Streamlit 面板、甚至是未加保护的 Jupyter Notebook。这种能力的价值在于，它跳过了大量通用扫描阶段，直接将结果聚焦到“高价值且高风险”的目标上。

在实际使用层面，次工具的门槛并不高，部署流程也比较工程化。首先你需要准备 Python 3.11 及以上版本环境，以及一个 Shodan API Key。随后通过 Git 克隆项目源码并安装依赖即可完成基础部署。核心步骤可以理解为三步：拉代码、装依赖、配密钥。配置完成后，在项目目录中创建 `.env` 文件并填入 API Key，就可以直接启动扫描。

### Docker

```
# Build and run with Docker Compose
docker-compose up -d

# Or build manually
docker build -t aasrt .
docker run -e SHODAN_API_KEY=your_key aasrt
```

### 配置

1. **创建环境文件:**

   ```
   cp .env.example .env
   ```
2. **添加 Shodan API key:**

   ```
   # .env
   SHODAN_API_KEY=your_shodan_api_key_here
   ```
3. **（可选）自定义设置 `config.yaml`:**

   ```
   shodan:
     rate_limit: 1      # Queries per second
     max_results: 100   # Results per query
     timeout: 30        # Request timeout
   ```

---

## 快速入门

### 示例 1：运行模板扫描 (CLI)

```
python -m src.main scan --template clawdbot_instances --yes
```

示例 2：启动 Web 控制面板

```
streamlit run app.py
# Open http://localhost:8501 in your browser
```

### 示例 3：自定义 Shodan 查询

```
python -m src.main scan --query 'http.title:"AutoGPT"' --yes
```

### 示例 4：查看扫描历史记录

```
python -m src.main history
```

### 示例 5：列出可用模板

```
python -m src.main templates
```

**输出:**

```
┌─────────────────────────────┬──────────┐
│ Template Name               │ Queries  │
├─────────────────────────────┼──────────┤
│ autogpt_instances           │ 2 queries│
│ clawdbot_instances          │ 3 queries│
│ langchain_agents            │ 2 queries│
│ jupyter_notebooks           │ 3 queries│
│ exposed_env_files           │ 2 queries│
│ ...                         │ ...      │
└─────────────────────────────┴──────────┘
```

如果你更偏向标准化部署，也可以选择使用 Docker。项目已经提供了完整的 Dockerfile 和 docker-compose 配置，只需要一条命令就可以将服务拉起，这对于团队环境或需要长期运行的场景非常友好。相比本地运行，Docker 方式更适合做持续资产监控或接入自动化流程。

真正进入使用阶段后，它提供了两种典型方式：CLI 和 Web 界面。对于习惯自动化的安全工程师来说，CLI 是最直接的入口。通过调用内置模板，可以快速对特定类型的 AI 资产进行扫描，例如针对某类 Agent 实例的批量发现，或者直接编写 Shodan 查询语句进行精准匹配。如果需要查看历史扫描记录或已有模板列表，也都有对应命令支持，整体体验类似成熟的安全工具链。

而如果你更关注结果分析与展示，可以直接启动基于 Streamlit 的 Web Dashboard。它提供了可视化界面，包括扫描结果、风险评分以及简单的威胁地图展示，非常适合在汇报或复盘场景中使用。

更关键的是，它不仅仅停留在“发现”，而是内置了一层轻量级的风险评估逻辑。系统会自动识别常见问题，比如 API Key 泄露、认证缺失、调试模式开启、SSL 配置异常等，并结合类似 CVSS 的评分体系对风险进行量化。这使得扫描结果可以直接用于优先级排序，而不是一堆杂乱的资产列表。

从工程角度来看，此工具还具备完整的报告输出能力（JSON/CSV）以及基于 SQLite 的扫描历史记录，这意味着你可以持续跟踪暴露面的变化趋势，而不是一次性的结果。同时其模块化结构（搜索引擎、风险评估、报告生成）也方便你根据实际需求进行二次开发或扩展，比如接入更多资产测绘平台。

对于专业安全人员来说，这类工具的价值其实非常明确：它填补了“AI 资产暴露面管理”这一尚未被充分重视的空白。传统的漏洞扫描器更多关注 Web、主机和中间件，而此工具则将视角转向 AI Agent 本身——这类系统往往具备更高权限、更复杂逻辑，一旦暴露，其风险远高于普通服务。

但需要强调的是，此工具本质上仍属于被动侦察工具，其使用必须建立在授权前提之上。无论是在企业内部做资产梳理，还是在合法授权的渗透测试项目中使用，都应严格遵守相关法律与合规要求。

如果你目前正从事渗透测试、红队、DevSecOps 或安全建设相关工作，那么此工具非常值得加入你的工具链。它不只是一个“扫描器”，更像是一个面向 AI 时代的资产发现与风险感知入口，在很多情况下，它能帮你更早一步看到真正的攻击面。

****后台回复：0058****

****获得项目地址****

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Pf9NC3AaQF6Ceuo3ZCjemDo0mPDNTyoUJ1GhrE8u8odwIKUZVtKHuLfynEO1oM8fhqzOF05HAHz0BZI9OxqDkA/0?wx_fmt=png)

安全视安

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Pf9NC3AaQF6Ceuo3ZCjemDo0mPDNTyoUJ1GhrE8u8odwIKUZVtKHuLfynEO1oM8fhqzOF05HAHz0BZI9OxqDkA/0?wx_fmt=png)

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