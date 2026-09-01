---
title: AutoPT 2.0 - 具有普适性的AI自动化渗透测试工具
url: https://mp.weixin.qq.com/s/tcEdoxRumYNVNPana5ucSQ
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:59:20.912419
---

# AutoPT 2.0 - 具有普适性的AI自动化渗透测试工具

# AutoPT 2.0 - 具有普适性的AI自动化渗透测试工具

shiyeshu
shiyeshu

李白你好

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 工具简介

AutoPT是一个基于LangGraph框架开发的自动化网络安全渗透测试工具。通过多个专业AI代理的协作，实现智能化的渗透测试流程自动化，帮助安全研究人员和渗透测试人员提高工作效率。本项目吸收了xbow的多agent、多模型协作特点，以实现AI能效最大化。但不同的是没有像多数渗透agent一样将提示词细化到具体操作、具体工具，这样做的目的是提高通用性，实现真正的AI智能化。作者：shiyeshu

![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNVxhePaq5DW30hcqzGZxx27W2SeibJNKpeDEZplPSIesjPD9p66dCMRN5jgQxtEvvvcyZvqQicC0b94KW1QZRA4dFyV1AHxNWUHU/640?wx_fmt=png&from=appmsg)

## 多Agent编排

1. **渗透任务指挥官 (Strategist)**

* 基于日志制定下一步攻击策略

2. **副指挥官 (Deputy)**

* 将战略意图转化为技术需求

3. **战术执行专家 (Operator)**

* 查看并选择合适的渗透测试工具，构造可执行的命令行

4. **执行与安全引擎 (Auditor)**

* 执行安全检查，防止危险操作，实际运行命令并获取结果，确保命令执行的安全性

5. **日志审计员 (Reporter)**

* 分析测试日志

整体分为渗透组和记录组，分工合作以求减少AI幻觉

### 💡 主要功能

* ✅ **自动化渗透测试流程** - 从信息收集到漏洞利用的全流程自动化
* ✅ **智能工具管理** - 自动识别和使用各类渗透测试工具，具有广泛通用性无需针对工具适配
* ✅ **安全机制保障** - 内置命令黑名单，防止危险操作
* ✅ **完整日志追踪** - 记录每个测试步骤，支持审计回溯
* ✅ **自动报告生成** - 基于测试结果自动生成专业报告
* ✅ **多模型支持** - 使用“模型合金”的概念提升效能

## 安装说明

### 环境要求

* Python 3.10 或更高版本（< 3.14）
* Windows操作系统（因为各个路径写的win,可自行修改）

### 安装步骤

1. **克隆项目**

```
git clone <项目地址>
cd AutoPT
```

2. **创建虚拟环境**

```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **安装依赖**

```
pip install -r requirements.txt
```

4. **配置环境变量**创建 `.env` 文件并配置必要的API密钥和相关路径
5. **添加渗透测试工具包**将工具复制到aptools文件夹中，以工具名称为父文件夹名 如：/aptools/nmap/nmap.exe

项目支持集成各类渗透测试工具，默认工具路径为 `/aptools/`。支持的不太偏门的几乎所有工具。冷门工具也支持，但可能消耗大量轮次和token

### Web GUI模式

```
# 启动Web界面
python gui_app.py
```

访问 `http://localhost:8080` 使用图形化界面进行操作。

1、填写目标和Attck Rounds

2、目标可以是ip、ip:端口、URL等，AI根据不同类型会自动识别并做出战略

3、Attck Rounds用于控制AI操作步骤次数上限。一般一个战略为一个轮次，即从指挥官到日志记录为一次。精确填写Attck Rounds可以限制token消耗。

## 安全说明

⚠️ **重要提醒**：

* 本工具仅用于授权的渗透测试和安全研究
* 严禁用于非法入侵或未经授权的测试
* 内置安全机制防止危险操作（如rm -rf等,虽有检查但不一定完全覆盖）

## 工作流程

1. **初始化** - 加载配置和AI代理
2. **策略制定** - 指挥官分析日志并制定策略
3. **需求转换** - 副指挥将策略转化为技术需求
4. **工具选择** - 执行专家查看并选择合适工具
5. **命令执行** - 安全引擎执行命令并获取结果
6. **日志记录** - 记录执行结果
7. **循环执行** - 重复步骤2-6直到达成目标
8. **报告生成** - 审计员生成最终测试报告（模板css在agent.py中可自行修改）

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNUVjCYPzNn1dnZRibdAzymBk0r9K7tP5a3PghlzUnt2GyQuzOku6brkuYEuqURU3dG2eDiasgJaZzJWzgEgTahKe250Klib5tJ4K0/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNUt2iadOf5zuHcY7lKesQzBA7WhmhqHroHsHUiaJAUVPu42MXMMTOkA7rb7Licxjukt0ObveMsFn7NSkzW6XOYsNxv2zIe3bRGCFo/640?wx_fmt=webp&from=appmsg)

## 工具下载

```
https://github.com/shiyeshu/Autopt
```

## 网络安全情报攻防站

**www.libaisec.com**

综合性的技术交流与资源共享社区

专注于红蓝对抗、攻防渗透、威胁情报、数据泄露

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNUtJZF7ASib6y7BTEEYWKmEUuVTMXA0fs48dEHoIsZdicmOYWHsLvlNBEE4s2HjSwZ8uiafHaN07ksyRBicqhvXO1xFnbROMjxEuCE/640?wx_fmt=webp&from=appmsg)
> 👇 点击阅读原文，访问**网络安全情报攻防站**

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAuS65pf9u98YWJSdI6kWZ64ziasaVXOFXiabEV2AuCY8yGygtKHicEFVvHnw3bzhsDXBB3DQIiaNhOiaQ/0?wx_fmt=png)

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