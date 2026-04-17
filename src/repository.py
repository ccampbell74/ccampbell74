from typing import Optional
from .models import User, Post, Comment


class UserRepository:
    def __init__(self):
        self._store: dict[int, User] = {}
        self._next_id = 1

    def create(self, username: str, email: str) -> User:
        user = User(id=self._next_id, username=username, email=email)
        self._store[user.id] = user
        self._next_id += 1
        return user

    def get(self, user_id: int) -> Optional[User]:
        return self._store.get(user_id)

    def find_by_email(self, email: str) -> Optional[User]:
        return next((u for u in self._store.values() if u.email == email), None)

    def list_active(self) -> list[User]:
        return [u for u in self._store.values() if u.is_active]


class PostRepository:
    def __init__(self):
        self._store: dict[int, Post] = {}
        self._next_id = 1

    def create(self, author: User, title: str, body: str, tags: list[str] = None) -> Post:
        post = Post(id=self._next_id, author=author, title=title, body=body, tags=tags or [])
        self._store[post.id] = post
        self._next_id += 1
        return post

    def get(self, post_id: int) -> Optional[Post]:
        return self._store.get(post_id)

    def list_published(self) -> list[Post]:
        return [p for p in self._store.values() if p.is_published()]

    def list_by_author(self, user_id: int) -> list[Post]:
        return [p for p in self._store.values() if p.author.id == user_id]

    def list_by_tag(self, tag: str) -> list[Post]:
        return [p for p in self._store.values() if tag in p.tags]


class CommentRepository:
    def __init__(self):
        self._store: dict[int, Comment] = {}
        self._next_id = 1

    def create(self, post: Post, author: User, text: str, parent: Comment = None) -> Comment:
        comment = Comment(id=self._next_id, post=post, author=author, text=text, parent=parent)
        self._store[comment.id] = comment
        self._next_id += 1
        return comment

    def list_for_post(self, post_id: int) -> list[Comment]:
        return [c for c in self._store.values() if c.post.id == post_id]

    def list_top_level(self, post_id: int) -> list[Comment]:
        return [c for c in self.list_for_post(post_id) if not c.is_reply()]
