class AutomationController:
    def __init__(self):
        self.config = None
        self.itens = []

    def load_config(self):
        from automacao_rewards_pc.config.runtime_config import get_runtime_config

        self.config = get_runtime_config()

    def preparar_itens(self):
        from automacao_rewards_pc.domain.items import gerar_lista_itens

        self.itens = gerar_lista_itens()

    def executar(self):
        self.load_config()
        self.preparar_itens()

        # Aqui entra Playwright / PyAutoGUI depois
        for item in self.itens:
            print(f"Executando automação para: {item}")
