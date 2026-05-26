---
title: LangChain AI代码审计Agent 初用心得
url: https://mp.weixin.qq.com/s/bXPJHX3iScORlbkBz5n80A
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:06:54.443959
---

# LangChain AI代码审计Agent 初用心得

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hYTcBbYGXIesEibGN8RsA3NiaeGkZawiaqqNBcjsayDoFcwyOcwXRaynAibJxlicdz0xYqsLbRliaPDgIyzibcjSDNHpU6iaPCOGBt6WpWSnl7EabwM/0?wx_fmt=jpeg)

# LangChain AI代码审计Agent 初用心得

d2550自留地

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于ap0s
，作者ap0s

![](http://wx.qlogo.cn/mmhead/X6Ucic5kYIBPrvcibYvOBIPSvniaR6CT6XcV6wPZzntpT1iaH5jPBhkJAPlibZdyFxvqEFX7jj1QECNw/0)

**ap0s**
.

安全小白

## LangChain AI代码审计Agent 初用心得

### 本人使用的优缺点总结

优点

1. 封装prompt、llm，Parser 调用确实方便
2. 工具集成，如一个`@tool`就可以封装成一个agent的方法
3. 链式调用
4. 对RAG处理以及向量数据库处理比较方便

缺点：

1. 受服务提供商的限制，如官方GLM暂未集成

### 框架

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hYTcBbYGXIeNIKYcRNxaNxhjLky3L4h8xkcWIXWnoiaFJImYLoguLiaFUwY8y7PheZNZPH9gLT2yfVdwicfBTCQySib0RvqJUw2iadWNp8zfCQac/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/hYTcBbYGXIcPcqAgzoYb5UjRNmibzWqBhn05XV1MaKkWAdqJMRMT3Zv1icpPtau7fweje42hSvNg4DSMV1w05YibNiaWOrA9ibE3icR9TMblHlOBE/640?wx_fmt=png&from=appmsg)

设计思想是通过对审计的重点使用`@tool`进行封装，让agent知道自己要干哪些事情，然后进行补充，这里写死比较局限，得喂一些rag

```
"""
PHP Ssrf 检测工具
"""
from langchain_core.tools import tool
from typing import List, Dict, Any
import re

@tool
def detect_php_ssrf(code: str) -> List[Dict[str, Any]]:
    """检测 PHP SSRF (服务端请求伪造) 漏洞"""
    import re
    vulnerabilities = []
    """例如"""
    patterns = {
        "file_get_contents": {
            "pattern": r'file_get_contents\s*\([^)]*\$_(GET|POST|REQUEST)',
            "severity": "HIGH",
            "description": "file_get_contents 使用用户输入，可能 SSRF"
        },
        "curl_setopt URL": {
            "pattern": r'curl_setopt.*CURLOPT_URL.*\$_(GET|POST|REQUEST)',
            "severity": "HIGH",
            "description": "cURL 请求 URL 由用户控制"
        },
        "fopen用户输入": {
            "pattern": r'fopen\s*\([^)]*\$_(GET|POST|REQUEST)',
            "severity": "MEDIUM",
            "description": "fopen 打开用户指定的 URL"
        },
    }

    lines = code.splitlines()
    for i, line in enumerate(lines, 1):
        for vuln_type, info in patterns.items():
            if re.search(info["pattern"], line, re.IGNORECASE):
                vulnerabilities.append({
                    "type": f"PHP SSRF - {vuln_type}",
                    "line": i,
                    "code": line.strip(),
                    "description": info["description"],
                    "severity": info["severity"]
                })

    return vulnerabilities
```

使用漏洞分析+污点检测的，判断此处是否用户可控

```
## 详细发现

### 1. SSRF (服务端请求伪造) - CRITICAL

**位置**: webhook/model.php 第 580-620 行，misc/model.php 第 200-250 行
**检测方式**: detect_php_ssrf + LLM 分析
**污点验证**: is_tainted=True, confidence=HIGH
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hYTcBbYGXIeAaS6YpBriblNiaj9c1wsiba4pOU9hZaVtgTVR7siaeJibD8s9ragaQGQlB4BN369a19K4KGEicb67oOTEL2F8IPWnzLQLEOthZNAK4/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/hYTcBbYGXIdzD128YO15iaupw309USIe9ohVjOicTfNrh4USzMG2dvXufubtHARHCWHFKcqBdLCL7aTmiad581qx5QgiaSDnia4LMm5e0zo1UByU/640?wx_fmt=png&from=appmsg)

### 审计结果

![](https://mmbiz.qpic.cn/mmbiz_png/hYTcBbYGXIdDge0xW9KvD37JAJT25KOsr4IiasZHyKIFic9V8wFoObmp04nAMg8hqicvcDSsPcxIp237XjkmIsqfbuvViafSGtG8bNibxQfa2ZwA/640?wx_fmt=png&from=appmsg)

目前看来，确实能够审计出来一些有用或者可以水cve的洞，对于组合漏洞的挖掘效果不是很尽如人意

#### 关于ai幻觉

让每次ai干活的时候，让读取一个类似于：《用户使用协议》的东西进行排除，但是不能完全排除

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hYTcBbYGXIcafB30h8Na6J61pHeTQNpGB0xxJDO717yrS2b6BF8wOyrQnT1nricPoh6wQERposUph6XSgce5Idak6Z1hAlzfHldbSqnUbqD0/640?wx_fmt=png&from=appmsg)

### 消耗

因为不集成GLM，所以我这里使用的`QWEN3.5-PLUS`,简单审计100w token就消耗完了，LangChain这种工具的开发还是得使用本地模型进行调试

![](https://mmbiz.qpic.cn/mmbiz_png/hYTcBbYGXIeYRCfiaZP34UpPVJXvI1YHib5bljMia18Kjhagybml4mnxEGQrbBq4csHt8j7ibSHvPDickzHhSL4merWPucGBKHyT268ic4iaKIEfXY/640?wx_fmt=png&from=appmsg)

### TODO

1. 添加LLM漏洞验证模块
2. 添加国标+实际漏洞的RAG
3. 添加任务模块让工具自行pull干活

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/bDFc8pniaibZKTFqPUQWQjMbNdRd2mI4JRfas2IfsTUxFIIWgc0OX83ZbktQcl6glsTKibuhpSa0rgrt19N1ibMLHg/0?wx_fmt=png)

d2550自留地

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/bDFc8pniaibZKTFqPUQWQjMbNdRd2mI4JRfas2IfsTUxFIIWgc0OX83ZbktQcl6glsTKibuhpSa0rgrt19N1ibMLHg/0?wx_fmt=png)

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