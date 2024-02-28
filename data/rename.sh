#!/bin/bash
obj_name="traffic_light"

a=1
for i in ./${obj_name}/*.png; do
    new=$(printf "%03d.png" "$a")  # 04 pad to length of 4
    mv -i -- "$i" "./${obj_name}/$new"
    let a=a+1
done

mv -r "./${obj_name}" "./${obj_name}_screenshot"