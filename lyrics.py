import time

def print_lirik():
    lirik = [
        ("It's stuck with you forever...", 1.0, 0.07),
        ("so promise you won't let it go", 1.0, 0.07),
        ("I'll trust the universe ", 1.0, 0.05),("will always bring me to you", 0.7, 0.05),
        ("", 0.3, 0.0),
        ("", 3.0, 0.0), 
        ("I'll imagine we fell in love", 0.7, 0.07),
        ("I'll nap under moonlight skies with you", 1.2, 0.05),
        ("I think I'll picture us, you with the waves", 1.0, 0.07),
        ("The ocean's colors on your face", 1.7, 0.07),
        ("I'll leave my heart with your air", 1.3, 0.07),
        ("So let me fly with you", 1.4, 0.07),
        ("Will you be forever with me?", 1.0, 0.09),
    ]

    for teks, delay_baris, delay_huruf in lirik:
        for c in teks:
            print(c, end='', flush=True)
            time.sleep(delay_huruf)
        print()
        time.sleep(delay_baris)

def print_big_heart():
    heart = [
        "       *****       *****       ",
        "     *********   *********     ",
        "   ************* *************   ",
        "  *****************************  ",
        " *******************************",
        " *******************************",
        "  *****************************  ",
        "   ***************************   ",
        "    *************************    ",
        "      *********************      ",
        "        *****************        ",
        "          *************          ",
        "            *********            ",
        "              *****              ",
        "               ***               ",
        "                *                "
    ]

    print("\n💖 Love for you 💖\n")
    for line in heart:
        print(line)
        time.sleep(0.7)  # แสดงผลแบบมีแอนิเมชัน

if __name__ == "__main__":
    print_lirik()
    print_big_heart()