FROM python:3-alpine

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن فایل‌ها
COPY . .
CMD ["python","manage.py","collectstatic"]
