_base_ = ['../_base_/models/resnet18.py','../_base_/datasets/imagenet_bs32.py','../_base_/default_runtime.py'] 

data = dict(
    # sample_per_gpu = 16,
    workers_per_gpu = 1,
    train = dict(
        data_prefix = 'data/flower_dataset/train',
        ann_file = 'data/flower_dataset/train.txt',
        classes =  'data/flower_dataset/classes.txt'
    ),
    val = dict(
        data_prefix = 'data/flower_dataset/val',
        ann_file = 'data/flower_dataset/val.txt',
        classes = 'data/flower_dataset/classes.txt'
    ),
)

model = dict(head=dict(num_classes=5,topk = (1, )))

optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

lr_config = dict(
policy='step',
step=[1])

runner = dict(type='EpochBasedRunner', max_epochs=100)