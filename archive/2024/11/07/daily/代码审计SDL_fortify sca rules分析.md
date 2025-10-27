---
title: fortify sca rules分析
url: https://mp.weixin.qq.com/s?__biz=MzI2NTExNzcxNQ==&mid=2247484336&idx=1&sn=c93f077955f1d5dad18d525ac2a6be2b&chksm=eaa30accddd483da475f52d506d465e74ea503430e8af42ba2186a839cb59e6be911666555e1&scene=58&subscene=0#rd
source: 代码审计SDL
date: 2024-11-07
fetch_date: 2025-10-06T19:18:54.522550
---

# fortify sca rules分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/a4tp2b7vTo7jJzCYtjl3llRy2bXvTY4D0F6yxfj5B8dnORhibqRrEM8orL7ztWLibYcQFKGxpQZgca0QFLRkFJDA/0?wx_fmt=jpeg)

# fortify sca rules分析

原创

sanduo

代码审计SDL

fortify sca rules 一直处于加密状态，只有在扫描的时候才会被加载，网上发现已经有大佬破解了，这里分享给大家，jar包知识星球自取，解密代码如下，自行编译即可：

```
import java.io.*;import java.nio.file.Files;import java.security.*;import java.util.Properties;import java.util.StringTokenizer;import java.util.zip.GZIPInputStream;import java.util.zip.GZIPOutputStream;
public class Main {    // 定义常量    private static final String MESSAGE_DIGEST_ALGORITHM = "SHA-1"; // 消息摘要算法    private static final String CRYPTO_PROVIDER = "SUN"; // 加密提供者    private static final int BUFFER_SIZE = 262144; // 缓冲区大小    private static final String STD = "1fea047f-dee0ac89-b5db25a6-b0c3a4cf"; // 默认密钥
    // 构造函数    public Main() {    }
    // 获取消息摘要算法实例    public static MessageDigest getMessageDigestAlgorithm() {        try {            return MessageDigest.getInstance(MESSAGE_DIGEST_ALGORITHM, CRYPTO_PROVIDER);        } catch (GeneralSecurityException e) {            throw new RuntimeException(e);        }    }
    // 计算输入流的摘要    public static byte[] makeDigest(InputStream inStream) throws IOException {        return makeDigest(inStream, getMessageDigestAlgorithm());    }
    // 计算输入流的摘要，使用指定的消息摘要算法    public static byte[] makeDigest(InputStream inStream, MessageDigest md) throws IOException {        md.reset();        DigestInputStream in = new DigestInputStream(inStream, md);        return md.digest(); // 返回摘要结果    }
    // 加密函数    private static void encrypt(long[] v, long[] k) {        long y = v[0];        long z = v[1];        long sum = 0L;        long delta = 2654435769L; // 常量 delta        long n = 32L; // 迭代次数        long top = 4294967295L; // 掩码
        // 加密循环        for (; n-- > 0L; z &= top) {            sum += delta;            sum &= top;            y += (z << 4) + k[0] ^ z + sum ^ (z >> 5) + k[1];            y &= top;            z += (y << 4) + k[2] ^ y + sum ^ (y >> 5) + k[3];        }
        v[0] = y;        v[1] = z;    }
    // 解密函数    private static void decrypt(long[] v, long[] k) {        long n = 32L; // 迭代次数        long y = v[0];        long z = v[1];        long delta = 2654435769L; // 常量 delta        long top = 4294967295L; // 掩码        long sum = delta << 5;
        // 解密循环        for (sum &= top; n-- > 0L; sum &= top) {            z -= (y << 4) + k[2] ^ y + sum ^ (y >> 5) + k[3];            z &= top;            y -= (z << 4) + k[0] ^ z + sum ^ (z >> 5) + k[1];            y &= top;            sum -= delta;        }
        v[0] = y;        v[1] = z;    }
    // 加密输入流到输出流    private static void enc(InputStream source, OutputStream dest, long[] usrKey) throws IOException {        long[] k = usrKey.clone(); // 克隆密钥        byte[] byteBuf = new byte[8]; // 字节缓冲区        byte[] tail = new byte[]{32, 32, 32, 32, 32, 32, 32, 8}; // 尾部字节        long[] unsigned32Buf = new long[2]; // 无符号32位缓冲区        long top = 4294967295L; // 掩码
        int bytesRead;        // 读取输入流并加密        while ((bytesRead = source.read(byteBuf)) != -1) {            if (bytesRead < 8) {                tail[7] = (byte) bytesRead; // 设置尾部字节            }
            byteArrayToUnsigned32(byteBuf, unsigned32Buf); // 字节数组转换为无符号32位数组            encrypt(unsigned32Buf, k); // 加密            k[0] = k[0] + 17L & top; // 更新密钥            k[1] = k[1] + 17L & top;            k[2] = k[2] + 17L & top;            k[3] = k[3] + 17L & top;            unsigned32ToByteArray(unsigned32Buf, byteBuf); // 无符号32位数组转换为字节数组            dest.write(byteBuf); // 写入输出流        }
        byteArrayToUnsigned32(tail, unsigned32Buf); // 处理尾部字节        encrypt(unsigned32Buf, k);        k[0] = k[0] + 17L & top;        k[1] = k[1] + 17L & top;        k[2] = k[2] + 17L & top;        k[3] = k[3] + 17L & top;        unsigned32ToByteArray(unsigned32Buf, tail);        dest.write(tail); // 写入尾部字节    }
    // 解密输入流到输出流    private static void dec(InputStream source, OutputStream dest, long[] usrKey) throws IOException {        long[] k = usrKey.clone(); // 克隆密钥        byte[] byteBuf = new byte[8]; // 字节缓冲区        byte[] byteBufDelay = null; // 延迟字节缓冲区        long[] unsigned32Buf = new long[2]; // 无符号32位缓冲区        long top = 4294967295L; // 掩码
        int bytesRead;        // 读取输入流并解密        while ((bytesRead = source.read(byteBuf)) != -1) {            if (bytesRead < 8) {                throw new IOException("invalid encrypted stream"); // 无效的加密流            }
            byteArrayToUnsigned32(byteBuf, unsigned32Buf); // 字节数组转换为无符号32位数组            decrypt(unsigned32Buf, k); // 解密            k[0] = k[0] + 17L & top; // 更新密钥            k[1] = k[1] + 17L & top;            k[2] = k[2] + 17L & top;            k[3] = k[3] + 17L & top;            unsigned32ToByteArray(unsigned32Buf, byteBuf); // 无符号32位数组转换为字节数组
            if (source.available() == 0) {                int bytesToWrite = byteBuf[7];                if (bytesToWrite > 8 || bytesToWrite < 0 || byteBufDelay == null) {                    throw new IOException("invalid encrypted stream"); // 无效的加密流                }
                dest.write(byteBufDelay, 0, bytesToWrite); // 写入延迟字节            }
            if (byteBufDelay != null) {                dest.write(byteBufDelay, 0, 8); // 写入延迟字节                byte[] t = byteBufDelay;                byteBufDelay = byteBuf;                byteBuf = t;            } else {                byteBufDelay = byteBuf;                byteBuf = new byte[8];            }        }    }
    // 执行块加密或解密    private static void doBlockCipher(InputStream source, OutputStream dest, boolean encrypt, long[] usrKey) throws IOException {        if (encrypt) {            enc(source, dest, usrKey); // 加密        } else {            dec(source, dest, usrKey); // 解密        }    }
    // 读取加密流中的头部信息    public static void readHeaders(InputStream encrypted) throws IOException {        Properties props = new Properties();        final PushbackInputStream src = new PushbackInputStream(encrypted);        props.load(new InputStream() {            boolean closed = false;
            public int read() throws IOException {                if (closed) {                    return -1;                } else {                    int c = src.read();                    if (c == 0) {                        src.unread(c);                        closed = true;                        return -1;                    } else {                        return c;                    }                }            }        });
        int read = src.read();        if (read != 0) {            throw new IOException("invalid encrypted stream"); // 无效的加密流        }    }
    // 解密并解压缩加密流中的数据    public static byte[] decryptCompressedAfterHeaders(InputStream encrypted, String keyString) throws IOException {        return decryptAfterHeaders(encrypted, keyString, true);    }
    // 解密加密流中的数据，可以选择是否解压缩    public static byte[] decryptAfterHeaders(InputStream encrypted, String keyString, boolean compressed) throws IOException {        long[] key = makeKeyFromString(keyString != null ? keyString : STD); // 生成密钥        ByteArrayOutputStream cleartext = new ByteArrayOutputStream();        doBlockCipher(encrypted, cleartext, false, key); // 解密        cleartext.close();        byte[] bytes = cleartext.toByteArray();        if (compressed) {            bytes = uncompressString(bytes); // 解压缩        }
        return bytes;    }
    // 解密并解压缩加密流中的数据    public static byte[] decryptCompressed(InputStream encrypted, String keyString) throws IOException {        readHeaders(encrypted); // 读取头部信息        return decryptCompressedAfterHeaders(encrypted, keyString);    }
    // 加密并压缩明文数据    public static void encryptAndCompress(InputStream cleartext, OutputStream ciphertext, String keyString, Properties properties) throws IOException {        if (properties != null) {            properties.store(ciphertext, null); // 存储属性        }
        ciphertext.write(new byte[]{0}); // 写入分隔符        encryptAfterHea...