from nose.tools import *
import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.gt("/", follow_redirects=True)
    assert_equal(rv.status_code, 404)
    rv = web.get("/", follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"fill out this form", rv.data)
    data = {"name": "Raja", "greet": "hola"}
    rv = web.post('/', follow_redirects=True, data=data)
    assert_in(b"Zed", rv.data)
    assert_in(b"Hola", rv.data)
