import configuration as conf
import json

from csv import DictReader


with open(conf.USERS_JSON, "r") as f:
    users = json.loads(f.read())

with open(conf.BOOKS_CSV, newline='') as f:
    reader = DictReader(f)
    # Create iterator from file with users
    iter_user = iter(users)

    for row in reader:
        try:
            current_user = next(iter_user)
        except StopIteration:
            # Recreate iterator if there are no more elements in users.json
            iter_user = iter(users)
            current_user = next(iter_user)
        if "books" not in current_user:
            current_user["books"] = []
        current_user["books"].append({"title": row["Title"],
                                      "author": row["Author"],
                                      "pages": int(row["Pages"]),
                                      "genre": row["Genre"]})


result_data = []
for user in users:
    result_data.append({
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": user["books"]
    })

with open(conf.RESULT_JSON, "w") as f:
    result_info = json.dumps(result_data, indent=4)
    f.write(result_info)
