from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data store for privacy tracking
privacy_data = []

@app.route('/api/privacy', methods=['POST'])
def add_privacy_item():
    """Add a privacy tracking item"""
    data = request.get_json()
    privacy_data.append(data)
    return jsonify({'message': 'Privacy item added successfully'}), 201

@app.route('/api/privacy', methods=['GET'])
def get_privacy_items():
    """Retrieve all privacy tracking items"""
    return jsonify(privacy_data), 200

@app.route('/api/privacy/<int:item_id>', methods=['DELETE'])
def delete_privacy_item(item_id):
    """Delete a privacy tracking item"""
    if item_id < len(privacy_data):
        privacy_data.pop(item_id)
        return jsonify({'message': 'Privacy item deleted successfully'}), 200
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)