from modules.comment.internal.store.comment_reader import CommentReader
from modules.comment.internal.store.comment_writer import CommentWriter
from modules.comment.internal.store.comment_repository import CommentRepository
from modules.comment.errors import CommentNotFoundError
from modules.comment.types import CreateCommentParams, UpdateCommentParams
from modules.application.database import get_db_session


class CommentService:
    @staticmethod
    def create_comment(params: CreateCommentParams):
        db = get_db_session()
        return CommentWriter.create(db, params.task_id, params.content)

    @staticmethod
    def get_comments_by_task_id(task_id: str):
        db = get_db_session()
        return CommentReader.get_by_task_id(db, task_id)

    @staticmethod
    def update_comment(comment_id: str, params: UpdateCommentParams):
        db = get_db_session()
        comment = CommentReader.get_by_id(db, comment_id)

        if not comment:
            raise CommentNotFoundError("Comment not found")

        comment.content = params.content
        return CommentRepository.save(db, comment)

    @staticmethod
    def delete_comment(comment_id: str):
        db = get_db_session()
        comment = CommentReader.get_by_id(db, comment_id)

        if not comment:
            raise CommentNotFoundError("Comment not found")

        CommentRepository.delete(db, comment)
