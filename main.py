from models.KafkaProducer import KafkaSyncProducer, KafkaAsyncProducer
from asyncio import run

async def main():
    conf = {
        'bootstrap.servers': 'localhost:9092',
    }

    kafka_lib_sync = KafkaSyncProducer(**conf)
    kafka_lib_sync.send_message_sync('test', 'NewSyncMessage', 'value')

    async with KafkaAsyncProducer(**conf) as kafka_lib_async:
        await kafka_lib_async.send_message_async('test', 'NewAsyncMessage', 'value')
    #
    with KafkaSyncProducer(**conf) as kafka_producer:
        kafka_producer.send_message_sync('test', 'NewContextManagerSyncMessage', 'value')

if __name__=='__main__':
    run(main())