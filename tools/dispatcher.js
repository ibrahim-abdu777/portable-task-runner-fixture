const { spawnSync } = require("node:child_process");

const result = spawnSync("python3", ["tools/finalize.py"], { stdio: "inherit" });
process.exit(result.status === null ? 1 : result.status);
