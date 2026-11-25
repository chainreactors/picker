---
title: 【安全运营】SIEM 规则建设
url: https://mp.weixin.qq.com/s/VNa899ma6iRp9I_Ysy6YOA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:42:28.946952
---

# 【安全运营】SIEM 规则建设

# 【安全运营】SIEM 规则建设

原创

AlanHR
AlanHR

白帽少年

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

前五篇把平台搭起来了：SIEM 收全网日志，主机层有 osquery 和 syscheck，Web 层有 ModSecurity 拦截，业务层有 demo-crm 的 JSON 日志。但从这一篇开始才真正进入 SIEM 的核心工作——规则建设。平台只是管道，规则才是大脑：决定哪些日志值得变成告警、告警有多严重、以及不同来源的信息怎么互相印证。

这一篇先讲清楚两件事：一是告警规则的方法论——为什么规则要按"事件"而不是按"日志"来设计；二是基于本套方法论设计符合当前数据的的规则。然后用七条规则把设计做出来，全程经过语法校验、logtest 验证和真实攻击触发。

## 一、方法论：告警按"事件"设计，而不是按"日志"

先明确一个概念转换。日志是"发生了什么"的原始记录，一条日志只是历史库里的一行；而事件是安全视角下对日志的解读——"谁、在什么条件下、做了什么、严重到什么程度"。SIEM 规则建设的本质，就是把日志流加工成事件流的流水线，告警则是事件的载体。

按事件维度设计规则，我总结为四层结构，对应事件的完整生命周期：

第一层：单事件识别。一条日志能否独立构成一个低级别事件？比如一次命令执行页的访问、一次登录失败。这一层的规则等级通常不高（5~6 级），作用是留痕和打标签——它不追求告警响度，追求的是后续所有分析的原料。

第二层：事件聚合升级。单条日志不可疑，但同一行为在时间窗口内累积就可能构成事件升级：同一 IP 反复访问敏感接口是扫描，反复提交登录是爆破。聚合维度一般选"行为 + 来源 + 时间窗口"三要素，这层的规则才产生真正的高危告警。

第三层：跨事件关联。单一数据源看到的事件往往只是碎片——主机层看到一次失败登录，Web 层看到一次拦截请求，各自都不算大事。但把它们按攻击者视角串起来（同一来源、时间上递进），就是一条完整的攻击链。关联规则是 SIEM 区别于单点设备的最大价值。

第四层：业务上下文定级。同样的技术行为，发生在不同业务上下文里严重性完全不同。测试环境的登录失败没人想半夜爬起来看，生产环境的登录失败则值得立刻关注。用业务标签调整告警等级，让分级反映业务重要性而不只是技术特征。

这四层不是四种孤立的规则，而是同一类事件在不同维度上的加工阶段。设计规则集时，先选好要检测的事件类型，再逐层问自己：识别条件是什么、聚合窗口多大、能不能跨源印证、业务上该多重——一条完整的事件设计就出来了。

## 二、数据源

方法论要落地，先盘清环境里有哪些数据源、每个数据源能看到什么。这是规则设计的起点——没有数据源支撑的规则写得再漂亮也是空转。

| 数据源 | 所在节点 | 内容 | 能支撑的检测 |
| --- | --- | --- | --- |
| Apache access log（dvwa\_access） | waf | 全部 HTTP 访问，含 URL、状态码 | Web 扫描、爆破、敏感接口访问 |
| Apache error log + ModSecurity | waf | WAF 拦截详情（规则 ID、载荷） | Web 攻击被拦截、攻击载荷特征 |
| auth.log / syslog | waf、edr | SSH 登录、sudo、账户行为 | 主机层爆破、伪用户探测 |
| demo-crm 业务 JSON 日志 | waf | 带业务标签的登录失败等事件 | 业务事件频次、环境分级 |
| osquery / syscheck | edr | 进程、文件完整性 | 主机层异常（后续篇目展开） |

把这些数据源和第一节的四层结构对上，规则设计的思路自然浮现：access log 支撑"识别 + 频次升级"，auth.log 和 ModSecurity 分属主机层、Web 层，天然适合做跨源关联；业务 JSON 日志自带环境标签，是第四层定级的理想输入。最终落到纸面上的就是这套七条规则：

| 规则 | 类型 | 触发条件 | 等级 | MITRE |
| --- | --- | --- | --- | --- |
| 100800 | 敏感接口识别 | 访问 /vulnerabilities/exec（命令执行功能页） | 6 | T1059.004 |
| 100801 | 频次升级 | 同一 IP 2 分钟内命中 100800 五次以上 | 12 | T1595 |
| 100810 | 登录请求识别 | POST /login.php | 6 | — |
| 100811 | 频次升级 | 同一 IP 2 分钟内命中 100810 八次以上 | 12 | T1110 |
| 100820 | 多源关联 | 先有 5710（SSH 伪用户探测），10 分钟内同源 IP 的 Web 攻击被 WAF 拦截 | 13 | T1595 |
| 100830 | 等级上调 | demo-crm 登录失败且带生产环境标签 | 14 | — |
| 100831 | 等级下调 | demo-crm 登录失败且带测试环境标签 | 3 | — |

几个设计取舍值得说明。频次类规则都是"识别 + 升级"两层：下层等级不高，每次访问都留痕，行为累积到阈值才升级为高危告警——单条日志不刷屏，攻击行为不漏报。阈值不是拍脑袋：登录爆破定 8 次，因为正常用户输错密码两三次很常见，定 8 次基本不误伤真人；敏感接口定 5 次，因为正常用户几乎不会反复访问命令执行页，可以收得更紧。100820 是这套规则里最有意思的一条：它同时引用主机层的 SSH 探测告警（Wazuh 内置 5710）和 Web 层的 WAF 拦截告警（前面 1006 系列写的 100630），两个完全不同的数据源通过同一攻击源 IP 串起来——单台设备各自看都是"一次小动静"，合在一起就是一条侦察攻击链。等级调整类复用了上一篇给采集项打的 app\_env 标签，同样的登录失败，生产标签上调到 14，测试标签降到 3。

![](https://mmbiz.qpic.cn/mmbiz_png/XW2mcarl9vgqyxflPj5ohP6Zr1kb6q7D3Lo31ZagkeEApVa3RlRu5F2rPSjQibrh84zPe76hyaFnnkjeCnJiakv08KDutPSaMT3p7u1X4bS1o/640?wx_fmt=png&from=appmsg)

## 三、编写与校验

规则文件部署在 siem 的 /var/ossec/etc/rules/1008-soc-lab\_rules.xml。写完先过 wazuh-analysisd -t 语法校验，再重启 manager 加载。加载是否成功有个可靠的核对方法：ossec.log 里每次 analysisd 启动都会输出 "Total rules enabled"，加规则前后对比数字差即可——这次从 8479 涨到 8486，正好七条。

![](https://mmbiz.qpic.cn/mmbiz_png/XW2mcarl9viaZJuaBOojN0SvibNkVVwQJlVPYQd6DMOe3hrG0tIZubAc5Nbu7Nicz6rQIVSibYxzf01bHfJxbYoVS46lQYOY1hJtdzz0wZYZ3qQ/640?wx_fmt=png&from=appmsg)

接下来是本篇最值得记录的部分：规则加载成功、语法完全正确，但触发测试时就是不告警。

第一轮实测，敏感接口和爆破场景都没有产出告警，只有关联规则正常触发。排查从三个方向同时收窄：agent 侧的 logcollector 状态文件确认 dvwa\_access.log 的事件全部读出、0 丢弃，事件确实送到了 manager；manager 侧 alerts.json 里，同批日志命中了内置规则 31164（SQL injection attempt），说明解码链路完全正常；把真实日志行喂给 wazuh-logtest，内置 31164 照样命中，我的规则依旧沉默。

最后对比规则结构找到了原因：能触发的 31164 是 if\_sid 挂在 31100（Access log messages grouped）之下的子规则，而我的规则是没有挂靠的根规则。Wazuh 的规则引擎按"父规则 → 子规则"的树来评估日志——日志一旦在 31100 这个分支命中，评估就沿着这棵子树走下去，同层排在后面的根规则根本没有机会被评估。所以给已解码的日志写规则，正确姿势不是写成根规则，而是挂到对应解码树的父规则下面：

```
/var/log/apache2/dvwa_access.log  GET /vulnerabilities/exec   31100  ^/vulnerabilities/exec
```

改完敏感接口规则立刻生效。但爆破规则还是不响，第二个坑接着浮出来：用 logtest 喂真实的 POST /login.php 日志，命中的是内置规则 31108——"Ignored URLs (simple queries)"，login.php 在 Wazuh 内置的忽略清单里，level 0，它作为 31100 的子规则排在我前面，把整个分支"吃"掉了。既然分支已经走到 31108，那就把爆破规则挂到 31108 之下：

```
31108  POST /login.php
```

这两个坑指向同一个教训：Wazuh 写规则，先搞清楚目标日志会被哪条内置规则接住，再把自定义规则挂进同一条链路里，而不是想当然写成独立规则。排查不触发问题时，logtest 加"内置规则先命中了谁"这个视角，比反复检查自己的正则有效得多。

规则定稿后，先用 logtest 把最复杂的关联链路验证一遍——它不落库，能在控制台上把整条链走给你看。先喂一条 SSH 伪用户登录日志，命中内置 5710（level 5）；再喂一条同源 IP 的 ModSecurity 拦截日志，100820 直接命中（level 13），"先前发生过 5710 + 当前事件是 WAF 拦截 + 同源 IP"三个条件全部按预期工作：

![](https://mmbiz.qpic.cn/mmbiz_png/XW2mcarl9vhdpR8iaARiag9GlRaicliafJA9JRYibUzkXLqzKh9TicYlgQDK2jdYyoyEcCWtJC4Bf6oEibIZyofGlkdaicLibNNxaoRSpe7M9lDn8jcU/640?wx_fmt=png&from=appmsg)

## 四、准备测试环境：给等级调整规则铺路

100830/100831 靠 app\_env 标签区分业务环境，上一篇只给 audit.log 配了生产标签，所以先给 waf 的 agent 补一个测试环境采集项：新增 /var/log/demo-app/audit-test.log 的 localfile，标签 key 为 app\_env、值为 demo-crm-test。改配置前备份、改完校验 XML 合法性、重启后必须在 ossec.log 里看到 Analyzing file——这套流程上一篇吃过亏，这次直接按标准动作执行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XW2mcarl9vjU8LJ0J0rGiaY95unDeCA2QfUIJklaG9fmYMQFhmHguEY9COYELBJAyTZYhZKlTGU680WK7qhGicSGHbHKAsibvI21lS5IW0MuAU/640?wx_fmt=png&from=appmsg)

另外有个插曲值得记一笔：第一轮触发时所有场景颗粒无收，最后发现是 agent 重启后没有重新连上 manager（systemctl 显示 inactive），事件全卡在这一层。把 agent 拉起、确认 "Connected to the server" 之后一切正常。这也解释了为什么巡检时 agent 状态要看到连接日志才算数。

## 五、实战触发

触发全部从 edr 节点发起，模拟真实的外部攻击者视角；等级调整场景从 waf 本地写入业务事件。

### 场景 A：敏感接口高频访问

对 DVWA 的命令执行功能页连续发起 10 次请求，每次间隔 2 秒：

![](https://mmbiz.qpic.cn/mmbiz_png/XW2mcarl9vgDDUSeykLzppkHGibq6H418HozVbXsTnkNyWv3iaqXggX0v7yYK9YUj1QCvkl67FY0qWTnicUBFibngjqT3ILyNN9xQmI6qG0ic9Ag/640?wx_fmt=png&from=appmsg)

命中情况符合设计：前几次只产生 level 6 的识别告警，第 6 次开始频次规则 100801 升级为 level 12，并挂上 MITRE T1595（Active Scanning）。Discover 里查 rule.id: 100801，16 条升级告警（含本轮与前几轮触发）时间线清晰，来源 IP 都是 192.168.202.130：

![](https://mmbiz.qpic.cn/mmbiz_png/XW2mcarl9vhtvYF6C1PDrqyic4NibKhziagm9R2zI8yRpicg1DTiaZF6rKb2riavDe4PjiawNVpyP80TfObouQTqbMpBSPVbOfu5CazoYibjmd5Ticibo/640?wx_fmt=png&from=appmsg)

### 场景 B：Web 登录爆破

对 /login.php 连续 POST 12 次错误口令：

![](https://mmbiz.qpic.cn/mmbiz_png/XW2mcarl9vgnOicbakJIXYHfuKFia5MCn3mQdB6D6XUP7efwdYHFPOYE4cMsjiamIplibYCUFKmMiaDXjHuCCmia9z5fjwIDzH11kWgV9icwCuXv38/640?wx_fmt=png&from=appmsg)

2 分钟窗口内 100811 升级告警正常产出（level 12，T1110 Brute Force）。这里能看出频次阈值设计的取舍：正常用户输错密码两三次很常见，阈值定 8 次基本不会误伤真人；真要漏过了，还有下一层的聚合告警兜底。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XW2mcarl9vjPbibsVV1xcmd9Rv55UicoSSnQTGRf17GG9HBhPwx5ibqibp1gKib5sYCkhzRlZwUs8ZpXnN0vf8AGu4h2nqnstgR0pqXVeLrXFMpg/640?wx_fmt=png&from=appmsg)

### 场景 C：跨数据源关联

这是整套规则的核心验证。两步操作，间隔几秒：先从 edr 对 waf 发起一次 SSH 伪用户登录尝试（noscanuser，必然认证失败，产生 5710），再用同一台机器对 DVWA 发一条 SQL 注入载荷，被 ModSecurity 拦截返回 403：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XW2mcarl9vgtkkcfxbXAaZ2K0sVGBic0mjjTpoS5QA3bWic6uVkFbvM155sG80T1XEoq4ngW3xNec6NpWW1jWUqXxfyGxgJQSazYdoK5qsSCg/640?wx_fmt=png&from=appmsg)

单独看，第一步只是主机层一次普通的失败登录，第二步只是 WAF 一次例行拦截——两台设备各自的视角里都没有什么大事。但 100820 把它们串成了链：同一 IP 在 10 分钟内先探测 SSH 再打 Web，level 13 告警直接给出攻击链描述。Discover 里展开这条告警，agent.id 002、srcip 192.168.202.130、解码器 apache-errorlog，链路信息完整：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XW2mcarl9viaKMbo5vYS0R9pc2HzswUcG5HPkI7R001XKvBmjkPDUqgGUgBNGVynr9pJSccicZJKLqr1BEsn1QqmlEvrpichO4lwNJzLqCmmia8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XW2mcarl9vguDZdvXUeryFnUlLALXLhOtPeBfLt50g5XSfPUMTrZlPZCLny6r8lsn0qbn4NW1SnVibYMxeGyOsBHPrLkQbDaN8x7teWbUUx8/640?wx_fmt=png&from=appmsg)

### 场景 D：业务重要性等级调整

同一类登录失败事件，分别写进生产标签和测试标签的日志文件，srcip、attempts 完全相同：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XW2mcarl9vjytiaKlyyxgbYibq5tIep8r0tCRyBroxfQjooqZ15bL5iaUkL212kMBcvAlcDRNCqX8Erx2rPCrkRxniaGo7Rahw54hzib4qVlXEc0/640?wx_fmt=png&from=appmsg)

结果就是 100830/100831 设计意图的直接展示——同样的登录失败，生产环境告警 level 14，测试环境 level 3，data.app\_env 列的值一眼可辨：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XW2mcarl9vgmr4uD93FcUjcYw6WZYgjxl28poYl8m8ZuxeiaIOMKN2KEECWHlCqzX4ibkiaPd90jics49DGzEVdzs1xQRHjDsUDFxegkkLGlxJo/640?wx_fmt=png&from=appmsg)

实际运营里这就是降噪的手段：测试环境的登录失败降到 3 留痕，既不进高危清单，检索时也还在。

## 六、落库核对

四个场景跑完，回到 manager 侧对告警做一次总核对。alerts.json 里七条规则的累计命中统计：100800×64、100801×16、100810×88、100811×8、100820×9、100830×9、100831×9——数字是多轮触发叠加的结果，识别类告警量与请求轮次对应，频次和关联类各触发数轮，量级关系都能解释得清。

![](https://mmbiz.qpic.cn/sz_mmbi...