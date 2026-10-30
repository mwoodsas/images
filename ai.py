import os
import subprocess
import time
import textwrap

_model_name = "llama3.2:1b"

def start():
    """Installs dependencies, starts the server, and pulls the default model."""
    print("⏳ Initializing AI environment (this takes about 30 seconds)...")
    
    # 1. Install zstd and Ollama CLI
    os.system("sudo apt-get update -y > /dev/null 2>&1 && sudo apt-get install -y zstd > /dev/null 2>&1")
    os.system("curl -fsSL https://ollama.com/install.sh | sh > /dev/null 2>&1")
    
    # 2. Install python SDK
    os.system("pip install -q ollama")
    
    # 3. Start background process
    subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)
    
    # 4. Pull default model
    os.system(f"ollama pull {_model_name} > /dev/null 2>&1")
    
    print("✅ AI Engine Ready!")

def prompt(text, wrap_width=80):
    """Sends a user prompt to the local LLM and prints formatted wrapped text."""
    import ollama
    
    response = ollama.chat(
        model=_model_name,
        messages=[{"role": "user", "content": text}]
    )
    
    output = response['message']['content']
    return textwrap.fill(output, width=wrap_width)
