from httpx import AsyncClient
import pytest


@pytest.mark.asyncio(scope="session")
async def test_create_user(ac: AsyncClient):
    response = await ac.post(
        "/create_user",
        json={
            "first_name": "test_name",
            "last_name": "test_last_name",
            "age": 21
        },
    )

    assert response.status_code == 200

    response = response.json()

    assert response["last_name"] == "test_last_name"
    assert response["first_name"] == "test_name"
    assert response["age"] == 21
