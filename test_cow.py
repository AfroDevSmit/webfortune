import pytest
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_cowsay(app, client):
    message = 'hello'
    res = client.get(f'/cowsay/{message}/')
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert message in page_output


def test_fortune(app, client):
    res = client.get('/fortune/')
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert '(oo)' in page_output
