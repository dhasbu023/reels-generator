import os
import pandas as pd

from moviepy import (
    TextClip,
    ImageClip,
    CompositeVideoClip
)

# ======================
# CONFIG
# ======================

WIDTH = 1080
HEIGHT = 1920

DURATION = 8

FONT_PATH = "fonts/BebasNeue-Regular.ttf"

BACKGROUND = "backgrounds/white.jpg"

OUTPUT_FOLDER = "output"

# ======================
# LOAD EXCEL
# ======================

df = pd.read_excel("quotes.xlsx")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ======================
# LOOP SEMUA QUOTES
# ======================

for index, row in df.iterrows():

    text = str(row["text"])

    print(f"MEMBUAT VIDEO {index+1}")

    # Background
    bg = (
        ImageClip(BACKGROUND)
        .with_duration(DURATION)
        .resized((WIDTH, HEIGHT))
    )

    # Text
    txt = (
        TextClip(
            text=text,
            font_size=70,
            color="black",
            font=FONT_PATH,
            method="caption",
            size=(900, None),
            text_align="center"
        )
        .with_duration(DURATION)
        .with_position("center")
    )

    # Combine
    final = CompositeVideoClip([bg, txt])

    # Export
    output_path = f"{OUTPUT_FOLDER}/reels_{index+1}.mp4"

    final.write_videofile(
        output_path,
        fps=30,
        codec="libx264"
    )

print("SELESAI")