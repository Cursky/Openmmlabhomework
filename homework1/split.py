import os
import random

def create_dataset(root_dir, classes_filename, train_filename, val_filename, train_ratio=0.8):
    # Step 1: Get all image file paths
    image_paths = []
    for class_dir in os.listdir(root_dir):
        class_path = os.path.join(root_dir, class_dir)
        if os.path.isdir(class_path):
            for image_filename in os.listdir(class_path):
                image_paths.append(os.path.join(class_dir, image_filename))
                
    # Step 2: Split into train and val sets
    random.shuffle(image_paths)
    num_train = int(len(image_paths) * train_ratio)
    train_set = image_paths[:num_train]
    val_set = image_paths[num_train:]

    # Step 3: Write classes file
    class_dirs = [os.path.basename(os.path.dirname(path)) for path in image_paths]
    unique_classes = set(class_dirs)
    with open(classes_filename, 'w') as f:
        for i, class_name in enumerate(sorted(list(unique_classes))):
            f.write(f"{class_name}\n")
            
    # Step 4: Write train and val files
    with open(train_filename, 'w') as f:
        for image_path in train_set:
            class_name = os.path.basename(os.path.dirname(image_path))
            class_id = sorted(list(unique_classes)).index(class_name)
            f.write(f"{image_path} {class_id}\n")
    with open(val_filename, 'w') as f:
        for image_path in val_set:
            class_name = os.path.basename(os.path.dirname(image_path))
            class_id = sorted(list(unique_classes)).index(class_name)
            f.write(f"{image_path} {class_id}\n")

# Example usage
create_dataset("./flower_dataset", "classes.txt", "train.txt", "val.txt")
