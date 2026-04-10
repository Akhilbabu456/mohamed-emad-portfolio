import os
import re

html_path = r'c:\Users\akhil\Downloads\html\html\gallery.html'
img_dir = r'c:\Users\akhil\Downloads\html\html\img'

files = os.listdir(img_dir)
valid_prefixes = ('inner-gallery', 'gallery-', 'service-', 'slider-')
selected_files = []
for f in files:
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4')):
        if any(f.startswith(pf) for pf in valid_prefixes):
            selected_files.append(f)

def sort_key(s):
    match = re.match(r'([a-zA-Z-]+)(\d+)', s)
    if match:
        return (match.group(1), int(match.group(2)))
    return (s, 0)

selected_files.sort(key=sort_key)

html_pieces = []
for i, f in enumerate(selected_files):
    ext = os.path.splitext(f)[1].lower()
    is_video = ext in ['.mp4']
    
    media_tag = f'<img src="img/{f}" alt="pic">'
    explore_type = ''
    
    if is_video:
        media_tag = f'<video src="img/{f}" class="autoplay-on-scroll gallery-video" muted loop playsinline style="width: 100%; height: auto;" onloadedmetadata="$(\'.gallery-items\').isotope(\'layout\');"></video>'
        explore_type = 'data-vbtype="iframe"'

    block = f"""                    <div class="col-md-6 single-item">
                        <div class="gallery-wrap">
                            {media_tag}
                            <div class="gallery-content">
                                <h3>Professional <br> Photography</h3>
                                <a href="img/{f}" class="gallery-link img-popup" {explore_type} data-gall="galleryimg">Explore <i class="ti-arrow-right"></i></a>
                            </div>
                        </div>
                    </div>"""
    html_pieces.append(block)

html_str = '\n'.join(html_pieces)

with open(html_path, 'r', encoding='utf-8') as fl:
    content = fl.read()

start_tag = '<div class="row gallery-items">'
end_tag = '                </div>\n            </div>\n        </section><!-- Gallery -->'

st = content.find(start_tag) + len(start_tag)
en = content.find(end_tag)

if st > len(start_tag) and en != -1:
    new_content = content[:st] + '\n' + html_str + '\n' + content[en:]
    with open(html_path, 'w', encoding='utf-8') as fl:
        fl.write(new_content)
    print(f'Added {len(selected_files)} items to gallery.html')
else:
    print('Failed to find tags in gallery.html')
