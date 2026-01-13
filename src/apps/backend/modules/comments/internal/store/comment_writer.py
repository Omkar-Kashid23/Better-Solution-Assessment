from modules.comment.internal.store.comment_model import Comment


class CommentWriter:
    @staticmethod
    def create(db, task_id, content):
        comment = Comment(task_id=task_id, content=content)
        db.add(comment)
        db.commit()
        db.refresh(comment)
        return comment
