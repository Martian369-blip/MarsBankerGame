# Create a fresh repository named 'mars_banker_game' with this script saved as 'app.py'
import streamlit as st
import random
import time

# --- INITIALIZATION MATRIX ---
st.set_page_config(page_title="QUANT REBEL: Institutional Horizon", page_icon="💼", layout="centered")

# ==================== ADVANCED SMART CASUAL INTUITION THEME ====================
st.markdown("""
    <style>
    .terminal-card {
        background: linear-gradient(135deg, #111622 0%, #070a10 100%);
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #1e293b;
        color: #e2e8f0;
        font-family: 'Segoe UI', sans-serif;
    }
    .hud-title {
        color: #ff9900;
        font-family: monospace;
        font-weight: bold;
        font-size: 14px;
        letter-spacing: 1.5px;
    }
    .metric-value {
        font-size: 26px;
        font-weight: bold;
        color: #ffffff;
        font-family: monospace;
    }
    .log-bubble {
        background-color: #0f141f;
        padding: 12px;
        border-radius: 6px;
        border-left: 4px solid #3b82f6;
        margin-bottom: 8px;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

# --- GAME SESSION MEMORY SPACE ---
if "game_state" not in st.session_state:
    st.session_state.game_state = {
        "level": 1,  # 1: Junior Desks, 2: VP Macro Desk, 3: Managing Director Co-Head
        "bank_profits": 2500000.00,  # Goal is $1,000,000,000.00
        "personal_wallet": 45000.00,  # Local personal lifestyle funds
        "stress_pct": 18.5,  # Max 100% (Actuarial Probability of System Failure)
        "family_sync": 85.0,  # Min 0% (Relationship Liquidation Floor)
        "years_elapsed": 0.0,
        "current_outfit": "Tailored navy chinos, white Egyptian cotton shirt (unbuttoned collar), leather loafers.",
        "logs": ["📌 System Initialization. BCom Economics & Actuarial Science majors confirmed. Vault cleared."]
    }

gs = st.session_state.game_state

# Level Definitions Metadata Array
level_map = {
    1: {"title": "Junior Derivative Scalper (FX & JSE Vaults)", "cap_requirement": "$2.5M Baseline", "next_gate": 25000000.00},
    2: {"title": "Vice President of Macro Strategy (London/NY Cross Desks)", "cap_requirement": "$25M Gate", "next_gate": 250000000.00},
    3: {"title": "Managing Director & Global Head of Arbitrage Flow", "cap_requirement": "$250M Ceiling", "next_gate": 1000000000.00}
}

# Dynamic Rank Engine Controller
if gs["bank_profits"] >= level_map[1]["next_gate"] and gs["level"] == 1:
    gs["level"] = 2
    gs["logs"].insert(0, "🏆 RANK PROMOTION: FSCA & Bank Executive board approves your move to VP Macro Desks!")
if gs["bank_profits"] >= level_map[2]["next_gate"] and gs["level"] == 2:
    gs["level"] = 3
    gs["logs"].insert(0, "🏆 RANK PROMOTION: Promoted to Managing Director. Global asset vaults unlocked.")

def execute_quant_cycle(choice_type):
    """Applies pure numerical actuarial logic matrices to choices."""
    gs["years_elapsed"] += 0.25  # 1 quarter elapsed
    
    if choice_type == "TRADE_ALGO":
        # High probability probability curves
        success_prob = 0.62 if gs["level"] == 1 else 0.55 if gs["level"] == 2 else 0.48
        variance_multiplier = 1.8 if gs["level"] == 1 else 12.5 if gs["level"] == 2 else 115.0
        base_swing = random.uniform(100000, 450000) * variance_multiplier
        
        if random.random() < success_prob:
            gs["bank_profits"] += base_swing
            bonus = base_swing * 0.03  # 3% Personal performance bonus allocation
            gs["personal_wallet"] += bonus
            gs["stress_pct"] += 8.2
            gs["family_sync"] -= 4.5
            gs["logs"].insert(0, f"📈 QUANT WIN: Executed a statistical arbitrage trade. Captured +${base_swing:,.2f} for the bank. Allocation Bonus: +${bonus:,.2f}.")
        else:
            loss_swing = base_swing * 0.85
            gs["bank_profits"] -= loss_swing
            gs["stress_pct"] += 14.5
            gs["family_sync"] -= 3.0
            gs["logs"].insert(0, f"📉 VOLATILITY DROP: Federal Reserve rate pivot caused variance skew. Lost -${loss_swing:,.2f} bank liquidity.")

    elif choice_type == "FAMILY_HOLIDAY":
        # De-stress capital allocation cycle
        cost = 12000.00 if gs["level"] == 1 else 45000.00 if gs["level"] == 2 else 120000.00
        if gs["personal_wallet"] >= cost:
            gs["personal_wallet"] -= cost
            gs["stress_pct"] = max(5.0, gs["stress_pct"] - 35.0)
            gs["family_sync"] = min(100.0, gs["family_sync"] + 25.0)
            gs["logs"].insert(0, f"🏝️ HOLIDAY ROUTINE: Fly to Mauritius/French Riviera. Outfit update: Premium linen shorts and polarized sunglasses. Actuarial family breakdown probability dropped to safe limits.")
        else:
            gs["logs"].insert(0, "❌ INSUFFICIENT LIQUIDITY: Personal cash account balance insufficient for luxury holiday parameters.")

    elif choice_type == "NETWORKING_FRIENDS":
        # Stabilize macro relations
        gs["personal_wallet"] -= 2500.00
        gs["stress_pct"] = max(5.0, gs["stress_pct"] - 10.0)
        gs["logs"].insert(0, "🥃 BRAIN TRUST SESSION: Single malt whiskies with Actuarial friends. Calculated the inflation-adjusted probability of local real estate yield shifts. Stress mitigated.")

    # Game Over Conditions check
    if gs["stress_pct"] >= 100.0:
        gs["logs"].insert(0, "🚨 SYSTEM FAILURE: Actuarial burnout threshold hit 100%. Executive health collapse.")
    if gs["family_sync"] <= 0.0:
        gs["logs"].insert(0, "🚨 LIFE LIQUIDATION: Family relationship synchronization hit 0%. Divorced, asset registry halved.")

# ==================== MAIN GAME BOARD INTERFACE ====================
st.title("💼 QUANT REBEL: THE $1B VAULT ENGINE")
st.caption("Majors: BCom Economics & Actuarial Science. Everything is numbers. Maximize bank profit to win.")

# HUD TOP DISPLAY PANEL
st.markdown("<div class='terminal-card'>", unsafe_allow_html=True)
st.markdown(f"<span class='hud-title'>CURRENT OPERATIONAL LEVEL 0{gs['level']}: {level_map[gs['level']]['title'].upper()}</span>", unsafe_allow_html=True)

h_col1, h_col2 = st.columns(2)
with h_col1:
    st.markdown(f"🏛️ **Institutional Bank Profits:**<br><span class='metric-value'>${gs['bank_profits']:,.2f}</span> / $1B Goal", unsafe_allow_html=True)
    st.markdown(f"💵 **Personal Checking Wallet:**<br><span class='metric-value'>${gs['personal_wallet']:,.2f}</span>", unsafe_allow_html=True)
with h_col2:
    st.markdown(f"🧠 **Actuarial Stress Load:**<br><span class='metric-value'>{gs['stress_pct']:.1f}%</span> / 100% Limit", unsafe_allow_html=True)
    st.markdown(f"🏡 **Family Sync Floor:**<br><span class='metric-value'>{gs['family_sync']:.1f}%</span> / 0% Floor", unsafe_allow_html=True)

st.markdown(f"<small style='color: #7f8c8d;'>👔 <b>Smart Casual Attire Matrix:</b> {gs['current_outfit']} | Timeline: Year {gs['years_elapsed']:.2f}</small>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# EVALUATE DYNAMIC WIN/LOSS THRESHOLDS
if gs["bank_profits"] >= 1000000000.00:
    st.balloons()
    st.success("🏆 **THE ACTUARIAL BILLION-TRADER CEILING REACHED!** You cracked the $1,000,000,000.00 institutional matrix! You are a legendary sovereign allocator.")
    if st.button("🔄 RETIRE & RESET VAULT"):
        st.session_state.clear()
        st.rerun()
elif gs["stress_pct"] >= 100.0 or gs["family_sync"] <= 0.0:
    st.error("🚨 **RISK REGIME LIQUIDATED (GAME OVER)**: Your personal statistics hit catastrophic boundaries.")
    if st.button("🔄 LOAD RE-DEPOSIT BACKUP FILE"):
        st.session_state.clear()
        st.rerun()
else:
    # ACTION CONTROL GRID KEYS
    st.write("### 💻 Choose Quarter Execution Decision:")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("📈 RUN ARBITRAGE BLOCK", use_container_width=True):
            execute_quant_cycle("TRADE_ALGO")
            st.rerun()
    with c2:
        if st.button("🏝️ BUY FAMILY HOLIDAY", use_container_width=True):
            execute_quant_cycle("FAMILY_HOLIDAY")
            st.rerun()
    with c3:
        if st.button("🥃 NETWORKING NIGHT OUT", use_container_width=True):
            execute_quant_cycle("NETWORKING_FRIENDS")
            st.rerun()

st.divider()
st.markdown("### 📡 Live Feed Telemetry Ledger")
for log in gs["logs"][:4]:
    st.markdown(f"<div class='log-bubble'>{log}</div>", unsafe_allow_html=True)
