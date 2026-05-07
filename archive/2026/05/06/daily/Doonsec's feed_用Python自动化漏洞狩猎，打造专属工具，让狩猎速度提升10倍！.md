---
title: 用Python自动化漏洞狩猎，打造专属工具，让狩猎速度提升10倍！
url: https://mp.weixin.qq.com/s/gymd7aPTPHPkc1Xcu49diQ
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:31:30.119986
---

# 用Python自动化漏洞狩猎，打造专属工具，让狩猎速度提升10倍！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnvrtbTibSYQ1F5uVEknIABR4GWYR47sJibeS0k7dX4gECRufZYesVtymx0lFicgARcJvj6iaSJnCuPlm3jBJ0m0Qtr0wFdxYPTHdGQ/0?wx_fmt=jpeg)

# 用Python自动化漏洞狩猎，打造专属工具，让狩猎速度提升10倍！

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#

# 官网：http://securitytech.cc

#

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnubgicR8ib7PMdyfBZrVo4ib3joGaUl3sBicWeglo83QGicR3OZnEuy58uFgnkmk1aBze7serdwSM0lkuIvAOR3VxaZCqCQJbLgfjEk/640?wx_fmt=png&from=appmsg)

## 今天学什么？

* 漏洞赏金的 Python 基础知识——快速回顾
* 针对HTTP请求发起攻击
* 创建自定义的IDOR扫描器
* 创建子域名暴力破解工具
* 创建API密钥暴露扫描器
* 多线程速度提升10倍
* 完整的重建自动化流水线

> **为什么一定要这么做？** 手动测试 = 慢 = 缺少漏洞！**Python自动化 = 10倍速度 = 10倍漏洞 = 10倍赏金！**顶尖猎手们会开发自己的定制工具，去挖掘那些通用工具遗漏的细节！这是**高级系列的第一篇文章**，从今以后，我们不仅要做猎手，还要成为**工具开发者**！
>
> ## 为什么我的漏洞赏金是Python？

```
1. 通用工具（Nuclei、Subfinder等）：

3. →所有猎人都拥有

5. →相同结果=重复风险 zyada！
6. →无法自定义逻辑，我的Python工具：

8. →只有你才有！

10. →自定义逻辑=独特的漏洞！
11. →针对特定目标进行优化

13. →多种技术串联起来

15. →可以集成AI！真正差异：

17. 100个猎人核心正在狩猎=相同结果

19. 1款猎人定制Python工具，挑战来袭！=独一无二！Python=漏洞赏金的秘密武器！🐍
```

## 第一部分：设置环境，准备Karo

```
1. # 检查 Python 3.10+：

3. python3 --version# 创建虚拟环境（最佳实践！）：
4. python3 -m venv bugbounty_env
5. 来源 bugbounty_env/bin/activate
6. # Windows: bugbounty_env\Scripts\activate# 一次性安装必备库：
7. pip 安装 requests \
8. httpx \
9. aiohttp \
10. BeautifulSoup4
11. lxml \
12. 颜色ama \
13. 丰富的
14. tqdm \
15. python-dotenv \
16. argparse# 验证安装：
17. python3 -c "import requests, colorama, rich; \

19. print('✅ 所有库已就绪！')
```

## 第二部分：HTTP请求基础 学习一下

## 基本请求：

```
1. import requests# ─── GET请求 ──────────────────────────

3. r = requests.get("https://target.com/api/user")
4. print(r.status_code)# 200、401、403、500……
5. print(r.text)# 完整响应体
6. print(r.json())# JSON解析（如果为JSON格式）
7. print(r.headers)# 响应头
8. print(r.cookies)# Cookies# ─── 带参数的GET请求 ──────────────────
9. 参数={"id":"1001","format":"json"}
10. r = requests.get(
11. “https://target.com/api/user”，
12. 参数=参数
13. )
14. # 最终URL：/api/user?id=1001&format=json# ─── 使用JSON的POST请求──────────────────────
15. 数据={"用户名":"admin","密码":"test123"}
16. r = requests.post(
17. “https://target.com/login”，
18. json=数据，# 自动内容类型：JSON
19. 超时=10
20. )#───包含头信息与Cookie的完整请求──
21. 头部={
22. “授权”:“Bearer YOUR_JWT_TOKEN”,
23. “用户代理”：Mozilla/5.0(X11;Linux x86_64)
24. “X-Forwarded-For”：“127.0.0.1”
25. }
26. cookies ={"session":"ABC123XYZ"}r = requests.get(
27. “https://target.com/api/dashboard”
28. headers=headers,
29. 饼干=饼干，
30. verify=False,# 跳过SSL检查（仅用于测试！）
31. 超时=10，
32. 允许重定向=True

34. )
```

## 会话对象 Cookie 自动管理：

```
1. import requests# 会话 = 登录一次——所有请求都用这个会话

3. # 自动化Cookie保持！session = requests.Session()# 第一步：登录

5. 会话.post(

7. “https://target.com/login”，

9. json={"用户":"attacker@test.com",

11. “密码”:“mypassword123”}

13. )

15. # ✅ 会话Cookie自动保存！# 第二步：经过身份验证的请求——Cookie自动附加！

17. r1 =会话.get("https://target.com/api/profile/1002")

19. r2 =会话.get("https://target.com/api/invoices/9876")

21. r3 = session.get("https://target.com/api/messages/555")print(r1.text)# 受害者个人资料——IDOR测试！

23. print(r2.text)# 受害者的发票！
24. print(r3.text)# 私密消息！# ─── Requests 忽略 SSL 警告 ─────────

26. 导入urllib3

28. urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

## 第三部分：打造属于你的自定义IDOR扫描器！

```
1. #!/usr/bin/env python3

3. """

5. IDOR扫描器v2.0 — HackerMD

7. 测试数字 + UUID ID 参数
```

python import requests

```
1. 导入 json

3. 导入时间
4. 来自colorama的Fore、Style和init
5. import urllib3urllib3.disable_warnings()
6. init(autoreset=True)类IDORScanner:
7. def __init__(self, base_url, token,
8. 我的ID，ID范围=(1,200)，
9. 延迟=0.1）：
10. self.base_url = base_url
11. self.my_id = my_id
12. self.id_range = id_range
13. self.delay =延迟
14. self.session = requests.Session()
15. self.session.headers.update({
16. “授权”: f“Bearer{token}”,
17. “用户代理”:“Mozilla/5.0”
18. })
19. self.session.verify =False
20. self.脆弱=[]
21. self.errors =0def get_baseline(self):
22. 获取你的数据——基线长度
23. 尝试：
24. r =self.session.get(
25. f"{self.base_url}/{self.my_id}",
26. 超时=10
27. )
28. 返回 r.status_code, len(r.text)
29. 除Exception以外：
30. print(f"{Fore.YELLOW}⚠️ 基线错误：{e}")
31. 返回空值，0def test_single_id(self, test_id, base_len):
32. “测试单个ID”
33. 尝试：
34. r =self.session.get(
35. f"{self.base_url}/{test_id}",
36. 超时=10
37. )# 200 + 长度显著不同
38. # = 可能是不同用户的数据！
39. 长度差= abs(len(r.text)-基线长度)如果 r.status_code ==200且长度差>30：
40. 返回{
41. “id”:测试ID，
42. “状态”：r.status_code，
43. “长度”：len(r.text)，
44. “差异”：长度差异，
45. “预览”：r.text[:150]
46. }
47. 除 requests.exceptions.Timeout之外：
48. self.errors +=1
49. 除了Exception作为 e：
50. self.errors +=1
51. 返回空def扫描(self):
52. 打印(f"
53. {Fore.CYAN}╔══════════════════════════════╗）
54. print(f"{Fore.CYAN}║   IDOR扫描器—HackerMD║")
55. print(f"{Fore.CYAN}╚══════════════════════════════╝")
56. 打印(f"目标：{self.base_url}")
57. print(f"我的ID   :{self.my_id}")
58. print(f"范围:{self.id_range[0]}–{self.id_range[1]}")
59. print(f"延迟:{self.delay}秒")
60. print("─" * 40)        # 基线
61. 基础状态，基础长度 = 自我获取基线()
62. 如果基础状态不存在：
63. print(f"{Fore.RED}❌无法连接目标！")
64. 返回        打印(f"基准：{base_status}|{base_len}字节")
65. )        # 扫描卡罗
66. 总和 = self.id_range[1] - self.id_range[0]
67. 对于 i，测试 ID in enumerate(
68. 范围(self.id_range[0], self.id_range[1]+1)
69. ):
70. 如果 test_id == self.my_id：
71. 继续            # 进度条
72. 进度 = int((i / 总数) * 30)
73. bar = “█” * 进度 + “░” * (30 - 进度)
74. 百分比 = 整数((i / 总数) × 100)
75. print(f"\r{Fore.CYAN}[{bar}]{pct}%|")
76. f"测试ID：{test_id}",
77. end="", flush=True)            result = self.test_single_id(
78. 测试ID，基础长度
79. )            如果结果：
80. 打印(f"
81. {Fore.RED}🔴可能存在IDOR！)
82. print(f"   ID      : {result['id']}")
83. print(f"   状态  : {result['status']}")
84. print(f"   长度  : {result['length']}")
85. f"(差值：{result['diff']})")
86. 打印(f"   预览："
87. f"{result['preview'][:80]}...”
88. self.vulnerable.append(result)            time.sleep(self.delay)        # 总结
89. 打印(f"
90. {'─'*40}
91. print(f"✅ 扫描完成！")
92. 打印(f"   测试：{total} 个ID")
93. 打印(f"   找到   : "
94. f"{Fore.RED}{len(self.vulnerable)}"
95. “{Style.RESET_ALL}潜在的IDOR”
96. print(f"   错误  : {self.errors}")# 保存结果
97. 如果self.脆弱：
98. 输出文件=“idor_results.json”
99. with open(out_file,"w")as f:
100. json.dump(self.vulnerable, f, indent=2)
101. print(f"   已保存   : {out_file}")returnself.vulnerable# ─── 使用方法 ────────────────────────────────
102. 如果 __name__ =="__main__":
103. 扫描仪= IDOR扫描仪(
104. base_url ="https://target.com/api/v1/invoices",
105. 令牌=“您的认证令牌在这里”,
106. 我的ID     =1050，
107. id_range =(1000,1150),
108. 延迟=0.1# 用于避免速率限制！
109. )

111. 扫描仪.扫描()
```

## 第4部分：多线程子域名爆破工具！

```
1. #!/usr/bin/env python3

3. """

5. 子域名暴力破解器 v2.0 — HackerMD

7. 快速多线程子域名发现
```

python import requests

```
1. 导入线程

3. 来自队列的队列
4. 来自colorama的Fore、Style和init
5. 导入时间
6. 导入 jsonurllib3 已导入=False
7. 尝试：
8. 导入urllib3
9. 禁用 urllib3 警告
10. urllib3已导入=True
11. 除了：
12. passinit(autoreset=True)类子域名爆破器：
13. def __init__(self, domain, wordlist_path,
14. 线程数=50，超时=5）
15. self.domain        =域名
16. self.wordlist =self.load_wordlist(wordlist_path)
17. self.threads = threads
18. self.timeout       =超时
19. self.queue =Queue()
20. self.found         =[]
21. self.lock= threading.Lock()
22. self.checked=0
23. self.total = len(self.wordlist)
24. self.start_time =Nonedef load_wordlist(self, path):
25. 尝试：
26. with open(path,"r", errors="ignore")as f:
27. words =[line.strip()for line in f]
28. 如果行.strip()]
29. print(f"✅ 词表已加载：{len(words)} 个词")
30. 返回单词
31. 除了FileNotFoundError：
32. print(f"❌ 未找到字典文件：{path}")
33. # 默认小列表
34. 返回[
35. “www”、“mail”、“ftp”、“admin”、“api”，
36. “开发”、“测试”、“预发布”、“beta”、“旧版”，
37. 应用、门户、仪表板、安全、
38. “vpn”、“内部”、“备份”、“cdn”、“博客”，
39. 商店、店铺、支持、文档、Git
40. ]def check_subdomain(self, subdomain):
41. “检查单个子域名”
42. url = f"https://{子域名}.{self.domain}"
43. 尝试：
44. r = requests.get(
45. 网址，
46. 超时=self.超时，
47. 验证=False，
48. 允许重定向=True
49. )
50. 使用self.lock：
51. self.found.append({
52. “子域名”：f"{子域名}.{self.domain}",
53. “状态”：r.status_code，
54. “长度”：len(r.text),
55. “服务器”: r.headers.get(
56. “服务器”，“未知”
57. ),
58. “url”: url
59. })# 按状态码着色：
60. 如果 r.status_code ==200：
61. 颜色=前景.绿色
62. 如果 r.status_code 在[301,302]中：
63. 颜色=前景.黄色
64. 如果 r.stat...