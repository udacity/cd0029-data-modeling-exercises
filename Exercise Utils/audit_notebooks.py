"""
Audit script to compare solution and starter notebooks.

Expected differences (allowed):
  - Solutions have cell outputs and execution_count values
  - Solutions have code between BEGIN/END SOLUTION markers;
    starters replace those blocks with YOUR CODE HERE placeholders
  - Notebook-level metadata (kernelspec, language_info) may differ

Any other difference is flagged as an unexpected discrepancy.
"""

import json
import re
import os
from pathlib import Path
from datetime import datetime


# ---------- helpers ----------

def load_notebook(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def join_source(source):
    """Normalise a cell's source field to a single string."""
    if isinstance(source, list):
        return "".join(source)
    return source


def strip_solution_blocks(text):
    """
    Replace solution blocks with the placeholder the generator would produce.
    Handles both multi-line and inline cases:
      Multi-line: ### BEGIN SOLUTION\\n...\\n### END SOLUTION
      Inline:     '### BEGIN SOLUTION ... ### END SOLUTION'
    """
    # --- markers → -- YOUR CODE HERE
    # Inline case first (single-quote delimited on one line)
    text = re.sub(
        r"'--- BEGIN SOLUTION.*?--- END SOLUTION[^']*'",
        "'-- YOUR CODE HERE'",
        text,
    )
    # Multi-line case
    text = re.sub(
        r"--- BEGIN SOLUTION.*?--- END SOLUTION[^\n]*",
        "-- YOUR CODE HERE",
        text,
        flags=re.DOTALL,
    )
    # ### markers → ### YOUR CODE HERE
    # Inline case first (single-quote delimited on one line)
    text = re.sub(
        r"'### BEGIN SOLUTION.*?### END SOLUTION[^']*'",
        "'### YOUR CODE HERE'",
        text,
    )
    # Multi-line case
    text = re.sub(
        r"### BEGIN SOLUTION.*?### END SOLUTION[^\n]*",
        "### YOUR CODE HERE",
        text,
        flags=re.DOTALL,
    )
    return text


def normalise_whitespace(text):
    """Collapse runs of whitespace for a softer comparison."""
    return re.sub(r"\s+", " ", text).strip()


# ---------- pair discovery ----------

def find_pairs(root_dir):
    """
    Walk the tree and return a list of (solution_path, starter_path) tuples.
    """
    root = Path(root_dir)
    pairs = []
    for sol_dir in sorted(root.rglob("solution")):
        if not sol_dir.is_dir():
            continue
        starter_dir = sol_dir.parent / "starter"
        if not starter_dir.is_dir():
            continue
        for sol_nb in sorted(sol_dir.glob("*.ipynb")):
            starter_name = sol_nb.name.replace("Solutions", "Starter").replace("Solution", "Starter")
            starter_nb = starter_dir / starter_name
            if starter_nb.exists():
                pairs.append((sol_nb, starter_nb))
            else:
                pairs.append((sol_nb, None))
    return pairs


# ---------- cell-level diff ----------

def diff_cells(sol_cell, start_cell, cell_idx, issues):
    """Compare one solution cell against its starter counterpart."""
    prefix = f"  Cell {cell_idx + 1}"

    # Type check
    if sol_cell["cell_type"] != start_cell["cell_type"]:
        issues.append(f"{prefix}: cell_type mismatch — solution={sol_cell['cell_type']}, starter={start_cell['cell_type']}")
        return

    sol_src = join_source(sol_cell.get("source", ""))
    start_src = join_source(start_cell.get("source", ""))

    if sol_cell["cell_type"] == "markdown":
        # Markdown cells should be identical
        if normalise_whitespace(sol_src) != normalise_whitespace(start_src):
            issues.append(f"{prefix} (markdown): content differs")
            issues.append(f"    SOL : {sol_src[:200]!r}")
            issues.append(f"    START: {start_src[:200]!r}")
        return

    # Code cells: strip solution blocks from solution, then compare
    sol_stripped = strip_solution_blocks(sol_src)

    if normalise_whitespace(sol_stripped) != normalise_whitespace(start_src):
        # Check if starter simply has YOUR CODE HERE where solution had a block
        # If even after stripping they don't match, flag it
        issues.append(f"{prefix} (code): source differs after stripping solution blocks")
        # Show a short snippet of each
        sol_lines = sol_stripped.strip().splitlines()
        start_lines = start_src.strip().splitlines()
        # Find first differing line
        for i, (sl, stl) in enumerate(zip(sol_lines, start_lines)):
            if normalise_whitespace(sl) != normalise_whitespace(stl):
                issues.append(f"    First diff at source line {i + 1}:")
                issues.append(f"      SOL (stripped): {sl.rstrip()!r}")
                issues.append(f"      STARTER       : {stl.rstrip()!r}")
                break
        else:
            if len(sol_lines) != len(start_lines):
                issues.append(f"    Line count differs: solution(stripped)={len(sol_lines)}, starter={len(start_lines)}")


# ---------- notebook-level diff ----------

def audit_pair(sol_path, start_path):
    """
    Compare one solution/starter pair.
    Returns a list of issue strings (empty = clean).
    """
    issues = []

    if start_path is None:
        issues.append("  No matching starter notebook found!")
        return issues

    sol_nb = load_notebook(sol_path)
    start_nb = load_notebook(start_path)

    sol_cells = sol_nb.get("cells", [])
    start_cells = start_nb.get("cells", [])

    if len(sol_cells) != len(start_cells):
        issues.append(f"  Cell count mismatch: solution={len(sol_cells)}, starter={len(start_cells)}")
        # Still compare up to the shorter length
        if len(sol_cells) > len(start_cells):
            for i in range(len(start_cells), len(sol_cells)):
                src = join_source(sol_cells[i].get("source", "")).strip()
                kind = sol_cells[i]["cell_type"]
                desc = f"(empty)" if not src else f"({src[:80]!r})"
                issues.append(f"  Extra solution cell {i + 1} [{kind}]: {desc}")
        else:
            for i in range(len(sol_cells), len(start_cells)):
                src = join_source(start_cells[i].get("source", "")).strip()
                kind = start_cells[i]["cell_type"]
                desc = f"(empty)" if not src else f"({src[:80]!r})"
                issues.append(f"  Extra starter cell {i + 1} [{kind}]: {desc}")

    min_len = min(len(sol_cells), len(start_cells))
    for i in range(min_len):
        diff_cells(sol_cells[i], start_cells[i], i, issues)

    return issues


# ---------- main ----------

def main():
    root = Path(__file__).parent.parent  # repo root (one level up from Exercise Utils)
    pairs = find_pairs(root)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_lines = []
    log_lines.append(f"Notebook Audit Report — {timestamp}")
    log_lines.append("=" * 70)
    log_lines.append("")

    total_issues = 0
    clean_count = 0

    for sol_path, start_path in pairs:
        rel_sol = sol_path.relative_to(root)
        rel_start = start_path.relative_to(root) if start_path else "MISSING"

        log_lines.append(f"Pair: {rel_sol}")
        log_lines.append(f"  vs: {rel_start}")

        issues = audit_pair(sol_path, start_path)

        if issues:
            total_issues += len(issues)
            for issue in issues:
                log_lines.append(issue)
        else:
            log_lines.append("  ✓ Clean — no unexpected differences")
            clean_count += 1

        log_lines.append("")

    # Summary
    log_lines.append("=" * 70)
    log_lines.append(f"SUMMARY: {len(pairs)} pairs checked, {clean_count} clean, "
                     f"{len(pairs) - clean_count} with issues ({total_issues} total issues)")
    log_lines.append("=" * 70)

    report = "\n".join(log_lines)

    # Write log file next to this script (in Exercise Utils/)
    log_path = Path(__file__).parent / "audit_log.txt"
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(report)

    # Also print to console
    print(report)
    print(f"\nLog written to: {log_path}")


if __name__ == "__main__":
    main()
