
from PIL import Image
import numpy as np

TEST_REGIONS = [
    ("Ammonia", 50, 20, 30, 30),
    ("Nitrite", 50, 70, 30, 30),
    ("Nitrate", 50, 120, 30, 30)
]

AMMONIA_LEVELS = {
    "Safe": [(255, 255, 180)],
    "Danger": [(200, 255, 120)],
    "Extreme": [(0, 100, 80)],
}

NITRITE_LEVELS = {
    "Safe": [(135, 206, 250)],
    "Extreme": [(128, 0, 128)],
}

NITRATE_LEVELS = {
    "Safe": [(255, 255, 200)],
    "Caution": [(255, 200, 100)],
    "Danger": [(128, 0, 64)],
}

LEVEL_MAP = {
    "Ammonia": AMMONIA_LEVELS,
    "Nitrite": NITRITE_LEVELS,
    "Nitrate": NITRATE_LEVELS
}

SAFE_RANGES = {
    "Ammonia":   {"min": (200, 200, 20), "max": (255, 255, 60)},
    "Nitrite":   {"min": (200, 200, 20), "max": (255, 255, 60)},
    "Nitrate":   {"min": (200, 200, 20), "max": (255, 255, 60)},
}

def get_average_color(image, x, y, w, h):
    region = image.crop((x, y, x + w, y + h))
    np_region = np.array(region)
    return np_region.mean(axis=(0, 1))


def match_color_to_level(color, level_dict):
    def distance(c1, c2):
        return np.sqrt(np.sum((np.array(c1) - np.array(c2)) ** 2))

    min_dist = float('inf')
    best_match = None

    for label, ref_colors in level_dict.items():
        for ref in ref_colors:
            dist = distance(color, ref)
            if dist < min_dist:
                min_dist = dist
                best_match = label
    return best_match

def is_safe(compound, avg_color):
    min_vals = SAFE_RANGES[compound]["min"]
    max_vals = SAFE_RANGES[compound]["max"]
    return all(min_vals[i] <= avg_color[i] <= max_vals[i] for i in range(3))

def analyze_strip_image(image):
    results = {}
    for name, x, y, w, h in TEST_REGIONS:
        avg_color = get_average_color(image, x, y, w, h)
        avg_color = tuple(int(c) for c in avg_color)

        status = "Safe" if is_safe(name, avg_color) else "Danger"

        results[name] = {
            "label": "Manual detection",
            "avg_color": avg_color,
            "status": status
        }
    return results


