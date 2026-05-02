---
title: fic2026初赛pc部分wp
url: https://mp.weixin.qq.com/s/q-uE7GeEd6_C0xUTnEJMWw
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:55:11.637153
---

# fic2026初赛pc部分wp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SVAhggk0wby6e1NB34ic6Syd7GLjjSEgZLNKUvWIvPET8JZWFiaIIliaS7TgJQPQaERcUqO5Z0wkn1K3L0MCHIoqHhic47tTqFKKhDEEUv2bcZs/0?wx_fmt=jpeg)

# fic2026初赛pc部分wp

原创

老皮皮
老皮皮

老皮的碎碎念念

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

1. 分析计算机检材，操作系统版本号为

Deepin 23.1 cat /etc/os-release直接看

2. 分析计算机检材，李安弘曾收到一份免费领取token的邮件的疑似钓鱼邮件，其发送用户邮箱为

邮件中有

3. 分析计算机检材，李安弘电脑中记录的黄金换现金的商家联系方式为

语音记事本

4. 分析计算机检材，推广设计图中的apk下载链接为

- 在163邮箱中发现发件人 z07752443452@hotmail.com 发送的"转发: 推广设计图"邮件

- 邮件附件包含： 推广设计图.png.enc （RSA加密的图片）、 加密图片查看.html （解密工具）、 public.txt （RSA公钥）

- 从 public.txt 提取RSA公钥（n和e=65537）

- 对1024位RSA模数n进行因数分解，得到素因子p和q

- 计算RSA私钥d，使用Python脚本解密 推广设计图.png.enc

- 解密后的PNG图片有CRC错误，修复PNG chunk的CRC校验值

- 从修复后的图片中提取QR码，解码得到Google Drive下载链接

```
import paramikoimport timeimport sysdef ssh_exec(command, retries=5, timeout=120):    for attempt in range(retries):        try:            transport = paramiko.Transport(('192.168.1.136', 22))            transport.connect(username='lha', password='123456')            transport.default_window_size = 2147483647            channel = transport.open_session()            channel.settimeout(timeout)            channel.exec_command(command)            out = b''            while True:                try:                    data = channel.recv(65536)                    if not data:                        break                    out += data                except:                    break            transport.close()            return out        except Exception as e:            print(f"Attempt {attempt+1} failed: {e}", file=sys.stderr)            try:                transport.close()            except:                pass            time.sleep(5)    return b''print("=== Download encrypted image ===")result = ssh_exec("cat '/home/lha/.local/share/deepin/deepin-mail/imap.163.com/lihongan19851024@163.com/imap/d3b8fe30-e7d5-4d26-b96c-d335b82ae2f4/DP2/推广设计图.png.enc' 2>/dev/null")enc_data = resultprint(f"Downloaded {len(enc_data)} bytes")print("\n=== Download public key ===")result = ssh_exec("cat /home/lha/Downloads/public.txt 2>/dev/null")pub_key_text = result.decode('utf-8', errors='replace')print(pub_key_text)n = 57751892008149574447756694613209346511056045951970458143905594411398554113111623746466692172544473909892773600617029641656248235151775166339061269972238018743173330948084699695182438765935110193323089354031112350869626121317836465551360104372140181097747761558797918522051881262043738603183528521379831286761p = 7629417397247058569317994244683898237435779295980258469766809q = 7570257298495536404124232850334277264665764494243265578743print(f"\np * q == n: {p * q == n}")e = 65537phi = (p - 1) * (q - 1)d = pow(e, -1, phi)enc_block_size = 128plain_chunk_size = 120total_blocks = len(enc_data) // enc_block_sizeprint(f"Total blocks: {total_blocks}")print(f"Expected output size: {total_blocks * plain_chunk_size}")result = bytearray()for i in range(total_blocks):    if i % 50 == 0:        print(f"Decrypting block {i}/{total_blocks}...")    block = enc_data[i * enc_block_size:(i + 1) * enc_block_size]    c = int.from_bytes(block, byteorder='big')    m = pow(c, d, n)    m_bytes = m.to_bytes(plain_chunk_size, byteorder='big')    result.extend(m_bytes)output_path = r'c:\Users\Administrator\Documents\trae_projects\pc\decrypted_image2.png'with open(output_path, 'wb') as f:    f.write(result)print(f"Decrypted image saved to {output_path}")print(f"Total output size: {len(result)} bytes")print(f"First 32 bytes hex: {result[:32].hex()}")png_sig = b'\x89PNG\r\n\x1a\n'print(f"PNG signature check: {result[:8] == png_sig}")
```

致敬手搓的大佬

5. 分析计算机检材，李安弘电脑vpn软件开放的代理端口为

9527 右下角查看uos ai 系统代理

6. 分析计算机检材，李安弘电脑中AI软件当前使用的模型类型为

deepseek 右下角uos ai

7. 分析计算机检材，李安弘电脑中AI软件当前使用的模型apiKey为

/home/lha/.local/share/deepin/uos-ai-assistant/db/basic

火眼全盘搜索9676a，

8. 分析计算机检材，李安弘电脑中勒索软件提供的解密服务联系方式为

vc加密分区（密码在手机备忘录）挂载，ida加ai分析下面的get\_token\_linux程序

```
1. 构造通配符字符串 "*.mp4"2. 调用 filepath.Glob("*.mp4") 查找所有 MP4 文件3. 遍历每个文件：   - 读取文件内容（os.ReadFile）   - 调用 main._a(file_data, 1337) 进行加密   - 用 OR 操作累积返回值4. 如果有文件被修改（返回值非0）：   - 打印勒索信息   - 休眠1秒   - 打印第二条信息5. 否则静默退出
```

分析出其中的邮件地址 beijixin996@tutanota.com

9. 分析计算机检材，李安弘电脑中记录的存放黄金的保险柜编号是

其中的mp4文件，导出修复，可以直接用视频修复软件，也可以用上面的分析对每个 stco 中的 chunk offset 减去 1337 即可恢复文件，其中一个视频有

```
# 解密脚本思路import structdef decrypt_mp4(filepath):    with open(filepath, 'rb') as f:        data = bytearray(f.read())    # 找到 "stco" 原子    idx = data.find(b'stco')    if idx == -1:        return    # stco 结构: [4字节size][4字节"stco"][4字节版本/标志][4字节entry_count][entries...]    entry_count_off = idx + 4 + 4  # 版本/标志之后    entry_count = struct.unpack('>I', data[entry_count_off:entry_count_off+4])[0]    # 修改每个 chunk offset    for i in range(entry_count):        off = entry_count_off + 4 + i * 4        val = struct.unpack('>I', data[off:off+4])[0]        val -= 1337  # 减去 1337 还原        struct.pack_into('>I', data, off, val)    with open(filepath, 'wb') as f:        f.write(data)
```

10. 分析计算机检材，李安弘电脑中记录的保险柜密码是

在数据盘tools目录发现enrycpxls文件，是et文件的加密方式

丢给ai编写出解码程序

```
iimport olefileimport structimport osfolder = r'c:\Users\Administrator\Documents\trae_projects\2\zhongyao'filepath = os.path.join(folder, '保险箱的秘密.et')font = {    '0':[[1,0],[2,0],[0,1],[3,1],[0,2],[3,2],[0,3],[3,3],[1,4],[2,4]],    '1':[[2,0],[1,1],[2,1],[2,2],[2,3],[1,4],[2,4],[3,4]],    '2':[[1,0],[2,0],[0,1],[3,1],[2,2],[1,3],[0,4],[1,4],[2,4],[3,4]],    '3':[[0,0],[1,0],[2,0],[3,1],[1,2],[2,2],[3,3],[0,4],[1,4],[2,4]],    '4':[[3,0],[2,1],[3,1],[1,2],[3,2],[0,3],[1,3],[2,3],[3,3],[4,3],[3,4]],    '5':[[0,0],[1,0],[2,0],[0,1],[0,2],[1,2],[2,2],[3,3],[0,4],[1,4],[2,4]],    '6':[[1,0],[2,0],[0,1],[0,2],[1,2],[2,2],[0,3],[3,3],[1,4],[2,4]],    '7':[[0,0],[1,0],[2,0],[3,0],[3,1],[2,2],[1,3],[1,4]],    '8':[[1,0],[2,0],[0,1],[3,1],[1,2],[2,2],[0,3],[3,3],[1,4],[2,4]],    '9':[[1,0],[2,0],[0,1],[3,1],[1,2],[2,2],[3,2],[3,3],[2,4]],    'a':[[1,2],[2,2],[3,2],[0,3],[3,3],[1,4],[2,4],[3,4]],    'b':[[0,0],[0,1],[0,2],[1,2],[2,2],[0,3],[3,3],[0,4],[1,4],[2,4]],    'c':[[1,0],[2,0],[3,0],[0,1],[0,2],[0,3],[1,4],[2,4],[3,4]],    'd':[[3,0],[3,1],[1,2],[2,2],[3,2],[0,3],[3,3],[1,4],[2,4],[3,4]],    'e':[[1,0],[2,0],[0,1],[0,2],[1,2],[2,2],[0,3],[1,4],[2,4]],    'f':[[1,0],[2,0],[1,1],[0,2],[1,2],[2,2],[1,3],[1,4]],    'g':[[1,2],[2,2],[3,2],[0,3],[3,3],[1,4],[2,4],[3,4],[3,5],[1,6],[2,6]],    'h':[[0,0],[0,1],[0,2],[1,2],[2,2],[0,3],[3,3],[0,4],[3,4]],    'i':[[1,0],[1,2],[1,3],[1,4]],    'j':[[2,0],[2,2],[2,3],[2,4],[2,5],[1,6],[0,5]],    'k':[[0,0],[0,1],[0,2],[0,3],[0,4],[2,2],[1,3],[3,3],[2,4]],    'l':[[1,0],[1,1],[1,2],[1,3],[1,4]],    'm':[[0,1],[1,1],[2,1],[3,1],[4,1],[0,2],[2,2],[4,2],[0,3],[4,3]],    'n':[[0,1],[1,0],[2,0],[0,2],[3,2],[0,3],[3,3],[0,4],[3,4]],    'o':[[1,1],[2,1],[0,2],[3,2],[1,3],[2,3]],    'p':[[0,2],[1,2],[2,2],[0,3],[3,3],[0,4],[1,4],[2,4],[0,5],[0,6]],    'q':[[1,2],[2,2],[0,3],[3,2],[3,3],[3,4],[3,5],[4,5]],    'r':[[0,2],[0,3],[0,4],[1,2],[2,2]],    's':[[1,0],[2,0],[3,0],[0,1],[1,2],[2,2],[3,3],[0,4],[1,4],[2,4]],    't':[[1,0],[1,1],[1,2],[1,3],[1,4],[0,2],[2,2]],    'u':[[0,2],[0,3],[3,2],[3,3],[1,4],[2,4],[3,4]],    'v':[[0,0],[4,0],[1,2],[3,2],[2,4]],    'w':[[0,2],[0,3],[1,4],[2,3],[3,4],[4,2],[4,3]],    'x':[[0,0],[4,0],[1,1],[3,1],[2,2],[1,3],[3,3],[0,4],[4,4]],    'y':[[0,0],[4,0],[1,1],[3,1],[2,2],[2,3],[1,4]],    'z':[[0,0],[1,0],[2,0],[3,0],[2,1],[1,2],[0,3],[0,4],[1,4],[2,4],[3,4]],    ':':[[1,1],[1,3]],    '@':[[1,0],[2,0],[0,1],[3,1],[0,2],[2,2],[3,2],[0,3],[1,4],[2,4]],    '.':[[1,4]]}def decrypt_value(val):    part1 = val // 1000    part2 = val % 1000    x = (part1 ^ 85) - 100    y = (part2 ^ 85) - 100    return x, ydef encrypt_coord(x, y):    return ((x + 100) ^ 85) * 1000 + ((y + 100) ^ 85)ole = olefile.OleFileIO(filepath)workbook_data = ole.openstream('Workbook').read()ole.close()print("Checking for missing 'i' character at position 4")print("="*70)expected_i_dots = font['i']print(f"\nExpected 'i' dots: {expected_i_dots}")for dot in expected...