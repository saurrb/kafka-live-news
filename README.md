# kafka-live-news
A Python project that demonstrates how to consume live news data from an API, process it using Kafka, and display it on a Flask web app. Includes instructions on setting up Kafka, creating topics, and installing required packages.


## Setup
### Kafka Setup
- Download Kafka from the [official website](https://kafka.apache.org/downloads) (Chooose Binary Download).
- Extract the downloaded file and navigate to the extracted directory.
- Start the Kafka server: 
  - `bin/kafka-server-start.sh config/server.properties`
- Start the ZooKeeper server: 
  - `bin/zookeeper-server-start.sh config/zookeeper.properties`
- To stop the ZooKeeper server: 
  - `bin/zookeeper-server-stop.sh`
- To stop the Kafka server: 
  - `bin/kafka-server-stop.sh`
- Create a new Kafka topic:  
  - `bin/kafka-topics.sh --create --topic Newtopic --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092`
- To list all topics: 
  - `bin/kafka-topics.sh --list --bootstrap-server localhost:9092`
- To delete a Kafka topic: 
  - `bin/kafka-topics.sh --delete --topic Newtopic --bootstrap-server localhost:9092`

### Installing Required Packages
- To upgrade pip in your local environment: 
  - `pip install --upgrade pip`
- To install kafka-python: 
  - `pip install kafka-python`
- To install requests: 
  - `pip install requests`
- To install Flask pandas: 
  - `pip install Flask pandas`

### Running the Application
- Open IntelliJ IDEA and create a new project, selecting Python as the language. Use a virtual environment if desired.
- Open a terminal and navigate to the location where you downloaded and extracted Kafka.
- Start the ZooKeeper server:

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

Start the Kafka server:
```bash
bin/kafka-server-start.sh config/server.properties
```
- Install Packages

- Go to the News API website at https://newsapi.org/docs/get-started and generate an API key.
- Open kafkaProducer.py and replace the placeholder API key with your own.

- Run the Kafka producer.
- Run the Kafka consumer.
- Run the Flask web app.

- Open a web browser and go to http://127.0.0.1:5000/ to view the live news feed.