curl http://127.0.0.1:8000/books/ | jq

curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:8000/book/  -d '{"id": 0, "title": "book0", "author": "author0", "publisher": "publisher0"}' | jq && \
curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:8000/book/  -d '{"id": "1", "title": "book1", "author": "author1", "publisher": "publisher1"}' | jq  && \
curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:8000/book/  -d '{"id": "2", "title": "book2", "author": "author2", "publisher": "publisher2"}' | jq && \
curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:8000/book/  -d '{"id": "3", "title": "book3", "author": "author3", "publisher": "publisher3"}' | jq

curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:8000/book/ -d '{"id": 0, "title": "string", "author": "string", "publisher": "string"}'

curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:8000/book/2  -d '{"id": "2", "title": "book22", "author": "author22", "publisher": "publisher22"}' | jq

curl -X DELETE http://127.0.0.1:8000/book/3 | jq


CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publisher VARCHAR(255) NOT NULL
);
