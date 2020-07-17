from flask import Flask, render_template
from ics import Calendar


def create_app():
    app = Flask(__name__)
    return app


def get_events(filename):
    # calendar = Calendar(open('./tests/basic_test.ics', 'r').read())
    # calendar = Calendar(open('./app/basic.ics', 'r').read())
    calendar = Calendar(open(filename, 'r').read())
    events = calendar.events
    return events


def get_filtered_events(events):
    filtered_events = [events for events in events if events.begin.year > 2019]
    return filtered_events


def get_ordered_events(events):
    ordered_events = sorted(get_filtered_events(events), reverse=True)
    return ordered_events


# events = get_ordered_events()

#app = create_app()


#@app.route('/')
#def index():
    #return "Hello world"

# @app.route("/")
# def index():
#   context = {
#       'events': events,
#   }
#   return render_template('index.html', **context)