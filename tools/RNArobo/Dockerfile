##########################################################################################
# Dockerfile for containerized RNArobo
#########################################################################################

# Base image
FROM nciccbr/ccbr_ubuntu_base_20.04:v2.1

# Download and install RNArobo
RUN wget https://github.com/rampasek/RNArobo/archive/refs/tags/v2.1.0.tar.gz && \
    tar -xzf v2.1.0.tar.gz && \
    cd RNArobo-2.1.0 && \
    make

# Add RNArobo to PATH
ENV PATH="/data2/RNArobo-2.1.0:${PATH}"
