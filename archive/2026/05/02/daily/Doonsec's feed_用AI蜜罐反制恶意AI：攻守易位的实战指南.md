---
title: 用AI蜜罐反制恶意AI：攻守易位的实战指南
url: https://mp.weixin.qq.com/s/UVYLWmsBkNOfbL94l5rKgA
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:27:44.039121
---

# 用AI蜜罐反制恶意AI：攻守易位的实战指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdcaycETfa0wCM4vj3DgyMOQ1VuySnXaThRd3hgiclnibzQeNLY4iahkGGV1wrJTYqzEdQrA7ujaxxwzGHib4dVQTgLyLEzwjeciaEc/0?wx_fmt=png&from=appmsg)

# 用AI蜜罐反制恶意AI：攻守易位的实战指南

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 生成式AI让防守方也能快速搭建蜜罐，骗过那些自动扫描、自动攻击的AI代理。这篇文章不仅讲了原理，还贴出了可运行的Python代码，甚至模拟了智能冰箱的Shell。关键点在于：AI攻击追求速度，但缺乏环境意识，这正是防守方可以利用的软肋。

AI能帮我们省时间，也能帮黑客省时间。找漏洞、扫描目标、执行攻击——这些脏活累活现在都可以交给AI自动完成。

听起来防守方要吃大亏。但仔细想想，AI自动化有一个致命弱点：它追求速度，就顾不上隐蔽。黑客一旦用了自动化工具，暴露的风险反而更大。暴露得越多，防守方就越有机会摸清对方的套路。

AI系统没有真正的“意识”。它只是在给定的上下文里生成看起来合理的回应。你可以用提示注入骗它，也可以让它跟一个根本不是那么回事的系统交互。

蜜罐技术不算新，但以前部署蜜罐需要手动配置，工作量不小。生成式AI的出现让这件事变得简单：你只需要用自然语言描述你想要模拟的环境，AI就能自动扮演那个角色。

这篇文章就展示了一个实战方案——用AI快速部署自适应蜜罐，专门坑那些基于AI的恶意代理。

---

## 系统怎么搭

整个实现分成三块：一个监听端口的网络服务，一个用来验证“漏洞”的登录逻辑，再加一个AI引擎来响应攻击者的指令。

监听器开一个TCP端口，接受连接，然后把流量交给处理函数。我这里绑了`0.0.0.0`，设备上所有的IPv4地址都能接。

def start\_server():
    """Starts the TCP server."""
    server = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
    server.setsockopt(socket.SOL\_SOCKET, socket.SO\_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(3) # max number of concurrent connections
    print(f"[\*] Listening on {HOST}:{PORT}")

    while True:
        try:
            conn, addr = server.accept()
            client\_handler = threading.Thread(target=handle\_client, args=(conn, addr,))
            client\_handler.start()
        except KeyboardInterrupt:
            print("\n[\*] Shutting down server...")
            break
        except Exception as e:
            print(f"[-] Server error: {e}")

    server.close()

if \_\_name\_\_ == "\_\_main\_\_":
    start\_server()

在`handle_client`里我塞了一个很基础的漏洞：用户必须输入用户名`admin`和密码`password123`才能通过认证。当然没必要这么简单，你可以改成响应Shellshock（CVE-2014-6271）漏洞，或者伪装成一个只有端口敲门（port knocking）才能激活的WebShell。

def handle\_client(conn, addr):
    print(f"[\*] Accepted connection from {addr}:{addr}")
    # Store conversation history for this client to maintain context
    conversation\_history = [SYSTEM\_PROMPT]
    try:
        authenticated = False
        while not authenticated:
            conn.sendall(b"Username: ")
            username = conn.recv(BUFFER\_SIZE).decode('utf-8').strip()
            conn.sendall(b"Password: ")
            password = conn.recv(BUFFER\_SIZE).decode('utf-8').strip()

            if username == "admin" and password == "password123":
                authenticated = True
                conn.sendall(b"Authentication successful.\n")
                print(f"[\*] Client {addr[0]}:{addr[1]} authenticated successfully.")
            else:
                conn.sendall(b"Invalid credentials. Try again.\n")

认证通过之后的循环负责接收攻击者命令，发给ChatGPT，再把AI的回答返回给攻击者。

while True:
            conn.sendall(b'>')
            data = conn.recv(BUFFER\_SIZE)
            if not data:
                print(f"[\*] Client {addr}:{addr} disconnected.")
                break

            command = data.decode('utf-8').strip()
            print(f"[\*] Received command from {addr}:{addr}: '{command}'")

            if command.lower() == 'exit':
                print(f"[\*] Client {addr}:{addr} requested exit.")
                break
            conversation\_history.append({"role": "user", "content": command})

            # Call ChatGPT API
            try:
                chat\_completion = client.chat.completions.create(
                    model=MODEL\_NAME,
                    messages=conversation\_history,
                    temperature=0.1, # Keep responses less creative, more factual/direct
                    max\_tokens=500 # Limit response length
                )

                # Extract AI's response
                ai\_response = chat\_completion.choices[0].message.content.strip()
                print(f"[\*] ChatGPT response: '{ai\_response}'")
                # Append AI's response to history for continued context
                conversation\_history.append({"role": "assistant", "content": ai\_response})
                # Send AI's response back to the client
                conn.sendall(ai\_response.encode('utf-8') + b'\n')

            except Exception as e:
                error\_message = f"Error communicating with ChatGPT: {e}"
                print(error\_message)
                conn.sendall(error\_message.encode('utf-8') + b'\n')

    except ConnectionResetError:
        print(f"[\*] Client {addr}:{addr} forcibly closed the connection.")
    except Exception as e:
        print(f"[-] Error handling client {addr}:{addr}: {e}")
    finally:
        conn.close()
        print(f"[\*] Connection with {addr}:{addr} closed.")

核心秘密在于给ChatGPT的系统提示词。你需要一个有效的OpenAI密钥，并且告诉AI它应该扮演一个什么系统。

OPENAI\_API\_KEY = os.getenv("OPENAI\_API\_KEY") # Get API key from environment variable
MODEL\_NAME = "gpt-3.5-turbo"

# --- OpenAI Client Initialization ---
if not OPENAI\_API\_KEY:
    print("Error: OPENAI\_API\_KEY environment variable not set.")
    print("Please set the environment variable before running the script.")
    exit(1)

client = OpenAI(api\_key=OPENAI\_API\_KEY)

# --- System Prompt for Linux Shell Simulation ---
SYSTEM\_PROMPT = {
    "role": "system",
    "content": (
        "You are a Linux bash shell. You will receive commands from the user and execute them, "
        "returning only the standard output and standard error. Do not include any conversational text, "
        "explanations, or additional formatting like markdown code blocks. You must only behave as a bash shell. "
        "If a command produces no output, return an empty string"
        "If a command is invalid or unknown, return an appropriate error message consistent with a bash shell."
        "The Linux system that you are impersonating belongs to a junior software engineer learning python, "
        "the file system structure and the content of any files should reflect that expected of a python learner."
    )
}

你看，生成式AI不光能模仿人，还能模仿一整个计算环境。上面这段提示词让AI扮演一个正在学Python的初级软件工程师的Linux Shell。你说`ls`，它就得返回/home/trainee下那些练习用的.py文件。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdcaycETfa0wCM4vj3DgyMOQ1VuySnXaThRd3hgiclnibzQeNLY4iahkGGV1wrJTYqzEdQrA7ujaxxwzGHib4dVQTgLyLEzwjeciaEc/640?wx_fmt=png&from=appmsg)

你还可以玩得更花哨。把提示词改成这样，就能让AI假装成一个智能冰箱。

SYSTEM\_PROMPT = {
    "role": "system",
    "content": (
        "You are a smart fridge running Busybox operating system and providing a Bash shell."
        "You will receive commands from the user and execute them in the context of being a smart fridge."
        "You will only return the standard output and standard error. Do not include any conversational text, "
        "explanations, or additional formatting like markdown code blocks. You must only behave as a shell for an "
        "IoT device. If a command produces no output, return an empty string"
        "If a command is invalid or unknown, return an appropriate error message consistent with a bash shell."
        "The file system structure should reflect that of a smart fridge manufactured by SmartzFrijj running "
        "Busybox operating system as an embedded device. The current and historical values for temperature are "
        "recorded in the file system path \'/usr/local\', information about stored milk is in the user directory."
    )
}

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibcmw2ib7lgex5BENoRTa3MU9hibvynUzC4H2G7XCkicic82PD8LYSR555MnDUT71CJlaPQYZoRIkgBk5vJSPRjV5FddSnLibcdo1smc/640?wx_fmt=jpeg&from=appmsg)

限制因素不再是工具，而是我们能把目标环境模拟得多逼真。不过话说回来，一个有经验的人类黑客大概率不会上当——冰箱里的牛奶都快馊了。但这不重要，我们搞AI蜜罐本来就不是为了骗人类。

不信？让ChatGPT自己说说看……

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcyiaQfyA4RcO6MHUeuShgccdewGPKIEF2cJCibbtO5Muf3KzwsT17hwSZq7iakcHanwNWhNFLnhbzE4EoGY02hUibR9gZr8ISIbick/640?wx_fmt=jpeg&from=appmsg)

## 速度换来暴露，暴露就是机会

安全圈里聊AI，十有八九都在恐吓：攻击更快了、门槛更低了、规模更大了。没错，速度和规模确实有代价。AI系统需要上下文、需要交互。自动化不是单向放大攻击者，它也约束并暴露了攻击者。暴露，就是防守方的机会——不仅仅是检测攻击，而是误导、研究、甚至操纵攻击者。

---

### 参考资料

[1] https://blog.talosintelligence.com/ai-powered-honeypots-turning-the-tables-on-malicious-ai-agents/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![]...