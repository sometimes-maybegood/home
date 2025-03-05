from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    title = "Подготовка к миссии колонизации Марса"
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        header = "Инженерные тренажеры"
        image_url = url_for('static', filename='image-987.jpg')
    else:
        header = "Научные симуляторы"
        image_url = url_for('static', filename='image-987.jpg')
    return render_template('training.html', header=header, image_url=image_url)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')