---
title: 10分漏洞：GitLab未授权任意文件读取
url: https://mp.weixin.qq.com/s/RJQI_HqqfmcS-3ImEvAXYQ
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T07:00:10.029025
---

# 10分漏洞：GitLab未授权任意文件读取

# 10分漏洞：GitLab未授权任意文件读取

零日手记
零日手记

随笔漫记安全路

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

9月11日，vulhub提交了CVE-2026-85706的完整复现环境和PoC。这个漏洞允许未认证攻击者读取GitLab服务器上的任意本地文件——不需要登录，只需要目标GitLab上存在一个公开项目。

GitLab CE和EE都受影响。

---

**漏洞根因：Workhorse与Rails的路径理解不一致**

GitLab的架构中，Workhorse是前置代理，负责处理大文件上传等请求；Rails是后端应用服务器。漏洞出在两者对同一个URL路径的理解不一致。

**关键绕过：末尾斜杠**

GitLab Workhorse有一条严格锚定的上传路由，用于匹配`/repository/commits`。攻击者在路径末尾加一个斜杠——`/repository/commits/`——Workhorse的严格锚定匹配失败，不把这个请求当作上传请求处理。

但GitLab Rails仍然把这个请求路由到Repository Commits API。

**攻击链：**

1. 攻击者无需认证，查询GitLab的公开项目API，找到一个公开项目
2. 向`/api/v4/projects/{project_id}/repository/commits/`发送POST请求，Content-Type为`application/x-www-form-urlencoded`
3. 请求体中包含`file.path`参数，指向服务器上的任意本地路径（如`/var/opt/gitlab/gitlab-rails/etc/gitlab.yml`）
4. Workhorse不匹配上传路由，直接转发给Rails
5. Rails在认证用户之前先读取该文件
6. 如果文件内容包含特殊字符（如百分号序列），触发Rack表单解析器的反射型错误——文件内容出现在HTTP 400响应中

**核心问题：Rails在认证之前就读取了文件。** 认证是后面才做的，但文件已经读进内存了，内容通过错误响应泄露出来。

---

**PoC分析**

vulhub提供的PoC脚本（poc.py）非常简洁：

```
TARGET_PATH = "/var/opt/gitlab/gitlab-rails/etc/gitlab.yml"

# 1. 无认证查询公开项目
GET /api/v4/projects?visibility=public&simple=true&per_page=100

# 2. 向Commits API末尾加斜杠绕过Workhorse
POST /api/v4/projects/{id}/repository/commits/
Content-Type: application/x-www-form-urlencoded

# 3. 请求体中指定要读取的文件路径
file=&file.path=/var/opt/gitlab/gitlab-rails/etc/gitlab.yml&file.size=1&Content-Type=application/x-www-form-urlencoded
```

目标文件选择`gitlab.yml`——这是GitLab Omnibus启动时自动生成的配置文件，包含数据库连接、密钥、SMTP配置等敏感信息。而且这个文件本身包含百分号序列，能触发Rack的反射型解析错误，内容直接出现在HTTP 400响应体中。

---

**内容泄露的条件性**

漏洞代码会读取任意可访问路径，但内容是否泄露取决于文件内容：

* **能泄露的文件**：内容包含特殊字符序列（如百分号），触发Rack表单解析器的反射型错误，文件内容出现在错误响应中
* **不能泄露的文件**：内容能被正常解析（如纯文本`/etc/passwd`），文件被读取但不一定出现在响应中

PoC选择`gitlab.yml`正是因为它是应用原生生成的文件，内容确定能触发泄露——不需要往镜像里塞任何构造数据。

---

**影响版本**

| 版本范围 | 受影响 |
| --- | --- |
| 18.7.0 - 19.1.7 | 受影响 |
| 19.2.0 - 19.2.5 | 受影响 |
| 19.3.0 - 19.3.1 | 受影响 |

修复版本：19.1.8、19.2.6、19.3.2。

---

**前置条件**

1. GitLab版本在受影响范围内
2. 目标GitLab上存在至少一个公开项目（公开项目是匿名访问漏洞接口的前提）
3. 攻击者能访问GitLab的Web端口（不需要登录）

公开项目这个条件门槛很低——大量GitLab实例用于开源项目托管，默认就有公开项目。

---

**泄露什么有价值**

`gitlab.yml`中包含：

* 数据库连接配置（PostgreSQL主机、端口、数据库名）
* Redis配置
* GitLab密钥（secret\_key、otp\_key等）
* SMTP邮件配置
* LDAP/SSO配置
* 对象存储配置（S3/OSS密钥）

拿到这些配置信息后，攻击者可以进一步攻击内网数据库、Redis、对象存储，甚至伪造会话Cookie接管管理员账号。

---

**修复建议**

1. **立即升级到修复版本**：19.1.8 / 19.2.6 / 19.3.2
2. 如果暂时无法升级，临时缓解：限制GitLab Web端口的公网访问，只允许VPN/内网访问
3. 检查`gitlab.yml`中的密钥是否曾泄露——如果GitLab曾暴露在公网且有公开项目，假设配置文件已被读取
4. 轮换以下凭据：数据库密码、Redis密码、secret\_key、对象存储密钥、SMTP密码
5. 检查GitLab访问日志中是否有对`/api/v4/projects/*/repository/commits/`（注意末尾斜杠）的异常POST请求

---

**参考链接**

* GitLab官方补丁发布：docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
* 修复commit：gitlab.com/gitlab-org/gitlab/-/commit/0d9ce3e758a85f0690be751e213625f7902c0361
* CVE记录：cve.org/CVERecord?id=CVE-2026-85706
* vulhub复现环境+PoC：github.com/vulhub/vulhub/pull/800

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/euBEasB1QK1mSyV63n51RYwjUnANgONCBIoG7rlnVw75VBa0K8ZtSh9RmNQBsX1ibHXx1Gw8emQgIjJAeNmdJGg/0?wx_fmt=png)

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