#MySQL : localhost:5012
  mysql:
    image: mysql:8.0
    container_name: MySQLDB
    restart: always
    cap_add:
      - SYS_NICE
    environment:
      - MYSQL_USER=user
      - MYSQL_PASSWORD=dockerpass
      - MYSQL_ROOT_PASSWORD=dockerpass
    volumes:
      - mysql-data:/var/lib/mysql
    ports:
      - 5012:3306
volumes:
  mysql-data:

# mongo.yaml

version: "3.7"
services:
#Mongo : localhost:5015
mongo:
image: mongo:4.4.2
container_name: MongoDB
restart: always
environment:
- MONGO_INITDB_DATABASE=chats
ports:
- 5015:27017
volumes:
      - mongodb-data:/data/db
#Mongo client UI : http://localhost:5016
  mongo_client:
    image: mongoclient/mongoclient:4.0.1
    container_name: Nosqlclient
    restart: always
    depends_on:
      - mongo
    ports:
      - 5016:3000
volumes:
  mongodb-data:
