class TestCommentAPI:
    def test_create_comment(self, client):
        response = client.post(
            "/api/tasks/1/comments",
            json={"content": "test comment"},
        )
        assert response.status_code == 201

    def test_delete_comment(self, client):
        response = client.delete("/api/comments/1")
        assert response.status_code == 204
