# 🚀 PingWire – Real-Time Messaging Backend  

PingWire is a **real-time messaging backend** built with **FastAPI**, **MongoDB**, **WebSockets**, and **JWT authentication**.  
It provides a secure, scalable, and low-latency solution for instant communication.  

---

## ✨ Features  
- 🔐 **Secure Authentication** with JWT  
- ⚡ **Real-Time Messaging** using WebSockets  
- 📦 **Scalable Storage** with MongoDB  
- 🛠️ **API Testing Ready** (Postman Collections available)  
- 🐳 **Dockerized Deployment** for portability  

---

## 🏗️ Tech Stack  
- **Backend**: FastAPI (Python)  
- **Database**: MongoDB  
- **Authentication**: JWT  
- **Protocols**: WebSockets  
- **Tools**: Docker, Git, Postman  

---

## 📂 Project Structure  
PingWire/
│── app/ # Core backend code
│ ├── main.py # Entry point
│ ├── auth/ # JWT authentication
│ ├── messaging/ # WebSocket messaging
│── tests/ # Unit tests
│── requirements.txt # Python dependencies
│── Dockerfile # Containerization setup
│── README.md # Documentation

yaml
Copy code

---

## ⚙️ Installation & Usage  

### 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/PingWire-Messaging-Backend.git
cd PingWire-Messaging-Backend
2. Create Virtual Environment & Install Dependencies
bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\\Scripts\\activate    # Windows
pip install -r requirements.txt
3. Run the Server
bash
Copy code
uvicorn app.main:app --reload
4. Access the API Docs
Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🧪 Testing
bash
Copy code
pytest tests/
🐳 Run with Docker
bash
Copy code
docker build -t pingwire-backend .
docker run -p 8000:8000 pingwire-backend
🌐 API Endpoints
Method	Endpoint	Description
POST	/auth/login	User login with JWT
POST	/auth/signup	User registration
GET	/messages	Fetch chat history
WS	/ws/chat	Real-time chat socket

📸 Screenshots (Optional)
(Add API docs screenshot, Postman test, or terminal output here)

🏆 Achievements
Designed for low-latency real-time communication

Scalable architecture with MongoDB and WebSockets

Successfully tested using Postman & JMeter

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the MIT License.

👩‍💻 Author
Dimple Kundu

