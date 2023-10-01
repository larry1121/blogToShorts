from moviepy.editor import *
from moviepy.audio.io.AudioFileClip import AudioFileClip
# pip install --trusted-host pypi.python.org moviepy
from glob import glob


def editVideo():

    avatar_clip = VideoFileClip('temp2/avatar170.mp4')

    print(avatar_clip.duration) 

    #####################################################################
    # 백그라운드 음악을 원본영상과 같은 길이로 만들어 줌
    #####################################################################
    audio_clip = AudioFileClip('temp2/bgm.mp3')

    audio_clip = audio_clip.volumex(0.2) 
    audio_clip = audio_clip.set_duration(avatar_clip.duration)

    print(audio_clip.duration)

    #####################################################################
    # 백그라운드 이미지 갯수와 영상길이 확인 후 이미지를 묶은 영상으로 만듦
    #####################################################################
    paper_imgs = sorted(glob('temp2/*.png')) 
    print(len(paper_imgs))

    
    clips = [ImageClip(m).set_duration(avatar_clip.duration / len(paper_imgs)) for m in paper_imgs] 
    print(clips)

    paper_clip = concatenate_videoclips(clips, method="compose")

    paper_clip = paper_clip.set_duration(avatar_clip.duration) 

    print(paper_clip.duration)


    #################################
    # 아바타를 오른쪽 아래에 위치, 크기를 작게 만듦
    #################################
    w, h = paper_clip.size

    print('Resize avatar clip and move position to bottom right')
    avatar_clip = avatar_clip.set_pos(('right', 'bottom')) 


    print('Text animation')

    t = u'소설책 1분 요약'.encode('utf-8')
    txt = TextClip(t, color='white', font='휴먼명조', fontsize=30)
    txt_col = txt.on_color(
        size=(txt.w + 10, txt.h + 10),
        color=(0, 0, 0),
        pos=(6, 'center'),
        col_opacity=0.6)
    txt_mov = txt_col.set_pos(('center', h / 10))
    txt_mov = txt_mov.set_duration(avatar_clip.duration)


    print('Composite and write the video file')
    result = CompositeVideoClip([paper_clip, avatar_clip, txt_mov]) 

    result.write_videofile(
        'result.mp4',
        codec='libx264',
        audio_codec='aac',
        threads=32)


editVideo()