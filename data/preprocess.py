from utils import list_files, crop_to_smallest_edge, makedirs
import cv2

obj_name = "traffic_light"

makedirs(obj_name)
folder_path = "./" + obj_name + "_screenshot/"
all_files = list_files(folder_path)
for file in all_files:
    crop_to_smallest_edge(folder_path + file, "./" + obj_name +"/" + file)
    img = cv2.imread("./" + obj_name + "/" + file)
    res = cv2.resize(img, dsize=(64, 64), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("./" + obj_name +"_train/" + file, res)