# OpenChat Wrapper

Welcome to the OpenChat Wrapper, a Python Flask application designed to host an OpenAI reverse proxy for communicating with OpenChat's Aura LLM. This wrapper enables you to seamlessly interact with OpenChat's powerful language model through a simple API.

## Features

- **Reverse Proxy:** Acts as a reverse proxy for OpenChat's Aura LLM, allowing you to make chat requests via a local server.
- **Flask Server:** Utilizes Flask, a lightweight web framework for Python, to provide a robust and easy-to-use API.
- **Cross-Origin Requests:** Supports cross-origin requests through Flask CORS to enable interactions from various sources.

## Getting Started

Follow the steps below to set up and run the OpenChat Wrapper on your local machine.

### Prerequisites

- Python 3.x (3.10 tested only)
- Flask (`pip install flask`)
- Flask CORS (`pip install flask_cors`)
- Requests (`pip install requests`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Recentaly/OpenChat-Wrapper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd OpenChat-Wrapper
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Flask application:

   ```bash
   python main.py
   ```

   The server will start running on `http://0.0.0.0:5000/`.

2. Make requests to the API using the provided endpoints.

## API Endpoints

### `/chat/completions` (POST)

This endpoint handles chat generation requests. You can send a POST request with the necessary data to receive responses from the OpenChat model.

**Request Body:**

```json
{
  "messages": [
    {"role": "user", "content": "Hello, how are you?"}
  ],
  "temperature": 0.8,
  "stream": false
}
```

### `/models` (GET)

This endpoint returns a list of available models.

### `/` (GET)

The root endpoint returns a simple "Hello World!" message. This is to ensure the link works.

## Models

- **OpenChat Aura**
  - ID: `openchat_v3.2_mistral`
  - Max Length: 256 (default, modifiable)
  - Token Limit: 8192

Feel free to contribute to this project by submitting issues or pull requests!

Happy chatting with OpenChat! 🚀
