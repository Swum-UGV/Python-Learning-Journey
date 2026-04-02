from moviepy import ImageClip,AudioFileClip
image_name='parrot.jpg'
audio_name='song.mp3'
duration=240
print('Please wait,I am generating your video')
clip=ImageClip(image_name,duration=duration)
audio=AudioFileClip(audio_name).with_duration(duration)
video=clip.with_audio(audio)
video.write_videofile('my parrot video.mp4',fps=24)
print('Welcome from your video')