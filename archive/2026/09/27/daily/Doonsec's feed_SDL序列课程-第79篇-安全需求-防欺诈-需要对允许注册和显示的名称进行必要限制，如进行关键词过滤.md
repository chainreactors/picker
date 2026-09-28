---
title: SDL序列课程-第79篇-安全需求-防欺诈-需要对允许注册和显示的名称进行必要限制，如进行关键词过滤
url: https://mp.weixin.qq.com/s/zRq2rN4-K-9mbjWpHEFQKg
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:52:36.271049
---

# SDL序列课程-第79篇-安全需求-防欺诈-需要对允许注册和显示的名称进行必要限制，如进行关键词过滤

# SDL序列课程-第79篇-安全需求-防欺诈-需要对允许注册和显示的名称进行必要限制，如进行关键词过滤

原创

Wens0n
Wens0n

软件开发安全生命周期

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

欢迎转发给有需要的人，微信公众号名称：软件开发安全生命周期。定期分享软件开发生命周期,SDLC、SDL、DevSecOps等相关的知识。致力于分享知识、同时会分享网络安全相关的知识点和技能点。

![](https://mmbiz.qpic.cn/mmbiz_png/j5JRTMh0KMpibaWlKOrIgFrZ3IhmwzxyNbC7S8NW7tX4qlNFwHZvVJ3NJAfmfjiaoKclxJlWjB2xiazxxKibKyJqqA/640?wx_fmt=png&from=appmsg)

需要对允许注册和显示的名称进行必要限制，如进行关键词过滤，“系统管理员”、“XXX管理员”等不允许注册

### 1. 引言

在构建网络应用时，防止欺诈行为是必须要考虑的一个重要因素。用户注册和显示名称的管理是防欺诈工作的重要组成部分。为了防止恶意用户利用特定的用户名进行欺诈或误导其他用户，我们需要对允许注册和显示的名称进行必要的限制。例如，"系统管理员"、"XXX管理员"等敏感词汇不应被允许注册。在Java应用中，我们可以通过提交埋点申请，添加通用关键字，开通权限自主管理关键字来实现这一目标。本文将详细讨论这个问题，并提供相关的Java代码示例。

### 2. 用户名的重要性和风险

用户名是用户在网络应用中的标识，它在许多方面都起着重要的作用。例如，它可以用于用户认证、消息传递、用户间的交流等。如果管理不当，用户名也可能成为欺诈行为的工具。

恶意用户可能会选择一些具有误导性的用户名，以欺骗其他用户。例如，他们可能会使用"系统管理员"、"客服"等用户名，让其他用户误以为他们是应用的官方代表。

恶意用户也可能会使用一些敏感词汇或不适当的词汇作为用户名，这可能会对应用的形象造成损害，或者引发其他用户的不满。

我们需要对允许注册和显示的名称进行必要的限制，以防止这些问题的发生。

### 3. 在Java中实现用户名的限制

在Java中，我们可以通过正则表达式和关键字过滤来实现用户名的限制。以下是一个简单的示例：

```
importjava.util.Arrays;
importjava.util.List;

publicclassUsernameValidator {
    privatestaticfinalList<String>FORBIDDEN_WORDS=Arrays.asList("系统管理员", "XXX管理员");

    publicstaticbooleanvalidate(Stringusername) {
        for (StringforbiddenWord : FORBIDDEN_WORDS) {
            if (username.contains(forbiddenWord)) {
                returnfalse;
            }
        }
        returntrue;
    }
}
```

在这个示例中，我们定义了一个`FORBIDDEN_WORDS`列表，包含了一些禁止注册的用户名。在`validate`方法中，我们检查用户名是否包含这些禁止的词汇。如果包含，我们返回`false`，表示这个用户名是无效的。

这是一个简单的实现，它只能处理一些基本的情况。在实际应用中，可能需要一个更复杂的系统，例如使用数据库来存储禁止的词汇，或者使用自然语言处理技术来识别敏感词汇。

### 4. 使用数据库存储禁止的用户名

在大型的网络应用中，可能需要存储大量的禁止注册的用户名。在这种情况下，我们可以使用数据库来存储这些用户名。以下是一个使用MySQL数据库的示例：

首先，我们需要创建一个表来存储禁止的用户名：

```
CREATETABLE forbidden_usernames (
    id INTAUTO_INCREMENTPRIMARYKEY,
    username VARCHAR(255)NOTNULL
);
```

然后，我们可以将禁止的用户名插入到这个表中：

```
INSERTINTO forbidden_usernames (username)VALUES('系统管理员'),('XXX管理员');
```

在Java中，我们可以使用JDBC（Java Database Connectivity）API来查询这个表。以下是一个示例：

```
importjava.sql.Connection;
importjava.sql.DriverManager;
importjava.sql.PreparedStatement;
importjava.sql.ResultSet;
importjava.sql.SQLException;

publicclassUsernameValidator {
    privatestaticfinalStringDB_URL="jdbc:mysql://localhost:3306/mydb";
    privatestaticfinalStringDB_USER="myuser";
    privatestaticfinalStringDB_PASSWORD="mypassword";

    publicstaticbooleanvalidate(Stringusername) {
        try (Connectionconn=DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            Stringsql="SELECT COUNT(*) FROM forbidden_usernames WHERE username = ?";
            PreparedStatementstmt=conn.prepareStatement(sql);
            stmt.setString(1, username);
            ResultSetrs=stmt.executeQuery();
            if (rs.next()) {
                intcount=rs.getInt(1);
                if (count>0) {
                    returnfalse;
                }
            }
        } catch (SQLExceptione) {
            e.printStackTrace();
        }
        returntrue;
    }
}
```

在这个示例中，我们首先创建一个数据库连接。我们创建一个预编译的SQL语句，用于查询给定用户名的数量。如果数量大于0，我们返回`false`，表示这个用户名是无效的。

这是一个更复杂的实现，它可以处理大量的禁止注册的用户名。这个实现依赖于数据库，因此它可能会受到数据库性能和可用性的影响。

### 5. 埋点申请和关键字管理

在大型的网络应用中，可能需要一个更灵活的方式来管理用户名的限制。一种可能的解决方案是使用埋点和关键字管理。

埋点是一种数据收集技术，它可以帮助我们了解用户的行为和应用的使用情况。通过在代码中添加埋点，我们可以收集到用户注册时使用的用户名，然后将这些用户名送入一个关键字过滤系统。

关键字过滤系统可以根据预定义的规则来判断一个用户名是否有效。这些规则可以包括关键字列表、正则表达式、自然语言处理模型等。关键字过滤系统可以提供一个接口，允许管理员添加、删除或修改规则。

在Java中，可以使用各种技术来实现埋点和关键字过滤。例如，我们可以使用日志库（如Log4j或SLF4J）来实现埋点，使用数据库（如MySQL或MongoDB）和自然语言处理库（如OpenNLP或Stanford NLP）来实现关键字过滤。

### 6. 通过埋点收集用户注册信息

在Java中，使用日志库来实现埋点。以下是一个使用Log4j的示例：

```
importorg.apache.logging.log4j.LogManager;
importorg.apache.logging.log4j.Logger;

publicclassRegistrationService {
    privatestaticfinalLoggerlogger=LogManager.getLogger(RegistrationService.class);

    publicvoidregister(Stringusername, Stringpassword) {
        // Validate the username and password
        if (!UsernameValidator.validate(username)) {
            thrownewIllegalArgumentException("Invalid username: "+username);
        }
        // Register the user
        // ...
        // Log the registration event
        logger.info("User registered: {}", username);
    }
}
```

在这个示例中，首先验证用户名。如果用户名无效，我们抛出一个异常。注册用户，并使用`logger.info`方法记录注册事件。这个方法会将注册事件写入到日志文件，我们可以后续分析这个日志文件，收集用户的注册信息。

这是一个简单的埋点实现，它可以收集基本的用户注册信息。这个实现只能收集到用户名，如果我们需要收集更多的信息，例如用户的IP地址、注册时间、注册设备等，我们可能需要一个更复杂的埋点系统。

### 7. 使用自然语言处理库进行关键字过滤

在Java中，我们可以使用自然语言处理库来进行更复杂的关键字过滤。以下是一个使用OpenNLP的示例：

```
importopennlp.tools.namefind.NameFinderME;
importopennlp.tools.namefind.TokenNameFinderModel;
importopennlp.tools.util.Span;

publicclassUsernameValidator {
    privatestaticfinalStringMODEL_FILE="en-ner-person.bin";

    publicstaticbooleanvalidate(Stringusername) {
        try (InputStreammodelIn=newFileInputStream(MODEL_FILE)) {
            TokenNameFinderModelmodel=newTokenNameFinderModel(modelIn);
            NameFinderMEnameFinder=newNameFinderME(model);
            String[] tokens=username.split("\\s+");
            Span[] names=nameFinder.find(tokens);
            if (names.length>0) {
                returnfalse;
            }
        } catch (IOExceptione) {
            e.printStackTrace();
        }
        returntrue;
    }
}
```

在这个示例中，我们首先加载一个名字识别模型。使用这个模型创建一个名字识别器。将用户名分割成单词，并使用名字识别器查找这些单词中的名字。如果找到任何名字，我们返回`false`，表示这个用户名是无效的。

这是一个更复杂的关键字过滤实现，它可以处理更复杂的情况。这个实现依赖于自然语言处理模型，因此它可能会受到模型的准确性和性能的影响。

### 8. 总结

防欺诈是网络应用的重要任务之一。为了防止恶意用户利用用户名进行欺诈或误导需要对允许注册和显示的名称进行必要的限制。在Java中，可以通过正则表达式和关键字过滤来实现这一目标。在大型的网络应用中，我们还可以使用埋点和关键字管理来提供更灵活的用户名限制。在实现这些功能时，我们需要考虑各种因素，例如数据库性能、自然语言处理模型的准确性、日志的存储和分析等。通过综合考虑这些因素，我们可以构建一个既安全又易于管理的用户名系统。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/j5JRTMh0KMoq0dK2MldYPjMayFLdNHOu8WgyNu3UUzibeBmaQjTmnU0PIUm7x9Q5XEXdficf1hvicOQQfwvjHgCPw/0?wx_fmt=png)

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