##########################################################################################
# Dockerfile for R2EasyR
#
#########################################################################################

# Load the base image
FROM nciccbr/ccbr_ubuntu_base_20.04:v2.1

 # Copy the conda env
COPY venv.yaml /conda-envs/0da11548494986e0fd1069c89ffda2be/environment.yaml

# Set the path to conda 
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

# Update stuff with apt-get 
RUN apt-get update
RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

# Install Python3
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download Conda
RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 
RUN conda --version

# Initialize conda in bash:
RUN conda init bash

RUN git clone https://github.com/jaswindersingh2/SPOT-RNA.git
RUN cd SPOT-RNA
RUN wget 'https://www.dropbox.com/s/dsrcf460nbjqpxa/SPOT-RNA-models.tar.gz' || wget -O SPOT-RNA-models.tar.gz 'https://app.nihaocloud.com/f/fbf3315a91d542c0bdc2/?dl=1'
RUN tar -xvzf SPOT-RNA-models.tar.gz && rm SPOT-RNA-models.tar.gz

# Create the environment:
RUN conda env create --prefix /conda-envs/0da11548494986e0fd1069c89ffda2be --file /conda-envs/0da11548494986e0fd1069c89ffda2be/environment.yaml && \
    conda clean --all -y

# Initialize conda in bash:
RUN conda init bash

# Activate the environment:
RUN echo "conda activate /conda-envs/0da11548494986e0fd1069c89ffda2be" >> ~/.bashrc

# Set the default environment:
ENV PATH="/conda-envs/0da11548494986e0fd1069c89ffda2be/bin:${PATH}"
