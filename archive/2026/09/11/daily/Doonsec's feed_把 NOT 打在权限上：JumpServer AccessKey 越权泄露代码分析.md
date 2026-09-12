---
title: 把 NOT 打在权限上：JumpServer AccessKey 越权泄露代码分析
url: https://mp.weixin.qq.com/s/0z3URWxrpyFwVsma9Ps_fQ
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:47:48.703276
---

# 把 NOT 打在权限上：JumpServer AccessKey 越权泄露代码分析

# 把 NOT 打在权限上：JumpServer AccessKey 越权泄露代码分析

原创

Kratos
Kratos

Kratos Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 把 NOT 打在权限上：JumpServer AccessKey 越权泄露代码分析

JumpServer 昨天发了通告（JS-2026.09.09），修了一个很漂亮的漏洞：任意已登录的普通用户，在请求里加两个查询参数，就能把全平台所有用户的 AccessKey 明文拖走——包括管理员的。这一个 GET 请求长这样：

```
GET /api/v1/authentication/access-keys/?action=create&_rel=not
```

没有注入，没有溢出，没有一个字节在"逃逸"。每个模块都严格按设计工作，但两个设计拼在一起，权限模型整体翻车。本文基于官方补丁（PR #17295）反推，逐行讲清楚这个漏洞是怎么长出来的。全文分析基于 v4.10.18 漏洞版本源码，属于代码级确认；官方通告与第三方公开复现已验证可利用性。

## 0x0 漏洞概述

| 项目 | 内容 |
| --- | --- |
| 漏洞类型 | 越权读取（认证后信息泄露） |
| 编号 | GHSA-6rp5-ff2m-qfrm（暂无 CVE）/ 国内威胁情报平台收录 QVD-2026-65008 |
| CVSS 3.1 | 8.8（AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H） |
| 影响版本 | v3.7.0 ~ v3.10.22；v4.0.0 ~ v4.10.18 |
| 修复版本 | v3.10.23-lts / v4.10.19-lts |
| 利用条件 | 一个普通账号能登录 Web（内置角色默认权限即可），无其他前置条件 |
| 报告者 | Sajjad Haqi（Smart Oasis），2026 年 8 月报告 |

攻击效果：拿到管理员的 AccessKey ID + Secret 后，可通过 HTTP 签名认证以管理员身份调用全部 REST API。堡垒机的 API 就是资产的入口——资产清单、账号凭据、会话记录、命令记录都在后面。

先给一句话论点，后面全部围绕它展开：

> JumpServer 把"属主过滤"和"业务过滤"写在了同一棵查询树里，然后又把改写这棵树的能力，通过查询参数发给了客户端。

## 0x1 权限模型：两层防线，第二层是 queryset

先看 JumpServer 通用 API 视图的权限是怎么落的。以 AccessKey 接口为例（`apps/authentication/api/access_key.py`）：

```
class AccessKeyViewSet(JMSModelViewSet):
    serializer_classes = {
        'default': AccessKeySerializer,
        'create': AccessKeyCreateSerializer
    }
    search_fields = ['^id']
    permission_classes = [RBACPermission]

    def get_queryset(self):
        return self.request.user.access_keys.all()
```

这里有两层完全不同性质的防线：

* **第一层，动作级**：`RBACPermission`。检查"你能不能对这个资源执行 list 动作"，对应 RBAC 里的 `authentication.view_accesskey`。
* **第二层，对象级**：`get_queryset()` 返回 `self.request.user.access_keys.all()`。注意这个写法——它不是"查出所有再在 serializer 里过滤"，而是把"只属于我"这个约束**编译进 SQL 的 WHERE 子句**。Django ORM 的惯例做法，也是 DRF 官方推荐的越权防护姿势。

第一层对普通用户是放行的。看内置角色定义（`apps/rbac/builtin.py`）：

```
system_user_perms = (
    ('authentication', 'connectiontoken', 'add,view,reuse,expire', 'connectiontoken'),
    ('authentication', 'temptoken', 'add,change,view', 'temptoken'),
    ('authentication', 'accesskey', '*', '*'),
    ...
)
```

系统用户（每个普通用户默认持有的角色）对 `accesskey` 拥有 `*` 全权限——这是合理的，用户本来就要管理自己的 API 密钥。所以整个漏洞的成败，完全取决于第二层那行 `access_keys.all()` 能不能守住。攻防焦点就这一个。

## 0x2 根因一：一个允许客户端改写查询树的过滤器

通用过滤器文件 `apps/common/drf/filters.py` 的第 413 行，v4.10.18 版本：

```
class NotOrRelFilterBackend(filters.BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name="_rel",
                location="query",
                required=False,
                type="string",
                example="/api/v1/users/users?name=abc&username=def&_rel=union",
                description="Filter by rel, or not, default is and",
            )
        ]

    def filter_queryset(self, request, queryset, view):
        _rel = request.query_params.get("_rel")
        if not _rel or _rel not in ("or", "not"):
            return queryset
        if _rel == "not":
            queryset.query.where.negated = True
        elif _rel == "or":
            queryset.query.where.connector = "OR"
        queryset._result_cache = None
        return queryset
```

这个类的本意很朴素：前端有时需要"多条件取并集"或"排除某些结果"，于是给了个 `_rel` 参数，让客户端声明多个过滤条件之间的关系是 AND、OR 还是 NOT。设计意图是**取反客户端自己提供的过滤表达式**。

但实现只有三行核心逻辑，每一行都在错位：

**第一处错位：操作对象错了。**

```
queryset.query.where.negated = True
```

`queryset.query.where` 是 Django ORM 组装完毕的整棵 WHERE 树——**到这个 backend 执行时，树上挂的早就不只是客户端的过滤条件了**。`get_queryset()` 写死的属主约束 `user_id = <me>`，还有前面所有 filter backend 追加的条件，全在这棵树上。给 `WhereNode.negated` 打 True，Django 生成 SQL 时会给**整棵树**包一个 NOT：

```
-- 正常请求
SELECT ... FROM authentication_accesskey WHERE user_id = 'me';

-- _rel=not 之后
SELECT ... FROM authentication_accesskey WHERE NOT (user_id = 'me');
```

"只看我的"一步变成"只看所有不是我的"。权限边界不是被绕过，是被精确反转——比绕过更狠，你自己的记录反而查不到了。

**第二处错位：执行时机错了。**

看它被挂载的位置，`apps/common/api/mixin.py`：

```
def get_filter_backends(self):
    self.set_compatible_fields()
    if self.filter_backends != self.__class__.filter_backends:
        return self.filter_backends
    backends = list(chain(
        self.filter_backends,
        self.default_added_filters,
        self.extra_filter_backends,
    ))
    # 这个要放在最后
    backends.append(NotOrRelFilterBackend)
    return backends

def filter_queryset(self, queryset):
    for backend in self.get_filter_backends():
        queryset = backend().filter_queryset(self.request, queryset, self)
    return queryset
```

注意那行注释：\*\*"这个要放在最后"\*\*。为什么？因为要等属主约束、业务过滤全部组装完毕之后再动手，才能"完整地"取反。写这行注释的人离正确答案只差一步：如果把"最后"再往后想一层——最后意味着取反的对象包含权限——这个漏洞在 code review 阶段就该死掉。这行注释是整个漏洞的墓志铭。

**第三处错位：能力下发错了。**

`queryset._result_cache = None` 这行是清掉已执行查询的结果缓存，确保前面的改写生效。说明作者很清楚自己在修改一棵"已经组装完"的查询树——这是 ORM 的内部结构，正常业务代码都不该碰的层，如今被一个查询参数直通。还嫌不够显眼，`get_schema_fields` 把 `_rel` 注册进了 API 文档，example 示范、description 齐全。一个文档化的后门。

顺带说 `_rel=or` 变体：`query.where.connector = "OR"` 把顶层连接符从 AND 改成 OR：

```
-- 正常：属主约束 AND 过滤条件，两者都要满足
WHERE user_id = 'me' AND (id LIKE 'xx%')

-- _rel=or 之后：满足任意一个即可
WHERE user_id = 'me' OR (id LIKE 'xx%')
```

只要右边任何一个宽松条件成立，属主约束即告失效。这是同一种错误的另一种表达：**逻辑连接符也是查询树的一部分，也不该归客户端管**。

## 0x3 根因二：允许客户端挑选 serializer

第一个根因负责"越权看到别人的记录"，但默认情况下列表响应里没有密钥。第二个根因负责把密钥加进响应。

通用 serializer 选择逻辑，`apps/common/api/serializer.py`：

```
def get_serializer_class_by_view_action(self):
    serializer_classes = self.get_serializer_classes()
    ...
    view_action = self.request.query_params.get('action') or self.action or 'list'
    if self.request.query_params.get('format'):
        view_action = 'retrieve'
    serializer_class = serializer_classes.get(view_action)
    ...
```

漏洞就在第一行：

```
view_action = self.request.query_params.get('action') or self.action or 'list'
```

`self.action` 是 DRF 根据 HTTP 方法 + URL 结构推导出的真实动作（list/retrieve/create/...），这本该是唯一依据。但这里让查询参数 `?action=`**优先于**真实动作。客户端发的是 GET list 请求，却可以声明"请用 create 的 serializer 来序列化结果"。

对照 AccessKey 的两个 serializer（`apps/authentication/serializers/token.py`）：

```
class AccessKeySerializer(serializers.ModelSerializer):
    ...
    class Meta:
        model = AccessKey
        fields = ['id', 'is_active', 'date_created', 'date_last_used'] + ['ip_group']
        read_only_fields = ['id', 'date_created', 'date_last_used']

class AccessKeyCreateSerializer(AccessKeySerializer):
    class Meta(AccessKeySerializer.Meta):
        fields = AccessKeySerializer.Meta.fields + ['secret']
```

| serializer | 挂载动作 | 字段 |
| --- | --- | --- |
| `AccessKeySerializer` | default / list | id、is\_active、日期、ip\_group —— **无 secret** |
| `AccessKeyCreateSerializer` | create | 上面全部 + **secret 明文** |

这个字段设计本身是讲究的：列表页只给元数据，密钥只在"创建"那一刻回显一次。`AccessKey.secret` 在数据库里是明文存储的（后面签名校验要用，没法只存哈希），所以"不出现在 list serializer"就是它唯一的防线。而 `?action=create` 一参数，防线蒸发。

## 0x4 组合成枪：一次 GET 的完整解剖

现在把三个部件拼起来。普通用户登录后发起：

```
GET /api/v1/authentication/access-keys/?action=create&_rel=not
Authorization: Bearer <普通用户自己的token>
```

沿着 DRF 的处理管线走一遍：

1. **认证**：Bearer token 有效，`request.user` = 普通用户。
2. **RBAC（第一层防线）**：真实动作是 `list`，检查 `authentication.view_accesskey`。内置角色给了 `*`，**放行**——用户本来就有权 list 自己的密钥，无可指摘。
3. \*\*`get_queryset()`\*\*：返回 `access_keys.filter(user_id = me)`，属主约束进树。
4. \*\*`filter_queryset()`\*\*：backend 链依次执行。前面的 backend 没收到对应参数，原样放行；最后一个 `NotOrRelFilterBackend` 读到 `_rel=not`，整棵树打上 NOT。
5. **serializer 选择**：`query_params.get('action')` 返回 `'create'`，命中 `AccessKeyCreateSerializer`。
6. **序列化输出**：其他所有用户的 AccessKey，带 `secret` 明文，分页返回。

两个根因单独存在时都不致命：

* 只有 `_rel=not`，没有 `?action=create`：能越权看到别人的密钥**记录**，但 serializer 只有元数据——拿到一堆 key id，没有 secret。
* 只有 `?action=create`，没有 `_rel=not`：响应里确实带 secret 字段，但查询范围被属主约束锁死——看到的全是自己的密钥。

组合起来，`WHERE NOT (user_id = 'me')` × 带 secret 的 serializer = **全平台所有 AccessKey 明文**。这才是它作为高危（8.8）的完整形态：CVSS 里那个 `C:H` 不是虚的。

还有一个细节堵死了"运维侧补救"的幻想：`AccessKeyViewSet.get_permissions()` 里有密码二次确认——但触发条件是 `self.action == 'create'`，而 `self.action` 始终是真实动作 `list`，查询参数骗不了它。密码确认防的是真创建，防不了借尸还魂的序列化。

## 0x5 拿到密钥之后：为什么这是"接管"级漏洞

泄露的 secret 明文能干什么？看签名认证的实现。JumpServer 支持 HTTP Signature 认证（`apps/common/auth/signature.py` + `apps/authentication/back...