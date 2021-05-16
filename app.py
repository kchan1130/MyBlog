from flask import Flask, render_template


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
    app.run(
        debug=False,
        port=7777,
    )

