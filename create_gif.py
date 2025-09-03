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
