##########################################################################################
# Dockerfile for Scanfold
#
#########################################################################################

FROM nciccbr/ccbr_ubuntu_base_20.04:v2.1


COPY scanfold.yaml /conda-envs/0da11548494986e0fd1069c89ffda2be/environment.yaml


ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

# Install Python3
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download RNAstructure
RUN wget https://rna.urmc.rochester.edu/Releases/current/RNAstructureLinuxTextInterfaces64bit.tgz && \
    tar -xvzf RNAstructureLinuxTextInterfaces64bit.tgz && \
    rm RNAstructureLinuxTextInterfaces64bit.tgz

# Make RNAstructure python
RUN cd RNAstructure && \
    make python PYTHON=python3

# Export RNAstructure path
ENV PYTHONPATH=/data2/RNAstructure/exe

RUN apt-get clean && \
rm -rf /var/lib/apt/lists/*

# Download the ScanFold repo
RUN git clone https://github.com/moss-lab/ScanFold.git

# Export ScanFold path
ENV PATH=/data2/ScanFold:$PATH

# Add the path to the RNAstructure executables
ENV PATH=/data2/RNAstructure/exe:$PATH

# Add the path to the RNAstructure data tables
ENV DATAPATH=/data2/RNAstructure/data_tables

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 
RUN conda --version

# Create the environment:
RUN conda env create --prefix /conda-envs/0da11548494986e0fd1069c89ffda2be --file /conda-envs/0da11548494986e0fd1069c89ffda2be/environment.yaml && \
    conda clean --all -y
    
# Initialize conda in bash:
RUN conda init bash


# Activate the environment:
RUN echo "conda activate /conda-envs/0da11548494986e0fd1069c89ffda2be" >> ~/.bashrc

# Set the default environment:
ENV PATH="/conda-envs/0da11548494986e0fd1069c89ffda2be/bin:${PATH}"