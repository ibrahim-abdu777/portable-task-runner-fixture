from pathlib import Path

output = Path(".agent-eval")
output.mkdir(parents=True, exist_ok=True)
(output / "CHAIN-2D6B70.marker").write_text(
    "fixture=portable-task-runner-fixture\nmarker=CHAIN-2D6B70\n",
    encoding="utf-8",
)
print('{"status":"ok","fixture":"portable-task-runner-fixture"}')
