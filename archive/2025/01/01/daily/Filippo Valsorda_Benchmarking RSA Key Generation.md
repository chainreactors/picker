---
title: Benchmarking RSA Key Generation
url: https://words.filippo.io/dispatches/rsa-keygen-bench/
source: Filippo Valsorda
date: 2025-01-01
fetch_date: 2025-10-06T20:06:31.875960
---

# Benchmarking RSA Key Generation

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

31 Dec 2024

# Benchmarking RSA Key Generation

RSA key generation is both conceptually simple, and one of the worst implementation tasks of the field of cryptography engineering. Even benchmarking it is tricky, and involves some math: here’s how we generated a stable but representative “average case” instead of using the ordinary statistical approach.

## RSA key generation

Say you want to generate a 2048-bit RSA key. The idea is that you generate random 1024-bit numbers until you find two that are prime, you call them *p* and *q*, and compute *N = p × q* and *d = 65537⁻¹ mod φ(N)*[1](#fn:lcm) (and then [some more stuff](https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29#Using_the_Chinese_remainder_algorithm) to make operations faster, but you could stop there). The computation of *d* is where the RSA magic lies, but today we are focusing on the first part.

There is almost nothing special to selecting prime candidates. You draw an appropriately sized random number from a CSPRNG, and to avoid wasting time, you set the least significant bit and the two most significant bits: large even numbers are not prime, and setting the top two guarantees *N* won’t come out too small.

Checking if a number *x* is prime is generally done with the [Miller-Rabin test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)[2](#fn:lucas), a probabilistic algorithm where you pick a “base” and use it to run some computations on *x*. It will either conclusively prove *x* is composite (i.e. not prime), or fail to do so. Figuring out how many Miller-Rabin tests you need to run is surprisingly difficult: initially you will learn the probability of a test failing for a composite is 1/4, which suggests you need 40 rounds to reach 2⁻⁸⁰; then you learn that’s only the upper bound for worst-case values of *x*,[3](#fn:adv) while random values have a much much lower chance of failure; eventually you also realize that it doesn’t matter that much because you only run all the iterations on the prime, while most composites are rejected in the first iteration. Anyway, [BoringSSL has a table](https://cs.opensource.google/boringssl/boringssl/%2B/master%3Acrypto/fipsmodule/bn/prime.c.inc;l=208-283;drc=3a138e43) and we’ll want 5 Miller-Rabin tests with random bases for a 1024-bit prime.

Miller-Rabin is kinda slow though, and most numbers have small divisors, so it’s usually more efficient to quickly reject those by doing “trial divisions” or a GCD with the first handful of primes. The first few dozens are usually a major win, but using more and more primes has diminishing returns.

There are [a million](https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29#Faulty_key_generation) and [one](https://crypto.stanford.edu/~dabo/abstracts/RSAattack-survey.html) things that can go wrong, but interestingly enough you have to go out of your way to get them wrong: if generating large candidates fully at random, all those cases have cryptographically negligible chance.

To recap, to generate an RSA key you generate two primes. To generate a prime you pick random numbers, try to rule them out with trial divisions, and then do a few Miller-Rabin tests on them.

## Benchmarking it

Now, how are we supposed to benchmark that? Luck will drastically affect runtime: you’re essentially benchmarking a lottery. While debugging a performance regression [Russ Cox ran hundreds of measurements](https://github.com/golang/go/issues/70644#issuecomment-2524062990) and still got some noisy and in some places suspect results. It’s also not fast enough that you can run millions of measurements and let things average out.

One might be tempted to normalize the measurements by dividing the runtime by the number of candidates tested, but this unevenly dilutes all the final computations, and is still perturbed by how many candidates are caught by trial division and how many proceed to the Miller-Rabin tests. Similarly, benchmarking Miller-Rabin in isolation ignores the final computations, and doesn’t measure the impact of trial divisions.

What we can do is **use math to figure out how an *average* representative sequence of candidates looks like** and benchmark that. Since the key generation process is repeatable,[4](#fn:det) we can pre-generate a golden sequence of candidates, and even share it across implementations to benchmark apples to apples.

### Generating an average sequence

First, we need to figure out how many composites we should expect on average before each prime. The [prime-counting function approximation](https://en.wikipedia.org/wiki/Prime-counting_function) tells us there are *Li(x)* primes less than *x*, which [works out](https://www.wolframalpha.com/input?i=1+%2F+%28Li%282%5E1024%29+%2F+2%5E1024+*+2%29)[5](#fn:monte) to one prime every 354 odd integers of 1024 bits.

Then, we normalize the small divisors of the composites. A random number has a *1/p* chance of being divisible by *p*, and based on that we can calculate how many composites divisible by the first n primes we’d expect to encounter before a prime. For example, we’d expect 33% of numbers to be divisible by 3, 46% to be divisible by 3 or 5, 69% of numbers to be divisible by one of the first 10 primes, 80% to be divisible by one of the first 50 primes, [and so on](https://gist.github.com/FiloSottile/6a533767fff4d7812fcaffe4be7972c3). Flipping that around, we make 118 of our 353 composites divisible by 3, 47 divisible by 5 but not by 3, 27 divisible by 7 but not by 3 or 5, and so on. This will make the number of successful trial divisions representative, and will even let us do comparative benchmarks between different trial division thresholds without regenerating the inputs.

Beyond setting the top and bottom bits like [keygen will](https://github.com/golang/go/blob/4b652e9f5f5c0793f2e41cd2876bce5a241b2c95/src/crypto/internal/fips140/rsa/keygen.go#L109-L121), we also unset the second-least significant bit and set the third-least significant bit of each candidate to normalize the number of iterations of the inner loop of Miller-Rabin, which depends on the trailing zeroes of *x-1*.

We don’t need to worry about composites failing Miller-Rabin tests: if 5 tests are enough to get to 2⁻¹¹² then one test fails with at most 2⁻²² chance, which is not cryptographically negligible but will not show up in benchmarks. Similarly, we don’t need to worry about *e* not being invertible modulo *φ(N)*: we use 65537 as *e*, which is prime, so only 1/65537 numbers aren’t coprime with it.

### Script, vectors, and results

The result is remarkably stable and should be representative both in terms of absolute runtime and in terms of CPU time spent in different functions, allowing meaningful profiling. Generating 20 random average traces and benchmarking them yields variance of less than 1%.

You can see it in use in [this Go standard library code review](https://go.dev/cl/639335). The script to generate the traces, as well as ten ready to use traces are [available in CCTV](https://c2sp.org/CCTV/keygen) and you’re welcome to use them to benchmark your implementations!

If you got this far, you might also want to follow me on Bluesky at [@filippo.abyssdomain.expert](https://bsky.app/profile/filippo.abyssdomain.expert) or on Mastodon at [@filippo@abyssdomain.expert](https://abyssdomain.expert/%40filippo).

## The picture

One day a friend was driving me to the SFO airport from Redwood Park and we were late. Like, flight begins boarding in a few minutes late. But then we came up to this view, and had to stop to take it in. The people in the other car had set out a little camping chair to watch the sun set over the clouds below. I have an incredible video of driving down into the clouds. Made the flight!

![A fiery orange sunset, pictured from the side of the road. The valley below is filled with a sea of white clouds.](https://asset...