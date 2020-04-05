FROM python:3.7

RUN apt-get update && apt-get install -y gcc ssh openssh-server gettext postgresql-client libpq-dev \
    libjpeg-dev libopenjp2-7-dev wget zsh

RUN mkdir /app/

COPY pip-requirements.txt /tmp/pip-requirements.txt
RUN pip install -r /tmp/pip-requirements.txt

RUN mkdir /var/run/sshd

RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

RUN echo "cd /app/weather-app" >> /root/.zshrc
