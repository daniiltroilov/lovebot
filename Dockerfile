FROM python:3.11-slim

# ������������� ������� ����������
WORKDIR /app

# �������� ����������� ������� �������� ��� ����������� pip install
COPY requirements.txt .

# ������������� �����������
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# �������� ��������� ����� ����
COPY . .

# ������� �� ���������
CMD ["python", "bot.py"]