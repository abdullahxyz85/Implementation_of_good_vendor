def get_accessories():
    """Returns a detailed list of wireless accessories with additional information."""
    accessories = {
        "Router A": {
            "price": "$50",
            "brand": "NetGear",
            "description": "High-speed dual-band router with advanced security features.",
            "rating": 4.5,
            "availability": "In Stock",
            "specifications": {
                "WiFi Standard": "802.11ac",
                "Bands": "Dual-band (2.4GHz and 5GHz)",
                "Speed": "Up to 1200 Mbps",
                "Ports": "4 x Gigabit Ethernet, 1 x USB 3.0",
                "Coverage": "Up to 1500 sq. ft."
            },
            "features": [
                "Advanced QoS for optimized streaming",
                "Parental controls",
                "MU-MIMO technology",
                "Easy setup with the Nighthawk app"
            ],
            "warranty": "1-year limited warranty",
            "customer_reviews": [
                {"user": "JohnDoe123", "rating": 5, "comment": "Great router for gaming and streaming!"},
                {"user": "JaneSmith456", "rating": 4, "comment": "Easy to set up, but range could be better."}
            ],
            "image_url": "https://example.com/router-a.jpg"
        },
        "WiFi Adapter B": {
            "price": "$20",
            "brand": "TP-Link",
            "description": "USB WiFi adapter with 600Mbps speed and easy setup.",
            "rating": 4.2,
            "availability": "In Stock",
            "specifications": {
                "WiFi Standard": "802.11n",
                "Bands": "2.4GHz",
                "Speed": "Up to 600 Mbps",
                "Interface": "USB 2.0",
                "Antenna": "Internal antenna"
            },
            "features": [
                "Plug-and-play setup",
                "Supports WEP/WPA/WPA2 encryption",
                "Compact and portable design"
            ],
            "warranty": "2-year limited warranty",
            "customer_reviews": [
                {"user": "TechGuru789", "rating": 4.5, "comment": "Works great for my old laptop!"},
                {"user": "AnonymousUser", "rating": 3.5, "comment": "Good for the price, but speed is average."}
            ],
            "image_url": "https://example.com/wifi-adapter-b.jpg"
        },
        "Mesh System C": {
            "price": "$100",
            "brand": "Google Nest",
            "description": "Whole-home mesh WiFi system with seamless coverage.",
            "rating": 4.7,
            "availability": "Out of Stock",
            "specifications": {
                "WiFi Standard": "802.11ac",
                "Bands": "Dual-band (2.4GHz and 5GHz)",
                "Speed": "Up to 2200 Mbps",
                "Coverage": "Up to 4400 sq. ft.",
                "Nodes": "3-pack"
            },
            "features": [
                "Seamless roaming with a single network name",
                "Built-in Google Assistant",
                "Easy setup with the Google Home app",
                "Automatic updates"
            ],
            "warranty": "1-year limited warranty",
            "customer_reviews": [
                {"user": "HomeOwner123", "rating": 5, "comment": "Perfect for my large house!"},
                {"user": "TechEnthusiast", "rating": 4.8, "comment": "Great performance, but a bit pricey."}
            ],
            "image_url": "https://example.com/mesh-system-c.jpg"
        },
        "Range Extender D": {
            "price": "$35",
            "brand": "Linksys",
            "description": "WiFi range extender with dual-band support.",
            "rating": 4.0,
            "availability": "In Stock",
            "specifications": {
                "WiFi Standard": "802.11ac",
                "Bands": "Dual-band (2.4GHz and 5GHz)",
                "Speed": "Up to 1200 Mbps",
                "Coverage": "Up to 10,000 sq. ft.",
                "Ports": "1 x Gigabit Ethernet"
            },
            "features": [
                "Cross-band technology",
                "Spot Finder technology for optimal placement",
                "Easy setup with the Linksys app"
            ],
            "warranty": "1-year limited warranty",
            "customer_reviews": [
                {"user": "User123", "rating": 4.2, "comment": "Improved my WiFi coverage significantly."},
                {"user": "Anonymous", "rating": 3.8, "comment": "Works well, but setup was a bit tricky."}
            ],
            "image_url": "https://example.com/range-extender-d.jpg"
        },
        "Powerline Adapter E": {
            "price": "$60",
            "brand": "D-Link",
            "description": "Powerline adapter with built-in WiFi and Gigabit port.",
            "rating": 4.3,
            "availability": "In Stock",
            "specifications": {
                "WiFi Standard": "802.11ac",
                "Bands": "Dual-band (2.4GHz and 5GHz)",
                "Speed": "Up to 1200 Mbps",
                "Ports": "1 x Gigabit Ethernet",
                "Encryption": "128-bit AES"
            },
            "features": [
                "Built-in WiFi access point",
                "Plug-and-play setup",
                "Compact design"
            ],
            "warranty": "2-year limited warranty",
            "customer_reviews": [
                {"user": "TechLover", "rating": 4.5, "comment": "Great for extending WiFi to my garage."},
                {"user": "AnonymousUser", "rating": 4.0, "comment": "Works well, but speed drops occasionally."}
            ],
            "image_url": "https://example.com/powerline-adapter-e.jpg"
        }
    }
    return accessories

# Test
if __name__ == "__main__":
    accessories = get_accessories()
    for item, details in accessories.items():
        print(f"{item}:")
        for key, value in details.items():
            if key == "customer_reviews":
                print(f"  {key}:")
                for review in value:
                    print(f"    - User: {review['user']}, Rating: {review['rating']}, Comment: {review['comment']}")
            elif key == "specifications" or key == "features":
                print(f"  {key}:")
                for subkey, subvalue in value.items() if isinstance(value, dict) else enumerate(value, 1):
                    print(f"    - {subkey}: {subvalue}")
            else:
                print(f"  {key}: {value}")
        print()