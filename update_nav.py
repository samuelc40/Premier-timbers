import os
import glob
import shutil

# Create gallery.html by copying project.html
if not os.path.exists("gallery.html"):
    shutil.copy("project.html", "gallery.html")
    
    # Update gallery header from "Product" to "Gallery"
    with open("gallery.html", 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(
        '<h1 class="display-3 text-white mb-3 animated slideInDown">Product</h1>',
        '<h1 class="display-3 text-white mb-3 animated slideInDown">Gallery</h1>'
    )
    content = content.replace(
        '<li class="breadcrumb-item text-white active" aria-current="page">Product</li>',
        '<li class="breadcrumb-item text-white active" aria-current="page">Gallery</li>'
    )
    content = content.replace(
        '<title>Woody - Carpenter Website Template</title>',
        '<title>Gallery - Premier Timber Company</title>'
    )
    with open("gallery.html", 'w', encoding='utf-8') as f:
        f.write(content)

# Update all navbars
html_files = glob.glob("*.html")
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if 'href="gallery.html"' in content:
        continue # skip if already added
        
    # We want to add gallery link directly after project link
    # Normal link
    target1 = '<a href="project.html" class="nav-item nav-link">Product</a>'
    repl1 = '<a href="project.html" class="nav-item nav-link">Product</a>\n                <a href="gallery.html" class="nav-item nav-link">Gallery</a>'
    
    # Active link
    target2 = '<a href="project.html" class="nav-item nav-link active">Product</a>'
    repl2 = '<a href="project.html" class="nav-item nav-link active">Product</a>\n                <a href="gallery.html" class="nav-item nav-link">Gallery</a>'
    
    content = content.replace(target1, repl1)
    content = content.replace(target2, repl2)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
