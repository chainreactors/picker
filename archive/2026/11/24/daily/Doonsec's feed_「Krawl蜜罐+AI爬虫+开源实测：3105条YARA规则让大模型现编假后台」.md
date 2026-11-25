---
title: 「Krawl蜜罐+AI爬虫+开源实测：3105条YARA规则让大模型现编假后台」
url: https://mp.weixin.qq.com/s/udzWVW_YVlee9e9LTy8paw
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:45:31.431773
---

# 「Krawl蜜罐+AI爬虫+开源实测：3105条YARA规则让大模型现编假后台」

# 「Krawl蜜罐+AI爬虫+开源实测：3105条YARA规则让大模型现编假后台」

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

夜里两点，一个只跑着 Nginx 默认页的域名，十分钟内收到四百多个请求。路径从 `/.env` 到 `/wp-config.php.bak`，再到 `/api/v1/users`，User-Agent 一会儿是空字符串，一会儿伪装成 Googlebot。这些不是人点出来的，是扫描器和 AI 爬虫按清单挨个试出来的。

传统的做法是封 IP、上 WAF、写规则。Krawl 走的是另一条路：既然它们这么爱找漏洞，就造一个到处是漏洞的假站，让它们把时间花在假后台、假配置、假凭证上，同时把每一次试探记成可以查询的证据。

这篇文章只拆这一个工具。它的代码、规则库、评分逻辑我都拉下来跑过，下面出现的数字都能在仓库或本机复现。

## 一、它到底是什么

Krawl 是一个云原生的 Web 欺骗服务器，也就是蜜罐。项目用 MIT 协议，Python + FastAPI + SQLAlchemy，当前 843 星、76 个 fork、4 个未关闭 issue，最新版本 v3.0.0 发布于 2026 年 11 月 9 日，仓库 2025 年 12 月 10 日建立，最后推送在 2026 年 11 月 21 日。

它的思路很直接：起一个假站，里面放满"低垂果实"——假的后台登录页、假的目录列表、假的 `.env`、假的数据库备份名、假 API Key。扫描器按字典打过来，每一个路径都能命中，但命中的全是假的。真正的业务站在它后面，或者干脆不在同一台机器上。

![Krawl 的诱饵页示例](https://mmbiz.qpic.cn/sz_mmbiz_png/J2hBCjr4LfshicQgFx2vfMWIVbt8HaAykiaWtH242yC953mFOOic5ZB9XjMOyOKV7oXqcyS57gwB8708XogoqK9AMNt2ibvlbSwV2tD4WVQY1icA/640?wx_fmt=png "Krawl 的诱饵页示例")

官方给了一个在线 demo（demo.krawlme.com），我本地也起了一份：`docker run` 一条命令，或者用 uvicorn 直接跑 `app:app`。单机模式用 SQLite，不需要任何外部依赖；要横向扩展就切到 PostgreSQL + Redis，Helm chart 默认就是这个模式。

## 二、一条请求进来，会发生什么

这是 Krawl 最值得看的部分，因为它的处理顺序写得很清楚。

请求进来后，`path`、`query`、`body`、`User-Agent` 和每一个 header 会被**分别扫描**，每个字段都过两遍：原始值和 URL 解码后的值。这样一条规则永远只看到一个字段，通过 `scan_target` 变量知道自己看的是哪一个，误报会少很多。

命中之后产生一个 finding，带四样东西：规则名、攻击类型、严重级、以及该回什么类型的假回复。同一个请求里如果命中多条规则，同一种攻击类型只保留严重级最高的那一条，然后写进 `attack_detections` 表。

回复阶段按三层走：先看有没有规则指定了 `response_type`，有就按类型去 `responses/manifest.yaml` 里取假回复；没有就看这个路径在 `pages:` 里有没有诱饵页；再没有就进"蜘蛛迷宫"，返回一页随机链接。

我本地实测了四条请求，结果和文档一致：

* `/?id=1' UNION SELECT password FROM users--` 返回 200，215 字节，内容是一段 MySQL 1064 语法错误，`attack_type=sql_injection`。
* `/../../../../etc/passwd` 返回 200，592 字节，内容是伪造的 `root:x:0:0:root:/root:/bin/bash`，同时命中 `path_traversal` 和 `lfi_rfi` 两条规则。
* `/.env` 返回 200，342 字节，里面是伪造的 `APP_KEY=base64:...`、`DB_HOST=127.0.0.1`，被记为 `common_probes` 并触发蜜罐路径。
* `POST /login` 带 `username=admin&password=Passw0rd123`，凭证被原样写进 `credential_attempts` 表，路径记为 `login_attempt`。

六个请求，五类攻击，全部落库。这就是它和"只写日志的蜜罐"的区别：它把"谁在探、探什么、用什么规则"变成了结构化字段。

## 三、规则库的硬数字

README 写的是"3,100+ 条规则"，我把 `rules/` 目录下 14 个 `.yar` 文件全下载下来数了一遍：**3,105 条**，对得上。

拆开看：

* `vulnerabilities.yar` 567 条，`cve_2017_and_older.yar` 351 条，`cve_2018` 116 条，`cve_2019` 124 条，`cve_2020` 156 条，`cve_2021` 279 条，`cve_2022` 289 条，`cve_2023` 308 条，`cve_2024` 337 条，`cve_2025` 223 条，`cve_2026` 257 条，`cve_enterprise.yar` 75 条，`exposures.yar` 4 条，`recon.yar` 19 条。
* 规则里出现的**唯一 CVE 编号 2,519 个**。
* 回复类型 16 种，按命中次数排：XSS 662、路径穿越 569、命令注入 491、SQL 错误 295、云元数据 113，剩下的是模板求值、敏感文件、Spring Actuator、版本库元数据、phpinfo、GraphQL、容器 API 等小类。
* 严重级分布：5 分 1,043 条、7 分 903 条、9 分 823 条、10 分 239 条，8 分 75 条，其余是 2 到 6 分。
* 置信度：medium 3,062 条、high 110 条、low 1 条。

最后这行数字比前面所有数字都重要。**98% 以上的规则是 medium 置信度**，规则文件开头自己写了原因：一条规则只能说明有人在探这个端点，它分不清对方是在利用漏洞，还是扫描器在给这个端点打指纹。所以 Krawl 给你的是线索，不是结论。谁要拿它当"漏洞扫描器"用，第一天就会误判。

![仪表盘里的攻击类型分布](https://mmbiz.qpic.cn/sz_mmbiz_png/J2hBCjr4LftBS3pODhnbEWZlYoMSnx3ZicSNuYjD6PzqtAR0or5M8Tj8G9XPr5Gn3uXhzPDNvBSvk7mibibNEBQRvdrU3weKp5iaick62NJLqp5c/640?wx_fmt=png "仪表盘里的攻击类型分布")

规则本身是从 ProjectDiscovery 的 nuclei-templates 里提取最具体的请求特征改写的，每个规则都带 `reference` 指回原始检查，协议是 MIT。这一点算诚实：它没有假装规则是自己从零挖出来的。

## 四、IP 评分：五个信号，四类人

Krawl 每分钟跑一次 `analyze-ips`，每次最多 2,000 个 IP，取最近 30 天、最多 10,000 行访问日志，按五个信号打分：

| 信号 | 触发条件 | attacker | bad\_crawler |
| --- | --- | --- | --- |
| 危险方法占比 | POST/PUT/DELETE 等超过 10% | 6 | 2 |
| robots.txt 违规 | 访问 Disallow 路径超过 10% | 4 | 6 |
| 请求间隔不均 | 300 秒窗口内变异系数 ≥ 0.5 | 3 | 0 |
| 多个 User-Agent | 不同 UA ≥ 2 个 | 2 | 6 |
| 攻击 URL | 窗口内攻击类型 ≥ 1 种 | 15 | 4 |

四类人是 attacker、bad\_crawler、good\_crawler、regular\_user，谁分高算谁，平局按这个顺序取第一个。文档给了一个算例：40 个 GET、4 个 POST（9%）、6 次 `/admin`（14%）、2 个 UA、一次 `/.env` 探测，attacker 得 4+2+15=21 分，bad\_crawler 得 6+6=12 分，判为 attacker。

这套评分不是机器学习，是手写权重，所以它可解释，也可以改。文档里还老老实实列了三条已知限制：`regular_user` 的"多 UA"权重 3 分永远不会被触发；被剪枝的请求仍然进分母；时间指标存的均值，比较用的是变异系数。

我本地发完六个请求、等了一轮 `analyze-ips`，127.0.0.1 的评分是 attacker 28 分、bad\_crawler 8 分、regular\_user 8 分，最终判成 attacker。和文档给的算例对得上：攻击 URL 15 分、危险方法 6 分、robots 违规 4 分、间隔不均 3 分。这种"把缺点写进文档"的做法，在安全工具里不多见。

![IP Insight 里的行为评分与分类](https://mmbiz.qpic.cn/mmbiz_png/J2hBCjr4LfvWpIsXfychC90P9mVXia1ibUmv0XRu6BsRYxNh1icTrj2vkNYoQS5jaLjxNiazuTx0R5pVvz4aRV3NlXZxcssYPDoskiaiaV1W2CeGI/640?wx_fmt=png "IP Insight 里的行为评分与分类")

## 五、蜘蛛迷宫和 tarpit：专门对付抓数据的

任何没有命中的 GET 请求会进"蜘蛛迷宫"：返回一页随机链接，链接名由配置里的字符集随机生成，每页 5 到 10 条，点进去还是随机链接。我本地请求了一个随机路径，返回 200、3,527 字节、9 个链接，全是 `/I2SB8VyhJ3` 这种没有语义的路径。

同一个 IP 在蜜罐路径上访问到 250 页（`crawl.max_pages_limit`）就会被封 600 秒，而且封禁时长按违规次数递增（`ban_multiplier`）。这条规则对"跟着链接一直爬"的爬虫特别有效：它永远走不到尽头，每走一步都在给自己加违规次数。

tarpit 是另一层，默认关闭，打开后每个蜜罐响应额外延迟 5 秒，并在页面里塞一段随机单词组成的"词沙拉"——没有语法、没有意义，但看起来像正常正文。官方文档写得很直白：这是给"抓页面训练模型"的爬虫准备的，让它烧时间、收噪音。

这里有个必须说清楚的取舍：**tarpit 对所有蜜罐访客生效**，包括遵守 robots.txt 的搜索引擎爬虫和误入的真人。官方文档自己也承认，这只适合独立蜜罐域名，不适合你想被索引的站点上的诱饵路径。延迟调得越高，你自己的连接占用也越高，超过客户端超时时间反而提前结束，效果更差。

## 六、AI 生成诱饵页：最值得看，也最需要想清楚

这是 Krawl 和传统蜜罐最大的差别：诱饵页可以由大模型现场生成。

配置里 `ai.enabled` 打开，`provider` 选 `openrouter`、`openai`，或者把 `openai_base_url` 指向自托管的 llama.cpp / Ollama。仓库自带 compose 里就有这两个服务，测试用的是 Qwen 1.5-1.8B 和 Qwen3.5-4B 这类小模型，官方说法是参数量越大，生成的 HTML 越像真的。

生成逻辑我读了 `generative_ai.py`：

1. 先按路径查数据库缓存，命中就直接返回，大小写变体（`/.ENV` 和 `/.env`）复用同一页。
2. 没命中且当天生成次数没到上限，才调模型。默认 `max_daily_requests` 是 10，超过就回落到静态蜜罐。
3. prompt 模板存在 `config.yaml` 里，只有两个占位符：`{path}` 和 `{query_part}`。
4. 模型返回的内容去掉 Markdown 代码块，按路径后缀决定 `content_type`，HTML 就直接回给请求方。

问题就在这里：**`{path}` 和 `{query_part}` 来自攻击者的请求，原样拼进 prompt**。代码只做了 `normalize_path`（合并重复斜杠、去掉末尾斜杠），没有做任何转义或截断。攻击者可以把指令写进 URL 路径，让模型按他的意思生成页面；生成结果又会以 `text/html` 直接回给攻击者。

这不是一个"漏洞"，因为蜜罐本来就是给攻击者看的，页面内容也不涉及你的真实数据。但它意味着三件事：

* 你的 LLM 配额和账单，有一部分是攻击者在花。日限 10 页是成本闸门，不是安全闸门，路径变体多了照样会打满。
* 如果你把真实内部信息（真实域名、真实员工名、真实系统名）写进 prompt，攻击者可以通过生成页面反推出来。
* 蜜罐域名必须独立：不要和真实业务同域，不要共享 cookie 域，不要让蜜罐页面能读到业务站的任何东西。

官方文档还提醒，诱饵页默认是所有安装都一样的，部署前必须替换 `responses/` 下的文件，否则攻击者一眼就能认出这是 Krawl。

## 七、上手：三条路

最省事的是单容器：

```
docker run -d -p 5000:5000 \
  -e KRAWL_DASHBOARD_SECRET_PATH="/my-secret-dashboard" \
  -e KRAWL_DASHBOARD_PASSWORD="my-secret-password" \
  -v krawl-data:/app/data \
  --name krawl ghcr.io/blessedrebus/krawl:latest
```

要 PostgreSQL + Redis 就上 `docker/docker-compose.scalable.yaml`；K8s 用 Helm chart，默认就是 scalable 模式，也能横向扩副本。单机模式用 SQLite + 进程内字典，适合 homelab 和 50 万请求以内；scalable 模式用 PostgreSQL + Redis，仪表盘有三级缓存，适合生产和高流量。

仪表盘不是固定路径：启动时随机生成一个 32 位十六进制的 secret path，密码也随机生成并打在日志里。我本地启动日志里就是 `/5fbf93ff...` 加一串 48 位密码。五个标签页对"拿到路径的人"开放，登录后才开放封禁列表、规则管理、webhook 这些高危操作。

## 八、避坑：我读代码和实测看到的

**1. 会话 cookie 没有 Secure 标记。** 登录成功后种的是 `krawl_auth`，`httponly=True`、`samesite="strict"`，但没有 `secure=True`。如果你用 HTTP 反代访问仪表盘，这个 cookie 会明文过网络。会话有效期 12 小时，存在 Redis 或进程内字典里。

**2. Cloudflare token 明文返回。**`/api/webhooks/status` 这个接口会把 Cloudflare 的 `auth_token` 原样放进 JSON 返回给任何已登录仪表盘的人。也就是说，仪表盘账号等于 Cloudflare API token 的全部权限。要么别在仪表盘里配 CF，要么给这个 token 单独限权。

**3. 登录失败会锁定，但密码是单因子。** 我实测连续 5 次错误密码：前 4 次返回 401 并提示剩余次数，第 5 次返回 429，锁定 30 秒；锁定时间按 `30 × 2^n` 递增。比较用的是 `hmac.compare_digest`，这点做得对；但仪表盘本身只有密码，没有用户名、没有 MFA。放到公网就必须再加一层反代认证或 IP 白名单。

**4. 它会存下攻击者提交的凭证明文，而且默认不会过期。** 我在本地数据库 `credential_attempts` 表里直接看到了 `admin / Passw0rd123`。撞库数据里很可能有真实用户的密码。`retention.non-suspicious` 的 30 天只管访问日志、检测和请求资产，**不管凭证**；凭证只有在显式设置 `retention.overall` 时才会被一起删，而这个开关默认是关的。也就是说，这些数据默认一直留着。留存期、访问控制、脱敏、以及能不能给第三方看，都要你自己定。

**5. 默认诱饵页所有安装都一样。** README 自己提醒要替换。假 `.env` 里的 `APP_KEY`、假 AWS Key 都是固定模板，攻击者见多了就会认出来。

**6. robots.txt 主动列了 30 条敏感路径。** 这是诱饵设计，不是失误；但别把蜜罐挂在你希望被索引的站点上，否则搜索引擎也会把这些路径当真实内容。

**7. tarpit 对所有人生效。** 前面说过，不再重复。

**8. 规则只能证明"有人在探"，不能证明"有漏洞"。** 98% 的规则是 medium 置信度，别拿它当漏洞扫描器的结论。

**9. banlist 联邦要谨慎。** 它支持把别人的 IP 名单拉进来合并（`banlist.sources`，默认 3600 秒刷新一次），也支持把自己的名单公开出去（`export_path`）。拉别人的名单等于信任别人的判定，误封的风险由你承担。

**10. 别和真实业务放同一台机器。** 蜜罐会被打、会被扫、会存一堆攻击者上传的文件（它会把上传文件按 TLSH 模糊哈希聚成"战役"）。这些东西都不应该和业务共享文件系统、共享网络、共享凭证。

## 九、适合谁

适合：有自己的域名和公网 IP 的蓝队、想看清"谁在扫我"的自建站站长、做蜜罐研究或教学的人、以及想把 AI 爬虫挡在真实站点外面的团队。

不适合：把蜜罐直接挂在生产业务站上的人、没有独立域名和隔离网络的人、指望它输出"漏洞报告"的人、以及不愿意处理攻击者上传文件和凭证数据的人。

## 十、最后

Krawl 的价值不在"抓了多少攻击"，而在它把"谁在探、探什么、用什么规则、从哪个 IP 来"变成了可以查询、可以聚类、可以导出的证据链。它的风险也不在代码里，而在你把它放在哪里：...