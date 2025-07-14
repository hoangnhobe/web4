FROM python:3.11-slim
WORKDIR /app
COPY . .

# Thêm PYTHONPATH để tìm được app/
ENV PYTHONPATH="${PYTHONPATH}:/app"

RUN pip install -r requirements.txt
CMD ["python", "app/main.py"]