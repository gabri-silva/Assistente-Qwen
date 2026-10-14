"""Contrato de integração. Nenhum navegador pessoal é conectado nesta versão."""

class BrowserAdapter:
    def open(self, url):
        raise NotImplementedError("Configurar Browser Use/Playwright e o perfil autorizado antes de habilitar.")
