
## The Service

The service is a small Flask application with two endpoints:

| Endpoint  | Description                                              |
|-----------|----------------------------------------------------------|
| `/`       | Returns a JSON message, the app version, and the host name |
| `/health` | Returns `{"status": "ok"}` with a timestamp              |

## The CI/CD Pipeline

The pipeline is defined in `.github/workflows/ci-cd.yml` and runs on every push to `main` and on every pull request.

1. **Test:** Installs the dependencies and runs `pytest` against the service.
2. **Build and push image:** Builds the Docker image, tags it with the Git commit SHA, and pushes it to GitHub Container Registry (`ghcr.io`). Pull requests build the image but do not push it.
3. **Deploy container:** Runs only on pushes to `main`. It pulls the image, starts the container on port 8080, waits for `/health` to respond, and runs a smoke test against `/`. If the health check fails, the container logs are printed and the job fails.

The deploy step runs the container on the GitHub Actions runner. To deploy to a real server instead, replace the deploy job with an SSH step or a self-hosted runner on that machine.

## Running Locally

**Run the tests:**

```bash
pip install -r app/requirements.txt -r app/requirements-dev.txt
pytest -v app/
```

**Build and run the container:**

```bash
docker build -t devops-demo .
docker run -d -p 8080:8000 --name demo devops-demo
```

Then open `http://localhost:8080` (or `http://localhost:8080/health`) in a browser.

Stop the container with:

```bash
docker rm -f demo
```

## Pipeline Output

- Repository: https://github.com/Likhitha-5/devops-demo
- Successful pipeline run: https://github.com/Likhitha-5/devops-demo/actions/runs/41190408240
- Container image: `ghcr.io/likhitha-5/devops-demo:<commit-sha>`

## Technologies

Python 3.12, Flask, Gunicorn, pytest, Docker, GitHub Actions, GitHub Container Registry.
