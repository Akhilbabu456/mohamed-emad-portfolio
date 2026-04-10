import re

new_item = """
          <div class="col-md-6 single-item video">
            <div class="gallery-wrap">
              <video
                src="img/inner-gallery-13.MOV"
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
                  href="img/inner-gallery-13.MOV"
                  data-vbtype="iframe"
                  class="gallery-link img-popup"
                  data-gall="galleryimg"
                  >Explore <i class="ti-arrow-right"></i
                ></a>
              </div>
            </div>
          </div>
"""

def add_to_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the closing tags for the gallery
    # The gallery items container closes with </div> right before the </div> for container
    # Let's search for "inner-gallery-35.mp4" block and insert after it.
    if "inner-gallery-13.MOV" not in html:
        # Find where inner-gallery-35 block ends
        search = 'inner-gallery-35.mp4'
        idx = html.find(search)
        if idx != -1:
            # find the end of this div block
            # we look for the next "</div>\n          </div>\n        </div>" roughly
            # a safer way:
            after_35 = html[idx:]
            # index.html has:
            #           </div>
            #         </div>
            #       </div>
            #       ...
            # Find the line with </section>
            section_idx = html.find('</section>', idx)
            if section_idx != -1:
                # Go backwards to find the closing div of row gallery-items
                # Usually it's `        </div>\n      </div>\n    </section>`
                insert_idx = html.rfind('</div>\n      </div>\n', idx, section_idx)
                if insert_idx != -1:
                    new_html = html[:insert_idx] + new_item + html[insert_idx:]
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(new_html)
                    print(f"Added to {filename}")

add_to_file('index.html')
add_to_file('gallery.html')
