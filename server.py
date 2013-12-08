from flask import Flask, request, abort
app = Flask(__name__)

from barconfig import bars

@app.route("/<int:bar>/<int:port>", methods=['GET', 'POST'])
def powerbar_i(bar, port):
    if request.method == 'GET':
        return "Bar: %d, Port %d\n" % (bar, port)
    else:
        if 'state' in request.form:
            if request.form['state'] == 'On':
                state = True
            elif request.form['state'] == 'Off':
                state = False
            else:
                return 'Go away\n'
            bars[bar].sockets[port].set_state(state)
            return "Bar: %d, Port %d\n" % (bar, port)
        return 'Go away\n'

@app.route("/group/<int:bar>", methods=['GET', 'POST'])
def powerbar_g(bar, port):
    if request.method == 'GET':
        return "Bar: %d, Port %d\n" % (bar, port)
    else:
        return "Bar: %d, Port %d\n" % (bar, port)

@app.route("/prefix/<int:bar>", methods=['GET', 'POST'])
def powerbar_p(bar, port):
    if request.method == 'GET':
        return "Bar: %d, Port %d\n" % (bar, port)
    else:
        return "Bar: %d, Port %d\n" % (bar, port)

if __name__ == "__main__":
    app.run()
