class InstapMethod:
    def __init__(self, method: str, params: dict):
        self.method = method
        self.params = params

    def json(self) -> dict:
        return {
            "method": self.method,
            "params": self.params
        }
