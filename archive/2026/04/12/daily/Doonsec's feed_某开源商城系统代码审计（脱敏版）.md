---
title: 某开源商城系统代码审计（脱敏版）
url: https://mp.weixin.qq.com/s/OihMDtUvnax2kjkvT_5kxQ
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:56:29.197017
---

# 某开源商城系统代码审计（脱敏版）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QT8iaU7O4fGM3ZE7DZxUs7DLHUIMKVfsB2DS8MIsAXiads21aCuV6Z5HibicTV6ou4Z7jhTzUV6ECdWymlWicg3pI5Hx6uyEXb1cfBkJRJHK83JM/0?wx_fmt=jpeg)

# 某开源商城系统代码审计（脱敏版）

原创

仰恩网安校队
仰恩网安校队

GET不到的FLAG

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

某开源商城系统代码审计（脱敏版）

本文仅记录代码审计思路。所有项目名称、接口路径、字段细节、版本信息、目标信息均已脱敏处理，不提供完整利用链和可直接复现的请求。

前言

最近在一次代码审计中，遇到了一处比较典型、也比较容易被忽略的业务逻辑问题。

漏洞点位于某电商系统的“远程登录 / 远程注册”模块。该模块的设计初衷是为了支持第三方系统同步用户身份，实现类似单点登录的效果。

从功能上看，这类接口并不罕见：

第三方系统生成用户身份数据
业务系统接收远程登录凭证
业务系统解析用户信息
业务系统创建或登录本地用户
业务系统签发本地登录态

但问题在于，代码实现中将外部传入的数据“解码”后直接作为可信身份使用，却没有完成最关键的“验签”步骤。

最终，该问题可导致攻击者伪造远程登录凭证，并在特定条件下获得指定前台用户的登录态，同时影响部分用户资料及资产相关字段。

漏洞类型

该问题属于业务逻辑与认证设计类漏洞，主要涉及：

远程登录凭证未验签
认证绕过
前台账号接管
用户资料污染
资产字段异常写入

严格来说，它不是传统意义上的注入、文件上传或命令执行，而是身份信任边界被破坏。

审计入口

审计过程中，首先注意到系统中存在一个远程登录相关接口。

该接口大致用于接收一个外部登录凭证，然后根据其中的用户信息创建或登录本地用户。

脱敏后的路由逻辑如下：

```
Route::get('remote_xxx', 'LoginController/remoteLogin');
```

该路由位于基础接口分组中，并未强制要求用户登录。

从业务语义上看，这类接口本身可以是公开接口，因为第三方登录入口通常需要在用户未登录时访问。

控制器逻辑

脱敏后的控制器代码如下：

publicfunction remoteLogin(Request $request)
{
    [$remoteToken] = $request->getMore([
        ['remote\_token', ''],
    ],true);

    if($remoteToken == '') {
        return app('json')->success('登录失败', [
            'remote\_login\_url' => sys\_config('remote\_login\_url')
        ]);
    }

    return app('json')->success(
        '登录成功',
        $this->services->remoteLogin($remoteToken)
    );
}

1. 从请求中读取远程登录凭证
2. 判断是否为空
3. 交给服务层处理

这里没有做签名校验，也没有做来源校验。不过很多项目会把核心校验放在服务层，因此继续向下跟进。

服务层关键逻辑

服务层中出现了本次审计的核心问题。

脱敏后的代码如下：

publicfunction remoteLogin(string$token = '')
{
    $info = JwtTool::jsonDecode(
        JwtTool::base64UrlDecode($token)
    );

    $userInfo = $this->userDao->get([
        'uid' => $info->uid
    ]);

    $data = [];

    if(!$userInfo) {
        $data['uid'] = $info->uid;
        $data['account'] = $info->phone ?:'out\_' . $info->uid;
        $data['phone'] = $info->phone;
        $data['password'] = md5('default\_password');
        $data['nickname'] = $info->nickname;
        $data['avatar'] = $info->avatar;

        $data['balance'] = $info->balance;
        $data['points'] = $info->points;
        $data['growth'] = $info->growth;

        $this->userDao->save($data);
    } else {
        $data['nickname'] = $info->nickname;
        $data['avatar'] = $info->avatar;

        $data['balance'] = $info->balance;
        $data['points'] = $info->points;
        $data['growth'] = $info->growth;

        $this->userDao->update($info->uid, $data);
    }

    return$this->createFrontendToken((int)$info->uid);
}

真正危险的是这一段：

$info = JwtTool::jsonDecode(
    JwtTool::base64UrlDecode($token)
);

乍一看，代码里出现了 JwtTool，似乎和 JWT 相关。

但这里并没有执行 JWT 验签，只是做了：

base64url 解码
JSON 解析

这不是认证。

这只是解析用户输入。

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGNia17R9ibkFGqESSKKM2ct8aMxSIJIp3aKF4hbU2iaMGHljiaFxzicAviazv7JgNClEgQzItGc0lAwaVVGmEeAyadb73GY7stiaIYrTM/640?wx_fmt=png)

“解码”和“验签”的区别

这是这类漏洞中最容易被忽略的地方。

很多开发者看到 JWT，容易产生一个误解：

只要能解析 JWT，就说明 JWT 是可信的

实际上并不是。

JWT 的安全性来自签名校验，而不是 base64 编码。

JWT 的 Payload 本质上只是 base64url 编码后的 JSON，任何人都可以构造和修改。

不安全逻辑：

$payload = jsonDecode(base64UrlDecode($token));

安全逻辑应该类似：

$payload = Jwt::verifyAndDecode($token, $secret, ['HS256']);

漏洞影响

该漏洞的影响主要分为三层。

第一层：绕过注册校验

如果远程凭证中的用户在本地不存在，系统会进入创建用户逻辑。

由于该流程不要求短信验证码、密码校验或人工确认，因此可能造成：

虚假手机号注册
批量创建异常用户
绕过正常注册风控

第二层：指定前台用户登录

如果远程凭证中指定的本地用户已经存在，系统会进入更新用户逻辑，并在最后签发该用户的前台 token。

这意味着攻击者可能通过伪造远程身份数据，获得指定前台用户的登录态。

第三层：敏感业务字段被覆盖

更严重的是，代码中并不只更新昵称、头像等展示字段，还更新了资产或权益相关字段。

脱敏后可以概括为：

余额类字段
积分类字段
成长值或等级类字段

这意味着攻击者伪造远程身份数据时，可能同时污染用户资产或权益数据。

如果业务系统中存在余额支付、积分抵扣、会员等级、分销佣金等功能，风险会进一步扩大

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGO2icTtLymgGFEVJvda5rKrRfTIeJWtOeUBB8f19qe1UpvvMxsiaOYPpnqYNbyr0JSLTowhGEvgkia0cGR7h4SC7PvAsHKiayibgUhc/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IiaWHPesOyByGQUwBp3nNCsxVtk6CEZ6toGflQhXxD6en4Y8feOk3sgM2o1qezPlhS3qiaZwAJzJ3Vgws9utuS2g/0?wx_fmt=png)

GET不到的FLAG

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IiaWHPesOyByGQUwBp3nNCsxVtk6CEZ6toGflQhXxD6en4Y8feOk3sgM2o1qezPlhS3qiaZwAJzJ3Vgws9utuS2g/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过