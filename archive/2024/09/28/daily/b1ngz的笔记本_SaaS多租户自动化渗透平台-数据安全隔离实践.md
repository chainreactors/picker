---
title: SaaS多租户自动化渗透平台-数据安全隔离实践
url: https://mp.weixin.qq.com/s?__biz=MzkwNDE5NzUyMA==&mid=2247483699&idx=1&sn=3d35c690bff8246d0f8e320c59108828&chksm=c08be5ccf7fc6cda4ece5c805eba67be1ee3287684f3db3d2d4d5ca2fe658274cb4a922ddbfb&scene=58&subscene=0#rd
source: b1ngz的笔记本
date: 2024-09-28
fetch_date: 2025-10-06T18:28:15.567458
---

# SaaS多租户自动化渗透平台-数据安全隔离实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1JicUwKQqRQ7VeezpovtfjXuSEPEQ6n98xsofHiclXNElympFICb4S9TZUsako3CsPX1NgEpwrbhQ5cnVFrZ6K0A/0?wx_fmt=jpeg)

# SaaS多租户自动化渗透平台-数据安全隔离实践

原创

b1ngz

b1ngz的笔记本

0x01. 简介

---

在上一篇 [SaaS多租户自动化渗透平台-架构笔记](https://mp.weixin.qq.com/s?__biz=MzkwNDE5NzUyMA==&mid=2247483694&idx=1&sn=f790233f79f52fb60fcd1aefa25d4820&scene=21#wechat_redirect) 中提到了 “客户对 SaaS 形态产品的数据安全性非常敏感”，因此实现数据安全隔离是平台的一个核心要求。同时因产品的定位是自动化渗透平台，用户为专业安全人员，使得保障平台自身的数据安全更加重要。这篇笔记介绍了在多租户架构下，实现数据安全隔离的一些思考和实践，主要内容包括

* 多租户架构数据安全隔离的要求和设计思路
* 基于 Flask、SQLAlchemy、Dramatiq 框架如何实现多租户数据库安全访问
* ORM 框架特性导致出现“数据库跨租户越权”问题的排查过程和解决办法

PS：🔥 团队急招后端研发，感兴趣可私信联系。另外公司正在广纳人才，可复制访问下方链接在线查看职位详情和投递简历

**https://app.mokahr.com/su/5wsls**

# 0x02. 要求和思路

---

在多租户架构下，不同客户的访问和操作均对应同一套代码和服务，如何防止一个用户越权访问到其他租户的数据，是一个非常关键和基础的安全问题。这里首先想到的方案是，每个租户分配一个独立的数据库，有不同的账号密码，并限制访问权限。而从研发安全的视角，需要尽量避免在写业务代码时，手动处理选择和访问数据库资源的操作，即在底层进行统一的封装和屏蔽，实现根据当前用户所属的租户自动选择对应的数据库。而这也依赖用户所属租户的信息无法被篡改和伪造，即需要保证身份认证的安全性

梳理一下，有几个要点

1. 获取当前登陆用户所属租户信息的代码逻辑是安全的
2. 业务代码只关注功能逻辑，对数据库的选择无感知
3. 不同租户对应不同数据库、不同账号密码，无法相互访问

# 0x03. 代码实践

---

平台使用的技术栈为：Web 框架 Flask 、数据库框架 SQLAlchemy、异步任务框架 Dramatiq

实现过程包括

1. 获取当前用户所属租户信息

这里使用 JSON Web Token (JWT) 的方式来保存用户身份和所属租户信息。对于 JWT 的安全，需要确保进行 signature 的验证（第三方库通常默认开启），以及使用的 secret key 复杂度足够强。另外为了避免共用 secret key 泄露后相互影响，这里为每个租户生成不同了 secret key。代码示例如下

```
```
verified_info = jwt.decode(jwt_token, jwt_secret)enterprise_id = verified_info.get("enterprise_id")
```

JWT 安全部分详细可参考 https://portswigger.net/web-security/jwt
```

2. 在当前上下文设置所属租户信息

在 Flask 中提供了 Application Context 来实现在一次请求、CLI 命令等需要在特定执行范围内，管理和共享数据的能力。使用者可在当前上下文环境，通过 `g` proxy 变量来设置、访问、修改数据。详细可参考

* https://flask.palletsprojects.com/en/3.0.x/appcontext/
* flask.g https://flask.palletsprojects.com/en/3.0.x/api/#flask.g

代码实现方面，需要区分不同的业务场景。一是用户使用平台访问 Web 接口，Flask 会在处理请求前后，自动 push 和 pop application context。我们只需要在用户成功登录后，通过`g`变量设置租户的信息，示例代码如下

```
```
from flask import g
g.enterprise_id = "tenant-A"
```

另一个业务场景是执行租户相关的异步任务。此时我们需要
```

1. 在执行任务的前后 push 和 pop application context
2. 发送任务时，自动在参数中添加所属租户信息
3. 执行任务前后，从参数中获取租户信息，通过 `g`变量设置/清除租户信息

在 Dramatiq 框架中，我们可通过编写自定义 Middleware，在对应 hooks 函数中实现以上逻辑，详细参考 https://dramatiq.io/reference.html#middleware

示例代码如下，需求 1 对应 AppContextMiddleware，需求 2，3 对应 EnterpriseMiddleware

```
```
from threading import localfrom dramatiq import Message, Middlewarefrom flask import g

class AppContextMiddleware(Middleware):    # 每个线程有自己独立的 context    STATE = local()
    def __init__(self, app):        self.app = app
    def before_process_message(self, broker, message):        context: AppContext = self.app.app_context()        context.push()        self.STATE.context = context
    def after_process_message(self, broker, message, *, result=None, exception=None):        try:            context = self.STATE.context            context.pop(exception)            del self.STATE.context        except AttributeError:            pass
    after_skip_message = after_process_message

class EnterpriseMiddleware(Middleware):
    def before_enqueue(self, broker, message: Message, delay):        # 发送任务时自动设置  enterprise_id        message.options.setdefault("enterprise_id", g.enterprise_id)
    def before_process_message(self, broker, message):        if enterprise_id := message.options.get("enterprise_id", None):            g.enterprise_id = enterprise_id
    def after_process_message(self, broker, message, *, result=None, exception=None):        g.pop("enterprise_id", None)
    after_skip_message = after_process_message
```
```

3. 数据访问操作时，根据当前所属租户选择对应数据库

在 SQLAlchemy 中，会使用 Session 来进行 ORM 相关操作，我们可以通过重写 Session 的 `get_bind`方法来实现根据第一步中的租户信息 `g.enterprise_id`来动态选择对应数据库连接（通常为 Engine 实例）

代码示例如下

```
```
from flask_sqlalchemy.session import Sessionfrom flask import g
class DynamicSession(Session):    def get_bind(        self,        mapper: t.Any | None = None,        clause: t.Any | None = None,        bind: sa.engine.Engine | sa.engine.Connection | None = None,        **kwargs: t.Any,    ) -> sa.engine.Engine | sa.engine.Connection:        found_bind = None          if bind_key := g.get("enterprise_id", ""):            found_bind = self._db.engines.get(bind_key)                # 其他逻辑 ...
        if not found_bind:            found_bind = super().get_bind(mapper, clause, bind, **kwargs)
        return found_bind
```
```

其中 `self._db.engines`保存了所有租户数据库的连接信息，类型为 map，key 为租户的 ID。这部分由另一个独立的线程定时同步和动态加载租户的数据库连接配置。

详细可参考

* Session.get\_bind https://docs.sqlalchemy.org/en/20/orm/session\_api.html#sqlalchemy.orm.Session.get\_bind
* Engine https://docs.sqlalchemy.org/en/20/core/engines.html

# 0x04. 安全问题

---

在完成上述数据安全隔离措施后，我们仍遇到了在特定场景下 “某个租户获取到了其他租户数据” 的安全问题。

首先介绍发生问题的业务场景“扫描任务的执行”。当用户在平台创建任务后，并不会立刻被运行，而是在“任务队列表”中插入一条数据。再由“任务调度服务”定期检查任务队列表中是否有任务，满足运行的条件后才会发送到队列运行。在多租户架构下，“任务调度服务”会依次访问所有租户的数据库进行检查，其代码示例如下

```
while True:    enterprise_ids = get_enterprise_ids()        for enterprise_id in enterprise_ids:      # 设置 g.enterprise_id 值，用于切换数据库      with bind_enterprise(enterprise_id):        # 查询待运行的任务列表        stmt = select(TaskQueue).where(TaskQueue.handled == false())        tasks = session.scalars(stmt).all()        # ... 运行条件检查        # 发送任务到队列        for task in tasks:          _send_task(task)          # 每个租户单次只发送一个任务          break        time.sleep(1)
```

`TaskQueue` model 的定义如下

```
class TaskQueue(Base):  id: Mapped[int] = mapped_column(    BigInteger(), primary_key=True  )  task_id: Mapped[int] = mapped_column(    BigInteger(), nullable=False, index=True  )  # 任务对应的全局唯一消息 UUID  message_id: Mapped[str] = mapped_column(    String(36), index=True, nullable=False  )  # 是否已处理  handled: Mapped[bool] = mapped_column(        Boolean(), default=False, server_default=false()  )
```

运行任务的代码函数

```
@dramatiq.actor(queue_name="task")def run_flow_task(task_id):    try:      obj = get_task_obj_by_id(task_id)      ...    except Exception:      ...
```

某天监控告警发现，在租户 A 下运行任务报错，错误信息为“task\_id = 121 在数据库里任务记录不存在”，其消息 ID（message\_id）为 `6d4a0abc-d277-44db-8f6a-2a90491b1dee`。之后我们开始排查，在租户 A 对应的数据库中，最大的任务 ID 为 39，确实不存在 121 的记录。接着开始查询 “任务调度服务” 的日志，发现日志中的参数值和错误信息能对应上

任务调度服务日志

```
租户A：send message_id='xxxx' task_id=37租户A：send message_id='6d4a0abc-d277-44db-8f6a-2a90491b1dee' task_id=121租户A：send message_id='xxxx' task_id=39
```

根据前后的日志判断，正确的 task\_id 应该是 38。到租户 A 的 “任务队列表” 中查看，确实有 38，但 message\_id 是 `47fb72b3-64dd-460d-bc03-bccfe18fa039`与前面任务调度器的日志对应不上

租户A-任务队列表数据

```
id, task_id, message_id40, 37, xxxxx     41, 38, 47fb72b3-64dd-460d-bc03-bccfe18fa03942, 39, xxxx
```

“任务调度服务日志” 中有一个需要注意的点是，前后 task\_id 37 和 39 的两个任务是正常运行的，经过手工测试，也无法复现该问题。

因为 message\_id  为全局唯一消息 ID，根据日志查询到 `47fb72b3-64dd-460d-bc03-bccfe18fa039`属于租户B，其“任务队列表表”数据如下，task\_id 为 `121` 也能对的上

租户B-任务队列表数据

```
id, task_id, message_id41, 121, 47fb72b3-64dd-460d-bc03-bccfe18fa039
```

上述问题的表现像是“租户A”读取到的“租户B”下的数据，出现了跨租户越权的问题。起初我们怀疑是代码实现有问题，但经过排查和讨论，并未找到原因。

我们又继续排查任务调度日志，发现在租户A之前，调度的上一个租户恰巧是租户B的，且也找到了同 `message_id`和 `task_id`的任务发送日志（第一行和第四行）

```
租户B：send message_id='6d4a0abc-d277-44db-8f6a-2a90491b1dee' task_id=121...租户A：send message_id='xxxx' task_id=37租户A：send message_id='6d4a0abc-d277-44db-8f6a-2a90491b1dee' task_id=121租户A：send message_id='xxxx' task_id=39
```

再根据 “任务队列表” 的数据对比，发现这两条数据拥有相同的数据库主键值，id 均为 41

```
租户Aid, task_id, message_id41, 38, 47fb72b3-64dd-460d-bc03-bccfe18fa039

租户Bid, task_id, message_id41, 121, 47fb72b3-64dd-460d-bc03-bccfe18fa039
```

根据上述表现，我们怀疑是业务层代码在进行数据库查询时，没有刷新已加载到内存中的数据。

经过文档的搜索，发现在 SQLAlchemy ORM 中存在一个默认特性，“同一主键 model object 只会被 load 一次，后续再次查询不会更新当前 object 的状态”，目的为了保留内存中 model 已经被修改的状态，以及避免刷新已经存在数据的成本和复杂度。官方文档中的描述原文为

Normally, ORM objects are only loaded once, and if they are matched up to the primary key in a subsequent result row, the row is not applied to the object. This is both to preserve pending, unflushed changes on the object as well as to avoid the overhead and complexity of refreshing data which is already there.

文档地址：https://docs.sqlalchemy.org/en/20/orm/queryguide/api.html#populate-existing

我们来看一个代码示例，以便更好的理解特性背后的表现，这里有一个 User model，有 ...