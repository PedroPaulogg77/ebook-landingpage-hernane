from PIL import Image
import os

def remove_white_bg(source, target):
    if not os.path.exists(source):
        print(f"File {source} not found.")
        return
    
    img = Image.open(source).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # If pixel is very close to white, make it transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(target, "WEBP", quality=85)
    print(f"Successfully removed white background from {source} -> {target}")

remove_white_bg('freepik_br_bff64527-be7b-4266-a57c-e9128dfb9d3b.png', 'mockup.webp')
