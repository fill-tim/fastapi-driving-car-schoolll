from httpx import AsyncClient
import pytest
from sqlalchemy import select
from conftest import async_session_maker, User


@pytest.mark.asyncio(scope="session")
async def test_list(ac: AsyncClient):
    async with async_session_maker() as db:
        test_user1 = User(first_name="test1", last_name="test1", age=10)
        test_user2 = User(first_name="test2", last_name="test2", age=11)
        test_user3 = User(first_name="test3", last_name="test3", age=12)

        db.add_all([test_user1, test_user2, test_user3])
        await db.commit()

    response = await ac.get(f"user/list")

    assert response.status_code == 200

    response = response.json()
    print(response)
    assert response[0]["last_name"] == "test1"
    assert response[0]["first_name"] == "test1"
    assert response[0]["age"] == 10


@pytest.mark.asyncio(scope="session")
async def test_create(ac: AsyncClient):
    response = await ac.post(
        "user/create",
        json={"first_name": "test_name", "last_name": "test_last_name", "age": 21},
    )

    assert response.status_code == 200

    response = response.json()
    print(response)

    assert response["first_name"] == "test_name"
    assert response["last_name"] == "test_last_name"
    assert response["age"] == 21
    assert response["school_id"] == None
    assert response["role_id"] == None
    assert response["photo"] == None
    assert response["telegram_user_id"] == None


@pytest.mark.asyncio(scope="session")
async def test_get_by_id(ac: AsyncClient):
    async with async_session_maker() as db:
        test_user = User(first_name="test1", last_name="test1", age=10)

        db.add(test_user)
        await db.commit()
        await db.refresh(test_user)

    response = await ac.get(f"user/get_by_id/{test_user.id}")

    assert response.status_code == 200

    response = response.json()

    assert response["last_name"] == "test1"
    assert response["first_name"] == "test1"
    assert response["age"] == 10


@pytest.mark.asyncio(scope="session")
async def test_update(ac: AsyncClient):
    async with async_session_maker() as db:
        test_user = User(first_name="test2", last_name="test2", age=11)

        db.add(test_user)
        await db.commit()
        await db.refresh(test_user)

        user_id = test_user.id

    response = await ac.patch(
        "user/update",
        json={"id": user_id, "first_name": "test_2", "last_name": "test_2", "age": 12},
    )

    async with async_session_maker() as db:
        user = await db.execute(select(User).filter_by(id=test_user.id))
        user = user.scalar()

    assert response.status_code == 200

    response = response.json()

    assert response["rowcount"] == 1

    assert user.last_name == "test_2"
    assert user.first_name == "test_2"
    assert user.age == 12
