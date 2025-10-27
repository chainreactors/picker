---
title: 如何保护 Web 应用程序免受密码破解（下）
url: https://www.4hou.com/posts/7JP1
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-12
fetch_date: 2025-10-04T03:38:20.098797
---

# 如何保护 Web 应用程序免受密码破解（下）

如何保护 Web 应用程序免受密码破解（下） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 如何保护 Web 应用程序免受密码破解（下）

walker
[技术](https://www.4hou.com/category/technology)
2023-01-11 11:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)119726

收藏

导语：在本文中，我们讨论了密码破解的危险并提供了减少恶意身份验证尝试的最佳实践。

[如何保护 Web 应用程序免受密码破解（上）](https://www.4hou.com/posts/6VOR)

**什么是 Fail2ban，它是如何工作的？**

Fail2ban是一种用于扫描日志文件、检测可疑活动（例如过多失败的身份验证尝试）并阻止潜在恶意 IP 地址的工具。

这项免费服务有助于保护 Linux 机器免受暴力破解和其他自动攻击。通常，Fail2ban 用于更新防火墙规则以在指定时间内拒绝 IP 地址。

Fail2ban 具有以下优点：

* 易于设置
* 免费使用
* 可以与大量应用程序交互
* 提供大量配置参数
* 易于监控当前保护状态
* 与各种通知服务集成

尽管 Fail2ban 可以帮助您最大程度地减少不正确的身份验证尝试次数，并在一定程度上降低密码破解和未经授权访问的风险，但这并不是灵丹妙药。

不利的一面是，Fail2ban 无法解决因服务器身份验证策略薄弱而出现的问题。即使是最好的 Fail2ban 配置也不能替代我们上面讨论的密码保护最佳实践。此外，Fail2ban 仅适用于 Linux，不适用于 IPv6。

为了有效地保护您的服务，您还可以应用用于多因素和公共/私人身份验证机制的工具。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673423507190065.png "1673422554148156.png")

Fail2ban 优缺点

**Fail2ban 如何运作？**

以下是对其机制的简单解释：

1. 任何应用程序或服务器总是将日志保存在特定文件中，包括失败的身份验证尝试的唯一日志。
2. Fail2ban 扫描这些文件，搜索与身份验证失败相关的日志。
3. 如果检测到失败的身份验证尝试，Fail2ban 会保存尝试时间和负责的 IP 地址。
4. Fail2ban 计算在指定时间段内来自同一 IP 的失败身份验证尝试。
5. 如果 IP 地址超过允许的尝试次数，Fail2ban 会创建一个新的防火墙规则来阻止此 IP 地址。

结果，可疑的 IP 地址将失去访问服务器的能力。经过一段可配置的时间后，IP 地址可以自动解禁，也可以手动解禁。

例如，您可以配置 Fail2ban，如果任何威胁行为者开始密码破解攻击，他们的 IP 地址将被禁止五个小时。

现在，让我们探索配置过程本身。

**如何配置 Fail2ban**

您可以配置 Fail2ban 来读取不同应用程序的日志。开箱即用，此工具可以与以下应用程序类型交互：

* SSH 服务器
* HTTP 服务器
* 网络邮件和群件服务器
* 网络应用
* HTTP 代理服务器
* FTP服务器
* 邮件服务器
* 邮件服务器验证器
* DNS 服务器
* 来自不同类别的各种服务器应用程序

默认情况下，Fail2ban 启用使用sshd的通信，这是一个 OpenSSH 服务器进程。这意味着在多次 SSH 身份验证尝试失败后，负责的 IP 地址将被禁止。

为了与任何应用程序交互，Fail2ban 使用Jail，它是一个过滤器和一个或多个操作的组合。此交互允许您在身份验证尝试失败后禁止 IP 地址。

默认情况下， Jail配置保存在 jail.conf 文件中。如果要更改默认设置，请复制配置文件并将副本命名为 jail.local。如果 jail.local 文件存在，Fail2ban 将自动使用它而不是默认文件。

我们不建议更改原始配置文件，因为如果出现任何错误，返回默认设置将是一个挑战。此外，一旦安装了 Fail2ban 的新更新，jail.conf 文件也将更新，所有自定义设置都将消失。

以下是 Fail2ban 如何确定失败的身份验证尝试：

1. 该工具具有写入 jail.local 配置文件中的服务日志文件的路径。
2. 失败的身份验证日志和常规异常会自动添加到 Fail2ban 文本过滤器中。
3. 该工具使用文本过滤器扫描日志文件。

如果您打开配置文件，您会发现一个相当大的 Fail2ban 可以与之交互的应用程序列表。这些应用程序的名称在括号中，如下面的示例代码所示：

```
# Mail servers
[assp]
port = smtp,465,submission
logpath = /root/path/to/assp/logs/maillog.txt
[courier-smtp]
port = smtp,465,submission
logpath = %(syslog_mail)s
backend = %(syslog_backend)s
[postfix]
# To use another modes set filter parameter "mode" in jail.local:
mode = more
port = smtp,465,submission
logpath = %(postfix_log)s
backend = %(postfix_backend)s
[postfix-rbl]
filter = postfix[mode=rbl]
port = smtp,465,submission
logpath = %(postfix_log)s
backend = %(postfix_backend)s
maxretry = 1
```

默认情况下，Fail2ban 被配置为仅使用 SSH，所有其他通信协议都被禁用。如果需要开启其他类型的通信，在配置文件中找到需要的类型，添加如下字符串：

```
enabled = true
```

这是一个例子：

```
[nginx-http-auth]
enabled = true
port = http, https
logpath = %(nginx_error_log)s
```

如果需要，您还可以更改与特定应用程序交互的现有参数或添加新参数。以下是常用参数列表：

* ignoreip指定要被 Fail2ban 忽略的 IP 地址。默认情况下，此参数设置为忽略当前机器的流量。
* bantime 以秒为单位设置禁令持续时间。默认值为 600 秒。
* findtime定义了监视来自每个 IP 地址的失败身份验证尝试的时间段。默认值为 600 秒。
* maxretry指定在 findtime 指定的时间内每个地址的失败登录尝试限制。
* usedns确定是否使用反向 DNS 进行阻止。如果设置为 NO，那么 Fail2ban 将阻止 IP 地址而不是主机名。如果设置为 YES，该工具将尝试使用反向 DNS 来查找主机名并阻止它。默认值为 WARN。它的工作方式与 YES 值一样，但也会记录警告。系统工程师稍后可以查看所有警告。
* 协议指定将被阻止的流量类型。默认情况下它是 TCP。
* port指定要禁止的端口。
* logpath显示日志文件的路径。

注意：上面的列表并未描述所有 Fail2ban 参数。您可以在配置文件中找到所有这些。

您可以在 /etc/fail2ban 文件夹中的文件中的日志路径参数中找到默认设置的日志文件路径（例如，上面代码示例中的 nginx\_error\_log ） ：

* paths-common.conf — 具有默认服务日志路径的文件
* paths-opensuse.conf、paths-arch.conf、paths-debian.conf — 包含不同 Linux 系统特定路径的文件

如果您打开上面提到的文件，您可以看到类似于这些的日志文件的路径：

```
apache_error_log = /var/log/apache2/*error.log
apache_access_log = /var/log/apache2/*access.log
auditd_log = /var/log/audit/audit.log
exim_main_log = /var/log/exim/mainlog
nginx_error_log = /var/log/nginx/*error.log
nginx_access_log = /var/log/nginx/*access.log
```

如有必要，您可以编辑过滤器以指示应在日志中搜索哪些文本以确定失败的身份验证。每个过滤器都位于 /etc/fail2ban/filter.d 文件夹中的单独文件中。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673423508118991.png "1673422796128295.png")

屏幕截图 1. /etc/fail2ban/filter.d文件夹中的过滤器列表

当您打开任何过滤器文件时，您将看到一个正则表达式，其中包含所需的失败身份验证文本，如下例所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673423510196922.png "1673422832112602.png")

屏幕截图 2. 验证失败的过滤文本

配置完成后，使用以下命令重新加载 Fail2ban：

```
sudo fail2ban-client reload
```

如果您只更改一个Jail文件的设置，则无需重新启动该工具。只需使用此命令重新加载它：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673423510168996.png "1673422880110118.png")

此外，您可以将 Fail2ban 配置为与配置文件中不存在的任何应用程序进行交互。您需要做的就是如上所述添加您的自定义配置。

**如何使用 Fail2ban**

要检查当前启用了哪些Jails ，请使用以下命令：

```
sudo fail2ban-client status
```

以下是响应示例：

```
Status
|- Number of jail: 2
`- Jail list: nginx-http-auth, sshd
```

如您所见，服务器上启用了nginx-http-auth 和 sshd Jails 。如果你想检查任何Jail参数的值，你不需要打开配置文件；只需使用以下命令：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673423511970876.png "1673422932876312.png")

下面的代码示例向我们展示了 sshd Jail maxretry 等于 5：

```
sudo fail2ban-client get sshd maxretry 5
```

如果Jail超过其失败身份验证尝试的限制，Fail2ban 将禁止在Jail配置中为 IP 地址指定的端口。要检查Jail状态，请使用以下命令：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673423511120202.png "1673422950195015.png")

下面是一个响应示例，向我们展示了两个 IP 地址当前被禁止进行 SSH 访问：

```
Status for the jail: sshd
|- Filter
|  |- Currently failed:     0
|  |- Total failed:            25
|  `- File list:                  /var/log/auth.log
`- Actions
   |- Currently banned: 2
   |- Total banned:        5
   `- Banned IP list:      192.168.10.107 192.168.10.115
```

如果您尝试在您的 IP 在禁止列表中时访问服务器，您会收到如下所示的“连接被拒绝”错误：

```
ssh: connect to host 192.168.10.105 port 22: Connection refused
```

如果 IP 地址被任何 HTTP 服务器Jail禁止，错误将类似于：

```
curl: (7) Failed to connect to 192.168.10.105 port 80: Connection refused
```

您还可以使用以下命令手动将任何 IP 地址添加到禁止列表：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673423512426680.png "1673422980128048.png")

这是一个例子：

```
sudo fail2ban-client set nginx-http-auth banip 10.100.1.210
```

要手动取消禁止 IP 地址，请使用以下命令：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673423513149433.png "1673423001538566.png")

这是一个例子：

```
sudo fail2ban-client set nginx-http-auth unbanip 10.100.1.210
```

考虑到这一点，让我们开始在 Fail2ban 中配置通知。

**如何配置 Viber 聊天机器人以接收 Fail2ban 通知**

如果要监控 Fail2ban 活动，请使用以下三个步骤配置实时活动通知：

1. 配置您要使用的任何通知服务
2. 准备 Fail2ban 动作配置文件
3. 更新jail.local 文件中的action参数值

Fail2ban 具有使用电子邮件服务的配置。您需要做的就是在服务器上配置服务。

但是，如果您想通过 Viber 等消息服务获取通知怎么办？让我们讨论如何配置它！

首先，要将 Viber 用作通知服务，您需要创建一个 Viber 聊天机器人。您可以在Viber API 文档页面上找到有关 Viber 聊天机器人设置和配置的文档。

一旦您的聊天机器人准备就绪，请务必执行以下步骤：

1. 获取 Viber 聊天机器人的身份验证令牌。您可以在Viber 管理面板页面上找到它。

2.在订阅 Viber 聊天机器人的所有用户列表中找到您的用户 ID。为此，请使用以下 HTTP 请求：

![image.png](https://img.4hou.com/uploads...