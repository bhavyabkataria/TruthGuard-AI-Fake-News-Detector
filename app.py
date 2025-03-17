from flask import Flask, request, jsonify
import tensorflow as tf
from text_processing import preprocess_text

app = Flask(__name__)
model = tf.keras.models.load_model('models/fake_news_model.h5')  # Pretrained model

@app.route('/scan', methods=['POST'])
def scan_text():
    try:
        data = request.json
        text = data.get('text', '')
        processed_text = preprocess_text(text)
        prediction = model.predict([processed_text])[0][0]
        return jsonify({
            "is_fake": bool(prediction > 0.7),  # Threshold for fake news
            "confidence": float(prediction),
            "explanation": "High emotional language and unverified sources detected."
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)