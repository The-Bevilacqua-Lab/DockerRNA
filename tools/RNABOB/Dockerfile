##########################################################################################
# Dockerfile for containerized RNArobo
#########################################################################################

# Base image
FROM nciccbr/ccbr_ubuntu_base_20.04:v2.1

# Download and install RNArobo
RUN wget http://eddylab.org/software/rnabob/rnabob.tar.gz && \
    tar -xzf rnabob.tar.gz && \
    cd rnabob-2.2.1 && \
    make

# Add RNArobo to PATH
ENV PATH="/data2/rnabob-2.2.1:${PATH}"