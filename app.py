from flask import Flask

app = Flask(__name__)

app.register_blueprint(task_dp)

@app.route('/')
def main():
    print(4+2)
    return  '<h1> Главная страница <h1>'


if __name__ == '__main__':
    qpp.run(debug=True)

