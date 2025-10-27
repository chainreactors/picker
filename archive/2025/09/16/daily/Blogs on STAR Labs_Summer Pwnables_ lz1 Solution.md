---
title: Summer Pwnables: lz1 Solution
url: https://starlabs.sg/blog/2025/09-lz1-solution/
source: Blogs on STAR Labs
date: 2025-09-16
fetch_date: 2025-10-02T20:11:30.445090
---

# Summer Pwnables: lz1 Solution

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Summer Pwnables: lz1 Solution

September 15, 2025 · 8 min · Zafir Rasyidi Taufik

Table of Contents

* [TL;DR 🚀](#tldr-)
* [The Technical Deep Dive](#the-technical-deep-dive)
* [Memory Layout: Our Battlefield](#memory-layout-our-battlefield)
* [Exploit](#exploit)
* [Sources and links](#sources-and-links)
* [Writeup by students](#writeup-by-students)

## TL;DR 🚀[#](#tldr-)

We’re turning a simple compression library into a shell delivery service! This writeup exploits a buffer overflow in lz1/lz77 decompression by crafting malicious compressed data that overflows the stack and chains ROP gadgets for code execution.
Ever wondered how a simple file compression tool could hand you the keys to a system? Well, buckle up because we’re about to turn andyherbert’s innocent [lz1 compressor](https://github.com/andyherbert/lz1) into our personal shell delivery service! 🎭

There is a [closed issue on GitHub](https://github.com/andyherbert/lz1/issues/1) where afl-fuzz discovered inputs that crash the program. While it might be possible to use these crashes to find a bug, here’s the thing: if you take a look at the decompression function and understand how lz1 (also known as lz77) works, spotting the buffer overflow isn’t too difficult.

Here’s how lz1 handles compression: it takes repeated bytes and compressed them into “pointers.” Each pointer encode two thing: position and length.

lz1 works by compressing repeated bytes into “pointers”. These pointers encode 2 things, the position, and length. For example, lets compress the string “ABCABCABC”. lz1 notices “ABC” is repeated (how it exactly does this, check the compression code), and compresses it as `ABC<position:3><length:6>`. Notice `<position:3>` doesnt mean index three, but 3 bytes before the current byte, so it points to the the first letter “A”. During decompression, lz1 will start at the position, and repeat `length` bytes. What previously took 6 bytes can be compressed into 2 bytes.

Let’s test your understanding before we dive into the exploit:

> Quiz 1: How does lz1 differentiate normal bytes from pointers?

> Quiz 2: Notice how length in a pointer (6 in our example case) can be longer than the already decompressed data (ABC). How does that make sense? Follow the code, and it should be clear how it works.

> The above example of `ABC<position:3><length:6>` is techincally wrong. It will instead be like `ABC<position:3><length:5>C`. Just lz1 things

## The Technical Deep Dive[#](#the-technical-deep-dive)

In the lz1 code, a pointer is a uint16\_t value\*\*. You may think, we should just use 8 bits (1 byte) for position and 8 bits (1 byte) for length, but actually, we can set the `bit_size` for both position and length. You could totally give position 4 bits and length 12 bits if needed - real compression algorithms do exactly this kind of thing. Sometimes, compressing using lz1 with smaller bitsize for position but larger for length or vice versa can improve the compression. For our case, this will actually help us to exploit it. We will later use 7 bits for position and 9 bits for length.

\*\* Its more like uint24\_t. position, length, and data. Data is just 1 byte of uncompressed data.

Now that we’ve got lz1 figured out, let’s exploit that bug we mentioned. The original code uses malloc to set up both compressed and `uncompressed_text` buffers:

```
uint32_t file_lz77_decompress (char *filename_in, char *filename_out)
{
    .
    .
    .
    compressed_size = fsize(in);
    compressed_text = malloc(compressed_size); // [1] memory for compressed_text
    if(fread(compressed_text, 1, compressed_size, in) != compressed_size)
        return 0;
    fclose(in);

    uncompressed_size = *((uint32_t *) compressed_text);
    uncompressed_text = malloc(uncompressed_size); // [2] memory for uncompressed_text

    if(lz77_decompress(compressed_text, uncompressed_text) != uncompressed_size)
        return 0;
    .
    .
    .
}
```

**Plot twist:** Turns out exploiting this in heap memory was a dead end 🚫, so I swapped it for alloca to get stack allocation instead. Sometimes you gotta pivot!

```
uint32_t lz77_decompress (uint8_t *compressed_text, uint8_t *uncompressed_text)
{
    uint8_t pointer_length_width;
    uint16_t input_pointer, pointer_length, pointer_pos, pointer_length_mask;
    uint32_t compressed_pointer, coding_pos, pointer_offset, uncompressed_size;

    uncompressed_size = *((uint32_t *) compressed_text);
    pointer_length_width = *(compressed_text + 4);
    compressed_pointer = 5;

    pointer_length_mask = pow(2, pointer_length_width) - 1;

    for(coding_pos = 0; coding_pos < uncompressed_size; ++coding_pos) // [1] coding_pos is bounded here
    {
        input_pointer = *((uint16_t *) (compressed_text + compressed_pointer));
        compressed_pointer += 2;
        pointer_pos = input_pointer >> pointer_length_width;
        pointer_length = pointer_pos ? ((input_pointer & pointer_length_mask) + 1) : 0;
        if(pointer_pos)
            for(pointer_offset = coding_pos - pointer_pos; pointer_length > 0; --pointer_length)
                uncompressed_text[coding_pos++] = uncompressed_text[pointer_offset++]; // [2] but unbounded here, so it may be possible to overflow
        *(uncompressed_text + coding_pos) = *(compressed_text + compressed_pointer++);
    }

    return coding_pos;
}
```

Notice that uncompressed\_size is integer value of the first 4 bytes in `compressed_text`. Since we can control this value, it possible to make it less than the size of `length` in a pointer. If we do so, its possible to overflow `uncompressed_text` in [2] in the `lz77_decompress` function above.

**Challenge Checkpoint:** This is a perfect spot to pause and try solving it yourself if you haven’t! The pieces are all there…

## Memory Layout: Our Battlefield[#](#memory-layout-our-battlefield)

In the stack, The memory allocations result in the following structure:

```
┌──────────────────────────────────────┐
│ uncompressed_text [uncompressed_size]│
│        (aligned to 8 bytes)          │
├──────────────────────────────────────┤
│ compressed_text [compressed_size]    │
│        (aligned to 8 bytes)          │
├──────────────────────────────────────┤
│ uncompressed_size (4 bytes)          │
│ compressed_size (4 bytes)            │
│ in FILE (8 bytes)                    │
│ out FILE (8 bytes)                   │
├──────────────────────────────────────┤
│ saved rbp                            │
│ return address                       │
└──────────────────────────────────────┘
```

None of the variables are reordered because the code was compiled without stack protection. Somehow, we need a pointer value that will overflow both compressed\_text, the other variables, and still be a good ROP chain (also notice the code is compiled statically with no PIE, so no leaks are needed and we have lots of gadgets).

With the layout above, it means our payload must *atleast* be longer than compressed\_size, plus a bit more. Since a ROP payload isnt so incredibly compressable 🫤, we need to try to have a short payload. Also, the usable length is sorta inversely correlated to the pointer length we can use. For example, if we use if we use 4 bits for position and 12 bits for length, this means we can overflow a lot, up to 4096 bytes(!) but with only 4 bits for position, we only have 16 bytes for a useful ROP chain, the 4096 byte overflow will just be those 16 bytes repeated over and over which isnt to ...