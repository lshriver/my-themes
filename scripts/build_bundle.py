# scripts/build_bundle.py
import pathlib, shutil, subprocess

ROOT = pathlib.Path(__file__).parents[1]    # repo root
SRC_CSS = ROOT / "theme" / "css"
BUILD_DIR = ROOT / "build"

# ----------------------------------------------------------------------
# 1️⃣  Clean old build
# ----------------------------------------------------------------------
shutil.rmtree(BUILD_DIR, ignore_errors=True)
BUILD_DIR.mkdir(parents=True)

# ----------------------------------------------------------------------
# 2️⃣  Define the order you want the files concatenated in
# ----------------------------------------------------------------------
order = [
    "base.css",
    "typography.css",
    "layout.css",
    "components.css",
    "responsive.css",
    "overrides.css",
]

# ----------------------------------------------------------------------
# 3️⃣  Concatenate
# ----------------------------------------------------------------------
bundle_path = BUILD_DIR / "bundle.css"
with bundle_path.open("w", encoding="utf-8") as out:
    for name in order:
        src = SRC_CSS / name
        if not src.is_file():
            print(f"⚠️ Missing {src}", file=sys.stderr)
            continue
        out.write(f"\n/*----- {name} -----*/\n")
        out.write(src.read_text(encoding="utf-8"))
        out.write("\n")

print(f"✅ Created {bundle_path}")

# ----------------------------------------------------------------------
# 4️⃣  Optional minification (requires `csso` npm package)
# ----------------------------------------------------------------------
try:
    subprocess.run(
        ["npx", "csso", str(bundle_path), "--output", str(BUILD_DIR / "bundle.min.css")],
        check=True,
    )
    print(f"✅ Minified bundle to {BUILD_DIR / 'bundle.min.css'}")
except Exception as exc:            # npx not installed or csso missing
    print(f"⚠️ Skipping minification: {exc}")