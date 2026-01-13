from modules.comment.internal.store.comment_model import Comment


class CommentReader:
    @staticmethod
    def get_by_id(db, comment_id):
        return db.query(Comment).filter(Comment.id == comment_id).first()

    @staticmethod
    def get_by_task_id(db, task_id):
        return db.query(Comment).filter(Comment.task_id == task_id).all()
