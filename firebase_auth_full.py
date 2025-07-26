import requests

API_KEY = "AIzaSyD4Atemhc2PD1G8nyLH3WPZKlhgRgH5Eeg"  # Your Firebase Web API key here

def firebase_sign_up(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    res = requests.post(url, json=payload)
    print("Sign Up response:", res.json())
    res.raise_for_status()
    data = res.json()
    return data["idToken"], data["localId"]

def firebase_sign_in(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    res = requests.post(url, json=payload)
    if res.status_code != 200:
        print("Sign In error response:", res.json())
    res.raise_for_status()
    data = res.json()
    return data["idToken"], data["localId"]

class QuantumDecision:
    def __init__(self):
        self.branches = []

    def add_branch(self, name, data):
        self.branches.append({"name": name, "data": data})

    def evaluate(self):
        print("Evaluating non-collapsing superposition:")
        for branch in self.branches:
            print(f"Branch '{branch['name']}' => {branch['data']}")

def upload_to_firebase(branches, uid, id_token):
    url = f"https://new-smartconnect-project-default-rtdb.firebaseio.com/decisions/{uid}.json?auth={id_token}"
    response = requests.post(url, json=branches)
    print(f"🔥 Firebase upload response: {response.status_code} | {response.text}")

if __name__ == "__main__":
    # Replace these with your desired Firebase Auth user credentials
    email = "your_actual_email@example.com"
    password = "your_actual_password"

    try:
        print("Trying to sign up user...")
        id_token, uid = firebase_sign_up(email, password)
        print(f"Sign-up successful. UID: {uid}")
    except requests.exceptions.HTTPError as e:
        print("User probably already exists, trying to sign in...")
        id_token, uid = firebase_sign_in(email, password)
        print(f"Sign-in successful. UID: {uid}")

    decision = QuantumDecision()
    decision.add_branch("approve_payment", {"status": "approved", "risk": "low"})
    decision.add_branch("review_payment", {"status": "pending", "risk": "medium"})
    decision.add_branch("block_payment", {"status": "blocked", "risk": "high"})

    decision.evaluate()

    upload_to_firebase(decision.branches, uid, id_token)
