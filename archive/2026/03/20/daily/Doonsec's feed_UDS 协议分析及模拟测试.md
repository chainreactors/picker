---
title: UDS 协议分析及模拟测试
url: https://mp.weixin.qq.com/s/kiNf37fF_fk4WfaqRR_5Kg
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:01:13.034590
---

# UDS 协议分析及模拟测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/94kIPh1QgiaAXLQWCuUibg0hsmrgWmCgFZGxocGicGCwiann3xNUicxWS8pdFL32Gv8GCLELPGLLiaX1yoG04ZgvTEXDRf8PibGyfFeDVT6AAenpE0/0?wx_fmt=jpeg)

# UDS 协议分析及模拟测试

原创

朝阳
朝阳

Sec朝阳

![]()

在小说阅读器中沉浸阅读

### 前言

车辆诊断目的是为了快速判断车辆或某个控制器的故障及故障原因，以此进行维修。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDWeiabyzWvTT5s1Pc6g5RJf52xejFBALPveTPNWrpBMZv40ZHru8m9H3opM44ffykgJD0n4bhvJRZGPN4wJPB2icdrU9gXG35rE/640?wx_fmt=png&from=appmsg)

常见的诊断协议有 ISO 14230，ISO 15031，ISO 15765，我们熟悉的 ISO 14229 就是 UDS 协议，在协议里定义了诊断请求，诊断响应的报文格式，以及 ECU 怎样处理诊断请求报文，以及诊断服务的应用。

### 一、UDS 诊断方法

大多数 ECU 都装有自诊系统 (OBD),能够及时发现传感器、执行器、ECU 和通信网络产生的电力故障。

当 OBD 检测到故障时，会生成相应故障码信息，并点亮故障灯。此外，把诊断仪插入 OBD 接口即可以和 OBD 系统进行通信，从而获取故障码和相关信号流等数据，实现快速定位故障源和故障类型。

表 1 UDS 诊断服务类型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDoicZ1hKTribKvOyiaYC3oqdHS8kibm1zichuUsph53mltNB32vciaQQ0wI2TmyuD7HRsbOGibSSXSIQcVsuEU5VicbrvTUtnqvI4Tvib4/640?wx_fmt=png&from=appmsg)

这里先把我们称为客户端，OBD 称为服务端。

也就是我们使用诊断仪向 ECU 发送请求信息，等待 ECU 回复同意或拒绝。

这两种反馈称为正响应和负响应。

UDS 服务请求消息和服务响应消息都以报文的形式呈现。

UDS 明确定义了服务请求报文的基本格式为“SID+其他参数”，正响应报文的基本格式为“[SID+0x40]+其他参数“，负响应报文的格式为"0x7F+其他参数"。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaBxyEOnqzvG2f21GaXJNAp5Sfh1UcptEvIUeusUqiaIicT23BCyUS5Bwp9GPx8N1OsCOZ02YbVTicz96KhwqMqeibw7FKScLbSHo3I/640?wx_fmt=png&from=appmsg)

上图我们得知，我们使用诊断仪向 ECU 发送请求报文”0x22 0x01 0x0a“,该报文中的第一个数据”0x22“表示当前请求的服务为 SID 为 22 的”通过 ID 读数据“服务。该报文中的”0x01 0x0a“表示要读的数据的 ID 为”010a“,其含义为油门开度，由汽车生产商指定。

如果 OBD 给出了正响应，则发送报文”0x62 0x01 0x0a 0x00 0x23“,该报文的第一个数据值为”0x62“是 0x22 加上 0x40 的结果，后面第二、三个数据为请求报文中指定的 ID 值”0x01 0x0a“,第四、五个数据”0x00 0x23“,为当前油门开度值”0x23(十进制为35)“，表示当前发动机油门开度为 35%。

如果 OBD 给出了负响应，则发送报文”0x7f 0x22 0x11“,该报文第一个数据值为”0x7f“，表示拒绝服务，第二个数据为被拒绝的服务的 SID 值”0x22“，第三个数据为被拒绝原因，该值由 UDS 定义，”0x11“表示当前服务不支持。

UDS 协议定义了所有服务的报文格式和数据含义(见ISO 14229-1),诊断仪和 OBD 都必须遵循该协议，才能正确完成各种诊断服务。参照 ISO 网络通信体系，该部分协议称 UDS 应用层协议。

### 二、UDS 传输方法

诊断仪和 OBD 生成的 UDS 报文需通过通信网络进行传输。但汽车 ECU 普遍使用 CAN 总线进行数据通信，因此 UDS 报文必须加载到 CAN 帧中才能发送。

但是每个 CAN 帧的最大传输数据量只有 8 个字节，而 UDS 报文的数据量是根据服务内容进行变化的。

最小的 UDS 报文有 2 个字节，大的 UDS 报文往往超过8字节。

所以超过 8 字节的 UDS 报文需多个 CAN 帧才能完成传输。为了保证报文传输的有效性和可靠性，需定义 UDS 报文在 CAN 总线上的传输协议(ISO-15765-2),其一般称为 UDS 的网络层或传输层协议。

UDS 定义了四种类型的 CAN 帧来传输 UDS 报文，分别单帧(Single Frame,SF)、首帧(Firsst Frame,FF)、连续帧(Consecutive Frame,CF)和流控帧(Flow Control,FC)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDcbiaG9oSDX6R3WcAibWKPticA0wm6xuDLibz1htYMFpHEdPFVBqL3D7ASQIR6qsTZZ7Tpyia2Qxnr5ImDwQWXVlfkMSwNgMUic30Do/640?wx_fmt=png&from=appmsg)

每种 CAN 帧都占用第一个字节的高 4 位来存放帧类型数据。

单帧的第一个字节低 4 位存放了该帧传输的报文数据量，剩余字节存放 UDS 报文数据，有空余则填充为 0 作为对齐。

以图 2 中传输的请求报文"0x22 0x01 0x0a"和正响应报文"0x62 0x01 0xa 0x0 0x23"为例，其单帧数据区的内容如图 3 所示：

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaBt1Fa85qdhs8xGZUiceruPRcPTFMN9HCMVEjicSHeak4cRL5IOqPoRp57KmUCibqhB9MUfIEfYNyhKBkoricJzNa5Ric8aGC0p728k/640?wx_fmt=png&from=appmsg)

请求响应报文单帧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDOOEvXDMiazpOYiaJYEqd6COYjKEvYAkxRrbuZbsdQFYZfz90psRXibGc8sQiafd1bGknEXqLeAUicL7Wa9R7bhVBjqBnYU6fekyY8/640?wx_fmt=png&from=appmsg)

正响应报文单帧。

能看到，单帧最多可传 7 个字节 UDS 报文，当要发送的报文的数据量大于7个字节时，就需要使用首帧、连续帧和流控帧了，机制如图 4 所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaAURYzFBXDHjSBibRqEpqagibDZ7bhanNlmvPHYeBicAAZiboEk4g41WcppdsPnKTHKUq97l5CJ62rb5QPJlKnYX3UWkZ13kFjUzLg/640?wx_fmt=png&from=appmsg)

这里就是发送端将 UDS 报文写入首帧，首帧第一个字节低 4 位和第二个字节带着传输 UDS 报文总量，其余放数据。

接收端收到首端后回复流控帧，流控帧为了控制后续发送报文的速率。

发送端收到流控帧后把 UDS 报文其余数据填入连续帧，并标记顺序发出，以此来判断 UDS报文是否传输完。

流控帧的第一个字节的低 4 位存放 FlowStatus(FS)值。该值为 0 表示可以继续发送后续连续帧；如为 1 表示暂停发送后续连续帧；如为 2 表示接收端已经溢出。

流控帧的第二个字节存放 BlockSize(BS值)，该值如果为 0 表示接收端后续将不会再发送流控帧，发送端直接发送余下的所有连续帧；如果为 01-0xff 之间的某个值，表示发送端在连续发送了该值数量的连续帧个数后，需要等待接收方再次发送流控帧。

流控帧的第三个字节存放 Stmin 值，该值为两个连续帧传输的时间间隔，单位 ms。流控帧的剩余字节存放填充数据。

连续帧的第一个字节低 4 位存放连续帧的序号 SN 值。第一个连续帧的序号为 1，后续连续帧序号依次加 1，知道 0xf 后，后续连续帧的 SN 值从 0 开始依次加 1。

#### 1、传输案例

以传输 17 位 VIN 码为例：

(1)、诊断仪向 ECU 发出”0x22 0xf1 0x90“ 的 UDS 报文，请求读取车辆 VIN 码；

(2)、ECU 收到请求后回复正响应报文”0x62 0xf1 0x90 0x57 0x30 0x4c 0x30 0x30 0x30 0x30 0x34 0x33 0x4d 0x42 0x35 0x34 0x31 0x33 0x32 0x36“，共 20 个字节的数据量。

因此 ECU 先发出首帧，其数据区内容为图 5 所示：

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaCpDXjam64M0XTicuvayqxqhw6wWnJniajnRZ745QINZcMDgY9vicUcE7XiariaXKsgbsdCth3PpjQgwQE5ns7JxHoJhlz9BKH8WY00/640?wx_fmt=png&from=appmsg)

(3)、诊断仪收到首帧后，向 ECU 回复流控帧，其数据区内容为如图 6 所示：

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDWUudZdgbzYg45tRYxrGVncfq7ZCibbVjGVAVCYxrQE1iaV4BOKiboc2olz9bicDLqOorQbrSrs7BoYq79NwtvdAOGntkJTmcsPZU/640?wx_fmt=png&from=appmsg)

(4)、ECU 收到流控帧后，会依次发送剩余 2 个连续帧，其数据区内容为如图 7 所示：![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDWbhJXL91iaVkLuDb4fm9n6YF4JuZiceQkeric12R0rMy0z0JzWKZPe9PIPuBOJjsb916w9trLOP5WBib6qDXLcsNNjMSzpBvL7d8/640?wx_fmt=png&from=appmsg)

### 三、UDS 时间管理

UDS 在传输的过程中，可能会遇到因网络故障或节点故障导致的通信延迟或终端的情况，因此 UDS 定义了通信时间管理基址来保证其工作的时效性，并基于设定的时间参数实现。

(1)、UDS 应用层时间参数

P2 Client：诊断仪成功发送请求报文后，接收到 ECU 响应报文的时间间隔

P2 Server：ECU 接收到诊断报文请求后，发出回复想要报文的时间间隔

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaBbfB7AYYibSM9l9dWaDqUbHLT5a4OT8emicHiceMkSPdiaOibiawumZ13qdjs9c29wAAASYxWQyW1Ns9unibC2ic5nAiasqnlFAx4riaFoU/640?wx_fmt=png&from=appmsg)

(2)、UDS 网络层时间参数

N\_As：发送端发送一帧所需的时间

N\_Ar：接收端发送一帧所需的时间

N\_Bs：发送端等待成功接收流控帧的时间间隔，超时则发送端接收流控帧失败

N\_Br：接收端等待发送流控帧的时间间隔，超时则接收端流控帧发送失败

N\_Cs：发送端等待发送一连续帧的时间间隔，Stmin

N\_Cr：接收端等待成功接收一连续帧的时间间隔，超时则接收失败

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDyXjZsIzTfwUgm0ULDIbiaxAqgWxia0C9B1C7LB9ntJraFr9pJwZnadvWq7qqRqExTxzsLLfYzZnaCDT9lIBKpzTxR0Kc8jFI0c/640?wx_fmt=png&from=appmsg)

UDS 协议明确给出了各个时间参数的取值范围，具体取值可以根据网络环境、节点速率和诊断应用需求进行调整。

### 四、仿真实验

首先我们先模拟搭建一个 ECU。

```
import can
import time

# 1. 初始化虚拟总线，起名叫vcan0 'vcan0'
bus = can.interface.Bus('vcan0', bustype='socketcan')
print("  [ECU] 模拟器已上线，正在监控总线...")

while True:
    # 2. 持续接收总线上的报文
    msg = bus.recv()
    if msg is None: continue

    data = msg.data
    # 这里的 data 是一个字节数组，比如 [0x02, 0x10, 0x01, ...]

    # --- 逻辑 A：处理单帧 (Single Frame) ---
    # UDS规定：第一个字节的高4位是 0，代表单帧
    if (data[0] & 0xF0) == 0x00:
        length = data[0] & 0x0F
        sid = data[1]
        print(f"📩 [ECU] 收到单帧请求! 长度:{length}, 服务ID:{hex(sid)}")

        # 如果是 10 01 (进入默认会话)
        if sid == 0x10 and data[2] == 0x01:
            # 回复 Positive Response: [长度, SID+0x40, 子功能, ...]
            # 0x10 + 0x40 = 0x50
            resp = can.Message(arbitration_id=0x7E8, data=[0x02, 0x50, 0x01, 0,0,0,0,0], is_extended_id=False)
            bus.send(resp)
            print("✅ [ECU] 已回复: 50 01 (OK)")

    # --- 逻辑 B：处理首帧 (First Frame) - 准备多帧传输 ---
    # UDS规定：第一个字节高4位是 1，代表后面还有很多货
    elif (data[0] & 0xF0) == 0x10:
        total_len = ((data[0] & 0x0F) << 8) | data[1]
        print(f"📦 [ECU] 警告！收到首帧。对方要传 {total_len} 字节。发送流控帧(FC)...")

        # 按照 CSDN 文章说的，我们要回 30 (流控帧)
        # 30 00 00: 3代表流控，后面00代表不限速
        fc = can.Message(arbitration_id=0x7E8, data=[0x30, 0x00, 0x00, 0,0,0,0,0], is_extended_id=False)
        bus.send(fc)

    # --- 逻辑 C：接收连续帧 (Consecutive Frame) ---
    # 第一个字节高4位是 2
    elif (data[0] & 0xF0) == 0x20:
        sn = data[0] & 0x0F # 序号 1, 2, 3...
        print(f"🧩 [ECU] 收到连续帧 SN:{sn} | 内容:{list(data[1:])}")
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaAB2HdrIn1Np6J57xVeUETnKcDib7iaNicjZvIqA81XDUaPOvo6iapEXMTictn7dSjFhZRliaZNsN1ZxgScJ91pziczxMw59mHs4WSDibc/640?wx_fmt=png&from=appmsg)

我们先模拟一个 ECU，然后我们向其发送报文。

##### 单帧

```
import can

# 连接到同一条总线 vcan0
# 忽略那个警告，咱们按新版本写法：interface='virtual'
bus = can.interface.Bus('vcan0', interface='socketcan')

print("🚀 [Tester] 已就绪，发送单帧指令 (10 01)...")

# 构造 UDS 单帧：[长度02, 服务10, 子功能01, 后面补0]
msg = can.Message(arbitration_id=0x7E0,
                  data=[0x02, 0x10, 0x01, 0, 0, 0, 0, 0],
                  is_extended_id=False)

bus.send(msg)

# 等待 ECU 回复
reply = bus.recv(timeout=1.0)
if reply:
    print(f" [Tester] 抓到响应报文: {list(reply.data)}")
else:
    print(" [Tester] 没收到回复，检查 ECU 脚本是否在运行。")
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBDXjOyibvUBbnkWVscGtAKggHe4zTcSoFZoR5iaqia1dMwteg4RzwtStSQCpWEmxsZGB2iaPertPBe8xPDiczDJWBQt3he49xmHp5I/640?wx_fmt=png&from=appmsg)

此处为单帧测试结果，Linux 的 CAN 通信用的是 socketcan。...