from pydub import AudioSegment


def generate_audio_files(main_file):

    t_old=210000
    t_new=210000
    #hindi_train
    #46-84 ravish-discussion
    #85-129 ravish-indi
    #130-148 hindi-gst
    #1-45 podcast

    #english train
    #1-45 borderline_male
    #46-92 borderline_female
    #93-113 deep
    #114-134 social


    for i in range(91,94):
        t_old=t_new
        t_new=t_old+(10*1000)
        new_audio=AudioSegment.from_wav('sound_samples/'+main_file+".wav")
        new_audio=new_audio[t_old:t_new]
        new_audio.export('sound_samples/'+"test"+ str(i)+'.wav',format='wav')

generate_audio_files("english_social")

    #test
    #6-25 ravish-disscussion
    #26-37 podcast
    #38-49 ravish-indi
    #50-60 gst_hindi
    #61-65 borderline male
    #66-82 borderline female
    #83-90 deep
    #91-93 social