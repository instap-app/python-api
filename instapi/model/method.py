from dataclasses import dataclass


@dataclass
class InstapMethod:
    method: str
    params: dict

    def json(self) -> dict:
        return {
            "method": self.method,
            "params": self.params
        }
