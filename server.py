from flask import Flask, request, abort, render_template
app = Flask(__name__)
app.debug = True

from barconfig import bars, groups, groups_state #,prefixes

ALLOW_GET = False # True to allow GET requests

class InputException(Exception):
    pass

def get_state(request, post=True):
    if post:
        if 'state' in request.form:
            if request.form['state'] == 'On':
                return True
            elif request.form['state'] == 'Off':
                return False
    elif ALLOW_GET:
        if request.args.get('state') == 'On':
            return True
        elif request.args.get('state') == 'Off':
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

@app.route("/<int:bar>/<int:port>", methods=['POST'])
def powerbar_i(bar, port):
    # TODO: Disable this in general
    if request.method == 'GET':
        return "Bar: %d, Port %d\n" % (bar, port)
    else:
        state = get_state(request, request.method=='POST')

        # XXX: Check if bar is valid and return 404 if not
        bars[bar].sockets[port].set_state(state)

        return "Bar: %d, Port %d\n" % (bar, port)

@app.route("/group/<group>", methods=['POST'])
def powerbar_g(group):
    state = get_state(request, request.method=='POST')

    if flip_state(groups_state, group, state):
        for socket in groups[group]:
            group_set_state(group, socket, state)

        print_state()

        return render_template('status.html', group=group,
                state="ON" if state else "OFF")


#@app.route("/prefix/<prefix>", methods=['POST'])
#def powerbar_p(prefix):
#    if request.method == 'GET':
#        pass
#    else:
#        state = get_state(request)
#
#        for group in prefixes[prefix]:
#            for socket in group:
#                threshold_set_state(socket, state)
#                #socket.set_state(state)
#
#        print_state()
#
#        return "Prefix: %s\n" % prefix

if __name__ == "__main__":
    app.run(host='0.0.0.0')
