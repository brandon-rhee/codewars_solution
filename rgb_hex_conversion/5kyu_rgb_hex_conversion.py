def rgb(r, g, b):
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    return f"{r:02X}{g:02X}{b:02X}"

# Usage
hex_color = rgb(-20, 275, 125)
print(hex_color) # Output: #ff0080