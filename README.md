# Fundamentals_of_layout_design
## Структура проекта

- `home/` — статические HTML-страницы:
  - `index.html` — главная страница.
  - `catalog.html` — каталог товаров.
  - `category.html` — страница категории.
  - `contacts.html` — страница контактов с формой.
- `server.py` — простой веб-сервер на Python (стандартная библиотека `http.server`). Обрабатывает GET (отдает контакты) и POST (логирует данные).
- `.gitignore` — правила игнорирования служебных файлов.
- `pyproject.toml` — конфигурация Poetry.

## Как запустить

1. Активировать окружение: `poetry shell`
2. Запустить сервер: `python server.py`
3. Открыть в браузере: `http://localhost:8000`
