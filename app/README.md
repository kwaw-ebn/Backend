# Malaria Prediction Backend

This is a **FastAPI backend** for malaria prediction and Nigeria map data.  
It serves:

- **User API** (`/users`) – example CRUD endpoints.  
- **Malaria Prediction API** (`/predict`) – predicts malaria risk using a pre-trained model.  
- **Nigeria Map API** (`/map/nigeria`) – serves a JSON file (`ng.json`) for visualization.

---

## **Project Structure**


backend_project/
│
├── app/
│ ├── init.py # FastAPI app instance
│ ├── main.py # Entrypoint
│ ├── routes/
│ │ ├── user_routes.py
│ │ └── map_routes.py
│ ├── utils/
│ │ ├── load_model.py
│ │ └── load_json.py
│ └── models/
│ └── malaria_model.pkl
├── data/
│ └── ng.json
├── requirements.txt
├── .gitignore
└── README.md


---

## **Installation**

1. Clone the repo:

```bash
git clone https://github.com/your-username/malaria-backend.git
cd malaria-backend
Create a virtual environment:
python -m venv venv
# Activate:
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Run Locally
uvicorn app.main:app --reload
Open browser: http://127.0.0.1:8000/docs
Swagger UI will display all endpoints.
Endpoints
Users
GET /users – Get all users
GET /users/{id} – Get single user
POST /users – Add new user
DELETE /users/{id} – Delete user
Prediction
POST /predict – Make malaria prediction
JSON body example:
{
  "feature1": 10,
  "feature2": 5,
  "feature3": 7
}
Nigeria Map
GET /map/nigeria – Get ng.json data for visualization
Environment Variables

Optional .env:

SECRET_KEY=your_secret_key
MODEL_PATH=app/models/malaria_model.pkl
Set these on Render dashboard when deploying.
Deployment
Backend: Render (free tier works fine)
Build Command: pip install -r requirements.txt
Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
Frontend: GitHub Pages
Fetch backend endpoints via the Render URL.
Notes
The backend is production-ready for a prototype or small-scale app.
CORS middleware is configured to allow requests from your frontend.
Raw datasets used to train malaria_model.pkl are not included, only the pre-trained model.