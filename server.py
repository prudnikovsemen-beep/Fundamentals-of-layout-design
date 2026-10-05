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
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        file_path = os.path.join('home', 'contacts.html')
        abs_path = os.path.abspath(file_path)

        # Отладка: сразу видно, где сервер ищет файл
        print(f"[GET] Ищем файл: {abs_path}")
        print(f"[GET] Файл существует: {os.path.exists(abs_path)}")

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            # Только ASCII в байтовом литерале
            self.wfile.write(b'<h1>Contacts page not found</h1>')
        except Exception as e:
            self.wfile.write(f'<h1>Error: {str(e)}</h1>'.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')

        print("Получены данные POST-запроса:")
        print(post_data)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Кодируем строку в UTF-8 вместо байтового литерала с кириллицей
        response_text = "Данные успешно получены и выведены в консоль"
        self.wfile.write(response_text.encode('utf-8'))


if __name__ == '__main__':
    print(f"Сервер запущен на порту {PORT}")
    print("Откройте в браузере: http://localhost:8000")
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        httpd.serve_forever()
