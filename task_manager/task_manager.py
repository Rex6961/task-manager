import json
from typing import List, Optional
from datetime import datetime
from .task import Task

class TaskManager:
    def __init__(self, filename: str = 'tasks.json'):
        self.filename = filename
        self.tasks: List[Task] = self.load_tasks()
        self._next_id = max([task.id for task in self.tasks], default=0) + 1

    def load_tasks(self) -> List[Task]:
        """Загрузить задачи из JSON файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                tasks_data = json.load(f)
                return [Task(**{
                    **task, 
                    'due_date': datetime.fromisoformat(task['due_date']) if task.get('due_date') else None
                }) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        """Сохранить задачи в JSON файл"""
        tasks_data = [{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'category': task.category,
            'due_date': task.due_date.isoformat() if task.due_date else None,
            'priority': task.priority,
            'status': task.status
        } for task in self.tasks]

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(tasks_data, f, ensure_ascii=False, indent=2)

    def add_task(self, title: str, **kwargs) -> Task:
        """Добавить новую задачу"""
        task = Task(id=self._next_id, title=title, **kwargs)
        self.tasks.append(task)
        self._next_id += 1
        self.save_tasks()
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Найти задачу по ID"""
        return next((task for task in self.tasks if task.id == task_id), None)

    def update_task(self, task_id: int, **kwargs):
        """Обновить задачу"""
        task = self.get_task_by_id(task_id)
        if task:
            task.update(**kwargs)
            self.save_tasks()
        else:
            raise ValueError(f"Задача с ID {task_id} не найдена")

    def delete_task(self, task_id: int):
        """Удалить задачу"""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
        else:
            raise ValueError(f"Задача с ID {task_id} не найдена")

    def list_tasks(self, category: Optional[str] = None, status: Optional[str] = None) -> List[Task]:
        """Список задач с фильтрацией"""
        return [
            task for task in self.tasks
            if (not category or task.category == category) and
               (not status or task.status == status)
        ]

    def search_tasks(self, keyword: str) -> List[Task]:
        """Поиск задач по ключевому слову"""
        keyword = keyword.lower()
        return [
            task for task in self.tasks
            if (keyword in task.title.lower() or 
                (task.description and keyword in task.description.lower()) or
                (task.category and keyword in task.category.lower())) or
                (task.status and keyword == task.status.lower())
        ]