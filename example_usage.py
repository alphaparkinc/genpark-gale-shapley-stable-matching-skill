import sys
from client import GaleShapleyMatcher

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

def run():
    print(">>> Demonstrating Gale-Shapley Stable Matching...")
    men = {
        'Alice': ['Hospital_A', 'Hospital_B'],
        'Bob':   ['Hospital_A', 'Hospital_B']
    }
    hospitals = {
        'Hospital_A': ['Bob', 'Alice'],
        'Hospital_B': ['Alice', 'Bob']
    }

    matcher = GaleShapleyMatcher(men, hospitals)
    res = matcher.match()
    print(f"Stable Matching Result: {res}")
    assert res['Bob'] == 'Hospital_A'
    assert res['Alice'] == 'Hospital_B'
    print("[PASS] Gale-Shapley Stable Matching verified.")

if __name__ == "__main__":
    run()
