from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model(source=["data/V1.jpg", "data/V2.jpg", "data/dog.jpg"], conf=0.4, save=True, save_txt=True) 