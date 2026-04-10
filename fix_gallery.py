import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add filter if not there
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
parts = html.split('<div class="col-md-6 single-item')
new_html = parts[0]
for part in parts[1:]:
    # Ensure we don't duplicate class if already there
    first_close = part.find('>')
    classes = part[:first_close]
    content = part[first_close:]
    
    first_tag_search = re.search(r'<(img|video)\b', content)
    if first_tag_search:
        tag = first_tag_search.group(1)
        if tag == 'img':
            if 'image' not in classes:
                new_html += '<div class="col-md-6 single-item image' + classes + content
            else:
                new_html += '<div class="col-md-6 single-item' + classes + content
        else:
            if 'video' not in classes:
                new_html += '<div class="col-md-6 single-item video' + classes + content
            else:
                new_html += '<div class="col-md-6 single-item' + classes + content
    else:
        new_html += '<div class="col-md-6 single-item' + classes + content

html = new_html

# 3. Add 30-35 items if not there
new_items = ""
for i in range(30, 36):
    new_items += f"""
          <div class="col-md-6 single-item video">
            <div class="gallery-wrap">
              <video
                src="img/inner-gallery-{i}.mp4"
                class="autoplay-on-scroll gallery-video"
                muted
                loop
                playsinline
                style="width: 100%; height: auto"
                onloadedmetadata="$('.gallery-items').isotope('layout');"
              ></video>
              <div class="gallery-content">
                <h3>
                  Cinematic Content
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

parts = html.split('</section><!-- Gallery -->')
if len(parts) > 1 and 'inner-gallery-30.mp4' not in parts[0][-1000:]: 
    # insert before the closing div and section tags
    # Usually it's:
    #                 </div>
    #             </div>
    #         </section><!-- Gallery -->
    last_block = parts[0]
    pos = last_block.rfind('</div>\n            </div>\n')
    if pos != -1:
        new_last_block = last_block[:pos] + new_items + last_block[pos:]
        html = new_last_block + '</section><!-- Gallery -->' + parts[1]

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated gallery.html")
