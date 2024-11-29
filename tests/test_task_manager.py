import pytest
from ..task_manager.task_manager import TaskManager
import os

@pytest.fixture
def task_manager():
    """Fixture для создания TaskManager с временным файлом"""
    test_filename = 'test_tasks.json'
    task_manager = TaskManager(filename=test_filename)
    yield task_manager
    # Удаление тестового файла после завершения теста
    if os.path.exists(test_filename):
        os.remove(test_filename)

def test_add_task(task_manager):
    """Тест добавления задачи"""
    task = task_manager.add_task("Тестовая задача", description="Описание")
    assert task.title == "Тестовая задача"
    assert len(task_manager.tasks) == 1

def test_update_task(task_manager):
    """Тест обновления задачи"""
    task = task_manager.add_task("Первая задача")
    task_manager.update_task(task.id, title="Обновленная задача")
    updated_task = task_manager.get_task_by_id(task.id)
    assert updated_task.title == "Обновленная задача"

def test_delete_task(task_manager):
    """Тест удаления задачи"""
    task = task_manager.add_task("Задача для удаления")
    task_manager.delete_task(task.id)
    assert len(task_manager.tasks) == 0

def test_search_tasks(task_manager):
    """Тест поиска задач"""
    task_manager.add_task("Изучить Python", category="Обучение")
    task_manager.add_task("Прочитать книгу по Python", category="Личное")
    
    results = task_manager.search_tasks("Python")
    assert len(results) == 2

def test_list_tasks_by_category(task_manager):
    """Тест списка задач по категории"""
    task_manager.add_task("Задача 1", category="Работа")
    task_manager.add_task("Задача 2", category="Работа")
    task_manager.add_task("Задача 3", category="Личное")
    
    work_tasks = task_manager.list_tasks(category="Работа")
    assert len(work_tasks) == 2