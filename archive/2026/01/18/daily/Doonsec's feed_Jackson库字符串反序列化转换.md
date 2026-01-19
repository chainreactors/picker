---
title: Jackson库字符串反序列化转换
url: https://mp.weixin.qq.com/s/YWyu0F9-6OosdkF519hlrQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:37:22.338455
---

# Jackson库字符串反序列化转换

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YFxLNg1BibfnLT9yZszIwTLHia1m6mRuHKxxWO5YOdtEGsmyaGDjhgc8j4NcPfTfibweVQ3ZVeAr24epUgmszc41w/0?wx_fmt=jpeg)

# Jackson库字符串反序列化转换

原创

静观云起
静观云起

码云精炼

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnLT9yZszIwTLHia1m6mRuHKj4qwbZDnLknzUYiaxmPtlt5zlMqXdKhPTxxjnUXgx5yKRudWeflD7Eg/640?wx_fmt=png&from=appmsg)

在Java开发中，经常要将JSON字符串转换为普通的pojo对象，数组，`List<T>`集合和嵌套对象。Jackson库性能高，功能全面，Spring框架默认集成。

一 配置maven依赖

```
<project>    <dependencies>        <dependency>            <groupId>com.fasterxml.jackson.core</groupId>            <artifactId>jackson-databind</artifactId>            <version>2.15.2</version>        </dependency>    </dependencies></project>
```

二 封装工具类

```
import com.fasterxml.jackson.core.type.TypeReference;import com.fasterxml.jackson.databind.ObjectMapper;import java.util.List;public class JsonUtils {    private static final ObjectMapper objectMapper = new ObjectMapper();        static {      // 将Java对象序列化为JSON字符串时，忽略值为null的字段      objectMapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);       // 反序列化时希望忽略JSON中不存在的字段      objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);    }
    // 1.转换为普通POJO对象    public static <T> T fromJson(String json, Class<T> clazz) {     try {          return objectMapper.readValue(json, clazz);         } catch (Exception e) {        throw new RuntimeException("JSON转对象失败", e);         }    }
    // 2.泛型集合，如List<T>    public static <T> List<T> fromJsonToList(String json, Class<T> elementClass) {     try {           return objectMapper.readValue(json, new TypeReference<List<T>>() {});         } catch (Exception e) {           throw new RuntimeException("JSON转List失败", e);         }    }
    // 3.更通用的方式，支持任意复杂泛型(如Map<String, List<T>>)    public static <T> T fromJsonToGenericType(String json, TypeReference<T> typeRef) {     try {          return objectMapper.readValue(json, typeRef);         } catch (Exception e) {          throw new RuntimeException("JSON转泛型对象失败", e);         }     }}
```

三 测试

1.转换普通对象

```
// 普通对象String personJson = "{\"name\":\"李四\",\"age\":30}";Person person = JsonUtils.fromJson(personJson, Person.class);
```

2. List<T>类型转换

```
String listJson = "[{\"name\":\"王五\",\"age\":28},{\"name\":\"赵六\",\"age\":35}]";List<Person> personList = JsonUtils.fromJsonToList(listJson, Person.class);
```

3. 嵌套结构

```
// Map<String, List<Person>> 或自定义结构 Map<String, List<Person>> map = JsonUtils.fromJsonToGenericType(            jsonStr,             new TypeReference<Map<String, List<Person>>>() {});
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YFxLNg1Bibfnia4huCODlTdyh6PTbL1pic45RaY9PANbJVIia0XOz1gV28f9BHd4341P1lpqQwn0cRGBjHPbHYmYIQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnlOXAcdPXnWKdTyfxKRwkUYCzGrICTx2DxXjHOOr3JOX74dPjlW71DIy7udMwgvWdUuh3FgJs6Pw/0?wx_fmt=png)

码云精炼

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnlOXAcdPXnWKdTyfxKRwkUYCzGrICTx2DxXjHOOr3JOX74dPjlW71DIy7udMwgvWdUuh3FgJs6Pw/0?wx_fmt=png)

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