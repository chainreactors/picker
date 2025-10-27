---
title: Killing Filecoin nodes
url: https://blog.trailofbits.com/2024/11/13/killing-filecoin-nodes/
source: Trail of Bits Blog
date: 2024-11-14
fetch_date: 2025-10-06T19:17:13.299444
---

# Killing Filecoin nodes

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Killing Filecoin nodes

Simone Monica

November 13, 2024

[blockchain](/categories/blockchain/), [vulnerability-disclosure](/categories/vulnerability-disclosure/)

In January, we identified and reported a vulnerability in the Lotus and Venus clients of the Filecoin network that allowed an attacker to remotely crash a node and trigger a denial of service. This issue is caused by an incorrect validation of an index, resulting in an index out-of-range panic.

The vulnerability demonstrates an insecure practice we often observe in our audits of blockchain nodes: the dangers of using signed integers. This blog post details the issue we found, how we fixed it, and why you should use unsigned integers wherever possible to prevent similar problems in your codebase. Both Lotus and Venus fixed the vulnerability by casting to unsigned integers.

## How Filecoin works

Filecoin is a network that allows storing and retrieving files, and it is built on the IPFS protocol. Filecoin is a chain of tipsets where a tipset is a set of blocks with the same height and parent tipset. There exist three major clients: [Lotus](https://github.com/filecoin-project/lotus), the official implementation in Go; [Venus](https://github.com/filecoin-project/venus), another implementation in Go, which has some part of the codebase shared with Lotus; and [Forest](https://github.com/ChainSafe/forest), an experimental implementation in Rust. Our vulnerability affects both Lotus and Venus, but for simplicity, we will provide the example for Lotus only.

Lotus has a data structure, `CompactedMessages`, that contains all the messages of a tipset to save space.

```
type CompactedMessages struct {
    Bls         []*types.Message
    BlsIncludes [][]uint64

    Secpk         []*types.SignedMessage
    SecpkIncludes [][]uint64
}
```

[Structure of CompactedMessages](https://github.com/filecoin-project/lotus/blob/924af42947df4b3d0980e3e51aa715485ef67846/chain/exchange/protocol.go#L159-L165)

We will use the message type for Bls (`CompactedMessages`) as a reference; the `Secpk`, which represents a signed message, works the same in the context of our issue. The struct has a `Bls` field containing all of the messages and a `BlsIncludes` field that matches the messages in the `Bls` field to blocks in the tipset. The first index is the block index, and the second is the message index. For example, if we want the message 5 in block 1, we would use the returned value by `BlsIncludes[1][5]` to index the `Bls` slice.

## Exploiting the issue

When processing a response from a peer containing a tipset’s messages, the message index `BlsIncludes` value is incorrectly validated to be in the range of the `Bls` slice.

This issue consists of two parts: an incorrect array’s length validation in `validateCompressedIndices` and the resulting out-of-range access.

### Incorrect array length validation

In the `validateCompressedIndices` function, the message index (unsigned integer) is cast to a signed integer and then validated to be less than the Bls `len`; otherwise, the function returns an error.

```
func (c *client) validateCompressedIndices(chain []*BSTipSet) error {
    resLength := len(chain)
    for tipsetIdx := 0; tipsetIdx < resLength; tipsetIdx++ {
        msgs := chain[tipsetIdx].Messages
        blocksNum := len(chain[tipsetIdx].Blocks)

        if len(msgs.BlsIncludes) != blocksNum {
            return xerrors.Errorf("BlsIncludes (%d) does not match number of blocks (%d)",
                len(msgs.BlsIncludes), blocksNum)
        }

        for blockIdx := 0; blockIdx < blocksNum; blockIdx++ {
            for _, mi := range msgs.BlsIncludes[blockIdx] {
                if int(mi) >= len(msgs.Bls) {
                    return xerrors.Errorf("index in BlsIncludes (%d) exceeds number of messages (%d)",
                        mi, len(msgs.Bls))
                }
            }
                        ...
}
```

[The incorrect index validation](https://github.com/filecoin-project/lotus/blob/924af42947df4b3d0980e3e51aa715485ef67846/chain/exchange/client.go#L271-L305)

However, since the message index is controlled by the peer who sent the message, the peer can bypass the validation by setting the index to a value greater than the signed integer max, causing the index to become negative when it is cast to signed.

### Out-of-range access

There are multiple ways to exploit this incorrect array’s length validation, but let’s focus on the one in `checkMsgMeta`. This function is called during the syncing phase process when a node attempts to obtain all of the tipsets that include a header and message.

When `[checkMsgMeta(ts, cm.Bls, cm.Secpk, cm.BlsIncludes, cm.SecpkIncludes)](https://github.com/filecoin-project/lotus/blob/b0bc4a96320942c0673a3cab08314074edf4b4f9/chain/sync.go#L1128)` is called:

* `cm.Bls / allbmsgs` is the slice of the `CompactedMessages` struct containing the messages
* `cm.BlsIncludes / bmi` contains the indexes to match a specific message in the `Bls` slice.

```
func checkMsgMeta(ts *types.TipSet, allbmsgs []*types.Message, allsmsgs []*types.SignedMessage, bmi, smi [][]uint64) error {
    for bi, b := range ts.Blocks() {
        if msgc := len(bmi[bi]) + len(smi[bi]); msgc > build.BlockMessageLimit {
            return fmt.Errorf("block %q has too many messages (%d)", b.Cid(), msgc)
        }

        var smsgCids []cid.Cid
        for _, m := range smi[bi] {
            smsgCids = append(smsgCids, allsmsgs[m].Cid())
        }

        var bmsgCids []cid.Cid
        for _, m := range bmi[bi] {
            bmsgCids = append(bmsgCids, allbmsgs[m].Cid())
        }

                         ...

    return nil
}
```

[The checkMsgMeta function](https://github.com/filecoin-project/lotus/blob/924af42947df4b3d0980e3e51aa715485ef67846/chain/exchange/protocol.go#L159-L165)

As we saw earlier, the user controls both values. Since the expected length is not correctly validated, it can cause an index out-of-range panic, as shown in the following video:

This lack of validation can also be exploited through the `Hello` protocol, which is executed when two peers meet for the first time. The protocol allows the peers to exchange information about their heaviest tipsets. If the other peer’s tipset is more recent, and the requesting peer does not have it, the latter peer can request it. Similar to syncing, when decompressing the received messages to form a tipset, a panic occurs with an index out of range.

```
// Decompress messages and form full tipsets with them. The headers
// need to have been requested as well.
func (res *validatedResponse) toFullTipSets() []*store.FullTipSet {
    if len(res.tipsets) == 0 || len(res.tipsets) != len(res.messages) {
        // This decompression can only be done if both headers and
        // messages are returned in the response. (The second check
        // is already implied by the guarantees of `validatedResponse`,
        // added here just for completeness.)
        return nil
    }
    ftsList := make([]*store.FullTipSet, len(res.tipsets))
    for tipsetIdx := range res.tipsets {
        fts := &store.FullTipSet{} // FIXME: We should use the `NewFullTipSet` API.
        msgs := res.messages[tipsetIdx]
        for blockIdx, b := range res.tipsets[tipsetIdx].Blocks() {
            fb := &types.FullBlock{
                Header: b,
            }
            for _, mi := range msgs.BlsIncludes[blockIdx] {
                fb.BlsMessages = append(fb.BlsMessages, msgs.Bls[mi])
            }
            for _, mi := range msgs.SecpkIncludes[blockIdx] {
                fb.SecpkMessages = append(fb.SecpkMessages, msgs.Secpk[mi])
            }

            fts.Blocks = append(fts.Blocks, fb)
        }
        ftsList[tipsetIdx] = fts
    }
    return ftsList
}
```

[Index out of range](https://github.com/filecoin-project/lotus/blob/b...