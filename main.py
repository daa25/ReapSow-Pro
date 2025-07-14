import os
import json
from flask import Flask, request, abort
from fulfillment import process_orders

try:
    import firebase_init  # Handles Firebase setup
    print('Firebase module loaded successfully')
except Exception as e:
    print(f'Warning: Firebase initialization failed: {e}')

app = Flask(__name__)

def route_fulfillment(order_data):
    """Process order fulfillment using the fulfillment module"""
    try:
        print(f"Processing fulfillment for order: {order_data.get('id')}")
        return process_orders(order_data)
    except Exception as e:
        print(f"Error in fulfillment: {e}")
        return False

def log_to_supabase(order_id, status, data):
    """Log order to Supabase"""
    try:
        # Add your Supabase logging logic here
        print(f"Logging to Supabase - Order: {order_id}, Status: {status}, Data: {data}")
        # You can implement actual Supabase logging here when ready
        return True
    except Exception as e:
        print(f"Error logging to Supabase: {e}")
        return False

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    incoming_token = request.headers.get("X-Webhook-Token")
    expected_token = os.environ.get("REAP_WEBHOOK_SECRET")
    if incoming_token != expected_token:
        print("🚫 Unauthorized webhook attempt.")
        abort(403)
    data = request.get_json()
    print("✅ Webhook received:", json.dumps(data, indent=2))
    return "ok", 200

@app.route("/", methods=["GET"])
def index():
    return "ReapSow HQ API is live", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
