FROM ubuntu:17.10

## 维护者信息
LABEL version="1.0"
ENV myName Mervyn.Zhang <zmy@foreverz.cn>

## 更改配置源
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get upgrade && apt-get update && apt-get install -y apt-utils

## 安装 必要软件
RUN apt-get install -y vim
RUN apt-get install -y bash-completion
RUN apt-get install -y curl
RUN apt-get install -y wget

## 安装 python 和 pip
RUN apt-get install -y python3.6
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN cd /usr/bin && ln -s python3.6m python
RUN python get-pip.py
RUN rm -rf get-pip.py

## pip 换源并更新
RUN mkdir ~/.pip
RUN echo "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" > ~/.pip/pip.conf 
RUN pip install -U pip

## 安装 pipenv 和 virtualenv
RUN pip install --user pipenv
RUN pip install virtualenv
# RUN pipenv --update

## 安装 yarn 和 npm
RUN apt-get install -y npm
# RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
# RUN echo 'deb https://dl.yarnpkg.com/debian/ stable main' > /etc/apt/sources.list.d/yarn.list
RUN apt-get update -y
# RUN apt-get install -y yarn

## 安装 node
# RUN yarn global add n
# RUN n latest