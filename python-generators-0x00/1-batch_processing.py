import csv
import sys

def get_all_users():
    with open('user_data.csv', newline='') as f:
        return list(csv.DictReader(f))

def stream_users_in_batches(batch_size):
    users = get_all_users()
    for i in range(0, len(users), batch_size):
        batch = users[i:i + batch_size]
        yield [
            {**user, 'age': int(user['age'])}
            for user in batch
        ]

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)