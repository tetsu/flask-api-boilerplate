FROM python:3.7.1-alpine

ARG project_dir=/api/

ADD . $project_dir

WORKDIR $project_dir
RUN apk update
RUN apk add zsh vim tmux git tig
RUN pip install -r ./api/requirements.txt

CMD python ./api/index.py
