# My Python App

This is a simple Python application using FastAPI and PostgreSQL.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo/backend
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Set up environment variables**:
    Create a `.env` file in the [backend](http://_vscodecontentref_/2) directory with the following content:
    ```plaintext
    DATABASE_URI=postgresql://helberth:helberthCO9189@db:5432/taskManagerDB
    SECRET_KEY=helb_key_task_manager
    ```

2. **Run the application using Docker**:
    ```bash
    docker-compose up --build
    ```

3. **Access the application**:
    Open your browser and go to `http://localhost:8000`.

## API Endpoints

- **GET /**: Returns a simple greeting message.
- **POST /register**: Registers a new user.
    - Request body:
        ```json
        {
            "name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "password": "password123"
        }
        ```
- **POST /login**: Authenticates a user and returns an access token.
    - Request body:
        ```json
        {
            "username": "johndoe",
            "password": "password123"
        }
        ```

## Testing

1. **Run tests**:
    ```bash
    pytest
    ```

## License

This project is licensed under the MIT License.