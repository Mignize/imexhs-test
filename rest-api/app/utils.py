from typing import List

def validate_and_normalize(data: List[str]) -> tuple[float, float, int]:
    flat = [int(n) for row in data for n in row.strip().split()]
    if not flat:
        raise ValueError("No valid numbers found.")
    max_val = max(flat)
    avg_before = sum(flat) / len(flat)
    normalized = [x / max_val for x in flat]
    avg_after = sum(normalized) / len(normalized)
    return avg_before, avg_after, len(flat)
