import ffmpeg

def test_ffmpeg_input():
    try:
        stream = ffmpeg.input('input_video.mp4')
        print("ffmpeg.input() works correctly.")
    except AttributeError as e:
        print(f"AttributeError: {e}")

if __name__ == "__main__":
    test_ffmpeg_input() 