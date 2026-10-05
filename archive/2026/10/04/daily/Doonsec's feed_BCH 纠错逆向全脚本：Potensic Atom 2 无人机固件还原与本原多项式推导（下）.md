---
title: BCH 纠错逆向全脚本：Potensic Atom 2 无人机固件还原与本原多项式推导（下）
url: https://mp.weixin.qq.com/s/R7F7GJyautAm_lLnsF2dyA
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:56:41.155957
---

# BCH 纠错逆向全脚本：Potensic Atom 2 无人机固件还原与本原多项式推导（下）

# BCH 纠错逆向全脚本：Potensic Atom 2 无人机固件还原与本原多项式推导（下）

原创

黑卷
黑卷

黑卷的IoT攻防日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# BCH 纠错逆向全脚本：Potensic Atom 2 无人机固件还原与本原多项式推导（下）

上篇里，Neodyme 在一台没有 UART/JTAG、固件包又加密的 **Potensic Atom 2** 无人机上热风枪拆下 SPI NAND，用 **ESP32** 读出 544 MiB 镜像，靠多数表决和熵分析摸清 OOB/ECC 布局。随后暴力枚举 14 次本原多项式和取反/位序变换，22 秒爆出 BCH 参数（prim\_poly = 17475，t = 16），纠正 24.7 万个位错误并解出 UBIFS。下篇是作者附录：三份可直接复用的完整脚本，以及 BCH 背后的多项式代数推导。

## 附录

### 最终还原脚本

```
import os.path
import sys

import bchlib

ECC_POLYNOMIAL = 17475
CORRECTION_CAPACITY = 16

USER_DATA_SIZE = 4096
PAGE_SIZE = USER_DATA_SIZE + 256

SLICE_DATA_0 = slice(0, 1028)
SLICE_ECC_0 = slice(1028, 1056)
SLICE_DATA_1 = slice(1056, 2084)
SLICE_ECC_1 = slice(2084, 2112)
SLICE_DATA_2 = slice(2112, 3140)
SLICE_ECC_2 = slice(3140, 3168)
SLICE_DATA_3 = slice(3168, 4096)
SLICE_BB = slice(4096, 4098)
SLICE_DATA_4 = slice(4098, 4182)
SLICE_ECC_3 = slice(4182, 4210)
SLICE_CTRL = slice(4210, 4224)

def parse_flash_page(flash_page: bytes) -> list[tuple[bytearray, bytearray]]:
    """
    Transforms a flash-layout page into a userdata-layout page according to SoC datasheet,
    chunked according to ECC coverage.

    Flash layout:
    data + ecc + data + ecc + data + ecc + data + bb + data + ecc + ctrl

    Userdata layout:
    data + bb + ctrl

    ECC coverage:
    data0 <- ECC0
    data1 <- ECC1
    data2 <- ECC2
    data3+data4+bb+ctrl <- ECC3

    :param flash_page: The 4224 or 4352 byte flash-layout page
    """

    chunks = []

    # three simple chunks of full-sized data + ecc
    chunks.append((flash_page[SLICE_DATA_0], flash_page[SLICE_ECC_0]))
    chunks.append((flash_page[SLICE_DATA_1], flash_page[SLICE_ECC_1]))
    chunks.append((flash_page[SLICE_DATA_2], flash_page[SLICE_ECC_2]))

    # last chunk is fragmented a bit
    userdata_chunk = bytearray()
    userdata_chunk.extend(flash_page[SLICE_DATA_3])
    userdata_chunk.extend(flash_page[SLICE_DATA_4])
    userdata_chunk.extend(flash_page[SLICE_BB])
    userdata_chunk.extend(flash_page[SLICE_CTRL])

    chunks.append((userdata_chunk, flash_page[SLICE_ECC_3]))

    return chunks

def invert(b: bytearray) -> bytearray:
    return bytearray(x ^ 0xFF for x in b)

def fix_chunk_inplace(data: bytearray, ecc: bytearray) -> tuple[int, bytearray]:
    data_transformed = invert(data)
    ecc_transformed = invert(ecc)

    bch = bchlib.BCH(t=CORRECTION_CAPACITY, prim_poly=ECC_POLYNOMIAL, swap_bits=True)
    err_count = bch.decode(data_transformed, ecc_transformed)
    bch.correct(data_transformed, ecc_transformed)

    return err_count, invert(data_transformed)

def main():
    if len(sys.argv) != 2:
        print(
            f"Usage: {sys.argv[0]} full_flash_dump.bin "
            f"(with {PAGE_SIZE} byte pages)",
            file=sys.stderr,
        )
        sys.exit(1)

    total_page_count = os.path.getsize(sys.argv[1]) // PAGE_SIZE
    f_in = open(sys.argv[1], "rb")
    f_out = open("firmware-corrected.bin", "wb")
    page_index = 0

    total_errors = 0
    pages_with_errors = 0
    highest_chunk_error_count = 0
    while (page := f_in.read(PAGE_SIZE)) != b"":
        page_index += 1

        chunks = parse_flash_page(page)

        errors_in_page = 0
        page_corrected = bytearray()
        for i, (data, ecc) in enumerate(chunks):
            err_count, data = fix_chunk_inplace(data, ecc)
            page_corrected.extend(data)
            errors_in_page += err_count
            highest_chunk_error_count = max(highest_chunk_error_count, err_count)

        # cut off BB and CTRL
        f_out.write(page_corrected[:USER_DATA_SIZE])

        print(
            f"[{page_index/total_page_count*100: 4.0f} % ] Extracted page {page_index: 8d} / {total_page_count: 8d} "
            + (
                f"(errors in page: {errors_in_page})"
                if errors_in_page > 0
                else f"(no errors)"
            )
        )
        total_errors += errors_in_page
        if errors_in_page > 0:
            pages_with_errors += 1

    print()
    print(f"======== DONE EXTRACTING")
    print(f"- Total pages: {total_page_count}")
    print(
        f"- Pages with errors: {pages_with_errors} ({pages_with_errors/total_page_count*100:.02f} %)"
    )
    print(
        f"- Total bit errors: {total_errors} ({total_errors / (total_page_count*PAGE_SIZE*8)*100:.04f} %)"
    )
    print(f"- ECC polynomial: {ECC_POLYNOMIAL}")
    print(f"- Correction capacity per chunk: {CORRECTION_CAPACITY}")
    print(
        f"- Highest error count in a single chunk: {highest_chunk_error_count} "
        f"({highest_chunk_error_count/CORRECTION_CAPACITY*100:.02f} %)"
    )

if __name__ == "__main__":
    main()
```

### ECC 爆破脚本

```
import datetime
import itertools
import sys

import bchlib

PAGE_SIZE = 4096 + 256

SLICE_DATA_0 = slice(0, 1028)
SLICE_ECC_0 = slice(1028, 1056)

def reverse_bit_order(b: bytes) -> bytes:
    # credit to this hack at
    # https://graphics.stanford.edu/~seander/bithacks.html#ReverseByteWith64BitsDiv
    return bytes((x * 0x0202020202 & 0x010884422010) % 1023 for x in b)

def reverse_byte_order(b: bytes) -> bytes:
    return b[::-1]

def swap_nibbles(b: bytes) -> bytes:
    return bytes((x >> 4 | x << 4) & 0xFF for x in b)

def invert(b: bytes) -> bytes:
    return bytes(x ^ 0xFF for x in b)

TRANSFORMATIONS = [reverse_bit_order, reverse_byte_order, swap_nibbles, invert]

def all_transformation_sequences():
    """
    :return:  Iterator over all possible subsets and
              orderings of transformations
              (without duplicate transformations).
    """
    for transformation_count in range(0, len(TRANSFORMATIONS)):
        for subset in itertools.combinations(TRANSFORMATIONS, transformation_count):
            for permutation in itertools.permutations(subset):
                yield permutation

def main():
    if len(sys.argv) != 2:
        print(
            f"Usage: {sys.argv[0]} full_flash_dump.bin "
            f"(with {PAGE_SIZE} byte pages)",
            file=sys.stderr,
        )
        sys.exit(1)

    f = open(sys.argv[1], "rb")

    # Both of these work about equally fast
    # primitive_polynomials = list(primitive_binary_polynomials(14))
    primitive_polynomials = list(range(2**14 + 1, 2**15, 2))

    # try all pages
    t0 = datetime.datetime.now()
    page_index = 0
    while (page := f.read(PAGE_SIZE)) != b"":
        print(f"Trying page {page_index}, userdata segment 0")
        page_index += 1

        user_data = page[SLICE_DATA_0]
        known_ecc = page[SLICE_ECC_0]

        # try all primitive polynomials of the correct degree
        for prim_poly in primitive_polynomials:
            try:
                bch = bchlib.BCH(t=16, prim_poly=prim_poly)
            except RuntimeError:
                continue

            # try all combinations of pre-transformations
            for pre_transform_seq in all_transformation_sequences():
                user_data_transformed = user_data
                for pre_transform in pre_transform_seq:
                    user_data_transformed = pre_transform(user_data_transformed)

                ecc = bch.encode(user_data_transformed)

                # try all combinations of post-transformations
                for post_transform_seq in all_transformation_sequences():
                    ecc_transformed = ecc
                    for post_transform in post_transform_seq:
                        ecc_transformed = post_transform(ecc_transformed)

                    if ecc_transformed == known_ecc:
                        print(f"========== ECC parameters found!")
                        print(f"- prim_poly = {prim_poly}")
                        print(f"- pre_transform_seq = {pre_transform_seq}")
                        print(f"- post_transform_seq = {post_transform_seq}")
                        t1 = datetime.datetime.now()
                        print(f"- time to brute force: {t1 - t0}")
                        return

if __name__ == "__main__":
    main()
```

### 本原二元多项式生成...