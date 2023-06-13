##########################################################################################
# Dockerfile for containerized ShapeMapper2
#########################################################################################

# Base image
FROM nciccbr/ccbr_ubuntu_base_20.04:v2.1

# Download ShapeMapper2
RUN wget https://github.com/Weeks-UNC/shapemapper2/releases/download/2.1.5/shapemapper-2.1.5.tar.gz

# Install ShapeMapper2
RUN tar -xzf shapemapper-2.1.5.tar.gz && \
    cd shapemapper-2.1.5

# Add ShapeMapper2 to PATH
ENV PATH="/data2/shapemapper-2.1.5:${PATH}"
