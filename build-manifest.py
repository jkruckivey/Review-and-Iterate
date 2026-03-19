#!/usr/bin/env python3
"""
build-manifest.py
Scans the Course Widgets/ directory and generates manifest.json
for use by course-widget-compare.html.

Run this script whenever you add or remove widget files, then commit
manifest.json alongside the HTML files.

Usage:
    python build-manifest.py
"""

import os
import json
import re
from datetime import datetime, timezone

WIDGET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Course Widgets")
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "manifest.json")


def detect_font(content):
    if re.search(r"'Geist'|\"Geist\"|family:\s*Geist", content):
        return "Geist"
    if re.search(r"'Inter'|\"Inter\"", content):
        return "Inter"
    return "System UI"


def detect_color(content):
    # Legacy Ivey Brand: uses Ivey red (#8B2433) or deep Ivey blue (#003865)
    if re.search(r"#8[Bb]2433|#003865|#8b2433", content):
        return "Legacy Ivey Brand"
    # Pastel Tints: uses pastel CSS vars or known pastel hex values
    if re.search(r"--color-pastel|#6b9085|#e8f4f1|#f0ede0|#c8ddd9|#d4e6e1|pastel", content, re.I):
        return "Pastel Tints"
    return "Neutral / Minimal"


def detect_depth(content):
    # Look for box-shadow declarations
    shadows = re.findall(r'box-shadow\s*:[^;}{]+', content)
    if not shadows:
        return "Flat (No shadows)"
    # Heavy: large blur/spread values (>= 10px in the blur position) or gradients
    has_heavy = any(
        re.search(r'\b[12]\dpx\b|\b[3-9]\dpx\b', s) for s in shadows
    )
    has_gradient = bool(re.search(r'linear-gradient|radial-gradient', content))
    if has_heavy or has_gradient:
        return "Heavy Shadows & Gradients"
    return "Light Drop Shadows"


def detect_mobile(content):
    if re.search(r'@media\s*\(max-width', content):
        return "Mobile Ready (@media)"
    return "Desktop Only (Fixed)"


def detect_a11y(content):
    aria_count = len(re.findall(r'\baria-\w+', content))
    has_role = bool(re.search(r'\brole=', content))
    if aria_count >= 3 or has_role:
        return "A11y Partial (Keyboard only)"
    return "A11y Warning"


def detect_tech(content):
    if re.search(r'd3\.js|d3\.min\.js|["\']d3["\']|d3\.select|d3\.scale|d3\.arc', content):
        return "D3.js Visualization"
    return "Vanilla HTML/JS"


def detect_traits(content, filename):
    return {
        "font":   detect_font(content),
        "color":  detect_color(content),
        "depth":  detect_depth(content),
        "mobile": detect_mobile(content),
        "a11y":   detect_a11y(content),
        "tech":   detect_tech(content),
    }


def build_manifest():
    if not os.path.isdir(WIDGET_DIR):
        print(f"Error: Widget directory not found: {WIDGET_DIR}")
        return

    courses = {}
    total = 0

    for course_name in sorted(os.listdir(WIDGET_DIR)):
        course_path = os.path.join(WIDGET_DIR, course_name)
        if not os.path.isdir(course_path):
            continue

        widgets = []
        for filename in sorted(os.listdir(course_path)):
            if not filename.lower().endswith(".html"):
                continue

            filepath = os.path.join(course_path, filename)
            rel_path = f"Course Widgets/{course_name}/{filename}"

            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                traits = detect_traits(content, filename)
            except Exception as e:
                print(f"  Warning: could not read {filename}: {e}")
                traits = {k: "Unknown" for k in ("font", "color", "depth", "mobile", "a11y", "tech")}

            widgets.append({
                "path":     rel_path,
                "filename": filename,
                "traits":   traits,
                "course":   course_name,
            })

        if widgets:
            courses[course_name] = widgets
            total += len(widgets)
            print(f"  {course_name}: {len(widgets)} widgets")

    manifest = {
        "generated":  datetime.now(timezone.utc).isoformat(),
        "totalCount": total,
        "courses":    courses,
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\nDone. {OUTPUT_FILE}")
    print(f"Total: {total} widgets across {len(courses)} courses")


if __name__ == "__main__":
    build_manifest()
