---
title: 浅析Smartbi逻辑漏洞
url: https://y4tacker.github.io/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/
source: Y4tacker's Blog
date: 2023-07-06
fetch_date: 2025-10-04T11:50:57.540056
---

# 浅析Smartbi逻辑漏洞

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. 浅析Smartbi逻辑漏洞](#%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E)
   1. [1.1. 写在前面](#%E5%86%99%E5%9C%A8%E5%89%8D%E9%9D%A2)
   2. [1.2. 分析](#%E5%88%86%E6%9E%90)
   3. [1.3. 利用](#%E5%88%A9%E7%94%A8)
   4. [1.4. 后话](#%E5%90%8E%E8%AF%9D)

# 浅析Smartbi逻辑漏洞

Y4tacker

2023-07-05 (Updated: 2024-08-04)

[Java](/categories/Java/)

[Java](/tags/Java/), [Smartbi](/tags/Smartbi/)

# 浅析Smartbi逻辑漏洞

## 写在前面

仅分享逻辑漏洞部分思路，全文以无害路由做演示，后续利用部分打码处理

厂商已发布补丁：<https://www.smartbi.com.cn/patchinfo>

## 分析

最近可以看到smartbi官网突然发布了新的补丁，对比学习了下

利用也仍然和RMIServlet相关，在这个Servlet上还有个Filter(smartbi.freequery.filter.CheckIsLoggedFilter)

如果我们访问调用一些未授权的类方法，就会返回如下字段

![image-20230705095525401](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705095525401.png)

我们先来看看如果正常情况程序该怎么走，首先如果调用RMIServlet，则会尝试获取到className与methodName，获取的方式也多种多样

![image-20230705095800089](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705095800089.png)

有通过解码windowUnloading参数获取

![image-20230705100021973](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705100021973.png)

有通过GET/POST获取

![image-20230705100158411](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705100158411.png)

甚至支持从请求体流中解析

![image-20230705100240104](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705100240104.png)

后面通过下面这两个判断对类与方法做鉴权，如果为true则会继续判断是否登录，未登录则抛出CLIENT\_USER\_NOT\_LOGIN

![image-20230705100351950](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705100351950.png)

这里对于未授权右边部分我们可以不必关心，按照运算符优先级只要`FilterUtil.needToCheck`返回false那么整个结果一定为false，而`FilterUtil.needToCheck`中返回false的都是白名单，代表我们不需要登录都能访问，这也就是为什么上个版本通过利用`loginFromDB`登录默认内置用户

![image-20230705101505359](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705101505359.png)

接下来过了过滤器部分，我们在看RMIServlet如何取值，通过parseRMIInfo从request当中取得

![image-20230705101708783](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705101708783.png)

在这个方法中首先通过request.getParameter取值，若为空则通过multipart获取参数，如果都不行则通过request.getAttribute从之前保存的属性当中获取

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 ``` | ``` public static RMIInfo parseRMIInfo(HttpServletRequest request, boolean forceParse) {         if (!"/vision/RMIServlet".equals(request.getServletPath()) && !forceParse) {             return null;         } else {             RMIInfo info = getRMIInfoFromRequest(request);             if (info != null) {                 return info;             } else {                 String className = request.getParameter("className");                 String methodName = request.getParameter("methodName");                 String params = request.getParameter("params");                 if (StringUtil.isNullOrEmpty(className) && StringUtil.isNullOrEmpty(methodName) && StringUtil.isNullOrEmpty(params) && request.getContentType() != null && request.getContentType().startsWith("multipart/form-data;")) {                     DiskFileItemFactory dfif = new DiskFileItemFactory();                     ServletFileUpload upload = new ServletFileUpload(dfif);                     String encodeString = null;                      try {                         List<FileItem> fileItems = upload.parseRequest(request);                         request.setAttribute("UPLOAD_FILE_ITEMS", fileItems);                         Iterator var10 = fileItems.iterator();                          while(var10.hasNext()) {                             FileItem fileItem = (FileItem)var10.next();                             if (fileItem.isFormField()) {                                 String itemName = fileItem.getFieldName();                                 String itemValue = fileItem.getString("UTF-8");                                 if ("className".equals(itemName)) {                                     className = itemValue;                                 } else if ("methodName".equals(itemName)) {                                     methodName = itemValue;                                 } else if ("params".equals(itemName)) {                                     params = itemValue;                                 } else if ("encode".equals(itemName)) {                                     encodeString = itemValue;                                 }                             }                         }                     } catch (UnsupportedEncodingException | FileUploadException var14) {                         LOG.error(var14.getMessage(), var14);                     }                      if (!StringUtil.isNullOrEmpty(encodeString)) {                         String[] decode = (String[])((String[])CodeEntry.decode(encodeString, true));                         className = decode[0];                         methodName = decode[1];                         params = decode[2];                     }                 }                  if (className == null && methodName == null) {                     className = (String)request.getAttribute("className");                     methodName = (String)request.getAttribute("methodName");                     params = (String)request.getAttribute("params");                 }                  info = new RMIInfo();                 info.setClassName(className);                 info.setMethodName(methodName);                 info.setParams(params);                 request.setAttribute("ATTR_KEY_RMIINFO", info);                 return info;             }         }     } ``` |

## 利用

这时候稍微对漏洞敏感的人已经意识到了一些问题

前面提到了有个windowUnloading参数，如果存在则会对值做解码，并将结果赋给className/methodName/params，

![image-20230705102704861](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705102704861.png)

那么我们是不是就能首先根据此对参数做污染，让其帮助我们通过FilterUtil.needToCheck的校验，之后等到了RMIServlet，又通过GET/POST/表单当中的值恢复真实调用

![image-20230705102814870](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705102814870.png)

关于构造windowUnloading，为了演示方便我选择else分支，因为这样返回的内容是明文，省去一次解码的问题

![image-20230705102953412](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705102953412.png)

当然选择上面这个if分支其实更好，这更方便我们使攻击流量更隐蔽，可以通过传入`jsonpCallback`参数去除解码，

![image-20230705103219188](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705103219188.png)

当然为了演示方便我还是选择else分支，任意选择FilterUtil.needToCheck当中的类方法

|  |  |
| --- | --- |
| ``` 1 ``` | ``` className=UserService&methodName=checkVersion&params=y4 ``` |

下面做演示，未使用windowUnloading前，调用受限方法会提示未登录(这里以无害方法做演示)

![image-20230705103836736](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705103836736.png)

使用后成功调用

![image-20230705103930047](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705103930047.png)

通过未授权调用，我们可以获取用户敏感信息包括密码

![image-20230705104148109](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705104148109.png)

通过上版本中提到的直接比对数据库方式登录

![image-20230705104321315](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705104321315.png)

最终可实现RCE，当然RCE也不止这一种

![image-20230705104529432](/2023/07/05/year/2023/7/%E6%B5%85%E6%9E%90Smartbi%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E/image-20230705104529432.png)

## 后话

上面提到可以配合RMICoder编解码使流量更隐蔽，同样以第一个无害方法getSystemId为例子

![image-20230705105...