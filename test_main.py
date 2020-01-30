from models import User


def test_users():
    user = User(first_name="Ahmed", last_name="Nafies", age=19)
    assert user.first_name == "Ahmed"
