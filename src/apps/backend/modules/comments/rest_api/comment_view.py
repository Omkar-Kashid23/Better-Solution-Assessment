from dataclasses import asdict
from flask import jsonify, request
from flask.views import MethodView
from flask.typing import ResponseReturnValue

from modules.comment.comment_service import CommentService
from modules.comment.types import CreateCommentParams, UpdateCommentParams
from modules.comment.errors import CommentBadRequestError


class CommentView(MethodView):
    def post(self, task_id: str) -> ResponseReturnValue:
        data = request.get_json()
        if not data or "content" not in data:
            raise CommentBadRequestError("content is required")

        params = CreateCommentParams(task_id=task_id, content=data["content"])
        comment = CommentService.create_comment(params)

        return jsonify(asdict(comment)), 201

    def get(self, task_id: str) -> ResponseReturnValue:
        comments = CommentService.get_comments_by_task_id(task_id)
        return jsonify([asdict(c) for c in comments]), 200

    def patch(self, id: str) -> ResponseReturnValue:
        data = request.get_json()
        if not data or "content" not in data:
            raise CommentBadRequestError("content is required")

        params = UpdateCommentParams(content=data["content"])
        comment = CommentService.update_comment(id, params)

        return jsonify(asdict(comment)), 200

    def delete(self, id: str) -> ResponseReturnValue:
        CommentService.delete_comment(id)
        return "", 204
