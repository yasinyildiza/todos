class TestItemsSearch:
    endpoint = '/api/v1/items'

    def test_search(self, test_client):
        rv = test_client.get(self.endpoint)
        assert rv.status_code == 200
        assert rv.json() == {'data': []}
