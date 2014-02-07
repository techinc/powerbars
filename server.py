from flask import Flask, request, abort, render_template
app = Flask(__name__)
app.debug = True

from barconfig import bars, groups, groups_state, presets

import json

ALLOW_GET = False # True to allow GET requests

class InputException(Exception):
    pass

def get_state(request):
    if 'state' in request.form:
        if request.form['state'] == 'On':
            return True
        elif request.form['state'] == 'Off':
            return False

    raise InputException('')

def group_set_state(group, socket, state):
    if state:
        if group not in socket.refcount:
            socket.refcount.append(group)
        socket.set_state(state)
    else:
        if group in socket.refcount:
            socket.refcount.remove(group)
        if len(socket.refcount) == 0:
            socket.set_state(state)



def flip_state(state_dict, key, state):
    if state_dict[key] == None:
        state_dict[key] = state
        return True

    if state_dict[key]:
        if state:
            return True
        else:
            state_dict[key] = False
            return True
    else:
        if state:
            state_dict[key] = True
            return True
        else:
            return True
    return False


def print_state():
    s = ""
    for bar in bars:
        for socket in bar.sockets:
            s += '%d is at count: %s\n' % (socket.num, str(socket.refcount))

    for k, v in groups_state.iteritems():
        s += '%s: %s\n' % (k, str(v))

    print s
    return s

@app.route("/")
def index():
    return render_template('9000.html')

@app.route("/<int:bar>/<int:port>", methods=['GET', 'POST'])
def powerbar_i(bar, port):
    # TODO: Disable this in general
    if request.method == 'GET':
        return json.dumps({str(bars[bar].sockets[port]) :
                str(bars[bar].sockets[port].state)})
    else:
        state = get_state(request)

        # XXX: Check if bar is valid and return 404 if not
        bars[bar].sockets[port].set_state(state)

        return "Bar: %d, Port %d\n" % (bar, port)

@app.route("/group/<group>", methods=['GET', 'POST'])
def powerbar_g(group):
    if request.method == 'GET':
        states = []
        for socket in groups[group]:
            states.append((str(socket), str(socket.state)))
        return json.dumps(states)
    else:
        state = get_state(request)

        if flip_state(groups_state, group, state):
            for socket in groups[group]:
                group_set_state(group, socket, state)

            print_state()

            return render_template('status.html', group=group,
                    state="ON" if state else "OFF")


@app.route("/preset/<preset>", methods=['GET','POST'])
def powerbar_p(preset):
    if request.method == 'GET':
        pass
    else:
        for state in presets[preset]:
            state = state == 'On'
            for group in presets[preset]['On' if state else 'Off']:
                if flip_state(groups_state, group, state):
                    for socket in groups[group]:
                        group_set_state(group, socket, state)

        print_state()

        return "Prefix: %s\n" % preset

if __name__ == "__main__":
    app.run(host='0.0.0.0')
