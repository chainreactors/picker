---
title: AWS IAM 信任链 和 EKS IRSA
url: https://jiajunhuang.com/articles/2025_02_16-aws_iam.md.html
source: Jiajun的技术笔记
date: 2025-02-17
fetch_date: 2025-10-06T20:33:26.108928
---

# AWS IAM 信任链 和 EKS IRSA

[Jiajun的技术笔记](/)

搜索

* [EN](https://blog.jiajunhuang.com)
* [归档](/archive)
* [分享](/sharing)
* [随想](/notes)
* [友链](/friends)
* 工具

  [面试题库](https://tiku.jiajunhuang.com)
  [幻灯片](https://jiajunhuang.com/page/index.md)
* [关于](/aboutme)

目录

* [AWS IAM 信任链 和 EKS IRSA](#AWS%2bIAM%2b%25E4%25BF%25A1%25E4%25BB%25BB%25E9%2593%25BE%2b%25E5%2592%258C%2bEKS%2bIRSA)
* [<strong>1. 信任链的定义</strong>](#1.%2b%25E4%25BF%25A1%25E4%25BB%25BB%25E9%2593%25BE%25E7%259A%2584%25E5%25AE%259A%25E4%25B9%2589)
* [<strong>2. 信任链的核心组件</strong>](#2.%2b%25E4%25BF%25A1%25E4%25BB%25BB%25E9%2593%25BE%25E7%259A%2584%25E6%25A0%25B8%25E5%25BF%2583%25E7%25BB%2584%25E4%25BB%25B6)
* [<strong>3. 信任链的典型场景</strong>](#3.%2b%25E4%25BF%25A1%25E4%25BB%25BB%25E9%2593%25BE%25E7%259A%2584%25E5%2585%25B8%25E5%259E%258B%25E5%259C%25BA%25E6%2599%25AF)
* [<strong>4. 信任策略（Trust Policy） vs. 访问策略（Access Policy）</strong>](#4.%2b%25E4%25BF%25A1%25E4%25BB%25BB%25E7%25AD%2596%25E7%2595%25A5%25EF%25BC%2588Trust%2bPolicy%25EF%25BC%2589%2bvs.%2b%25E8%25AE%25BF%25E9%2597%25AE%25E7%25AD%2596%25E7%2595%25A5%25EF%25BC%2588Access%2bPolicy%25EF%25BC%2589)
* [<strong>5. 最佳实践</strong>](#5.%2b%25E6%259C%2580%25E4%25BD%25B3%25E5%25AE%259E%25E8%25B7%25B5)
* [<strong>6. 常见问题排查</strong>](#6.%2b%25E5%25B8%25B8%25E8%25A7%2581%25E9%2597%25AE%25E9%25A2%2598%25E6%258E%2592%25E6%259F%25A5)

# AWS IAM 信任链 和 EKS IRSA

最近读了一下AWS IAM的文档，此外，AWS 的 EKS 可以结合 IAM 一起使用，而且是推荐的用法，可以最小权限化，
比如创建 NodeGroup 时创建一个 Node Role，默认情况下，EC2 和 里面运行的pod都会使用这个权限来运行，
如果想要将权限绑定到 pod，还可以进一步细化权限，创建 pod 的时候绑定 role：

```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-service-account
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/my-iam-role
```

pod绑定：

```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  serviceAccountName: my-service-account
  containers:
    - name: my-container
      image: my-image
```

这样 pod就可以以 `my-iam-role` 的身份来运行。

由于懒得打字，下面的部分都是 DeepSeek 总结出来的😂，总结的还怪好的咧。

---

以下是 AWS IAM 信任链的核心知识总结，帮助你快速掌握其核心概念和应用场景：

---

### **1. 信任链的定义**

IAM 信任链（Trust Chain）指通过 **角色委托（Role Assumption）** 建立的权限传递机制。
- **核心场景**：允许一个实体（用户/角色/服务）临时获取另一个角色的权限。
- **关键术语**：
- **信任策略（Trust Policy）**：定义谁（Principal）可以扮演（Assume）该角色。
- **访问策略（Access Policy）**：定义角色被扮演后拥有的具体权限。

---

### **2. 信任链的核心组件**

#### **(1) IAM 角色（Role）**

* 角色是权限的载体，本身不关联用户或资源，需被其他实体“扮演”。
* **关键字段**：

  ```
  {
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::123456789012:user/Alice"}, // 允许扮演角色的主体
    "Action": "sts:AssumeRole" // 必须包含 sts:AssumeRole 权限
  }]
  }
  ```

#### **(2) 临时凭证（Temporary Credentials）**

* 通过 STS（Security Token Service）生成，包含临时密钥、令牌和过期时间。
* 有效期默认 1 小时，可配置（15分钟至12小时）。

#### **(3) 服务相关角色（Service-Linked Roles）**

* AWS 服务自动创建的预定义角色（如 AWS Lambda 执行角色），自动信任对应服务。

---

### **3. 信任链的典型场景**

#### **(1) 跨账户访问**

* **场景**：允许 Account A 的用户访问 Account B 的资源。
* **步骤**：
  1. Account B 创建角色 Role-B，配置信任策略允许 Account A 的特定用户/角色。
  2. Account A 的用户通过 `AssumeRole` API 获取 Role-B 的临时凭证。

#### **(2) 服务间委托**

* **场景**：允许服务（如 EC2）调用其他服务（如 S3）。
* **方法**：为 EC2 实例附加 IAM 角色，角色信任策略自动允许 EC2 服务调用 `sts:AssumeRole`。

#### **(3) 身份联合（Identity Federation）**

* **场景**：允许外部身份（如企业 AD 用户）通过 SAML/OIDC 获取 AWS 临时权限。

---

### **4. 信任策略（Trust Policy） vs. 访问策略（Access Policy）**

| **对比项** | **信任策略** | **访问策略** |
| --- | --- | --- |
| **作用对象** | 角色（Role） | 用户/组/角色/资源 |
| **核心权限** | 控制谁可以扮演角色 | 控制被授权者的具体操作权限 |
| **关键 Action** | `sts:AssumeRole` | 如 `s3:GetObject`, `ec2:StartInstances` |

---

### **5. 最佳实践**

1. **最小权限原则**
   * 仅授予角色必要的权限，信任策略中严格限制可扮演角色的主体。
2. **使用外部 ID**

   * 跨账户委托时，通过 `Condition` 字段添加 `sts:ExternalId`，防止混淆代理问题。

     ```
     "Condition": {
     "StringEquals": {"sts:ExternalId": "unique-secret-id"}
     }
     ```
3. **监控与审计**

   * 启用 CloudTrail 记录 `AssumeRole` 事件。
   * 使用 IAM Access Analyzer 分析信任策略风险。

---

### **6. 常见问题排查**

* **权限冲突**：检查角色访问策略是否与用户原有权限冲突。
* **跨账户失败**：
  + 确保目标角色的信任策略包含源账户/用户 ARN。
  + 检查是否配置了 `sts:ExternalId`（如适用）。
* **服务角色无法使用**：确认服务是否支持服务相关角色，并检查信任策略中的服务标识符（如 `ec2.amazonaws.com`）。

---

通过理解信任链的机制和策略配置，可以有效管理 AWS 环境中的跨实体权限委托，提升安全性。建议结合 AWS 控制台实操角色创建和策略配置以加深理解。

---

##### 相关文章

* [Grafana Gravatar头像显示bug修复](/articles/2019_12_10-grafana_gravatar_http_hijack.md.html)
* [flutter中使用RESTful接口](/articles/2019_12_09-dart_flutter_json.md.html)
* [Vim YouCompleteMe使用LSP(以dart为例)](/articles/2019_12_04-ycm_lsp_dart.md.html)
* [flutter webview加载时显示进度](/articles/2019_12_03-flutter_webview_indicator.md.html)
* [SQLAlchemy快速更新或插入对象](/articles/2019_12_02-sqlalchemy_update_or_insert.md.html)
* [修复Linux下curl等无法使用letsencrypt证书](/articles/2019_11_26-lets_encrypt_linux_shell.md.html)
* [欣赏一下K&R两位大神的代码](/articles/2019_11_24-code_from_k_and_r.md.html)
* [MySQL的ON DUPLICATE KEY UPDATE语句](/articles/2019_11_19-mysql_duplicate_key_update.md.html)
* [使用microk8s快速搭建k8s](/articles/2019_11_17-microk8s.md.html)
* [Python中优雅的处理文件路径](/articles/2019_11_15-python_pathlib_path.md.html)
* [Go语言MySQL时区问题](/articles/2019_11_14-golang_mysql_timezone.md.html)
* [我的技术栈选型](/articles/2019_11_13-tech_stack.md.html)
* [为什么我要用Linux作为桌面？](/articles/2019_11_11-why_linux_as_desktop.md.html)
* [disqus获取评论时忽略query string](/articles/2019_11_08-disqus_thread_identifier.md.html)
* [MySQL性能优化指南](/articles/2019_11_06-mysql.md.html)

---

加载评论

* [![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=dedfc09c3066&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
* [![](/static/email.png)
  邮件 订阅](https://eepurl.com/guVPMj)
* [![](/static/rss.png)
  RSS 订阅](/rss)
* [![](/static/web.png)
  Web开发简介系列](/articles/2017_10_19-web_dev_series.md.html)
* [![](/static/computer.png)
  数据结构的实际使用](/tutorial/data_structure/index.md)
* [![](/static/golang.png)
  Golang 简明教程](/tutorial/golang/index.md)
* [![](/static/python.png)
  Python 教程](/tutorial/python/index.md)

本站热门

* [socks5 协议详解](/articles/2019_06_06-socks5.md.html)
* [zerotier简明教程](/articles/2019_09_11-zerotier.md.html)
* [搞定面试中的系统设计题](/articles/2019_04_29-system_design.md.html)
* [frp 源码阅读与分析(一)：流程和概念](/articles/2019_06_11-frpc_source_code_part1.md.html)
* [用peewee代替SQLAlchemy](/articles/2020_05_29-use_peewee.md.html)
* [Golang(Go语言)中实现典型的fork调用](/articles/2018_03_08-golang_fork.md.html)
* [DNSCrypt简明教程](/articles/2019_10_31-dnscrypt.md.html)
* [一个Gunicorn worker数量引发的血案](/articles/2020_03_11-gunicorn_worker.md.html)
* [Golang validator使用教程](/articles/2020_04_10-golang_validator.md.html)
* [Docker组件介绍（二）：shim, docker-init和docker-proxy](/articles/2018_12_24-docker_components_part2.md.html)
* [Docker组件介绍（一）：runc和containerd](/articles/2018_12_22-docker_components.md.html)
* [使用Go语言实现一个异步任务框架](/articles/2020_04_24-gotasks.md.html)
* [协程(coroutine)简介 - 什么是协程？](/articles/2018_04_03-coroutine.md.html)
* [SQLAlchemy简明教程](/articles/2019_10_30-sqlalchemy.md.html)
* [Golang的template(模板引擎)简明教程](/articles/2019_08_23-golang_html_template.md.html)

[@jiajunhuang](https://github.com/jiajunhuang) 2015-2024, All Rights Reserved。本站禁止转载，引用请注明作者与原链。