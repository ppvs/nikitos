from bottle import route, run, template, HTTPResponse

@route('/health')
def index():
    status_code = 200
    return HTTPResponse(status=status_code)

@route('/cable')
def index():
    status_code = 200
    return HTTPResponse(status=status_code)


run(host='0.0.0.0', port=8080)
