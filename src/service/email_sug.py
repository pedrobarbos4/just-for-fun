from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/hint_email")
async def hint_email(name: str, lastname: str, birth: str):
    """

    """

    v=[1,2,3,4]
    v_weights = [10, 40, 40, 10]
    x=random.choices(v, v_weights, k=100)[0]
    sort_name_email = []
    list_birth_componentes = birth.split('-')

    year = list_birth_componentes[0]
    month = list_birth_componentes[1]
    day = list_birth_componentes[2]

    sort_name_email.append(name)
    sort_name_email.append(lastname)

    sort_name_email.append(year)
    sort_name_email.append(month)
    sort_name_email.append(day)

    weights = [50, 20, 10, 10, 10]

    samples = random.choices(sort_name_email, weights, k=100)

    unique = set(samples)

    unique_list = list(unique)

    email = ''.join(list(unique_list[:x]))+"@"+"email.com"

    return {"hint_email": email}