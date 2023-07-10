from fastapi import FastAPI
import requests,redis



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


task=redis.Redis(host="localhost",port=6379,db=0)

	
@app.get("/animal")
def get_animal_details(animal_name):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{animal_name}"
    # cache=task.get(animal_name)
    cache=task.hgetall(animal_name)
    if not cache:
        print("not include")
        response = requests.get(url)
        data = response.json()
        summary = data.get('extract')
        data={"summery":summary,"search":animal_name}
        task.hmset(animal_name,data)
        # task.set(animal_name,summary)
        return summary
    else:
        print("included----------")
        return  cache
    
 