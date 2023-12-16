from flask import Flask, render_template, request
from ssl_checker import SSLChecker

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hosts = request.form.get('hosts', '').split(',')
        analyze = 'analyze' in request.form
        verbose = 'verbose' in request.form

        args = {
            'hosts': hosts,
            'analyze': analyze,
            'verbose': verbose
        }

        ssl_checker = SSLChecker()
        result = ssl_checker.show_result(ssl_checker.get_args(json_args=args))
        return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
