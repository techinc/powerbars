from flask import Flask, request, abort
app = Flask(__name__)
app.debug=True

from barconfig import bars, groups, groups_state #,prefixes

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
        socket.set_state(state)



def flip_state(state_dict, key, state):
    if state_dict[key] == None:
        state_dict[key] = state
        return True

    # TODO: Add None
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
    for bar in bars:
        for socket in bar.sockets:
            print socket.num, 'is at count:', socket.refcount

    for k, v in groups_state.iteritems():
        print k, v

@app.route("/<int:bar>/<int:port>", methods=['GET', 'POST'])
def powerbar_i(bar, port):
    # TODO: Disable this in general
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


    if flip_state(groups_state, group, state):
        for socket in groups[group]:
            group_set_state(group, socket, state)

        print_state()

        return "Group: %s\n" % group


#@app.route("/prefix/<prefix>", methods=['GET', 'POST'])
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
