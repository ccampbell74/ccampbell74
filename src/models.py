from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: int
    username: str
    email: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True

    def deactivate(self):
        self.is_active = False

    def display_name(self) -> str:
        return self.username.title()


@dataclass
class Post:
    id: int
    author: User
    title: str
    body: str
    published_at: Optional[datetime] = None
    tags: list[str] = field(default_factory=list)

    def publish(self):
        self.published_at = datetime.utcnow()

    def is_published(self) -> bool:
        return self.published_at is not None

    def word_count(self) -> int:
        return len(self.body.split())


@dataclass
class Comment:
    id: int
    post: Post
    author: User
    text: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    parent: Optional["Comment"] = None

    def is_reply(self) -> bool:
        return self.parent is not None
