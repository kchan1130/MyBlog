from flask import Flask, render_template

from utils.Log import Log


app = Flask(
    __name__,
    template_folder='blog-vue-typescript-master/dist',
    static_folder='blog-vue-typescript-master/dist',
    static_url_path='',
)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    Log.info('start run server')
    app.run(
        debug=True,
        port=7777,
    )
