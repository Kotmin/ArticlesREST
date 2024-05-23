# ArticlesREST
## API for managing articles and blog posts.

Demo set up to work with in memory database



[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/Kotmin/ArticlesREST/article-management-api)
[![Build Status](https://img.shields.io/github/workflow/status/Kotmin/ArticlesREST/article-management-api/CI)](https://github.com/Kotmin/ArticlesREST/article-management-api/actions)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Kotmin/ArticlesREST/article-management-api/blob/main/LICENSE)

---



## Table of Contents

- [Description](#description)
- [Features](#features)
- [Quickstart](#quickstart)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)


## Description

ArticlesREST API is a FastAPI-based service for managing articles with details like name, tags, dates, category, and more. This demonstration version operates on an in-memory database, making it easy to test and experiment with the API.

## Features

- CRUD operations for Articles
- Auto-generated documentation with OpenAPI and Swagger UI
- In-memory database for demonstration purposes

## Quickstart 

### Local Setup

To run the application locally, follow these steps:

#### One click run (no venv)

```bash
pip install -r requirements.txt;\
uvicorn main:app --reload

```
#### Proper way

1. Clone the repository:
    ```bash
    git clone git@github.com:Kotmin/ArticlesREST.git
    cd ArticlesREST
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

5. Access the API documentation:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - OpenAPI YAML: [http://127.0.0.1:8000/openapi.yaml](http://127.0.0.1:8000/openapi.yaml)
    - OpenAPI JSON: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)



### Docker Setup

To run the application using Docker, follow these steps:

1. Clone the repository:
    ```bash
    git clone git@github.com:Kotmin/ArticlesREST.git
    cd ArticlesREST
    ```

2. Build the Docker image:
    ```bash
    docker build -t ArticlesREST .
    ```

3. Run the Docker container:
    ```bash
    docker run -d -p 8000:8000 ArticlesREST
    ```

4. Access the API documentation:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - OpenAPI YAML: [http://127.0.0.1:8000/openapi.yaml](http://127.0.0.1:8000/openapi.yaml)
    - OpenAPI JSON: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)



## API Documentation

The API documentation is auto-generated and can be accessed via Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). The OpenAPI specification is also available in YAML format at [http://127.0.0.1:8000/openapi.yaml](http://127.0.0.1:8000/openapi.yaml). You can also access JSON fortmat at [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json).

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements, bug fixes, or documentation improvements.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.