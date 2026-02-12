---
title: appId和appSecret利用方法
url: https://mp.weixin.qq.com/s/AgFlWGyAacF6Z95UXVugTA
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:17:29.565517
---

# appId和appSecret利用方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EAbmJhJ6dbdtgfwlBXjcpJkjVYjwKTsVBDkgu9FfRS10RvzxmdE587pI2EFZ5icpicMqa2HFvHvjUg8f43Cg8pPd3LUBrl4yJD7W6EsiaTAzpY/0?wx_fmt=jpeg)

# appId和appSecret利用方法

小白鱼来了
小白鱼来了

Joker One Security

![]()

在小说阅读器中沉浸阅读

文章首发于https://www.freebuf.com/articles/web/469130.html

## 微信小程序及公众号

参考链接：

https://developers.weixin.qq.com/doc/subscription/guide/dev/api/

#### 获取accesstoken

```
https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
```

#### ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EAbmJhJ6dbfUJCSJvjT2u4246PZNqfJ1wv6W6o8EdIZPtgwJdxfHwegZQueyprKnWHMtan0oLhM8GaMmMEC2Fa5E9x9cyPveCOqW00DI1ibQ/640?wx_fmt=other&from=appmsg)

在获取accesstoken后可利用其他接口获取微信服务信息

#### 获取微信API服务器IP

```
https://api.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token=ACCESS_TOKEN
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbeQia6oALyPDnQ3UibBBfPrkhs1hdVo7PDfO385IkdJ3zBYpr7JibLl8md6ou1UdZcsrsSMcCK4usTX80pN2KJQcEUngl7bIqfkQE/640?wx_fmt=other&from=appmsg)

#### 获取微信推送服务器IP

```
https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=ACCESS_TOKEN
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbd1DJqUa7Dp6Ts91HHWv8gByeSeicFOvvnN9EY1WyYDprQLUEhDG00JiauJVmZp5j8DeRNDxASzlDice0ibDHzcEydricvVOv2vADgw/640?wx_fmt=other&from=appmsg)

#### 操作评论

1. 删除评论

```
POST /cgi-bin/comment/delete?access_token=ACCESS_TOKEN HTTP/1.1Host: api.weixin.qq.comContent-Type: application/jsonContent-Length: 80
{  "msg_data_id": MSG_DATA_ID,  "index": 0,  "user_comment_id": USER_COMMENT_ID}
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbeDm2Ciay93m9xDndyOROeHbiaFjwWGXuKbqRVVkPGpibPLhxzRKpTNSVA40IbHOSs0ALf64IDPOsfS3O7bEwT5AH0EYV0DpdBOBk/640?wx_fmt=other&from=appmsg)

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbdlLugqK64G2pyFaEXiauaqtbJ9Bgh2syTPl35GdO5BMjmnTEcIpAemrUnfFbFwI5nBq6kFWkibNHlJoyqiaHVfibtfc28V0qv1U5k/640?wx_fmt=other&from=appmsg)

2. 回复评论

```
POST /cgi-bin/comment/reply/add?access_token=ACCESS_TOKEN HTTP/1.1Host: api.weixin.qq.comContent-Type: application/jsonContent-Length: 80
{  "msg_data_id" : MSG_DATA_ID,  "index": 0,  "user_comment_id": COMMENT_ID,  "content": "内容"}
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbdwV8kWS7d3BuyDh8AERDiacL6e1BvpAqG5nWHibx4kA9x0icTdqsgiasQ4BzMUrgsufYowY9OBSmPgTjPPjyF4bRP6HDj1QW4EA9U/640?wx_fmt=other&from=appmsg)

#### ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EAbmJhJ6dbeWlP89h6CBWbxFVnPfJV9vasibXzicsic5w8Y6sEB0nO483SdPf4zLbtwxZU4ekriciayyPz5TCBZjP0GV77hxnllpwjEsnENeTUUo/640?wx_fmt=other&from=appmsg)

3. 删除回复

```
POST /cgi-bin/comment/reply/delete?access_token=ACCESS_TOKEN HTTP/1.1Host: api.weixin.qq.comContent-Type: application/jsonContent-Length: 80
{  "msg_data_id" : MSG_DATA_ID,  "index": 0,  "user_comment_id": COMMENT_ID}
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbfzKgcI6SxCxuNzGn7w1iasJv8arVsaVkxTtEhuPTLqvyeIsQLOmPpnY01K1AvybShMvvQ4ibKgicRINoPJfRWlMfprZDgzticWPGU/640?wx_fmt=other&from=appmsg)

#### ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EAbmJhJ6dbemwfehxedFfZeoxmkibBODibm7qqxX98tNKBg37NySTGibYVpXGBdBXnQw9Ggr5CkkKic8U2dB3cUmbKwe795qhCdBsmA8ILnc0vw/640?wx_fmt=other&from=appmsg)

## 企业微信

参考链接：

https://developer.work.weixin.qq.com/document/path/91039

#### 获取accesstoken

```
 https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbdbia2iakNTXDZ1O2ffEUCtUCTkRwUfav8JkCUibSVzFOd6tqw2PFgB91w2hcVEh4eNUtGBQic0uyFKVjriaBcTctMEKN4XerJLPvSM/640?wx_fmt=other&from=appmsg)

#### 获取企业微信接口IP段

```
 https://qyapi.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token=ACCESS_TOKEN
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbcgbGWqLmsT4GfchusHT5R9uibhKgAJjrmoCIZQFsJ9qURhgCRB8MwRXpjdFvJ171KsF1XnqibAcMaOVicqX4kZF6wxxfPib2IUMBQ/640?wx_fmt=other&from=appmsg)

#### 获取企业微信回调IP段

```
https://qyapi.weixin.qq.com/cgi-bin/getcallbackip?access_token=ACCESS_TOKEN
```

#### ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EAbmJhJ6dbfgKic6nNXzrnKu0sx1wW9SqahIx8KJxibUXAKt3zOiaduVLTjGlKnQOnbCgCzSe8zqcEISy5FLUToOaM30ciam4N1sxqaiay1VEicwg/640?wx_fmt=other&from=appmsg)

#### 创建成员

```
POST /cgi-bin/user/create?access_token=ACCESS_TOKEN HTTP/1.1Host: qyapi.weixin.qq.comContent-Type: application/jsonContent-Length: 320
{"userid": "zhangsan","name": "张三","mobile": "+86 13800000000","department": [1],"position": "产品经理","gender": "1","email": "zhangsan@qq.com","enable": 1,"main_department": 1,"to_invite": true,"external_position": "高级产品经理"}
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbdNJC3fBVmXs25oic8NpHAiaN8yicxlc6GyjHFeKMXqZYtbUmnbgZMFibtHxAXCSzib4Jh0eJBa9sHuPZRTgqD7xGtzOJI3n6u7j4FY/640?wx_fmt=other&from=appmsg)

#### 读取成员

```
https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
```

#### ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EAbmJhJ6dbfjj8t2kuiaoMavrNfmgTro0iasy6LvmyekbyPfaRh9h9akKyacG5p6M4JQoeEAicXNL9icXU954HjcVZkFzAAzjGo9vFJAOiczcicOk/640?wx_fmt=other&from=appmsg)

#### 获取部门成员

```
https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token=ACCESS_TOKEN&department_id=DEPARTMENT_ID
```

#### ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EAbmJhJ6dbeXAfjP53Xtj2nBelhGCGurtnoghxJIGjEeeJHWMCiaeVjt1icrSf1kFVFYKXjMsldxrtF1ibZqhpNBibBUo0hYkhJY2WqHTfwAbFQ/640?wx_fmt=other&from=appmsg)

#### 获取部门成员详情

```
https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token=ACCESS_TOKEN&department_id=DEPARTMENT_ID
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbffkskDJemss0ibjFdYp7OU8ONLoXgM78THmkuVPgnsDOaepW4gc9LF5HXghxbaPqawVbcLCe4aUWicL8OpQ6Ir6nyibDYxvMKia1o/640?wx_fmt=other&from=appmsg)

#### 邀请成员

```
POST /cgi-bin/batch/invite?access_token=ACCESS_TOKEN HTTP/1.1Host: qyapi.weixin.qq.comContent-Type: application/jsonContent-Length: 108
{   "user": ["UserID1", "UserID2", "UserID3"],   "party": [1, 2, 3],   "tag": [101, 102, 103]}
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbcvo0O9QUmOSzSAF0dW0An1NWnP1eicSA4Mj4t054qKG17yoqLA6kSHjxe2bZtxRDwbDDnLcH2Juraib3dYVjtjQ1VQtGRF5PJB0/640?wx_fmt=other&from=appmsg)

#### 获取加入企业二维码

```
https://qyapi.weixin.qq.com/cgi-bin/corp/get_join_qrcode?access_token=ACCESS_TOKEN&size_type=SIZE_TYPE
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dben5oE3icnhIupt50Ty6eoJPJlVb0myAMLOQGjAGe17tzFdlrqDcvY1DXmFq6wUGGhvu3JydF5KqFT0eRicAjpxdzJoFWD3SROOg/640?wx_fmt=other&from=appmsg)

#### 获取成员ID列表

```
POST /cgi-bin/user/list_id?access_token=ACCESS_TOKEN HTTP/1.1Host: qyapi.weixin.qq.comContent-Type: application/jsonContent-Length: 108
{"cursor": "xxxxxxx","limit": 10000}
```

#### ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EAbmJhJ6dbeTsg0Lvxoa1VqODvVlwcJLxOIoRqXibx9guRxlQqymOCrckw02eHiazCcrmxUmcZ9bAmweGz7b5pVrvAQibO3nKUyicFym6ptvbhM/640?wx_fmt=other&from=appmsg)

## 飞书

参考链接：

https://open.feishu.cn/document/server-docs/api-call-guide/calling-process/get-access-token

#### 获取accesstoken

```
POST https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal HTTP/1.1Host: open.feishu.cnContent-Type: application/json; charset=utf-8Content-Length: 88
{    "app_id": "APP_ID",    "app_secret": "APP_SECRET"}
```

#### ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EAbmJhJ6dbcadXMgUplfGlGAdGPyjom3m0Hak9xFzAB9uP90X2toJXI29lBfibDCmZh1GxicnGlaWSv3icfQE8npvnibLUTulgpNokRicL8G28UE/640?wx_fmt=other&from=appmsg)

#### 获取用户信息

```
GET /open-apis/contact/v3/users/7be5fg9a?department_id_type=open_department_id&user_id_type=open_id HTTP/1.1Host: open.feishu.cnAuthorization: accesstoken
```

#### ![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbeagPiaZUgHDURD4wZ6qG1GpOjRLTgpQBWQA6ajTlZDOOhtgEs2q7kwhcaQsp7yEem5gHK5dntm8FeaRiaYFsNlxsuNLCvbnD98Y/640?wx_fmt=other&from=appmsg)

## 钉钉

参考文档：

https://open.dingtalk.com/document/development/obtain-user-token

https://developer.aliyun.com/ask/532363

#### 获取accesstoken

```
https://oapi.dingtalk.com/gettoken?appkey=your_app_k...