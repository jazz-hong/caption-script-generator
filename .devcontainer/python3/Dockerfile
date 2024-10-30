ARG IMAGE_TAG

FROM python:$IMAGE_TAG

ARG USERNAME
ARG USER_UID
ARG USER_GID=$USER_UID

RUN apt update && apt install -y --no-install-recommends \
    nodejs \
    git \
    wget \
    && apt clean

# RUN pip install "pip==22.3.1"

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME


ENV PATH=$PATH:/home/$USERNAME/.local/bin
RUN echo $PATH

USER $USERNAME
