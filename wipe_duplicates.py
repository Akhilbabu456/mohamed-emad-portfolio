import re

def clean_file(filename, boundary_str):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Split the file right before the first injected 30
    # Actually, let's find the closing tags of the last *original* item.
    # In index.html, it's `<!-- Pic-9 -->`.
    # In gallery.html, it's `img/slider-3.jpg` block ending.
    
    parts = html.split(boundary_str)
    if len(parts) < 2:
        return
    
    # We want everything before the boundary + the boundary itself.
    base_html = parts[0] + boundary_str
    
    # Generate the 30-35 items once
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

    # We append the exact closing sequence:
    # </div>
    # </div>
    # </section>
    
    # The remainder of the html after the gallery:
    # `</section><!-- Gallery -->` onwards.
    # Let's split original html by `</section><!-- Gallery -->`
    after_gallery = html[html.find('</section><!-- Gallery -->'):]
    
    final_html = base_html + new_items + """
        </div>
      </div>
    """ + after_gallery

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_html)

# For index.html, the boundary is `<!-- Pic-9 -->`
clean_file('index.html', '<!-- Pic-9 -->')

# For gallery.html, the boundary is the end of the slider-3 block
boundary_gallery = """<img src="img/slider-3.jpg" alt="pic">
                            <div class="gallery-content">
                                <h3>Cultural Storytelling</h3>
                                <a href="img/slider-3.jpg" class="gallery-link img-popup"  data-gall="galleryimg">Explore <i class="ti-arrow-right"></i></a>
                            </div>
                        </div>
                    </div>"""
clean_file('gallery.html', boundary_gallery)

print("Duplicates cleaned!")

