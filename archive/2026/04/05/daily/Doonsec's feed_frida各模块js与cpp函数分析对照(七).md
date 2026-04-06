---
title: frida各模块js与cpp函数分析对照(七)
url: https://mp.weixin.qq.com/s/TuC7SFD3j4UdR1hEQMp6yQ
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:42:19.781367
---

# frida各模块js与cpp函数分析对照(七)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnuOBeLgIFLDOiawUCnfnormWw84gHdk3iaO7aXGzfUIEzvRZrrjxBIzLxTe3wGa3SDVZlJwlh2ftF7NRf0D3HeDAklx7TBjwONXA/0?wx_fmt=jpeg)

# frida各模块js与cpp函数分析对照(七)

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

* # 官网：http://securitytech.cc

  ![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuSkNPRkjuaPf2NThmBooRdeZ52XpiazERTicv0JAic4CZiblUdhmSExjRiaWMny6SgstgHB2B2pibXcLCyH6ygjrnuQqzRrzuZyrtT0/640?wx_fmt=png&from=appmsg)

  # CPU和Instruction模块 JavaScript与底层C++函数映射关系分析

  ## 文档概述

  本文档详细分析Frida中CPU指令相关模块（包括Instruction、X86Writer、Arm64Writer等）的JavaScript API与其底层C/C++实现之间的映射关系，涵盖完整的五层架构模型分析。

  ## 五层架构模型分析

  ### 1. 接口定义层 (JavaScript API Layer)

  #### CPU模块主要接口：

  #### Instruction模块主要接口：

  #### 指令写入器模块：

  主要接口包括：

  #### 枚举类型：

  ### 2. 基础结构层 (GumJS Binding Layer)

  在 `subprojects/frida-gum/bindings/gumjs`目录中，CPU和Instruction模块的绑定实现在相关文件中。

  #### 关键数据结构

  ```

  ```

  ### 3. 具体实现层 (Platform-specific Implementation)

  #### Instruction实现 ( `guminstruction.c`)

  关键函数：

  #### 指令写入器实现

  关键函数：

  #### 指令重定位器实现

  关键函数：

  ### 4. 工厂模式层 (Backend Factory)

  #### 指令解析器工厂

  ```

  ```

  #### 指令写入器工厂

  ```

  ```

  #### 指令重定位器工厂

  ```

  ```

  ### 5. 应用集成层 (Integration with Frida Core)

  CPU和Instruction模块通过frida-core与上层应用集成，为Interceptor、Stalker等高级功能提供底层支持，并与代码生成和动态插桩深度集成。

  ## 详细函数映射关系表

  ### Instruction映射表

  | JavaScript Function | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `Instruction.parse()` | `gum_instruction_parse()` | `guminstruction.c` | 解析指定地址的指令 |
  | `instruction.address` | `gum_instruction_get_address()` | `guminstruction.c` | 获取指令地址 |
  | `instruction.mnemonic` | `gum_instruction_get_mnemonic()` | `guminstruction.c` | 获取助记符 |
  | `instruction.opStr` | `gum_instruction_get_op_str()` | `guminstruction.c` | 获取操作数字符串 |

  ### X86Writer映射表

  | JavaScript Constructor/Method | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `newX86Writer()` | `gum_x86_writer_new()` | `gumx86writer.c` | 创建x86指令写入器 |
  | `putCallAddressWithArguments()` | `gum_x86_writer_put_call_address_with_arguments()` | `gumx86writer.c` | 生成函数调用指令 |
  | `putJmpAddress()` | `gum_x86_writer_put_jmp_address()` | `gumx86writer.c` | 生成跳转指令 |
  | `flush()` | `gum_x86_writer_flush()` | `gumx86writer.c` | 刷新写入器缓冲区 |

  ### Arm64Writer映射表

  | JavaScript Constructor/Method | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `newArm64Writer()` | `gum_arm64_writer_new()` | `gumarm64writer.c` | 创建ARM64指令写入器 |
  | `putCallAddressWithArguments()` | `gum_arm64_writer_put_call_address_with_arguments()` | `gumarm64writer.c` | 生成函数调用指令 |
  | `putBImm()` | `gum_arm64_writer_put_b_imm()` | `gumarm64writer.c` | 生成分支指令 |
  | `flush()` | `gum_arm64_writer_flush()` | `gumarm64writer.c` | 刷新写入器缓冲区 |

  ### Relocator映射表

  | JavaScript Constructor/Method | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `newX86Relocator()` | `gum_x86_relocator_new()` | `gumx86relocator.c` | 创建x86指令重定位器 |
  | `readOne()` | `gum_x86_relocator_read_one()` | `gumx86relocator.c` | 读取一条指令 |
  | `writeAll()` | `gum_x86_relocator_write_all()` | `gumx86relocator.c` | 写入所有重定位指令 |

  ## 内存布局与数据结构可视化

  ### GumInstruction结构体内存布局

  ```

  ```

  ### GumX86Writer结构体内存布局

  ```

  ```

  ### GumArm64Writer结构体内存布局

  ```

  ```

  ### GumX86Relocator结构体内存布局

  ```

  ```

  ## 系统调用级执行流程追踪

  ### Instruction.parse()执行流程

  ### X86Writer.putCallAddressWithArguments()执行流程

  ### Arm64Writer.putBImm()执行流程

  ### X86Relocator.readOne()执行流程

  ## 跨平台差异与抽象机制

  ### 指令集架构差异

  #### x86/x86\_64架构特点

  #### ARM/ARM64架构特点

  #### MIPS架构特点

  ### ABI差异处理

  ### 抽象层设计

  ```

  ```

  ## 调试命令与安全实践

  ### GDB调试示例

  ```

  ```

  ### 性能优化建议

  ### 安全考虑

  ## 错误处理与边界情况

  ### 常见错误场景

  ### 最佳实践

  ```

  ```

  ## 攻击检测场景映射

  ### 可用于检测的场景

  ### 防御绕过技术

  ## 性能分析与优化

  ### 时间复杂度分析

  ### 内存使用分析

  ## 扩展功能与自定义实现

  ### 自定义指令分析工具

  ```

  ```

  ### 自定义代码生成器

  ```

  ```

  ### 底层扩展点

  ## 版本兼容性与演进

  ### API变更历史

  ### 向后兼容性保证

  ## 实战案例分析

  ### 案例1: 动态代码补丁

  ```

  ```

  ### 案例2: ROP链构建

  ```

  ```

  ### 案例3: ARM64函数Hook

  ```

  ```

  ### 案例4: 指令级别性能剖析

  ```

  ```

  ## 总结与最佳实践

  CPU和Instruction模块是Frida最底层也是最强大的功能之一，提供了对机器指令级别的精确控制能力。理解其JS与C++的映射关系有助于：

  通过本文档的五层架构分析，开发者可以全面掌握CPU和Instruction模块的工作原理和使用技巧，为底层动态分析任务提供坚实的基础。

+ 核心API保持稳定
+ 新功能通过扩展方式添加
+ 废弃的API会标记并提供迁移路径

+ **Frida早期版本**: 基本的x86指令支持
+ **Frida 6.x**: 添加ARM和ARM64支持
+ **Frida 8.x**: 完善跨平台支持和性能优化
+ **Frida 10.x**: 添加MIPS支持和更多指令特性
+ **Frida 12.x**: 优化内存使用和错误处理
+ **Frida 14.x**: 改进指令解析准确性和性能

+ 可以通过修改 `guminstruction.c`添加新的指令解析特性
+ 通过修改 `gumx86writer.c`等文件添加新的指令生成原语
+ 扩展指令重定位器支持更复杂的控制流模式
+ 添加新的架构支持（如RISC-V、PowerPC等）

+ **Instruction对象**: 每个对象占用固定内存（包含字符串和数组）
+ **Writer缓冲区**: 需要预分配足够的代码缓冲区
+ **Relocator缓冲区**: 需要存储输入和输出指令信息
+ **优化建议**:
+ 重用Instruction对象避免频繁分配
+ 预估代码大小避免缓冲区重新分配
+ 及时释放不再需要的对象

+ **Instruction.parse()**: O(1)，单条指令解析
+ **Writer操作**: O(1)，每条指令生成
+ **Relocator操作**: O(n)，n为重定位的指令数量
+ **批量操作**: O(m)，m为总指令数量

+ **指令混淆**: 使用等价但不同的指令序列
+ **多态代码**: 运行时动态生成不同的指令序列
+ **加密指令**: 加密存储指令，运行时解密执行
+ **间接跳转**: 使用间接跳转隐藏控制流

+ **代码注入检测**: 监控可执行内存的分配和修改
+ **ROP链检测**: 分析可疑的指令序列模式
+ **Shellcode检测**: 识别常见的shellcode特征
+ **反调试检测**: 检测指令级别的反调试技术

+ **Instruction错误**:
+ 无效地址：无法读取指令字节
+ 无效指令：遇到未定义的操作码
+ 内存保护：无法访问受保护的内存区域
+ **Writer错误**:
+ 缓冲区溢出：写入超出分配的代码缓冲区
+ 无效地址：跳转目标超出指令范围
+ ABI不匹配：参数类型与ABI要求不符
+ **Relocator错误**:
+ 指令边界：无法正确识别指令边界
+ 自修改代码：重定位过程中代码被修改
+ 复杂控制流：无法处理复杂的跳转模式

+ **内存保护**: 确保代码缓冲区具有可执行权限
+ **地址验证**: 验证跳转和调用目标地址的有效性
+ **缓冲区溢出**: 避免指令写入超出分配的缓冲区
+ **异常处理**: 正确处理无效指令和编码错误

+ **指令缓存**: 缓存常用的指令序列避免重复生成
+ **批量写入**: 减少flush()调用次数，批量生成指令
+ **内存对齐**: 确保代码缓冲区正确对齐以获得最佳性能
+ **架构特定优化**: 利用特定架构的优化指令

+ **x86\_64 System V ABI** (Unix/Linux/macOS):
+ 参数传递：整数%rdi, %rsi, %rdx, %rcx, %r8, %r9；浮点%xmm0-%xmm7
+ 返回值：整数%rax，浮点%xmm0
+ 栈对齐：16字节对齐
+ **Microsoft x64 ABI** (Windows):
+ 参数传递：整数%rcx, %rdx, %r8, %r9；浮点%xmm0-%xmm3
+ 影子空间：调用者为前4个参数预留32字节栈空间
+ 栈对齐：16字节对齐
+ **ARM64 AAPCS64 ABI**:
+ 参数传递：整数x0-x7，浮点v0-v7
+ 返回值：整数x0，浮点v0
+ 栈对齐：16字节对齐

+ **固定长度指令**: 32位固定长度
+ **延迟槽**: 分支指令后的延迟槽
+ **加载/存储架构**: 类似ARM的内存访问模式
+ **流水线优化**: 指令流水线设计考虑

+ **固定长度指令**: ARM64为32位固定长度
+ **条件执行**: ARM支持条件执行指令
+ **加载/存储架构**: 只有加载/存储指令访问内存
+ **Thumb模式**: ARM支持16/32位混合指令集

+ **变长指令**: 1-15字节不等
+ **复杂寻址模式**: 支持多种内存寻址方式
+ **寄存器重命名**: 现代CPU的寄存器重命名机制
+ **指令前缀**: 支持多种指令前缀（LOCK, REP, SEG等）

+ 是否为跳转指令
+ 是否为调用指令
+ 是否有延迟槽（MIPS）

+ **System V ABI**: 前6个整数参数使用%rdi, %rsi, %rdx, %rcx, %r8, %r9
+ **Microsoft x64 ABI**: 前4个整数参数使用%rcx, %rdx, %r8, %r9

+ **x86/x86\_64**: 使用Intel XED或Capstone反汇编引擎
+ **ARM/ARM64**: 使用自定义ARM指令解码器
+ **MIPS**: 使用自定义MIPS指令解码器

+ `gum_x86_relocator_new()`
+ `gum_x86_relocator_read_one()`
+ `gum_x86_relocator_write_all()`

+ **x86/x86\_64**: `gumx86relocator.c` - x86指令重定位
+ **ARM/ARM64**: `gumarmrelocator.c`, `gumarm64relocator.c` - ARM指令重定位
+ **Thumb**: `gumthumbrelocator.c` - Thumb指令重定位
+ **MIPS**: `gummipsrelocator.c` - MIPS指令重定位

+ `gum_x86_writer_new()`
+ `gum_x86_writer_put_call_address_with_arguments()`
+ `gum_x86_writer_put_jmp_address()`
+ `gum_x86_writer_flush()`

+ **x86/x86\_64**: `gumx86writer.c` - x86指令生成
+ **ARM/ARM64**: `gumarmwriter.c`, `gumarm64writer.c` - ARM指令生成
+ **Thumb**: `gumthumbwriter.c` - Thumb指令生成
+ **MIPS**: `gummipswriter.c` - MIPS指令生成

+ `gum_instruction_parse()`
+ `gum_instruction_free()`
+ `gum_instruction_get_address()`
+ `gum_instruction_get_mnemonic()`

+ **通用指令解析**: `guminstruction.c` - 跨平台指令解析框架
+ **平台特定后端**:
+ **x86/x86\_64**: `gumx86reader.c` - 基于Intel XED或Capstone
+ **ARM/ARM64**: `gumarmreader.c`, `gumarm64reader.c` - ARM指令解析
+ **MIPS**: `gummipsreader.c` - MIPS指令解析

+ **x86**: `X86Register`, `X86OperandType`, `X86Group`
+ **ARM**: `ArmRegister`, `ArmOperandType`, `ArmGroup`
+ **ARM64**: `Arm64Register`, `Arm64OperandType`, `Arm64Group`
+ **MIPS**: `MipsRegister`, `MipsOperandType`, `MipsGroup`

+ `newX86Writer(codeAddress[,options])`
+ `writer.putCallAddressWithArguments(func,argTypes,args)`
+ `writer.putJmpAddress(address)`...