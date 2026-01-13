from dataclasses import dataclass


@dataclass
class CreateCommentParams:
    task_id: str
    content: str


@dataclass
class UpdateCommentParams:
    content: str
