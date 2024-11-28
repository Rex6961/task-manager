from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: str = "Низкий"
    status: str = "Не выполнена"

    def mark_completed(self):
        """Отметить задачу как выполненную"""
        self.status = "Выполнена"

    def update(self, **kwargs):
        """Обновить поля задачи"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)