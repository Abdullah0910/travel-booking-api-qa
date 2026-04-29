# Travel Booking API QA System

## Overview

A QA-focused project simulating a travel booking system. It demonstrates end-to-end API testing using manual and automated approaches.


## Features

1. REST API for search, booking, and cancellation
2. Manual API testing using Postman
3. Automated testing using PyTest
4. Edge case and negative scenario validation


## Tech Stack

* Python (Flask)
* PyTest (automation)
* Postman (manual testing)

-
## API Endpoints

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


## Testing

### Manual Testing

* Performed using Postman
* Validated status codes, JSON responses, and edge cases

### Automated Testing

Run tests:
pytest -v


## Bug Identified

- Issue: Booking can be cancelled multiple times
- Expected: Should return error if already cancelled
- Impact: Incorrect system behavior

---

## Key QA Learnings

* API validation (status codes, JSON structure)
* Test case design (positive and negative scenarios)
* Automation using PyTest
* Debugging API issues (415 errors, incorrect endpoints)

## Screenshorts
<img width="848" height="212" alt="localtestcase passed" src="https://github.com/user-attachments/assets/ab399cf3-166a-4df1-8c60-bfd524abd5b2" />

<img width="848" height="212" alt="localtestcase passed" src="https://github.com/user-attachments/assets/9c133abc-a783-4ff2-bf3c-5a77617e8559" />

<img width="844" height="568" alt="image" src="https://github.com/user-attachments/assets/df7607b5-1bc5-44f8-a141-80a7855e3cc0" />

<img width="795" height="529" alt="image" src="https://github.com/user-attachments/assets/306b40e2-577c-4fa4-9abd-64891301ddc0" />





---
Author
Abdullah Khan

