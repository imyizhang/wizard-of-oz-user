import urllib.parse

import requests


class Client:
    """A client for service-to-service communication."""

    def __init__(self, base_url: str, api_key: str):
        """Initialize the client with API base URL and API key."""
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        self.test_connection()

    def test_connection(self):
        """Verify that API connection is working."""
        response = requests.get(
            urllib.parse.urljoin(self.base_url, "/api/test"),
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()

    def get_messages(self):
        """Get all messages from the server."""
        response = requests.get(
            urllib.parse.urljoin(self.base_url, "/api/messages"),
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()["messages"]

    def clear_messages(self):
        """Clear all messages on the server."""
        response = requests.delete(
            urllib.parse.urljoin(self.base_url, "/api/messages"),
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()

    def post_message(
        self,
        role: str,
        content: str,
        files: list | None = None,
        reasoning: str | None = None,
        feedback: str | None = None,
    ):
        """Submit a new message to the server."""
        payload = {
            "role": role,
            "content": content,
            "files": files,
            "reasoning": reasoning,
            "feedback": feedback,
        }
        response = requests.post(
            urllib.parse.urljoin(self.base_url, "/api/messages"),
            json=payload,
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()

    def update_message(self, index: int, feedback: int):
        """Update a message on the server."""
        payload = {"feedback": feedback}
        response = requests.put(
            urllib.parse.urljoin(self.base_url, f"/api/messages/{index}"),
            json=payload,
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()
