import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add filter
filter_html = """
        <ul class="gallery-filter text-center mb-50">
            <li class="active" data-filter="*">All</li>
            <li data-filter=".image">Images</li>
            <li data-filter=".video">Videos</li>
        </ul>
        <div class="row gallery-items">"""

if '<ul class="gallery-filter' not in html:
    html = html.replace('<div class="row gallery-items">', filter_html)

# 2. Add classes to existing items
# We'll use regex to find `<div class="col-md-6 single-item">` that contain `img` or `video`
# We can do this by splitting on `<div class="col-md-6 single-item">`
parts = html.split('<div class="col-md-6 single-item">')
new_html = parts[0]
for part in parts[1:]:
    # To determine if this item has image or video, check the contents before the next item or end
    # Actually part contains the inner content until the next split or end of file
    first_tag_search = re.search(r'<(img|video)\b', part)
    if first_tag_search:
        tag = first_tag_search.group(1)
        if tag == 'img':
            new_html += '<div class="col-md-6 single-item image">' + part
        else:
            new_html += '<div class="col-md-6 single-item video">' + part
    else:
        new_html += '<div class="col-md-6 single-item">' + part

html = new_html

# 3. Add 30-35 items
new_items = ""
for i in range(30, 36):
    new_items += f"""
          <div class="col-md-6 single-item video">
            <div class="gallery-wrap">
              <video
                src="img/inner-gallery-{i}.mp4"
                class="autoplay-on-scroll"
                muted
                loop
                playsinline
                style="width: 100%; height: auto"
              ></video>
              <div class="gallery-content">
                <h3>
                  Cinematic <br />
                  video experience
                </h3>
                <a
                  href="img/inner-gallery-{i}.mp4"
                  data-vbtype="iframe"
                  class="gallery-link img-popup"
                  data-gall="galleryimg"
                  >Explore <i class="ti-arrow-right"></i
                ></a>
              </div>
            </div>
          </div>
"""

# Find where to insert: right before `<!-- Pic-9 -->`'s parent div's closing div, which is after it.
# Original end of index.html gallery:
#           </div>
#           <!-- Pic-9 -->
#         </div>
#       </div>
#     </section>
if 'img/inner-gallery-30.mp4' not in html:
    html = html.replace('<!-- Pic-9 -->', '<!-- Pic-9 -->' + new_items)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")

