import os

# Attempt to import the real Hindsight client; if unavailable, provide a lightweight stub
try:
    from hindsight import HindsightClient
except Exception:
    class HindsightClient:
        """Fallback stub for development when the hindsight package isn't installed."""
        def __init__(self, *args, **kwargs):
            print("(stub) HindsightClient initialized")

        def add_memory(self, text: str, metadata: dict = None):
            # Simulate storing a memory by printing; keeps behavior visible during tests
            print(f"(stub) add_memory called. text={text!r}, metadata={metadata!r}")

def seed_hackathon_memories():
    print("🧠 Initializing Hindsight Vector Memory Store...")
    
    # Initialize the hindsight client 
    # (It will look for HINDSIGHT_API_KEY in your env)
    client = HindsightClient()
    
    # Let's seed past historical errors so our agents can find matches
    past_incidents = [
        {
            "error_signature": "test_payment_gateway_timeout FAILED SocketError: connection reset by peer",
            "resolution": "Known flaky test environment issue caused by payment gateway sandbox downtime. Safe to automatically trigger a pipeline retry."
        },
        {
            "error_signature": "Cannot install package_x because of a version conflict. package_x requires numpy<=1.21.5",
            "resolution": "Dependency conflict introduced by recent DevOps configuration patch. Fix by adjusting requirements.txt constraints or updating package_x."
        }
    ]
    
    for incident in past_incidents:
        # Saving the historical text logs into Vector memory blocks
        client.add_memory(
            text=incident["error_signature"],
            metadata={"solution": incident["resolution"]}
        )
        print(f"✅ Documented historical memory patch for: '{incident['error_signature'][:40]}...'")

if __name__ == "__main__":
    # If you have your Vectorize key set up, you can execute this file
    try:
        seed_hackathon_memories()
    except Exception as e:
        # Keep the error visible but continue; stub client will have handled memory calls
        print("⚠️ Hindsight Key not active yet. Standing up simulated offline memory blocks!", str(e))