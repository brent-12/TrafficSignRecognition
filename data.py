
import torchvision.transforms as tfrms

# data adjustments for training
# Resiszing all of the images to 32x32

data_tfrms = tfrms.Compose([
        tfrms.Resize((32,32)),
        tfrms.ToTensor(),
        tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),
])

data_brightness = tfrms.Compose([
    tfrms.Resize((32,32)),
    tfrms.ColorJitter(brightness=-5),
    tfrms.ColorJitter(brightness=5),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),
])

data_saturation = tfrms.Compose([
    tfrms.Resize((32,32)),
    tfrms.ColorJitter(saturation=-5),
    tfrms.ColorJitter(saturation=5),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),

])

data_contrast = tfrms.Compose([
    tfrms.Resize((32,32)),
    tfrms.ColorJitter(contrast=-5),
    tfrms.ColorJitter(contrast=5),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),

])

data_hue = tfrms.Compose([
    tfrms.Resize((32,32)),
    tfrms.ColorJitter(hue=0.4),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),

])

data_rotation = tfrms.Compose([
    tfrms.Resize((32,32)),
    tfrms.RandomRotation(15),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),
])

data_flips = tfrms.Compose([
    tfrms.Resize((32,32)),
    tfrms.RandomHorizontalFlip(1),
    tfrms.RandomVerticalFlip(1),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),
])

data_hflip = tfrms.Compose([
    tfrms.Resize((32,32)),
    tfrms.RandomHorizontalFlip(1),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),
])

data_vflip = tfrms.Compose([
    tfrms.Resize((32,32)),
    tfrms.RandomVerticalFlip(1),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),
])

data_shear = tfrms.Compose([
    tfrms.Resize((32,32)),
    tfrms.RandomAffine(degrees = 15, shear=2),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),
])

data_translate = tfrms.Compose([
    tfrms.Resize((32,32)),
    tfrms.RandomAffine(degrees=15, translate=(0.1,0.1)),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),
])

data_crop = tfrms.Compose([
    tfrms.Resize((36,36)),
    tfrms.CenterCrop(32),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),
])

data_grayscale = tfrms.Compose([
    tfrms.Resize((32,32)),
    tfrms.Grayscale(num_output_channels=3),
    tfrms.ToTensor(),
    tfrms.Normalize((0.3337, 0.3064, 0.3171), ( 0.2672, 0.2564, 0.2629)),
])
