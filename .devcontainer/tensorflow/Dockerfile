ARG IMAGE_TAG

FROM tensorflow/tensorflow:$IMAGE_TAG

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# pip needs to be upgraded to avoid issue with some package installation (e.g. dvc)
RUN pip install "pip==22.3.1"

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# This adds python binaries installed by pip to PATH
ENV PATH=$PATH:/home/$USERNAME/.local/bin
RUN echo $PATH

# install custom fonts for zsh
RUN mkdir /home/$USERNAME/.fonts
WORKDIR /home/$USERNAME/.fonts
RUN wget https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf \
         https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf \
         https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf \
         https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf \
    && fc-cache -f -v

# install zsh
WORKDIR /home/$USERNAME
RUN git clone https://github.com/robbyrussell/oh-my-zsh.git ./.oh-my-zsh \
    && git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ./.oh-my-zsh/custom/themes/powerlevel10k \
    && git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git ./.oh-my-zsh/custom/plugins/zsh-syntax-highlighting \
    && git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions ./.oh-my-zsh/custom/plugins/zsh-autosuggestions    

COPY shell/* ./
RUN chsh -s /bin/zsh $USERNAME

# force changing user
USER $USERNAME
