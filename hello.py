def app(environ, start_response):
    start_response('200 0K', [('Content-Type', 'text/plain')])
    return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), encoding='utf-8')]
