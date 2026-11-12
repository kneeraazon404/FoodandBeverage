import pytest
from django.contrib.auth.models import User
from django.urls import reverse

REGISTER = {
    "first_name": "A",
    "last_name": "B",
    "username": "alice",
    "email": "alice@example.com",
    "password": "pw-12345-xyz",
    "password2": "pw-12345-xyz",
}


@pytest.fixture
def user(db):
    return User.objects.create_user("bob", "bob@example.com", "pw-12345-xyz")


def test_register_page(client, db):
    assert client.get(reverse("register")).status_code == 200


def test_register_creates_user(client, db):
    res = client.post(reverse("register"), REGISTER)
    assert res.status_code == 302
    assert res.url == reverse("login")
    assert User.objects.filter(username="alice").exists()


def test_register_password_mismatch(client, db):
    res = client.post(reverse("register"), {**REGISTER, "password2": "nope"})
    assert res.status_code == 302
    assert res.url == reverse("register")
    assert not User.objects.filter(username="alice").exists()


def test_register_duplicate_username(client, user):
    client.post(reverse("register"), {**REGISTER, "username": "bob"})
    assert User.objects.filter(username="bob").count() == 1


def test_register_duplicate_email(client, user):
    client.post(reverse("register"), {**REGISTER, "email": "bob@example.com"})
    assert not User.objects.filter(username="alice").exists()


def test_login_success_and_failure(client, user):
    bad = client.post(reverse("login"), {"username": "bob", "password": "wrong"})
    assert bad.url == reverse("login")
    ok = client.post(reverse("login"), {"username": "bob", "password": "pw-12345-xyz"})
    assert ok.url == reverse("dashboard")
    assert "_auth_user_id" in client.session


def test_logout_requires_post(client, user):
    client.force_login(user)
    assert client.get(reverse("logout")).status_code == 405
    assert "_auth_user_id" in client.session
    assert client.post(reverse("logout")).status_code == 302
    assert "_auth_user_id" not in client.session


def test_dashboard_redirects_home(client, db):
    assert client.get(reverse("dashboard")).url == reverse("home")
