---
title: Tp-Link Router Deep Research
url: https://r0keb.github.io/posts/Tp-Link-Router-Deep-Research/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-13
fetch_date: 2026-01-14T03:35:45.266616
---

# Tp-Link Router Deep Research

[![avatar](/imgs/general/blogPic11.jpg)](/) [r0keb](/)

Diving into low-level computing and systems.

* [HOME](/) * [CATEGORIES](/categories/) * [TAGS](/tags/) * [ARCHIVES](/archives/) * [ABOUT](/about/)

[Home](/)  Tp-Link Router Deep Research

Post

       Cancel

# Tp-Link Router Deep Research

Posted  Nov 15, 2025    Updated  Nov 15, 2025

By  *[r0keb](https://twitter.com/r0keb)*

*85 min* read

Tp-Link Router Deep Research

 Contents

Tp-Link Router Deep Research

Good morning! In this blog I would like to delve into hardware hacking and start expanding my learning.

To begin, in today’s blog we go from 0 (sealed router) to reversing the u-boot by physically extracting the firmware as well as analyzing internal binaries and potential vulnerabilities.

The target is an old router which is one of the most purchased on Amazon (my version is older than the current one, I bought it second-hand):

# Target - **TL-WR841N**

This is the router itself, as I mentioned it is not the latest range but an earlier version:

[![](/imgs/blog/10TpLinkRouterResearch/20251110184021.png)](/imgs/blog/10TpLinkRouterResearch/20251110184021.png)

This is the back:

[![](/imgs/blog/10TpLinkRouterResearch/20251110184127.png)](/imgs/blog/10TpLinkRouterResearch/20251110184127.png)

If we look closely we can see both the model and the serial number:

[![](/imgs/blog/10TpLinkRouterResearch/20251110184337.png)](/imgs/blog/10TpLinkRouterResearch/20251110184337.png)

## Footprinting

Now we can open it and start looking at the internal components and the SoC:

[![](/imgs/blog/10TpLinkRouterResearch/20251110184712.png)](/imgs/blog/10TpLinkRouterResearch/20251110184712.png)

If we zoom in more…

[![](/imgs/blog/10TpLinkRouterResearch/20251110190053.png)](/imgs/blog/10TpLinkRouterResearch/20251110190053.png)

For now there are two visible components, the RAM (rectangular) and the CPU (square).

Here we have the RAM which is not very important for our objective but it is always important to record the serial number. The more information the better tho.

[![](/imgs/blog/10TpLinkRouterResearch/20251110185839.png)](/imgs/blog/10TpLinkRouterResearch/20251110185839.png)

The other visible component is the CPU, in this case Mediatek:

[![](/imgs/blog/10TpLinkRouterResearch/20251110190217.png)](/imgs/blog/10TpLinkRouterResearch/20251110190217.png)

We have a Mediatek **`MT7628NN`**, which if we check the datasheet:

[![](/imgs/blog/10TpLinkRouterResearch/20251111220955.png)](/imgs/blog/10TpLinkRouterResearch/20251111220955.png)

We obtain useful information but nothing groundbreaking.

If we look at the back of the chip, we will see that it has a flash memory, responsible for loading the operating system:

[![](/imgs/blog/10TpLinkRouterResearch/20251111221227.png)](/imgs/blog/10TpLinkRouterResearch/20251111221227.png)

if we zoom in we will see that it is the model **`25Q64CS1G`**:

[![](/imgs/blog/10TpLinkRouterResearch/20251111221321.png)](/imgs/blog/10TpLinkRouterResearch/20251111221321.png)

We will leave this chip for later.

Looking at the router’s physical interfaces we find what could be a `UART`:

[![](/imgs/blog/10TpLinkRouterResearch/20251111223617.png)](/imgs/blog/10TpLinkRouterResearch/20251111223617.png)

The first thing is to make sure which one is the **GND** with the multimeter. In this case it is marked on the board but I don’t like to trust that completely.

[![](/imgs/blog/10TpLinkRouterResearch/20251111223747.png)](/imgs/blog/10TpLinkRouterResearch/20251111223747.png)

The other probe of the multimeter we would place on something we know is a **GND**, such as a conductor of one of the router’s connectors, in my case I put it here:

[![](/imgs/blog/10TpLinkRouterResearch/20251111224326.png)](/imgs/blog/10TpLinkRouterResearch/20251111224326.png)

By testing with the multimeter we can observe how it indeed matches the chip’s `rx` and `tx` of the UART protocol. On the `rx` we see information activity when we power on the router, however on the `tx` we don’t see anything.

### Uart Protocol

UART or *Universal Asynchronous Receiver (Rx) Transmitter (Tx)* is a serial communication protocol between devices. It uses asynchronous communication which means there is no dedicated clock signal on the data line; instead the transmitter and receiver agree on a baud rate (9600 bps, 19200 bps, 38400 bps, 57600 bps, 115200 bps, 230400 bps, 460800 bps, 921600 bps, 1000000 bps, 1500000 bps) and synchronize from the start bit. Being serial, the bits are sent one after another over a single data line. Data can also be sent and received simultaneously.

[![](/imgs/blog/10TpLinkRouterResearch/20251112121924.png)](/imgs/blog/10TpLinkRouterResearch/20251112121924.png)

here we can see a diagram ([resource](https://en.wikipedia.org/wiki/File%3AUART_block_diagram.svg)) of UART to make it clearer:

[![](/imgs/blog/10TpLinkRouterResearch/20251112122018.png)](/imgs/blog/10TpLinkRouterResearch/20251112122018.png)

When establishing device-to-device communication over UART it is important to connect Ground to Ground, `tx` to `rx` and vice versa. The following [image](https://www.secureideas.com/blog/hardware-hacking-interfacing-to-uart-with-your-computer) explains it:

[![](/imgs/blog/10TpLinkRouterResearch/20251112122210.png)](/imgs/blog/10TpLinkRouterResearch/20251112122210.png)

## Communication

Now that we understand the UART protocol, we will proceed to connect. for that we can use a static mechanical arm which I don’t have, or solder.

[![](/imgs/blog/10TpLinkRouterResearch/20251112123500.png)](/imgs/blog/10TpLinkRouterResearch/20251112123500.png)

### Uart: `tx`

now we can connect to the `tx` with our logic analyzer to see the output:

[![](/imgs/blog/10TpLinkRouterResearch/20251112123625.png)](/imgs/blog/10TpLinkRouterResearch/20251112123625.png)

in **Logic 2** we can see the output:

[![](/imgs/blog/10TpLinkRouterResearch/20251015000003.png)](/imgs/blog/10TpLinkRouterResearch/20251015000003.png)

Which would be the following (removing the dirty bytes at the beginning):

```` |  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 50...