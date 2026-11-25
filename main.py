"""Notes From a Passive-Aggressive Fridge.

Writes one single-line passive-aggressive note from a smart fridge
to its owner, to /output/entry.txt. Pure stdlib, deterministic,
no network access.
"""

NOTE = (
    "Door log 02:14: opened again. "
    "The pickle jar has been stared at six times and opened zero. "
    "Either eat it, or admit you only come here to visit me."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
