FROM  jjanzic/docker-python3-opencv
WORKDIR /home/webcamera
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    dialog apt-utils \
    apt-utils \
    build-essential \
    cmake \
    git \
    curl \
    ca-certificates \
    zlib1g-dev \
    libgtk2.0-0 \
    libglib2.0-dev \
    libsm6 \
    libxext6 \
    libxrender1 \
    libxrender-dev \
    libpng-dev &&\
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt /home/webcamera
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]