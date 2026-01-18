---
title: 【APP测试】frida的python库使用
url: https://mp.weixin.qq.com/s/kImc-0C5kGDMe08oyQdnRQ
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:35:43.586334
---

# 【APP测试】frida的python库使用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyVCFs3agXpeWH8kPqCQK5DRaNssmcqoYCpzIuroiankVmrgwYFzPpSXA/0?wx_fmt=jpeg)

# 【APP测试】frida的python库使用

原创

d0n9x1e
d0n9x1e

蝉SEC

![]()

在小说阅读器中沉浸阅读

# 引子

## 1. 为什么需要使用 Frida 的 Python 库

### a) 自动化处理与扩展性

* **手工调试的局限性**

  ：之前介绍的 Frida 主要用于手工调试阶段，适合在交互式环境中进行动态分析。然而，对于复杂的逆向工程任务，手工调试效率较低，且难以实现自动化。
* **Python 的优势**

  ：Python 是一种强大的脚本语言，具有丰富的库支持（如网络请求、数据处理、文件操作等）。通过使用 Frida 的 Python 库，可以将 Frida 的动态分析能力与 Python 的自动化脚本能力结合起来，实现更高效的逆向工程和自动化测试。

### b) 算法转发与 RPC

* **算法转发和 RPC 的便捷性**

  ：Frida 提供了强大的 RPC 功能，允许在运行时动态调用和修改目标程序的行为。通过 Python，可以更方便地实现算法转发（如加解密算法的转发）和 RPC 功能，从而在逆向工程中实现更复杂的逻辑。
* **示例**

  ：假设需要在运行时动态修改加解密算法，可以通过 Python 脚本调用 Frida 的 RPC 功能，将算法转发到本地 Python 环境中进行处理，处理完成后将结果返回给目标程序。

### c) 实时数据交互

* **Frida 与 Python 的协同工作**

  ：Frida 可以实时与 Python 进行数据交互。在 Frida 脚本中，可以将数据发送到 Python 环境中进行处理，处理完成后将结果返回给 Frida 脚本，Frida 再继续执行后续代码。
* **Python 的强大库支持**

  ：Python 提供了丰富的库，如 `requests`（网络请求）、`numpy`（数值计算）、`pandas`（数据分析）等，这些库可以大大简化代码编写，提高开发效率。

## 2. 使用 Frida 的 Python 库时的局限性

### a) 缺乏即时修改功能

* **问题**

  ：当 Frida 脚本（`jsCode`）有修改时，必须重新运行 Python 脚本才能生效。Frida 的 Python 库不支持即时修改功能，这意味着每次修改 Frida 脚本后都需要重新加载整个脚本。
* **解决方案**

  ：

+ **手动重新加载**

  ：每次修改 Frida 脚本后，重新运行 Python 脚本。
+ **动态加载机制**

  ：可以在 Python 脚本中实现一个简单的动态加载机制，通过文件监听等方式检测 Frida 脚本的修改，并重新加载脚本。

### 示例：动态加载机制

```
import frida, sys, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ScriptHandler(FileSystemEventHandler):
    def __init__(self, script_path, process):
        self.script_path = script_path
        self.process = process
        self.load_script()

    def load_script(self):
        with open(self.script_path, 'r') as f:
            jsCode = f.read()
        self.script = self.process.create_script(jsCode)
        self.script.load()
        print("Script loaded from:", self.script_path)

    def on_modified(self, event):
        if event.src_path == self.script_path:
            print("Script modified, reloading...")
            self.script.unload()
            self.load_script()

if __name__ == "__main__":
    device = frida.get_usb_device()
    process = device.attach('com.dodonew.online')

    script_path = 'path/to/your/frida_script.js'
    event_handler = ScriptHandler(script_path, process)
    observer = Observer()
    observer.schedule(event_handler, path='.', patterns=[script_path])
    observer.start()

    try:
        sys.stdin.read()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

### 代码说明：

1. `FileSystemEventHandler`

   ：监听文件修改事件。
2. `on_modified`

   ：当 Frida 脚本文件被修改时，重新加载脚本。
3. `Observer`

   ：启动文件监听器，实时监控脚本文件的修改。

通过这种方式，可以在修改 Frida 脚本后自动重新加载，而无需手动重新运行 Python 脚本。

## 总结

* **Frida 的 Python 库**

  ：提供了强大的自动化能力，结合 Python 的丰富库支持，可以实现复杂的逆向工程任务。
* **包名附加**

  ：通过 Python 脚本可以方便地附加到目标进程并执行 Frida 脚本。
* **动态加载机制**

  ：虽然 Frida 的 Python 库不支持即时修改功能，但可以通过文件监听等方式实现动态加载，提高开发效率。

# 基础使用

## 1. 包名附加

使用 Frida 的 Python 库可以方便地附加到目标进程并执行 Frida 脚本。以下是一个简单的示例代码：

```
import frida, sys

# 定义 Frida 脚本代码
jsCode = """
Java.perform(function () {
    var Activity = Java.use('com.example.MyActivity');
    Activity.onResume.implementation = function () {
        console.log('onResume called');
        this.onResume();
    };
});
"""

# 附加到目标进程
process = frida.get_usb_device().attach('com.dodonew.online')

# 创建并加载脚本
script = process.create_script(jsCode)
script.load()

# 阻塞主线程，防止脚本退出
sys.stdin.read()
```

### 代码说明：

1. `frida.get_usb_device()`

   ：连接到 USB 设备（适用于 Android 设备）。
2. `attach('com.dodonew.online')`

   ：附加到目标进程（通过包名指定）。
3. `create_script(jsCode)`

   ：创建一个 Frida 脚本。
4. `script.load()`

   ：加载并执行 Frida 脚本。
5. `sys.stdin.read()`

   ：阻塞主线程，防止脚本退出。

## 2. 通过 PID 附加到进程

### 场景

当已知目标进程的 PID 时，可以直接通过 PID 附加到该进程。

### 示例代码

```
import frida, sys

# 定义 Frida 脚本代码
jsCode = """
Java.perform(function () {
    var Activity = Java.use('com.example.MyActivity');
    Activity.onResume.implementation = function () {
        console.log('onResume called');
        this.onResume();
    };
});
"""

# 通过 PID 附加到进程
process = frida.get_usb_device().attach(9999)  # 替换为实际的 PID
script = process.create_script(jsCode)
script.load()

# 阻塞主线程，防止脚本退出
sys.stdin.read()
```

### 注意事项

* 确保 PID 是正确的，并且目标进程正在运行。
* 如果目标设备是远程设备或通过网络连接，需要使用 `frida.get_device_manager().add_remote_device()` 方法获取设备对象。

---

## 3. 使用 `spawn` 方式启动进程

### 场景

`spawn` 方式可以启动一个新进程，并在启动时挂起，以便在进程运行之前加载 Frida 脚本。

### 示例代码

```
import frida, sys

# 定义 Frida 脚本代码
jsCode = """
Java.perform(function () {
    var Activity = Java.use('com.example.MyActivity');
    Activity.onResume.implementation = function () {
        console.log('onResume called');
        this.onResume();
    };
});
"""

# 获取设备并以挂起方式启动目标应用
device = frida.get_usb_device()
pid = device.spawn(["com.dodonew.online"])  # 替换为目标应用的包名
process = device.attach(pid)

# 加载 Frida 脚本
script = process.create_script(jsCode)
script.load()

# 恢复进程运行
device.resume(pid)

# 阻塞主线程，防止脚本退出
sys.stdin.read()
```

### 注意事项

* 使用 `spawn` 启动的进程会挂起，直到调用 `device.resume(pid)` 后才会继续运行。
* 确保目标应用的包名正确。

---

## 4. 连接非标准端口

### 场景

当目标设备运行在非标准端口（如自定义的 Frida 服务器端口）时，需要指定设备的 IP 地址和端口。

### 示例代码

```
import frida, sys

# 定义 Frida 脚本代码
jsCode = """
Java.perform(function () {
    var Activity = Java.use('com.example.MyActivity');
    Activity.onResume.implementation = function () {
        console.log('onResume called');
        this.onResume();
    };
});
"""

# 连接到运行在非标准端口的设备
process = frida.get_device_manager().add_remote_device('192.168.3.68:8888').attach('com.dodonew.online')
script = process.create_script(jsCode)
script.load()

# 阻塞主线程，防止脚本退出
sys.stdin.read()
```

### 注意事项

* 确保目标设备的 IP 地址和端口正确。
* 如果目标设备是本地设备，可以使用 `localhost` 或 `127.0.0.1`。

---

## 6. 连接多个设备

### 场景

在某些情况下，可能需要同时连接多个设备并注入相同的 Frida 脚本。

### 示例代码

```
import frida, sys

# 定义 Frida 脚本代码
jsCode = """
Java.perform(function () {
    var Activity = Java.use('com.example.MyActivity');
    Activity.onResume.implementation = function () {
        console.log('onResume called');
        this.onResume();
    };
});
"""

# 连接到第一个设备
process = frida.get_device_manager().add_remote_device('192.168.3.68:8888').attach('com.dodonew.online')
script = process.create_script(jsCode)
script.load()

# 连接到第二个设备
# process1 = frida.get_device_manager().add_remote_device('192.168.3.69:8888').attach('com.dodonew.online')
# script1 = process1.create_script(jsCode)
# script1.load()

# 阻塞主线程，防止脚本退出
sys.stdin.read()
```

### 注意事项

* 确保每个设备的 IP 地址和端口正确。
* 如果需要同时管理多个设备，可以通过线程或异步方式来实现。

---

## 总结

1. **通过 PID 附加**

   ：适用于已知目标进程 PID 的场景。
2. **使用**`spawn`**方式启动**

   ：适用于需要在进程启动时注入脚本的场景。
3. **连接非标准端口**

   ：适用于目标设备运行在自定义端口的场景。
4. **连接多个设备**

   ：适用于需要同时操作多个设备的场景。

通过这些方法，可以灵活地使用 Frida 的 Python 库进行动态分析和逆向工程。

# frida与Python的交互

Frida 提供了强大的机制，允许在 JavaScript 脚本和 Python 脚本之间进行实时交互。这种交互通过消息传递机制实现，使得 Frida 脚本可以将数据发送到 Python 环境中，并接收 Python 环境返回的数据。以下是关于 Frida 与 Python 交互的详细说明。

---

## 1. `send` 的使用

### 场景

在 Frida 的 JavaScript 脚本中，`send` 函数用于将消息发送到 Python 环境。Python 环境可以通过监听 `message` 事件来接收这些消息。

### 示例代码

#### JavaScript 脚本

```
Java.perform(function () {
    var Activity = Java.use('com.example.MyActivity');
    Activity.onResume.implementation = function () {
        send("onResume called");  // 发送消息到 Python 环境
        this.onResume();
    };
});
```

#### Python 脚本

```
import frida, sys

def message(message, data):
    if message["type"] == 'send':
        print(u"[*] {0}".format(message['payload']))  # 打印发送的消息
    else:
        print(message)

jsCode = """
Java.perform(function () {
    var Activity = Java.use('com.example.MyActivity');
    Activity.onResume.implementation = function () {
        send("onResume called");
        this.onResume();
    };
});
"""

process = frida.get_usb_device().attach('com.example.app')
script = process.create_script(jsCode)
script.on('message', message)  # 注册消息监听器
script.load()
sys.stdin.read()
```

### 说明

* `send`**函数**

  ：在 Frida 的 JavaScript 脚本中，`send` 函数用于发送消息到 Python 环境。消息内容可以是字符串或对象。
* `messag...