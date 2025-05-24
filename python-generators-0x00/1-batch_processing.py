import csv
import sys

def get_all_users():
    with open('user_data.csv', newline='') as f:
        return list(csv.DictReader(f))

def stream_users_in_batches(batch_size):
    users = get_all_users()
    for i in range(0, len(users), batch_size):
        for user in users[i:i + batch_size]:
            user['age'] = int(user['age'])
        yield users[i:i + batch_size]

def batch_processing(batch_size):
    user_batch = stream_users_in_batches(batch_size)

    while True:
        try:
            batch = next(user_batch)
            for user in batch:
                if user.get('age', 0) > 119:
                    print(user)
        except StopIteration:
            break
  

try:
    batch_processing(50)
except BrokenPipeError:
    sys.stderr.close()
