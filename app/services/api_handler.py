import requests
import time

class YachtsAPIHandler:
    def __init__(self):
        self.base_url = ""
        self.holding_time = 86400  # 24 hours in seconds
        self.agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        self.last_fetched = None

    def setup(self, base_url, holding_time=None, agent=None):
        self.base_url = base_url
        if holding_time:
            self.holding_time = holding_time
        if agent:
            self.agent = agent

    def write_fetch(self, data):
        print(f"Writing fetched data to cache. At {time.time()}")
        formated_data = ""
        for item in data:
            new_item = f"||{item}^\n"
            formated_data += new_item
        self.last_fetched = {
            "timestamp": time.time(),
            "data": formated_data
        }
    def get_last_fetched(self):
        print("Retrieving last fetched data from cache.")
        return self.last_fetched

    def get_content(self):
        if self.last_fetched and time.time() - self.last_fetched["timestamp"] < self.holding_time:
            print("Returning cached data.")
            return {"status": "success", "content": self.last_fetched["data"]}
        headers = {
            "User-Agent": self.agent
        }

        try:
            response = requests.get(self.base_url, headers=headers)
            if response.status_code != 200:
                return {"status": "error", "code": response.status_code, "message": response.text}
            if response.headers.get('Content-Type') != 'application/json':
                return {"status": "error", "code": response.status_code, "message": "Website did not return JSON content."}
            self.write_fetch(response.json())
            new_data = self.get_last_fetched()
            return {"status": "success", "content": new_data["data"]}
        except requests.RequestException as e:
            print(f"Error fetching content: {e}")
            return {"status": "error", "code": 500, "message": str(e)}

yacht_handler = YachtsAPIHandler()