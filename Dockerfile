FROM python:3.12

ADD requirements.txt /
# установка Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# установка chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


# установка Java OpenJDK 17
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    openjdk-17-jdk

# установка переменных окружения для JAVA_HOME
ENV JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
ENV PATH=$PATH:$JAVA_HOME/bin

# установка переменной окружения для дисплея
ENV DISPLAY=:99

# обновление pip и установка зависимостей Python
RUN pip install --upgrade pip
RUN pip install --upgrade webdriver-manager
RUN pip install --upgrade selenium
RUN pip show webdriver-manager
RUN pip install -r /requirements.txt
