from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os


app = Flask(__name__)

# 配置 Gemini API
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)


def analyze_sentiment(text):
    """使用 Gemini 進行情感分析"""
    prompt = f"""請對以下文字情感進行簡短評分。100 分為完全正面；0 分為完全負面，並給出評價（正面/負面/中性），以及對應的表情符號。
	只需給出評分，不必說明原因。
	例如：「正面，80分。😄」
    文字內容：{text}"""

    model = genai.GenerativeModel('gemini-2.0-flash-001')
    response = model.generate_content(prompt)

    return response.text


@app.route('/', methods=['GET'])
def index():
    """渲染主頁"""
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def sentiment_analysis():
    """處理情感分析請求"""
    data = request.json
    text = data.get('text', '').strip()

    if not text:
        return jsonify({
            'error': '請提供要分析的文字內容'
        }), 400

    try:
        sentiment_result = analyze_sentiment(text)
        return jsonify({
            'input_text': text,
            'sentiment_analysis': sentiment_result
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
