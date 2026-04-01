---
title: 2026 DesCTF网络安全挑战赛 官方WP
url: https://mp.weixin.qq.com/s/7KTABvSr1LsAngT6EbTubQ
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:42:53.732438
---

# 2026 DesCTF网络安全挑战赛 官方WP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mFCErZsUXhMSAgRiax4ENga9fdlQqg2Ucwa081TER3KX9u5JiaVkvp0Zo02fSZhRUFHYPL3Xia9XsDibVNU5nKwvVrlGmnCmKMRennPHfibvhBEU/0?wx_fmt=jpeg)

# 2026 DesCTF网络安全挑战赛 官方WP

原创

天命
天命

天命团队

![]()

在小说阅读器中沉浸阅读

# Misc

## 张三的秘密

在屏幕截图找到第一二个密钥

```
0x4e769b2cb222e299d33ea4b89e2831e12399a6b0117336e981a567371726b3368c73f3488e18
0x47bb1ac5f6a422e8b4d483334b5d7fe2f8bae6ae665322ff30b2cade7f03e434a2e849d08599
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mFCErZsUXhNSPtODA1ia8XZwsoNOQz4gV22uO40myMltnPqv7eBzwrIriaxmY4aiaic2glshfpnjiaYPsrn6coiasBibGveI1vLGcjMQCbiammGicOEw/640?wx_fmt=png&from=appmsg)

返回到桌面有个饭卡里面有个二维码找到第三个密钥

![](https://mmbiz.qpic.cn/mmbiz_png/mFCErZsUXhMYlQgaFYfAibN6sib2xPM6gwuKDTMdq7jblFvsyCpUn7FmpxsAjZLGks2Nibwpn1BjlSqoltwZKZPWWkLU9CMAXP5Uzaj15aiaxOU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/mFCErZsUXhPqibIzTfyHbhB7iajYRKZ4GD0hs9joeWr4moxV1lnE7d5Fgww90K79xUjm7ZaJTWMyu3crH5nasmD1BU1mSpb1B9bTd5Y4GnoQI/640?wx_fmt=png&from=appmsg)

在壁纸缓存处找到第四个密钥

![](https://mmbiz.qpic.cn/mmbiz_png/mFCErZsUXhO31HVPtDrN3ynAKRVn4FniaAJUBsteSZ2vHYicaQlcM88eZJLEp0jUcohiaqMlsJibKuCwTCKq8e5JZTiaYcX4SPVNzTMcR5l1jDmc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/mFCErZsUXhNbibdfyI4kWWG1IE684J1gIYKG2laf3AiaqbSygltCgKiaX3bdmpsicZceAvwYKjq0Z3e9U235TEib9UbPKStHfwErfSdcMMsQGmmA/640?wx_fmt=png&from=appmsg)在注册表找到第五个密钥

![](https://mmbiz.qpic.cn/mmbiz_png/mFCErZsUXhPiaibISdMRRemUzAdH6HYgs61QB8lPse0raDgO02NjdBjM80pMjibca1nvibPlrabHs9vWEsckZYRHMxUcnXoJHzWjz5pLbCfcG5E/640?wx_fmt=png&from=appmsg)shamir门限

```
from Crypto.Util.number import *

p = 0x666c61677b3431e120579912cdf6831aed2476b0f3fab7c37b86a5c7b847e226a97f72f45783
t = [0x4e769b2cb222e299d33ea4b89e2831e12399a6b0117336e981a567371726b3368c73f3488e18,
     0x47bb1ac5f6a422e8b4d483334b5d7fe2f8bae6ae665322ff30b2cade7f03e434a2e849d08599,
     0x4a37c5fad9d060d12f2cf65650fdd718d18d7e0a777276e85e1dd70a4a3c5b842d1feb896c42,
     0x3f961ff18045be09c0ef92b6a5813cdfe8dc365f613b130ed430095e657c8391a1c03ac5ace5,
     0xf0fe0b8be939ecd598f774ca043352f43dfb9fa3b74678aa9f9c9f68ab385f071d84376e64e]

m = ([0, t[0]], [0, t[1]], [0, t[2]], [0, t[3]], [0, t[4]])
for i in permutations(range(9), 5):
    m[0][0] = i[0]
    m[1][0] = i[1]
    m[2][0] = i[2]
    m[3][0] = i[3]
    m[4][0] = i[4]
    try:
        r = (
                    m[0][1] * (0 - m[1][0]) * (0 - m[2][0]) * (0 - m[3][0]) * (0 - m[4][0]) * inverse(
                (m[0][0] - m[1][0]) * (m[0][0] - m[2][0]) * (m[0][0] - m[3][0]) * (m[0][0] - m[4][0]), p) +
                    m[1][1] * (0 - m[0][0]) * (0 - m[2][0]) * (0 - m[3][0]) * (0 - m[4][0]) * inverse(
                (m[1][0] - m[0][0]) * (m[1][0] - m[2][0]) * (m[1][0] - m[3][0]) * (m[1][0] - m[4][0]), p) +
                    m[2][1] * (0 - m[1][0]) * (0 - m[0][0]) * (0 - m[3][0]) * (0 - m[4][0]) * inverse(
                (m[2][0] - m[1][0]) * (m[2][0] - m[0][0]) * (m[2][0] - m[3][0]) * (m[2][0] - m[4][0]), p) +
                    m[3][1] * (0 - m[1][0]) * (0 - m[2][0]) * (0 - m[0][0]) * (0 - m[4][0]) * inverse(
                (m[3][0] - m[1][0]) * (m[3][0] - m[2][0]) * (m[3][0] - m[0][0]) * (m[3][0] - m[4][0]), p) +
                    m[4][1] * (0 - m[1][0]) * (0 - m[2][0]) * (0 - m[3][0]) * (0 - m[0][0]) * inverse(
                (m[4][0] - m[1][0]) * (m[4][0] - m[2][0]) * (m[4][0] - m[3][0]) * (m[4][0] - m[0][0]), p)
            ) % p
        temp = str(long_to_bytes(r))
        if ("flag" in temp):
            print(temp)
    except:
        pass

#b'flag{37af8b400737929ad29ad6876d283e92}'
```

## infrared\_code

通过该手册可知电视的datasheet，从

https://raw.githubusercontent.com/Lucaslhm/Flipper-IRDB/refs/heads/main/TVs/Hisense/Hisense\_32A4HAU.ir

找到它的ir指令定义。通过编写程序筛选出仅进行上下左右和OK的按键操作，对着操作还原按键顺序，输入的按键即为flag，脚本如下所示：

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

KEYBOARD = [
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['G', 'H', 'I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P', 'Q', 'R'],
    ['S', 'T', 'U', 'V', 'W', 'X'],
    ['Y', 'Z', '1', '2', '3', '4'],
    ['5', '6', '7', '8', '9', '0'],
]

COMMAND_TO_OP = {
    '16 E9 00 00': 'u',  # Up
    '17 E8 00 00': 'd',  # Down
    '19 E6 00 00': 'l',  # Left
    '18 E7 00 00': 'r',  # Right
    '15 EA 00 00': 'o',  # Ok
}

NOISE_COMMANDS = {
    '44 BB 00 00',  # Vol_up
    '43 BC 00 00',  # Vol_dn
    'CA 35 00 00',  # Pause/play
    '54 AB 00 00',  # Yellow
    '55 AA 00 00',  # Blue
    '52 AD 00 00',  # Red
    '53 AC 00 00',  # Green
    '0E F1 00 00',  # Mute
    '4A B5 00 00',  # Ch_next
    '4B B4 00 00',  # Ch_prev
}

class VirtualKeyboard:
    def __init__(self):
        self.keyboard = KEYBOARD
        self.row = -1# -1 means we're in the special row above
        self.col = 4   # Column 4 is E, which is under 删除
        self.result = ""

    def move_up(self):
        if self.row > -1:
            self.row -= 1

    def move_down(self):
        if self.row < len(self.keyboard) - 1:
            self.row += 1

    def move_left(self):
        if self.col > 0:
            self.col -= 1

    def move_right(self):
        if self.col < 5:  # Max column is 5 (F)
            self.col += 1

    def press_ok(self):
        if self.row == -1:
            # Special row: 清空 (col 0-2) or 删除 (col 3-5)
            if self.col <= 2:
                self.result = ""
            else:
                if self.result:
                    self.result = self.result[:-1]
        else:
            # Normal keyboard
            char = self.keyboard[self.row][self.col]
            self.result += char.lower()

    def get_current_char(self):
        if self.row == -1:
            if self.col <= 2:
                return'清空'
            else:
                return'删除'
        else:
            return self.keyboard[self.row][self.col]

    def get_result(self):
        return self.result

def parse_ir_file(file_path):
    """
    Parse IR commands file and extract command codes

    Returns:
        List of command codes
    """
    commands = []

    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith('command:'):
            # Extract command code
            parts = line.split(':', 1)
            if len(parts) == 2:
                cmd = parts[1].strip()
                commands.append(cmd)

    return commands

def ir_to_operations(commands):
    operations = []

    for cmd in commands:
        if cmd in COMMAND_TO_OP:
            operations.append(COMMAND_TO_OP[cmd])
        # Ignore noise commands

    return operations

def execute_operations(operations, verbose=False):

    kb = VirtualKeyboard()
    operation_buffer = []

    for op in operations:
        operation_buffer.append(op)

        if op == 'u':
            kb.move_up()
        elif op == 'd':
            kb.move_down()
        elif op == 'l':
            kb.move_left()
        elif op == 'r':
            kb.move_right()
        elif op == 'o':
            # Ok pressed - execute action
            if verbose:
                ops_str = ''.join(operation_buffer)
                char = kb.get_current_char()
                print(f"{ops_str:15s} -> {char:5s} (pos: {kb.row},{kb.col})")

            kb.press_ok()
            operation_buffer = []

    return kb.get_result()

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python decode_ir_commands.py <ir_file>")
        print("Example: python decode_ir_commands.py ir_challenge.txt")
        sys.exit(1)

    ir_file = sys.argv[1]

    commands = parse_ir_file(ir_file)

    operations = ir_to_operations(commands)
    print(f"\n[*] Executing operations on virtual keyboard...")
    print(f"\n{'Operation':<15s} -> {'Char':<5s}")
    print("-" * 30)

    result = execute_operations(operations, verbose=True)

    print(result)

if __name__ == "__main__":
    main()
```

运行得到flag：flag1nfr4r3disfun，最终flag为

```
flag{1nfr4r3disfun}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mFCErZsUXhMELRRUqu54FEqxRVO...