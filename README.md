ITIS Django project
Runing instructions:
1. `python3 -m venv .venv` or `python -m venv .venv` - инициализация виртуального окружения
2. macOS: `source .venv/bin/activate` or Windows cmd (чтобы запустить cmd из PowerShell выполните `cmd.exe`): `.venv\Scripts\activate.bat` - вход в виртуальное окружение
3. `pip install -r requirements.txt` - установка зависимостей
4. `python manage.py migrate` - запуск миграций
5. `python manage.py runserver` - запуск приложения
you can visit links:
`http://127.0.0.1:8000/bboard/`
`http://127.0.0.1:8000/bboard/add/`
`http://127.0.0.1:8000/blog/flow/`
`http://127.0.0.1:8000/blog/post/`
`http://127.0.0.1:8000/info/`
...
