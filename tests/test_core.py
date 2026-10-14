import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock
from assistente.tools.files import WorkspaceFiles
from assistente.memory import Memory
from assistente.ollama import OllamaClient

class CoreTests(unittest.TestCase):
    def test_rejects_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            files = WorkspaceFiles(directory)
            for path in ("../outside.txt", str(Path(directory).resolve() / "absolute.txt")):
                with self.assertRaises(ValueError):
                    files.read(path)

    def test_write_keeps_previous_version(self):
        with tempfile.TemporaryDirectory() as directory:
            files = WorkspaceFiles(directory)
            files.write("notes.txt", "primeira")
            files.write("notes.txt", "segunda")
            self.assertEqual(files.read("notes.txt"), "segunda")
            self.assertEqual(files.read("notes.txt.bak"), "primeira")
            with self.assertRaises(ValueError):
                files.write("notes.txt", "terceira")

    def test_memory_survives_reopen(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "memory.sqlite3"
            Memory(path).add("Uso português")
            self.assertEqual(Memory(path).list(), [(1, "Uso português")])

    def test_chat_payload(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b'{"message":{"content":"Oi"}}'
        with patch("assistente.ollama.urlopen", return_value=response) as request:
            self.assertEqual(OllamaClient("http://127.0.0.1:11434", "qwen3.5:9b").chat([{ "role": "user", "content": "Oi"}]), "Oi")
            payload = json.loads(request.call_args.args[0].data)
            self.assertFalse(payload["stream"])
            self.assertEqual(payload["model"], "qwen3.5:9b")

if __name__ == "__main__":
    unittest.main()
