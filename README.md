

# Secure Fast API


Fast API blueprint that implements [Oauth bearer token](https://fastapi.tiangolo.com/tutorial/security/#oauth2) with [OAuth scopes](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/) on a "multiple files" application with API Routers.

Database is mocked as Python memory lists. 

### How to


```shell
poetry install --with dev
source .venv/bin/activate

# you should save it somewhere safe, eg in a .env
export JWT_SECRET_KEY=$(openssl rand -hex 32)
uvicorn src.main:app --reload
```

Visit [127.0.0.1:8000/docs](https://127.0.0.1:8000/docs)

### Use case example
1. **Bob** authenticates (user `bob`, password `secret`)
2. **Bob** cannot manipulate items since he is `admin`
3. **Bob** can create a new user `Mike` with type `manager`
4. **Bob** provides to **Mike** the generated password
5. **Mike** can connect and plays with his items
6. **Alice** can only review her items
7. **Bob** can list everyone's all items
