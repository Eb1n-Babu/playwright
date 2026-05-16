from playwright.sync_api import sync_playwright, expect

def test_simple_api_validation():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        # Send a GET request
        response = request_context.get("http://127.0.0.1:8000/auth/")

        # Validate status code
        assert response.status == 200

        # Clean up
        request_context.dispose()
