import speedtest

def check_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1e6  # Convert to Mbps
    upload_speed = st.upload() / 1e6  # Convert to Mbps
    return round(download_speed, 2), round(upload_speed, 2)

# Test
if __name__ == "__main__":
    print(check_speed())
