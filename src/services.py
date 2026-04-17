from .models import User, Post, Comment
from .repository import UserRepository, PostRepository, CommentRepository


class BlogService:
    def __init__(self):
        self.users = UserRepository()
        self.posts = PostRepository()
        self.comments = CommentRepository()

    def register_user(self, username: str, email: str) -> User:
        if self.users.find_by_email(email):
            raise ValueError(f"Email already registered: {email}")
        return self.users.create(username, email)

    def write_post(self, author_id: int, title: str, body: str, tags: list[str] = None) -> Post:
        author = self.users.get(author_id)
        if not author:
            raise ValueError(f"User {author_id} not found")
        if not author.is_active:
            raise PermissionError("Inactive users cannot post")
        return self.posts.create(author, title, body, tags)

    def publish_post(self, post_id: int, requester_id: int) -> Post:
        post = self.posts.get(post_id)
        if not post:
            raise ValueError(f"Post {post_id} not found")
        if post.author.id != requester_id:
            raise PermissionError("Only the author can publish their post")
        post.publish()
        return post

    def comment_on_post(self, post_id: int, author_id: int, text: str, parent_id: int = None) -> Comment:
        post = self.posts.get(post_id)
        if not post or not post.is_published():
            raise ValueError("Cannot comment on an unpublished post")
        author = self.users.get(author_id)
        if not author:
            raise ValueError(f"User {author_id} not found")
        parent = self.comments._store.get(parent_id) if parent_id else None
        return self.comments.create(post, author, text, parent)

    def get_feed(self, user_id: int) -> list[Post]:
        return sorted(
            self.posts.list_published(),
            key=lambda p: p.published_at,
            reverse=True,
        )

    def get_user_stats(self, user_id: int) -> dict:
        user_posts = self.posts.list_by_author(user_id)
        published = [p for p in user_posts if p.is_published()]
        all_comments = [
            c for p in published
            for c in self.comments.list_for_post(p.id)
        ]
        return {
            "total_posts": len(user_posts),
            "published_posts": len(published),
            "total_comments_received": len(all_comments),
            "total_words_written": sum(p.word_count() for p in user_posts),
        }


class ModerationService:
    def __init__(self, blog: BlogService):
        self.blog = blog

    def ban_user(self, user_id: int):
        user = self.blog.users.get(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found")
        user.deactivate()

    def remove_post(self, post_id: int):
        store = self.blog.posts._store
        if post_id not in store:
            raise ValueError(f"Post {post_id} not found")
        del store[post_id]

    def get_flagged_posts(self, min_length: int = 5000) -> list[Post]:
        return [p for p in self.blog.posts.list_published() if p.word_count() > min_length]
