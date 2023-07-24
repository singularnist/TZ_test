FROM python:3.7.8

RUN pip install cryptography
RUN pip uninstall -y kombu
RUN pip install --upgrade importlib_metadata
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту файлів проекту
COPY . /app/

# Запускаємо додаток Flask
CMD python main.py