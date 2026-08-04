---
title: 一个项目带你入门AI应用开发课程介绍 - bamb00
url: https://www.cnblogs.com/goodhacker/p/22168171
source: 博客园 - bamb00
date: 2026-08-03
fetch_date: 2026-08-04T04:56:30.001697
---

# 一个项目带你入门AI应用开发课程介绍 - bamb00

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [周边](https://cnblogs.vip/store)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19316348)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://www.cnblogs.com/my "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://www.cnblogs.com/my)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/goodhacker/)

# [人怜直节生来瘦，自许高材老更刚。](https://www.cnblogs.com/goodhacker)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/goodhacker/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/bamb00)
* 订阅
* [管理](https://i.cnblogs.com/)

# [一个项目带你入门AI应用开发课程介绍](https://www.cnblogs.com/goodhacker/p/22168171 "发布于 2026-08-03 11:46")

# AI Agent 编程实战：从零到全栈

## 课程概述

8 节课，从 `print("hello")` 写到完整的 AI Agent 项目。每节课的代码都可以独立运行，后一节课在前一节课的基础上增量构建。

**最终产出：** 一个基于 LangGraph 的多 Agent 电商客服系统，含 Chroma 向量数据库、Function Calling、多轮对话、可插拔数据源。

## 前置要求

* Python 3.9+
* 一个 LLM API Key（DeepSeek / OpenAI / 通义千问 等兼容接口的服务商均可）
* 基础 Python 语法

## 课程路线图

| 课 | 主题 | 核心内容 | 代码行数 |
| --- | --- | --- | --- |
| 1 | 基本 LLM 对话 | API 调用封装、配置管理 | 30 行 |
| 2 | 意图分类 | System Prompt、JSON mode、路由 | 80 行 |
| 3 | RAG 向量检索 | Chroma 向量数据库、语义检索 | 150 行 |
| 4 | Function Calling | 工具定义、执行、结果回传 | 250 行 |
| 5 | LangGraph 多 Agent | 状态图、条件路由、节点拆分 | 400 行 |
| 6 | 会话管理 | 多轮对话、滑动窗口 | 500 行 |
| 7 | 可插拔数据源 | 抽象接口、工厂模式 | 600 行 |
| 8 | 工程化与部署 | 错误处理、日志、测试、API | 800 行 |

## 快速开始

```
cd ai-agent-course
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env 填入你的 LLM_API_KEY

cd 01-basic-chat
python chat.py
```

## 课程约定

* 每课目录下的代码可以独立运行
* 第 5 课开始的项目会被逐步完善到第 8 课
* `.env` 在所有课程间共用（存在根目录）
* 每课末尾有课后作业和面试问题

posted @
2026-08-03 11:46
[bamb00](https://www.cnblogs.com/goodhacker)
阅读(28)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fgoodhacker%2Fp%2F22168171&targetId=22168171&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202607/35695-20260715081632770-1485313413.webp)](https://www.trae.com.cn/?utm_source=advertising&utm_medium=cnblogs_ug_cpa&utm_term=hw_trae_cnblogs)

### 公告

[博客园](https://www.cnblogs.com/)
  ©  2004-2026

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)