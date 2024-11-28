from task_manager.task_manager import TaskManager
from datetime import datetime
import click

@click.group()
def cli():
    """Консольное приложение для управления задачами"""
    pass

@cli.command()
@click.option('--title', prompt='Название задачи', help='Название задачи')
@click.option('--description', prompt='Описание', help='Описание задачи', default=None)
@click.option('--category', prompt='Категория', help='Категория задачи', default=None)
@click.option('--due-date', prompt='Дата выполнения (ГГГГ-ММ-ДД)', help='Дата выполнения', default=None)
@click.option('--priority', type=click.Choice(['Низкий', 'Средний', 'Высокий']), prompt='Приоритет', default='Низкий')
def add(title, description, category, due_date, priority):
    """Добавить новую задачу"""
    task_manager = TaskManager()
    try:
        due_date_parsed = datetime.fromisoformat(due_date) if due_date else None    
        task = task_manager.add_task(
            title=title, 
            description=description, 
            category=category, 
            due_date=due_date_parsed, 
            priority=priority
        )
        click.echo(f"Задача добавлена: {task}")
    except ValueError as e:
        print(f"Incorrect a date: {e}")

@cli.command()
@click.argument('task_id', type=int)
@click.option('--title', prompt='Название задачи', help='Название задачи')
@click.option('--description', prompt='Описание', help='Описание задачи', default=None)
@click.option('--category', prompt='Категория', help='Категория задачи', default=None)
@click.option('--due-date', prompt='Дата выполнения (ГГГГ-ММ-ДД)', help='Дата выполнения', default=None)
@click.option('--priority', type=click.Choice(['Низкий', 'Средний', 'Высокий']), prompt='Приоритет', default='Низкий')
def update(task_id, title, description, category, due_date, priority):
    """Обновить существующую задачу"""
    task_manager = TaskManager()
    try:
        due_date_parsed = datetime.fromisoformat(due_date) if due_date else None
        task_manager.update_task(
            task_id=task_id,
            title=title, 
            description=description, 
            category=category, 
            due_date=due_date_parsed, 
            priority=priority
        )
        click.echo(f"Задача обновлена")
    except ValueError as e:
        print(f"Incorrect a date: {e}")

@cli.command()
def list():
    """Показать список всех задач"""
    task_manager = TaskManager()
    tasks = task_manager.tasks
    if not tasks:
        click.echo("Список задач пуст")
    else:
        for task in tasks:
            click.echo(f"ID: {task.id} | {task.title} | Категория: {task.category} | Статус: {task.status}")

@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Отметить задачу как выполненную"""
    task_manager = TaskManager()
    try:
        task_manager.update_task(task_id, status="Выполнена")
        click.echo(f"Задача {task_id} отмечена как выполненная")
    except ValueError as e:
        click.echo(str(e))

@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Удалить задачу"""
    task_manager = TaskManager()
    try:
        task_manager.delete_task(task_id)
        click.echo(f"Задача {task_id} удалена")
    except ValueError as e:
        click.echo(str(e))

@cli.command()
@click.option('--keyword', prompt='Ключевое слово', help='Ключевое слово для поиска')
def search(keyword):
    """Поиск задач"""
    task_manager = TaskManager()
    tasks = task_manager.search_tasks(keyword)
    if not tasks:
        click.echo("Задачи не найдены")
    else:
        for task in tasks:
            click.echo(f"ID: {task.id} | {task.title} | Категория: {task.category} | Статус: {task.status}")

if __name__ == '__main__':
    cli()