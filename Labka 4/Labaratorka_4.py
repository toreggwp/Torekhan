from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


# === Задача 1: Класс Player ===
class Player:
    def __init__(self, id_val: int, name: str, hp: int):
        # Инкапсуляция: приватные атрибуты
        self._id = id_val
        # String методы: strip() убирает пробелы, title() делает "John"
        self._name = name.strip().title()
        # Проверка HP: если меньше 0, то ставим 0
        self._hp = hp if hp >= 0 else 0

    def __str__(self):
        """Магический метод для вывода объекта через print()"""
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        """Деструктор: выводит сообщение при удалении объекта"""
        print(f"Player {self._name} удалён")

    def to_dict(self):
        """Метод для преобразования объекта в словарь (для JSON ответа)"""
        return {"id": self._id, "name": self._name, "hp": self._hp}


# === Схема Pydantic для валидации входных данных ===
class PlayerCreate(BaseModel):
    id: int
    name: str
    hp: int


# === Эндпоинт FastAPI ===
@app.post("/player")
async def create_player(data: PlayerCreate):
    # Создаем экземпляр твоего класса
    p = Player(data.id, data.name, data.hp)

    # Печатаем объект в консоль сервера (сработает __str__)
    print(f"Лог сервера: {p}")

    # Возвращаем данные клиенту
    return p.to_dict()


# === Запуск сервера ===
if __name__ == "__main__":
    # Запускаем сервер через uvicorn внутри кода
    uvicorn.run(app, host="127.0.0.1", port=8000)

