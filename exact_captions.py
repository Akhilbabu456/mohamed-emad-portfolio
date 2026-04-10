import codecs
import re

html_path = r'c:\Users\akhil\Downloads\html\html\gallery.html'

with codecs.open(html_path, 'r', 'utf-8') as f:
    content = f.read()

exact_captions = [
    "High-Performance Automotive", # 0: gallery-1
    "Track Racing Coverage",       # 1: gallery-2
    "Fashion & Lifestyle",         # 2: gallery-3
    "Exotic Cars & Details",       # 3: gallery-4
    "Editorial Portraits",         # 4: gallery-5
    "Desert Landscapes",           # 5: gallery-6
    "Desert Wildlife Details",     # 6: gallery-7
    "Automotive Details",          # 7: inner-gallery-1
    "Luxury Automotive",           # 8: inner-gallery-2
    "Lifestyle Portraits",         # 9: inner-gallery-3
    "Motorsports Photography",     # 10: inner-gallery-4
    "Nature & Wildlife",           # 11: inner-gallery-5
    "Studio Portraits",            # 12: inner-gallery-6
    "Creative Direction & BTS",    # 13: inner-gallery-7
    "Fashion Editorials",          # 14: inner-gallery-8
    "Wildlife Cinematography",     # 15: inner-gallery-9
    "Fashion Portfolio",           # 16: inner-gallery-10
    "Sports & Fitness Coverage",   # 17: inner-gallery-11
    "Desert Safari Experiences",   # 18: inner-gallery-12
    "Event Decor & Food",          # 19: inner-gallery-13
    "Event Setup & Styling",       # 20: inner-gallery-14
    "Sunset Cityscapes",           # 21: inner-gallery-15
    "Desert Portraits",            # 22: inner-gallery-16
    "Cultural & Travel Portraits", # 23: inner-gallery-17
    "Luxury Real Estate",          # 24: inner-gallery-18
    "Interior Photography",        # 25: inner-gallery-19
    "Real Estate Interiors",       # 26: inner-gallery-20
    "Architectural Details",       # 27: inner-gallery-21
    "Real Estate Walkthrough",     # 28: inner-gallery-22
    "Culinary & Food Showcase",    # 29: inner-gallery-23
    "Camel Photography",           # 30: service-1
    "Kids & Wildlife Portraits",   # 31: service-2
    "Corporate Interiors",         # 32: service-3
    "Destination Weddings",        # 33: service-4
    "Romantic Silhouettes",        # 34: slider-1
    "Couples & Engagements",       # 35: slider-2
    "Cultural Storytelling"        # 36: slider-3
]

idx = 0
def replacer(match):
    global idx
    cap = exact_captions[idx] if idx < len(exact_captions) else "Professional Photography"
    idx += 1
    return f"<h3>{cap}</h3>"

# We only replace h3 tags inside the gallery item blocks
def gallery_replacer(match):
    gallery_block = match.group(0)
    return re.sub(r'<h3>.*?</h3>', replacer, gallery_block)

new_content = re.sub(r'<div class="gallery-content">.*?</div>', gallery_replacer, content, flags=re.DOTALL)

with codecs.open(html_path, 'w', 'utf-8') as f:
    f.write(new_content)

print(f"Updated {idx} exact captions based on visual inspection mapping!")
