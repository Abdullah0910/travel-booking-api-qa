import requests

BASE_URL = "http://127.0.0.1:5000"

def test_search_valid():
    res = requests.get(f"{BASE_URL}/search?from=Delhi&to=Agra")
    assert res.status_code == 200
    assert "routes" in res.json()

def test_search_missing_params():
    res = requests.get(f"{BASE_URL}/search")
    assert res.status_code == 400

def test_booking_flow():
    booking = requests.post(f"{BASE_URL}/book", json={
        "route_id": 1,
        "user": "Abdullah"
    })

    assert booking.status_code == 201
    booking_id = booking.json()["booking_id"]

    cancel = requests.post(f"{BASE_URL}/cancel", json={
        "booking_id": booking_id
    })

    assert cancel.status_code == 200