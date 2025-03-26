# Sentiment Analysis Web Application

A web application that performs simple sentiment analysis on text using Google's Gemini AI model.

## Installation

### Local Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sentiment_analysis_web
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variable for Gemini API key:
   ```
   export GEMINI_API_KEY=your_api_key_here
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Access the application at http://localhost:8080

### Docker Setup

1. Build the Docker image:
   ```
   docker build -t sentiment-analysis-web .
   ```

2. Run the container with your API key:
   ```
   docker run -p 8080:8080 -e GEMINI_API_KEY=your_api_key_here sentiment-analysis-web
   ```

3. Access the application at http://localhost:8080
