FROM python:3.6.5


WORKDIR /usr/src/MarketPlace/back-end

COPY ./ ./

RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
RUN pipenv install
RUN pip install psycopg2-binary

CMD ["/bin/bash"]