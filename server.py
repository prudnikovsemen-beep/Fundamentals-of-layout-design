"""
Файл: server.py
Назначение: Простой веб-сервер (движок) на базе http.server.
Логика:
  - do_GET: на любой запрос возвращает contacts.html.
  - do_POST: принимает данные формы, выводит их в консоль.
Стек: Python 3.x, стандартная библиотека.
"""
import http.server
import socketserver
import os

PORT = 8000


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # На любой GET-запрос возвращаем страницу контактов
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Читаем contacts.html из папки home
        file_path = os.path.join('home', 'contacts.html')
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            self.wfile.write(b'<h1>Страница контактов не найдена</h1>')

    def do_POST(self):
        # Дополнительное задание: принимаем POST-запрос и печатаем данные в консоль
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')

        print("Получены данные POST-запроса:")
        print(post_data)

        # Возвращаем простой ответ
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'Данные успешно получены и выведены в консоль')


if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Сервер запущен на порту {PORT}")
        print("Откройте в браузере: http://localhost:8000")
        httpd.serve_forever()
