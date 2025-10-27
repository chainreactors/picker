---
title: Risc-v之Cache设计方案 - potatso
url: https://www.cnblogs.com/potatso/p/18986911
source: 博客园 - potatso
date: 2025-07-17
fetch_date: 2025-10-06T23:27:35.623891
---

# Risc-v之Cache设计方案 - potatso

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [Risc-v之Cache设计方案](https://www.cnblogs.com/potatso/p/18986911 "发布于 2025-07-16 09:59")

# cache设计

# 目的

为了解决访问DDR的慢速的问题。将常用指令，数据等缓存在CPU寄存器中，加快访问速度。

1. 解决操作系统内存按字节寻址与内存控制器按行寻址的矛盾
2. 解决操作系统按字节操作内存与内存控制器按行操作的矛盾

# 设计思路/原理

Cache可以根据数据的缓存分组方式，可以分为三大类。我们在设计Risc-v的L1 cache的时候，有必要简单了解一下高云提供的DDR3内存控制器的用法与SDRAM原理图。

## SDRAM寻址

在一根内存条中会包含多个SDRAM芯片，真正的内存数据会使用SDRAM芯片存储。如图黑色的部分

![image](https://img2024.cnblogs.com/blog/1916047/202507/1916047-20250716095256385-1977909804.png)

在内存寻址中使用rank信号线选择在哪个SDRAM芯片中寻址。每个SDRAM芯片中有着一模一样的架构。

在每个SDRAM芯片中，使用bank信号线选择具体分区。在每个bank中有着同样的行和列去选择。所以在硬件选址中是图中的寻址架构。

![image 1](https://img2024.cnblogs.com/blog/1916047/202507/1916047-20250716095328422-1310499833.png)

那我们是如何知道，每一行的数据宽度呢？可以查询DDR3芯片的datasheet，或者数DQ线。DQ的意义在于，DDR3芯片中，**每一行是多少字节**。根据上面这些基本知识，我们可以查看逻辑派-G1的原理图

![image 2](https://img2024.cnblogs.com/blog/1916047/202507/1916047-20250716095339295-1359979217.png)

在原理图中，一共有

* 16根DQ线，说明DDR3芯片的行宽度是16位，x16
* rank是片选信号，SDRAM芯片无能力做片选，忽略
* 3根bank信号线，BAR0-BAR2
* 行和列公用A0-A13
* CAS与RAS代表是行地址选通信号和列地址选通信号
* WE代表写使能

下面我们来计算一下该SDRAM的芯片大小

2^(bank宽度 + 行宽度 + 列宽度 + DQ总线宽度)，其中行宽度和列宽度请查阅SDRAM芯片手册。同理，我们也可以很容易设置高云提供的IP核

![image 3](https://img2024.cnblogs.com/blog/1916047/202507/1916047-20250716095350541-1236582492.png)

## DDR3内存控制器用法

在DDR3中我们发现，命令之间是互斥的，这里的命令包括但不限于自充电（刷新），读与写。并且寻址是按照行，而不是操作系统端的以字节。这是一个很大的区别.在我们的例子中，DDR3每行是两个字节。

在DDR3中，还有一个是时钟比例，你可以通俗理解为，在某一时钟边缘能对DDR3进行几次读写。在我们的例子中为1:2。所以，在每个时钟边沿，最少要对DDR3数据操作字节数

`APP_DATA_WIDTH = 2 * nCK_PER_CLK * DQ_WIDTH` 例如在我们的DDR3中，一次最少操作64位，8字节数据。

这揭示了我们为什么需要L1 cache。在内存控制器的读写中，一次最少读写8字节数据，在高端cpu中这个数字只增不减。而在操作系统端，内存寻址只操作4字节数据。这其中就会有严重不匹配，cpu也不能因为这个理由频繁向内存控制器发出请求，如果cpu向内存请求的地址处在行中末尾，内存控制器需要复杂的运算才能完成任务，这样即增加了内存请求次数，也增加了FPGA实现的复杂度。所以增加L1 cache，将一次性读取的内容缓存，以供后续使用，被称为Cache line。

从DDR3控制器用法中，我们也可以得到**内存对齐的重要性**。让我们的内存访问尽量在一个缓存行中，否则就要发起两次内存请求，麻烦。

内存控制器的用法如下流程。内存控制器最大的意义是，为我们屏蔽了DDR3复杂的时序操作等需求，对开发者只暴露最简单的读写操作。

flowchart TD
A[上电/复位] --> B[等待DDR3初始化完成]
B --> C{控制器是否准备好接收命令}
C -- 是 --> H{读或写?}
C -- 否 --> P
H -- 读 --> I[READ（发出读命令）]
I --> K[数据输出]
K --> P
H -- 写 --> M{控制器当前是否允许写}
M -- 是 --> N[数据写入]
N --> P[结束]

示例代码如下，简化不必要的部分

```
 if (BURST_MODE == "4") begin : app_burst_4
      // 每次地址往前+4，
      // DDR3内存访问说明:
      // 总容量=rank数×bank数×row数×col数×数据宽度
      // DDR3数据总线宽度为16位（2字节）
      // 由于DDR3为双倍数据速率（DDR），每个时钟周期可传输2个数据
      // 控制器突发长度通常为4或8（BL4/BL8），常用为BL8
      // 若BL8，则一次突发传输16字节（16位 × 8 = 128位 = 16字节）
      // 实际内存控制器每个操作周期可访问64位（8字节）数据，地址步进为8
      // 列地址（col）作为突发起始列地址，一次操作可访问连续多列（如4列）
      // 因此，col寻址时，一次写入4列，带宽和

			// 步进大小，DDR3 配置下，一次可以读写4行，每行2字节，一共8字节
      assign addr_step = 4'd4;

      always @(posedge clk or posedge rst) begin
				// 初始化完成，并且当前内存控制器可以接收指令和可以写
        if (app_rdy && app_wdf_rdy && init_calib_complete && cnt == 8'd10) begin
          // 向内存控制器发出命令与地址信号的使能
          app_en       <= 1'b1;
          // 命令
          app_cmd      <= 3'b000;  //write
          // 写使能
          app_wdf_wren <= 1'b1;
          // 写结束，我们的写入只跨越一个时钟周期，所以写完停止即可
          app_wdf_end  <= 1'b1;
          // 写掩码，0写1不写
          app_wdf_mask <= {APP_MASK_WIDTH{1'b0}};
          // 固定设置0
          app_burst    <= 1'b0;
          // 内存寻址
          app_addr     <= reg_addr;
          // 写入内容
          app_wdf_data <= mem_data[mem_index];
        end else if (app_rdy && init_calib_complete && cnt == 8'd70) begin
          app_en       <= 1'b1;
          app_cmd      <= 3'b001;  //read
          app_wdf_wren <= 1'b0;
          app_wdf_end  <= 1'b0;
          app_wdf_mask <= {APP_MASK_WIDTH{1'b0}};
          app_burst    <= 1'b0;
          app_addr     <= reg_addr;
          app_wdf_data <= {APP_DATA_WIDTH{1'b0}};
        end
      end
```

## 时序约束文件的编写

我们都知道电子虽然传输速度很快，但是也是需要时间的，类似于MINECRAFT中的红石系统延迟。时序约束文件的主要作用是，告诉FPGA在优化布线中，一个语句块的信号传输的时间一定要小于我们规定的时间，防止出现一个信号跨越多个传输周期的情况。如果违反时序约束，就会出现亚稳态传输，造成FPGA的结果不确定。知道了原理，下面简单介绍一下时序文件的写法。

* 用 `get_ports {xxx}` 选中的端口，以及**和这个端口相关联的时序路径**（比如从这个端口到内部寄存器，或者从内部寄存器到这个端口），**综合和布局布线工具会根据你设定的时序约束来分析和优化布线**，以满足你的时序要求（比如最大延迟、保持时间等）。

### 常见命令说明

* **create\_clock**

  创建一个时钟约束，指定时钟周期、占空比、作用对象等。

  `create_clock -name clk -period 20 -waveform {0 10} [get_ports {clk}]`

  上例表示在输入端口 `clk` 上创建一个 20ns 周期、50MHZ的时钟，下降沿是0ns，上升沿在10ns处。
* **set\_input\_delay / set\_output\_delay**

  指定端口的输入/输出延迟（如外部设备到 FPGA 的采样延迟），通常配合时钟使用。

  ```
  set_input_delay 3 -clock [get_clocks clk] [get_ports {data_in}]
  set_output_delay 5 -clock [get_clocks clk] [get_ports {data_out}]
  ```
* **set\_clock\_groups**

  设置不同时钟域为“互斥时钟组”，工具不会分析它们之间的时序路径。

  `set_clock_groups -exclusive -group [get_clocks {clk}] -group [get_clocks {memory_clk}]`

## Cache 设计

### **直接相联映射**

将内存地址划分为Tag、Index和Offset三部分，查找时先用Index快速定位缓存组，再用Tag在组内少量候选项中匹配，有效降低查找硬件的复杂度和延迟。

![image 4](https://img2024.cnblogs.com/blog/1916047/202507/1916047-20250716095412937-757976380.png)

查找的流程如下：

1. 根据行地址查找Cache中对应的行
2. 根据区地址（标记位TAG）以及一些标志位（有效位 ）来判断是否与主存中所要查找的区对应
3. 如果TAG一致，则输出该行的数据内容，同时根据字地址来选择最终字的输出
4. 如果TAG不一致，则从主存中载入到相应地址的内容到Cache中，再由Cache传输给CPU

![image-20200822111450390](https://floral.github.io/2020/08/22/Cache%E6%98%A0%E5%B0%84%E6%9C%BA%E5%88%B6%E4%B8%8E%E9%80%BB%E8%BE%91%E5%AE%9E%E7%8E%B0/image-20200822111450390.png)

这种方法的命中率较低，因为主存中的块只能对应一个Cache块。一个块可能刚进入Cache，就被另一个块给覆盖了。

不过其优点是硬件逻辑简单，成本较低。如果硬要解决，可以增加多个TAG区即可。

### **全相联映射**

全相联就是主存中的任意一块（行）可以放在Cache中的任意一块（行）中，没有分区的概念。于是贮存地址就只分为两部分：**主存块地址（标记部分）、字地址**。核心就是上一种方案提及的Hash算法，将Cache index均匀地落在set中。

![image-20200822185746130](https://floral.github.io/2020/08/22/Cache%E6%98%A0%E5%B0%84%E6%9C%BA%E5%88%B6%E4%B8%8E%E9%80%BB%E8%BE%91%E5%AE%9E%E7%8E%B0/image-20200822185746130.png)

由于主存中一个块对应的Cache块地址不确定，所以需要其他的结构来辅助确定，即查找表。查找表的行数与Cache的行数相同，每一行存放着一个主存块地址，一个对应的Cache块地址，以及一些标志位。值得注意的是，查找表（CAM）与Cache是分开存放的，而直接相联中的区地址、标记位等与Cache数据则是一起存放的。

查找流程如下：

1. 根据主存块地址在CAM中并行查找Cache中是否存在该块地址
2. 若存在，则根据该行对应的Cache块地址直接访问Cache中的相应行，然后根据字地址选择输出的字
3. 若不存在，则从RAM中载入相应地址的块到一个空的Cache行中，然后输出

![image-20200822203942775](https://floral.github.io/2020/08/22/Cache%E6%98%A0%E5%B0%84%E6%9C%BA%E5%88%B6%E4%B8%8E%E9%80%BB%E8%BE%91%E5%AE%9E%E7%8E%B0/image-20200822203942775.png)

优点命中率会显著提高，缺点硬件开销大（Hash算法）

### **组相联映射**

组相联映射结合了直接相联和全相联的特点，首先将Cache分为n组，一组中有k行。主存中也是按照每n行进行分割（类比直接相联的分区），每一行只能进入到相应的Cache组中，但是可以是组中的任意一行（类比全相联）。

> 每一组中的行数即路数，有k行则被称为k路组相联

于是主存的地址就被分为3个部分：**标记字段（区地址）、组地址、字地址。**

Cache中一行的组成与直接相联映射类似。

![image-20200822210623668](https://floral.github.io/2020/08/22/Cache%E6%98%A0%E5%B0%84%E6%9C%BA%E...