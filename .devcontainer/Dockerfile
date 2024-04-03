# Use the official Rust image as a parent image
FROM rust:1.56

# Update and install necessary tools
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    libssl-dev \
    cmake \
    curl \
    git \
 && rm -rf /var/lib/apt/lists/*

# Add a non-root user for VS Code
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Switch to the new user
USER $USERNAME

# Set the default working directory
WORKDIR /workspace

# [Optional] Install Rust nightly and additional components
# RUN rustup install nightly && rustup default nightly
# RUN rustup component add rustfmt clippy

# Set the default command for the container
CMD ["bash"]
