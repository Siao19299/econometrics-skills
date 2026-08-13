from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "econometrics-replication" / "scripts" / "audit_replication.py"
SPEC = importlib.util.spec_from_file_location("audit_replication", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ReplicationAuditTests(unittest.TestCase):
    def test_flags_high_risk_static_patterns(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "main.py").write_text(
                "import requests\nAPI_KEY = 'not-a-real-key'\nDATA = r'C:\\\\Users\\\\author\\\\data.csv'\nrequests.get('https://example.invalid')\n",
                encoding="utf-8",
            )
            report = MODULE.inspect(root)
            codes = {item["code"] for item in report["findings"]}
            self.assertIn("MISSING_README", codes)
            self.assertIn("POSSIBLE_CREDENTIAL", codes)
            self.assertIn("ABSOLUTE_WINDOWS_PATH", codes)
            self.assertIn("NETWORK_CALL", codes)
            self.assertIn("MISSING_DEPENDENCIES", codes)

    def test_clean_minimal_python_package(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("Run python main.py", encoding="utf-8")
            (root / "requirements.txt").write_text("pandas==2.2.3\n", encoding="utf-8")
            (root / "main.py").write_text("print('deterministic')\n", encoding="utf-8")
            report = MODULE.inspect(root)
            self.assertEqual(report["summary"]["blockers"], 0)
            self.assertEqual(report["summary"]["major"], 0)


if __name__ == "__main__":
    unittest.main()
