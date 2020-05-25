from azure.servicebus import QueueClient, Message

sbconnstring = "<>"

sbqueuename = "kedaqueue"

# Create the QueueClient
queue_client = QueueClient.from_connection_string(sbconnstring, sbqueuename)

# Receive the message from the queue
with queue_client.get_receiver() as queue_receiver:
    messages = queue_receiver.fetch_next(timeout=3)
    for message in messages:
        print(message)
        message.complete()

while True:
    aa = 999
