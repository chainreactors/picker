---
title: 不怕封号，不用海外卡，这样用 Claude Code
url: https://mp.weixin.qq.com/s/7qkEOsSDGUt75X5Zxk3g-A
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:23:20.007989
---

# 不怕封号，不用海外卡，这样用 Claude Code

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MGmpoYTX6riacLJEIpZUa5RqGDV1RpY9C0OcB6sdqF9tNdrpmvsZbtPibiaiaXX6uYcp64mtibS2sfp4tO6RqOO85G0yIxlGDiak7pI6NlyCCbmbw/0?wx_fmt=jpeg)

# 不怕封号，不用海外卡，这样用 Claude Code

原创

AI安全工坊
AI安全工坊

AI安全工坊

![]()

在小说阅读器中沉浸阅读

# 不怕封号，不用海外卡，这样用 Claude Code

最近 Anthropic 对国内用户大面积封号，很多人充了钱、配好环境，账号直接没了，钱也退不回来。

就算运气好没被封，官网订阅要海外信用卡，国内用户根本付不了款。

再退一步，就算搞到了账号和信用卡，国内网络直连 Anthropic / OpenAI / Google 的 API 也不通，Claude Code 打开直接报错，什么都用不了。

三道坎，一道都不好过。

![](https://mmbiz.qpic.cn/mmbiz_jpg/MGmpoYTX6rhLp5FkJssUotZh6XibhfMwhgbWvb2UmcBAQRvxu0z2pTVhI923Wgd5CKibTf6AoDJFDruk2sFoYY8SWHtQacevwcKDxgEAHKvHs/640?wx_fmt=jpeg&from=appmsg)

国内用 Claude Code 的三道坎与解决方案

我自己踩过前两道，后来找到了现在用的方案，分享出来，照着配应该半小时内能跑起来。

---

## 一、注册 HongMaCC

HongMaCC 是专门给国内用户做的 API 中转，Claude Code、Codex、Gemini 三个都支持，国内直连，微信支付宝付款，不需要任何海外账号。

我用了几个月，延迟和稳定性都没什么问题，偶尔高峰期慢一点，但不影响正常使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MGmpoYTX6riaia0Bd51Lft1ia1lvBht6EFCloTOng9kas6mzVdlL4nZW7UiadDGWImLZUnRacFqibZicdRicyhgLicDwBBZZUvPzwoHHkFGak5TVTZI/640?wx_fmt=png&from=appmsg)

用下面这个链接注册 ，先跑一段时间看看稳不稳：

https://hongmacc.com/signup?ref=HONGMACC-F1B3FE4D

注册完进控制台拿 API Key：

https://hongmacc.com/console/keys

企业用户需要发票报销的，在后台「工单中心」提交工单就行。

---

## 二、套餐

按量计费（用多少扣多少）：

| 套餐 | 价格 | 额度 |
| --- | --- | --- |
| 超值体验卡（限购一次） | ¥9.90/年 | 30 刀 |
| 轻量包 | ¥79.80/年 | 100 刀 |
| 标准包 | ¥398.00/年 | 500 刀 |
| 海量包 | ¥788.00/年 | 1000 刀 |

包月（每天有额度上限）：

| 套餐 | 价格 | 每日额度 |
| --- | --- | --- |
| 轻享月卡 | ¥248.00/月 | 25 刀 |
| 标准月卡 | ¥368.00/月 | 40 刀 |
| 旗舰月卡 | ¥798.00/月 | 100 刀 |

先用体验卡 额度跑通配置，没问题再选套餐。新用户体验卡 ¥9.90 也可以买，便宜。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MGmpoYTX6rh0r71WvQCUUHV2ZFw806shKrFaffV2YLLNzWNsiaJN5ibnY7E7T0cGEt9vlTdDiaz2SLZ3AoyHjKGDibicYqpTgrCa0yPPEDic9Hzdk/640?wx_fmt=png&from=appmsg)

---

## 三、配置（选一种方式）

新手推荐 CC-Switch，图形界面，不用动命令行。

想自己手动配也行，下面两种都有教程。

---

## CC-Switch（推荐）

开源桌面工具，三个 AI 工具的配置统一在这里管，内置 HongMaCC 预设，填个 Key 就完事。Windows / macOS / Linux 都有。

下载：GitHub 国内慢，我打包到夸克网盘了：

> "
>
> 公众号后台回复「ccswitch」也能拿到下载链接。

配置步骤：

1. 1. 安装打开 CC-Switch
2. 2. 顶部选工具（Claude Code / Codex / Gemini）
3. 3. 「供应商管理」→「新增供应商」→ 找到 HongMaCC 预设
4. 4. 填 API Key，保存
5. 5. 主界面切换，完成

三个工具共用一个 Key，配一次全搞定。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MGmpoYTX6rgCYCWKlJdYpO33o83gaonTV9nJHV5KnnJWrkGuje72Tpy1jT8Of2bkmXjbxdbLSDkyV4TFg3eibc3PeQ0C69L2MLWIftWMdJKM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MGmpoYTX6riaF9NUgR7huwzZIZRCxZIqEic97KSRDKmCKDUuLqFiaVq1rB3vQAYQYeec38kohOx2Zdzo7iaGfj3PATEzY3MdASBWE1icEZySEz3s/640?wx_fmt=png&from=appmsg)

---

## 手动配置

先装 Node.js，三个工具都要用：

https://nodejs.org 下载 LTS 版本，装完终端跑 `node --version` 验证一下。

macOS 用 Homebrew 的话：`brew install node`

Linux / WSL 推荐 nvm：

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install --lts
```

---

### Claude Code

安装：

```
npm install -g @anthropic-ai/claude-code
```

npm 慢的话加镜像：

```
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
```

配置中转，macOS zsh：

```
echo 'export ANTHROPIC_BASE_URL="https://hongmacc.com/api"' >> ~/.zshrc
echo 'export ANTHROPIC_AUTH_TOKEN="你的API密钥"' >> ~/.zshrc
source ~/.zshrc
```

macOS bash / Linux：

```
echo 'export ANTHROPIC_BASE_URL="https://hongmacc.com/api"' >> ~/.bashrc
echo 'export ANTHROPIC_AUTH_TOKEN="你的API密钥"' >> ~/.bashrc
source ~/.bashrc
```

Windows PowerShell（永久生效）：

```
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://hongmacc.com/api", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_AUTH_TOKEN", "你的API密钥", "User")
```

重开 PowerShell 生效。跑 `claude` 启动。

---

### Gemini CLI

安装：

```
npm install -g @google/gemini-cli
```

macOS zsh：

```
echo 'export GOOGLE_GEMINI_BASE_URL="https://hongmacc.com/gemini"' >> ~/.zshrc
echo 'export GEMINI_API_KEY="你的API密钥"' >> ~/.zshrc
echo 'export GEMINI_MODEL="gemini-2.5-pro"' >> ~/.zshrc
source ~/.zshrc
```

macOS bash / Linux：

```
echo 'export GOOGLE_GEMINI_BASE_URL="https://hongmacc.com/gemini"' >> ~/.bashrc
echo 'export GEMINI_API_KEY="你的API密钥"' >> ~/.bashrc
echo 'export GEMINI_MODEL="gemini-2.5-pro"' >> ~/.bashrc
source ~/.bashrc
```

Windows PowerShell：

```
[System.Environment]::SetEnvironmentVariable("GOOGLE_GEMINI_BASE_URL", "https://hongmacc.com/gemini", "User")
[System.Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "你的API密钥", "User")
[System.Environment]::SetEnvironmentVariable("GEMINI_MODEL", "gemini-2.5-pro", "User")
```

跑 `gemini` 启动。

---

### Codex CLI

Codex 和前两个不一样，要改配置文件，稍微麻烦一点。

第一步，编辑 `~/.codex/config.toml`（Windows 是 `C:\Users\你的用户名\.codex\config.toml`），文件开头加上：

```
model_provider = "crs"
model = "gpt-5-codex"
model_reasoning_effort = "high"
disable_response_storage = true
preferred_auth_method = "apikey"

[model_providers.crs]
name = "crs"
base_url = "https://hongmacc.com/openai"
wire_api = "responses"
requires_openai_auth = true
env_key = "CRS_OAI_KEY"
```

第二步，编辑 `~/.codex/auth.json`：

```
{
  "OPENAI_API_KEY": null
}
```

第三步，设环境变量。macOS / Linux：

```
echo 'export CRS_OAI_KEY="你的API密钥"' >> ~/.zshrc
source ~/.zshrc
```

Windows：

```
[System.Environment]::SetEnvironmentVariable("CRS_OAI_KEY", "你的API密钥", "User")
```

三个工具用的是同一个 API Key。

---

## 三个工具怎么选

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MGmpoYTX6rjfs4Hjp2NdO6uYuTVdbdlgYaWibWPD96KN14eVEDKuL3Y93sCS2tncMa7zhNjcZibP4nmIF8PjVkYoJMqUoIMczYgfMc1yPjFt0/640?wx_fmt=jpeg&from=appmsg)

Claude Code、Gemini CLI、Codex CLI 适用场景对比

| 工具 | 我的用法 |
| --- | --- |
| Claude Code | 日常主力，代码理解强，上下文长 |
| Gemini CLI | 需要联网查资料的时候 |
| Codex CLI | 快速生成代码片段 |

三个都配好，用 CC-Switch 切换一下就行。

---

## 最后

注册：https://hongmacc.com/signup?ref=HONGMACC-F1B3FE4D

拿 API Key：https://hongmacc.com/console/keys

> "
>
> CC-Switch 多平台客户端下载：公众号回复「ccswitch」）

文档：https://hongmacc.com/docs

有卡住的地方评论区说，我看到就回。

---

*价格以官网实时为准。*

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BibeFvVBkRA8RWa5pyic1Xob8V1UxQjOHLAx5qbkPJ2gibKpIQpRw4ogjL6jE9xIxc26o12ZRTBvPaLQNjxXDAO5g/0?wx_fmt=png)

AI安全工坊

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BibeFvVBkRA8RWa5pyic1Xob8V1UxQjOHLAx5qbkPJ2gibKpIQpRw4ogjL6jE9xIxc26o12ZRTBvPaLQNjxXDAO5g/0?wx_fmt=png)

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