from flask import Flask, request, abort
app = Flask(__name__)

from barconfig import bars, groups, prefixes

class InputException(Exception):
    pass

def get_state(request):
    if 'state' in request.form:
        if request.form['state'] == 'On':
            return True
        elif request.form['state'] == 'Off':
            return False
        else:
            raise InputException('')

@app.route("/<int:bar>/<int:port>", methods=['GET', 'POST'])
def powerbar_i(bar, port):
    if request.method == 'GET':
        return "Bar: %d, Port %d\n" % (bar, port)
    else:
        state = get_state(request)

        # XXX: Check if bar is valid and return 404 if not
        bars[bar].sockets[port].set_state(state)

        return "Bar: %d, Port %d\n" % (bar, port)

@app.route("/group/<group>", methods=['GET', 'POST'])
def powerbar_g(group):
    if request.method == 'GET':
        pass
    else:
        state = get_state(request)

        print groups[group]
        for socket in groups[group]:
            print socket, state
            socket.set_state(state)

        return "Group: %s\n" % group


@app.route("/prefix/<prefix>", methods=['GET', 'POST'])
def powerbar_p(prefix):
    if request.method == 'GET':
        pass
    else:
        state = get_state(request)

        print prefixes[prefix]
        for group in prefixes[prefix]:
            for socket in group:
                print socket, state
                socket.set_state(state)

        return "Prefix: %s\n" % prefix

if __name__ == "__main__":
    app.run(host='0.0.0.0')
