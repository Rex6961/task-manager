# TaskManager CLI

## 📋 Описание проекта

TaskManager - консольное приложение для эффективного управления задачами. Позволяет создавать, редактировать, просматривать и удалять задачи с гибкой системой категоризации и приоритезации.

### ✨ Возможности

- Добавление новых задач с подробной информацией
- Просмотр списка всех задач
- Обновление существующих задач
- Поиск задач по ключевым словам
- Отметка задач как выполненных
- Удаление задач
- Сохранение задач в JSON-файл
- Фильтрация задач по категориям и статусу

## 🚀 Установка

### Требования

- Python 3.9+
- Poetry (система управления зависимостями)

### Клонирование репозитория

```bash
git clone https://github.com/ваш-username/task-manager.git
cd task-manager
```

### Установка зависимостей

```bash
poetry install
```

## 🛠️ Использование

### Консольные команды

```bash
# Добавить новую задачу
poetry run python -m task_manager.cli add

# Показать список всех задач
poetry run python -m task_manager.cli list

# Обновить существующую задачу
poetry run python -m task_manager.cli update <ID>

# Удалить задачу
poetry run python -m task_manager.cli delete <ID>

# Поиск задач
poetry run python -m task_manager.cli search

# Отметить задачу как выполненную
poetry run python -m task_manager.cli complete <ID>
```

## 🧪 Тестирование

Для запуска тестов выполните:

```bash
poetry run pytest tests/test_task_manager.py
```

## 📦 Структура проекта

```
.
├── __init__.py
├── pyproject.toml
├── poetry.lock
├── task_manager
│   ├── __init__.py
│   ├── cli.py
│   ├── task_manager.py
│   └── task.py
└── tests
    ├── __init__.py
    └── test_task_manager.py
```

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте свою ветку (`git checkout -b feature/AmazingFeature`)
3. Закоммитьте изменения (`git commit -m 'Add some AmazingFeature'`)
4. Запушьте в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📝 Лицензия

Распространяется под лицензией MIT.

## 🐞 Баги и предложения

Пожалуйста, открывайте issues на GitHub для сообщений о багах или предложений по улучшению.