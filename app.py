import streamlit as st
import random
import time

# --- INITIALIZATION MATRIX ---
st.set_page_config(page_title="QUANT REBEL: Animated Horizon", page_icon="💼", layout="centered")

# ==================== INSTITUTIONAL ANIMATION THEME LAYOUT ====================
st.markdown("""
    <style>
    .terminal-card {
        background: linear-gradient(135deg, #111622 0%, #070a10 100%);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1e293b;
        color: #e2e8f0;
        font-family: 'Segoe UI', sans-serif;
    }
    .hud-title {
        color: #ff9900;
        font-family: monospace;
        font-weight: bold;
        font-size: 13px;
        letter-spacing: 1.5px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
        font-family: monospace;
    }
    .log-bubble {
        background-color: #0f141f;
        padding: 10px;
        border-radius: 6px;
        border-left: 4px solid #3b82f6;
        margin-bottom: 6px;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

# --- GAME SESSION MEMORY SPACE ---
if "game_state" not in st.session_state:
    st.session_state.game_state = {
        "level": 1,
        "bank_profits": 2500000.00,
        "personal_wallet": 45000.00,
        "stress_pct": 18.5,
        "family_sync": 85.0,
        "years_elapsed": 0.0,
        "character_sprite": "🤵‍♂️",  # Default starting character emoji asset state
        "current_outfit": "Navy Chinos, White Egyptian Cotton Shirt, Leather Loafers",
        "current_scene": "🏢 JSE Trading Vault Desk Panel",
        "logs": ["📌 Quant Matrix Loaded. BCom Economics & Actuarial Science parameters active."]
    }

gs = st.session_state.game_state

level_map = {
    1: {"title": "Junior Derivative Scalper", "next_gate": 25000000.00},
    2: {"title": "Vice President of Macro Strategy", "next_gate": 250000000.00},
    3: {"title": "Managing Director & Global Head", "next_gate": 1000000000.00}
}

# Dynamic Promotion & Animation Sprite Switch Matrix
if gs["bank_profits"] >= level_map["next_gate"] and gs["level"] == 1:
    gs["level"] = 2
    gs["character_sprite"] = "👑"
    gs["current_outfit"] = "Tailored Charcoal Suit, Unbuttoned Silk Shirt, Polarized Glasses"
    gs["current_scene":] = "🇬🇧 London Macro Trading Desk Floor"
    gs["logs"].insert(0, "🏆 LEVEL UP: Promoted to VP! Unlocked the London Macro Suite.")
    
if gs["bank_profits"] >= level_map["next_gate"] and gs["level"] == 2:
    gs["level"] = 3
    gs["character_sprite"] = "🛸"
    gs["current_outfit"] = "Bespoke Midnight Tuxedo, Rose Gold Patek Philippe Chronograph"
    gs["current_scene"] = "🏙️ New York Hex-Screen Arbitrage Vault"
    gs["logs"].insert(0, "🏆 LEVEL UP: Promoted to Global MD! The Billion-Dollar Vault is online.")

def execute_quant_cycle(choice_type):
    gs["years_elapsed"] += 0.25
    
    if choice_type == "TRADE_ALGO":
        success_prob = 0.62 if gs["level"] == 1 else 0.55 if gs["level"] == 2 else 0.48
        variance = 1.8 if gs["level"] == 1 else 12.5 if gs["level"] == 2 else 115.0
        swing = random.uniform(100000, 450000) * variance
        
        if random.random() < success_prob:
            gs["bank_profits"] += swing
            bonus = swing * 0.03
            gs["personal_wallet"] += bonus
            gs["stress_pct"] += 9.5
            gs["family_sync"] -= 5.0
            gs["logs"].insert(0, f"📈 ALGO WIN: Scalped the volatility curve! +${swing:,.2f} bank returns. Bonus +${bonus:,.2f}")
        else:
            loss = swing * 0.85
            gs["bank_profits"] -= loss
            gs["stress_pct"] += 15.0
            gs["family_sync"] -= 3.5
            gs["logs"].insert(0, f"📉 SKEW DROP: Arbitrage model hit tail-risk variance block. Lost -${loss:,.2f}")

    elif choice_type == "FAMILY_HOLIDAY":
        cost = 12000.00 if gs["level"] == 1 else 45000.00 if gs["level"] == 2 else 120000.00
        if gs["personal_wallet"] >= cost:
            gs["personal_wallet"] -= cost
            gs["stress_pct"] = max(5.0, gs["stress_pct"] - 35.0)
            gs["family_sync"] = min(100.0, gs["family_sync"] + 30.0)
            # Temporary Scene Animation Change
            gs["logs"].insert(0, f"🏝️ VACATION CYCLE: Flew to private villa islands. Stress levels dropped safely.")
        else:
            gs["logs"].insert(0, "❌ LIQUIDITY ERROR: Personal checking account funds insufficient for luxury holiday flight.")

    elif choice_type == "NETWORKING_FRIENDS":
        gs["personal_wallet"] -= 2500.00
        gs["stress_pct"] = max(5.0, gs["stress_pct"] - 12.0)
        gs["logs"].insert(0, "🥃 WHISKEY GLASSES NETWORK: Logged macro trends with fellow actuarial science minds.")

# ==================== VISUAL ANIMATION CANVAS INJECTION GRID ====================
# This HTML block renders a dynamic visual gameplay window inside the browser
st.markdown("### 🖥️ LIVE ACTION INTERFACE VIEWPORT")

# Dynamic status color logic matrix calculations
stress_color = "#ef5350" if gs["stress_pct"] > 65 else "#ff9900" if gs["stress_pct"] > 40 else "#26a69a"
family_color = "#ef5350" if gs["family_sync"] < 40 else "#26a69a"

st.components.v1.html(
    f"""
    <div style="background-color: #0c0e14; border: 2px solid #232936; border-radius: 12px; padding: 20px; font-family: monospace; color: white;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #232936; padding-bottom: 10px; margin-bottom: 15px;">
            <span style="color: #787b86; font-size: 11px;">🌍 YEAR: {gs['years_elapsed']:.2f}</span>
            <span style="background-color: #26a69a; color: white; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold;">{gs['current_scene']}</span>
        </div>
        
        <!-- MAIN ANIMATION STAGE BLOCK CONTAINER -->
        <div style="text-align: center; padding: 30px 10px; background: radial-gradient(circle, #1a2233 0%, #0d111a 100%); border-radius: 8px; margin-bottom: 15px; position: relative;">
            <div style="font-size: 70px; margin-bottom: 10px; animation: bounce 1s infinite alternate;">{gs['character_sprite']}</div>
            <div style="font-size: 11px; color: #ff9900; font-weight: bold; text-transform: uppercase;">Actuary Level 0{gs['level']} Spec</div>
            <div style="font-size: 10px; color: #787b86; margin-top: 4px;">👔 Style Matrix: {gs['current_outfit']}</div>
        </div>
        
        <!-- LIVE TICKING INTERACTIVE HEALTH PROGRESS BARS -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; font-size: 12px;">
            <div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span>🧠 STRESS METER</span>
                    <span style="color: {stress_color}; font-weight: bold;">{gs['stress_pct']:.1f}%</span>
                </div>
                <div style="width: 100%; background-color: #1a202c; height: 8px; border-radius: 4px; overflow: hidden;">
                    <div style="width: {gs['stress_pct']}%; background-color: {stress_color}; height: 100%; transition: width 0.4s ease;"></div>
                </div>
            </div>
            <div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span>🏡 FAMILY SYNC</span>
                    <span style="color: {family_color}; font-weight: bold;">{gs['family_sync']:.1f}%</span>
                </div>
                <div style="width: 100%; background-color: #1a202c; height: 8px; border-radius: 4px; overflow: hidden;">
                    <div style="width: {gs['family_sync']}%; background-color: {family_color}; height: 100%; transition: width 0.4s ease;"></div>
                </div>
            </div>
        </div>
    </div>
    
    <style>
    @keyframes bounce {{
        from {{ transform: translateY(0); }}
        to {{ transform: translateY(-8px); }}
    }}
    </style>
    """, height=280
)

# ==================== HUD NUMERICAL LEDGER PANEL ====================
st.markdown("<div class='terminal-card'>", unsafe_allow_html=True)
h_col1, h_col2 = st.columns(2)
with h_col1:
    st.markdown(f"🏛️ **Institutional Bank Profits:**<br><span class='metric-value'>${gs['bank_profits']:,.2f}</span> / $1B", unsafe_allow_html=True)
with h_col2:
    st.markdown(f"💵 **Personal Balance Wallet:**<br><span class='metric-value'>${gs['personal_wallet']:,.2f}</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# EVALUATE TERMINAL CONDITIONS (WIN / LOSS SKEWS)
if gs["bank_profits"] >= 1000000000.00:
    st.balloons()
    st.success("🏆 **THE ACTUARIAL BILLION-TRADER CEILING CRACKED!** You maximized the $1,000,000,000.00 banking matrix! Absolute legendary allocation status.")
    if st.button("🔄 RETIRE & RESET QUANT VAULT"):
        st.session_state.clear()
        st.rerun()
elif gs["stress_pct"] >= 100.0 or gs["family_sync"] <= 0.0:
    st.error("🚨 **RISK REGIME LIQUIDATED (GAME OVER)**: Your metrics crossed catastrophic boundaries.")
    if st.button("🔄 LOAD SYSTEM RE-DEPOSIT REBOOT FILE"):
        st.session_state.clear()
        st.rerun()
else:
    # ACTION MOVES SELECTION TILES
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
for log in gs["logs"][:3]:
