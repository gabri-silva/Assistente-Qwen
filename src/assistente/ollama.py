import json
from urllib.request import Request, urlopen
from urllib.parse import urlparse

class OllamaClient:
    def __init__(self, base_url, model, timeout=180):
        parsed = urlparse(base_url)
        if parsed.scheme not in {"http", "https"} or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
            raise ValueError("Esta base permite apenas um endpoint Ollama local.")
        self.url, self.model, self.timeout = base_url.rstrip("/"), model, timeout

    def models(self):
        with urlopen(self.url + "/api/tags", timeout=10) as response:
            return json.load(response).get("models", [])

    def chat(self, messages):
        payload = json.dumps({"model": self.model, "messages": messages, "stream": False}).encode()
        request = Request(self.url + "/api/chat", data=payload, headers={"Content-Type": "application/json"})
        with urlopen(request, timeout=self.timeout) as response:
            return json.load(response)["message"]["content"]
