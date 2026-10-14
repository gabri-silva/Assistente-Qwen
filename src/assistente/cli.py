import argparse
import json
from pathlib import Path
from urllib.error import URLError
from .ollama import OllamaClient
from .memory import Memory
from .tools.files import WorkspaceFiles

ROOT = Path(__file__).resolve().parents[2]

def main():
    parser = argparse.ArgumentParser(description="Assistente pessoal local com Qwen")
    parser.add_argument("--config", type=Path, default=ROOT / "config.example.json")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("doctor", help="Verificar conexão e modelo local")
    sub.add_parser("chat", help="Conversar com o modelo")
    remember = sub.add_parser("remember", help="Guardar uma memória explícita")
    remember.add_argument("text")
    sub.add_parser("memories", help="Listar memórias")
    read = sub.add_parser("read", help="Ler arquivo dentro de workspace")
    read.add_argument("path")
    write = sub.add_parser("write", help="Escrever arquivo dentro de workspace")
    write.add_argument("path")
    write.add_argument("text")
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    client = OllamaClient(config["ollama_url"], config["model"], config["timeout_seconds"])
    try:
        if args.command == "doctor":
            names = [m["name"] for m in client.models()]
            print("Ollama acessível. Modelos:", ", ".join(names) or "nenhum")
            if config["model"] not in names:
                print("Modelo configurado ausente. Execute: ollama pull " + config["model"])
                return 1
            print("Modelo configurado disponível.")
            return 0
        memory = Memory(ROOT / config["database"])
        files = WorkspaceFiles(ROOT / config["workspace"])
        if args.command == "remember":
            memory.add(args.text)
            print("Memória registrada.")
        elif args.command == "memories":
            for ident, text in memory.list():
                print(f"{ident}: {text}")
        elif args.command == "read":
            print(files.read(args.path))
        elif args.command == "write":
            files.write(args.path, args.text)
            print("Arquivo salvo na pasta workspace.")
        elif args.command == "chat":
            messages = [{"role": "system", "content": config["system_prompt"]}]
            facts = memory.list()
            if facts:
                messages.append({"role": "system", "content": "Memórias declaradas pelo usuário:\n" + "\n".join(t for _, t in facts)})
            print("Digite /sair para encerrar. A conversa fica apenas nesta sessão.")
            while True:
                user = input("Você: ").strip()
                if user == "/sair":
                    break
                if not user:
                    continue
                messages.append({"role": "user", "content": user})
                answer = client.chat(messages)
                messages.append({"role": "assistant", "content": answer})
                print("Assistente:", answer)
        return 0
    except (URLError, OSError, ValueError, KeyError) as error:
        print("Não foi possível concluir:", error)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
