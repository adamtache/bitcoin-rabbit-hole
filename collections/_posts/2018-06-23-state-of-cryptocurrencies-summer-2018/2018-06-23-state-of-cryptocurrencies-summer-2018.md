---
layout: post
title: State of Cryptocurrencies&#58; Summer 2018
date: 2018-06-23
categories: [Bitcoin, Altcoins]
author: Adam Tache
excerpt: Provides a comprehensive overview of the current state of the cryptocurrency ecosystem as of Summer 2018.
---
This article will provide a comprehensive overview of the current state of the
cryptocurrency ecosystem as of Summer 2018.
<br/><br/>
This includes high-level introductions and discussions on top current and
upcoming projects: Bitcoin, Bitcoin Cash, Chia, Decred, smart contract platforms
(Ethereum, DFINITY, Cosmos, EOS, Filecoin, Rchain, Tezos, Algorand), privacy
coins (Zcash, Monero, Grin/MimbleWimble, Mobilecoin), and stablecoin projects
(Basis, MakerDAO).
<br/><br/>
#### Bitcoin

Overview:
[Bitcoin](https://hackernoon.com/bitcoin-past-and-future-f2feba1f419d) is the
original decentralized, [programmable](https://en.bitcoin.it/wiki/Contract)
cryptocurrency and market leader, and was launched in January 2009 by anonymous
developer(s) using the pseudonym Satoshi Nakamoto. It’s
[primarily](https://hackernoon.com/the-many-faces-of-bitcoin-1c298570d191)
referred to as “sound money” and digital gold; proponents believe it may
eventually transcend the store of value function to become the world reserve
currency and international standard of value, and others view it as a hedge
against adverse macroeconomic scenarios.
<br/><br/>
![](https://cdn-images-1.medium.com/max/1600/1*FxvbHiP2PPr4D3Qho4N8Zw.png)
<br/><br/>
Bitcoin has two main components: miners that solve computational problems using
special-purpose chips through Proof-of-Work, and full nodes that store the
blockchain and relay and validate transactions and blocks that miners build.The
current roadmap emphasizes keeping blocks as small as possible to minimize the
cost of trustlessly verifying blocks created by miners, and using the blockchain
mostly as a settlementlayer for settling any number of transactions from complex
upper-layer systems into one.
<br/><br/>
The Bitcoin community views small blocks as essential to allow all users to
verify transactions and enforce consensus rules, transact more privately, and to
develop a constant back-log of transactions in the mempoolto pay for miner
security through transaction fees as inflation further decreases and leads to
zero newly minted bitcoins per block.
<br/><br/>
Bitcoiners believe the killer-app of blockchain is already here: an
uninflatable, dis-inflationary, censorship-resistant, fixed-supply asset that
can’t be shut down by any governments and operates without any trusted-third
parties on the most [reliable](http://bitcoinuptime.com/) financial system ever
created.They view most
[alt-coin](https://blog.coinbase.com/ethereum-is-the-forefront-of-digital-currency-5300298f6c75)
founders and crypto [VCs](http://www.usv.com/blog/fat-protocols) as
[charlatans](https://nakamotoinstitute.org/mempool/everyones-a-scammer/)
[pumping](https://www.youtube.com/watch?v=2wyC9AEUoYI) digital ‘[fools
gold](https://www.youtube.com/watch?v=NUyCO3FXHS4).’
<br/><br/>
> “Any quantity of money in society is ‘optimal.’ Once a money is established, an
> increase in its supply confers no social benefit.” — [Murray
Rothbard](https://mises.org/library/case-against-fed)

> “SV has lost patience with BTC so moves on to shinier things, but BTC remains
> 99% of the value and a great opportunity for biz to emerge.” — [Steve
Lee](https://twitter.com/moneyball/status/928723161352347648), Former Product
Director at Google

> “The reason most new crypto investors hype the “utility hypothesis” is because
> you can’t get a 75% discount to the Bitcoin pre-sale.” — [Arjun
Balaji](https://twitter.com/arjunblj/status/995343678641246208)

The [Lightning
Network](https://bitcoinmagazine.com/articles/future-bitcoin-what-lightning-could-look/)
(LN) is a peer-to-peer network of trustless payment channels built using Bitcoin
smart contracts, and is one proposed scalability solution to increase
transaction throughput without sacrificing decentralization.Using the
malleability fixfrom a 2017 [update called
SegWit](https://bitcoincore.org/en/2016/01/26/segwit-benefits/), smart contracts
enabling payment channels are now more easily implemented.
<br/><br/>
The LN allows any two users to open payment channels between each other from the
main chain, and [Hashed Timelock
Contracts](https://hackernoon.com/what-are-hashed-timelock-contracts-htlcs-application-in-lightning-network-payment-channels-14437eeb9345)are
used to route payments through other payment channels if the payer and payee
don’t have a direct channel open. The LN is currently in beta with over 2000
nodes and 5000 channels already [open](https://lnmainnet.gaben.win/), and
certain LApps (Lightning Apps) that demonstrate the potential for micro-payments
have been launched, such as [Satoshi’s Place](https://satoshis.place/) and
[Poketoshi](https://poketoshi.com/).
<br/><br/>
Monetary Policy: There will only ever be 21 million bitcoins. The
[supply](https://nakamotoinstitute.org/mempool/the-bitcoin-central-banks-perfect-monetary-policy/)
is dis-inflationary, with the rate of production halving roughly every four
years or 210,000 blocks. Initially, 50 bitcoins were minted each block, and in
2020, this rate will half once again to 6.25 per block, with the last ever
fraction of a new bitcoin expected to be minted in 2140.
<br/><br/>
#### Bitcoin Cash

Overview: Bitcoin Cash is a fork of Bitcoin that emphasizes increasing
throughput on-chain, not off-chain.The [roadmap](https://youtu.be/By0w43NQdiY)
includes steadily increasing the block size roughly every six months, with the
system currently supporting a 32 MB block size. This limit is in comparison to
Bitcoin’s 4 MB [block
weight](https://medium.com/@jimmysong/understanding-segwit-block-size-fd901b87c9d4)
limit, which has resulted in blocks greater than 2 MB.
<br/><br/>
Bitcoin Cash plans to incrementally scale toward unlimited block size, and the
community does not believe in average users being able to afford validating
blocks that miners produce. Proponents emphasize low transaction fees and
encourage on-chain applications for increased utility, and spending and
replacing BCH instead of just [hodling](https://en.wikipedia.org/wiki/Hodl).
Developers are working on supporting on-chain
[tokenization](https://coingeek.com/bitcoin-cash-bch-tokenization-contest-5-million-prize/),
including ICOs and tokenized assets, such as through a [Smart Contract
Engine](https://www.meetup.com/SF-Cryptocurrency-Devs/events/251480208/?_cookie-check=X9YgzmTqpbGeggRK),
as well as [UTXO
commitments](https://www.yours.org/content/first-utxo-commitment-on-testnet-db7bf45bf83d).
<br/><br/>
Monetary Policy: Bitcoin Cash introduced a new difficulty adjustment algorithm
(DAA) through a hard-fork that has resulted in ~90,000 more BCHs in existence in
comparison to BTCs. It is also hard-capped at 21m.
<br/><br/>
#### Chia

Overview: Chia is an upcoming cryptocurrency led by Bram Cohen, the creator of
[BitTorrent](https://www.bittorrent.com/) and former developer at
[MojoNation,](https://www.youtube.com/watch?v=r76WIdqjw4s) and is marketed as a
“better” version of Bitcoin that can be more distributed, more secure, and
greener.
<br/><br/>
The network is composed of full nodes that store the blockchain and relay
transactions and blocks, and farmers (analogous to miners) that use
[Proof-of-Space](https://youtu.be/iqxkO7C-cyk) and
[Proof-of-Time](https://cyber.stanford.edu/sites/default/files/bramcohen.pdf)(Bram
[thinks](https://youtu.be/2Zlcgt8FVz4?t=561) Proof-of-Stake sucks and
establishes a “decentralized centralized system” among the stakeholders, and he
isn’t fond of the bonding and slashing dynamics) to leverage unutilized mass
storage space around the globe instead of solving energy-intensive computational
problems with Proof-of-Work.
<br/><br/>
> “Storage is an over $100 billion a year industry with about 50% utilization”

For proof of space, farmers fill hard-drives with data as proof they allocated
space for a challenge, then search for their best proof of space. Because proofs
of space don’t cost (much) power, the chain would be vulnerable to what are
called “[grinding](https://www.youtube.com/watch?v=2Zlcgt8FVz4)” attacks if only
proof of space was used. For example, a farmer could attempt to re-farm the
entire chain years after genesis, which would theoretically be possible given
the rapid growth in hard-drive capacity in comparison to what would have been
available when the chain started.
<br/><br/>
Chia solves the main grinding attack by alternating between proofs of space
(parallelizable) and proofs of time (sequential). Proof-of-Time is formally
known as Proof-of-Sequential-Work, or [Verifiable Delay
Algorithm](https://eurocrypt.iacr.org/2018/Slides/Tuesday/TrackA/01-04.pdf), and
is a special type of Proof-of-Work that requires a specific number of
iterations, which proves a certain amount of wall-clock time (iterations, not
actual time) has passed.Because VDA proves wall-clock time, a grinder could
never catch up as it would take them two years to re-write two years of history.
<br/><br/>
For each block, farmers are to first work on a challenge for proof of space
which requires taking a hash of the last proof of time and randomly mapping it
to points on [0, 1], then a proof of time which finalizes the block. The “best”
or closest proof of space point to the challenge is to finish first, as the
number of iterations required to finish a proof of time is dependent on the
result of the proof of space.
<br/><br/>
Proof-of-Time outputs a proof, which proves to verifiers that both a certain
amount of time (iterations) was spent generating the output, and that the output
is the right canonical output (the single correct output). VDA will likely
produce a SNARK proof to speed up verification — Chia will
[require](https://youtu.be/UT0LtMLDJiI?t=972) a trusted setup; if a fake setup
is caught, the setup ceremony would have to be re-performed, but funds would not
be at risk and the chain would operate normally with slower verification.
<br/><br/>
Chia will be based on the Bitcoin codebase, have Lightning Network
compatibility, support
[MAST](https://bitcointechtalk.com/what-is-a-bitcoin-merklized-abstract-syntax-tree-mast-33fdf2da5e2f)
and [SegWit](https://bitcoincore.org/en/2016/01/26/segwit-benefits/), and is
planning to start with Bitcoin Script before rolling out an upgradeable
stack-based [Chia Script](https://www.youtube.com/watch?v=Og52VDU-pjc) with
[BLS](https://en.wikipedia.org/wiki/BonehâLynnâShacham) Signatures (instead
of ECDSA or Schnorr) and a new set of op-codes including new flow controls.Bram
noted that he’s a fan of the Bitcoin Core roadmap and wants Chia to never have
to hard-fork.
<br/><br/>
Monetary Policy: [Mostly](https://techcrunch.com/2018/03/28/chia-vs-bitcoin/)
[unknown](https://chia.net/faq/) to the public. Mini pre-IPO. Plans to offer
equity to public, non-accredited investors, potentially distributing part of its
massivepre-mine to share holders. Permanently inflationary.
<br/><br/>
### Decred

*Overview:* Decred is a cryptocurrency known for its hybrid Proof-of-Work and
Proof-of-Stake protocol, and was launched in December 2016. The main
distinguishing factor of Decred is its community-driven on-chain governance
structure, which aims to give shareholders a say in
[consensus](https://blog.decred.org/2016/11/16/Upgrading-Consensus/) and future
hard-forks to the system.
<br/><br/>
> “Decred’s killer feature is good governance, and with good governance, you can
> have any feature you want.” —
[Placeholder](https://www.placeholder.vc/blog/2018/5/12/decred-investment-thesis)

All users are able to participate in governance through a staking process. Users
purchase “tickets” using DCR, which requires locking the value of tokens into a
lottery pool for a certain amount of time (~28 days on average) and paying a
ticket fee to incentivize miners to include the purchase in a block. The [ticket
price](https://blog.decred.org/2017/04/03/A-New-Ticket-Price-Algorithm/) is
determined by an algorithm akin to a staking difficulty.
<br/><br/>
Each block, a lottery runs which picks five random tickets. The winning
stakeholders are required to vote to approve that the block a miner proposed is
valid; three of five votes are required for the state-change to be recorded to
the blockchain, and stakeholders must be online to vote. The tickets expire
after ~142 days or 40,960 blocks; if the stakeholder is never randomly chosen to
vote, they receive back their initial deposit.
<br/><br/>
This staking process is not only used to vote on the validty of miner blocks.
Winning stakeholders are also able to vote on any changes to the system. When a
consensus rule change is proposed for the network, there is a 8064 block long
(~28 days) voting window. If over this time 75% of stakeholder votes and 75% of
hash power signal the change, the hard-fork is approved and users must update
their software to apply the fork.
<br/><br/>
As a reward for voting, each stakeholder receives 6% of the block reward. PoW
miners receive 60%, and the remaining 10% is reserved for a
[development](https://docs.decred.org/getting-started/constitution/#funding)
subsidy. If stakerholders reject a block, the PoW and development rewards are
not paid out.
<br/><br/>
The 2018 Decred
[roadmap](https://blog.decred.org/2018/02/28/2018-Decred-Roadmap/) includes
Lightning Network compatability, a new proposal system called
[Politeia](https://blog.decred.org/2017/10/25/Politeia/) to create a
time-stamped public repository of user proposals, a [decentralized
exchange](https://blog.decred.org/2018/06/05/A-New-Kind-of-DEX/), Decentralized
Autonomous Entities, and scalability improvements.
<br/><br/>
*Monetary Policy:* Decred has a fixed-supply of 21 million coins. The supply
schedule differs from Bitcoin in that the genesis block subsidy started at ~31.2
coins/block, and the subsidy reduces by a factor of 100/101 every ~21.33 days.
There are currently 7.15 million DCR tokens circulating, of which over
[45%](https://dcrstats.com/) is being staked.
<br/><br/>

### Smart Contract Platforms

#### Ethereum

Overview: Ethereum is a virtual computer spearheaded by [Vitalik
Buterin](https://davidgerard.co.uk/blockchain/buterins-quantum-quest/). It aims
to be a “decentralized world computer” by offering a more extensible,
([nearly](https://www.youtube.com/watch?v=cGFOKTm_8zk)) Turing-Complete smart
contract capability in comparison to Bitcoin Script’s Turing-Incomplete smart
contracts. Ethereum did not opt for the
[UTXO](https://www.safaribooksonline.com/library/view/mastering-bitcoin/9781491902639/ch05.html)
model of coins;
[instead](https://github.com/ethereum/wiki/wiki/Design-Rationale#accounts-and-not-utxos),
Ethereum has accounts and contracts with balances. Unlike Bitcoin where all
transactions cost roughly the same for miners to execute, Ethereum contracts
have highly differing levels of complexity in terms of bandwidth, storage, and
computation. For this reason, Ethereum opted for a gas model in which each
transaction is priced depending on a cost per quantity of gas consumed by the
miners to execute contracts. Miners are able to dynamically
[adjust](https://www.etherchain.org/tools/gasLimitVoting) the *gas limit* that
the system supports by a certain factor each block, which is analogous to the
block size in Bitcoin.
<br/><br/>
The network is currently composed of miners, full nodes, and [light
nodes](https://medium.com/zkcapital/a-primer-on-ethereum-blockchain-light-clients-f3cadde49137).
Light nodes rely on full nodes for security and can validate state relevant to
the user by downloading block headers from the longest PoW chain, and full nodes
are mostly composed of go-ethereum (geth) and Parity nodes. These offer full or
“fast/warp” syncing, and pruning modes. A subset of full nodes are fully
archival nodes, which fully validate all miner blocks, execute all contracts,
and store the entire blockchain state. Ethereum offers
[many](https://medium.freecodecamp.org/lets-talk-about-the-ethereum-token-standards-you-need-to-know-8af9fcb7e54b)
token standards:
[ERC-20](https://theethereum.wiki/w/index.php/ERC20_Token_Standard) for platform
tokens and [ERC-721](https://github.com/ethereum/eips/issues/721) for
non-fungible tokens like collectibles being the most prominent.
<br/><br/>
The current [roadmap](https://github.com/ethereum/wiki/wiki/Sharding-roadmap)
for Ethereum includes three fundamental design changes: sharding, a new
consensus protocol called Casper, and replacing the Ethereum Virtual Machine
(EVM) with the eWASM. The
[eWASM](https://paritytech.io/wasm-smart-contract-development/) will allow
developers to write smart contracts using high-level programming languages that
compile down to Wasm(Web Assembly)instead of using Ethereum’s current
JavaScript-like Solidity language.
<br/><br/>
The most significant change coming to Ethereum over the next two years is
[Casper](https://notes.ethereum.org/SCIg8AH5SA-O4C1G1LYZHQ?view)+[Sharding](https://github.com/ethereum/wiki/wiki/Sharding-FAQ),
which is Ethereum’s proposal to (mostly) switch from Proof-of-Work to
Proof-of-Stake (as part of Casper), and break up state of the network into a
bunch of partitions called shards. Each shard would have independent state and
transaction history, and all validators on the network wouldn’t be responsible
for handling all transactions; instead, notaries within each shard would be
responsible for their own shard. Cross-shard transacting and shards of shards
are both possible. There is a
[proposal](https://ethresear.ch/t/pragmatic-signature-aggregation-with-bls/2105)
to integrate BLS Signaturesand zk-STARKs for verification to aid scalability.
<br/><br/>
Casper developers have “[learned to love” weak
subjectivity](https://blog.ethereum.org/2014/11/25/proof-stake-learned-love-weak-subjectivity/)
and aim to simulate the security of PoW through threats of economic penalties
for validators (slashing dishonest actors by taking away deposits) instead of
burning energy. They think it’s possible to design a PoS protocol that is more
secure, decentralized, offers faster block times, finality, and is more flexible
than PoW, which is “limited” by physics.
<br/><br/>
Ethereum has been [highly
criticized](https://medium.com/@jimmysong/crypto-keynesian-lunacy-16bb9193a58)
by Bitcoiners for introducing toxic speculation into the cryptocurrency
ecosystem through ICOs and
[promoting](https://hackernoon.com/sharding-centralizes-ethereum-by-selling-you-scaling-in-disguised-as-scaling-out-266c136fc55d)
increased centralization of validation over time. Vitalik and other Ethereum
developers [do not
believe](https://twitter.com/VitalikButerin/status/873177382164848641) in cheap
fully validating nodes for average users.
<br/><br/>
Ethereum dApps currently have [very few](https://dappradar.com/) DAUs (Daily
Active Users) despite there being tens of thousands of DADs (Daily Active
Developers), of which most are Solidity developers, not protocol developers. The
Ethereum community is much more optimistic; members have noted that most dApps
are not yet launched and that criticizing an early-stage blockchain for lack of
DAU is futile, as they believe DADs is an accurate predictor for future DAUs and
that “killer apps are coming.” They are excited about various current and
upcoming projects, such as
[Plasma](https://www.youtube.com/watch?v=jTc_2tyT_lY), [Plasma
Cash](https://www.youtube.com/watch?v=uyuA11PDDHE), the [Raiden
Network](https://www.youtube.com/watch?v=93qOwUSj4PQ), generalized [state
channels](https://medium.com/spankchain/a-state-channels-adventure-with-counterfactual-rick-part-1-ce68e16252ea),
[off-chain computations](https://www.youtube.com/watch?v=7uQdEBVu8Sk),
sidechains like
[DAppChains](https://medium.com/loom-network/dappchains-scaling-ethereum-dapps-through-sidechains-f99e51fff447),
[lending](https://blog.dharma.io/dharma-an-open-protocol-for-generic-tokenized-debt-agreements-9a4e6a4e6fc0),
[games](https://funfair.io/), [financial
derivatives](https://medium.com/dydxderivatives/introducing-dydx-2d0f0f326fd),
[0x](https://0xproject.com/), and
[more](https://medium.com/loom-network/the-state-of-ethereum-scaling-march-2018-74ac08198a36).
<br/><br/>
Monetary Policy: The exact monetary policy is not currently known. Eventually,
Ethereum is
[expected](https://twitter.com/VitalikButerin/status/879858608091144193) to have
either a 0.5%-2% inflation
[rate](https://blog.ethereum.org/2016/07/27/inflation-transaction-fees-cryptocurrency-monetary-policy/)
per year or a hard-cap of ether. Vitalik recently
[proposed](https://github.com/ethereum/EIPs/issues/960) a hard-cap, but Vlad
Zamfir
[disagreed](https://coinjournal.net/ethereum-vlad-zamfir-ethereum-hard-cap-eip960/),
and the topic is being debated within Ethereum research. Ethereum was originally
launched through an
[ICO](https://blog.ethereum.org/2014/07/22/launching-the-ether-sale/), but was
deemed not a security by the SEC.
<br/><br/>
#### DFINITY

Overview: *DFINITY is an upcoming competitor to Ethereum’s “blockchain
computer” throne aiming to launch Q4 2018. The engineering
[team](https://www.dfinity.org/team) is extremely experienced with distributed
systems and cryptography, and is aiming to build a much more performant,
scalable, and secure decentralized computer that eventually offers unlimited
computational capacity.
<br/><br/>

> In DFINITY the “Code is Law” is contingent upon the decisions of the nervous
> system. The omnipotence of the BNS is highly important. AI is Law.

<br/><br/>
DFINITY is known for its “[Blockchain Nervous
System](https://medium.com/dfinity/the-dfinity-blockchain-nervous-system-a5dd1783288e)”
governance model (liquid democracy) in which a distributed intelligence is to
act as a benevolent superuser for managing and integrating changes to the
protocol. The goals for BNS are to allow for a rapid upgrade process in
comparison to traditional blockchains, be able to adjust economic parameters if
needed (such as number of tokens required for staking deposit), increase the
value of dfinity tokens, and perform mitigation of thefts (in cases such as
Bitcoin’s Mt Gox exchange and Ethereum DAO hacks) without human intervention
using its privileged control over token ownership (including freezing accounts)
and ability to execute arbitrary code.
<br/><br/>
The BNS will be guided by a human market process where constitution-directed
“neurons” can create proposals and vote for changes. Voting power is
proportional to deposits of dfinities to the BNS, and neurons can earn rewards
and autonomously vote by tapping into the directed trust graph of neurons. The
BNS is to analyze the “[moral
authority](https://medium.com/dfinity/the-dfinity-blockchain-nervous-system-a5dd1783288e)”
behind proposals.
<br/><br/>
At a high-level, the DFINITY blockchain is built on top of a decentralized
randomness beacon acting as a Verifiable Random Function (VRF) and verifiable
heartbeat of the system. This allows randomness to be used for both the
consensus process and the application layers. The system is composed of a
network of processes that includes miners and a p2p broadcast network composed
of an unlimited amount of clients with permanent pseudonymous identities. The
broadcast network is organized into random groups, which can send messages to
everyone else. Dfinity is Ethereum compatible; Ethereum code can run on DFINITY.
<br/><br/>
The consensus mechanism is Threshold Relay, where a group is assigned a public
key through a generation method to sign messages using BLS threshold signatures
if a certain threshold of group members agree. The signatures produced are
random numbers using the VRF, which can be used to select a next group. This
threshold process is used for notarizing blocks (time-stamping and proving
publication), which allows for a block time of only a few seconds and finality
after two confirmations or roughly six seconds. It prioritizes consistency over
availability, and eliminates selfish mining and the nothing at stake problem for
its Proof-of-Stake sybil resistance, and will be used to facilitate sharding and
validation towers. Shards act as the storage layer, receive transactions, record
updates to their local state, then pass the transactions to validation towers,
which execute contracts (written in Solidity and high-level languages compiled
to [WASM](https://webassembly.org/)) and validate transactions.
<br/><br/>
Monetary Policy: The majority (52.93%) of the tokens are owned by the DFINITY
foundation, team, and for partnerships. 45.82% of tokens were sold to investors
in a
[pre-sale](https://medium.com/dfinity/announcing-the-dfinity-presale-fundraise-and-public-airdrop-cdea19892ef6).
The remainder (1.25%) were distributed through a community
[airdrop](https://medium.com/dfinity/liftoff-the-dfinity-community-airdrop-is-here-5a11b94a2d03).
<br/><br/>
#### Cosmos

Overview: Cosmos is an upcoming ecosystem marketed as the internet of
blockchains, and will be a network of independent, interoperable blockchains
divided into hubs with zones. The main hub is the Cosmos Hub, which is a
blockchain powered by the Atom staking token. The independent blockchains with
their own tokens are called zones, and there can be any number of hubs with
their own public or private zones. Hubs connect to zones using the IBC
(inter-blockchain communication) protocol, which allows tokens to be sent from
one zone to another. Cosmos is [expected](https://cosmos.network/roadmap) to
launch in 2018 and is said to support thousands of transactions per second (tps)
within its zones.
<br/><br/>
The Cosmos team developed [Tendermint](https://tendermint.com/), which they call
a *general-purpose blockchain consensus engine*, and powers a peer-to-peer
gossip protocol and traditional Byzantine Fault Tolerant (BFT) consensus
protocols, which allow for up to 1/3 of machines to fail.
[Tendermint](https://tendermint.readthedocs.io/en/master/introduction.html#what-is-tendermint)
will power Cosmos’ Proof-of-Stake, and offers developers an
Application-Blockchain [Interface](https://github.com/tendermint/abci) (ABCI) to
write smart contracts in any programming language.
<br/><br/>
![](https://cdn-images-1.medium.com/max/1600/1*_o_LeDb3UKGGzYEUy514BQ.png)
<br/><br/>
Cosmos will have a transactional token for payments, which is currently called
the
[Photon](https://blog.cosmos.network/cosmos-fee-token-introducing-the-photon-8a62b2f51aa),
and is to be rewarded to validators (who bond Atoms) and used to pay fees for
zones that accept it. There’s a proposal to distribute photons to ether holders
through a “[hard
spoon](https://blog.cosmos.network/introducing-the-hard-spoon-4a9288d3f0df)” of
Ethereum, which will create [Ethermint](https://ethermint.zone/), a PoS EVM zone
with mirrored account balances of Ethereum’s.
<br/><br/>
Tendermint
[hosts](https://blog.cosmos.network/consensus-compare-casper-vs-tendermint-6df154ad56ae)
a weakly synchronous round-based voting system where
[validators](https://cosmos.network/validators/faq) bond atoms as collateral,
propose blocks, signal intent, then sign to commit new blocks. It requires 2/3s
of validators to commit to a block, prioritizes consistency over availability,
and allows for 1–3 second finality when fully operational. Tendermint is a
delegated system which only supports 100 validators participating at a time.
[Delegators](https://cosmos.network/resources/delegators) participate in
consensus, police validators, and share revenue with their chosen validators
through a commission rate.
<br/><br/>
Monetary Policy: Cosmos conducted an
[ICO](https://blog.cosmos.network/fundraiser-was-a-resounding-success-bf378b96fe00),
which raised $16m in BTC and ETH for over 60% of the initial atoms for
fundraiser
[participants](https://blog.cosmos.network/atom-supply-and-distribution-b4dd3404ff26).
The
[inflation](https://blog.cosmos.network/understanding-inflation-in-cosmos-622651c83303)
rate of atoms will be dynamically adjusted by the Cosmos Hub to be between 7%
and 21%.
<br/><br/>
#### EOS

Overview: EOS is the latest general purpose, Turing-Complete smart contract
platform to launch, and is [Dan
Larimer](https://decentralize.today/the-ugly-truth-behind-steemit-1a525f5e156)’s
third blockchain. EOS sacrifices decentralization and censorship-reistance for
speed and high throughput, and uses inflation to pay for network security to
enable zero fee payments for users. It uses a BFT Delegated Proof-of-Stake
(dPoS) model — invented by Larimer — for consensus and as part of on-chain
governance. 21 pseudonymous Block Producers (BPs) are voted in by delegates that
hold EOS tokens, and are to abide by the (evolvable) EOS
[constitution](https://twitter.com/NickSzabo4/status/1008974899690463232). The
BPs also host a replicated [storage
service](https://github.com/EOSIO/Documentation/blob/master/EOS.IO Storage.pdf)
using IPFS for token holders.
<br/><br/>
Block time is roughly half a second, finality is achieved within two seconds,
and the platform can supposedly handle thousands of tps. Contracts are compiled
down to WASM, accounts are human-readable usernames, and the platform offers
protocol-level account recovery through account recovery partners.
<br/><br/>
The launch and election process for EOS were notoriously messy; the platform was
plagued with [low voter
turnout](https://twitter.com/spencernoon/status/1007264978393591809) until a
large whale with over 5% of tokens cast a vote, the platform
[crashed](https://eosuptime.com/) for over five hours the first week, and BPs
have already frozen [34](https://www.eosblacklist.com/) user accounts. Despite
the rough launch,
[some](https://multicoin.capital/wp-content/uploads/2018/04/EOS-Analysis-and-Valuation.pdf)
investors are optimistic that the project finds a niche for applications in need
of a high throughput blockchain without sovereign-grade censorship resistance.
[Block.one](https://block.one/) raised over $4b in the EOS ICO, and has over $1b
of ecosystem funds to help the blockchain grow. There are
[dozens](https://usethebitcoin.com/the-complete-list-with-eos-airdrops-in-2018/)
of air-drops planned for EOS token holders.
<br/><br/>
Monetary Policy: Token holders can vote on inflation rates; the default is
currently 5% per year.
<br/><br/>
#### Filecoin

Overview:
[Filecoin](https://cyber.stanford.edu/sites/default/files/filecoin.bpase-2018.compressed.pdf)
is a work-in-progress blockchain that aims to be a decentralized, highly
efficient, and robust storage network (DSN) to challenge traditional cloud
platforms, such as Amazon S3, Google Storage, and Microsoft Azure Cloud Storage.
It aims to scale to ZB and beyond through economic incentives by allowing users
to profit from offering hard-drive space, analogous to Bitcoin scaling security
to over 40 TH/s through incentives for providing hash rate. It will also support
generic smart contracts.
<br/><br/>
Various platforms, such as the upcoming personal operating system and personal
server [Urbit](https://urbit.org/), have identified a lingering problem with the
modern web: all of your personal data is stored on centralized private servers,
and the data is not guaranteed to last forever. Filecoin is built around
[IPFS](https://ipfs.io/), a peer-to-peer distributed web protocol, and plans on
building bridges to provide file storage and retrieval for other networks, such
as to allow Ethereum contracts to use Filecoin, and integration with Bitcoin and
ZCash.
<br/><br/>
Filecoin aims to offer a formally verified protocol and (stateful) smart
contracts using SNARKs, as well as proofs of when data is stored, that data is
still stored, and that participants can actually extract the data.
Proofs-of-Storage, such as Proofs of Replication, Data Possession, and
Retrievability, would allow a prover to prove to a verifier that data is stored
and replicated and for the verifier to retrieve the data from the proofs to
prevent withholdings.
<br/><br/>
Filecoin aims to facilitate storage and retrieval markets with bids and asks
that allow price undercutting and tiers of service within mining; for example,
tiered read access would allow for differing rewards for differing levels of
caching, well-placed (physical) nodes, and for optimized low latency and high
bandwidth nodes. Filecoin plans to launch purely on-chain markets initially and
develop state channels in the future.
<br/><br/>
The network is broken up into *clients* (users) which hire miners to store their
data, *miners*, and a *network* that organizes work, verifies and repairs
corrupted storage using erasure coding (analogous to a RAID array), and rewards
miners enacting correct behavior with Filecoins proportionately to their *power*
metric, which measures how much useful storage miners are providing. Miners
participate in consensus through a “useful” Proof-of-Work algorithm by
generating Proofs-of-Spacetime to allow the network to audit storage offered by
miners overtime, and consensus is to be achieved using rounds of miner elections
where the probability of a miner being elected is proportional to its provided
storage. Proofs-of-Spacetime are added to the chain if a majority of the power
in the network deem them valid.
<br/><br/>
Some are
[skeptical](https://blog.dshr.org/2018/06/the-four-most-expensive-words-in.html)
that Filecoin (and the other blockchain storage networks, such as
[Storj](https://storj.io/storj.pdf) and [Sia](https://sia.tech/)) can compete
with the centralized alternatives due to problems with speed, access control,
reliability, volatility, and the marketplace UI/UX.
<br/><br/>
Monetary Policy: There will be a finite 2 billion Filecoins, with
[70%](https://coinlist.co/assets/index/filecoin_index/Filecoin-Sale-Economics-e3f703f8cd5f644aecd7ae3860ce932064ce014dd60de115d67ff1e9047ffa8e.pdf)
to be mined and released through a
[smoother](https://medium.com/@ryanshea/the-economics-of-filecoin-a8d826774674)
exponential decay curve in comparison to Bitcoin and ZCash. The rest are to be
distributed to investors through an ICO which raised $257m, and to the Filecoin
Foundation and Protocol Labs (the team).
<br/><br/>
#### RChain

Overview: [RChain](https://www.rchain.coop/) is a work-in-progress virtual
computer aiming to be a highly scalable, concurrent, and performant blockchain
offering general-purpose, formally verified, Turing-Complete smart
[contracts](http://rchain-architecture.readthedocs.io/en/latest/contracts/contract-design.html),
and has a democratic [cooperative](https://en.wikipedia.org/wiki/Cooperative)
governance structure. [RChain](https://youtu.be/kojlx2ykRsA) is unique because
its [architecture](http://rchain-architecture.readthedocs.io/en/latest/) is
based on a computational model called
[Rho-Calculus](http://rho.loria.fr/index.html), as opposed to a machine with a
von Neumann architecture like the serialized Ethereum Virtual Machine. RChain
aims to support 40,000–100,000 tps.
<br/><br/>
![](https://cdn-images-1.medium.com/max/1600/1*DeGYDORjOY991dImczUAoQ.png)
<br/><br/>
Rho-Calculus supports 4 C’s: completeness, compositionality (making larger
programs out of smaller programs),
[concurrency](https://en.wikipedia.org/wiki/Concurrency_(computer_science)), and
complexity (being able to measure computations using resources). RChain
contracts are programmed using the concurrent and functional
[Rholang](https://github.com/rchain/rchain/tree/master/rholang) language, which
focuses on message-passing, runs on the Rho Virtual Machine (RhoVM), and is
formally modeled using rho-calculus. Contracts are paid for using the RChain
Phlogiston token (analogous to gas in Ethereum), and the main staking token is
called the RChain Rev.
<br/><br/>
The network is broken up into nodes that each run the RChain
[environment](http://rchain-architecture.readthedocs.io/en/latest/introduction/introduction.html)
and communicate between each other. The RhoVM Execution Environment runs on the
JVM (Java Virtual Machine) and runs multiple RhoVMs on each node; each VM
executes a smart contract, which run concurrently and are multi-threaded.
<br/><br/>
RChain uses a Proof-of-Stake
[protocol](http://rchain-architecture.readthedocs.io/en/latest/execution_model/consensus_protocol.html)
similar to Ethereum’s Casper for Sybil resistance, and sharding (resulting in
multiple parallel and synchronizable blockchains that can communicate over
channels), concurrency, and security come as part of the ρ-calculus model.
<br/><br/>
*Monetary Policy: *RChain raised ~$30m in an ICO. There is a
[fixed](https://etherscan.io/token/tokenholderchart/0x168296bb09e24a88805cb9c33356536b980d3fc5)
supply of 861,185,194 RChain tokens, which are currently ERC-20 but will be 1:1
converted when the blockchain launches. The team owns 30%, 20% were burned, and
the co-op owns ~7%.
<br/><br/>
#### Tezos

Overview: [Tezos](https://tezos.com/) is a
[long-awaited](https://www.wired.com/story/tezos-blockchain-love-story-horror-story/)
blockchain that has been under development since
[2014](https://tezos.com/static/papers/white_paper.pdf), and is aiming to
support formally-verified smart contracts through a stack-based programming
language called [Michelsen](https://www.michelson-lang.com/). It is marketed as
a “self-amending crypto-ledger,” which is a reference to the ability for stake
holders to
“[self-upgrade](https://medium.com/tezos/there-is-no-need-for-hard-forks-86b68165e67d)”
the protocol through an [on-chain
governance](https://www.placeholder.vc/blog/2018/5/12/decred-investment-thesis)
mechanism.
<br/><br/>
In terms of the
[network](https://medium.com/tezos/a-quick-tour-of-the-tezos-code-base-and-the-state-of-its-development-c4e5fcb34b8a),
the main components are:
<br/><br/>
* [Bakers](https://www.youtube.com/watch?v=andKrImAfVE)* *(stakers) that
participate in consensus through a BFT Delegated Proof-of-Stake (dPoS) model by
staking bonds, create and validate blocks when randomly chosen, and are paid
through transaction fees and bonds.
* *Endorsers* (delegates) that are required to safety deposit bonds to get
rewarded, and give powers to another account to bake for them and generate and
sign blocks for them.
* *Nodes *which relay and validate blocks and transactions and store the
blockchain state.
<br/><br/>
Tezos chose not to pursue sharding for
[scaling](https://hackernoon.com/scaling-tezo-8de241dd91bd), and although they
are initially starting with a low gas limit per block, the developers do not
believe in cheap validation for all and want to scale to large block sizes. They
plan to eventually use recursive SNARKs to allow users to sync the blockchain
from scratch and validate it from the genesis block in less than one second; in
order to do this, each block would be a hash of the merkle root of the content
of the block, and a proof that the state transition was valid (similar to
[Coda](https://codaprotocol.com/static/coda-whitepaper-05-10-2018-0.pdf)’s
succint blockchain design).
<br/><br/>
*Monetary Policy: *There is a 5% inflation rate per year with an initial supply
of 763,306,930 tokens, with a
[possibility](https://medium.com/tezos/diff-2014-tezos-2017-tezos-1cb566cca892)
of a future hard-cap.
<br/><br/>
#### Algorand

Overview: *[Algorand](https://www.algorand.com/) is an upcoming project, led by
MIT professor and Turing Award Laueate [Silvio
Micali](https://people.csail.mit.edu/silvio/), that aims to be a highly
scalable, censorship-resistant blockchain that is partition resilient and
achieves block finality in one minute. A new Byzantine Agreement called BA★ is
used to achieve consensus on state transitions, and Proof-of-Stake is employed
for Sybil resistance; users are weighted based on their token ownership, and a
small set of users — called a committee — is chosen to perform each step of the
[protocol](https://medium.com/algorand/algorands-instant-consensus-protocol-e66ac5807e37),
with other users voting on the proposed values.
<br/><br/>
Similarly to DFINITY, [Algorand](https://www.youtube.com/watch?v=_nQE_HAGlmM)
uses a Verifiable Random Function (VRF) to employ randomness within the
protocol, and does so for committee selection. Through a process called
“cryptographic sortition,” each user selects themselves for each committee by
running a lottery, and propagates proof they are selected if they win, as well
as a priority for other users to determine which of potentially multiple blocks
they should accept.
<br/><br/>
Algorand avoids targeted attacks on chosen participants by replacing the
participant at each step, and as long as a 2/3 weight of the token ownership is
honest, the chain has a negligible proability of forking and guarantees of
agreement and consistency. Unlike other PoS protocols, Algorand does not slash
malicious actor deposits if they propose an illicit state for the ledger. There
is also a set of [leaders](https://www.algorand.com/team/) for project
governance.
<br/><br/>
Monetary Policy: Unknown. Upcoming token sale.
<br/><br/>

### Privacy Coins
<br/><br/>
#### Zcash

Overview: Founded by [Zooko](http://twitter.com/zooko) and
[other](https://z.cash/team.html) cryptographers in 2016, Zcash is an
implementation of the
[Zerocash](http://zerocash-project.org/media/pdf/zerocash-extended-20140518.pdf)
protocol. As a privacy-centric cryptocurrency, Zcash is the leader in
zero-knowledge (ZK) cryptography. Zcash is the first blockchain to use zk-SNARKs
(Succinct Non-interactive ARguments of Knowledge, a zero-knowledge proof of
knowledge), which were
[invented](http://zerocash-project.org/media/pdf/zerocash-extended-20140518.pdf)
by scientists on the team. Zcash was built using the Bitcoin codebase, and
required a one-time trusted multi-party computation
[ceremony](https://blog.z.cash/the-design-of-the-ceremony/) to generate public
parameters for SNARKs using
[air-gapped](http://trilema.com/2013/how-to-airgap-a-practical-guide/)
computers.
<br/><br/>
zk-SNARK proofs allow fully encrypted information to be verified by validators
without the validators being able to access the unencrypted data. They
facilitate z-transactions, also known as shielded transactions, where balance
and address data are hidden from the network.The sender of a shielded
transaction constructs a small proof that currently takes up to 40 seconds to
generate but can be verified in a few milliseconds.
<br/><br/>
Zcash also supports non-anonymous t(ransparent)-transactions, which have been
shown to reduce the anonymity of shielded transactions through
[linkability](https://arxiv.org/pdf/1712.01210.pdf). In the future with speed
improvements of zk-SNARK technology, it is expected that the percentage of
shielded transactions will increase from the current ~31.5% usage.
<br/><br/>
<span class="figcaption_hack">Upcoming upgrade called
[Sapling](https://blog.z.cash/cultivating-sapling-faster-zksnarks/) for faster
zk-SNARKs, following [Overwinter](https://z.cash/upgrade/overwinter.html).</span>
<br/><br/>
Zcash currently uses Proof-of-Work, although it
[seems](https://twitter.com/zooko/status/1005007237713047552) Zooko and the team
would be willing to switch to a provably secure alternative protocol, such as a
Proof-of-Stake variant. Zcash also plans to upgrade zk-SNARKs to a more
scalable, quantum-safe zero-knowledge variant called
[zk-STARKs](https://www.youtube.com/watch?v=VUN35BC11Qw), which don’t require a
trusted setup. Block time is 2.5 minutes, and the maximum block size is 2 MB.
<br/><br/>
*Monetary Policy: *ZCash has an identical monetary policy as Bitcoin (21 million
maximum coins). It was launched in late 2016, so only 4.1 million coins have
been mined. 10% of all coins will be
[awarded](https://medium.com/@dhsue/an-analysis-of-zcash-governance-692793f9c9ef)
to the Zcash Company — founders, investors, employees, and advisors — from block
rewards.
<br/><br/>
#### Monero

Overview: Monero is a private cryptocurrency that was launched in April 2014
by anonymous developer(s) using the pseudonym Nicolas van Saberhagen. Unlike
Zcash, Monero does not support non-anonymous transactions; all origins,
destinations, and amounts are completely obfuscated, and thus Monero tokens are
fungible.
<br/><br/>
Monero uses one-time ring signatures to hide the sender, [ring confidential
transactions](https://eprint.iacr.org/2015/1098.pdf) (RingCT) to hide
transaction amounts, stealth addresses to hide the receiver, and has two minute
block times. It is built using the
[CryptoNote](https://cryptonote.org/whitepaper.pdf) protocol, which implements a
[dynamic block size](https://monero.stackexchange.com/a/4563) with a cap on
growth rate. Monero is mined using Proof-of-Work, and the developers are
attempting an ASIC-resistant scheme by
[changing](https://getmonero.org/2018/02/11/PoW-change-and-key-reuse.html) the
PoW algorithm roughly every six months. The last PoW change was in April, and
the hash rate is still recovering; it’s currently
[60%](https://bitinfocharts.com/comparison/monero-hashrate.html) lower than at
its all time high. The latest update added
[Ledger](https://www.ledgerwallet.com/) hardware wallet support and made compact
blocks called [fluffy
blocks](https://monero.stackexchange.com/questions/2633/what-are-fluffy-blocks)
default.
<br/><br/>
![](https://cdn-images-1.medium.com/max/1600/0*QKXPh-8tvW-GfNft.)
<span class="figcaption_hack">[Source](https://monero.stackexchange.com/questions/1516/comparison-of-monero-and-bitcoin-money-supply-and-block-reward-schedules)</span>
<br/><br/>
Monetary Policy: There are ~16.1m XMR in existence, and the main emission
schedule will issue ~18.4m XMR until the year 2022. After that, a “tail
emission” curve kicks in where 0.3 XMR will be issued per minute (157,680 per
year).
<br/><br/>
#### Grin and MimbleWimble

Overview: [MimbleWimble](https://www.youtube.com/watch?v=aHTRlbCaUyM) is a
design for a massively-prunable, scalable blockchain-based ledger
[dropped](https://download.wpsoftware.net/bitcoin/wizardry/mimblewimble.txt)
into a Bitcoin IRC chat in 2016 by pseudonymous engineer(s) named [Tom Elvis
Jedusor](http://fr.harrypotter.wikia.com/wiki/Tom_Jedusor).
[Grin](https://grin-tech.org/) is an upcoming cryptocurrency that is an
implementation of MimbleWimble using Rust. Grin uses a Proof-of-Work algorithm
called [Cuckoo
Cycle](https://github.com/mimblewimble/grin/blob/master/doc/pow/pow.md) which is
supposed to be fairly resistant to a Bitcoin-style ASIC arms-race, and is being
developed by mostly pseudonymous engineers using other Harry Potter character
names, such as [Ignotus
Peverell](http://harrypotter.wikia.com/wiki/Ignotus_Peverell). MimbleWimble can
also be implemented as a Bitcoin side-chain, or soft-forked in as an extension
block.
<br/><br/>
MimbleWimble supports confidential transactions to encrypt the amounts of all
transaction data via
[homomorphic](https://en.wikipedia.org/wiki/Homomorphic_encryption) encryption
and uses
[rangeproofs](https://github.com/mimblewimble/grin/blob/master/doc/rangeproofs.md)
for validity, but does not support
[scripting](https://en.bitcoin.it/wiki/Script). Instead, properties of Elliptic
Curve Cryptography were
[used](https://github.com/mimblewimble/grin/blob/master/doc/grin4bitcoiners.md)
to enable multi-signature transactions, atomic swaps, time-locked transactions
and outputs, and the Lightning Network.
<br/><br/>
With Bitcoin, new validators that join the network have to sync from the genesis
block and validate that each and every transaction has been valid. [With
MimbleWimble](https://github.com/mimblewimble/grin/blob/master/doc/grin4bitcoiners.md),
new validators only need block headers, unspent outputs, and excess data
(transaction data recording the difference between outputs and inputs, and
signatures of which only one is created for all parties involved in a
transaction). Transactions are indistinguishable from one another; there are no
addresses or amounts.
<br/><br/>
<span class="figcaption_hack">[Source](https://twitter.com/nic__carter)</span>
<br/><br/>
*Monetary Policy: *Grin plans to
[emit](https://github.com/mimblewimble/docs/wiki/Monetary-Policy) a new coin
every second forever. There is a currently a test net, and the coin plans to
launch this year.
<br/><br/>
#### Mobilecoin

Overview: [MobileCoin](https://www.mobilecoin.com/whitepaper-en.pdf) is an
upcoming privacy-centric cryptocurrency advised by the founder of Signal, [Moxie
Marlinspike](https://en.wikipedia.org/wiki/Moxie_Marlinspike). MobileCoin is
mobile-first, hence the prefix *mobile*; the idea is to integrate MobileCoin
wallets into messaging applications, such as Signal, WhatsApp, and Facebook
Messenger, and to allow cheap, fast payments, and key management and recovery
using a PIN.
<br/><br/>
MobileCoin uses Stellar’s [Consensus
Protocol](https://medium.com/a-stellar-journey/on-worldwide-consensus-359e9eb3e949)
(SCP), which is a Federated Byzantine Agreement (FBA) that prioritizes safety.
The goal is for a set of nodes, called a quorum, to obtain global consensus for
state changes. Nodes select their own subset of the quorum, called a quorum
slice, based on arbitrary conditions like reputation. The quorum slices vote to
convince their nodes of arbitrary statements, and individual quorum slices can
fail without the entire network failing. MobileCoin also uses
[CryptoNote](https://cryptonote.org/whitepaper.pdf) addresses and
ring-signatures for transaction anonymity. Nodes are to be run in [SGX secure
enclaves](https://github.com/lsds/spectre-attack-sgx) as one layer of security.
<br/><br/>
Monetary Policy: Fixed supply. More details unknown.
<br/><br/>

### Stablecoins
<br/><br/>
Stablecoins are cryptocurrencies that attempt to maintain a stable price; most
currently attempt to peg their price to 1 US Dollar, but they could
theoretically attempt a peg to anything, such as a basket of goods. A number of
people have described a functional stablecoin as the “holy grail” of the
cryptocurrency realm, and others are
[extremely](https://prestonbyrne.com/2017/12/10/stablecoins-are-doomed-to-fail/)
skeptical they will ever work without collapsing.
<br/><br/>
Volatility of existing cryptocurrencies has detracted from their potential use
as global media of exchange and day-to-day currencies. It is expected that a
functional stablecoin would immediately be usable as a store of value, medium of
exchange, and unit of account, regardless of its size and age. This is unlike
regular cryptocurrencies, which would require a long monetization period and
massive market cap to become relatively stable.
<br/><br/>
There exist three major kinds of stablecoins. The most common and arguably the
simplest kind are fiat-collateralized stablecoins, which include Tether (USDT)
and TrueUSD (TUSD), and attempt a peg to a unit of fiat (e.g. 1 USD).
Fiat-collateralized stablecoins are expected to be stable, with the assumption
that the backing is legitimate and regularly audited. They are highly
centralized and are necessarily tied to existing financial institutions and
banks.
<br/><br/>
Another kind of stablecoin is the crypto-collateralized stablecoin, and one
prominent example is MakerDAO’s DAI. Crypto-collateralized stablecoins attempt
to maintain their stability through over collateralizing the stablecoins with
another cryptocurrency, such as ETH, and utilizing a trading bot to maintain the
desired peg.
<br/><br/>
The third type of stablecoin is a non-collateralized / algorithmic kind. These
stablecoins are not explicitly backed by any underlying collateral; instead,
their algorithms conduct active, automated monetary policy (i.e. expansions and
contractions of supply to keep the stablecoin price pegged to $1). These systems
can be decentralized; however, they are still susceptible to large death spirals
if the demand for the overall system drops too suddenly.
<br/><br/>
#### MakerDAO

Overview: MakerDAO is one of the most prominent Decentralized Autonomous
Organizations (DAOs) built on the Ethereum blockchain. One of their core
products is the DAI stablecoin, which is a “crypto-collateralized” stablecoin.
<br/><br/>
The system is composed of both MKR tokens and DAI tokens; the former represents
ownership in the system and allows owners to participate in governance
decisions, and the latter is the actual stablecoin. The system attempts to
constantly peg the value of the DAI token to $1, and uses collateral to back its
value and algorithmic interest rate adjustments to stabilize its price.
<br/><br/>
The peg is maintained by modifying the incentives for borrowing and holding DAI.
Notably, DAI requires at least 1.5x worth of ETH to be deposited in order to
receive 1x worth of DAI stablecoins. The system is decentralized and uses a
series of oracles to provide smart contracts price data from exchanges; however,
it requires a high cost of capital and is mildly susceptible to black swan price
drops in the underlying asset.
<br/><br/>
The cost of borrowing DAI becomes more expensive when the price is below its
target. If the price rises above target, then the cost of creating new DAI is
reduced. These forces act to either decrease or increase the total supply of
DAI, ensuring that the asset has low volatility. The stability of DAI is also
supported by liquidating collateralized debt positions when the underlying
collateral falls too far in value. When this happens, the collateral needs to be
sold off to cover the outstanding DAI backed by it.
<br/><br/>
#### Basis

Overview: [Basis](https://basis.io/) is a stablecoin expected to launch in
2018, having raised $133M+ in
[funding](https://medium.com/basis-blog/introducing-basis-a-stable-cryptocurrency-with-an-algorithmic-central-bank-7a795393a525)
in the Spring of 2018 from a wide variety of prominent investors in the crypto
space. [Basis](https://basis.io/basis_whitepaper_en.pdf) describes itself as an
“Algorithmic Central Bank.” By utilizing a relatively complex three-token system
composed of stablecoins (Basis), bonds (Restore Tokens) and shares (Growth
Tokens), Basis attempts to utilize what is described as an Algorithmic Monetary
Policy to keep the Basis price pegged to $1.
<br/><br/>
Basis will be using a to-be-defined oracle system for the blockchain to
continuously receive the current stablecoin price across global cryptocurrency
exchanges. Basis plans to expand the supply of stablecoins when the coins are in
high demand and the price goes above $1.00, and contract the supply by
auctioning off bonds when there is a drop in demand and the price goes below
$1.00. It promises to return a full Basis stablecoin to bond holders when the
price returns to $1.00.
<br/><br/>
In this way, Basis is inspired by the existing central banking techniques, and
attempts to bring the proven monetary methods of central banks and combine them
with the transparency and decentralization potential of blockchain technology.
Base shares provide ownership in the entire system. They are described as “like
owning a piece of the Fed,” and the Basis system is often described as a
[Private Central Bank](https://www.youtube.com/watch?v=vbNMYfqTCkA). Base shares
receive newly issued stablecoins whenever the demand for the stablecoin
increases and the supply expands.
<br/><br/>
If the Basis system ever gets big enough where it is used globally as a medium
of exchange, or even widely accepted for goods and services, Basis would be able
to peg the stablecoin to a basket of goods / a CPI Index, rather than the US
Dollar.
<br/><br/>
<br/><br/>
_Originally posted on [Hackernoon](https://hackernoon.com/state-of-cryptocurrencies-summer-2018-932016549375)_.
<br/><br/>