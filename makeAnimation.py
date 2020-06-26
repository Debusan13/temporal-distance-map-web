import os
import imageio

c = 0
dir_path = os.path.dirname(os.path.realpath(__file__))
with imageio.get_writer(dir_path+'/static/warpAnimation.mp4', mode='I') as writer:
    for filename in sorted(os.listdir(dir_path+"/static/Frames/"),key=lambda f: int(''.join(filter(str.isdigit, f)) or -1)):
        if filename.endswith(".png"):
            image = imageio.imread(dir_path+"/static/Frames/"+filename)
            writer.append_data(image)
            print(f"{(c/6)*100}%")
            c+=1;
