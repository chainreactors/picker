---
title: 短信验证码防泄漏安全机制逆向分析
url: https://mp.weixin.qq.com/s/4pkcIsXh9AS09-3iSlELyA
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:22:40.743856
---

# 短信验证码防泄漏安全机制逆向分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/arAE014sTgyKVyZ4RjLlUJI85TGsAuGnZwUaQVjGq9N3HwPBNUa3qSuqicFLzicA06lvEWkG7uVm4FB4KKF49smBFezcdib17s6beJQjdEPZ7c/0?wx_fmt=jpeg)

# 短信验证码防泄漏安全机制逆向分析

原创

0pen1
0pen1

白帽技术与网络安全

![]()

在小说阅读器中沉浸阅读

> 通过 JADX 逆向Mms.apk（63MB，Android 15），完整还原 ColorOS 短信验证码的五层纵深防护体系：从 NLP 智能识别、通知内容遮蔽、ContentProvider 隔离存储、权限控制的系统广播分发，到 7 天定时自毁清理。

![](https://mmbiz.qpic.cn/mmbiz_png/arAE014sTgyvlpO8X0eEN2LoOyjpLZ9MGk39qUDibfPmhYsibflxduncxMuQTXTpaguWwafQnvGOibSAyx9U7Xtx0tJgUXho51U0eLG4QGttibY/640?wx_fmt=png)

## 引言

短信验证码是移动互联网账户安全的第一道防线，却也是攻击者觊觎的高价值目标。恶意应用通过 `READ_SMS` 权限静默读取验证码、SIM Swap 攻击、剪贴板嗅探等手段层出不穷。

OPPO 在 ColorOS 中构建了一套完整的验证码防泄漏机制，将短信验证码从"被动明文暴露"升级为"主动安全防护"。本文基于对 OPPO Mms.apk 的逆向分析，深入剖析这套防护体系的技术实现。

## 防护架构总览

验证码防护并非单一策略，而是一个五层纵深防御体系：

![](https://mmbiz.qpic.cn/mmbiz_png/arAE014sTgxeUXsDNy4EJuLWLNbBTl5nGOpqu6OXCEUgIRZaqibVsfVjOtBaIWVo6cibrneHwUdS6oB4f93AeKia2D6m4gsVhaLZNBnqEjGtP8/640?wx_fmt=png&from=appmsg)

下面逐层分析其实现细节。

## 第一层：NLP 智能识别引擎

### 1.1 识别入口

当短信到达时，系统调用 `VerificationCodeUtil.d()` 判断是否为验证码：

```
// nu.VerificationCodeUtil
publicstaticbooleand(Contextcontext, Stringbody, Stringaddress,
                        Stringtag, longtimeout) {
    if (TextUtils.isEmpty(body) ||!FeatureOption.i) {
        returnfalse;
    }
    // 预处理：清除空字符、统一换行符
    Stringcleaned=body.replace("\u0000", "")
                        .replace("\r\n", "\n")
                        .replace("\r", "\n");
    // 调用 NLP 引擎解析，带超时保护
    returnf(h(context, cleaned, TedUtils3.e(address), tag, timeout));
}
```

### 1.2 NLP 解析引擎

`h()` 方法将短信内容提交给 `SmartDecorateManager` 的 NLP 引擎进行语义分析：

```
protectedstaticISmsEntityh(Contextcontext, Stringbody,
                               StringserviceId, Stringtag, longtimeout) {
    if (!FeatureOption.i) returnnull;

    ExecutorServiceexecutor=Executors.newFixedThreadPool(1);
    try {
        // 异步提交 NLP 任务，带超时保护
        ISmsEntityentity=executor.submit(() -> {
            returnSmartDecorateManager.l(-1L, body, serviceId);
        }).get(timeout, TimeUnit.MILLISECONDS);
        returnentity;
    } catch (TimeoutExceptione) {
        // NLP 超时不影响短信接收
        returnnull;
    } finally {
        executor.shutdown();
    }
}
```

设计亮点：

* **异步执行 + 超时机制**：NLP 分析在独立线程池中运行，不阻塞短信接收链路
* **超时降级**：若 NLP 引擎响应超时，直接返回 null，短信按普通消息处理，保证可用性

### 1.3 验证码特征识别

NLP 引擎解析后返回 `ISmsEntity` 对象，其内部结构采用"气泡（Bubble）"模型：

```
publicstaticbooleanf(ISmsEntityentity) {
    if (entity!=null) {
        List<IBubbleEntity>bubbles=entity.f();
        if (bubbles!=null) {
            for (IBubbleEntitybubble : bubbles) {
                // id="-1" 是验证码气泡的固定标识
                if (bubble!=null&&"-1".equals(bubble.getId())) {
                    returntrue;
                }
            }
        }
    }
    returnfalse;
}
```

NLP 引擎将短信拆解为多个 Bubble，每个 Bubble 代表一个语义单元。验证码 Bubble 使用特殊 ID `"-1"` 标识，其 `d()` 方法返回提取的验证码值，`b()` 方法返回关联的 Action 列表（如"复制验证码"）。

### 1.4 消息类型标记

识别为验证码后，系统通过 `VCodeMarkMessageTypeAction` 对消息打标：

```
// 消息类型常量（MessageData）
TYPE_NONE=0;                         // 未分类
TYPE_FORBID_READ_VERIFICATION_CODE=1; // 受保护的验证码（默认）
TYPE_VERIFICATION_CODE=2;             // 普通验证码
TYPE_OTHERS=100;                      // 通知/服务类

// 标记结果写入两处：
// 1. bugle_db → messages.message_type
// 2. content://sms → oplus_sms_type 字段
privatebooleanupdateTypeToRemoteDb(List<String>uriList, inttype) {
    ContentValuesvalues=newContentValues();
    values.put("oplus_sms_type", Integer.valueOf(type));
    SqliteWrapper.f(app, resolver, Telephony.Sms.CONTENT_URI, values, ...);
}
```

`TYPE_FORBID_READ_VERIFICATION_CODE`（值为 1）是安全防护的核心——标记为此类型的短信将进入最严格的保护模式。

## 第二层：通知内容遮蔽

### 2.1 遮蔽策略

当验证码短信到达时，锁屏和通知栏不显示原始内容，而是替换为脱敏文案：

```
// VerificationCodeUtil.e() — 构建遮蔽后的通知文本
publicstaticbooleane(Contextcontext, ISmsEntityentity,
                        Stringtag, StringBuildersb) {
    List<IBubbleEntity>bubbles=entity.f();
    for (IBubbleEntitybubble : bubbles) {
        if ("-1".equals(bubble.getId())) {
            List<IActionBase>actions=bubble.b();
            if (actions!=null&&!actions.isEmpty()) {
                StringactionText=actions.get(0).d();
                // 获取遮蔽提示文案
                Stringhint=context.getString(
                    R.string.please_click_to_view_details);
                // 中文格式："验证码：XXXX，请点击查看详情"
                // 英文格式："Code: XXXX, Please click to view details"
                if (isChinese(actionText)) {
                    sb.append(actionText.subSequence(2, length));
                    sb.append("：");
                    sb.append(bubble.d());  // 验证码值
                    sb.append("，");
                    sb.append(hint);
                } else {
                    sb.append(codeLabel);
                    sb.append(": ");
                    sb.append(bubble.d());
                    sb.append(", ");
                    sb.append(hint);
                }
            }
            returntrue;
        }
    }
    returnfalse;
}
```

### 2.2 效果

用户看到的通知：

```
途虎养车
验证码：3554，请点击查看详情
```

而非原始短信全文：

```
【途虎养车】您的登录验证码是：3554，5分钟内有效，请勿泄漏。如非本人操作，请忽略此信息。
```

这防止了：

* 锁屏状态下验证码被偷窥
* 通知栏被恶意应用通过 NotificationListenerService 截获完整内容
* 投屏/录屏场景下验证码泄漏

### 2.3 区分验证码类型

系统还区分了无需特殊警告的验证码类型：

```
public static boolean c(ISmsEntity entity, Context context) {
    List<IBubbleEntity> bubbles = entity.f();
    for (IBubbleEntity bubble : bubbles) {
        List<IActionBase> actions = bubble.b();
        if (actions != null && actions.size() > 0) {
            String actionText = actions.get(0).d();
            // 与 "no_need_show_warn_code" 配置列表比对
            String[] noWarnList = context.getResources()
                .getStringArray(R.array.no_need_show_warn_code);
            for (String item : noWarnList) {
                if (actionText.equals(item)) {
                    return true; // 此类验证码无需额外安全警告
                }
            }
        }
    }
    return false;
}
```

## 第三层：ContentProvider 隔离存储

### 3.1 存储隔离机制

这是最关键的防护层。被识别为验证码的智能短信**不写入 Android 标准的 `content://sms`**，而是仅存入 Mms 应用私有的 `bugle_db` 数据库：

```
标准 Android 短信流程:
  短信 → TelephonyProvider → content://sms → 任何有 READ_SMS 权限的 App 可读

ColorOS 验证码流程:
  短信 → OPPO 云端识别 → bugle_db (私有数据库)
                          ↓
                  custom_messages_ext 表存储完整内容
                          ↓
                  content://sms ← 不写入!
```

### 3.2 数据库结构

```
-- bugle_db 中的存储结构

-- messages 表：消息元数据
-- 验证码短信的 sms_message_uri 字段为空（从不关联标准 sms 数据库）
SELECT _id, sms_message_uri, message_type FROM messages;
-- _id=11, sms_message_uri=NULL, message_type=1  ← 验证码，无标准 URI

-- custom_messages_ext 表：智能短信的实际内容
SELECT messages_id, content, data_text5 FROM custom_messages_ext;
-- messages_id=11, content="【途虎养车】您的验证码是：3554..."
```

### 3.3 安全效果

这意味着即使恶意应用拥有 `READ_SMS` 运行时权限，也**完全无法**通过以下任何方式获取验证码：

```
// 以下查询均返回空结果
context.getContentResolver().query(
    Uri.parse("content://sms"), null, null, null, "date DESC");

context.getContentResolver().query(
    Uri.parse("content://mms-sms/conversations"), ...);

// caller_is_syncadapter 参数也无效
Uri.parse("content://sms")
    .buildUpon()
    .appendQueryParameter("caller_is_syncadapter", "true")
    .build();
```

验证码被完全隔离在 Mms 应用的 `/data/data/com.android.mms/databases/bugle_db` 中，只有系统级权限（root）才能访问。

## 第四层：权限控制的广播分发

### 4.1 分发架构

验证码识别完成后，通过受权限保护的广播将验证码分发给受信任的系统组件：

```
// VerificationCodeUtil.l() — 分发入口
public static void l(Context context, int protocolStatus,
                     ISmsEntity entity, MessageData messageData) {
    // 三重前置校验
    if (FeatureOption.U                  // 功能开关
        && ProtocolDialogUtil.g()        // 用户已同意隐私协议
        && protocolStatus == 0           // 协议状态正常
        && f(entity)) {                  // 确认是验证码
        // 提取验证码值
        String code = b(entity, "VerificationCodeUtil");
        // 触发安全分发
        k(context, messageData, code);
    }
}
```

### 4.2 三路分发

```
// VerificationCodeUtil.k() — 验证码广播的三路分发
public static void k(Context context, MessageData data, String code) {
    Intent intent = a(data, code);  // 构建携带验证码的 Intent

    ...