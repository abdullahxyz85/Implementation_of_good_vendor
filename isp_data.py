import requests

def get_isp_data(latitude, longitude):
    url = f"https://broadbandmap.fcc.gov/api/isp?lat={latitude}&lng={longitude}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch ISP data"}

# Test
if __name__ == "__main__":
    print(get_isp_data(40.7128, -74.0060))  # Example for New York
