---
title: 书生大模型实战营闯关 第二关：Python 基础知识
url: https://mp.weixin.qq.com/s?__biz=MzAwMTMzMDUwNg==&mid=2650889164&idx=1&sn=2cf5a75ca555fe92ec7ec293054d4d95&chksm=812ea7e9b6592eff092f56f0124b677673bd358386a7658449a85f8876b4a4b3e5030931f7d0&scene=58&subscene=0#rd
source: 网安杂谈
date: 2024-10-31
fetch_date: 2025-10-06T18:54:40.762790
---

# 书生大模型实战营闯关 第二关：Python 基础知识

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhg1qzBjzlSbZnD0Z5LibvPFYZJkRZ4cg3xRUUdj27AT8iaGea51gVuf0tQ/0?wx_fmt=jpeg)

# 书生大模型实战营闯关 第二关：Python 基础知识

原创

网安杂谈

网安杂谈

这个实战营是我自己参加，觉得内容非常不错的，因为开源免费，内容也是有一定难度的，有兴趣的一起学习。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgichzau3fnMFSic2pFIVamY8HovMFlCENmnN2MCbEs1yyoVdzUKXBAicZg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

实战营第二关，主要是学习下python的基础知识。

任务要求如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgpt8G5eFrH1Zx5ficXSJylxyVqEcwfT9P8Ipcl3ia71tUUVu3mAPcxn7g/640?wx_fmt=png)

1.任务一：python编程

Leetcode 383，这个题目的具体内容是这样的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgzvMPHicqCbvjbq837KngaDlBvNOB4vhXwNysVBbuwTuC49kPvSkUM3g/640?wx_fmt=png)

我得靠大模型帮助才行。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgmwibaG0iaibppMPcgIcK4ibLExicjnH05a99vcNxtKjt0VG2tRCbbewlViaA/640?wx_fmt=png)

2.任务二：Vscode连接InternStudio debug

调用书生浦语API实现将非结构化文本转化成结构化json的例子

首先获取API Tokens

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgSC3URn54gqxDVic7or5lhIH6zu87Z5kdiabicKUGT1libH6EknbFOiaibo4g/640?wx_fmt=png)

训练营给了一段代码，通过debug发现，响应的内容前后有多余的标记和换行符，json.loads() 无法正确解析。响应是用代码块格式包裹的，不是有效的 JSON 格式，需要去掉这些额外的标记。下面代码OK了

```
from openai import OpenAIimport jsondef internlm_gen(prompt,client):    '''    LLM生成函数    Param prompt: prompt string    Param client: OpenAI client     '''    response = client.chat.completions.create(        model="internlm2.5-latest",        messages=[            {"role": "user", "content": prompt},      ],        stream=False    )    return response.choices[0].message.content
api_key ='ey******'client = OpenAI(base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",api_key=api_key)
content = """书生浦语InternLM2.5是上海人工智能实验室于2024年7月推出的新一代大语言模型，提供1.8B、7B和20B三种参数版本，以适应不同需求。该模型在复杂场景下的推理能力得到全面增强，支持1M超长上下文，能自主进行互联网搜索并整合信息。"""prompt = f"""请帮我从以下``内的这段模型介绍文字中提取关于该模型的信息，要求包含模型名字、开发机构、提供参数版本、上下文长度四个内容，以json格式返回。`{content}`"""res = internlm_gen(prompt,client)# 打印响应内容以供调试print("Raw Response:", repr(res))# 检查响应是否为空if not res:    print("Response is empty")else:    # 去除多余的空格和换行符    res = res.strip()        # 去掉代码块标记    if res.startswith("```json") and res.endswith("```"):        res = res[8:-3].strip()  # 去掉开头的 ```json 和结尾的 ```        # 修正 JSON 格式，确保参数版本用双引号包围    res = res.replace("1.8B", "\"1.8B\"").replace("7B", "\"7B\"").replace("20B", "\"20B\"")        print("Processed Response:", repr(res))        try:        res_json = json.loads(res)        print("Parsed JSON:", res_json)    except json.JSONDecodeError as e:        print("JSON decoding error:", e)
```

输出结果是这样的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgVTZe68G8cIfa7cUXWBpJtdObokkGsRxticm4MkBVYnEzfNx8lq4EoaA/640?wx_fmt=png)      就用简单的API调用，我们就能抽取出文本中的关键信息了 ！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgff9UZRloG5SVQiawkhDicPMD3VaLUxuicv7nWOZ8C3fayPatJX7TjDibfg/640?wx_fmt=png)

扫二维码报名一起学吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

网安杂谈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

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