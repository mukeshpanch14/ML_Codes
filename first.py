with open('image.jpg','r') as rf:
    with open('image_cp.jpg', 'w') as wf:
        for line in rf:
            wf.write(line)
