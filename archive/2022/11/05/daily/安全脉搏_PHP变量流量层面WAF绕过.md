---
title: PHP变量流量层面WAF绕过
url: https://www.secpulse.com/archives/190540.html
source: 安全脉搏
date: 2022-11-05
fetch_date: 2025-10-03T21:44:36.649797
---

# PHP变量流量层面WAF绕过

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# PHP变量流量层面WAF绕过

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Lemon](https://www.secpulse.com/newpage/author?author_id=5109)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2022-11-04

8,691

## 简介

* 本文主要研究PHP的GET/POST/COOKIE大变量生成过程，及可能在WAF流量层面绕过的一些TRICKS
* 实验环境：PHP 7.3.4 在FPM模式下运行
* PHP变量处理的主要代码在main/php\_variables.c，调用栈如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190540-1667553721.png)

* 由于代码流程过长，本文不贴出具体代码，但是会在相应地方给出github链接供参考
* PHP示例代码

```
<?phpecho "get:";var_dump($_GET);echo "cookie:";var_dump($_COOKIE);echo "post:";var_dump($_POST);
```

## TRICKS

### 变量名和值会进行url解码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190540-16675537211.png)

* 以解析`$_GET`变量为例，大致流程为：获取请求字符串-->获取分割符`&`-->使用`=`分割key和value。
* 在解析key和value时，会分别对其进行url解码，关键代码如下：

```
if (val) { /* have a value */
            size_t val_len;
            size_t new_val_len;

            *val++ = '';
            // 对key进行url解码
            php_url_decode(var, strlen(var));
            // 对value进行url解码
            val_len = php_url_decode(val, strlen(val));
            val = estrndup(val, val_len);
            if (sapi_module.input_filter(arg, var, &val, val_len, &new_val_len)) {
                php_register_variable_safe(var, val, new_val_len, &array);
            }
            efree(val);
    }
```

### 变量名截断

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190540-1667553722.png)

* 我们知道`00`在C语言中意味着字符串的结尾，其编码为`%00`。
* 在对key进行url解码之后，`%00`转换为`00`而截断了key字符串。
* 但是对value进行url解码的时候，获取了其返回值`val_len`，即字符串长度，后续注册变量时，也是使用`val_len`进行内存中的操作，所以未能截断value的值

### 变量名之前的空格会被忽略

* URL 不能包含空格。URL 编码通常使用 + 来替换空格

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190540-1667553723.png)

* 使用`%20`替换空格

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190540-1667553724.png)

* 在注册变量时，PHP会对变量名进行判断，丢弃变量名前的空格，关键代码如下：

```
while (*var_name==' ') {
        var_name++;
    }
```

### 变量名的空格和`.`会转化为`_`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190540-1667553725.png)

* 首先明确一个问题，PHP的变量名中是不能包含点号的。但是为了处理表单中的点号命名，PHP就会自动把点号`.`转换成下划线`_`。
* 这个转换的过程也是发生在PHP变量的注册过程中，关键代码如下：

```
/* ensure that we don't have spaces or dots in the variable name (not binary safe) */
    for (p = var; *p; p++) {
        if (*p == ' ' || *p == '.') {
            *p='_';
        } else if (*p == '[') {
            is_array = 1;
            ip = p;
            *p = 0;
            break;
        }
    }
```

### 变量名的`[`会转换为`_`![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190540-1667553726.png)

* 这个转换过程与`.`的转换过程不同。PHP在遇到`[`符号时，会认为变量为数组。后续进行数组处理时，如果未能找到与`[`匹配的`]`，则会将`[`替换为`.`。关键代码如下：

```
ip = strchr(ip, ']');
        if (!ip) {
            /* PHP variables cannot contain '[' in their names, so we replace the character with a '_' */
            *(index_s - 1) = '_';

            index_len = 0;
            if (index) {
                index_len = strlen(index);
            }
            goto plain_var;
            return;
        }
```

## 参考

* https://www.laruence.com/2008/11/07/581.html

**侵权请私聊公众号删文**

**本文作者：[Lemon](newpage/author?author_id=5109)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/190540.html**](https://www.secpulse.com/archives/190540.html)

Tags: [PHP变量](https://www.secpulse.com/archives/tag/php%E5%8F%98%E9%87%8F)、[tricks](https://www.secpulse.com/archives/tag/tricks)、[waf绕过](https://www.secpulse.com/archives/tag/waf%E7%BB%95%E8%BF%87)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![HVV之Windows应急排查tricks](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2021/03/16163937741-300x196.png)

  HVV之Windows应急排查trick…](https://www.secpulse.com/archives/155313.html "详细阅读 HVV之Windows应急排查tricks")
* [![WAF Bypass数据库特性（Oracle探索篇）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2019/01/link-5-e1548835769911-300x181.jpg)

  WAF Bypass数据库特性（Orac…](https://www.secpulse.com/archives/96167.html "详细阅读 WAF Bypass数据库特性（Oracle探索篇）")
* [![Web渗透之文件上传漏洞总结](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2019/01/link5-300x166.jpg)

  Web渗透之文件上传漏洞总结](https://www.secpulse.com/archives/95987.html "详细阅读 Web渗透之文件上传漏洞总结")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/f43a6447ea66cf84915afd0ca2631f09.png)](https://www.secpulse.com/newpage/author?author_id=5109aaa) | [Lemon ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)](https://www.secpulse.com/newpage/author?author_id=5109) | |
| 文章数：68 | 积分： 647 |
|  | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](https://www.bagevent.com/event/8022600?bag_track=AQMB)

#### 2022-05-12

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-event.com/)

#### 2021-11-18

[AutoSW 2021智能汽车软件开发大会](https://autosw2021.artisan-event.com)

#### 2021-06-27

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo...