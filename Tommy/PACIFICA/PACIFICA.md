# Pacifica Review 2026: Complete Beginner's Guide to the Solana Perps DEX

> Hands-on public-interface review, last checked October 19, 2026. This is educational content, not financial advice. Perpetuals and leverage can cause rapid losses.

Pacifica is a Solana-based trading platform that combines perpetuals and spot with a CEX-like order ticket, managed Vaults, a Points programme, Print and Swim. In this public walkthrough, the interface loaded without a wallet, but it displayed a restricted-jurisdiction notice. No wallet was connected, no deposit was made, and no order was submitted.

**Quick take:** Pacifica has a broad product surface and a capable trading terminal. The important caveats are regional eligibility, leverage and liquidation risk, dynamic points rules, and the difference between visible headline volume and executable liquidity for a particular order size.

## What is Pacifica?

Pacifica describes its product as a high-performance decentralized trading platform launched in June 2025. Its documentation positions perpetuals and spot as core products, with a hybrid approach: a fast order-book experience alongside Solana-based deposits, withdrawals and settlement. Read the [official trading overview](https://docs.pacifica.fi/trading-on-pacifica/overview) before funding an account.

The visible app navigation includes Trade, Print, Swim, Portfolio, Vaults, Points, Leaderboard and Referral. The product breadth is useful, but each feature has distinct risks and eligibility conditions.

## Device views

The desktop view presents the chart, order book, ticket and positions together. Tablet and phone views remain useful for monitoring, but a larger screen is less error-prone for managing a leveraged trade.

![Pacifica desktop trade terminal with BTC chart, order book and ticket](pacifica-assets/pacifica-live-desktop.png)

*Desktop capture: chart, order book, ticket and position panel are visible in one workspace.*

![Pacifica tablet trade terminal](pacifica-assets/pacifica-live-tablet.png)

*Tablet capture: the same trading surface at a narrower viewport.*

![Pacifica phone trade terminal](pacifica-assets/pacifica-live-phone.png)

*Phone capture: useful for checking the market, though complex order entry is easier to review on a larger screen.*

## Core features

### Perpetuals and spot

Pacifica supports USDC-denominated perpetual and spot trading. The interface exposes market and oracle prices, 24-hour change and volume, open interest, funding information, a chart, a central order book, and an order ticket.

### Advanced order tooling

The documentation describes Market, Limit, Stop Market, Stop Limit, TWAP, Scale, Chase, Conditional, OCO, Trailing Stop, Swarm, Trigger Swarm and Atomic orders. Those tools can help with execution planning but do not remove slippage, liquidation or operational risk.

### Print, Swim, Vaults and Neptune

Pacifica also exposes Print, Swim, Vaults and related strategy products. Treat each product’s mechanics, eligibility and reward terms separately rather than assuming a single risk profile across the platform.

## Markets and the live trading surface

| Visible area | What it shows | Why it matters |
| --- | --- | --- |
| Market header | Mark/oracle price, 24-hour change, volume and open interest | A quick activity and price-reference check |
| Chart | Timeframes, indicators, depth, liquidation heatmap and funding views | Context before entering or managing exposure |
| Order book | Bid/ask levels, spread and displayed size | Visible liquidity, not a guarantee of execution |
| Order ticket | Cross/isolated selection, leverage, order type and risk fields | Inputs that materially change liquidation risk |

![Pacifica market chart](pacifica-assets/pacifica-step2-market-chart.png)

*Live Trade capture: chart and market data were publicly visible.*

![Pacifica order book and order ticket](pacifica-assets/pacifica-step3-orderbook-ticket.png)

*Live Trade capture: the order book and ticket were visible, while the ticket stated that trading was unavailable in the captured region.*

![Pacifica positions panel](pacifica-assets/pacifica-step4-positions-panel.png)

*Live Trade capture: positions, open orders, strategies and history tabs appear below the main terminal.*

## Fees, margin, funding and liquidation

Pacifica’s documentation lists Tier 1 fees of 0.015% maker and 0.040% taker, with lower tiers at higher trailing volume. Funding, spread, slippage and liquidation costs are separate from the displayed trading fee.

For a $1M notional trade, a one-way Tier 1 taker fee is about $400 before funding and slippage; a round trip is about $800. A maker order can be cheaper, but it may not fill. Always check current rates in the [official fee schedule](https://docs.pacifica.fi/trading-on-pacifica/trading-fees).

Cross margin shares collateral across positions; isolated margin limits collateral to a position. Neither mode makes a highly leveraged trade safe. Before submitting an eligible trade, verify the order type, leverage, liquidation price, available margin, slippage and funding exposure.

## Step-by-step: how to approach the app safely

### 1. Open the app and check eligibility

![Pacifica app opening screen](pacifica-assets/pacifica-step1-open-app.png)

*The public interface can be visible before wallet connection.*

Start at [app.pacifica.fi](https://app.pacifica.fi/), read any access notice, and do not try to circumvent geographic restrictions.

### 2. Select a market and read the header

Check the mark and oracle price, 24-hour activity, open interest and upcoming funding before looking at an order ticket.

### 3. Choose margin, leverage and order type

For an eligible user, decide between Cross and Isolated margin and use the smallest reasonable leverage. A market order prioritizes execution, while a limit order prioritizes price but may not fill.

### 4. Review positions and liquidation fields

Use the positions, open-orders and funding sections to confirm the account state. Do not rely on a green PnL figure alone: liquidation price and available margin matter.

### 5. Connect a wallet only if eligible

![Pacifica regional warning in the live interface](pacifica-assets/pacifica-step5-location-warning.png)

*The captured interface showed a restricted-jurisdiction banner and an unavailable-trading warning. This review did not connect a wallet, deposit or submit an order.*

Pacifica documents Solana-compatible wallets and USDC funding. Review its [deposits and withdrawals guide](https://docs.pacifica.fi/trading-on-pacifica/deposits-and-withdrawals) for current minimums, fees and limits before moving funds.

## Points and referrals

Pacifica’s Points programme documents weekly allocations and periodic snapshots, but its formula is dynamic and intentionally opaque. The official documentation does not confirm a token, TGE date or a points-to-token conversion rate. Do not describe points as guaranteed value.

![Pacifica Points page](pacifica-assets/pacifica-points-live.png)

*Live Points capture: the public page loaded with the regional notice present; account-specific results remain wallet-gated.*

The referral programme has separate eligibility and reward conditions. Review the [Points programme](https://docs.pacifica.fi/programs/points-program) and [referral programme](https://docs.pacifica.fi/programs/referral-and-affiliate-program) for the current rules.

## Vaults, delivery context and security

![Pacifica Vaults interface](pacifica-assets/pacifica-funding-team-live.png)

*Live Vaults capture: managed-vault listings and platform status were publicly visible.*

The platform documentation describes a wider ecosystem, but product availability does not replace due diligence. Pacifica publishes a [BlockSec audit report](https://raw.githubusercontent.com/blocksecteam/audit-reports/main/rust/blocksec_pacifica_fi_perp_contracts_signed_20250424.pdf); an audit is useful review evidence, not a guarantee against smart-contract, oracle, liquidity, custody or liquidation failures.

## Independent market context

![DefiLlama public dashboard](pacifica-assets/pacifica-independent-defillama.png)

*DefiLlama public dashboard capture. Protocol metrics are live and should be refreshed from the [Pacifica protocol page](https://defillama.com/protocol/pacifica) before publication or investment use.*

Headline protocol volume is not equivalent to the depth available to your exact order. Compare the spread, visible book levels, expected price impact and liquidation path for the market you intend to trade.

## Pacifica compared with other perp venues

Pacifica is most naturally compared with Solana-native trading venues and order-book perpetual DEXs. Hyperliquid and dYdX are order-book benchmarks; GMX has a different, pool-based model; Jupiter and Drift are closer Solana ecosystem references. Compare current market depth and trading costs rather than making a choice based only on brand familiarity or historical volume.

## Conclusion

Pacifica is more than a points-farming interface: the public terminal shows market data, an order book, risk controls and a broader product suite. That breadth also raises the due-diligence burden. Verify regional eligibility first, read the current documentation, test only with an amount you can afford to lose, and use conservative leverage.

## FAQs

### What is Pacifica?

Pacifica is a Solana-based decentralized trading platform offering perpetuals, spot trading and adjacent products such as Vaults, Points, Print and Swim.

### What are Pacifica’s trading fees?

The review cites a documented Tier 1 rate of 0.015% maker and 0.040% taker. Check the [current fee schedule](https://docs.pacifica.fi/trading-on-pacifica/trading-fees) before trading.

### Does Pacifica have an airdrop?

Pacifica has a points programme, but its documentation does not confirm a token, TGE date or conversion ratio. Treat potential rewards as speculative.

### Which wallet and network does Pacifica use?

Pacifica uses Solana-compatible wallet access and USDC funding, subject to eligibility and the platform’s current rules.

## Quick links

- [Pacifica app](https://app.pacifica.fi/)
- [Pacifica docs](https://docs.pacifica.fi/)
- [Trading overview](https://docs.pacifica.fi/trading-on-pacifica/overview)
- [Points programme](https://docs.pacifica.fi/programs/points-program)
- [Fees](https://docs.pacifica.fi/trading-on-pacifica/trading-fees)
- [Liquidations](https://docs.pacifica.fi/trading-on-pacifica/liquidations)
