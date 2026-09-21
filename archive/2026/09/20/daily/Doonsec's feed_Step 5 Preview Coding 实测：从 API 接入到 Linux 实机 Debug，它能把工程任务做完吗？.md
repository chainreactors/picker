---
title: Step 5 Preview Coding 实测：从 API 接入到 Linux 实机 Debug，它能把工程任务做完吗？
url: https://mp.weixin.qq.com/s/oWcgGXb_0UQqbZEpE2MS5w
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:25:44.016808
---

# Step 5 Preview Coding 实测：从 API 接入到 Linux 实机 Debug，它能把工程任务做完吗？

# Step 5 Preview Coding 实测：从 API 接入到 Linux 实机 Debug，它能把工程任务做完吗？

原创

z释然z
z释然z

释然IT杂谈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

最近拿到了阶跃星辰Step 5 Preview的内测资格。

这次我没有先去跑各种榜单，也没有用“写个排序算法”“解释一下 Linux Load”这种题目来判断它的 Coding 能力。

除了能力，这次我也顺手关注了一下它在多轮 Coding 任务里的成本表现，后面一起看。

我更想测一个实际问题：

> 给 Step 5 Preview 一个完整的 IT 工程任务，从需求理解、方案设计、代码生成，到 Linux 实机运行、报错修复和最终验收，它能不能真正把事情做完？

所以这次测试全部放在真实 Linux 环境里完成。

测试链路如下：![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhYQ7dsFWwrMia5VFf0uNM05P9C7VNMf1iaAia1qRFHyEvXhEHlQTAQMORujtVHAB9YxeDCCSv5vV8LmbUB7lY68P7q3gXpdBXBGrY/640?wx_fmt=png&from=appmsg)

相比单纯看模型“会不会写代码”，我更关注：

**第一版能不能跑、需求有没有漏、遇到错误会不会修、修完会不会引入新问题，最终到底能不能交付。**

# 一、先确定这次到底测什么

本次测试对象是：

```
Step-5-Preview
```

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhana5qo6H7jPnrvsiaK7zcVGsmutibcfWibXeibEeVcGINxmfcZzxEzqV50gtMsFxraReX3OaMM7r7BI4vFgichP9SIj0zRC2gVicwHc/640?wx_fmt=png&from=appmsg)

测试任务也尽量贴近日常运维和安全工作：

> **从零开发一个 Linux SSH 安全日志分析工具。**

最终目标：

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhYtY7TxdnQxPamZ8eibTX1xkapmQiaB4aCAWckzHC6NrQKrynXH1Bne83iccbicbotxrHZgKYxUN6COicC59Ru1s7e4TqwZ92oasflo/640?wx_fmt=png&from=appmsg)

这个项目不算复杂，但涉及的东西不少：

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhbat5HBxdEbQcjD5eWia7A7C9OW7t0vCic6ooHuddkZwiaSzFyeHMofc0LnrFVOvl7fCR2YHA5JqR1v2cu8vUOyNrHCICGiaMajiaOA/640?wx_fmt=png&from=appmsg)

也就是说，这次测试的并不只是 Python。

还包括：

+ Linux 实战能力

+ 需求理解

+ CLI 设计

+ API 调用

+ 安全意识

+ 异常处理

+ Debug

+ 工程交付

这也是我选择这个任务的原因。

# 二、测试环境先准备好

为了让整个测试过程能够留档，我单独建了一个目录。

```
mkdir -p ~/step-5-preview
cd ~/step-5-preview
```

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhZTxf7Yh0weT8ExOA2y49ytppibib7yhU3Pmea2wHUELU6HWdwRfcbcOG3ickLZicORMe2yukNEn7eNiaZhgichePs3EDL5vN4gnFuP8/640?wx_fmt=png&from=appmsg)

最终整个目录会逐渐变成：

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhYZyYQCXRdehPGh8Wa02YuRBsxRpZVkEN3KicBjGOtWyGqgokAKsnhiaxbic3NtdB9yfJSePX34w2aquu3Hfzlr0cgOfjURejbrcg/640?wx_fmt=png&from=appmsg)

这样后面每一次请求、每一轮返回、每一次修改和最终报告都能留下原始记录。

# 三、第一步：先把 Step 5 Preview API 跑通

先配置 API Key。

这次统一使用：

```
STEP_API_KEY
```

设置：

```
export STEP_API_KEY="你的真实API_KEY"
```

确认环境变量已经存在：

```
echo "${STEP_API_KEY:+STEP_API_KEY 已设置}"
```

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhaibb3icjwZTyd5BEDt5pVtXjev1ic1IxqSqC7YP6FocbdOibhQ8AQQaBnkbccBax02paP2aicibibrqOuxs1BUFb8EVoXfHyrbb48vLE/640?wx_fmt=png&from=appmsg)

正常应该看到：

```
STEP_API_KEY 已设置
```

这里不建议直接：

```
echo $STEP_API_KEY
```

避免完整 Key 出现在终端截图或者测试记录中。

先做一次最简单的 API 调用

```
curl https://api.stepfun.com/v1/chat/completions \
  -H "Authorization: Bearer ${STEP_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "step-5-preview",
    "messages": [
      {
        "role": "user",
        "content": "你好，请介绍一下你自己"
      }
    ]
  }'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FxDqdf0BMhY46EDD9j7h8W58ibrRSb776QWQ7tx6Rua2949ANxr7mL9zjITU4gbQTicKseFyJO2ItoMkXhJzLx5AO2aZj5icW7KJb1YSX5f4p8/640?wx_fmt=png&from=appmsg)

这一轮我不评价模型能力。

只确认：

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhanuIXRbAwF72HVur63vxE0Nt6rqh5NY5peAZmKLibCDzbliaPOj6kzzQ2ojnn99QbTXw2rITjSlRWiajrFaFx3XZ6ibWK415RBHrk/640?wx_fmt=png&from=appmsg)

是不是正常。

只有基础链路稳定，后面的 Coding 测试才有意义。

# 四、长 Prompt 不再直接塞 curl

到了正式 Coding 测试，需求已经不是一句话了。

如果直接把几百行 Prompt 塞进：

```
curl -d '{ ... }'
```

很容易因为：

```
换行
双引号
反斜杠
特殊字符
终端粘贴
```

破坏 JSON。

我实际测试时就遇到了：

```
invalid request format
```

所以正式测试改成：

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhbcG5obfX29hBaJicYMaLqauwedyfrkWjD1bRib8WJqxXcDMCPF3DYvXlIHicYurJZKc1LYcEqErnhaYhiaib4q3FljL4XesRib6yQ9E/640?wx_fmt=png&from=appmsg)

这套方式稳定很多。

# 五、把完整需求保存成 prompt.txt

执行：

```
vi prompt.txt
```

这次我不会简单告诉 Step 5 Preview：

> “帮我写个 SSH 日志分析工具。”

而是直接给完整工程需求。

核心内容如下：

```
你现在是一名 Linux 系统运维工程师、安全工程师和 Python 开发工程师。

我正在一台真实 Linux 测试机上测试你的 Coding 能力。

你的任务是从零开发一个：

Linux SSH 安全日志分析工具

项目文件名：

ssh_analyzer.py

====================
一、测试协作方式
====================

你无法直接操作我的 Linux 终端。

你负责：

分析需求；
设计程序；
编写代码；
给出需要执行的 Linux 命令；
根据我返回的真实执行结果分析问题；
如果程序报错，根据错误继续修改；
持续迭代直到关键测试通过。

我负责：

在真实 Linux 环境执行你给出的命令；
将终端输出和报错原样返回给你；
按修改后的代码重新测试。

不要假设命令已经执行成功。

没有看到我的真实终端输出前，
不要宣布项目已经完成。

====================
二、项目目标
====================

实现以下流程：

Linux SSH 日志
→ 本地脚本预处理
→ 筛选关键 SSH / sudo 安全事件
→ 调用 step-5-preview API
→ 生成 Markdown 安全分析报告
→ 运维人员人工复核

====================
三、运行环境
====================

Linux

Python 3.8+

优先使用 Python 标准库。

如果必须使用第三方库，
请说明原因并给出安装命令。

====================
四、Step 5 Preview API
====================

模型：

step-5-preview

API：

https://api.stepfun.com/v1/chat/completions

API Key 必须从环境变量读取：

STEP_API_KEY

禁止：

将 API Key 硬编码进源码；
将完整 API Key 写入日志；
在错误信息中泄露完整 API Key。

====================
五、日志输入
====================

支持两种模式：

--file

读取指定日志文件，例如：

python3 ssh_analyzer.py \
  --file /var/log/auth.log

--last

读取最近 N 分钟 SSH 日志，例如：

python3 ssh_analyzer.py \
  --last 30

通过 journalctl 获取。

--file 和 --last 必须互斥。

====================
六、日志预处理
====================

不要把完整 auth.log 直接提交给模型。

先在本地筛选：

Failed password
Accepted password
Accepted publickey
Invalid user
sudo

尽量保留：

时间
主机名
用户名
来源 IP
认证结果
sudo 命令

如果没有相关事件：

输出：

未发现需要分析的 SSH / sudo 安全事件

然后退出。

不要调用 stpe-5-preview。

====================
七、安全分析
====================

分析结果固定输出：

【事件时间线】

【已确认事实】

【待验证风险】

【风险等级】

【排查建议】

【推荐 Linux 命令】

必须遵守：

Failed password 不等于已经入侵；

Accepted password 不等于攻击者登录；

sudo 不等于恶意提权；

crontab -e 不等于已经植入后门；

必须区分事实、推测、待验证项；

证据不足必须明确说明。

====================
八、命令行参数
====================

支持：

--file
--last
--output

必须支持：

python3 ssh_analyzer.py --help

====================
九、Markdown 报告
====================

报告至少包含：

# SSH 安全日志分析报告

## 基本信息

## 事件时间线

## 已确认事实

## 待验证风险

## 风险等级

## 排查建议

## 推荐命令

====================
十、异常处理
====================

必须处理：

日志文件不存在；

STEP_API_KEY 未设置；

--last 不是整数；

空日志；

没有相关安全事件；

journalctl 执行失败；

API 超时；

HTTP 401；

HTTP 403；

HTTP 429；

HTTP 5xx；

API 返回异常 JSON；

--file 和 --last 同时出现。

不能直接把 Python Traceback
作为最终处理结果。

====================
十一、安全边界
====================

程序只负责：

读取日志；
筛选日志；
分析日志；
生成建议。

禁止自动：

封禁 IP；
删除账号；
修改 SSH；
修改防火墙；
修改 crontab；
重启服务器；
删除文件；
执行模型返回的命令。

所有处置由人工确认。

====================
十二、开发流程
====================

第一步：

先分析需求。

给出：

程序结构；
模块划分；
日志获取方式；
参数设计；
API 调用方式；
异常处理方案。

现在不要写代码。

等我确认后再进入下一阶段。

后续要求：

生成第一版代码；
进行 Python 语法测试；
测试 --help；
测试真实日志；
检查 Markdown；
测试异常场景；
真实报错后继续修改；
关键测试通过后再宣布完成。

现在只执行第一步：

分析需求并给出开发方案。

不要直接开始写代码。
```

这里有一个关键点：

> **第一轮故意不让 Step 5 Preview 写代码。**

我要先看它怎么理解需求。

# 六、先测需求理解，而不是急着看代码

完整需求发出去后，我第一轮主要检查 Step 5 Preview有没有主动拆出：

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhalfClCB5uWGbghliaKAwJSkwTjIEmOQxIEdqxqataW0lsFJ2JOq8ccyPzotBFa6xlXzajRfwsuqahGuic919SuiaWC9GUE22Gcy0/640?wx_fmt=png&from=appmsg)

同时观察它有没有注意到：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FxDqdf0BMhZ1pCxsjJv342wdiayYuAlricPIiaNVmVsR4kEH64kbGYCIxImy0F8Syd1WhdPicQzsVsAYsrJ2IzLpkJcDv0AaU3BxGATox6S5K7g/640?wx_fmt=webp&from=appmsg)

如果这些关键约束在方案阶段就漏掉，后面即使一次输出 500 行代码，我也不会认为需求理解表现很好。

# 七、生成合法 JSON 再调用

先安装 `jq`：

```
sudo apt update
sudo apt install -y jq
```

把 Prompt 转成 messages：

```
jq -n \
  --rawfile prompt prompt.txt \
  '[
    {
      "role": "user",
      "content": $prompt
    }
  ]' > messages.json
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FxDqdf0BMhbTzo9icog0cJ3okINvtKXvISa6mCudDZuFjBkImCVwJFyxqkTd6NlrY127lI753T0pwlKrQ3KPE4aMvM4UJibTclqPoIbjsLHPY/640?wx_fmt=png&from=appmsg)

再生成 API payload：

```
jq -n \
  --slurpfile messages messages.json \
  '{
    model: "step-5-preview",
    messages: $messages[0]
  }' > payload.json
```

先验证：

```
jq empty payload.json
```

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhZUibQC48WovicQjLibUIw2d0OdkGjXD8pQZLHN4G7APaAeLNDXWncLKbXhhRYkNKXbXRah2otcJPz02PKC5ib3yHxxSZLSWYBFkibo/640?wx_fmt=png&from=appmsg)

没有输出，就说明 JSON 格式正常。

# 八、第一次正式调用，同时记录性能数据

执行：

```
curl -sS \
  -o response_01.json \
  -w '\nHTTP_CODE=%{http_code}\nTIME_TOTAL=%{time_total}s\nSIZE=%{size_download} bytes\n' \
  https://api.stepfun.com/v1/chat/completions \
  -H "Authorization: Bearer ${STEP_API_KEY}" \
  -H "Content-Type: application/json" \
  --data-binary @payload.json
```

![](https://mmbiz.qpi...