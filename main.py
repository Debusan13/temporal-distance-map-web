import os
import time
from flask import Flask, render_template, request, url_for
from rq import Queue
from redis import Redis
from MapLogic import do_thing, get_static_img
from worker import work


def queue_work():
    # Tell RQ what Redis connection to use
    conn = Redis()
    q = Queue(connection=conn, default_timeout=3600)

    job = q.enqueue(work)
    


def get_progress (file):
    x = True
    while x:
        with open(file, 'r') as f:
            last_line = f_read.readlines()[-1]
            prev_line = last_line
            if (prev_line == last_line):
                x = False
            else:
                time.sleep(1)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html", map_preview_src = "https://via.placeholder.com/2048")


@app.route("/", methods=['GET', 'POST'])
def form_post():
    placeholder = "https://via.placeholder.com/2048"
    preview_src = placeholder

    if request.method == "POST":

        req = request.form
        
        if 'Preview' in req:
            lat = req["lat"]
            long = req["long"]
            key = req["apiKey"]

            get_static_img(lat, long, key)
            preview_src = url_for('static', filename='geoImage.png')
        elif 'Submit' in req:
            lat = req["lat"]
            long = req["long"]
            key = req["apiKey"]

            get_static_img(lat, long, key)
            do_thing(lat, long, key)
            preview_src = url_for('static', filename='geoImage.png')
            queue_work()

            


    return render_template("main.html", map_preview_src = preview_src)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == "__main__":
    app.run(debug=True)

