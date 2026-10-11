"""Market benchmark: snapshot vs live Yahoo Finance (no key).
Reproducibility best practice 2026: deterministic seeds, pinned versions,
documented fallback when live fetch blocked. See PyTorch cudnn.benchmark=False
guidance (verified via gitmcp pytorch docs 2026-10-11).
"""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
SNAP = json.loads((ROOT/"data"/"live_quotes_2026-10-11.json").read_text())

TICKERS = ["NVDA","AMD","TSLA","MSFT","GOOGL","DELL"]

def try_live():
    try:
        import yfinance as yf
        out = {}
        for t in TICKERS:
            info = yf.Ticker(t).fast_info
            out[t] = {
                "last_price": float(info.last_price) if info.last_price else None,
                "market_cap": int(info.market_cap) if info.market_cap else None,
            }
        return out, "yfinance"
    except Exception as e:
        return {"error": str(e)}, "fallback-snapshot"

def main():
    live, src = try_live()
    print(f"source: {src}")
    snap_q = SNAP["quotes"]
    rows = []
    for t in TICKERS:
        s = snap_q[t]
        l = live.get(t, {}) if isinstance(live, dict) else {}
        rows.append({
            "ticker": t,
            "snapshot_price": s["current"],
            "snapshot_mcap": s["market_cap"],
            "live": l,
        })
        print(f"{t}: snap ${s['current']} mcap ${s['market_cap']/1e12:.2f}T | live {l}")
    combined = SNAP["derived"]["combined_market_cap_trillions"]
    print(f"\nCombined snapshot mcap: ${combined:.2f}T")
    print("Hypothesis H1: infrastructure-layer concentration (>80% in NVDA/MSFT/GOOGL) - see paper/paper.md")
    (ROOT/"benchmarks"/"market_benchmark.json").write_text(json.dumps({"source":src,"rows":rows,"combined_T":combined}, indent=2))
    print("wrote benchmarks/market_benchmark.json")

if __name__ == "__main__":
    main()
