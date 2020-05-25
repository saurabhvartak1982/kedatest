from azure.servicebus import QueueClient, Message

sbconnstring = "<>"

sbqueuename = "kedaqueue"

msgcnt = 3

# Create the QueueClient
queue_client = QueueClient.from_connection_string(sbconnstring, sbqueuename)

# Send a test message to the queue
for ctr in range(msgcnt):
    msg = Message(b'Keda Test Message '+ str(ctr))
    queue_client.send(msg)
