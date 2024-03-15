import cv2
import os
classes = ['traffic_light', 'zebra_crossing', 'bus', 'double_yellow_line', 'nothing']
data = {}

for category in classes:
    count = 0
    os.makedirs(os.path.join('dataset_aug', category), exist_ok=True)
    for file_name in os.listdir(os.path.join('square', category)):
        img_path = os.path.join('square', category, file_name)
        print(img_path)
        img = cv2.imread(img_path)
        res = cv2.resize(img, dsize=(64, 64), interpolation=cv2.INTER_CUBIC)
        count += 1
        cv2.imwrite(os.path.join('dataset_aug', category, str(count).zfill(3)+'.jpg'), res)
        count += 1
        new_img = cv2.flip(res, 1)
        cv2.imwrite(os.path.join('dataset_aug', category, str(count).zfill(3)+'.jpg'), new_img)
        count += 1
        new_img = cv2.flip(res, 0)
        cv2.imwrite(os.path.join('dataset_aug', category, str(count).zfill(3)+'.jpg'), new_img)
        new_img = cv2.flip(res, -1)
        count += 1
        cv2.imwrite(os.path.join('dataset_aug', category, str(count).zfill(3)+'.jpg'), new_img)
