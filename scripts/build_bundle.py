#!/usr/bin/env python3
"""
Build and optionally minify the Scriber‑Labs theme CSS bundle.
"""

import pathlib
import shutil
import subprocess
import sys  # <-- needed for sys.stderr

# ----------------------------------------------------------------------
# Paths
# ----------------------------------------------------------------------
ROOT = pathlib.Path(__file__).resolve().parents[1]   # repo root
SRC_CSS = ROOT / "theme" / "css"
BUILD_DIR = ROOT / "build"

# ----------------------------------------------------------------------
# 1️⃣ Clean old build
# ----------------------------------------------------------------------
shutil.rmtree(BUILD_DIR, ignore_errors=True)
BUILD_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------------
# 2️⃣ Order of files (adjust if your filenames differ)
# ----------------------------------------------------------------------
ORDER = [
    "base/reset.css",
    "base/variables.css",
    "base/theme.css",
    "base/layout.css",

    "components/buttons.css",
    "components/cards.css",
    "components/search.css",
    "components/icons/icons.css",
    "components/icons/icon-style.css",
    "components/feature-box.css",  
    "components/typography.css",

    "base/responsive.css",
    
    "overrides/streamlit.css",
]

# ----------------------------------------------------------------------
# 3️⃣ Concatenate – with defensive checks
# ----------------------------------------------------------------------
bundle_path = BUILD_DIR / "bundle.css"

with bundle_path.open("w", encoding="utf-8") as out:
    for name in ORDER:
        src = SRC_CSS / name
        if not src.is_file():
            print(f"⚠️  Missing {src}", file=sys.stderr)
            continue                     # skip missing files, keep going
        out.write(f"\n/* ----- {name} ----- */\n")
        out.write(src.read_text(encoding="utf-8"))
        out.write("\n")                  # guarantee a trailing newline

print(f"✅ Created {bundle_path}")

# ----------------------------------------------------------------------
# 4️⃣ Optional minification (requires `csso` npm package)
# ----------------------------------------------------------------------
MINIFIED = BUILD_DIR / "bundle.min.css"
try:
    # `npx` will look for a local csso-cli first, then fall back to a global one.
    subprocess.run(
        ["npx", "csso", str(bundle_path), "--output", str(MINIFIED)],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    print(f"✅ Minified bundle → {MINIFIED}")
except subprocess.CalledProcessError as exc:
    # csso ran but returned a non‑zero exit code (syntax error in CSS)
    print(
        f"⚠️  Minification failed (csso exit code {exc.returncode}). "
        f"stderr:\n{exc.stderr}",
        file=sys.stderr,
    )
except FileNotFoundError:
    # npx or csso not found at all
    print("⚠️  npx or csso-cli not installed – run `npm install csso-cli --save-dev`", file=sys.stderr)