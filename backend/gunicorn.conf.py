# Bind to the specified address and port
bind = "0.0.0.0:8000"

# Number of worker processes
workers = 4

# Worker class to use for handling requests
worker_class = "uvicorn.workers.UvicornWorker"