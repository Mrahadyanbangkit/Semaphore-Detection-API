from flask import Flask, request, jsonify
from semaphore_detection import detect_semaphore  # Import your semaphore detection logic

app = Flask(__name__)

@app.route('/detect-semaphore', methods=['POST'])
def detect_semaphore_route():
    try:
        # Assuming the image data is sent as JSON in the request
        image_data = request.json.get('image_data')

        # Perform semaphore detection
        result = detect_semaphore(image_data)

        # Return the result as JSON
        return jsonify({'result': result})

    except Exception as e:
        # Handle exceptions, log them, etc.
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Use the PORT environment variable or default to 3000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=port)
