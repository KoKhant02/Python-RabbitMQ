# Python RabbitMQ Example

This project demonstrates a basic producer-consumer pattern using RabbitMQ and Python. The producer sends messages to a queue, and the consumer receives and processes those messages.

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Pika (Python RabbitMQ client)
- RabbitMQ server running locally

### Setup

1. **Install RabbitMQ**
   Follow the instructions to install RabbitMQ on your local machine. Ensure the RabbitMQ server is running and accessible.

2. **Install Python Dependencies**
   You need the `pika` library to interact with RabbitMQ. Install it using `pip`:

   ```bash
   pip3 install pika
   ```

3. **Clone the Repository**

   If you haven't cloned the repository yet, do so with the following command:

   ```bash
   git clone https://github.com/KoKhant02/Python-RabbitMQ.git
   cd Python-RabbitMQ
   ```

### Running the Code

#### 1. **Run the Consumer First**

Start by running the consumer, which will listen to the RabbitMQ queue and process the messages sent by the producer.

```bash
cd consumer/
python3 consumer.py
```

The consumer will start and wait for messages from the queue.

#### 2. **Run the Producer**

In a separate terminal window, run the producer script, which will continuously prompt you to enter messages and send them to the RabbitMQ queue.

```bash
cd producer/
python3 producer.py
```

Each time you enter a message, the producer will send it to the RabbitMQ queue, and the consumer will receive and log it.


### Example Log Output

**Producer**:
```
Producer is running. Type your message and press Enter (Ctrl+C to stop):
Enter message: Hello, RabbitMQ!
Successfully Sent Message 'Hello, RabbitMQ!' to queue.
Enter message: Another message!
Successfully Sent Message 'Another message!' to queue.
```

**Consumer**:
```
 [*] Waiting for messages. To exit press Ctrl+C
 [x] Received 'Hello, RabbitMQ!'
 [x] Received 'Another message!'
```


**Stopping the Producer**

To stop the producer, press `Ctrl+C`. This will gracefully shut down the producer and close the connection to RabbitMQ.

---
