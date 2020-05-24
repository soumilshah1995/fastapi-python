FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY . /app/app
RUN pip install fastapi uvicorn
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]
