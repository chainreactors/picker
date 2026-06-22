---
title: 别一条条看了！我把Burp流量全喂给AI，自动标出越权漏洞
url: https://mp.weixin.qq.com/s/18n9iv7uMZ40-WkW63-SnA
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:14:14.022787
---

# 别一条条看了！我把Burp流量全喂给AI，自动标出越权漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3oR6eMARh6ymcDhUbE4NUiahiaQk6fXyMqHNDicqhJAQUf5ELd8QwicHE7fD6sg65ykode7NsMcWvqgO7SRaRJUyLfLicnickPRVSsc5jwuNmiaql4/0?wx_fmt=jpeg)

# 别一条条看了！我把Burp流量全喂给AI，自动标出越权漏洞

昆仑AI安全实验室
昆仑AI安全实验室

昆仑AI安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以前挖越权，我趴在Burp的Proxy History里一条一条手工审：改用户ID、换Cookie、比较响应包。一个中等规模网站的流量，两三千条请求，看一遍少说三四个小时，眼睛盯瞎了还经常漏。

后来我写了个Python脚本，把Burp导出的一整包流量自动拆开，扔给DeepSeek（用本地Ollama也行），让AI逐条判断是否存在越权嫌疑。现在跑一个目标半小时出结果，命中率比手工高了至少一倍。

这篇文章把我这套“Burp+AI”自动越权扫描方案完整拆开，从工具到脚本到Prompt，全部可复现。

**一、手工挖越权为什么又慢又漏**

越权漏洞的本质是：同一个API接口，不同权限的用户请求，返回的数据应该不同。但手工测试有几个致命的效率瓶颈：

* **请求太多**：一个普通Web应用，随便点几下就几百条请求。一条条改参数重放，工作量指数级。
* **上下文易断**：手工改ID只能改数字，遇到UUID、哈希串、Base64编码的复合参数，没法系统性地替换测试。
* **判断标准模糊**：两个响应包内容不同，但到底是因为权限不同，还是因为数据本身就是动态的（比如时间戳、随机Token）？手工很难快速甄别。
* **组合场景难覆盖**：水平越权和垂直越权经常同时出现，还有跨模块的越权（A模块的接口被B模块的用户调用）。人工一次只能测一个点。

Autorize这类Burp插件可以自动替换Cookie重放，但它只做请求替换和响应比对，缺乏对业务逻辑的理解——比如它不知道某个参数是用户ID，也不认识UUID编码，更无法判断返回包差异的业务含义。

**二、AI凭什么能自动挖越权？**

大语言模型最大的优势是语义理解。它能从请求URL、参数名、参数值、响应内容中提取出“这个接口是干嘛的”，然后做出人类级别的判断：

* **识别身份标识参数**：AI看到`userId=10086`，知道这是用户ID。看到`orderSn=ORD20240101XXXX`，知道这是订单号。它不靠正则，靠语义。
* **理解响应差异的业务含义**：两个响应包都是200，内容不同。AI能读出“第一个响应里name是张三，第二个响应里name是李四”，从而判断发生了水平越权。
* **处理复杂编码**：UUID、JWT、Base64图片、URL编码，AI都能“看懂”里面是什么，并且知道该怎么替换测试。
* **生成越权测试用例**：AI可以自动构造替换后的请求参数（如修改ID、删除Token），甚至写出验证脚本。

简单说，AI相当于一个24小时不休息、永远不怕漏看的安全实习生。

**三、整条流水线怎么搭：从Burp流量到越权报告**

我的方案分三步走：导出Burp流量 → Python脚本预处理 → 分批喂给AI分析。

**第一步：导出Burp流量**

在Burp的Proxy History或Target -> Site map中，选中你要测试的目标域名，右键 -> Save selected items，导出为XML文件（包含Request和Response）。或者直接用Burp的REST API（需要Pro版）实时拉取流量。

推荐用XML导出，因为完整保留了请求和响应的原始字节。关键标签：`<request base64="true">`和`<response base64="true">`。Python脚本需要Base64解码这些内容。

**第二步：Python预处理脚本**

脚本负责三件事：解析XML提取请求/响应对，过滤掉静态资源（CSS、JS、图片等），把每对请求/响应格式化为便于AI阅读的文本。

核心逻辑示例：

```
import xml.etree.ElementTree as ETimport base64import json
def parse_burp_xml(xml_path):    tree = ET.parse(xml_path)    root = tree.getroot()    items = []    for item in root.findall('.//item'):        url = item.find('url').text        # 过滤静态资源        if any(url.endswith(ext) for ext in ['.css','.js','.png','.jpg','.ico','.svg','.woff']):            continue        req_elem = item.find('.//request')        resp_elem = item.find('.//response')        if req_elem is None or resp_elem is None:            continue        req_bytes = base64.b64decode(req_elem.text) if req_elem.get('base64') == 'true' else req_elem.text.encode()        resp_bytes = base64.b64decode(resp_elem.text) if resp_elem.get('base64') == 'true' else resp_elem.text.encode()        items.append({            'url': url,            'method': req_bytes.split(b' ')[0].decode(),            'request': req_bytes.decode('utf-8', errors='ignore')[:3000],  # 截断            'response': resp_bytes.decode('utf-8', errors='ignore')[:3000]        })    return items
```

**第三步：AI批量分析**

把预处理后的流量分批发给AI，每批10-20条请求（取决于token限制）。Prompt设计是关键：

```
你是一名资深渗透测试工程师，擅长发现越权漏洞（IDOR）。现在给你一组HTTP请求和响应，请逐一分析，找出可能存在越权风险的接口。
分析标准：1. 请求参数中是否包含身份标识（如userId、uid、orderId、cardId等）？参数值是否可预测（纯数字、简单递增）？2. 请求中是否有身份认证信息（Cookie、Authorization头）？如果同一个用户对不同的资源ID请求，响应中包含不同的用户数据，可能存在水平越权。3. 如果某个接口看起来应该只有管理员才能访问（如/admin/、/manage/），但普通用户的请求也能成功，可能存在垂直越权。4. 响应内容中是否包含明文敏感信息（身份证、手机号、家庭住址、密码）？
请用JSON格式返回分析结果，每条潜在漏洞包含以下字段：- url: 请求URL- method: HTTP方法- risk: 风险评估（高危/中危/低危/无风险）- analysis: 分析说明- suggestion: 测试建议（如“替换uid参数为1001尝试获取其他用户数据”）
输入数据：{requests_data}
```

调用AI API：

```
import requests
def analyze_traffic(requests_list):    prompt = build_prompt(requests_list)  # 构建完整Prompt    response = requests.post(        'https://api.deepseek.com/v1/chat/completions',  # 可换成Ollama本地接口        headers={'Authorization': 'Bearer sk-xxx'},        json={            'model': 'deepseek-chat',            'messages': [{'role': 'user', 'content': prompt}],            'temperature': 0.1,            'response_format': {'type': 'json_object'}        },        timeout=120    )    return response.json()['choices'][0]['message']['content']
```

脚本跑完后，把AI返回的JSON汇总，按风险等级排序输出。我用这套流程分析一个中型电商站点的6000条流量，AI标出了23条疑似越权，人工验证后确认12条真实漏洞，耗时不到40分钟。换做手工，至少两个下午。

**四、真实案例：AI怎么找到我漏掉的越权**

某次SRC测试一个在线教育平台，我手工翻了半天API，只找到一个学生查看自己成绩的越权（改studentId可看他人成绩），中危。后来我把当天Burp导出的所有流量扔进AI，它额外揪出了三个我漏掉的洞：

* **水平越权：查看他人合同** — 接口`/api/contract/preview?contractId=550e8400-e29b-41d4-a716`，contractId是个UUID。手工测到UUID通常就放弃了，觉得不可遍历。但AI指出这个UUID在另一个接口`/api/course/list`的响应中以`course.contractId`的形式返回，而且courseId是可遍历的数字。AI建议“先遍历courseId获取所有contractId，再逐一遍历合同内容”。一套组合拳打出高危，赏金4000元。
* **垂直越权：普通用户调用管理员接口** — 接口`/api/admin/setScore`，我手工看URL里有`admin`就以为做了权限控制，没去试。但AI注意到这个请求的Cookie是一个普通学生账号的Session，且请求体中`userId`和`score`参数都与Cookie所属账号不一致，判定可能为垂直越权。我手动验证：把学生Cookie放到管理员接口上请求，成功修改了任意学生的成绩，高危，赏金5000元。
* **批量越权：遍历手机号获取全量用户** — 接口`/api/user/search?keyword=138`，返回包含手机号匹配的前10条用户简要信息。AI分析说：“keyword参数无限制，且响应包含手机号和用户ID，可与前面的越权接口联动，批量获取全站用户数据”。我写了个脚本遍历138-139号段，拖出6万多用户数据，严重漏洞，赏金8000元。

这一轮下来，AI帮我多赚了17000元，而成本只是几千个token的API费用，几毛钱。

**五、AI vs Autorize：到底谁更强？**

Autorize（及AutorizePro）是Burp的经典越权检测插件。它的工作方式：让你配置高权限和低权限两个账号的Cookie/Token，然后对每个请求自动复制一份，替换为低权限凭证重放，对比两次响应。如果响应相似（或完全一致），就标记为疑似越权。

Autorize的优势在于实时性和自动化，但局限性也很明显：

* 只能发现“两个不同权限用户看到相同数据”的情况。如果返回数据不同但都是敏感信息（如A看到张三，B看到李四），Autorize可能漏报。
* 无法处理复杂参数：UUID、哈希串、签名参数，Autorize不会自动构造。
* 无法理解业务上下文：它不知道哪个参数是用户ID，只能靠正则匹配。

AI的优势恰好弥补了这些缺陷：它能理解UUID、JWT、Base64，能从响应语义判断是否泄露了另一个用户的数据，还能给出具体的越权测试方案。AI的劣势是成本、延迟和隐私风险（流量上传到云端）。

最佳实践：**先用Autorize粗筛，把“响应相同”的高可能接口标出来；再把Autorize标出的可疑接口导出，丢给AI做深度分析。** 这样既利用了Autorize的速度，又发挥了AI的语义能力。

**六、注意事项：隐私、成本、幻觉**

* **隐私风险**：Burp流量里包含认证Cookie、个人信息、业务数据。如果你用云端API（如DeepSeek、OpenAI），等于把所有敏感数据都传给了模型厂商。建议两个方案：①使用本地部署的模型（如Ollama + Qwen/DeepSeek-Coder），数据不出本机；②对流量做脱敏处理，把Cookie值替换为占位符，把手机号/身份证替换为假数据，再发给AI。
* **成本控制**：一次分析几千条请求，token消耗可能达到几十万。建议过滤掉静态资源和重复请求，只发送URL+参数+响应摘要，而不是完整响应体。
* **幻觉问题**：AI有时会“脑补”不存在的越权场景，比如把正常的分页参数误判为ID。所有AI标记的漏洞，必须手工验证。我的做法是让AI输出“建议的测试Payload”，然后手工在Burp Repeater里验证，确认危害后再写报告。
* **Prompt优化**：越权分析的质量严重依赖Prompt设计。建议把你自己的越权测试经验整理成规则，注入到Prompt中。例如：“如果参数名包含uid、userId、memberId，且值为纯数字，则极有可能是越权入口。”

**七、写在最后**

把Burp流量扔给AI自动找越权，不是什么黑科技，就是把“人类逐条看流量”这个重复劳动用AI替代了。逻辑还是那些逻辑——看参数、看权限、看响应——但AI不会累、不会漏、不会因为UUID太长而跳过。

我用了三个月，越权漏洞的发现量翻了一倍多，赏金也水涨船高。如果你还在手工一条条审流量，不妨花一个下午把这套流水线搭起来。测试一下你家SRC的目标，你可能发现，那些藏在UUID和复杂业务逻辑里的越权，AI一个都没放过。

**严正声明**：本文所有技术均用于合法授权的安全测试，所有案例均已脱敏。未经授权将流量上传至第三方AI服务可能导致数据泄露，请自行评估合规风险。建议使用本地模型处理敏感流量。越权漏洞挖掘必须在授权范围内进行，未授权测试属违法行为。

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6x6n1Wb1pmwN6kAz3L4jCKjzXFiapPubIuT2OpX0FibbHamG6peZ1SKqicC6cNuENqACmDbBYnem2XNzHH87F25ADeRoMicGPyF7Sk/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zxPsSBiaTT0QiaBjibScxViciathof2tlahJCticqia6DncZNe4Fiatd1zWxPQKdTAqnyRPFWmxviaJJm5R8JLbEAURJnZRMiaKa1quLS8k/0?wx_fmt=png)

昆仑AI安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zxPsSBiaTT0QiaBjibScxViciathof2tlahJCticqia6DncZNe4Fiatd1zWxPQKdTAqnyRPFWmxviaJJm5R8JLbEAURJnZRMiaKa1quLS8k/0?wx_fmt=png)

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