# Top 5 Telegram Trading Bots for Sniping Meme Coins in 2026

*By the Editorial Team — Updated October 21, 2026*

> **Disclaimer:** This article is for informational purposes only and does not constitute financial advice. Meme coin trading carries extreme risk. You may lose all funds. Never invest more than you can afford to lose.

---

## Quick Comparison Table

| Bot | Networks | Trading Fee | Custody | Best For | Notable Safety Record |
|-----|----------|------------|---------|----------|----------------------|
| Banana Gun | ETH, SOL, Base, TON | 0.5% manual / 1% sniper | Non-custodial | Multi-chain power users | Sep 2024 hack: $3M — fully refunded |
| Trojan on Solana | SOL | 1% (0.9% with referral) | Non-custodial | Pure Solana sniping | No major exploit recorded |
| Maestro | ETH, BSC, SOL, Base, Avalanche, Arbitrum, TON, Linea | 1% | Non-custodial | Multi-chain feature depth | Oct 2023 exploit: ~$500K — fully refunded in 10 hours |
| BonkBot | SOL | 1% | Non-custodial | Beginners on Solana | No major exploit recorded |
| FOMO | Hyperliquid (perps) | 0.1% | Non-custodial | Perpetual futures via Telegram | Closed Beta — DWF Labs backed |

---

## What Is a Telegram Trading Bot?

A Telegram trading bot is an automated software program embedded in the Telegram messaging app that executes crypto trades on your behalf — faster than any human can manually click "buy." In the meme coin arena, where tokens can 50x and collapse to zero within minutes, speed is survival.

There are three categories worth understanding before you start:

**1. Signal bots** — These send buy/sell alerts based on technical analysis, on-chain data, or influencer call channels. They don't execute trades; they notify you so you can act. They carry low technical risk but are only as good as their signal source.

**2. Execution bots (Telegram-native)** — This is the category this article focuses on. Bots like Banana Gun, Trojan, and BonkBot connect your wallet directly inside Telegram. You send a token contract address and the bot routes and executes the trade on-chain. Most operate on a non-custodial model, meaning *they never hold your private key* — your wallet stays under your control.

**3. Custodial bots** — Platforms like Pionex (0.05% fee) hold your funds on their own exchange infrastructure. They're easier to use and better suited to grid trading on established coins, but you surrender custody. **Pionex is the only mainstream custodial option in this list's orbit.** Every bot reviewed below is non-custodial.

Understanding this distinction matters enormously for risk management — a point the safety section below reinforces with hard data.

---

## Are Telegram Bots Safe? The Exploit History You Need to Know

Before ranking any bot, you need the full picture on security incidents. The track record across this space is mixed, and the worst outcomes are permanent.

### ✅ Banana Gun — September 2024

In September 2024, a vulnerability in Banana Gun's Telegram message oracle was exploited. **11 users had a total of approximately $3 million drained from their wallets.** The team detected the attack quickly, halted affected systems, and — critically — **fully refunded every impacted user from the Banana Gun treasury within days.** No tokens were sold to cover the cost; it came from protocol reserves. This response, while painful, demonstrated the team's commitment to user protection at significant cost to themselves.

*(Separate earlier incident: In September 2023, a bug in the $BANANA token smart contract was discovered before launch. The team redeployed the contract entirely and took a snapshot of all holders — no funds were lost.)*

### ✅ Maestro — October 2023

Maestro suffered an exploit in October 2023 in which a router contract vulnerability allowed an attacker to drain approximately **$500,000 in ETH.** The response was remarkable: **all affected users were fully reimbursed within 10 hours** — funded by bot revenue rather than user funds. Maestro later published a post-mortem and patched the vulnerability. The speed of the refund set a benchmark for incident response in this space.

### ✅ Unibot — October 2023

Unibot, a competing bot that has since declined in market share, was exploited for approximately **$640,000 in the same month as Maestro's incident.** The stolen funds were initially routed through Tornado Cash. Users were eventually refunded, though the process was slower and less transparent.

### ❌ 3Commas API Leak — December 2022 (No Refunds)

This is the cautionary tale. In December 2022, 3Commas — a custodial/API-based trading bot platform — suffered a catastrophic API key leak. **Approximately $14.8 million was stolen across 44 wallets.** The FBI launched an investigation. **Victims were never refunded.** 3Commas initially denied the leak was their fault, then later admitted to it. This incident underlines the difference between non-custodial bots (where you retain key control) and platforms that hold or have deep access to your account credentials.

### The Fake Bot Problem (2025–2026)

A persistent threat that accelerated through 2025 is impersonation bots. Bad actors create Telegram bots with near-identical names and usernames to legitimate bots, then promote them through fake subreddits, Discord DMs, and fraudulent YouTube videos. Victims connect wallets to these clones, which promptly drain all funds. **Always verify the official bot handle through the project's verified website or official Twitter/X account before clicking any Telegram link.**

---

## 1. Banana Gun — Highest Volume, Multi-Chain Pioneer

**Official bot:** @BananaGunBot on Telegram | **Website:** bananagun.io

Banana Gun is the undisputed volume leader among Telegram trading bots. As of late 2026, the platform has processed **over $16.09 billion in cumulative trading volume** and serves more than **1.3 million registered users** — figures that dwarf most competitors and speak to both adoption and infrastructure reliability.

### Networks and Features

Banana Gun supports **Ethereum, Solana, Base, and TON**, making it one of the few true multi-chain solutions in the Telegram bot space. Core capabilities include:

- **Automated sniping** — buy tokens the moment they list on DEXs (Uniswap, Raydium, etc.)
- **Copy trading** — mirror successful wallets automatically
- **Limit orders** — set conditional buys and sells
- **MEV protection** — reduce exposure to front-running
- **Banana Pro** — a web-based trading terminal for power users wanting a full dashboard experience

### Fee Structure and $BANANA Token

Fees are tiered by trade type:
- **Manual trades:** 0.5%
- **Sniper trades:** 1%

What distinguishes Banana Gun from most competitors is its **revenue-sharing model**: 40% of all trading fees are distributed to holders of the $BANANA governance token. This creates direct alignment between the protocol's commercial success and token holders — a design uncommon in this category.

### What Reddit Users Are Saying

> *"I ended up using Banana Gun the most lately tbh. The copy trading is probably the best I've tested so far, especially for fast-moving Solana plays. Their fills are crazy fast too — you can actually notice it compared to slower bots when entering the same token with friends."*
> — u/MarieB_Schultz, r/CryptoCurrencyTrading

> *"You can pull the Solana wallet behind any [FOMO] profile and paste it into a Telegram bot like Banana Gun to copy it automatically. The part most people get wrong is the exit — copy sells off, your own take profit on."*
> — u/Wessly-willson, r/CryptoExchange

### Pros and Cons

**Pros:**
- Largest user base and proven infrastructure ($16B+ volume)
- Best-in-class copy trading on Solana
- Transparent refund response to the 2024 exploit
- Revenue sharing via $BANANA token
- Multi-chain with Base and TON support

**Cons:**
- 1% sniper fee is on the higher end for frequent traders
- Web app (Banana Pro) still maturing — some chain/pair support gaps noted
- One significant exploit in its history (though fully refunded)

---

## 2. Trojan on Solana — Best Dedicated Solana Sniper

**Official bot:** @TrojanTradingBot on Telegram | **Website:** trojan.finance (verify on official site)

If your focus is exclusively Solana meme coins, Trojan is the bot most frequently cited in community discussions as the dedicated Solana specialist. While Banana Gun handles multiple chains, Trojan's architecture is optimized from the ground up for Solana's high-throughput, low-latency environment.

### Features

- **Instant token sniping** on Raydium and PumpFun at launch
- **Copy trading** — follow high-performing Solana wallets
- **DCA (Dollar-Cost Averaging)** — automated entry strategies over time
- **Limit orders and take-profit automation**
- **Anti-rug tools** — auto-sell on liquidity removal events
- **Referral program** — a 0.9% fee tier if you join via referral link (vs. standard 1%)

### Fee Structure

- Standard: **1%** per transaction
- With referral: **0.9%**
- Inviters receive **25% fee share** on referred user volume (similar model to Maestro)

The referral incentive creates a network of organic promoters, which helps explain Trojan's strong community presence across r/solana and r/CryptoCurrencyTrading.

### What Reddit Users Are Saying

> *"The best and fastest bot I've used so far has been Trojan — directly on Telegram. Just import your wallet, paste the CA, and it executes in under a second."*
> — u/Headbanger2021, r/solana

> *"For Telegram bot, check out Trojan on Solana, Maestro, SolTradingBot — these are your options if you want actual speed."*
> — u/Max_Xryptix99, r/solana

> *"I import my Solana wallet on a Telegram trading bot called Trojan bot. I copy paste the address of the memecoin I'm buying on Trojan and hit buy."*
> — u/LikkinBoots, r/CryptoIndia

### Pros and Cons

**Pros:**
- Purpose-built for Solana — architecture optimized for speed on one chain
- Strong community presence with active referral network
- DCA feature useful for scaling into positions
- No major security exploit on record

**Cons:**
- Solana-only — no Ethereum, Base, or other chain support
- Some users report execution lag during peak Solana network congestion
- 1% fee applies to all trades regardless of size

---

## 3. Maestro — Most Feature-Rich Multi-Chain Bot

**Official bot:** @MaestroSniperBot on Telegram | **Website:** maestrobots.com

Maestro is the veteran of the Telegram trading bot space and arguably the most feature-complete option available. Founded earlier than most competitors, it has processed over **$6.18 billion in lifetime volume** across **343,330 users** and completed **18.3 million lifetime trades** — making it one of the most battle-tested bots in the ecosystem.

### Networks

Maestro supports **nine blockchain networks**: Ethereum (ETH), Binance Smart Chain (BSC), Solana (SOL), Base, Avalanche (AVAX), Arbitrum, Metis, TON, and Linea. For traders operating across multiple ecosystems simultaneously, this breadth is Maestro's core value proposition.

### Key Features

- **Multi-chain sniper bot** — Lightning-fast entry on BSC, ETH, Arbitrum, Base, and Solana launches
- **Wallet and whale tracker** — Monitor up to 6 wallets; receive alerts on up to 3 whale transactions
- **Copy trading** — Follow wallets at high speed with auto-sell fraud protection
- **Anti-rug protection** — Automated exits on suspicious LP events
- **Call channel auto-buy** — Automatically execute buys when specific Telegram channels call a token
- **Multi-wallet management** — Up to 5 wallets, simultaneous purchases across all
- **AES encryption** — Data security at rest and in transit
- **Limit orders** and advanced slippage controls

### Fee Structure

- **1%** per trade (standard)
- Inviters receive **25% of fees** from referred users (same model as Trojan)

### Community Scores (Coinpedia)

| Category | Score |
|----------|-------|
| Overall | 8.3 / 10 |
| Features & Capabilities | 9.0 |
| Security & Privacy | 9.5 |
| Performance & Reliability | 8.5 |
| User Interface | 8.3 |
| Pricing | 7.5 |

### Pros and Cons

**Pros:**
- Broadest multi-chain support (9 networks)
- Most comprehensive feature set — whale tracking, call-channel auto-buy, multi-wallet
- Excellent incident response: 2023 exploit fully refunded in under 10 hours
- High security rating from independent reviewers

**Cons:**
- Interface can feel overwhelming for beginners
- Higher learning curve than BonkBot or Trojan
- 1% fee with no volume-based discount tier
- Solana features slightly less refined than Trojan's

---

## 4. BonkBot — Best for Beginners

**Official bot:** @bonkbot_io on Telegram | **Website:** bonkbot.io

BonkBot is the entry point for most new Solana meme coin traders. Where Maestro offers depth and complexity, BonkBot deliberately simplifies. Its core philosophy: fast, clean, Solana-native, and approachable for anyone who has never used a trading bot before.

### Features

- **Instant buys and sells** directly in Telegram
- **Auto-sniping** at new token launch
- **Limit orders** with price-triggered execution
- **Copy trading** — follow high-performing wallets
- **Rug pull protection** — auto-sell on suspicious liquidity events
- **MEV protection** — sandwiching resistance built in

### Fee Structure and BONK DAO Partnership

- **1%** per transaction
- **10% of all fees** are sent to the BONK DAO — creating a community-aligned revenue stream and a formal partnership with the broader Solana meme coin ecosystem

### Why Beginners Choose BonkBot

The interface is genuinely the most accessible in this list. New users can connect a wallet, fund it, and execute their first snipe in under three minutes. The Telegram menu structure is linear and self-explanatory — no configuration files, no complex dashboards, no API keys to manage.

Compared directly to Banana Gun: BonkBot lacks Banana Gun's cross-chain capability and more advanced copy trading configuration, but for a trader who only wants to trade Solana tokens quickly and simply, the reduced complexity is a genuine advantage.

### Pros and Cons

**Pros:**
- Simplest onboarding experience in the category
- MEV protection included by default
- Trusted partnership with BONK DAO
- Clean, minimal interface reduces user error
- No major exploit on record

**Cons:**
- Solana-only — no Ethereum or other chain support
- Fewer advanced features than Maestro or Banana Gun
- 1% fee with no discount tiers
- Copy trading less configurable than competitors

---

## 5. FOMO — Best for Hyperliquid Perpetuals

**Official bot:** @fomoapp_bot on Telegram (verify on official site) | **Website:** fomo.fund

FOMO occupies a unique niche in this list: it is the only bot here focused on **perpetual futures** rather than spot meme coin sniping. Built for the Hyperliquid L1 ecosystem, FOMO brings the speed and simplicity of Telegram-native trading to leveraged positions — a category that was previously only accessible through web interfaces.

*Note: As of late 2026, FOMO is operating in **Closed Beta**. Access requires an invitation or waitlist approval.*

### Networks and Features

- **Hyperliquid** perpetuals trading via Telegram
- Long/short positions with leverage from Telegram commands
- DCA and limit order support for perpetuals
- Portfolio tracking inside Telegram
- Risk management parameters configurable per position

### Fee Structure

- **0.1% per trade** — by far the lowest fee in this list
- Non-custodial: your Hyperliquid account keys stay under your control

### Backing and Context

FOMO is backed by **DWF Labs**, one of the more active crypto venture and market-making firms. This provides meaningful runway, credibility for a closed-beta product, and integration leverage with exchange liquidity partners.

The Hyperliquid ecosystem has grown substantially in 2025–2026, and FOMO's thesis is that Telegram-native access to on-chain perps will attract traders who want the execution quality of Hyperliquid without leaving their messaging app.

### Pros and Cons

**Pros:**
- Lowest fee in this list at 0.1%
- Unique focus on perpetuals opens leverage strategies unavailable on spot bots
- Backed by DWF Labs — strong institutional support
- Non-custodial model maintained

**Cons:**
- Currently Closed Beta — not publicly accessible
- Hyperliquid-only: no spot meme coin sniping
- No track record yet (relatively new)
- Perpetuals add liquidation risk that spot trading does not carry

---

## Honourable Mentions

**Sol Trading Bot (@SolTradingBot)** — A Solana-native bot favoured for its clean execution and 1% fee. Well-regarded in r/solana communities for reliability during congested network conditions.

**Sigma Bot** — A cross-chain bot gaining traction for multi-DEX routing across Ethereum, BSC, and Solana. Still establishing its community presence but worth monitoring for 2026.

**GMGN Sniper Bot** — Frequently mentioned alongside BullX and Photon as a web/Telegram hybrid platform. u/Solana_Chief on r/solana rated it "just average, nothing special" versus the leaders, but it has a dedicated user base for its token discovery features.

---

## What Reddit Really Says About Telegram Bots

Community sentiment across r/solana, r/CryptoCurrencyTrading, and r/CryptoIndia paints a nuanced picture. Here are real voices from the past 12 months:

> *"I'm testing and trying Solana trading bots all the time since I started with memecoins. Banana Gun: pretty decent, the second best for me. Trojan: slow, not happy with it. GMGN: just average, nothing special. BullX: too much hype and marketing."*
> — u/Solana_Chief, r/solana

> *"I ended up using Banana Gun the most lately. The copy trading is probably the best I've tested so far, especially for fast-moving Solana plays. Their fills are crazy fast too — you can actually notice it compared to slower bots when entering the same token with friends."*
> — u/MarieB_Schultz, r/CryptoCurrencyTrading

> *"There are a dozen platforms that can be used for automated trading on Solana. The most popular ones are Telegram bots such as BonkBot and Trojan. However, most of these are quite expensive in their fees and their advanced automated strategies aren't fully reliable."*
> — u/SniperooMonke, r/solana

> *"The interesting thing with Solana trading is that a lot of people moved from building their own bots to using specialized terminals or Telegram bots. Tools like Axiom, Photon, Trojan or Banana Gun basically act as trading interfaces on top of the DEX ecosystem."*
> — u/AffectionateTop8793, r/solana

> *"You don't use bots to buy memecoins on Phantom — that sentence doesn't make sense. Phantom is a wallet. A trading bot is a different platform, usually in Telegram. Examples of trading bots are Trojan, Photon and BullX."*
> — u/KofiUchiha, r/solana

One pattern emerges consistently: users value **execution speed above almost everything else**. A bot that fills 100ms faster than a competitor can mean the difference between a 5x and a 2x entry, particularly at launch. Fees matter, but speed is the primary differentiator the community focuses on.

---

## Bot Safety Checklist

Before connecting any Telegram bot to your wallet, run through this checklist:

**1. Verify the official handle**
Go to the project's verified website or their official Twitter/X account. Copy the exact bot username from there — do not click Telegram links from Reddit DMs, YouTube comments, or unsolicited messages. The fake bot epidemic of 2025–2026 has drained millions from traders who skipped this step.

**2. Understand the custody model**
Every bot in this list is non-custodial — you retain control of your private key. Confirm this before depositing. If a platform asks you to deposit funds to *their* wallet address, treat that as a red flag unless you have verified it is a legitimate custodial exchange (like Pionex).

**3. Never share your seed phrase**
No legitimate bot will ever ask for your 12- or 24-word seed phrase. If a "support agent" in a Telegram group asks for it, you are being scammed. Period.

**4. Use a dedicated trading wallet**
Keep a separate, lower-funded wallet specifically for bot trading. Never connect your primary cold storage wallet. This limits your maximum loss to what you've transferred into the hot wallet.

**5. Check for recent audit reports**
Reputable bots publish smart contract audits. Maestro, Banana Gun, and BonkBot all have public security documentation. If a bot has no audit record and is asking you to connect your wallet, skip it.

**6. Monitor social channels during incidents**
The fastest signal of an ongoing exploit is usually the project's official Telegram announcement channel or Twitter. Follow these channels — during the Banana Gun and Maestro incidents, the teams communicated within hours.

---

## How to Set Up a Sniper Bot: Step-by-Step

The following is a generic walkthrough applicable to most non-custodial Telegram bots:

**Step 1: Find the official bot**
Navigate to the project's official website (e.g., bananagun.io, bonkbot.io) and click the official Telegram link. **Do not search for the bot inside Telegram — always start from the verified website.**

**Step 2: Start the bot and create a wallet**
Send `/start` to the bot. Most bots will either generate a new wallet for you or prompt you to import an existing one using your private key (not seed phrase). Use a fresh, dedicated wallet for this step.

**Step 3: Fund the wallet**
Send the native chain token (SOL for Solana bots, ETH for Ethereum bots) to the wallet address shown by the bot. Keep amounts small until you're comfortable with the platform. Start with $50–$100 to learn the interface.

**Step 4: Configure basic settings**
Set your:
- **Buy amount** — how much to spend per trade
- **Slippage tolerance** — typically 10–25% for volatile meme coins
- **Gas / priority fee** — higher priority = faster execution but higher cost
- **Take profit levels** — e.g., sell 50% at 3x, 30% at 6x, hold 20%
- **Stop loss** — recommended at -30% to -50% to limit downside

**Step 5: Execute your first trade**
Copy the token contract address from a trusted source (DexScreener, GMGN, or a verified call channel). Paste it into the bot chat. The bot will display token details — confirm and execute.

**Step 6: Set up take-profit automation**
After entry, configure your exit rules immediately. Do not rely on manual monitoring in volatile markets. Most bots support limit-sell orders that execute automatically when your target price is hit.

**Step 7: Monitor and withdraw**
Regularly withdraw profits to cold storage. Never leave large balances in a hot trading wallet longer than necessary.

---

## FAQ

**Q: Are Telegram trading bots legal?**
In most jurisdictions, using automated trading bots for personal trading is legal. However, regulatory treatment of crypto trading tools varies by country. Consult local regulations before using these tools.

**Q: Can I lose all my money with a trading bot?**
Yes. Meme coins are highly speculative assets. A bot executes your strategy; it cannot make a fundamentally bad token profitable. Losses from bad trade decisions, rug pulls, or market conditions are not covered by most platforms.

**Q: Which bot is fastest on Solana?**
Community consensus and benchmark comparisons in 2026 most often cite Trojan and Banana Gun as the fastest execution options on Solana. Performance varies with network congestion — no bot is immune to Solana's periodic congestion events.

**Q: What's the difference between sniping and copy trading?**
Sniping means buying a token the moment it launches on a DEX — ideally within milliseconds of the liquidity pool opening. Copy trading means automatically mirroring the buys and sells of a chosen wallet. Both carry significant risk.

**Q: Do these bots work 24/7?**
Yes — automated bots run continuously as long as they are connected and funded. You don't need to be online for them to execute trades, which is both their main benefit and a key risk (you need to set appropriate stop losses and take-profit levels before going offline).

**Q: What happened to Unibot?**
Unibot was one of the early leaders in this space but suffered significant market share decline following its October 2023 exploit and changing user preferences. As of 2026, most of its former user base has migrated to Banana Gun, Trojan, or web-based terminals like BullX and Photon.

**Q: Is Pionex safe?**
Pionex is a legitimate, licensed exchange with grid trading bots built in. As a custodial platform, it holds user funds on-exchange — different risk profile to non-custodial bots. It is regulated in multiple jurisdictions and is not analogous to the Telegram bots in this article.

**Q: How do I report a fake/scam bot?**
Report the bot directly within Telegram (three-dot menu → Report) and post evidence in the official project's community channels. Projects actively hunt impersonation bots and can escalate removal requests to Telegram.

---

*Last updated: October 21, 2026. Fee rates and platform features are subject to change. Always verify current information on each project's official website before trading.*
