from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd
import kagglehub

app = FastAPI()

path = kagglehub.dataset_download("migalpha/spanish-names")

female_df = pd.read_csv(f"{path}/female_names.csv")
male_df = pd.read_csv(f"{path}/male_names.csv")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def get_home():
    with open("templates/index.html", "r") as file:
        return file.read()

def format_name(name):
    return name.title()

@app.get("/proper-names")
def get_random_proper_names(gender: str = "all", limit: int = 10):
    if gender == "male":
        proper_names = male_df["name"].drop_duplicates().sample(n=limit).tolist()
    elif gender == "female":
        proper_names = female_df["name"].drop_duplicates().sample(n=limit).tolist()
    else:
        all_names = pd.concat([male_df["name"], female_df["name"]]).drop_duplicates().sample(n=limit).tolist()
        proper_names = all_names

    formatted_names = [format_name(name) for name in proper_names]

    return {"proper_names": formatted_names}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
