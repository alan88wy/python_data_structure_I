from pathlib import Path

def folder_size(p):
    return sum(f.stat().st_size for f in p.rglob("*") if f.is_file())

base = Path("c:/aToRead")
sizes = [(p, folder_size(p)) for p in base.iterdir() if p.is_dir()]
for p, s in sorted(sizes, key=lambda x: x[1], reverse=True)[:10]:
    print(f"{p}: {s/1e9:.2f} GB")
