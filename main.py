import os
# One-word entry: the single word below is the entire submission.
# Output goes to /output/entry.txt.
LINE = "Micromanager"
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
