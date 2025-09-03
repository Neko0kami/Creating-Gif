<h1 align="center">🎞️ Python GIF Maker</h1>

<p align="center">
  A simple Python script to automatically generate GIFs from a folder of images.
</p>

<p align="center">
  <img src="output.gif" alt="GIF Preview" width="400"/>
</p>

<h2>✨ Features</h2>
<ul>
  <li>Loads all images from a folder</li>
  <li>Converts them to a consistent <b>RGBA</b> format</li>
  <li>Resizes all images to the same dimensions</li>
  <li>Exports as a smooth looping GIF</li>
  <li>Adjustable <b>frame duration</b> (slow down or speed up the animation)</li>
</ul>

<h2>🖼️ Example</h2>
<pre>
📂 GifMaker/
 ├── Cat.jpg  
 ├── Cat2.jpg  
 ├── Cat3.png.jpg  
 ├── Cat4.png.jpg  
 └── create_gif.py  
</pre>

Output:
<pre>
output.gif
</pre>

<h2>⚡ Installation</h2>
<pre>
pip install imageio pillow numpy
</pre>

<h2>🚀 Usage</h2>
<p>Put your images in the same folder as <code>create_gif.py</code>, then run:</p>

<pre>
python create_gif.py
</pre>

<h3>Example Script</h3>

<pre><code class="language-python">
import imageio.v2 as iio
import os
import numpy as np
from PIL import Image


# images location
folder = r"D:\Programming\Python\Py\Meh\GifMaker"

# Get all files (ignore the script itself)
files = [f for f in os.listdir(folder) if f != "create_gif.py"]
files.sort()

img = []
target_size = None  # will be set to the first valid image

for f in files:
    path = os.path.join(folder, f)
    try:
        im = Image.open(path).convert("RGBA")  # ensure RGBA
        if target_size is None:
            target_size = im.size  # (width, height)
            print(f"Target size set from {f}: {target_size}")
        else:
            im = im.resize(target_size, Image.Resampling.LANCZOS)

        arr = np.array(im, dtype=np.uint8)  #force uint8 array
        img.append(arr)
        print(f"✅ Added {f}, resized to {arr.shape}, dtype={arr.dtype}")

    except Exception as e:
        print(f"❌ Skipped {f}: {e}")

# Save as GIF
if img:
    output = os.path.join(folder, "output.gif")
    iio.mimsave(output, img, duration=5.0, loop=0)  # ✅ use mimsave for multiple images
    print(f"🎉 GIF saved as {output}")
else:
    print("No valid images found to make a GIF.")
</code></pre>

<h2>⚙️ Options</h2>
<ul>
  <li><code>duration=5.0</code> → how long each frame is shown (in seconds)</li>
  <li><code>loop=0</code> → loop forever (set to a number for limited repeats)</li>
</ul>

<h2>📌 Next Steps</h2>
<ul>
  <li>Add <b>per-frame durations</b> (some images stay longer than others)</li>
  <li>CLI support (choose input/output folder from terminal)</li>
  <li>Resize images to a <b>custom fixed size</b> instead of matching the first</li>
</ul>

<h2>📝 License</h2>
<p>This project is open-source under the MIT License.</p>
