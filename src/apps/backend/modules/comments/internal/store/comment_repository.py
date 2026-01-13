class CommentRepository:
    @staticmethod
    def save(db, comment):
        db.add(comment)
        db.commit()
        db.refresh(comment)
        return comment

    @staticmethod
    def delete(db, comment):
        db.delete(comment)
        db.commit()
