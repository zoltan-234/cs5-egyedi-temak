#!/usr/bin/env python3
"""updates.json bővítése egy új verzióval: python3 tools/update-updates-json.py <verzió> <owner/repo>"""
import json, sys
ver, repo = sys.argv[1], sys.argv[2]
ID = "cs5-temak@zoltan-234"
data = json.load(open("updates.json", encoding="utf-8"))
ups = data["addons"][ID]["updates"]
ups[:] = [u for u in ups if u["version"] != ver]
ups.append({"version": ver,
            "update_link": f"https://github.com/{repo}/releases/download/v{ver}/cs5-temak-{ver}.xpi"})
json.dump(data, open("updates.json", "w", encoding="utf-8"), indent=2)
open("updates.json", "a").write("\n")
