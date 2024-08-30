import os
import sys
import requests
from git import Repo

MULTION_API_KEY = os.environ.get('MULTION_API_KEY')
MULTION_API_URL = 'https://api.multion.ai/v1/web/browse'

def get_new_words():
    repo = Repo('.')
    diff = repo.git.diff('origin/main', name_only=True)
    if 'words-and-phrases.txt' not in diff:
        return []
    
    with open('words-and-phrases.txt', 'r') as f:
        current_words = set(f.read().splitlines())
    
    with open('words-and-phrases.txt', 'r') as f:
        new_words = set(f.read().splitlines()) - current_words
    
    return list(new_words)

def validate_word(word):
    payload = {
        "cmd": f"Evaluate if the phrase '{word}' is overused in AI-generated content.",
        "url": "https://www.google.com",
        "local": False
    }
    headers = {
        "X_MULTION_API_KEY": MULTION_API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.post(MULTION_API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        # Assuming the Multion API returns a clear indication of overuse
        return "overused" in result['message'].lower()
    else:
        print(f"Error validating word '{word}': {response.status_code}")
        return False

def main():
    new_words = get_new_words()
    rejected_words = []

    for word in new_words:
        if not validate_word(word):
            rejected_words.append(word)

    if rejected_words:
        print("The following words were rejected:")
        for word in rejected_words:
            print(f"- {word}")
        sys.exit(1)
    else:
        print("All new words passed validation.")
        sys.exit(0)

if __name__ == "__main__":
    main()