from flask import Blueprint
from modules.comment.rest_api.comment_view import CommentView


class CommentRouter:
    @staticmethod
    def create_route(*, blueprint: Blueprint) -> Blueprint:
        blueprint.add_url_rule(
            "/tasks/<task_id>/comments",
            view_func=CommentView.as_view("comment_create"),
            methods=["POST", "GET"],
        )

        blueprint.add_url_rule(
            "/comments/<id>",
            view_func=CommentView.as_view("comment_update"),
            methods=["PATCH", "DELETE"],
        )

        return blueprint
