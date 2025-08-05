def save_as_image(fig, filename, dpi=150):
    fig.savefig(filename, dpi=dpi)
    print(f"Saved image as {filename}")

def save_as_gif(frames, filename, duration=100):
    import imageio
    imageio.mimsave(filename, frames, duration=duration)
    print(f"Saved GIF as {filename}")

def save_as_mp4(frames, filename, fps=30):
    import cv2
    height, width, layers = frames[0].shape
    video = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    
    for frame in frames:
        video.write(frame)
    
    video.release()
    print(f"Saved MP4 as {filename}")