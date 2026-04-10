import re
import os

html_dir = r"c:\Users\rgrak\html"
files = [f for f in os.listdir(html_dir) if f.endswith('.html') and f != 'services.html']

header_pattern = r'<h1><a href="index\.html"><img src="[\./]*img/logo\.png" alt="logo"></a></h1>'
header_repl = r'<h1><a href="index.html">Emad</a></h1>'

footer_pattern = r'<footer class="footer-section.*?</footer><!-- /\.footer-section -->'
footer_repl = """<footer class="footer-section padding text-center">
			<div class="container">
			<div class="text-center">
                    <div class="brand"><a href="index.html">Emad</a></div>
                    <ul class="social-link">
                        <!-- <li><a href="https://www.linkedin.com/" target="_blank"><i class="fa fa-linkedin"></i></a></li> -->
                        <li><a href="https://www.behance.net/mohammedemad3" target="_blank"><i class="fa fa-behance"></i></a></li>
                        <li><a href="https://www.instagram.com/mandu.158?igsh=NGcyamVudnBycWV2" target="_blank"><i class="fa fa-instagram"></i></a></li>
                    </ul>
                </div>
				<p>&copy; @2025 Mohamed Emad</p>
			</div>
		</footer><!-- /.footer-section -->"""

for f in files:
    path = os.path.join(html_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = re.sub(header_pattern, header_repl, content)
    content = re.sub(footer_pattern, footer_repl, content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updates applied to all files except services.html")
