from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_recruto():
    # Получаем параметры из GET-запроса
    name = request.args.get('name', 'Recruto')  # По умолчанию "Recruto"
    message = request.args.get('message', 'Давай дружить!')  # По умолчанию "Давай дружить!"

    # Формируем ответ
    return f"Hello {name}! {message}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
