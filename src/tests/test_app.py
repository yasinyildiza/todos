import fastapi

class TestApp:

    def test_health(self, test_client):
        rv = test_client.get('/health')
        assert rv.status_code == 200
        assert rv.json() == {'success': True}
