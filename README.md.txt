# Travel Booking API QA System

## 🚀 Overview

A QA-focused project simulating a travel booking system. It demonstrates end-to-end API testing using manual and automated approaches.

---

## 🧠 Features

* REST API for search, booking, and cancellation
* Manual API testing using Postman
* Automated testing using PyTest
* Edge case and negative scenario validation

---

## 🛠️ Tech Stack

* Python (Flask)
* PyTest (automation)
* Postman (manual testing)

---

## 🔌 API Endpoints

### Search Routes

GET `/search?from=Delhi&to=Agra`

### Book Ticket

POST `/book`
{
"route_id": 1,
"user": "Abdullah"
}

### Cancel Booking

POST `/cancel`
{
"booking_id": 1
}

---

## 🧪 Testing

### Manual Testing

* Performed using Postman
* Validated status codes, JSON responses, and edge cases

### Automated Testing

Run tests:
pytest -v

---

## 🐞 Bug Identified

* API allows multiple cancellations of the same booking without validating current status

---

## 💼 Key QA Learnings

* API validation (status codes, JSON structure)
* Test case design (positive and negative scenarios)
* Automation using PyTest
* Debugging API issues (415 errors, incorrect endpoints)

---

## 👨‍💻 Author

Abdullah Khan
