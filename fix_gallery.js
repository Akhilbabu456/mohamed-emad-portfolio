const fs = require('fs');

let html = fs.readFileSync('gallery.html', 'utf-8');

// Add tabs
if (!html.includes('<ul class="gallery-filter')) {
    const filterHTML = `
                <ul class="gallery-filter text-center mb-50">
                    <li class="active" data-filter="*">All</li>
                    <li data-filter=".image">Images</li>
                    <li data-filter=".video">Videos</li>
                </ul>
`;
    // We replaced the row gallery items definition
    html = html.replace('<div class="row gallery-items">', filterHTML + '                <div class="row gallery-items">');
}

// Add .image to items with img
html = html.replace(/<div class="col-md-6 single-item">(\s*<div class="gallery-wrap">\s*<img)/g, '<div class="col-md-6 single-item image">$1');
// if there are multiple classes already:
html = html.replace(/<div class="col-md-6 single-item ">(\s*<div class="gallery-wrap">\s*<img)/g, '<div class="col-md-6 single-item image">$1');

// Add .video to items with video
html = html.replace(/<div class="col-md-6 single-item">(\s*<div class="gallery-wrap">\s*<video)/g, '<div class="col-md-6 single-item video">$1');

// Add videos 30-35
let newItems = '';
for (let i = 30; i <= 35; i++) {
    newItems += `
                    <div class="col-md-6 single-item video">
                        <div class="gallery-wrap">
                            <video src="img/inner-gallery-${i}.mp4" class="autoplay-on-scroll gallery-video" muted loop playsinline style="width: 100%; height: auto;" onloadedmetadata="$('.gallery-items').isotope('layout');"></video>
                            <div class="gallery-content">
                                <h3>Cinematic Experience</h3>
                                <a href="https://www.instagram.com/mandu.158?igsh=NGcyamVudnBycWV2" target="_blank" class="gallery-link">Explore <i class="ti-arrow-right"></i></a>
                            </div>
                        </div>
                    </div>`;
}

// ensure we don't add multiple times
if (!html.includes('img/inner-gallery-30.mp4')) {
    html = html.replace(/<\/div>\s*<\/div>\s*<\/section><!-- Gallery -->/, newItems + '\n                </div>\n            </div>\n        </section><!-- Gallery -->');
}

fs.writeFileSync('gallery.html', html, 'utf-8');
console.log('Update complete');
