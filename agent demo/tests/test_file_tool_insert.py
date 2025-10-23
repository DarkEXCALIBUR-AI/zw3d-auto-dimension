import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.file_tool import FileTool


def test_insert_preserves_newlines(tmp_path):
    file_tool = FileTool()
    test_file = tmp_path / "test.txt"
    file_tool.run({"operation": "write", "path": str(test_file), "content": "a\nb\n"})

    file_tool._insert(test_file, 1, "x\ny")

    with open(test_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert lines == ["a\n", "x\n", "y\n", "b\n"]
