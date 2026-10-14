from pathlib import Path

class WorkspaceFiles:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.root.mkdir(parents=True, exist_ok=True)

    def resolve(self, relative):
        given = Path(relative)
        if given.is_absolute():
            raise ValueError("Use um caminho relativo à pasta workspace.")
        candidate = (self.root / given).resolve()
        if not candidate.is_relative_to(self.root) or candidate == self.root:
            raise ValueError("Caminho fora da pasta de trabalho.")
        return candidate

    def read(self, relative):
        return self.resolve(relative).read_text(encoding="utf-8")

    def write(self, relative, content):
        destination = self.resolve(relative)
        if destination.exists():
            backup = destination.with_name(destination.name + ".bak")
            if backup.exists():
                raise ValueError("Já existe um backup .bak. Preserve-o antes de sobrescrever novamente.")
            backup.write_bytes(destination.read_bytes())
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
