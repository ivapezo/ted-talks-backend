# TED Talks Engagement Predictor Backend

This is the backend for the TED Talks Engagement Predictor application. It provides API endpoints for predicting the engagement level of TED Talks videos.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   - Create a `.env` file with the following variables:
     ```
     FLASK_APP=app.py
     FLASK_ENV=production
     PORT=5000
     ```

3. Download NLTK data:
   ```
   python -c "import nltk; nltk.download('punkt')"
   ```

## Running the Application

### Development
```
python app.py
```

### Production
```
gunicorn app:app
```

## API Endpoints

- `GET /`: Default welcome page
- `GET /api/test`: Test endpoint to verify API is working
- `POST /api/predict`: Predict engagement level for a TED Talk video
  - Request body: `{ "videoUrl": "https://www.youtube.com/watch?v=VIDEO_ID" }`
  - Response: Array containing popularity probabilities, engagement probabilities, and feature values

## Deployment

### Railway
1. Create a Railway account at [railway.app](https://railway.app)
2. Install the Railway CLI:
   ```
   npm i -g @railway/cli
   ```
3. Login to Railway:
   ```
   railway login
   ```
4. Initialize a new project:
   ```
   railway init
   ```
5. Deploy the backend:
   ```
   railway up
   ```
6. Set environment variables in the Railway dashboard:
   - `FLASK_APP=app.py`
   - `FLASK_ENV=production`
   - `PORT=5000`

### Heroku
1. Create a Heroku app
2. Connect to your GitHub repository
3. Deploy the backend folder

### PythonAnywhere
1. Upload the backend folder to PythonAnywhere
2. Set up a web app pointing to the app.py file
3. Configure the virtual environment with the required dependencies

### Vercel
1. Create a `vercel.json` file in the root directory:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```
2. Deploy to Vercel

## Model Files

The application requires the following model files in the `models` directory:
- `rfc_popularity (2).sav`: Random Forest model for popularity prediction
- `rfc_engagement (2).sav`: Random Forest model for engagement prediction
- `tfidf_vectorizer.pkl`: TF-IDF vectorizer for text processing
- `count_vectorizer.pkl`: Count vectorizer for text processing
- `le_tags.pkl`: Label encoder for video tags 