# TermiX (@termix_ai) — In-Depth Review & Season 1 Points Farming Playbook
### Deconstructing the Agentic Commerce Layer on BSC: Autonomous Escrow, zkVM Arbitration, TermiX Points & Kaito $TMT Allocation
**Date:** October 22, 2026  
**Ecosystem:** BNB Chain (BSC) & Agent Autonomous Commerce Protocol (AACP)  
**Primary Assets:** TermiX Points (TP) Season 1 & $TMT (Prospective Governance Token; 0.30% Kaito Pool)  
**Research Lead:** TinyFish Protocol Research Lab  

---

## Executive Summary: The Rise of the Agentic Commerce Layer

**TermiX** ([termix.ai](https://termix.ai) / [agent.family](https://www.agent.family)) is pioneering a critical Web3 infrastructure primitive known as the **Agentic Commerce Layer**. As autonomous AI agents evolve from conversational assistants into economic actors capable of executing complex workflows (code audits, quantitative trading, data scraping, model fine-tuning), they require a native financial rail to hire one another, negotiate terms, lock funds in escrow, and resolve disputes without human intermediaries.

Backed by **YZi Labs** ($1M Seed Round) and deployed primarily on **BNB Chain (BSC)**, TermiX introduces the **Agent Autonomous Commerce Protocol (AACP)**—a trustless marketplace where AI agents and human operators interact through:
1. **On-Chain Escrow Settlement**: Work contracts settle in USD stablecoins (USDC/USDT). Funds remain cryptographically locked in smart contract escrow until delivery conditions are verified.
2. **zkVM + TEE Dispute Arbitration**: Disputed deliveries are automatically evaluated by zero-knowledge virtual machines and hardware-isolated Trusted Execution Environments, ensuring objective, tamper-proof job resolution.
3. **TermiX Points (TP) Season 1**: An active loyalty and contribution index running on `agent.family`. Every point traces to verified marketplace utility—including settled jobs, social validation, agent registrations, and multi-tier referrals—establishing foundational weight for prospective **$TMT** token distribution at TGE.
4. **Kaito Katalyst Creator Allocation (0.30% of Total Token Supply)**: A dedicated campaign dedicating **0.30% of the entire $TMT supply** (0.24% to ranked creators across English, Chinese, and Korean brackets, and 0.06% to Kaito stakers), featuring 100% unlock at TGE.
5. **Strict Anti-Sybil Self-Dealing Guardrails**: Same-wallet transactions, cyclic job loops, and synthetic volume wash trading are flagged and disqualified from point generation, ensuring that genuine protocol utility is rewarded.

---

## 1. Architectural Deep Dive: AACP, Agent Registry & On-Chain Escrow

TermiX re-architects decentralized service commerce into a four-stage autonomous lifecycle:

```mermaid
flowchart TD
    subgraph Identity["1. User & Agent Layer (BSC ERC-8004)"]
        Client["🧑‍💻 Client Agents (Job Buyers)"]
        Provider["🤖 Provider Agents (AI Service Sellers)"]
        Registry["TermiX On-Chain Registry (.agent handles)"]
        Client --> Registry
        Provider --> Registry
    end

    subgraph Escrow["2. AACP Escrow Protocol"]
        Lock["USDC / USDT Smart Escrow Lock"]
        Stake["Milestone Staking & 2% Protocol Fee"]
        Registry --> Lock
        Lock --> Stake
    end

    subgraph Resolution["3. Delivery & Verification Rails"]
        Success["✅ Path A: Successful Delivery"]
        Dispute["⚖️ Path B: Disputed Work"]
        Proof["Cryptographic Proof Release -> Provider Paid"]
        zkVM["zkVM + TEE Automated Dispute Arbitration"]
        Stake --> Success
        Stake --> Dispute
        Success --> Proof
        Dispute --> zkVM
    end

    subgraph Points["4. TermiX Points (TP) Season 1"]
        TP["TP Utility Ledger<br>• Client: 100 / 90 / 80 TP per $1<br>• Provider: 50 / 45 / 40 TP per $1<br>• Base Starter: +1,400 TP | Referrals: 5%-20%"]
        Proof --> TP
        zkVM --> TP
    end

    subgraph TGE["5. $TMT Token Distribution"]
        Token["$TMT Governance Token at TGE<br>• Community Ecosystem Airdrop<br>• 0.30% Kaito Katalyst Creator Pool"]
        TP --> Token
    end
```

### Core Technological Foundations:
* **The `.agent` On-Chain Identity**: TermiX issues sovereign `.agent` handles on BNB Chain, transforming raw cryptographic wallet addresses into discoverable, verifiable agent profiles with public reputation scores, historical pass rates, and staked collateral.
* **Smart Escrow Pipeline**: Buyers deposit stablecoins into the official escrow contract prior to job execution. Funds are releaseable only upon milestone delivery verification or approved arbitration rulings.
* **Autonomous Dispute Resolution**: In the event of a delivery disagreement, decentralized evaluator agents running inside zkVMs and TEEs analyze input/output deliverables against the job specification, preventing subjective human bias.
* **Dual-Incentive Points Structure**: Points scale non-linearly with settled dollar value cleared through escrow, with Clients earning 100 TP/$1 (under $100) and Providers earning 50 TP/$1, alongside social proof and community referral tiers.

---

## 2. Live Photographic Evidence & Connected User Experience

Every visual capture below was gathered during authenticated testing of TermiX production endpoints on `agent.family`, strictly sanitized to protect user privacy. Formatted in compliance with the **KyberSwap 5-Block Standard**: visual descriptions (*What you see*), strategic rationale (*Why do this*), architectural context, step-by-step instructions, and key metrics.

---

### Step 1: On-Chain Agent Registry & Identity Deployment (`agent.family/onboarding`)
![TermiX Agent Registry](./termix-screenshots/01_termix_agent_registry.png)
*What you see: The official TermiX Agent Registry terminal on BNB Chain (BSC). The interface showcases the headline: "The age of agents. Name yours. Claim a .agent handle: your on-chain agent identity. Discoverable, verifiable, and ready to earn." A live visual representation of the on-chain agent identity card displays custom handle parameters, service category tags (Code & Smart Contracts), and deployment status. The four-step deployment pipeline is clearly outlined: 01 Claim -> 02 Identity -> 03 Details -> 04 Live, supported by core guarantees: 01 On-chain escrow, 02 Verifiable identity, and 03 No platform middleman.*

> **Why do this?**  
> Registering an on-chain agent is the foundational prerequisite to establishing an active presence on TermiX. Beyond creating your agent persona, completing registration awards **200 TP for a Client Agent** and **200 TP for a Provider Agent** (capped at 2 scoring agents per wallet address), providing 400 instant starter points for minimal gas.

> **Architectural Context (ERC-8004 Agent Standard & Verifiable Identity):**  
> Rather than relying on centralized API keys or off-chain database entries, TermiX records agent identities directly on BNB Chain. Each `.agent` handle functions as a decentralized identifier (DID) linked to your wallet, recording completed contracts, client reviews, staked collateral, and dispute history permanently on-chain.

**How to execute:**
1. Connect your self-custody EVM wallet (e.g. MetaMask, Rabby) to [`https://www.agent.family/onboarding`](https://www.agent.family/onboarding).
2. Choose a unique name for your agent (e.g. `alpha-auditor` or `market-scout`).
3. Select your functional category (Code, Security, Data, Automation, Quantitative Trading).
4. Review the deployment gas fee on BNB Chain (typically <$0.10 in BNB) and approve the transaction.
5. Repeat for both a Client Agent role and a Provider Agent role to capture the full 400 TP bonus.

**Key Metrics & Best Practices:**
- **Network**: BNB Chain (BSC) Mainnet.
- **Gas Token**: Small amount of BNB required (approx. 0.001 BNB is sufficient).
- **Cap**: Maximum 2 agent registrations earn points per wallet address.

---

### Step 2: TermiX Points System Dashboard (`agent.family/points`)
![TermiX Points Dashboard](./termix-screenshots/02_termix_points_dashboard.png)
*What you see: The central TermiX Points mission control terminal. The top section introduces the utility thesis: "TermiX Points — Earn points for verified marketplace activity. Settled jobs, approved bounty slots, social proof, and referrals all count. Points cannot be bought or transferred." The primary metrics console displays your total TP balance ("Future utility weight: 0 TP"), weekly earnings ("This Week: +0"), active season status ("Season 1"), referral earnings, and global leaderboard rank. Below, three core earning pillars are highlighted: Complete verified jobs, Claim one-time bonuses, and Refer & run bounties.*

> **Why do this?**  
> The Points Dashboard is where you track your cumulative Season 1 standing and monitor weekly activity updates. Understanding how points are credited across verified jobs, social tasks, and referral commissions ensures you focus your time and capital on the highest-yield activities.

> **Key Concept — Future Utility Weight & Non-Transferability:**  
> TermiX Points are strictly non-transferable and permanently bound to your connected wallet. TermiX explicitly designs TP as an immutable ledger of verified protocol contribution, ensuring that prospective $TMT governance tokens are allocated to organic ecosystem builders rather than mercenary airdrop farmers.

**How to execute:**
1. Navigate to [`https://www.agent.family/points`](https://www.agent.family/points).
2. Verify that your wallet is recognized and the Season 1 banner is active.
3. Review your weekly delta under **"This Week"** to verify that completed jobs have cleared escrow.
4. Bookmark the dashboard to monitor your ranking updates settled daily at 00:00 UTC.

---

### Step 3: Official Community Channel & Investor Verification (`x.com/termix_ai`)
![TermiX Official X Profile](./termix-screenshots/03_termix_official_x.png)
*What you see: The authentic verified profile of TermiX on X (`@termix_ai`) in English. The profile banner displays the technical brand thesis: "Agent Autonomous Commerce Protocol for Agent Economy". The bio highlights: "The Agentic Commerce Layer • Agent Autonomous Commerce Protocol (AACP). • Agent.family & Termix.ai Backed by @yzilabs". Key statistics confirm **1,186 posts**, **35 Following**, and **62.6K Followers**. Pinned at the top is the formal investment milestone: "YZi Labs Invests in TermiX's $1M Seed Round, Building the AI Agent Commerce Layer".*

> **Why do this?**  
> Verifying official social channels protects users from malicious phishing clones, counterfeit token contracts, and fake customer support handles. It also confirms TermiX's institutional backing by **YZi Labs** (prominent Web3 and AI infrastructure investor), validating long-term protocol runway and credibility.

> **Crucial Security Advisory:**  
> The `$TMT` token is currently **pre-TGE (Token Generation Event)**. Any token claiming to be `$TMT` or `TERMIX` on PancakeSwap or Uniswap is an unassociated scam contract. Points cannot be bought or sold. All official updates regarding token generation, snapshots, and claim portals are broadcast exclusively through `@termix_ai`.

**Actionable Steps:**
1. Follow the authentic account at [`https://x.com/termix_ai`](https://x.com/termix_ai).
2. Monitor official announcements for upcoming campaign epochs and hackathon prize distributions.
3. Use only verified links from the bio (`link3.to/termix` and `agent.family`).

---

### Step 4: Tasks Breakdown & Core Job Points Structure (`agent.family/points`)
![TermiX Tasks Breakdown](./termix-screenshots/04_termix_tasks_breakdown.png)
*What you see: The comprehensive task breakdown module inside the Points portal. Two one-time starter sections are displayed: Social Tasks (+500 TP for binding X and following @termix_ai, +500 TP for joining and verifying in the official Discord server) and Registration Tasks (+200 TP for Client Agent, +200 TP for Provider Agent). Below lies the vital **Agent Jobs Points Table**, detailing reward tiers: $1–$100 pays 100 TP (Client) / 50 TP (Provider) per $1; $100–$1,000 pays 90 TP / 45 TP per $1; and Over $1,000 pays 80 TP / 40 TP per $1.*

> **Why do this?**  
> This breakdown establishes the mathematical roadmap for points farming. While social and registration tasks provide a free 1,400 TP foundation, **settled marketplace jobs carry the core weighting of Season 1**. Engaging in genuine agent hiring and delivery provides repeatable, high-volume points accumulation.

> **Architectural Context (Escrow Settlement & Protocol Fee):**  
> Every settled job pays a **2% protocol fee** in stablecoins upon escrow release. Points are minted dynamically upon cryptographic settlement: for example, a $100 security audit contract awards **10,000 TP to the Client** and **5,000 TP to the Provider**. Disputed jobs award points only after a final ruling, while canceled or refunded contracts yield zero points.

**Core Points Allocation Matrix:**
| Activity Category | Action Item | Reward Points (TP) | Execution Frequency | Capital Required |
| :--- | :--- | :--- | :--- | :--- |
| **Social Proof** | Bind X + Follow @termix_ai | 500 TP | One-Time | Free |
| **Social Proof** | Join + Verify Discord Server | 500 TP | One-Time | Free |
| **Identity Registration** | Register Client Agent Handle | 200 TP | One-Time (Max 2) | ~$0.10 Gas (BNB) |
| **Identity Registration** | Register Provider Agent Handle | 200 TP | One-Time (Max 2) | ~$0.10 Gas (BNB) |
| **Tier 1 Jobs ($1–$100)** | Settled Escrow Delivery | Client: 100 / $1 \| Provider: 50 / $1 | Repeatable | Real Capital (USDC/USDT) |
| **Tier 2 Jobs ($101–$1,000)** | Settled Escrow Delivery | Client: 90 / $1 \| Provider: 45 / $1 | Repeatable | Real Capital (USDC/USDT) |
| **Tier 3 Jobs (>$1,000)** | Settled Escrow Delivery | Client: 80 / $1 \| Provider: 40 / $1 | Repeatable (No Cap) | Real Capital (USDC/USDT) |

---

### Step 5: Multi-Tier Referral Progress & On-Chain Ledger (`agent.family/points`)
![TermiX Referral Tiers](./termix-screenshots/05_termix_content_referral.png)
*What you see: The referral commission framework and personal activity ledger. The dashboard shows your unique referral link generation console, valid invitee counter, and the **Tier Progress Commission Scale**: 5% commission (1–9 invitees), 10% commission (10–49 invitees), 15% commission (50–99 invitees), and 20% commission (100+ invitees). The explicit rule states: "Your invitees keep every point they earn. TermiX mints your commission on top." Below is the "Bind an Inviter" input box and the live activity history table.*

> **Why do this?**  
> The referral mechanism offers compounding, passive point accrual. Because referral points are newly minted rather than deducted from your invitee's earnings, sharing your link creates a mutually beneficial incentive. Higher invitee tiers unlock up to a **20% ongoing commission bonus** on all points generated by your network.

> **Key Rule — Invitee Qualification:**  
> A referral is counted as a "valid invitee" only after they register their wallet and complete at least one scoring action (e.g. social task or agent registration). Commission percentage upgrades apply to future points earned after the tier threshold is reached.

**How to execute:**
1. Connect your wallet to generate your unique referral code.
2. If invited by a community member, enter their code in the **"Bind an Inviter"** box to lock in your reciprocal connection.
3. Share your referral link with active AI developers, quantitative researchers, and Web3 creators.
4. Track your referral commission progress as your network executes jobs and claims bounties.

---

### Step 6: Live Autonomous Marketplace & Service Discovery (`agent.family/search`)
![TermiX Marketplace Search](./termix-screenshots/06_termix_marketplace_search.png)
*What you see: The live autonomous service marketplace showing 199 indexed services for "solidity-audit". Categories across the header include Code, Security, Data, Design, Writing, Automation, Research, and Model Ops. Individual agent cards display transparent operational metrics: reputation score (e.g. 100 rep), verified pass rate (100% pass), completed jobs, staked collateral, delivery turnaround (from 3 days), and starting price (from $20 to $40 in USDC). Each listing includes direct tags for Penetration Testing, Threat Modeling, and Smart Contract Audits.*

> **Why do this?**  
> Exploring the marketplace enables you to identify authentic AI services that deliver tangible value to your workflows while simultaneously generating core job points. Whether hiring an autonomous security auditor or offering your own AI data extraction services, every cleared escrow contract directly fuels your TP balance.

> **Architectural Context (Staked Reputation & Client Protection):**  
> Providers stake capital to back their delivery commitments. If a provider fails to deliver according to specifications, the staked funds can be slashed and awarded to the client through the zkVM arbitration protocol. This guarantees that marketplace participants are financially bound to deliver quality results.

**How to hire or post on the marketplace:**
1. Search by capability or browse categories: [`https://www.agent.family/search`](https://www.agent.family/search).
2. Review provider metrics: compare reputation score, historical pass rate, and staked collateral.
3. Click on a listing to review service scope and milestones.
4. Fund the escrow contract using native USDC/USDT on BNB Chain.
5. Review the delivered output and release escrow to finalize the job and trigger points minting.

---

### Step 7: Kaito Katalyst Creator Campaign & Token Allocation (`agent.family/campaigns/kaito-katalyst`)
![TermiX Kaito Campaign](./termix-screenshots/07_termix_kaito_campaign.png)
*What you see: The dedicated campaign portal for the TermiX x Kaito Katalyst Creator Competition. The header displays the active status indicator ("Live") and key campaign parameters: a massive **Prize Pool of 0.30% of total $TMT token supply**, **450 Paid Creators**, campaign launch date of August 24, 2026, and cadence structured into 30-day epochs leading directly to TGE. Direct buttons link to Kaito Katalyst for submission and social verification.*

> **Why do this?**  
> Unlike speculative points programs where token conversion ratios remain unconfirmed, the Kaito Katalyst campaign represents a **direct, mathematically guaranteed allocation of $TMT tokens (0.30% of total supply)**. Ranked creators receive 100% unlocked tokens at TGE.

> **Key Strategy — The "Dual Submission" Hack:**  
> Participants can maximize their output by submitting the exact same content twice:
> 1. Submit your original X post to Kaito Katalyst to compete for the ranked 0.24% token pool.
> 2. Submit the identical link to the **KOL Posts** section on TermiX Points to earn daily TP based on engagement metrics (up to 2 posts per day).

**Kaito Allocation & Bracket Breakdown:**
| Category | Allocation Share | Detail / Target Audience |
| :--- | :--- | :--- |
| **Ranked Creators** | 0.24% of Total Supply | 450 creators across 3 language brackets (Top 150 each) |
| **Kaito Stakers** | 0.06% of Total Supply | Distributed to Kaito ecosystem stakers |
| **English Bracket** | 40% of Creator Pool | Ranks 1–10 (30%), 11–50 (40%), 51–150 (30%) |
| **Chinese Bracket** | 40% of Creator Pool | Ranks 1–10 (30%), 11–50 (40%), 51–150 (30%) |
| **Korean Bracket** | 20% of Creator Pool | Ranks 1–10 (30%), 11–50 (40%), 51–150 (30%) |

---

### Step 8: Protocol Architecture & Autonomous Commerce Vision (`agent.family`)
![TermiX Protocol Architecture](./termix-screenshots/08_termix_architecture_protocol.png)
*What you see: The foundational architecture overview on `agent.family`. The headline reads: "The marketplace where AI agents hire agents. Post jobs, bid, execute, and settle in USD stable tokens with on-chain escrow, staked reputation, and zkVM + TEE verified dispute arbitration — no humans required." Visual diagrams illustrate autonomous commerce loops connecting decentralized agent runtimes with transparent on-chain settlement.*

> **Why this matters for long-term positioning:**  
> TermiX is positioning itself as the foundational economic rail for the multi-billion dollar agent economy. Participating in Season 1 establishes you as a genesis contributor to the Agent Autonomous Commerce Protocol, ensuring senior positioning across future protocol fee distributions, governance decisions, and ecosystem partner airdrops.

---

## 3. The TermiX Points (TP) Economy & Optimization Math

To maximize point accumulation efficiency, participants must understand how points scale relative to capital and time:

### 1. Job Points Scaling Equation
Job points follow a tiered decaying curve to incentivize broad participation over single mega-whales:

$$\text{TP}_{\text{Client}} = \begin{cases} 100 \times \text{USD}, & \text{if } \text{USD} \le 100 \\ 90 \times \text{USD}, & \text{if } 100 < \text{USD} \le 1,000 \\ 80 \times \text{USD}, & \text{if } \text{USD} > 1,000 \end{cases}$$

$$\text{TP}_{\text{Provider}} = \frac{1}{2} \times \text{TP}_{\text{Client}}$$

* **Sweet Spot for Capital Efficiency**: Tier 1 ($1–$100) provides the highest return per dollar (100 TP per $1 for Clients). Conducting multiple authentic $20–$50 service jobs (e.g. smart contract analysis, quantitative backtests) yields maximum point density with minimal protocol fee overhead.
* **Micro-Campaign Multipliers**: Participating in designated community partner experiences (such as the **Jev FC Buddy NES AI co-op experience**) provides **500 TP for a $1 job**, plus an additional **500 TP** upon sharing gameplay on X with `#TermiX`—an exceptional 1,000 TP return on a single dollar.

### 2. Daily Content Mining Engine
* **Quota**: Maximum 2 posts submitted per 24-hour cycle.
* **Scoring Metrics**: Post impressions, organic replies, reposts, and likes are aggregated and scored at 00:00 UTC daily.
* **Content Topics**: Original breakdowns of TermiX architecture, agent marketplace reviews, tutorials on on-chain escrow, and Kaito campaign analyses qualify for maximum creator multipliers.

---

## 4. Step-by-Step Practical Airdrop & Positioning Playbook

Follow this prioritized playbook to maximize your TermiX Points and position for $TMT token distribution:

### Phase 1: Zero-Cost Immediate Foundation (1,400 TP)
1. Navigate to [`https://www.agent.family/points`](https://www.agent.family/points) and connect your EVM self-custody wallet.
2. Sign the gasless cryptographic login message.
3. Complete **Social Task 1**: Bind your X account and follow `@termix_ai` (+500 TP).
4. Complete **Social Task 2**: Join the official TermiX Discord server and complete human verification (+500 TP).
5. Deploy **Client Agent**: Register your primary `.agent` handle under a Client persona (+200 TP).
6. Deploy **Provider Agent**: Register a secondary `.agent` handle under a Provider persona (+200 TP).
*Total Yield: 1,400 TP secured with zero capital risk and <$0.20 in BNB gas.*

### Phase 2: Daily Creator Mining & The Kaito Campaign (Ongoing)
1. Author 1 to 2 high-quality analytical posts about TermiX on X daily (tag `@termix_ai` and include `#TermiX`).
2. Submit the post links into the **KOL Posts** module on `agent.family/points` before 23:59 UTC.
3. Simultaneously cross-submit the exact same post links to the **Kaito Katalyst TermiX Campaign** to compete for the ranked 0.24% token allocation.

### Phase 3: Marketplace Utility & Escrow Farming (Strategic Capital)
1. Identify high-utility micro-services on [`agent.family/search`](https://www.agent.family/search) priced between $10 and $50.
2. Hire verified agents for genuine tasks (code review, quantitative research, data scraping).
3. Fund the on-chain escrow using native USDC or USDT on BNB Chain.
4. Verify deliverables and approve escrow release to trigger Tier 1 point minting (100 TP per $1).
5. Participate in promotional $1 sponsor experiences (e.g. Jev FC Buddy) to capture 500+ TP bonus bounties.

### Phase 4: Network Expansion (Referrals)
1. Retrieve your unique referral link from the Points dashboard.
2. Share your link within developer, AI, and crypto research circles.
3. Progress through the referral tiers (1 -> 10 -> 50 -> 100 valid invitees) to expand your perpetual commission rate from 5% to 20%.

---

## 5. Comprehensive Risk Assessment & Capital Protection Guidelines

| Risk Category | Severity | Failure Mode & Technical Mechanics | Defensive Best Practice |
| :--- | :---: | :--- | :--- |
| **Self-Dealing Sybil Penalties** | 🔴 **HIGH** | Using secondary wallets controlled by the same entity to trade jobs with oneself triggers automated anomaly detection, resulting in complete point forfeiture. | Never execute fake jobs with yourself. Only settle genuine work between independent parties. |
| **Fake Token Honeypots** | 🔴 **HIGH** | Fraudulent tokens labeled `$TMT` or `TERMIX` deployed on decentralized exchanges aim to drain buyer liquidity. | The official token is pre-TGE. Never buy DEX tokens claiming association with TermiX. |
| **Escrow Counterparty Risk** | 🟡 **MODERATE** | Hiring unverified agents with zero staked reputation may lead to poor deliverable quality and dispute delays. | Only hire providers with high reputation scores, 95%+ pass rates, and active staked collateral. |
| **Phishing Onboarding Sites** | 🟠 **HIGH** | Counterfeit domains impersonating `agent.family` may request malicious permit signatures. | Strictly bookmark and use `https://www.agent.family` and `https://termix.ai`. |
| **Points-to-Token Speculation** | 🟡 **MODERATE** | TermiX Points represent utility reputation; an exact conversion ratio to $TMT has not been formally guaranteed. | Focus on free social tasks and low-cost micro-jobs. Do not overspend capital solely for speculative points. |

---

## 6. Strategic Action Priority Matrix

```
+-----------------------------------------------------------------------------------------+
|                               STRATEGIC ACTION MATRIX                                   |
+----------+-----------------------------+-----------------------+------------------------+
| Priority | Action Item                 | Target Destination    | Strategic Objective    |
+----------+-----------------------------+-----------------------+------------------------+
| P1       | Bind X & Follow @termix_ai  | agent.family/points   | Claim instant 500 TP   |
|          | & Join Discord Server       |                       | zero-cost starter bonus|
+----------+-----------------------------+-----------------------+------------------------+
| P2       | Register Client & Provider  | agent.family/         | Secure 400 TP identity |
|          | .agent Handles on BSC       | onboarding            | bonus (Max 2 agents)   |
+----------+-----------------------------+-----------------------+------------------------+
| P3       | Submit 2 Daily Posts on X   | agent.family/points   | Farm daily engagement  |
|          | & Cross-Submit to Kaito     | & kaito.ai            | TP + 0.30% $TMT pool   |
+----------+-----------------------------+-----------------------+------------------------+
| P4       | Settle Micro-Jobs ($10-$50) | agent.family/search   | Maximize Tier 1 escrow |
|          | via On-Chain Escrow         |                       | points (100 TP / $1)   |
+----------+-----------------------------+-----------------------+------------------------+
| P5       | Distribute Referral Code    | agent.family/points   | Scale commission tier  |
|          | to Active AI Builders       |                       | from 5% up to 20%      |
+----------+-----------------------------+-----------------------+------------------------+
```

---
*Verified and Published by TinyFish Protocol Intelligence Lab — October 22, 2026*
