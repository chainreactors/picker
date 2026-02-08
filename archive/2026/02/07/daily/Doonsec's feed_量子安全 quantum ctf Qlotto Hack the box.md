---
title: 量子安全 quantum ctf Qlotto Hack the box
url: https://mp.weixin.qq.com/s/rOi7PkG6PqCwCLlwPntVsw
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:30:36.837223
---

# 量子安全 quantum ctf Qlotto Hack the box

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2NvxwiaXLH1Cn1cZp00H1KfxJp8gbPmQpdk0abnoIxz3UZoriaIxkIeofTpZEibSK0ettfbGXdtSU5ArcTSfsWxClI1UII00PR8g/0?wx_fmt=jpeg)

# 量子安全 quantum ctf Qlotto Hack the box

枫林路大砍刀
枫林路大砍刀

看雪学苑

![]()

在小说阅读器中沉浸阅读

**01**

**代码分析server.py**

# 首先，拿到了一个server.py文件，我们先来分析代码：

#

这道题也是一上来是定义了一个类，然后引用了包和设置aer

```
from qiskit import QuantumCircuit, ClassicalRegister, transpile
from scipy.stats import binomtest
from qiskit_aer import Aer
from math import pi

#from my_secret import JACKPOT

class QuantumLotto:
    def __init__(self):
        self.backend = Aer.get_backend("qasm_simulator")
```

## **degrees\_to\_radians和**generate\_circuit

这里主要是第一个是角度的转换

然后是生成电路，和上一篇一样，门的输入范式等等，参数转化为int

上一篇：[量子安全 quantum ctf Global Hyperlink Zone Hack the box](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458606863&idx=1&sn=01fd80bfa67b7c7b26254022f0d11e81&scene=21#wechat_redirect)

这里一共生成了两条线路，并且0号最开始加了x门

```
    def degrees_to_radians(self, degrees: int):
        return degrees * (pi / 180)

    def generate_circuit(self, instructions: str):
        circuit = QuantumCircuit(2)

        circuit.h(0)

        instructions = instructions.split(";")
        for instr in instructions:
            parts = instr.split(":")

            if len(parts) != 2:
                print(f"[Dealer] The move '{instr}' isn't recognized at this table. Expected format: <gate>:<params>")
                return None

            gate, params = parts

            try:
                params = [ int(p) for p in params.split(",") ]
            except:
                print("[Dealer] Only number cards are allowed at this table.")
                return None
```

然后是这道题可以用到的门：H,S,T,ZZ,RXX,RYY,RZZ

```
            if len(params) == 1:
                if any(n >= circuit.num_qubits for n in params):
                    print(f"[Dealer] Card numbers must be less than {circuit.num_qubits}")
                    return None

                if   gate == "H": circuit.h(params[0])
                elif gate == "S": circuit.s(params[0])
                elif gate == "T": circuit.t(params[0])
                elif gate == "Z": circuit.z(params[0])
                else:
                    print(f"[Dealer] The 1-qubit move '{gate}' isn't recognized at this table.")
                    return None

                            …………

                                phase = self.degrees_to_radians(params[0])

                                if   gate == "RXX": circuit.rxx(phase, params[1], params[2])
                                elif gate == "RYY": circuit.ryy(phase, params[1], params[2])
                                elif gate == "RZZ": circuit.rzz(phase, params[1], params[2])
                                else:
                                    print(f"[Dealer] The 3-qubit move '{gate}' isn't recognized at this table.")
                                    return None
```

接下来这道题对于参数进行了检查：第一个检查是这个参数不能为0，包括我们的角度，和作用的门的index。

这个检查可以绕过，并且需要绕过，因为我们可能会对0号线路进行一些操作，绕过原因是因为python的数组索引可以用负数来倒数，比如这道题一共两条量子电路，-2为0就是倒数第二个，-1为1倒数第一个。

```
            if any(p == 0 for p in params):
                print("[Dealer] Hey, don't tamper with the house card — that's forbidden.")
                return None
```

第二个检查是对于三个参数的门，例如RXX，后两个参数即为门的index不能是一个门，也就是不能RXX(....,1,1)

这个检查不用绕过，因为我们本来用这种门也不会让两个index一样。

```
                if params[1] == params[2]:
                    print("[Dealer] Control and target cards must be different.")
                    return None
```

## **validate\_entropy**

这个代码是对于线路0进行测量，验证是不是随机分布的，验证方法为测量很多次，然后统计1和0出现的概率是不是50%

```
    def validate_entropy(self, base_circuit, shots = 100_000):
        circuit = base_circuit.copy()

        circuit.add_register(ClassicalRegister(1))

        circuit.measure(0, 0)

        compiled = transpile(circuit, self.backend)
        results = self.backend.run(compiled, shots = shots).result()
        counts = results.get_counts()

        binomial_test = binomtest(counts.get('0', 0), n = shots, p = 0.5, alternative = 'two-sided')

        if binomial_test.pvalue < 0.01:
            return False

        return True
```

## extract\_numbers

这里是memory是每次测量的结果，这个函数是把测量的结果每6个当作一个数字，并且每次测量是两条线路0和1，他把0号线路作为lotto，把1号线路作为test。然后每6个二进制数字变成一个十进制数字并且模42+1。

```
    def extract_numbers(self, memory):
        print(memory)
        lotto_numbers   = []
        testing_numbers = []

        for i in range(0, len(memory), 6):
            bits = memory[i : i + 6]

            lotto_number   = ""
            testing_number = ""

            for testing_bit, lotto_bit in bits:
                lotto_number   += str(lotto_bit)
                testing_number += str(testing_bit)
            lotto_number   = int(lotto_number,   2) % 42 + 1
            testing_number = int(testing_number, 2) % 42 + 1

            lotto_numbers.append(lotto_number)
            testing_numbers.append(testing_number)

        return lotto_numbers, testing_numbers
```

## run\_lotto

接下来是跑我们地电路，跑36次每次测量，并且0号线路要满足之前分布条件的函数的分布。之后因为每6个数字为一组，所以我们的test有6个十进制数字，lotto也有6个十进制数字。

```
    def run_lotto(self, instructions, shots = 36):
        circuit = self.generate_circuit(instructions)

        if not circuit:
            return None

        if not self.validate_entropy(circuit):
            print("[Dealer] The draw fizzles... not enough quantum energy in your play.")
            return None

        circuit.measure_all()
        print(circuit)

        compiled = transpile(circuit, self.backend)
        results = self.backend.run(compiled, shots = shots, memory = True).result()

        return self.extract_numbers(results.get_memory())
```

## main

这里还是老样子让我们给系统电路门，接下来是运行电路，给我们展示test线路的6个数字，让我猜测lotto的六个数字，如果猜对了就能获得flag。

```
def main():
    print("""
        ╔═════════════════════╗
        ║ ⚛ Welcome to the QLotto table ⚛  ║
        ╠═════════════════════╣
        ║ Minimum bet :  100,000 credits   ║
        ║ Provider    :  Qubitrix™     ║
        ╚═════════════════════╝
    """)

    lotto = QuantumLotto()

    instructions = input("[Dealer] Place your quantum moves : ")

    numbers = lotto.run_lotto(instructions)

    if not numbers:
        return

    lotto_numbers, testing_numbers = numbers

    if lotto_numbers == testing_numbers:
        print("[Dealer] Trying to mirror the house's numbers, are we?")
        return

    print(f"[Dealer] Your draws are: {testing_numbers}")

    guess_numbers = input("[Dealer] Place your six bets on the table : ")

    try:
        guess_numbers = [ int(n) for n in guess_numbers.split(",") ]
    except:
        print("[Dealer] Your wagers must be integers.")
        return

    if len(guess_numbers) != 6 or any(n < 1 or n > 42 for n in guess_numbers):
        print("[Dealer] Place six bets on the table, numbered 1 through 42.")
        return

    if guess_numbers == lotto_numbers:
        print("The table erupts in chaos — you've cracked the QLotto!")
        print(f"[Dealer] Your jackpot:")
    else:
        print(f"[Dealer] Oh, that's a shame, the numbers were {lotto_numbers}")
```

#

**02**

**量子计算相关知识**

H,X,CNOT门上篇文章讲过了，这里讲新的RXX门，也是本题的重点

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2YglSxhPp9Qav7WvPt2Iu36TV2upsb9HnZVIEJ8X8GKD123gstxPqicB3P9icT1qibOP0XW3kT9ADL4bswzbWNaP1VslzfkmsnMg/640?wx_fmt=other&from=appmsg)

这个门可以让两条线路陷入纠缠，RYY和RZZ类似，本题目不用先不讲解。

这里可以尝试给角度theta带入几个特殊值来看看都是啥：

theta为0：

和I是一样的，没有变化

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2zyCRkD3luNCYAhB7U0Il7fjsse6FYMeYribY88my2hPw4ia2RscmTqwclkz8jbDqibT2DvFYv4icyDBdFViaFoia1KjpTDMibnibMiaZQ/640?wx_fmt=other&from=appmsg)![]()

theta为pi/2：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3icdibiaFkz2YW6c009aOfFicC5j7iccib4GDTaNbJhRjJFtmo5AianuDY1sGwiaSiaV9UdXdciaOx08GiaXo2GQK9DrmRb6KaGXNDcS43U0/640?wx_fmt=other&from=appmsg)![]()

作用后效果：

让两条线路陷入纠缠，有相同相反的，如果两条线路一样，那么会进入相同的纠缠，即为0号为0时1号也为0，观测一个线路坍缩后可直接推另一个，比如观测0号为0，就可以知道1号一定为0，因为整体坍缩到了00态，11的可能性无线趋于0。

同理，如果两个线路初始情况不一样，一个0一个1，那也会陷入相反的叠加，观测一个线路坍缩后可直接推另一个，比如观测0号为0，就可以知道1号一定为1，因为这个是相反的并且整体坍缩到了01态，10的可能性...