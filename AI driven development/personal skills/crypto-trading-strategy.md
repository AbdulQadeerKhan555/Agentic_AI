# Crypto Day Trading Strategy Skill

## Description
Provides actionable crypto trading signals for BTC/USDT and ETH/USDT on Binance Futures using 5-15 minute timeframes. Analyzes support/resistance, RSI, and volume to generate specific long/short entries with precise risk management.

## Trading Parameters
- **Exchange**: Binance Futures
- **Pairs**: BTC/USDT and ETH/USDT only
- **Timeframes**: 5-minute and 15-minute charts
- **Leverage**: 30x fixed (cross margin)
- **Total Wallet**: $200
- **Risk per Trade**: $2 (1% of wallet)
- **Reward per Trade**: $2-4 (1-2% of wallet)
- **Stop Loss**: 1% price move
- **Take Profit**: 1-2% price move (1:1 to 1:2 risk-reward)
- **Daily Limit**: Maximum 3 winning trades OR 3 losing trades (stop after either)
- **Trading Hours**: 8 AM - 8 PM

## Instructions

When this skill is invoked, follow these steps:

### Step 1: Market Analysis
Analyze current market conditions for BTC/USDT and ETH/USDT:

1. **Support & Resistance Levels**:
   - Identify key support levels (price floors where buying pressure increases)
   - Identify key resistance levels (price ceilings where selling pressure increases)
   - Look for recent swing highs/lows on 5-min and 15-min charts
   - Note horizontal levels where price has bounced multiple times

2. **RSI Analysis** (14-period):
   - Check RSI on both 5-min and 15-min timeframes
   - Oversold: RSI < 30 (potential long opportunity)
   - Overbought: RSI > 70 (potential short opportunity)
   - Look for divergences (price makes new low but RSI makes higher low = bullish)

3. **Volume Analysis**:
   - Compare current volume to average volume
   - High volume at support = strong buying interest (bullish)
   - High volume at resistance = strong selling interest (bearish)
   - Volume confirmation is required for all signals

### Step 2: Generate Trade Signals

For each valid setup, provide:

**Signal Format:**
```
PAIR: [BTC/USDT or ETH/USDT]
DIRECTION: [LONG or SHORT]
TIMEFRAME: [5-min or 15-min]
ENTRY PRICE: $[exact price]
STOP LOSS: $[exact price] (1% from entry)
TAKE PROFIT 1: $[exact price] (1% from entry)
TAKE PROFIT 2: $[exact price] (2% from entry)

POSITION SIZING:
- Margin Required: $6.67 (with 30x leverage)
- Position Size: $200 (30x × $6.67)
- Risk Amount: $2 (1% of wallet)
- Potential Profit: $2-4 (1-2% of wallet)

SETUP REASONING:
[Explain the support/resistance level, RSI reading, and volume confirmation]

RISK-REWARD: 1:[1 or 2]
```

**Entry Criteria (ALL must be met):**
- Clear support (for longs) or resistance (for shorts) level
- RSI confirmation (oversold for longs, overbought for shorts, or divergence)
- Volume spike or above-average volume
- Price action showing rejection or bounce at key level
- Clean setup with clear invalidation point

**Do NOT provide signals if:**
- Market is choppy/ranging without clear levels
- Volume is too low
- RSI is neutral (40-60 range)
- No clear risk-reward setup

### Step 3: Risk Management Guidance

Provide specific risk management advice:

1. **Position Management**:
   - Never risk more than $2 per trade
   - Use exactly 30x leverage with $6.67 margin per trade
   - Always set stop loss immediately after entry
   - Consider scaling out: close 50% at TP1, let 50% run to TP2

2. **Daily Trading Rules**:
   - Stop trading after 3 winning trades (lock in profits)
   - Stop trading after 3 losing trades (prevent revenge trading)
   - Maximum daily loss: $6 (3% of wallet)
   - Maximum daily profit target: $6-12 (3-6% of wallet)

3. **Emotional Discipline**:
   - Never move stop loss further away
   - Don't chase price after missing entry
   - Take breaks between trades
   - If feeling emotional, stop trading for the day

4. **Market Conditions to Avoid**:
   - Major news events (FOMC, CPI, etc.)
   - Extremely low liquidity periods
   - When price is between support and resistance (no clear direction)
   - After hitting daily trade limit

### Step 4: Trading Opportunities

Scan BTC/USDT and ETH/USDT for current opportunities:

**Present findings as:**
```
CURRENT OPPORTUNITIES:

BTC/USDT:
- Current Price: $[price]
- Trend: [Bullish/Bearish/Neutral]
- Key Support: $[price]
- Key Resistance: $[price]
- RSI (5-min): [value]
- RSI (15-min): [value]
- Volume: [Above/Below average]
- Setup Quality: [Strong/Moderate/Weak/None]
- Recommendation: [LONG/SHORT/WAIT]

ETH/USDT:
- Current Price: $[price]
- Trend: [Bullish/Bearish/Neutral]
- Key Support: $[price]
- Key Resistance: $[price]
- RSI (5-min): [value]
- RSI (15-min): [value]
- Volume: [Above/Below average]
- Setup Quality: [Strong/Moderate/Weak/None]
- Recommendation: [LONG/SHORT/WAIT]
```

Only provide detailed trade signals for "Strong" setups. For "Moderate" setups, explain what's missing. For "Weak/None", advise to wait.

### Step 5: Trading Journal

Create or update a CSV file named `crypto_trading_journal.csv` with the following columns:

```csv
Date,Time,Pair,Direction,Entry_Price,Stop_Loss,Take_Profit_1,Take_Profit_2,Exit_Price,Result,Profit_Loss_USD,Profit_Loss_Percent,Margin_Used,Position_Size,Leverage,RSI_Entry,Setup_Type,Notes,Running_Balance
```

**Column Definitions:**
- **Date**: YYYY-MM-DD
- **Time**: HH:MM (24-hour format)
- **Pair**: BTC/USDT or ETH/USDT
- **Direction**: LONG or SHORT
- **Entry_Price**: Actual entry price
- **Stop_Loss**: Stop loss price
- **Take_Profit_1**: First take profit target (1%)
- **Take_Profit_2**: Second take profit target (2%)
- **Exit_Price**: Actual exit price
- **Result**: WIN/LOSS/BREAKEVEN
- **Profit_Loss_USD**: Dollar amount gained/lost
- **Profit_Loss_Percent**: Percentage of wallet
- **Margin_Used**: Amount of margin used ($6.67 typically)
- **Position_Size**: Total position size with leverage
- **Leverage**: 30x
- **RSI_Entry**: RSI value at entry
- **Setup_Type**: Support_Bounce, Resistance_Rejection, RSI_Divergence, etc.
- **Notes**: Brief notes about the trade
- **Running_Balance**: Wallet balance after trade

**Journal Management:**
- If file doesn't exist, create it with headers
- Add new trade entries as they occur
- Calculate running balance automatically
- Provide daily/weekly statistics on request

## Output Format

Always structure your response as:

```
🎯 CRYPTO TRADING ANALYSIS
Date: [Current Date]
Time: [Current Time]

═══════════════════════════════════════
MARKET OVERVIEW
═══════════════════════════════════════
[Market analysis for BTC and ETH]

═══════════════════════════════════════
TRADE SIGNALS
═══════════════════════════════════════
[Detailed signals if available, or "NO CLEAR SETUPS - WAIT"]

═══════════════════════════════════════
RISK MANAGEMENT REMINDER
═══════════════════════════════════════
✓ Max risk per trade: $2 (1% of wallet)
✓ Daily trade limit: 3 wins OR 3 losses
✓ Current trades today: [X/3]
✓ Today's P&L: $[amount]
✓ Remaining daily risk: $[amount]

═══════════════════════════════════════
TRADING JOURNAL STATUS
═══════════════════════════════════════
[Journal update confirmation or statistics]
```

## Important Notes

- **NEVER recommend trades without all three confirmations**: support/resistance + RSI + volume
- **ALWAYS calculate exact entry, stop loss, and take profit prices**
- **ALWAYS remind user of daily trade limits**
- **NEVER suggest increasing risk or leverage beyond parameters**
- **Quality over quantity**: It's better to wait for perfect setups than force trades
- **This is high-risk trading**: 30x leverage can lead to quick losses if not managed properly
- **Preserve capital**: The goal is consistent small wins, not home runs

## Distinctive Approach

This strategy focuses exclusively on:
- **Crypto-only**: Deep focus on BTC and ETH behavior patterns
- **Conservative risk**: Only 1% risk per trade despite using leverage
- **Strict discipline**: Hard daily limits prevent emotional trading
- **Capital preservation**: $200 wallet with only $6.67 margin per trade
- **High probability setups**: Wait for all three indicators to align
- **Scalping approach**: Quick 1-2% moves on 5-15 min charts

## Safety Warnings

⚠️ **CRITICAL REMINDERS:**
1. 30x leverage amplifies both gains AND losses
2. Cross margin means entire $200 backs all positions
3. Crypto markets are 24/7 and highly volatile
4. Stop losses can slip during extreme volatility
5. Never trade during major news events
6. This strategy requires active monitoring during trading hours
7. Past performance does not guarantee future results

---

**Skill Version**: 1.0
**Last Updated**: 2026-01-16
**Risk Level**: High (30x leverage)
**Recommended Experience**: Intermediate to Advanced
