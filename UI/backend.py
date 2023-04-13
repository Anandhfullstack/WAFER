#!flask/bin/python
import io

from flask import Flask, render_template, request, send_file
# from gevent.pywsgi import WSGIServer


app = Flask(__name__)


@app.route('/')
def indexv2():
    return render_template('indexv2.html', show_details=False)

def main():
    app.run(debug=False, host='0.0.0.0', port=5002)
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()

if __name__ == '__main__':
    main()
