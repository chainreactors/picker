---
title: 网络安全攻击载荷深度分析报告
url: https://mp.weixin.qq.com/s/z3J_js7CycPWpurXhK6F_A
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:44:44.095493
---

# 网络安全攻击载荷深度分析报告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RehIIpPl1Mqqg4icGJKvick5u627uiaTHJ06n0lb0e5IzykzvcwbrqQ2q7xa76MfthvFAlJpOZYImiaib26Doxr0uDqgz6wPHzfp5oauxlFbbeJc/0?wx_fmt=jpeg)

# 网络安全攻击载荷深度分析报告

归不去的光影

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、案例一：TCL官网疑似攻击探测

---

1.1 原始请求
http://www.tcl.com/About/about\_team\_detail/aid/${@print(phpinfo())}.html

1.2 攻击类型
服务器端模板注入（SSTI）与代码注入混合型探测。

1.3 载荷逐层拆解
[${...}]：PHP/模板引擎变量解析语法，试探是否执行表达式。
[@]：PHP错误控制运算符，抑制报错，静默探测。
[print()]：PHP输出函数，将结果返回到页面。
[phpinfo()]：PHP内置函数，输出完整PHP环境配置（版本、路径、禁用函数等），用于信息收集。

1.4 攻击链
发送请求 -> 服务器尝试解析${...} -> 若成功则执行phpinfo() -> 返回敏感信息 -> 攻击者分析输出，寻找可利用点（如未禁用的函数、可写路径、已知漏洞版本）。

1.5 修复方案（代码示例）
不安全写法：
aid=aid=\_GET['aid'];
文章：aid}</body></html>";
eval("?>" . $template . "<?php");

安全写法：
方案1（强类型转换）：aid=(int)aid=(int)\_GET['aid'];
方案2（HTML转义）：aid=htmlspecialchars(aid=htmlspecialchars(\_GET['aid'], ENT\_QUOTES, 'UTF-8');
方案3（白名单）：allowedids=[1,2,3,4,5];if(!inarray(allowedids=[1,2,3,4,5];if(!inarray(\_GET['aid'], $allowed\_ids)) { die('非法请求'); }

二、案例二：路径遍历攻击

---

2.1 原始请求
http://localhost/admincp.php?c=templet&a=delfile&id=%5C%5C..%5C%5C..%5C%5C..%5C%5C%2Findex.php

2.2 攻击类型
路径遍历（Directory Traversal），试图删除网站根目录的index.php。

2.3 载荷拆解
%5C%5C -> 解码为 \（双反斜杠，用于绕过过滤）
%2F -> 解码为 /（Linux路径分隔符）
最终路径：\..\..\..\/index.php，表示从当前目录向上跳转三级，指向根目录的index.php。

2.4 漏洞存在条件
(1) id参数未经过滤直接拼接到文件路径。
(2) Web服务器进程对目标文件有删除权限。
(3) 攻击者能绕过后台登录验证或存在越权漏洞。

2.5 修复方案
多层防御：
(1) 白名单过滤：preg\_match('/^[a-zA-Z0-9\_-.]+/′,/′,id)
(2) 使用basename()剥离路径信息。
(3) 使用realpath()验证最终路径是否在允许的基目录内。
(4) 确认文件存在且为常规文件（is\_file()）。

三、案例三：命令注入攻击

---

3.1 原始请求（POST数据）
login=%b5%c7%c2%bc&action=useraction&passwd=123456&username=%22set%7cset%26set%22

3.2 参数解码
login：%b5%c7%c2%bc -> "登录"（GBK编码）
username：%22set%7cset%26set%22 -> "set|set&set"

3.3 攻击载荷含义
["]：闭合双引号，逃逸原有字符串上下文。
[|]：管道符，将前一个命令的输出传递给后一个命令。
[&]：命令连接符（Windows顺序执行，Linux后台执行）。
[set]：查看环境变量的命令，用于信息收集。

3.4 攻击推演（假设后端代码）
不安全代码：
username=username=\_POST['username'];
system("echo " . $username . " >> logs/user.log");

正常输入：admin -> 执行 echo admin >> logs/user.log
攻击输入："set|set&set" -> 执行 echo "set|set&set" >> logs/user.log
后续演化："& whoami &" -> 额外执行 whoami 命令

3.5 修复方案
(1) 使用 escapeshellarg() 转义参数。
(2) 使用 escapeshellcmd() 转义命令中的特殊字符。
(3) 最佳实践：避免使用系统命令，改用纯语言功能（如 file\_put\_contents()）。

四、案例四：Elasticsearch远程代码执行

---

4.1 原始请求
http://xxx.com:9200/\_search?source={%22size%22:1,%22query%22:{%22filtered%22:{%22query%22:{%22match\_all%22:{}}}},%22script\_fields%22:{%22exp%22:{%22script%22:%22import%20java.util.*;\nimport%20java.io.*;\nString%20str%20=%20%22%22;BufferedReader%20br%20=%20new%20BufferedReader(new%20InputStreamReader(Runtime.getRuntime().exec(%22ifconfig%22).getInputStream()));StringBuilder%20sb%20=%20new%20StringBuilder();while((str=br.readLine())!=null){sb.append(str);}sb.toString();%22}}}

4.2 攻击类型
远程代码执行（RCE），漏洞编号：CVE-2014-3120（已修复）。

4.3 核心攻击原理
通过Elasticsearch的script\_fields功能，注入Groovy/Java脚本。
脚本中调用 Runtime.getRuntime().exec("ifconfig") 执行系统命令。
命令执行结果通过搜索结果返回给攻击者。

4.4 脚本代码拆解
(1) 导入 java.util.\* 和 java.io.\*。
(2) 获取 Runtime 对象，执行 "ifconfig" 命令。
(3) 通过 BufferedReader 读取命令输出。
(4) 将输出拼接为字符串并返回。

4.5 漏洞根因
Elasticsearch 1.x版本默认启用动态Groovy脚本 -> 未启用安全沙盒 -> 可直接调用Java API -> 可执行任意系统命令。

4.6 现代版本风险（2026年最新）
该特定漏洞已修复，但攻击向量已迁移到 sort\_query、function\_score 等新参数。
核心问题未变：用户可控参数被传递给脚本引擎执行。
配置不当（未设置 script.allowed\_types 和 script.allowed\_contexts）仍可导致风险。

4.7 Elasticsearch安全配置

# elasticsearch.yml

script.disable\_dynamic: true # 禁用所有动态脚本（最严格）
script.allowed\_types: inline # 只允许内联脚本
script.allowed\_contexts: score,update # 限制使用场景
script.default\_lang: painless # 使用安全的Painless脚本
http.host: 127.0.0.1 # 仅监听本地，不暴露公网

4.8 检测是否被攻击
检查日志：grep -E "script\_fields|Runtime.exec|Groovy" /var/log/elasticsearch/*.log
检查进程：ps aux | grep -E "wget|curl|nc|bash -i"
检查文件：find /usr/share/elasticsearch/ -name "*.jar" -mtime -7

五、组件知识深度整理

---

5.1 JEECMS漏洞全景
[漏洞类型] [影响版本] [攻击后果] [修复版本]
文件上传（Webshell） V6.0-V7.0 获取服务器权限 V9.0+
远程代码执行 V6.x-V8.x 执行任意命令 补丁/V9.0+
Struts2 RCE V6.x 执行任意命令 V9.0+
存储型XSS X1.1, 9.3 窃取Cookie 安全补丁
CSRF 9.3 添加非法管理员 安全补丁
SSRF 9.3 内网探测 安全补丁
OpenSSL依赖漏洞 V7及以下 信息泄露/拒绝服务 升级V9或手动更新系统库

真实攻击案例：
攻击者利用文件上传漏洞获取权限 -> 篡改Tomcat的spring-security-filter依赖包 -> 植入恶意过滤器，对搜索引擎返回黑链内容，对移动端用户跳转非法网站 -> 篡改时间戳和日志隐藏痕迹。

5.2 OpenSSL深度解析
性质：开源的SSL/TLS加密库（C语言实现）。
核心功能：数据加密（AES/RSA）、身份认证（X.509证书）、完整性校验（SHA）。
应用范围：Web服务器（Nginx/Apache）、操作系统、数据库、VPN、编程语言。
历史重大漏洞：Heartbleed（CVE-2014-0160）、POODLE（CVE-2014-3566）、DROWN（CVE-2016-0800）。

查看版本：openssl version -a

六、统一安全防御框架

---

6.1 输入处理六原则
(1) 永远不要信任用户输入。
(2) 先验证后处理（白名单优于黑名单）。
(3) 输出时转义（根据上下文选择正确方式）。
(4) 使用参数化查询（SQL/命令/模板）。
(5) 最小权限运行（进程、用户、文件权限）。
(6) 深度防御（多层安全机制）。

6.2 攻击类型与防御对照表
SSTI -> 分离代码与数据、转义 -> htmlspecialchars()
路径遍历 -> 路径规范化、白名单 -> realpath(), basename()
命令注入 -> 使用API替代命令、转义 -> escapeshellarg()
RCE（脚本引擎） -> 禁用动态脚本、沙盒 -> script.disable\_dynamic
文件上传 -> 校验MIME、重命名、隔离存储 -> 文件类型白名单
XSS -> 输出编码、CSP -> htmlspecialchars(), Content-Security-Policy
CSRF -> Token验证、SameSite Cookie -> csrf\_token, SameSite=Strict
SSRF -> URL白名单、内网IP过滤 -> 限制协议和端口

6.3 应急响应流程
发现攻击迹象 -> 确认攻击来源（分析日志） -> 隔离受影响系统 -> 保留现场证据 -> 清除攻击载荷 -> 修复漏洞 -> 更改所有密码 -> 重新审计 -> 形成报告

七、附录：快速查询表

---

7.1 常见端口与服务
80/443 - HTTP/HTTPS - Web应用漏洞
9200 - Elasticsearch - RCE（脚本注入）
6379 - Redis - 未授权访问
3306 - MySQL - 弱口令、SQL注入
22 - SSH - 暴力破解

7.2 关键安全配置速查
disable\_functions（PHP）：禁用 phpinfo, system, exec, shell\_exec, passthru 等
open\_basedir（PHP）：限制为项目目录
script.disable\_dynamic（ES）：设为 true
http.host（ES）：设为 127.0.0.1 或内网IP
bind（Redis）：设为 127.0.0.1
requirepass（Redis）：设置强密码
bind-address（MySQL）：绑定内网IP

声明：此报告仅限于学习，禁止用于任何非法用途

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/RehIIpPl1MpoSjjUbkjqaOq9rHqJGCicrk61XDTiabsXyxBlumhvqeULPvibjRetD66f778UOENzHdFZ6ibkUF2vTGQL4u1Jv0ygJHFW8cGnVCc/0?wx_fmt=png)

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