import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from contact.models import Contact
from posts.models import Post
from team.models import Team


def test_home_shows_latest_three_posts(client, db):
    for i in range(5):
        Post.objects.create(title=f"post{i}", video="https://youtu.be/dQw4w9WgXcQ")
    res = client.get(reverse("home"))
    assert res.status_code == 200
    assert len(res.context["posts"]) == 3


def test_about_lists_team(client, db):
    Team.objects.create(name="Pat", photo="x.jpg", position="Chef", email="p@example.com")
    res = client.get(reverse("about"))
    assert res.status_code == 200
    assert [t.name for t in res.context["teams"]] == ["Pat"]


def test_posts_paginate_by_six(client, db):
    for i in range(8):
        Post.objects.create(title=f"p{i}", video="https://youtu.be/dQw4w9WgXcQ")
    assert len(client.get(reverse("posts")).context["posts"]) == 6
    assert len(client.get(reverse("posts") + "?page=2").context["posts"]) == 2


def test_post_detail_and_404(client, db):
    p = Post.objects.create(title="Soup", video="https://youtu.be/dQw4w9WgXcQ")
    assert client.get(reverse("post", args=[p.pk])).status_code == 200
    assert client.get(reverse("post", args=[9999])).status_code == 404


@pytest.fixture
def member(db):
    return User.objects.create_user("carol", password="pw-12345-xyz")


def test_contact_requires_login(client, db):
    res = client.get(reverse("contact"))
    assert res.status_code == 302
    assert "login" in res.url


def test_contact_page_for_logged_in_user(client, member):
    client.force_login(member)
    assert client.get(reverse("contact")).status_code == 200


def _inquiry(user, post_id=1):
    return {
        "post_id": post_id,
        "post": "Soup",
        "name": "Carol",
        "email": "c@example.com",
        "phone": "123",
        "message": "hi",
        "user_id": user.id,
    }


def test_contact_saves_inquiry(client, member):
    client.force_login(member)
    res = client.post(reverse("contact"), _inquiry(member))
    assert res.status_code == 302
    assert Contact.objects.filter(user_id=member.id, post_id=1).count() == 1


def test_contact_rejects_duplicate_inquiry(client, member):
    client.force_login(member)
    client.post(reverse("contact"), _inquiry(member))
    client.post(reverse("contact"), _inquiry(member))
    assert Contact.objects.filter(user_id=member.id, post_id=1).count() == 1


def test_payments_page_exposes_publishable_key(client, db, settings):
    settings.STRIPE_PUBLISHABLE_KEY = "pk_test_123"
    res = client.get(reverse("payments"))
    assert res.status_code == 200
    assert res.context["key"] == "pk_test_123"


def test_charge_requires_login_and_is_unconfigured(client, member):
    anon = client.post(reverse("charge"))
    assert anon.status_code == 302
    client.force_login(member)
    assert client.post(reverse("charge")).status_code == 503
