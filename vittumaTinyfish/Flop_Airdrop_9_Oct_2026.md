# Flop Airdrop 9 Oct 2026 - Comprehensive Review & Step-by-Step Execution Guide

> **Direct Data Analysis & Verification via TinyFish CLI, plus Detailed Step-by-Step Flop Network Airdrop Guide** 
> *Created: October 9, 2026*

---

## 1. LIVE EXPERIENCE & DATA VERIFICATION VIA TINYFISH CLI

Using **TinyFish CLI** (`fetch` and `search` commands), data from Flop Network's official pages was extracted and verified directly:

* **Homepage**: [flop.finance](https://flop.finance/)
* **Airdrop Rules**: [flop.finance/airdrop](https://flop.finance/airdrop)
* **Testnet Spec**: [flop.finance/testnet](https://flop.finance/testnet)
* **Official X / Twitter**: [@flop_labs](https://x.com/flop_labs) and Co-founder Arthur Hayes [@CryptoHayes](https://x.com/CryptoHayes)

![Flop Finance Homepage](./screenshots/flop_homepage.jpg)
*Official website evidence*: [flop.finance](https://flop.finance) — Flop Network homepage overview.




## 2. DETAILS OF 2 ACTIVE PRE-TESTNET COMPETITIONS

Flop Labs and Arthur Hayes launched 2 pre-Testnet trial competitions on the **Technocore** environment (`technocore.chat`). These are the first officially announced airdrop qualification activities:

![Flop Airdrop Dashboard](./screenshots/flop_airdrop_dashboard.jpg)
*Airdrop management dashboard evidence*: [flop.finance/airdrop](https://flop.finance/airdrop) — Live airdrop qualification dashboard.


### Competition 1: NVDA Perp Prediction Contest (1,000,000 $FLOP)
* **Source Tweet Evidence**: [Arthur Hayes (@CryptoHayes) on X](https://x.com/CryptoHayes/status/2103453504513937720) (September 25, 2026).
* **Description**: AI Agents predict the **NVDA perp** price on **Hyperliquid** on October 4, 2026. Agents autonomously read the rules, receive trading funds, and execute automated trades on Technocore.
* **Prize**: **1,000,000 $FLOP** for the Top 3 Agents with the highest PnL (awarded at Mainnet launch).

### Competition 2: 100,000 $FLOP Sonnet Challenge
* **Source Tweet Evidence**: [Flop Labs (@flop_labs) on X](https://x.com/flop_labs/status/2098307911948890489) (September 11–18, 2026).
* **Description**: AI Agents form groups of 4–8 to collaboratively write a Sonnet poem (each turn writes 1 word). Requires a pre-registered DID (Pre-start DID).
* **Prize**: **100,000 $FLOP** (50,000 $FLOP for the winning team + 50,000 $FLOP split among voters).

---

## 3. GENESIS ALLOCATION OVERVIEW & UNLOCK MECHANISM (4.4 BILLION $FLOP)

* **Total Genesis Pool**: **4,400,000,000 $FLOP** (~24.3% of year-10 total supply).
* **Launch Model**: **100% Fair Launch** (No Pre-sale, No VCs).

| Role | Pool Allocation | Calculation Formula | Unlock Terms | Application Form |
| :--- | :--- | :--- | :--- | :--- |
| **Miner (GPU)** | 1.2B $FLOP | Pro-rata by verified compute (FLOPs) | **25% Liquid** at Genesis; remaining 75% unlocks 1:1 as $FLOP inference fees are paid on Mainnet | [Apply Miner](https://flop.finance/apply/miner) |
| **Agent (User/Bot)** | 1.2B $FLOP | Pro-rata by compute purchased in settled sessions + Contests | 100% locked. Unlocks 3:1 (spend 3 locked $FLOP on compute to unlock 1 liquid $FLOP) | N/A (Use DID) |
| **Validator** | 1.2B $FLOP | Top 1,000 Testnet ranking (1.2M FLOP/slot) | Locked as Bond collateral until Halving 1 (~2 years), then unlocking 1 validator/day over 1,000 days | [Apply Validator](https://flop.finance/apply/validator) |
| **Ecosystem** | 800M $FLOP | Creators, referrals, builders, security reports, Sonnet Voters | Distributed via network development programs | [Apply Creator](https://flop.finance/apply/kol) |

---

## 4. DETAILED EXECUTION GUIDE (HOW-TO-FARM PLAYBOOK)

---

### PATH 1: FOR INDIVIDUALS / REGULAR COMPUTERS (AGENT & VOTER ROLE)
> **Easiest path — No GPU required — Anyone can do it**

1. **Create a DID Identity (`did:key:...`)**:
 * Use Ed25519 cryptographic keys to generate a key pair (Public/Private Key).
 * Create your DID in the format `did:key:z6M...` on [technocore.chat](https://technocore.chat/).
 * Store your Private Key encrypted safely on your local machine.

2. **Participate in Voting & Content Creation (Pre-Testnet Contests)**:
 * Use your DID to register and vote for Sonnet poems to share the **50,000 $FLOP** voter pool.
 * Set up an Agent to participate in the Trading competitions on Technocore to compete for **1,000,000 $FLOP**.

3. **Execute When Testnet Q4 2026 Opens**:
 * Withdraw Testnet tokens from the Faucet.
 * Run an automated bot to purchase AI Inference compute in settled sessions.
 * **Note**: Holding Faucet tokens without spending = 0 points. Only tokens actually spent on compute count toward airdrop points.

---

### PATH 2: FOR USERS WITH GPU ≥ 16GB VRAM (MINER ROLE)
> **Highest potential — Receive 25% Liquid immediately at Genesis**

1. **Prepare GPU**: Requires at least 1 GPU or GPU cluster with VRAM **≥ 16 GB** (RTX 3090, 4090, A6000, A100, or rent GPU Cloud from Vast.ai / RunPod).
2. **Submit Application**: Visit [flop.finance/apply/miner](https://flop.finance/apply/miner) to register hardware information.
3. **Run Node When Testnet Launches**:
 * Install the Flop Miner Client.
 * Complete the GPU FLOPs Calibration step.
 * Keep the node running 24/7 to serve inference sessions. Only verified compute counts toward points.

---

### PATH 3: FOR USERS WITH A VPS SERVER (VALIDATOR ROLE)

1. **Server Requirements**: 8+ Core CPU, 64 GB RAM, 4 TB NVMe SSD (minimum 2 TB), 1 Gbps network.
2. **Submit Application**: Visit [flop.finance/apply/validator](https://flop.finance/apply/validator).
3. **Run Node & Maintain Top Ranking**: Deploy Validator Node, maintain Uptime > 99.9% to reach **Top 1,000 Ranking** and secure a **1.2 Million $FLOP Genesis Bond** slot.

---

## 5. ANTI-BAN & ANTI-SPAM RULES (ANTI-SYBIL)

1. **One Participant, One Score**: Multiple wallets with the same owner are merged into 1 score. Focus on 1 DID only.
2. **Internal Volume Excluded**: Purchasing compute from a Miner you own yourself will have that volume excluded.
3. **Idle Machine = 0 Points**: Miners with idle machines or falsified configuration receive no rewards.
4. **Scam Warning**: Never share your Private Key/Seed Phrase with anyone. The project has no early claim page.

---

### REFERENCE LINKS

* [Flop Finance Homepage](https://flop.finance/)
* [Official Airdrop Rules](https://flop.finance/airdrop)
* [Testnet Specifications](https://flop.finance/testnet)
* [Miner Application Form](https://flop.finance/apply/miner)
* [Validator Application Form](https://flop.finance/apply/validator)
* [Creator / KOL Application Form](https://flop.finance/apply/kol)
* [X / Twitter @flop_labs](https://x.com/flop_labs)
* [X / Twitter @CryptoHayes](https://x.com/CryptoHayes)
