import pandas as pd

def compare_isps():
    """Returns a detailed and comprehensive comparison of ISPs with additional attributes."""
    isp_data = pd.DataFrame({
        "ISP": ["ISP A", "ISP B", "ISP C", "ISP D", "ISP E", "ISP F", "ISP G", "ISP H", "ISP I", "ISP J"],
        "Speed (Mbps)": [100, 75, 50, 200, 150, 300, 500, 1000, 250, 400],
        "Upload Speed (Mbps)": [10, 5, 5, 20, 15, 30, 50, 100, 25, 40],
        "Reliability (%)": [95, 90, 85, 98, 92, 97, 99, 96, 94, 93],
        "Cost ($/month)": [50, 40, 30, 70, 60, 90, 120, 150, 80, 110],
        "Coverage Area": ["Urban", "Urban/Suburban", "Rural", "Urban", "Suburban", "Urban", "Urban/Suburban", "Urban", "Suburban", "Rural"],
        "Customer Support Rating": [4.5, 4.0, 3.8, 4.7, 4.2, 4.8, 4.9, 4.6, 4.3, 4.4],
        "Contract Length (months)": [12, 24, "No Contract", 12, 24, 12, 24, "No Contract", 12, 24],
        "Data Caps": ["None", "1 TB", "500 GB", "None", "2 TB", "None", "None", "None", "1 TB", "None"],
        "Installation Fees": ["$0", "$50", "$0", "$0", "$100", "$0", "$0", "$0", "$0", "$50"],
        "Special Features": [
            "Free installation, No data caps",
            "Free modem, Unlimited data",
            "Low-cost plans, No contract",
            "Gigabit speeds, Free router",
            "Family plans, Free streaming services",
            "Fiber-optic network, No data caps",
            "24/7 priority support, Free installation",
            "Business-grade reliability, Free static IP",
            "Free security suite, No data caps",
            "Free VoIP service, No contract"
        ],
        "Technology": ["Cable", "DSL", "Satellite", "Fiber", "Cable", "Fiber", "Fiber", "Fiber", "Cable", "Fiber"],
        "Latency (ms)": [20, 30, 600, 10, 25, 8, 5, 2, 15, 7],
        "Peak Hours Performance": ["Stable", "Moderate", "Unstable", "Excellent", "Good", "Excellent", "Excellent", "Excellent", "Good", "Excellent"],
        "Additional Fees": ["None", "$10/mo modem rental", "None", "None", "$5/mo router rental", "None", "None", "None", "$10/mo security suite", "None"],
        "Bundle Options": [
            "Internet + TV",
            "Internet only",
            "Internet + Phone",
            "Internet + TV + Phone",
            "Internet + Streaming",
            "Internet only",
            "Internet + TV + Streaming",
            "Internet + Business Services",
            "Internet + Security",
            "Internet + VoIP"
        ],
        "Promotional Offers": [
            "First 3 months at $30/mo",
            "Free installation for 1 year",
            "No contract, no fees",
            "Free Netflix for 6 months",
            "Free router for 2 years",
            "First 6 months at $70/mo",
            "Free HBO Max for 1 year",
            "Free static IP for businesses",
            "Free antivirus for 1 year",
            "Free VoIP service for 6 months"
        ],
        "IPv6 Support": ["Yes", "No", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes"],
        "Parental Controls": ["Yes", "No", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes"],
        "WiFi Equipment": ["Included", "Extra $10/mo", "Not included", "Included", "Included", "Included", "Included", "Included", "Extra $5/mo", "Included"]
    })
    return isp_data

# Test
if __name__ == "__main__":
    isp_comparison = compare_isps()
    print(isp_comparison)