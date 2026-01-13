from modules.comment.comment_service import CommentService
from modules.comment.types import CreateCommentParams


def test_create_comment_service():
    params = CreateCommentParams(task_id="1", content="hello")
    comment = CommentService.create_comment(params)
    assert comment.content == "hello"
