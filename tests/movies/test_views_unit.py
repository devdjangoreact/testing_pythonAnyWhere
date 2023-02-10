# app/tests/movies/test_views_unit.py

import pytest
from django.http import Http404

from movies.views import MovieSerializer, MovieViewSet


def test_add_movie(client, monkeypatch):
    payload = {"title": "The Big Lebowski", "genre": "comedy", "year": "1998"}

    def mock_create(self, payload):
        return "The Big Lebowski"

    monkeypatch.setattr(MovieSerializer, "create", mock_create)
    monkeypatch.setattr(MovieSerializer, "data", payload)

    resp = client.post("/api/movies/", payload, content_type="application/json")
    assert resp.status_code == 201
    assert resp.data["title"] == "The Big Lebowski"


def test_add_movie_invalid_json(client):
    resp = client.post("/api/movies/", {}, content_type="application/json")
    assert resp.status_code == 400


def test_add_movie_invalid_json_keys(client):
    resp = client.post(
        "/api/movies/",
        {"title": "The Big Lebowski", "genre": "comedy"},
        content_type="application/json",
    )

    assert resp.status_code == 400


def test_get_single_movie(client, monkeypatch):
    payload = {"title": "The Big Lebowski", "genre": "comedy", "year": "1998"}

    def mock_get_object(self):
        return 1

    monkeypatch.setattr(MovieViewSet, "get_object", mock_get_object)
    monkeypatch.setattr(MovieSerializer, "data", payload)

    resp = client.get(f"/api/movies/1/")
    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"


def test_get_single_movie_incorrect_id(client):
    resp = client.get(f"/api/movies/foo/")
    assert resp.status_code == 404


def test_get_all_movies(client, monkeypatch):
    payload = [
        {"title": "The Big Lebowski", "genre": "comedy", "year": "1998"},
        {"title": "No Country for Old Men", "genre": "triller", "year": "2007"},
    ]

    def mock_get_all_movies(self):
        return payload

    monkeypatch.setattr(MovieViewSet, "get_queryset", mock_get_all_movies)
    monkeypatch.setattr(MovieSerializer, "data", payload)

    resp = client.get(f"/api/movies/")

    assert resp.status_code == 200
    assert resp.data[0]["title"] == payload[0]["title"]
    assert resp.data[1]["title"] == payload[1]["title"]


def test_remove_movie(client, monkeypatch):
    def mock_get_object(self):
        class Movie:
            def delete():
                pass

        return Movie

    monkeypatch.setattr(MovieViewSet, "get_object", mock_get_object)

    resp = client.delete(f"/api/movies/1/")
    assert resp.status_code == 204


def test_remove_movie_incorrect_id(client, monkeypatch):
    def mock_get_object(self):
        raise Http404

    monkeypatch.setattr(MovieViewSet, "get_object", mock_get_object)

    resp = client.delete(f"/api/movies/99/")
    assert resp.status_code == 404


def test_update_movie(client, monkeypatch):
    payload = {"title": "The Big Lebowski", "genre": "comedy", "year": "1998"}

    def mock_get_object(self):
        return 1

    def mock_update_object(self, movie_object, data):
        return payload

    monkeypatch.setattr(MovieViewSet, "get_object", mock_get_object)
    monkeypatch.setattr(MovieSerializer, "update", mock_update_object)

    resp = client.put(f"/api/movies/1/", payload, content_type="application/json")
    assert resp.status_code == 200
    assert resp.data["title"] == payload["title"]
    assert resp.data["year"] == payload["year"]


def test_update_movie_incorrect_id(client, monkeypatch):
    def mock_get_object(self):
        raise Http404

    monkeypatch.setattr(MovieViewSet, "get_object", mock_get_object)

    resp = client.put(f"/api/movies/99/")
    assert resp.status_code == 404


@pytest.mark.parametrize(
    "payload, status_code",
    [[{}, 400], [{"title": "The Big Lebowski", "genre": "comedy"}, 400]],
)
def test_update_movie_invalid_json(client, monkeypatch, payload, status_code):
    def mock_get_object(self):
        return 1

    monkeypatch.setattr(MovieViewSet, "get_object", mock_get_object)

    resp = client.put(f"/api/movies/1/", payload, content_type="application/json")
    assert resp.status_code == status_code
