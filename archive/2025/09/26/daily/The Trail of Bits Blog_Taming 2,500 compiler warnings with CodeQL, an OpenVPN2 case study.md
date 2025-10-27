---
title: Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study
url: https://blog.trailofbits.com/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/
source: The Trail of Bits Blog
date: 2025-09-26
fetch_date: 2025-10-02T20:42:39.555790
---

# Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study

[Paweł Płatek](https://github.com/GrosQuildu), Jay Little

September 25, 2025

[codeql](/categories/codeql/), [c/c++](/categories/c/c%2B%2B/), [static-analysis](/categories/static-analysis/)

Page content

* [Why compiler warnings aren’t enough](#why-compiler-warnings-arent-enough)
* [When conversions matter for security](#when-conversions-matter-for-security)
* [Building a practical CodeQL query](#building-a-practical-codeql-query)
  + [Step 0: Learn from existing CodeQL queries](#step-0-learn-from-existing-codeql-queries)
  + [Step 1: Find all problematic conversions (7,000+ findings)](#step-1-find-all-problematic-conversions-7000-findings)
  + [Step 2: Eliminate provably safe constants (1,017 findings)](#step-2-eliminate-provably-safe-constants-1017-findings)
  + [Step 3: Apply range analysis (435 findings)](#step-3-apply-range-analysis-435-findings)
  + [Step 4: Model codebase-specific knowledge (254 findings)](#step-4-model-codebase-specific-knowledge-254-findings)
  + [Step 5: Focus on user-controlled inputs (20 findings)](#step-5-focus-on-user-controlled-inputs-20-findings)
* [Securing your code against silent failures](#securing-your-code-against-silent-failures)

Why are implicit integer conversions a problem in C?

```
if (-7 > sizeof(int)) {
    puts("That's why.");
}
```

During our [security review of OpenVPN2](https://github.com/trailofbits/publications/blob/master/reviews/2022-12-openvpn-openvpn2-securityreview.pdf), we faced a daunting challenge: which of the about 2,500 implicit conversions compiler warnings could actually lead to a vulnerability? To answer this, we created a new CodeQL query that reduced the number of flagged implicit conversions to just 20. Here is how we built the query, what we learned, and how you can run the queries on your code. Our [query is available on GitHub](https://github.com/trailofbits/codeql-queries/blob/18bceaadb084390e31f313eff4d061d91199bf4c/cpp/src/security/UnsafeImplicitConversions/UnsafeImplicitConversions.ql), and you can dig deeper into the details in our [full case study paper](https://github.com/trailofbits/publications/blob/master/reports/detecting-implicit-conversions-in-openvpn2-using-codeql-casestudy.pdf).

## Why compiler warnings aren’t enough

Modern compilers detect implicit conversions with flags like `-Wconversion`, but can generate a massive number of warnings because they do not distinguish between which are benign and which are dangerous for security purposes. When we compiled OpenVPN2 with conversion detection flags, we found thousands of warnings:

* GCC 14.2.0: 2,698 reported warnings with `-Wconversion -Wsign-conversion -Wsign-compare`
* Clang 19.1.7: 2,422 reported warnings with `-Wsign-compare -Wsign-conversion -Wimplicit-int-conversion -Wshorten-64-to-32`

Manual review of 2,500+ findings is impractical, and most warnings highlight benign conversions. The challenge isn’t identifying conversions—it’s determining which ones introduce security vulnerabilities.

## When conversions matter for security

C’s relaxed type system allows for implicit conversions, which is when the compiler automatically changes the type of a variable to make code compile. Not all conversions are problematic, but this behavior creates space for vulnerabilities. One problematic case is when the result of the conversion is used to alter data. To better understand the ways in which data alteration can be problematic, we have broken it down into three categories: truncation, reinterpretation, and widening.

Here is a concise example of each (for more details, check out the [full paper](https://github.com/trailofbits/publications/blob/master/reports/detecting-implicit-conversions-in-openvpn2-using-codeql-casestudy.pdf)):

```
unsigned int x = 0x80000000;

unsigned char a = x;  // truncation
int b = x;  // reinterpretation
uint64_t c = b;  // widening
```

The examples above were all altered via the same type of conversion: [conversion as if by assignment](https://en.cppreference.com/w/c/language/conversion.html#Conversion_as_if_by_assignment). There are two other types of conversions that C programmers often encounter.

Usual arithmetic conversion occurs when variables of different types are operated on and reconciled:

```
unsigned short header_size = 0x13;
int offset = 0x37;
return header_size + offset;  // usual arithmetic conversion
```

Integer promotions happen when unary bitwise, arithmetic, or shift operations happen on a single variable:

```
uint8_t val = 0x13;
int val2 = (~val) >> 3;  // integer promotion
```

By combining the conversion types with the data alteration types mentioned above, we can create a table to clarify which implicit conversions we should further analyze for possible security issues.

|  | Truncation | Reinterpretation | Widening |
| --- | --- | --- | --- |
| As if by assignment | Possible | Possible | Possible |
| Integer promotions | Not possible | Not possible | Possible |
| Usual arithmetic conversions | Not possible | Possible | Possible |

## Building a practical CodeQL query

Back to our security review of OpenVPN2, where we encountered more than 2,500 compiler warnings flagging implicit conversions. Rather than manually reviewing the thousands of warnings, we built a CodeQL query through iterative refinement. Each step improved the query to eliminate classes of false positives while preserving the semantics we cared about for security purposes.

### Step 0: Learn from existing CodeQL queries

Before writing a new query, we wanted to review existing queries that may be relevant or useful. We found three queries, but like Goldilocks, we found that none were a match for what we wanted. Each was either too noisy or checked only a subset of conversions.

* `cpp/conversion-changes-sign`: 988 findings. It detects only implicit unsigned-to-signed integer conversions and only filters out conversions with `const` values.
* `cpp/jsf/av-rule-180`: 6,750 findings. It detects only up to 32-bit types and does not report widening-related issues.
* `cpp/sign-conversion-pointer-arithmetic`: 1 finding. It checks only when type conversions are used for pointer arithmetic. It also covers explicit conversions.

### Step 1: Find all problematic conversions (7,000+ findings)

Our initial query found every implicit integer conversion and returned over 7,000 results in the OpenVPN2 codebase:

```
import cpp

from IntegralConversion cast, IntegralType fromType, IntegralType toType
where
    cast.isImplicit()
    and fromType = cast.getExpr().getExplicitlyConverted().getUnspecifiedType()
    and toType = cast.getUnspecifiedType()
    and fromType != toType
    and not toType instanceof BoolType

select cast, "Implicit cast from " + fromType + " to " + toType
```

This was expectedly broad, so we then updated it to filter the cases we were actually interested in, cutting the results to 5,725:

```
and (
    // truncation
    fromType.getSize() > toType.getSize()
    or
    // reinterpretation
    (
        fromType.getSize() = toType.getSize()
        and
        (
            (fromType.isUnsigned() and toType.isSigned())
            or
            (fromType.isSigned() and toType.isUnsigned())
        )
    )
    or
    // widening
    (
        fromType.getSize() < toType.getSize()
        and
        (
            (fromType.isSigned() and toType.isUnsigned())
            or
            // unsafe promotion
            exists(ComplementExpr complement |
                complement.getOperand().getConversion*() = cast
            )
        )
    )
)

and not (
    // skip conversions in arithmetic operations
    fromType.getSize() <= toType.getSize() // should always hold
    and exists(BinaryArithmeticOperation arithmetic |
        (arithmetic instanceof AddExpr or arithmetic instanceof SubE...