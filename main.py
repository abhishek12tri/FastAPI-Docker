import uvicorn
import os
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    env_name = os.environ.get("ENV_NAME")
    if "localhost" == env_name:
        print("SERVER START")
        uvicorn.run("app:app", host="0.0.0.0", port=8002, reload=True)
    else:
        print("please mention running environment [localhost, prod, dev].")