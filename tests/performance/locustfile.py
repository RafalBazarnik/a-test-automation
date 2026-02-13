import os

from locust import HttpUser, between, task


class PublicApiUser(HttpUser):
    """Basic API performance scenario for jsonplaceholder-like endpoints."""

    wait_time = between(1, 3)

    def on_start(self) -> None:
        # Allows overriding through env var while keeping a sensible default.
        self.host = os.getenv("LOCUST_HOST") or os.getenv(
            "API_BASE_URL", "https://jsonplaceholder.typicode.com"
        )

    @task(3)
    def get_todo(self) -> None:
        self.client.get("/todos/1", name="GET /todos/1")

    @task(1)
    def get_post(self) -> None:
        self.client.get("/posts/1", name="GET /posts/1")
