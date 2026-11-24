"""Write the one-line-of-earned-pride entry to /output/entry.txt.

One line, 1 to 240 characters: a quiet, earned moment of pride
for someone in a scene.
"""

from pathlib import Path

ENTRY = "After three years of night shifts, she watched her daughter cross the graduation stage — and knew every tired morning was worth it."
# One line, 131 characters (limit 240).

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
