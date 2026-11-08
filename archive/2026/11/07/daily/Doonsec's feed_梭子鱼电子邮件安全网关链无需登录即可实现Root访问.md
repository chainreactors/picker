---
title: 梭子鱼电子邮件安全网关链无需登录即可实现Root访问
url: https://mp.weixin.qq.com/s/c9xnFHdSD7BI7lN1qhFIyQ
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:11:01.575514
---

# 梭子鱼电子邮件安全网关链无需登录即可实现Root访问

# 梭子鱼电子邮件安全网关链无需登录即可实现Root访问

原创

骨哥说事
骨哥说事

骨哥说事

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

# **防走失：****https://gugesay.com/**

**不想错过任何消息？设置星标****↓ ↓ ↓**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg)

### 什么是"梭子鱼"（Barracuda）？为什么要说它？必须谈它吗？

梭子鱼（Barracuda）的邮件安全网关解决方案 (ESG) 可不太招人喜欢，这其中缘由颇多：

* 对很多企业而言，它是一台部署在邮件系统前的**关键安全设备**，负责甄别哪些是垃圾邮件、哪些携带恶意软件、哪些可以"通行无阻"。
* 对另一些运维人员来说，这就是那款在UNC4841（据Mandiant报告）利用CVE-2023-2868作为零日漏洞攻击后，**必须强制进行硬件更换的设备**。

无论你是哪类用户，有件事儿是确定的：它又是那类部署在网络边界、要"审视"所有流量、却很可能只配备了"刚好够用来拦截一封关于你博客文章的恶意邮件"的权限的设备。

### 好吧，那CVE-2026-116606和CVE-2026-111560到底是什么？

CVE编号总是出人意料的"好记"——这两个也不例外。先来看看Barracuda官方安全公告中的总结：

| CVE编号 | 漏洞类型 | CVSS评分 | 受影响产品范围 | 修复版本 |
| --- | --- | --- | --- | --- |
| CVE-2026-116606 | 认证前身份权限绕过（编者吐槽：哈哈？） | 9.3 (严重) | Barracuda ESG | 9.4.0.029 |
| CVE-2026-111560 | 操作系统命令注入 | 8.6 (高) | ESG，负载均衡ADC，消息归档器，WAF控制中心，Web应用防火墙，Web安全网关 | 9.4.0.029 |

如果单独分开看，你或许可以用英国人那种保守的口吻，说它们"不太理想"。但如果把它们串联起来（指组合利用），再以那种英式思维来评价，可能会说"嗯，还行吧"。这其中的讽刺意味不言而喻。

所以，这两项漏洞会成为今天watchTowr实验室深度技术分析的焦点，也就不足为奇了——让我们泡杯咖啡，细细道来。

### 场景搭建

为了展开今天的完整分析，我们搭建了真实设备环境，并使用我们常规的"这玩意儿到底改了啥"对比流程，对两个版本进行了比对：

* **存在漏洞的版本**：Barracuda ESG 9.4.0.027
* **已修复的版本**：Barracuda ESG 9.4.0.029

在深入细节前，需要补充一个背景：为了修复CVE-2026-111560和CVE-2026-116606，Barracuda发布了多个补丁文件。不过，我们重点分析了其中两个，它们在内部被称为：

* **补丁-1**（针对CVE-2026-116606 "认证前权限绕过"问题）
* **补丁-2**（针对CVE-2026-111560 操作系统命令注入问题）

  ![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhZfHTia4C3ibjEAMjfEjxEosLNorZ2LQGQpYdegDjxNxtVyBArLjqrYBCmUpx64ZibPo6viaicNfCbNWwDCh91S99Sya169HNtG8bw/640?wx_fmt=png&from=appmsg)

不得不说，没有什么比因为一个安全漏洞而需要对机架服务器进行"物理驱魔"（强制更换硬件）的往事回忆更让人"暖心"了（好吧，我们也知道背后另有故事）。

### "认证前权限绕过"到底长啥样？（CVE-2026-116606探秘）

这正是我们坐下来要搞清楚的问题。幸运的是，我们并没有等待太久。

在分析补丁-1时，安装脚本至少清晰地说明了它的修补目的：

```
..snip..
# 认证前权限绕过漏洞允许
# 任意触发Spam_Config恢复操作
# CVSS评分 9.8 (严重)
```

细心的读者可能注意到了，这里标注的CVSS分数是9.8分，而Barracuda官方公告中给出的是9.3分。我们推测，9.8分可能是将两个漏洞**组合评分**的结果（CVSS专家会立刻认出这种做法"不合规"），而不是此处发生了什么异常。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZhdY9DQibhzJALSU7SbLtsyTEvJmHD7VuWShE4BnFhGf5Hfyenyq7ibaTtQJaiczIsqJnnyAHHvuWyo1Fyo2SbicH2ynanLT7zWpjQ/640?wx_fmt=png&from=appmsg)

深入到这个补丁所修改的文件中，我们很快锁定了一批"嫌疑人"：

* Index.pm
* Backup2.pm
* bayesian\_upload.pm
* UserRole.pm
* Params.pm

### 第一个嫌疑人浮出水面：Index.pm

Index.pm文件中的改动虽然微小，却颇为有趣。

Barracuda值得赞扬的一点是，他们在代码注释中（虽然有些含糊）给出了问题线索：

```
+    # 发送错误并在此停止。如果返回一个userrole对象
+    # 将导致response()方法继续运行模块处理器。
```

这条注释体现在整个补丁的核心改动处。补丁前和补丁后的代码对比如下：

```
if ($password_change_status ==
     $Login::status_codes{ERROR_PASSWD_CHANGE}->{val}) {
-    $params->{json_authenticate} = {
+    $self->audit("failed_password_change", $params->{user});
+    # 发送错误并在此停止。如果返回一个userrole对象
+    # 将导致response()方法继续运行模块处理器。
+    return$self->_bailout_with_json_login_response(
+        $env, $params, {
         success => 'true',
         message => $Login::status_codes{ERROR_PASSWD_CHANGE}->{msg}
                    . ": " . $message,
         status => $Login::status_codes{ERROR_PASSWD_CHANGE}->{val},
-    };
-    return$userrole;
+    });
 }
```

所以，`Index.pm`这个模块负责处理密码修改请求，但问题就出在修补前的代码中：**当密码修改尝试失败**（状态为`ERROR_PASSWD_CHANGE`）时。

下面是存在漏洞的完整函数代码（保留原始文件行号）：

```
383:     if(defined($params->{new_password}) && defined($params->{retype_password}) && ! (-e "/tmp/bypass_password")){
384:         my $password_change_status=0;
385:         my $message = "";
386:         ($password_change_status, $message,$user) = Login::change_admin_password($params);
387:         if($password_change_status == 1 && $user){
388:            # 除非请求来自已通过认证的登录用户，否则不允许其注销
389:             my $url = "/cgi-mod/index.cgi" . uri_hash_to_querystring({
390:                     locale => $MS_globals::params{locale},
391:                     error => $status
392:                 });
393:             my %redir = (-location=>$url);
394:             $self->audit('password_change', $params->{user});
395:             Login::logoff_user($status, 1, $params->{user});
396:             return bailout();
397:         }
398:         else{
399:             if ($password_change_status == $Login::status_codes{ERROR_PASSWD_CHANGE}->{val}) {
400:                 $params->{json_authenticate} = {
401:                     success =>'true',
402:                     message => $Login::status_codes{ERROR_PASSWD_CHANGE}->{msg}.": ". $message,
403:                     status => $Login::status_codes{ERROR_PASSWD_CHANGE}->{val},
404:                 };
405:                 $self->audit("failed_password_change", $params->{user});
406:                 return $userrole;
407:             }
```

修补前的代码虽然返回了一个详细的JSON响应块，告知用户密码修改失败，但它**并未真正终止程序执行流程**。

我们来剖析一下：

* 当密码修改成功（行387），程序最终在第396行执行`return bailout();`，这里的`bailout()`函数意味着"请求处理完毕，**立即停止处理**"。
* 而当密码修改因`ERROR_PASSWD_CHANGE`而失败（行399）时，程序却在第406行执行了`return $userrole;`。

接下来的逻辑问题是：**`$userrole`是什么？** 简单说，它就是当前会话的"角色对象"。对于我们这个未经身份验证的请求，这个角色对象对应的是低权限的"登录页面角色"。

这有什么问题呢？问题在于，上面那段密码修改代码位于`_process_params`函数内部，而调用该函数的是`response`方法：

```
584: sub response {
585:     my ($self, $env, $params) = @_;
586:
587:     $self->set_self_url($env, $params);
588:
589:     # 如果设备未被激活，此行代码将清除用户可能在参数哈希中尝试的各种修改
590:     # 试图进行的更改操作
591:     $self->_check_activation($env, $params);
592:
593:     $self->_process_params($env, $params);
594:
595:     $self->_update_variables($env, $params);
596:
597:     Barracuda::Hooks::run_hooks("after write config");
```

在第593行，`_process_params`函数执行完毕，并将`$userrole`直接返回给了`response`方法——整个函数正常返回，并没有返回任何错误标识，导致程序**照常继续往下执行**。

要复现这个行为，我们可以向`/cgi-mod/index.cgi`（这个端点最终会走到上述代码路径）发送一个POST请求，并在请求体中携带两个参数：

* `new_password`
* `retype_password`

```
POST /cgi-mod/index.cgi HTTP/1.1
Host: barracuda.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 47

user=admin&new_password=one&retype_password=two
```

设备会返回HTTP 200状态码，以及一个宣告密码修改失败的JSON响应体：

```
{"message":"Error: Password Change: ","no_ajax_redirect":"true","redirect":"/cgi-mod/password_change.cgi?auth_type=Local&locale=en_US&user=admin&error=Error: Password Change: ","success":"true"}
```

"但是等等，"读者可能会问，"一个失败的身份认证操作，难道不应该阻止任何后续需要权限的操作吗？这'登录页面角色'权限能干什么呢？"

别那么天真。

我们现在需要的，就是一个**能将此漏洞利用价值最大化的"伙伴"漏洞**。而这正是我们要说的下一个安全弱点。

### 幸好，我们还有一个"绝佳拍档"：命令注入漏洞！（CVE-2026-111560解析）

虽然我们已经发现了Barracuda称之为"认证前权限绕过"的异常行为，但还得搞清楚我们能**用这个漏洞做些什么**。

分析我们称之为"补丁-2"的文件，我们又看到了完整的Perl源代码，这让分析工作轻松了不少。

在这份补丁中，有两个文件格外引人注目：

* Backup2.pm
* fix\_tz.pl![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhrnn4Vl9vTDBBh6I6C6crrA6DhuI9VeQ2Fe6cJR9uD4QQoUnBvyk0ZIjyQCzsrp9DiaKFE796eMomTSuxXMFNBQiaCOdMHqgw7I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZgpGyFfo474J127S6vhR0hdyfQFpz545dJY7MEvibbGicVx6NHn4uOjUE4N0XACdQMEF9o6vTXILuacnWpMxp8ec4mYoytzHXG0E/640?wx_fmt=png&from=appmsg)

### 对比分析Backup2.pm

快速分析后，我们发现Backup2.pm中最关键的修改集中在这个**存在漏洞的代码块**上：

```
if( -f "/home/product/code/config/tz" ) {
    my $system_timezone = Barracuda::Config::get('system_timezone');
    \`sed -i 's#TZ=.*#TZ=$system_timezone#' /home/product/code/config/tz\`;
}
```

通过对比修补后的代码，我们能更清楚地理解问题的本质。实际上，Barracuda用**更安全的本地文件读写方式替换了危险的shell命令执行**：

```
if( -f "/home/product/code/config/tz" ) {
     my $system_timezone = Barracuda::Config::get('system_timezone');
-    \`sed -i 's#TZ=.*#TZ=$system_timezone#' /home/product/code/config/tz\`;
+    if ($system_timezone && -f "/usr/share/zoneinfo/$system_timezone") {
+        open my $in, '<', '/home/product/code/config/tz' or die $!;
+        my @lines = <$in>;
+        close $in;
+        open my $out, '>', '/home/product/code/config/tz' or die $!;
+        for my $line (@lines) {
+            $line =~ s/^TZ=.*/TZ=$system_timezone/ if$line =~ /^TZ=/;
+            print$out$line;
+        }
+        close $out;
+    } else {
+        warn "Skipping tz restore: invalid system_timezone='$system_timezone'\n";
+    }
 }
```

总结起来，补丁揭示了三个关键点：

1. **开始进行输入验证**：供应商现在将`system_timezone`这个值视为**不受信任**的输入...