import toml
from typing import Any


class TOMLDataBase:

    def __init__(self, file_path: str) -> None:
        self.file_path : str = file_path
        self.data : dict[str, Any] = toml.load(file_path)
        print(self.data)

    def save(self) -> None:
        with open(self.file_path, 'w') as file:
            toml.dump(self.data, file)

    def copy(self, new_path: str) -> None:
        with open(new_path, 'w') as file:
            toml.dump(self.data, file)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.data[key] = value

