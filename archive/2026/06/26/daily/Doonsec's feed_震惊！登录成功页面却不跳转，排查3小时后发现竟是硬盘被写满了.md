---
title: 震惊！登录成功页面却不跳转，排查3小时后发现竟是硬盘被写满了
url: https://mp.weixin.qq.com/s/zBucQQ4uPbxySiaicKH73w
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:49:20.603773
---

# 震惊！登录成功页面却不跳转，排查3小时后发现竟是硬盘被写满了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6ynCILojBKquVZnOQP9gKdzEDCTPHMYhd3rE5lC29acDEWNr7SxTUupHBhIat76ic2rIB2gk43at6I4j8NmuRznfvskM3iaGZMFO3j4lZ6ftM/0?wx_fmt=jpeg)

# 震惊！登录成功页面却不跳转，排查3小时后发现竟是硬盘被写满了

原创

刘军军
刘军军

运维星火燎原

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/6ynCILojBKqwXiahv8OUWTNq7L5Sh1nehFH2OYJbyLIDmzianUNNEoIP4iaibrCktRovlVcnqJBbYNj9otVQbJQiaj4Yag0dGvTVB0MhnU74Vk2w/640?wx_fmt=png&from=appmsg)

## 一、问题现象

用户在某生产环境进行登录操作，输入用户名和密码后，系统提示"登录成功"，但页面始终不跳转，仍然停留在登录页面。用户可以反复登录，系统始终提示成功，但就是无法进入系统首页。

## 二、排查思路

遇到"登录成功但页面不跳转"的问题，通常从以下几个方向排查：

| 排查方向 | 可能原因 |
| --- | --- |
| 前端问题 | 路由配置错误、跳转逻辑失效、JavaScript错误 |
| 后端问题 | Session未正确创建、Cookie未返回、接口返回格式错误 |
| 网络问题 | 请求被拦截、响应被篡改、WebSocket异常 |
| 存储问题 | Session存储失败、磁盘满导致写入异常 |

## 三、详细排查过程

### 第一步：检查浏览器控制台

打开浏览器F12开发者工具，切换到Console和Network标签：

* **Console发现**：有JavaScript错误，但错误信息不明确
* **Network发现**：登录接口`/api/login`返回200状态码，响应体显示`{"code":0,"message":"登录成功","data":{...}}`

```
 // 控制台看到类似错误
 UncaughtTypeError: Cannotreadproperty'token'ofnull
```

### 第二步：检查登录接口响应

查看登录接口返回的完整数据：

```
 {
  "code": 0,
  "message": "登录成功",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user_id": 1001,
    "username": "admin"
  }
 }
```

后端返回数据正确，前端应该接收到token。但页面仍然不跳转。

### 第三步：检查前端登录逻辑

查看前端登录处理代码：

```
 async function handleLogin() {
  const response=await fetch('/api/login', {
    method: 'POST',
    body: JSON.stringify({ username, password })
  });
  const data=await response.json();

  if (data.code===0) {
    localStorage.setItem('token', data.data.token);  // 这里出问题了
    router.push('/dashboard');  // 跳转失败但不报错
  }
 }
```

代码看起来没问题，但`localStorage.setItem`可能静默失败。

### 第四步：检查浏览器localStorage

在浏览器控制台执行：

```
 localStorage.setItem('test', 'value');
 console.log(localStorage.getItem('test'));
```

结果：`null` —— localStorage无法写入！

### 第五步：检查后端日志

登录后端服务器，查看应用日志：

```
 tail -f /var/log/myapp/app.log
```

发现大量错误：

```
 ERROR - Failed to write session file: No space left on device
 ERROR - Cannot create temp file: No space left on device
 ERROR - Failed to write to /var/log/myapp/access.log
```

### 第六步：检查磁盘空间

```
 df -h
```

```
 Filesystem      Size  Used  Avail  Use%  Mounted on
 /dev/sda1       100G  100G    0G   100% /
```

**根因确认**：磁盘使用率100%，硬盘已写满！

## 四、问题根因分析

### 为什么登录成功但页面不跳转？

1. **登录流程**：

* 用户提交用户名密码到后端
* 后端验证成功，**尝试创建Session写入磁盘**
* 磁盘已满，Session写入失败（但后端可能未返回错误）
* 后端返回登录成功给前端
* 前端接收到成功响应，尝试将token存入localStorage
* localStorage受磁盘满影响也失败（浏览器需要写临时文件）
* 前端执行`router.push('/dashboard')`跳转
* 由于某些校验或状态异常，跳转被阻止

2. **为什么后端显示登录成功？**

* 后端在验证用户名密码阶段就返回成功
* Session写入是后续步骤，后端可能捕获了异常但仍返回成功
* 或者后端根本没有校验Session写入是否成功

### 硬盘写满导致的其他问题

| 问题 | 原因 |
| --- | --- |
| Session失效 | Session文件无法写入 |
| 日志不记录 | 日志文件无法写入 |
| 图片上传失败 | 临时文件无法创建 |
| 数据库写入变慢 | Write-Ahead日志无法刷盘 |
| SSH登录缓慢 | 系统需要写utmp/wtmp |

## 五、解决过程

### 紧急处理

```
 # 1. 清理临时文件
rm -rf /tmp/*
rm -rf /var/tmp/*

# 2. 清理旧日志
find /var/log -name "*.log" -mtime+7 -delete

# 3. 清理包管理器缓存
yum clean all
apt-get clean

# 4. 清理旧的核心转储文件
 find / -name "core.*" -delete 2>/dev/null
```

### 清理完成后检查

```
 df -h
```

```
 Filesystem      Size  Used  Avail  Use%  Mounted on
 /dev/sda1       100G   85G   15G   85% /
```

磁盘恢复到85%，有15G可用空间。

### 验证登录

重新测试登录功能，页面正常跳转，问题解决。

## 六、预防措施

### 1. 监控磁盘使用率

```
 # 添加cron任务，每天检查磁盘并告警
 0 0 * * * df -h | grep -E 'Use%|used' | awk '{if($5>85) print $0}' | mail -s "Disk Warning" admin@example.com
```

### 2. 日志轮转配置

```
 # /etc/logrotate.conf
/path/to/log {
    daily
    rotate 7
    compress
    delaycompress
    notifempty
    missingok
    maxsize 100M
 }
```

### 3. 设置磁盘空间告警阈值

| 阈值 | 动作 |
| --- | --- |
| 80% | 发送警告邮件 |
| 90% | 自动清理临时文件 |
| 95% | 自动清理旧日志 |

### 4. 应用程序端优化

```
 # 后端登录时增加磁盘检查
importshutil

defcheck_disk_space():
    total, used, free=shutil.disk_usage("/")
    iffree/total<0.1:  # 少于10%可用
        raiseException("Disk space critically low")

@app.route('/api/login')
deflogin():
    check_disk_space()  # 登录前检查
     # ... 后续登录逻辑
```

## 七、经验总结

1. **隐蔽性强**：硬盘写满不一定直接报错，可能表现为各种奇怪的功能异常
2. **排查要全面**：不要只看报错信息，要检查底层资源（磁盘、内存、网络）
3. **日志是关键**：应用日志中往往藏着真相
4. **监控要到位**：在问题发生前发现才能避免损失
5. **Session存储**：生产环境应使用Redis等内存存储，避免磁盘依赖

这个案例告诉我们，看似简单的登录问题，背后可能涉及服务器资源耗尽，需要系统性的排查思路才能定位根因。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/G7WSQyicBkgj2B5jst2Cx1Bx9b3NfXBzOmPldmsqoKWoyWr0s3BibONOSicegTCQVvdls7fkG4YchibVBXha6b6dqQ/0?wx_fmt=png)

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