---
title: 我用AI批量解剖小程序：10分钟挖出30个AccessKey，全是高危
url: https://mp.weixin.qq.com/s/WKeowavsUhHhhQJwQpf5xw
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:05:46.833547
---

# 我用AI批量解剖小程序：10分钟挖出30个AccessKey，全是高危

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3oR6eMARh6yqmuiaNhVtia7iaGlFAJCbxv3qFXBX11FgNYeyxH2J3ny4K4swWOobyFpjWHnjQUFOB6HiaibL3wSwBdH6GcspWIiaS8FZSIibVEnibics/0?wx_fmt=jpeg)

# 我用AI批量解剖小程序：10分钟挖出30个AccessKey，全是高危

原创

昆仑AI安全实验室
昆仑AI安全实验室

昆仑AI安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

去年双十一，我把手机里近半年打开过的小程序全翻了出来，一口气反编译了四十多个，然后丢给我自己训练的AI审计流水线。第二天早上，脚本给我生成了二十多份漏洞报告——全是AK/SK泄露、未授权API端点、甚至能直接连内网的IP。靠这一波，我那个月在几个大SRC平台刷了将近五万块的赏金。

你一定好奇：反编译小程序找密钥，不是早就有人用正则做了吗？问题就在这——正则太蠢，开发者太会藏。变量拼接、Base64编码、十六进制掩码、故意拆成多段……常规grep早就抓瞎了。而AI能读上下文，能推断变量引用，能还原编码，就像找茬游戏里开了天眼。

今天就摊开讲我这套AI辅助小程序批量挖洞的方案，从提取包到批量验证，一整套脚本和Prompt都给你。

**一、传统手法为什么失灵？**

先看几个真实案例，你就知道regex多无力了。

* **案例1**：某电商小程序，AccessKeyId硬编码在`app.js`里，但变量名是`e`，值是`'AKID' + atob('d3h3eA==')`。正则扫过去，毛都没有。
* **案例2**：某政务小程序，OSS密钥被切成三段放在三个不同文件里，最后在`utils.js`里拼接。AI能跨文件追踪调用链，把三段拼起来。
* **案例3**：某医疗小程序，密钥用`[84,105,97,110,120,105,97,110,107,101,121]`这种ASCII码数组表示，每次使用前`String.fromCharCode`还原。AI一眼看出这是什么东西。

这就是降维打击。AI不靠字符串匹配，靠语义理解。它知道变量怎么被赋值、怎么被引用、怎么被编码还原。

**二、我的AI挖掘流水线**

三步走，我把整个流程做成了自动化脚本。

**1. 采集wxapkg**

我不手动翻微信目录，直接写了个Python脚本，定期从PC微信缓存目录自动提取：

```
import os, shutilwechat_dir = r"C:\Users\admin\Documents\WeChat Files\wxid_xxx\Applet"output_dir = "D:\wxapkg_dump"os.makedirs(output_dir, exist_ok=True)for root, dirs, files in os.walk(wechat_dir):    for file in files:        if file.endswith('.wxapkg'):            appid = os.path.basename(root)            shutil.copy2(os.path.join(root, file), os.path.join(output_dir, f"{appid}.wxapkg"))
```

**2. 反编译**

用`unveilr`一键反编译整个目录：

```
unveilr -i D:\wxapkg_dump -o D:\decompiled
```

反编译后每个小程序一个文件夹，里面JS、JSON、WXML样样齐全。

**3. AI深度分析（核心）**

这里不是简单把整个文件丢给AI，而是做一个预处理：先用轻量正则初筛，把包含`key`、`token`、`url`等关键词的JS文件挑出来，只把这些文件送给AI。这样既省钱又高效。

我的Python脚本框架：

```
import os, re, requests, json
AI_API = "https://api.deepseek.com/v1/chat/completions"HEADERS = {"Authorization": "Bearer sk-xxx"}
def analyze_with_ai(file_path):    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:        code = f.read()    prompt = f"""你是资深安全审计专家。分析以下前端JS代码，提取所有可能的敏感信息：- 云服务AK/SK（阿里云、腾讯云、AWS等）- API端点（http/https）- 内网IP- 数据库连接串- JWT密钥要求：1. 即使密钥被拆分、编码、拼接，也尝试还原。2. 以JSON格式输出，包含字段：类型、原始代码片段、还原后的值、风险评估、利用建议。3. 无发现则返回空JSON。代码：{code[:6000]}"""    resp = requests.post(AI_API, headers=HEADERS, json={        "model": "deepseek-chat",        "messages": [{"role": "user", "content": prompt}],        "temperature": 0.1    }, timeout=60)    return resp.json()["choices"][0]["message"]["content"]
# 批量处理results = []for root, dirs, files in os.walk("D:\decompiled"):    for file in files:        if file.endswith('.js') and any(kw in file.lower() for kw in ['app', 'util', 'config', 'request', 'api', 'common']):            path = os.path.join(root, file)            try:                result = analyze_with_ai(path)                if result and '{}' not in result:                    results.append((path, result))                    print(f"[+] 发现: {path}")            except Exception as e:                print(f"[-] 错误 {path}: {e}")
# 保存报告with open('findings.json', 'w') as f:    json.dump(results, f, indent=2, ensure_ascii=False)
```

**4. 批量验证**

AI提取出的AK/SK需要验证。我集成了阿里云、腾讯云的SDK，自动检测权限和资源：

```
import oss2from alibabacloud_sts20150401.client import Client as StsClient
def verify_aliyun(ak, sk):    try:        sts = StsClient(config)        sts.get_caller_identity()        service = oss2.Service(oss2.Auth(ak, sk), 'oss-cn-hangzhou.aliyuncs.com')        buckets = [b.name for b in oss2.BucketIterator(service)]        return {"status": "有效", "buckets": buckets}    except Exception as e:        return {"status": "无效", "reason": str(e)}
```

整套流水线跑下来，睡前启动，睡醒收菜。

**三、实战案例：AI挖出三个“隐形炸弹”**

**案例1：电商小程序——OSS全权限密钥**

AI在`config.js`里发现一行`const _0x4f2a=['\x41\x4b\x49\x44']`（十六进制“AKID”），然后追踪变量引用，在文件末尾找到了拼接逻辑，还原出完整的AccessKey。我用验证脚本一查，权限是`AliyunOSSFullAccess`，所有商品图片、用户上传的身份证照片一览无余。高危，赏金6000元。

**案例2：政务小程序——内网API+数据库密码**

AI在一个叫`env.js`的文件中发现了注释掉的数据库配置：`// db: { host: '10.23.45.67', user: 'admin', pwd: 'Gov@2023!secure' }`。它敏锐地指出这是测试环境遗留信息。我尝试从外网反向代理进入，果然连接到了那个内网MySQL，里面几十万条市民个人信息。严重漏洞，赏金12000元。

**案例3：教育小程序——未授权管理员接口**

AI在`app.js`里提取到API端点`http://47.x.x.89:8080/admin/api/`，并注释说“疑似无认证”。我直接浏览器访问，返回了教师管理后台的全部功能列表，可以修改学生成绩、导出学籍。高危，赏金5000元。

**四、效率对比：AI vs 手工 vs 正则**

我拿同批20个小程序做了对照实验：

* **纯手工**：花了整整两天，找到4个漏洞。
* **正则脚本**：15分钟跑完，报出12个“可疑”，但其中9个是误报（比如把`keyCode`当成密钥），验证后只确认了3个有效洞。
* **AI流水线**：30分钟（含API调用等待），直接输出8份高度确认的漏洞报告，无误报，并给出了利用建议。效率提升数倍，且AI还发现了一个手工和正则都漏掉的十六进制编码密钥。

**五、防御建议：别再把钥匙放在门口地垫下**

写完报告我不禁感叹：这么多开发者为什么非要把AK/SK写在前端？其实无非图省事。但安全就是不能省事的。作为开发者，请记住：

* **所有云服务调用必须走后端中转**，前端只能拿STS临时凭证或预签名URL。
* **敏感配置严禁硬编码**，使用环境变量或配置中心。
* **代码提交前做敏感信息扫描**，git hooks加一道防线。
* **如果真的泄漏了，立刻在云平台轮换密钥**，别拖。

**六、写在最后**

AI不会取代渗透测试工程师，但用AI的工程师会取代不用AI的。我这一套流水线，本质就是把重复的、低级的、耗时的体力活交给AI，自己腾出时间做更高级的攻击链设计。

下次看到小程序，别只想着逻辑漏洞。把它的wxapkg拖出来，丢给AI，你可能会发现，它里面藏的东西远比想象中多。也许，下一个赏金最高的漏洞，就在那个毫不起眼的`config.js`里。

**严正声明**
本文所述技术仅用于合法授权的安全测试。未授权提取、反编译他人小程序或利用其漏洞均属违法行为。所有案例均已脱敏，仅保留技术原理供学习参考。安全之路，始于授权。

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6x6n1Wb1pmwN6kAz3L4jCKjzXFiapPubIuT2OpX0FibbHamG6peZ1SKqicC6cNuENqACmDbBYnem2XNzHH87F25ADeRoMicGPyF7Sk/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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