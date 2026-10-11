"""Hidden-pattern mining (hypotheses, not facts).
Each pattern labelled H1..H5 with falsification test so a PhD can proceed honestly.
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
SNAP = json.loads((ROOT/"data"/"live_quotes_2026-10-11.json").read_text())

def main():
    q = SNAP["quotes"]
    total = sum(v["market_cap"] for v in q.values())
    top3 = q["NVDA"]["market_cap"]+q["MSFT"]["market_cap"]+q["GOOGL"]["market_cap"]
    print(f"H1 infrastructure concentration: top3 share = {top3/total:.1%} (NVDA+MSFT+GOOGL / 6 total)")
    print("H2 copper-to-chiplet-to-exascale arc: Su IBM copper (1990s) -> Zen chiplet (2017) -> Frontier exascale (2022) -> SI training (2026). Test: cite IBM JRD + AMD Zen + ORNL Frontier + medal citation.")
    print("H3 policy-industry co-production: Accord (Sept 2026) -> Summit+medals (Oct 8 2026) -> Genesis 297 projects. Test: event timeline vs SEC 10-K R&D language.")
    print("H4 ASR fragility as object: Wang/Tuang/Hong, Sue/Su, Sata/Satya, Katzios/Kratsios, Aremis/Artemis, Neurolink/Neuralink. Test: WER on ceremony audio vs White House release.")
    print("H5 value-creation vs value-capture split: Science medals (Musk/Brin/Huang/Su) = new primitives; Tech medals (Dell/Nadella) = scale + deployment. Test: patent/citation network analysis.")
    amd_now = q["AMD"]["market_cap"]
    print(f"H6 AMD rehabilitation: <$2B trough (2015, needs CRSP verify) -> ${amd_now/1e9:.0f}B snapshot 2026-10-11. Claim directionally consistent, exact trough needs primary source - flagged.")
    (ROOT/"benchmarks"/"hidden_patterns.json").write_text(json.dumps({
        "top3_share": top3/total,
        "combined_T": total/1e12,
        "hypotheses": ["H1","H2","H3","H4","H5","H6"],
    }, indent=2))
    print("wrote benchmarks/hidden_patterns.json")

if __name__ == "__main__":
    main()
