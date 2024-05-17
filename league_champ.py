from ultralytics import YOLO

model = YOLO('/Users/tongge/Desktop/hua/League_champ_detect/league_champ.pt')

result = model(source = "/Users/tongge/Desktop/hua/League_champ_detect/league_v.mp4",show = True, conf =0.4, save=True)
