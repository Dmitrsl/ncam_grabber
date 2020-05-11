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

ADD http://static.matrix-vision.com/mvIMPACT_Acquire/2.37.1/install_mvGenTL_Acquire.sh /home/webcamera
ADD http://static.matrix-vision.com/mvIMPACT_Acquire/2.37.1/mvGenTL_Acquire-x86_64_ABI2-2.37.1.tgz /home/webcamera

RUN chmod ugo+x install_mvGenTL_Acquire.sh
RUN ./install_mvGenTL_Acquire.sh

COPY requirements.txt /home/webcamera
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]