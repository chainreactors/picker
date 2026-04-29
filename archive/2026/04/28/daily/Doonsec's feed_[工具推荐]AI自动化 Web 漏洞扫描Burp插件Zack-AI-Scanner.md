---
title: [工具推荐]AI自动化 Web 漏洞扫描Burp插件Zack-AI-Scanner
url: https://mp.weixin.qq.com/s/aSe-K12DmxPVCYURgrRb6g
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:10:59.082542
---

# [工具推荐]AI自动化 Web 漏洞扫描Burp插件Zack-AI-Scanner

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQrIhRvBgnCaIcEXu70YXYJY6Hic7zTNX4gP9uUUDl74LicBY0NSSibWPJwkjYmgOq7nn2CRyEM1tu0ZkdWvxnKCWzmForgFI4VMs/0?wx_fmt=jpeg)

# [工具推荐]AI自动化 Web 漏洞扫描Burp插件Zack-AI-Scanner

ZackSecurity
ZackSecurity

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

# Zack-AI-Scanner

## 项目概述

Zack-AI-Scanner 是一款基于大语言模型的自动化 Web 漏洞扫描工具，作为 Burp Suite 扩展运行。通过 AI 深度学习技术自动分析 HTTP 请求特征，智能识别潜在安全漏洞，动态生成针对性测试Payload，并智能验证漏洞真实性。

## 核心功能

* **AI 智能扫描**: 内置 Skills 利用 LLM 自动分析请求并制定测试策略
* **多漏洞类型支持**: 支持 17 种常见 Web 漏洞类型的检测
* **WAF 绕过能力**: 内置 Prompt 多种 WAF 绕过技术，50% 载荷为绕过载荷
* **实时结果验证**: AI 二次验证确保漏洞真实性（置信度阈值 ≥90%）
* **多格式报告导出**: 支持 HTML 和 Markdown 格式的渗透测试报告

## 支持的漏洞类型

| 漏洞类型 | 说明 |
| --- | --- |
| SQL\_INJECTION | SQL 注入 |
| XSS | 跨站脚本攻击 |
| COMMAND\_INJECTION | 命令注入 |
| FILE\_UPLOAD | 文件上传漏洞 |
| SSRF | 服务端请求伪造 |
| XXE | XML 外部实体注入 |
| FILE\_INCLUDE | 文件包含漏洞 |
| SSTI | 模板注入 |
| CSRF | 跨站请求伪造 |
| DESERIALIZATION | 反序列化漏洞 |
| AUTH\_BYPASS | 越权/认证绕过 |
| PATH\_TRAVERSAL | 路径遍历 |
| DIRECTORY\_TRAVERSAL | 目录穿越 |
| SENSITIVE\_DATA\_EXPOSURE | 敏感信息泄露 |
| LOGIC\_FLAW | 逻辑漏洞 |
| RACE\_CONDITION | 条件竞争 |
| TYPE\_CONFUSION | 类型混淆 |

## 支持的 AI 服务提供商

* OpenAI (GPT-4, GPT-3.5)
* Anthropic (Claude)
* Google Gemini
* Azure OpenAI
* 通义千问 (阿里云)
* 文心一言 (百度)
* 智谱 AI (GLM)
* Kimi (月之暗面)
* DeepSeek
* 讯飞星火
* 字节豆包
* 腾讯混元
* 百川智能
* MiniMax
* 零一万物
* 阶跃星辰

#### 环境安装（三步走）

1. **编译构建**：在项目根目录下执行命令 `mvn clean package`，等待打包完成。
2. **加载插件**：打开Burp Suite，切换到`Extender`标签页，点击`Add`，选择上一步生成的JAR文件。
3. **验证安装**：若Burp主界面出现“Zack-AI-Scanner”选项卡，即代表安装成功。

#### 核心配置（连接AI大脑）

1. 点击插件面板的 **“配置”** 按钮，进入配置中心。
2. 根据你使用的AI服务（如OpenAI或国内兼容接口），选择对应**提供商**并填写API Key。
3. 点击 **“获取模型”** 下拉框，系统会自动拉取你可用的模型列表（如GPT-4或DeepSeek）。
4. 点击保存，此时AI引擎已准备就绪。

#### 实战使用（一键智能扫描）

1. 在Burp的`Proxy`历史记录或`Repeater`中，选中任意一个HTTP请求包。
2. 右键呼出菜单，选择 **“Zack-AI-Scanner”**。
3. 根据需求选择模式：

* **AI智能扫描**：插件会全自动分析请求并检测逻辑漏洞。
* **特定漏洞类型**：针对SQL注入、越权等单一类型进行深入测试。

4. 切换至主面板，你可以实时看到AI的**思考过程**和**扫描进度**。
5. 扫描完毕后，支持**导出漏洞报告**，直接用于项目归档。

目录结构

```
src/main/java/com/zackai/├── AISentryExtender.java    # Burp 扩展主入口├── core/                    # 核心功能模块│   ├── AIEngine.java        # AI 扫描引擎│   └── ConfigManager.java   # 配置管理器（单例）├── model/                   # 数据模型│   ├── ScanTask.java        # 扫描任务模型│   ├── VulnResult.java      # 漏洞结果模型│   └── AIProvider.java      # AI 服务提供商模型├── ui/                      # UI 组件│   ├── MainPanel.java       # 主面板│   ├── TaskTablePanel.java  # 任务表格│   ├── TaskDetailPanel.java # 任务详情│   ├── LogPanel.java        # 日志面板│   ├── ConfigDialog.java    # 配置对话框│   ├── ExportDialog.java    # 导出对话框│   ├── EndpointManagerDialog.java  # 端点管理│   ├── PromptPanel.java     # 提示词管理│   └── HelpPanel.java       # 帮助面板└── util/                    # 工具类    └── ReportGenerator.java # 报告生成器
```

插件使用实例

配置大模型API Key信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRrRiaEl6cjss3hfyckwHT92xcTmejBETJYtibDpEt7Z3D9ZhH0zs52Qpl2llB4iaesIrQzuEZwaUiamK8EpF3IBiamLaicHgwCqnuUE/640?wx_fmt=png&from=appmsg)

右击请求包->拓展->Zack-AI-Scanner调用工具，可选择AI智能扫描和单漏洞扫描：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRWbZiaPMzkWetHibdANApjqEhGd41oRSPulucUt5lQPqJFCUiaU5oVrCg6Td8PedtzQNAVYvJYfStzcuFxguLZhkhNwbeA0nCGHE/640?wx_fmt=png&from=appmsg)

日志统计窗口可实时查看扫描信息：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRSUIfvoo8vbGXupvQu9O2ksIotXOaLgyNicDibN4TugOeBZuO8XTtV9I5tS5Zgc8CuOHbGpq5NO4QtKDs7lG6QhA9gib6nzzVcHI/640?wx_fmt=png&from=appmsg)

请求与响应详情窗口可以查看实时的扫描流量：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQQQgBKpQeJ9zM3uNRgYTibxJ0zIrW0ibHaG7mEhY4Aj0lJzWiaCrqqXZo2TOlvO0G1KAuazH8SendkyDAe5YeAqzBJjDa5w4P6rk/640?wx_fmt=png&from=appmsg)

在任务列表窗口可以查看所有扫描任务和状态，扫描结束导出漏洞报告，支持 HTML 和 Markdown 格式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ4ZebKTafvQjicnQRhwnu08MEQzX7IM7LwibIecmajUbHFMraev3NtDnfNnPU8WTpMYjq2DsySFCicGzicoQXcQBJ5TXgyh9HibLFU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboREk1iawTRNias24qvmlmbWU2GEB9pN0zsWMEFfC7nIKzKUyzeCzWVFMXAmjZJCdeP0iaIT07oibyQ4bicRtreVvku6NXNXCl9Wz4k8/640?wx_fmt=png&from=appmsg)

HTML 和 Markdown 格式报告内容：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTmVahBd1lWI9LJs9mfZgEshHG2YGaOy7ibhenUIze8uddIKWnamKib2KdQWHLdtXaCGicPMuScASVjDMD4zvVU3fXmYPqkaN4Lx8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQDbHFtoRzNvIgcrEB0Blq5aflFgATkZXymk8nicib0B1ybwWKaHgdEw9X6xT8cUVTpBib8dkibW8nEyE53w0N1kOQicgk2UIBYI5Rg/640?wx_fmt=png&from=appmsg)

工具地址

```
https://github.com/ZackSecurity/Zack-AI-Scanner
```

总结

```
工具好不好用，实践是检验真理的唯一标准。
```

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中!!!)**

```
信息收集(主域名信息收集,子域名信息收集等&会永久提供fofa-key助力)弱口令漏洞&未授权访问漏洞挖掘任意文件读取&删除&下载&上传漏洞sql注入漏洞url重定向漏洞csrf&ssrf漏洞挖掘XSS&XXE漏洞挖掘等等常见漏洞cors&目录遍历&越权漏洞挖掘EDUSRC(证书站挖掘案例分享&edusrc挖掘技巧分享)CNVD挖掘技巧分享&实战案例报告编写公益漏洞挖掘（公益src挖掘漏洞分享&提供补天1权重资产）SRC挖掘实战(针对各种常见功能总结的常见测试思路等快速提升)经典常见Nday漏洞(常见中间件&以及各种常见框架)复现云安全相关漏洞挖掘（云key扫盲&云存储桶&快速识别云环境&云攻防）AI相关学习（AI基础&AI代码审计实战测试&webLLM攻击等）APP&小程序漏洞挖掘等各模块不在一一介绍
```

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR45bibbJEb28a1gS5yth3r5HyOsgPiaOUHHYriahZyIyrk0LMOsHW4VoDibyBRibTNzptGiaLWX62UwykicwvbxCJPopvklqiaxML8lS8/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQVVlTXhibjR8UiakZBQicXRZrQ7hdoOz5G8MQrcuDBGbqJdO0kIz6R9IU4ObAeOiabT8pr6lc7jibdIkKoTjiaXNHPLAwAB3BV2UvLM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCrvarBbzP4L9kS6P0LVH9JMdmcbFDKiaicHqMFgTxq3x4iatjDJQicmc7NPC14C9Fk3icFjrouSgNVaN8Byuf0C0Iq9O6D1XPvFvY/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRPAemLYYSWRsc2cHYkwwxQicDQNf46MY8wUetFibPmetZdkicr4BNvPF0cBibqyS9emwayFf6njw9kjvBvWLoFDQJY5JQDMSUqh4E/640?wx_fmt=png&from=appmsg)

云安全&AI相关

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRfLMPDcF7l8FiaicK20uQdqQ9jrQnlIHk3J3DPhEpPxLfNia23dOuelLicVlNsvXgvSGa9Y4NfuTqUhxBOfF0nzHngWK01icdQWIDM/640?wx_fmt=png&from=appmsg)

**陌笙安全漏洞库介绍**

```
1day&0day分享EDU学校相关漏洞Web应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSajCclDhuRpaLic9Ld915CHU7RqSC1LCrPGfNZiavdPEVeDedDWOPBhtMLCicTp3RNd1lT0Pmfo3mx5B0hUxbQg3ic6Via90NMtZVk/640?wx_fmt=png&from=appmsg)

**陌笙安全面试库**

```
渗透测试基本问题一汇总渗透测试基本问题二汇总渗透测试基本问题三汇总微步护网面试题目长亭科技面试深信服护网面试启明星辰渗透测试面试题目安恒面试题目360面试奇安信护网面试运维面试题目运维面试题库网安面试相关文档大全相关面试文章推荐等等
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSoLqEzH0a3A4LQrvTIkGx81Sh5pf6fCoEQJhYg715vrJicSkfBuCoAmV2Kp4uOMe5jcUZutPwicibFibtJ1ZmyiaAibCg0XicWnsNcicE/640?wx_fmt=png&from=appmsg)

**陌笙****纷传****圈子介****绍**

```
1、src挖掘思维导图，信息收集思维导图，edusrc挖掘思维导图，以及后续的红队&面试思维导图&自己网安笔记等持续更新2、2025-2026的edusrc实战报告包含证书站和非证书站以及2025之前的各种优质报思路分享3、各种src报告思路分享（内部&外部）4、分享各种src挖掘&edusrc挖掘培训资料&视频5、不定期分享通杀、0day6、有圈子群可以技术交流以及不定期抽取证书&免费rank7.分享各种护网资料各家安全厂商讲解视频&精选实战面试题目8、各种框架漏洞技巧分享9、各种源码分享（泛微、正方系统、用友等）10、漏洞挖掘工具&信息收集工具&内网渗透免杀等网安工具分享11、各种ctf资料以...