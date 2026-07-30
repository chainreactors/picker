---
title: 我就靠这3句SQL，搞定了leader要的所有数据
url: https://mp.weixin.qq.com/s/MgvagQW0fofKNBsoE7bTqQ
source: Doonsec's feed
date: 2026-07-29
fetch_date: 2026-07-30T04:50:05.608751
---

# 我就靠这3句SQL，搞定了leader要的所有数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9bric97vH3E1vZoCQG03cwgW60hU8WEbIzs1AcfhXQPL46aCE1XHwB3abUgpwaUmlbFIQ7hsGicERSEXAQVO8YJoXF5pBYAWMrVfXGFjxGuok/0?wx_fmt=jpeg)

# 我就靠这3句SQL，搞定了leader要的所有数据

疆来攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

“帮我把最近7天注册的VIP用户导一下，下班前要。”leader丢过来一句话就走了。你打开数据库，盯着空白的输入框，脑子里飞速运转：

“用户表叫啥？VIP字段是哪个？时间怎么筛？”

——如果你经历过这个场景，那今天这篇就是为你写的。

不扯理论，直接给你3个能马上用的技巧，看完就能干活。

![](https://mmbiz.qpic.cn/mmbiz_jpg/9bric97vH3E26XDAQeo1ia0SulCoZrlXMmguy9wbKxA47fZKibcsiaImz2TdTpoFK06EV76pXcibjeiaId0XmYXqshWFaic7nqTVciaW4Kfva5Flvfg/640?wx_fmt=jpeg)

## 先做3步准备

拿到数据库，先别急着写SQL。花2分钟摸清底细，能省你2小时：

### 1. 看有哪些表

```
-- MySQL
SHOW TABLES;
```

### 2. 看表结构

```
DESC 表名;
-- 或
SHOW FULL COLUMNS FROM 表名;
```

### 3. 看几条真实数据

```
SELECT * FROM 表名 LIMIT 5;
```

**💡 关键**：看真实数据，避免写错条件。你以为状态是0/1，结果存的是'Y'/'N'。

---

## 技巧一：日期查询

按时间查数据，是最高频的需求。

### 查某一天

```
-- 推荐：简单直观
SELECT * FROM orders
WHEREDATE(created_at) = '2025-07-28';

-- 更精确，性能更好
SELECT * FROM orders
WHERE created_at >= '2025-07-28 00:00:00'
AND created_at < '2025-07-29 00:00:00';
```

### 查最近N天

```
-- 最近7天
SELECT * FROM orders
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 7 DAY);

-- 昨天
SELECT * FROM orders
WHEREDATE(created_at) = DATE_SUB(CURDATE(), INTERVAL 1 DAY);
```

**⚠️ 3个常见坑**
`created_at = '2025-07-28'` → 只匹配00:00:00，漏掉当天其他时间
`BETWEEN '2025-07-28' AND '2025-07-29'` → 多包含29号00:00:00
`created_at >= '2025-07-28'` → 同上，只匹配零点

**✅ 口诀**：查“某一天”用 `DATE(字段) = '日期'`，查“范围”用 `>= 开始 AND < 结束 + 1天`。

---

## 技巧二：连表查询

教程讲七八种JOIN，但工作中 **90%的场景只用 `LEFT JOIN`**。

### 什么时候用？

主表数据一条不能少，同时要带出关联表的信息。

### 示例：订单列表 + 用户手机号

```
SELECT
    o.order_id, o.amount, o.created_at,
    u.phone, u.vip_level
FROM orders o
LEFT JOIN users u ON o.user_id = u.id
WHERE o.created_at >= '2025-07-01';
```

| 写法 | 效果 |
| --- | --- |
| `INNER JOIN` | 只返回两表都匹配的记录，可能丢数据 |
| `LEFT JOIN` | 主表全量返回，关联表有则显示，无则NULL |

**✅ 原则**：不确定用哪种JOIN时，先用 `LEFT JOIN`，安全不丢数据。

---

## 技巧三：分组统计

“统计每个品类的销量”“各部门平均工资”——用 `GROUP BY`。

### 示例：7月每个用户的订单总金额

```
SELECT
    user_id,
COUNT(*) AS order_count,
SUM(amount) AS total_amount
FROM orders
WHERE created_at >= '2025-07-01'
AND created_at < '2025-08-01'
GROUP BY user_id
ORDER BY total_amount DESC;
```

### 执行顺序（记住这个）

```
FROM → WHERE → GROUP BY → SELECT → ORDER BY
```

**⚠️ WHERE和HAVING的区别**
• `WHERE` 在分组前执行，不能用聚合函数（如SUM）
• `HAVING` 在分组后执行，可以用聚合函数

---

## 完整实战

**需求**：7月每个VIP等级的用户下单总金额排名，只显示总金额 > 500的用户。

```
SELECT
    u.id, u.phone, u.vip_level,
COUNT(o.order_id) AS order_count,
SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
AND o.created_at >= '2025-07-01'
AND o.created_at < '2025-08-01'
GROUP BY u.id, u.phone, u.vip_level
HAVINGSUM(o.amount) > 500
ORDER BY total_amount DESC;
```

**逻辑线**：用户全量 → 关联7月订单 → 按用户分组 → 过滤小客户 → 排序输出

---

## 现在就动手

1. 装 **MySQL**（社区版免费）
2. 装 **DBeaver**（免费图形化工具）
3. 建两张表：用户表、订单表，各插20条假数据
4. 把上面3个技巧的代码跑一遍，改改参数

**SQL是动手的技能**，花2小时上手敲一遍，比看两天教程管用。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9bric97vH3E1pxobFicq5BarnibyrUvETufF521yAOvjWzzQNemP91E9U6aZnPXWeBuho9s8wL1ciaiauIyoAjickIlpNg3yye2NqDdGCTeEcfJXE/640?wx_fmt=gif&from=appmsg)

点分享

![](https://mmbiz.qpic.cn/mmbiz_gif/9bric97vH3E3qzbXEzibfxwy0SDDdabQ8ogr6eo6JV2xPibU2UkZXVObAwRxzk62IrLT5NQZkk9bEMibJb6DJkATm61Kar7epd6GicD2cZ0YAcX4/640?wx_fmt=gif&from=appmsg)

点收藏

![](https://mmbiz.qpic.cn/mmbiz_gif/9bric97vH3E1bzQZu3yL0AzXhwEw0kh7xg4ow52LAMyeyAJnWmJ3FBMPMtrwLI9Gt7YdpYDqPiaBWr2cibWQRdkFiay6kQ4sqsMcuxVNfuECRGA/640?wx_fmt=gif&from=appmsg)

点点赞

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9bric97vH3E30oEWoG48c7yNSO9VUsV3VAvyZpa3E0ibnGWcvic1r54JLKtn0GBeq7knRCvXAwZsoE6lPKrbb6doFiam8UwFNh68NFO68vJNgRo/640?wx_fmt=gif&from=appmsg)

点在看

![疆来攻防.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9bric97vH3E3iaEd5jg1QYHl5Rlic3RPYZJ9nZHI4wLA1jehlJTWoZQGeaaptLa7rQTkIoVgXkZzD5OObia9VecuSRVjfzib4egGI4aYkU5Cqjm0/640?wx_fmt=jpeg&from=appmsg "疆来攻防.jpg")

**扫码关注**

**疆来攻防**

**获取更多精彩资讯**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/tOs8TbI2yPvic8UicV7NibHf4f20YtJW6U7X7opeH8eichog64tXbBP6ibz5ia8hXribWr2VibKFPbT8l3uAGuJliaEHL8Q/0?wx_fmt=png)

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