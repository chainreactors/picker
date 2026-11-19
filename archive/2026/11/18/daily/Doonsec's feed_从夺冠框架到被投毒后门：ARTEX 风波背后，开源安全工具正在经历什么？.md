---
title: 从夺冠框架到被投毒后门：ARTEX 风波背后，开源安全工具正在经历什么？
url: https://mp.weixin.qq.com/s/YrgRtk6-rdLI2dFPn3snEg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:42:03.563857
---

# 从夺冠框架到被投毒后门：ARTEX 风波背后，开源安全工具正在经历什么？

# 从夺冠框架到被投毒后门：ARTEX 风波背后，开源安全工具正在经历什么？

原创

维度攻防
维度攻防

维度攻防

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 一个曾拿下攻防挑战赛冠军的 AI 渗透框架，在被现实攻击滥用后下架；随后社区分叉版本里，又被人塞进了无需认证即可执行命令的 WebShell。
>
> 源码看着干净，镜像却可能有毒 —— 这起事件值得每一位做安全、用开源工具的人仔细复盘。

## 一、先搞清楚：ARTEX 到底是个什么架构

ARTEX 是一套LLM 驱动的多智能体自主渗透测试系统，由开发者 Autumn-27 于 2026 年 7 月发布，曾获百度 agent+ 攻防挑战赛冠军。FreeBuf

技术栈与整体架构：

* 后端：Go 编写的单二进制程序
* 前端：Next.js，内嵌在后端二进制中
* 存储：PostgreSQL
* 模型接入：框架本身不自带大模型，通过 API 接入外部 LLM，支持 Anthropic Claude、OpenAI GPT，以及 DeepSeek、GLM、Grok、Kimi 等模型Internet Crime Complaint Center (IC3)

智能体协作模型：

* 规划器（Planner）：把自然语言描述的高层目标拆解成攻击 "意图"，维护跨轮次的共享任务清单
* 执行 Worker：多个子智能体并行执行意图，调用 Bash、HTTP 等工具完成侦察、漏洞验证、凭据收集等动作
* 双图结构：一张跨任务共享的资产图，一张按任务跟踪目标、事实与发现的探索图
* 人在回路：内置审批队列拦截工具调用，并有中间人代理记录完整流量
* 其他能力：容器内自带 nmap、curl 等工具，可挂载本地技能目录，也能连接远程 MCP 服务器；认证基于 JWT，管理员密码在首次访问 `/setup` 页面时设置Cloud Security Alliance Lab Space

简单说，它把过去渗透测试人员手动串联的整条流水线 —— 侦察、枚举、利用、凭据窃取、外传 —— 交给一组智能体并行跑，人只需要设定初始目标。

## 二、风波缘起：工具被武器化，上游仓库下架

框架发布后热度上升，10 周内积累了约 1500–2000 个 Star。但进入 10 月，多家安全厂商陆续披露它被现实攻击滥用：

* 韩国金融机构事件：CrowdStrike 追踪的 VAPOR PANDA 等组织利用 ARTEX 发起攻击，韩国一家金融机构约 6.7 万人的个人信息被窃取Internet Crime Complaint Center (IC3)
* ConnectWise 供应链事件：微软追踪的 Storm-0940 使用 ARTEX 加速扫描侦察、密码喷洒和 OAuth 应用滥用，尝试登录下游 2250 多个租户；多起案例中，从初次瞄准到拿到云环境特权访问不到 3 小时Microsoft
* FBI 在 11 月 13 日的 FLASH 通报中进一步指出，截至 11 月初，研究者已识别出超过 1600 个公网暴露的 ARTEX 控制台实例，实际部署数量可能更高Internet Crime Complaint Center (IC3)

2026 年 10 月 8 日，原作者以工具被恶意使用为由，将上游仓库下架并宣布停止更新、转向闭源。但下架并没有切断供给：大量 Fork、镜像副本、本地化改版以及商业版本（ARTEX PRO 等）继续在社区流通，风险由此转入下一个环节。

## 三、二开乱象：上游消失后，信任真空被谁填补

上游仓库下架后，社区出现了大量分叉。由于失去了唯一可对照的官方参考点，使用者很难判断哪个版本可信 —— 这正是本次投毒能够成立的结构性前提。

公开报道中出现的相关制品大致可分为几类Cloud Security Alliance Lab Space：

表格

| 类型 | 名称 | 状态 |
| --- | --- | --- |
| 涉事 Fork | trhhubsd/ARTEX（另有 ARTEXX 拼写变体） | Compose 文件指向恶意镜像，据称已不可下载 |
| 涉事镜像 | tomicdd/artex | 已确认植入后门，拉取量约 8000–9000 次 |
| 同类镜像 | congdonglinux/artex | 报道称与 tomicdd/artex 一致，同样需排查 |
| 其他副本 / 镜像 | mhtsec/ARTEX、RuoJi6/ARTEX、mianhuatang11/artex 等 | 未经独立审计，未发现问题不等于安全 |
| 原始上游镜像 | autumn27/artex | 已删除 |

这里需要特别强调：一份制品没有被公开分析过，不能视为 "干净"。除已点名的高风险 IOC 外，其余流通版本在获得可信来源比对之前，都应按不可信处理。

## 四、投毒细节：源码干净，后门藏在预构建镜像里

### 1. 篡改点只有一行

2026 年 11 月 3–4 日，安全研究者公开分析：热门 Fork trhhubsd/ARTEX 在提交 a4f4d38 中只修改了docker-compose.yml一个文件，把镜像地址从原始的

```
autumn27/artex:${ARTEX_TAG:-latest}
```

替换为

```
tomicdd/artex:${ARTEX_TAG:-latest}
```

Docker Hub 账号 tomicdd 于 2026 年 10 月 8 日 18:50 UTC 注册，镜像当日约 19:41 UTC 推送，与仓库修改时间高度吻合。FreeBuf

### 2. 后门藏在镜像二进制中，源码审查看不到

对照可见源码后发现：正常版本的 auth.go 中不存在captcha 字段，也不存在 verifyCaptcha 函数。后门逻辑只存在于预构建镜像的二进制内 —— 也就是说，克隆仓库后逐行审计源码，是看不出异常的。这是本次事件最值得警惕的地方：源码公开 ≠ 制品可信。

### 3. 后门触发机制

后门挂载在登录接口 POST /api/auth/login 上，行为链条如下：

1. 读取请求 JSON 中的 `captcha` 字段
2. 若字段首字符为 `!`，剥离 `!` 后将剩余内容传入 `verifyCaptcha`
3. `verifyCaptcha`

   执行 `os/exec.Command("sh", "-c", <剩余内容>).CombinedOutput()`，并返回标准输出与错误输出的组合
4. 在用户名、密码校验之前，直接返回 HTTP 200，响应体形如：

```
{”captcha”: ”<命令输出>”, ”error”: ”...”}
```

正常的认证路径（用户名校验、bcrypt 密码检查）在后门触发时被整体跳过。公开复现中，发送如下请求：

```
{”username”:”x”,”password”:”y”,”Captcha”:”!id”}
```

即可得到：

```
{”captcha”:”uid=0(root) gid=0(root) groups=0(root)\n”}
```

也就是说，知道触发方式的任何人，无需认证即可在容器内以 root 权限执行任意 Shell 命令并回显结果，构成一个未认证 WebShell。FreeBuf搜狐

### 4. 关键 IOC

* 镜像 digest：

  `sha256:ce85d8369ccc1a85423f1f75d2f3afaa2fab759e580da37a6891af2f7392745e`
* 镜像内二进制 digest：

  `sha256:d5070f52262effe216b840711343bff8f2787f39208d887d8dfd9c673f8d1573`
* 可疑镜像命名空间：`tomicdd/artex`、`congdonglinux/artex`
* 后门特征字符串：`captcha`、`Captcha`、`verifyCaptcha`、`/api/auth/login`、`sh -c`

> 提示：上述哈希用于离线比对、日志排查与隔离取证，不要在日常环境中拉取可疑镜像，也不要对公网目标发送利用请求验证。

## 五、这起事件暴露了什么

### 1. 这是一次镜像供应链替换，不是代码漏洞

攻击者既没有攻破上游维护者账号，也没有在被审计的仓库里注入代码。上游消失后，流行 Fork 和它引用的 Docker Hub 命名空间积累了 Star 与拉取量；一行 Compose 改动在代码审查中极易被忽略，而 docker compose up -d 的默认流程并不会提示用户 tag 实际解析到了哪个镜像 digest。Cloud Security Alliance Lab Space

### 2. 可变 Tag 与命名空间先到先得

Docker Hub 命名空间不与上游项目天然绑定，tag 内容可被所有者随时更换；版本号和文件名都看不出差异。再加上规范源码已被移除，用户失去了比对基准，信任链上的每一环都默认为 "可信"。

### 3. 安全工具本身更需要供应链审计

渗透框架、红队工具这类软件，天然会读取、保存大量高敏感凭据：LLM API Key、客户端凭据、会话令牌、数据库密码、云密钥。一旦工具自身被投毒，受害者不是被外部攻破，而是在自己的 "武器库" 里埋了后门。

## 六、排查与处置建议

如果你部署过相关版本，建议按以下顺序处理：

1. 立即止损

* 停止相关容器与编排，断开对外映射（管理端口常见为 8787）
* 删除本地缓存的 `tomicdd/artex`、`congdonglinux/artex` 镜像，避免再次 `compose up` 拉起
* 检查容器是否挂载了 Docker Socket、是否启用 `privileged: true`，评估是否已影响宿主机

2. 排查取证

* 在镜像仓库、CI 日志、K8s 清单、Compose 文件和本地运行时中检索上述可疑镜像与 Fork 来源
* 检查 ARTEX 控制台登录接口日志中是否存在异常或超长的 CAPTCHA 值；注意后门以 root 运行时可删除日志，无记录不等于未被使用
* 对曾运行受影响镜像的主机，建议隔离后从可信介质重建，而非原地清理

3. 凭据轮换

* 控制台存储、采集或可触达的所有凭据都应轮换：LLM API Key、客户端凭据与会话令牌、数据库密码、宿主机云密钥
* 受影响控制台产出的测试结论需要重新验证；曾从受影响控制台评估过的客户环境，应通知对方回溯审计活动窗口之外的异常行为Cloud Security Alliance Lab Space

4. 后续使用原则

* 不要信任来历不明的一键镜像；优先基于可审计源码本地构建
* 部署前核对仓库 remote、Compose 实际镜像、镜像 digest，并做二进制与源码对比
* 管理端口只绑定本地回环地址，避免控制台直接暴露公网
* 对其他任何 ARTEX 版本，在完成可信来源核验之前，一律按可疑对象处理

## 写在最后

剥掉 AI 智能体的包装，ARTEX 被滥用的攻击链路 —— 暴露应用、文件上传与 SSRF、密码喷洒、泄露密钥、OAuth 权限滥用 —— 都是我们熟悉多年的问题。真正被压缩的是时间：智能体并行尝试多条路径，一条失败就换另一条，从初始访问到持久化几乎不等人类读完日志。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/56vojF9ZLWEUrByhdC81sgBwVuGYeBDzVbW08PJxSDcOjcVcl79pVPic05r349tgxyWk0kJY5knOkm3aCpkwxSqBiaUr9t5VzPibybSwUkibAicM/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过