# Read about.html to grab the footer starting from `    <div class="instagram-import">`
with open('about.html', 'r', encoding='utf-8') as f:
    about = f.read()

instagram_import_idx = about.find('<div class="instagram-import">')
footer_part = about[instagram_import_idx:]

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Add `    </section>\n    <!-- Gallery -->\n\n    ` + footer_part
if '</section>' not in index_html[-50:]:
    index_html += "    </section>\n    <!-- Gallery -->\n\n    " + footer_part

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
