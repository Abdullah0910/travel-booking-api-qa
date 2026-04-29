from flask import Flask, request, jsonify

app = Flask(__name__)

bookings = []

@app.route('/search')
def search():
    source = request.args.get('from')
    dest = request.args.get('to')

    if not source or not dest:
        return jsonify({"error": "Missing parameters"}), 400

    return jsonify({
        "routes": [
            {"id": 1, "from": source, "to": dest, "price": 500}
        ]
    }), 200


@app.route('/book', methods=['POST'])
def book():
    data = request.json

    if not data.get("route_id") or not data.get("user"):
        return jsonify({"error": "Invalid booking data"}), 400

    booking = {
        "booking_id": len(bookings) + 1,
        "route_id": data["route_id"],
        "user": data["user"],
        "status": "CONFIRMED"
    }

    bookings.append(booking)
    return jsonify(booking), 201


@app.route('/cancel', methods=['POST'])
def cancel():
    booking_id = request.json.get("booking_id")

    for b in bookings:
        if b["booking_id"] == booking_id:
            b["status"] = "CANCELLED"
            return jsonify({"message": "Cancelled"}), 200

    return jsonify({"error": "Booking not found"}), 404


@app.route('/health')
def health():
    return {"status": "OK"}, 200

def home():
    return {"message": "Travel API Running"}, 200


if __name__ == "__main__":
    app.run(debug=True)