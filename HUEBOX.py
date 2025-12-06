# HUEBOX.py — Premium CLI Color Palette Extractor

import os
import sys
import time
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

# -------------------------------------------------
# Branding
# -------------------------------------------------
def print_logo():
    """Logo premium HUEBOX en mode gradient."""
    RESET = "\033[0m"
    L1 = "\033[38;2;255;180;90m▛▘█▖"
    L2 = "\033[38;2;255;130;60m█▞▚█"
    L3 = "\033[38;2;210;80;40m▙▚▞▟"
    print(f"\n   {L1}\n   {L2}\n   {L3}{RESET}\n")
    print("      \033[1mH U E B O X\033[0m — Premium Palette Extractor\n")


# -------------------------------------------------
# Animations
# -------------------------------------------------
def loading(text="Chargement", duration=2):
    """Animation minimaliste premium."""
    frames = ["∙∙∙", "●∙∙", "●●∙", "●●●"]
    for i in range(duration * 4):
        f = frames[i % len(frames)]
        sys.stdout.write(f"\r{text} {f}")
        sys.stdout.flush()
        time.sleep(0.25)
    print("\n")


# -------------------------------------------------
# Input Image
# -------------------------------------------------
def get_image_path():
    """Demande à l'utilisateur le chemin de l'image."""
    path = input("\n📁  Entrez le chemin de votre image : ").strip()

    while not os.path.isfile(path):
        print("❌  Fichier introuvable, réessayez.")
        path = input("📁  Entrez le chemin de votre image : ").strip()

    return path


# -------------------------------------------------
# Palette extraction
# -------------------------------------------------
def extract_palette(image_path, num_colors=5):
    """Extraction des couleurs dominantes."""
    img = Image.open(image_path)
    img = img.resize((200, 200))
    data = np.array(img).reshape((-1, 3))

    kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init="auto")
    kmeans.fit(data)
    return kmeans.cluster_centers_.astype(int)


# -------------------------------------------------
# Display colors in terminal
# -------------------------------------------------
def rgb_square(r, g, b):
    """Carré de couleur."""
    return f"\033[48;2;{r};{g};{b}m   \033[0m"

def show_palette(colors):
    print("\n🎨  Palette dominante détectée :\n")
    for (r, g, b) in colors:
        hex_code = f"#{r:02X}{g:02X}{b:02X}"
        print(f"  {rgb_square(r, g, b)}  {hex_code}")
    print()


# -------------------------------------------------
# Main
# -------------------------------------------------
def main():
    print_logo()
    loading("Initialisation")
    path = get_image_path()
    loading("Analyse de l'image")
    colors = extract_palette(path)
    show_palette(colors)
    print("✅  Analyse terminée ! Merci d'utiliser HUEBOX.\n")


if __name__ == "__main__":
    main()
