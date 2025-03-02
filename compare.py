import pandas as pd

def compare_isps():
    isp_data = pd.DataFrame({
        "ISP": ["ISP A", "ISP B", "ISP C"],
        "Speed (Mbps)": [100, 75, 50],
        "Reliability (%)": [95, 90, 85],
        "Cost ($/month)": [50, 40, 30]
    })
    return isp_data

# Test
if __name__ == "__main__":
    print(compare_isps())
